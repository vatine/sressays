# Why "helm" is not my most favourite way of managing kubernetes.

## Analyzing the problem space

Helm is a tool for managing Kubernetes manifests. It is a tool that falls in some sort of general "configuration managemet" space.

Among the things that you want from a tool in this space is taht it makes managing your configuration simpler than having to hand-edit every time a small portuion changes.

In the Kubernetes world, Helm seems to be among the most popular tools in this space.

## Strengths and failings of Helm

In helm's defense it is a pretty simple tool. Unfortunately, its simplicity makes it more complictaed and cumbersome to use. The main points of encumbrance are its tmplating system and its dependency system.

It also interacts badly with clusters that have certain RBAC restrictions in place.

Likewise, many existing helm bundles ("helm charts") have problems when RBAC has been applied to clusters. That, however, is more a failing with those bundles than helm as such.

## Templating

If yoyu are going down a configuration templating route, you have basically two options. The first option is to go with pure text templating (that is, you are glueing strings together) and the second is some sort of structural templating.

### Textual

Textual templating has the virtue of simplicity. The program does not need to interpret anythnig outside the template language. There's no real complicated reasoning about scopes or structure. It is just strings.

The downside with pure texual templating is that it will not allow you to squirrel away complexity inherent in your confguration into templates. As an example, if you set a CPU limit for a container containing compiled Go code, you (probably) want to make sure that the GOMAXPROCS environment variable is set to match that. Similarly if you set a memory limit for a container whose primary code runs on top of the JVM, you probably want to pass one or more of the JVM's memory/controlling flags.

With helm templates being plain text, this turns out to be hard to accomplish in a convenient way, leading to various workarounds that basically bil down to "manage the resource limits and the ancillary configuration separately", allowing for potentially broken combinations to appear. It also allows for ineffienct combinations to appear, but that is less of a problem.

Another possible issue is that YAML has semantically significant indentation and it is somewhat easy causing the Go template engine to insert (or fail to insert) indentation, causing valid results with inintended semantic value(s).

Furthermore, it is possible to accidentally introduce variable substitutions tht have line breaks, causing utter mayhem in the YAML structure.

### Structural

In contrast, a structural templating language has knowledge of the domain in which it is doing template expansion. For Kubernetes, this would essentially mean that it is aware of "ContainerSpec", "PodSpec" and similar, and an awareness of their inherent structure, meaning that you can then pull information from other parts of the template to help with the expansion.

In a structural templating system (see (Flabbergast)[https://www.flabbergast.org/] for one example), it is in principle possible to write a "go container" template that has the requisite knowledge to pull CPU limit into a correctly set GOMAXPROCS environment variable. 

## Namespace issues

Helm is designed on the premise that there is a 1:1 correspondence between namespaces and applications. It is harder than it necessarily needs to be to cope with multiple applications in a single namespace, or applications that may be better spread across multiple namespaces.

## The "package" manager

On the surface, Helm's ability to reference other helm charts looks like a nice idea. But, with helm charts having at best some conventions for how to set various parameters, you still need to check and double-check the external charts.

### Helm "values.yaml" files

The "values.yaml" file in the chart's main directory contains basically default values for all manifests in the chart. For good or bad, this does not have a fixed "shape" (good, in that you can tune the shape to fit the chart you're making, bad in that it basically forms the chart's API contract). This means that no matter what you intend, you still need to go and check what the other chart is doing in terms of settings.

If you follow the general recommended style, you can easily end up in a position where teh chart you're writing needs an API surface that is unsuited to what you want it to be.
