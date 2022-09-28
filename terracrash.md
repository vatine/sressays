# Terraform considered occasionally unhelpful

Or "how Terraform almost destroyed some infrastructure as code".
Or "correct is better than fast".

## Background

Once upon a time, there was a company that ran multiple Kubernetes clusters in-house, on top of CoreOS and ignition.

To alleviate possible "you can make things persist on disk" concerns, the machines would always boot "from scratch", using Ignition to always come up in a deterministic state.

However, building these files was somewhere between a chore and a pain. So, their building was automated using Terraform, an almost perfect fit for the purpose. Only thing is, part of what is needed for kubernetes head and worker nodes are some shared secrets. And these need to match. And, furthermore, for new clusters they need to be created.

Not to worry, there are Terraform plug-ins for key management, so this should not be a problem, right?

## This thing is kind of slow...

So, each cluster was defined in a terraform file of its own, leaning heavily on a set of "library" modules, defining the shape of an abstract cluster. All of these were kept in version control.

But, it is not at all ideal to keep the secrets and state files in version control, so what happened was that we built a set of bastion hosts where we could run terraform, then locked these bastion hosts down tight.

And to make sure that terraform would run, when needed, there was a Janekins pipeline that simply checked out the repository at the most recent, then ran terraform against each cluster defined in there. Because terraforming an unchanged file is idempotent.

It's also not at all the fastest thing in the world. Not a problem when you have one cluster, but as time grew, so did the number of clusters. And once we were getting to the "more than 5" stage, people went "well, this is kind of slow, and terraform is safe, so let's just make this run in parallel".

Which happened. And all was fine.

## Why is that cluster shrinking?"

One downside, as it were, is that terraforming the clusters (which, of course, ran on raw hardware, not virtualised) is that any terraforming effect requires a reboot to pick up. Which, for adding a cluster, or adding a node to a cluster, was not a problem.

But, the downside of that is that there could be multiple terrraformings without any visible effect.

And, one day, as a worker node rebooted, it did not come back. Head-scratching ensued. This was not at all expected. Some digging ensued.

Turns out, the freshly-rebooted worker node had a completely different set of certificates than the head nodes. Or, indeed, any other worker node in the cluster.

Well, that was clearly unexpected...

## Digging deeper

At this point, we're cleary in some sort of "oh shit" incident territory. An unknown number of nodes in potentially multiple clusters may be un-rebootable. Well, unable to be rebooted and rejoin the cluster as intended.

So, some digging in the ignition files happened. And it turns out that roughly half of the machines in three (IIRC, it was more than "one" and less than "all") clusters had certificates that woudl not allow them to rejoin.

With no obvious reason as to why, it was time to dig deeper. And the first obvious place was the terraform logs. Which, sadly, did not really make anything clearer.

Then, it was time to look at the system logs. And that showed something interesting. Quite a lot of OOM-killer messages, with timing that seemed to suspuciously co-incide with Jenkins runs.

Since the "identify incorrectly terraformed nodes" was sufficently automated (a shell script outside of version control, good enough for this purpose), the Jenkins pipeline was triggered, in the hope that it would either fix the certificate issue, or at least give some further clarity.

After the run, the nodes were checked again. And, would you believe it, there were still about the same number of broken nodes, but the clusters and specific nodes were different. And there were more OOM-killer messages in the system logs.

## But I prefer correct...

On a hunch, the Jenkins pipeline was flipped back from parallel to serial and activated. After that, the clusters were checked again, and all nodes were as expected. And the OOM-killer logs were no longer in evidence.

Turns out that "external plugin gets OOM-killed" (which shoulf typically result in a non-zero exit code) is (or at least was) interpreted as "there is no data and everything is fine", instead of "there may or may not be data, something went wrong". So, if the OOM-killer managed to kill the "check if there is a certificate" process, as a node was being terraformed, terraform would generate a new certificate. Thankfully, this did not overwrite any of the persisted certificates.

So, in the end, given sufficent parallelism, terraform was not quite as idempotent as you may have wanted.
