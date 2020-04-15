# Liveness and readiness probes, and other "standard" endpoints

## Why liveness probes?

In a distributed "cluster architecture" system like, say, Kubernetes, you normally say "hey, I want N instances/replicas of this thing" and the job of the cluster scheduler is to ensure that you do have N instances (or, as close to N as possible),

Part of this can be done simply by looking at "the program crashed", but not all terminal failure scenarios are exhibited by "program exited" (successfully or not). So, in order to better be able to ask  "hey, are you alive?", it's useful to have a "liveness probe". This can (and usually is) a web endpoint where a 2xx response means "yep, alive", any error (4xx, 5xx) or a failure to respond at all means "nope, consider me dead".

It's also useful to have a small amount of tolerance for "temporarily odd behaviour", it is possible for a program to not be able to answer the liveness probe in a timely fashion if it is under extreme load, so it is (in Kubernetes at least) possible to specify both how frequent the probes are, and how many consecutive failures are requried to consider the instance dead (as in "not alive").

Common names for this endpoint is `/healthz`, `/livez`, `/live`, `/-/live` and more.

## Why readiness probes?

Once you have N instances/replicas, and you're load-balancing traffic across them, it is useful to ask "hey, are you ready to serve traffic". This is, again, frequently done over a web endpoint, and can frequently be configured for "how many OK respones before added to backend set" and "how many failures to be taken out of the backend set".

This allows the system as a whole to (mostly) send traffic to backends taht are ready to respond to them.

## Why both liveness and readiness probes?

At the absolute minimum, it would be possible to have just liveness probes. However, having both liveness probes and readiness probes allows for a few things that just lveness probes won't provide.

The main reason is that for liveness, the typical action is "stop instance, start instance again" and this is frequently a costly operation, with several seconds being required to pull images, spin them up, acquiring a minimal set of "state required for serving" and so on.

So, in a temporary overload situation, it is a lot better for the system as a whole that a single overloaded instance can keep all its "running image" and "internal state", while shedding some load.

It is also useful in a graceful shutdown scenario, where you can start signalling "not ready" in advance of actually disappearing

## But what about /metrics?

Imagine we have an application, running as multiple separate instances. How can we say that it's working well? One possibility is "log introspection", but that's relatively computationally heavy (less so with structured logging), and tends to (but doesn;t always) have a bit of a lag.

Another possibility is to instrument your application for metrics exporting, using any of multiple monitoring farmeworks. Here, I will just discuss Prometheus.

The way Prometheus works is that (somehow, for now let's go with "magic") it knows that an instance exists, and knows that it should be scraped every N seconds. So, it goes off and does that. And for that to work, it needs to know two things, "what's the IP/hostname and port?" and "what local URL path should I use?" and for good or bad, it seems that `/metrics` has become that default.

You should, by the way, both emit sensible logging as well as instrument your application(s) for metrics exporting, it will making running them reliably much easier, and may even allow you to decrease the interval between production pushes, shorten your canary (or blue/green) testing, while increasing your confidence in what you have running.
