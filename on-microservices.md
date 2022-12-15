# The case for, and aganst, microservices

## What is a micro-service?

A micro-service is a software component in a larger distributed
system. In an ideal world, it is responsible for a small, well-defined
part of the system as a whole. A system built using a micro-service
architecture (MSA) is composed of multiple micro.services, possibly calling
each otehr via some sort of RPC/API mechanism to get some of the data
you need.

## The case against micro-services

Going for a MSA for your system comes with a cost.

A monolith has inter-component calls going at "the speed of RAM",
whereas a call between two microservices are "at the speed of the
network". This may still be fast, but it is by necessity longer than
that of just a call between functions in the same binary.

It is harder to write the full system when using MSA than it is to do it as a monlith. Partly because you smiply have more build targets, partly because some of your tests can end up needing more than a single running thing (or, you end up with extensive mocking).

## The case for using micro-services

Micro-services allow for scaling different parts of your service differently. This means that a component whose resource consumptions are linear in the incoming request load can be scaled up slower than a component that is (say) O(n log n) in resoucre requirements. Or, indeed, one that is inherently O(n ** 2) (which, hopefully, does not partake in all possible API calls).

It makes it possible to replace just a single component ("microservice" with a new version.

If the "world-facing API surface" (from here on forwards, "the
front-end" or "FE") is made in-house, the microservice architecture
can be re-worked without any client-side changes. Depending on how
API(s) are exposed in a third-party FE, this may or may not work, we will touch on that in the next section.

## The case against third-party API managers

A common theme for third-party API managers is "let us have one REST path prefix be dedicated to a single set of backends". This is understandable, it seems obvious that the "service structure" should be exposed in the "external world" API surface. It also makes it somewhere between easy and trivial to forward the requests.

However, exposing your internal architecture makes it somewhere between difficult and impossible to change the internal architecture, to meet new demands, changes in usage and/or hamper optimisation possibilities.

Thus, any third-party API manager that makes it easy to expose your internal architecture and makes it hard(er) not to is going to introduce friction in your microservice journey.

## Conclusions

There are cases where "go microservice" is the right choice. There are cases where "go monolith" is the right choice.

Microservices coe with advantages. But, they also come with drawbacks. Don't pick a microservice architecture because it is "the new hot thing", pick it because its advantages align with your needs and its drawbacks are things you can cope with.