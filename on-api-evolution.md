# On API Evolution In Distributed Systems

## Introduction

In this essay, I will discuss, in general, how to appoach API changes
in distributed systems. We will assume some sort of distributed
system, the smallest of which is a relatively rich Web UI running in a
browser, communicating with a backend of some sort. On the larger end,
you have multiple interconnected services, forming a larger system.

Between these parts of the system, there's some set of standards for
how one requests information, work to be done, and similar, as well as
the response to these requests. For the rest of this essay, we'll just
shorten that to API.

In both of these cases, as the nature of what needs to be done, as
well as experience gained over time, will probably lead to changes in
the "API surface" of components and our main discourse is how to
accomplish this in a way that allows or a minimum of pain for users of
that API, be they other services, UI clients or integrations from
external parties.

## The Lock-Step method

The lock-step method is the conceptually simplest model. As we see
that a request (or response) needs new parameters, or no longer need a
parameter, or a parameter needs to change type , we simply make sure
that we chage it in places at once.

This is relatively easy to reason about, but also requires that we
cannot release any component with a changed API surface, without
ensuring that all parts of the system (and ideally all clients,
especially external clients) are updated at the same (or close to the
same) time.

In a very small distributed system, this is quite possible, but the
larger it is (and the more developers involved), the more difficult
this becomes.

## The Gradual Change method

The gradual change method requires more discipline and more system
introspection capabilities. But, it should allow for pieces to
improve, in isolation, with other pieces adopting over time.

The basic idea that any specific request or response never changes (or
only changes by adding optional parameters).

The ideal way to change is to simply add new requests, or
responses. If that is done blindly, over time, it will lead to a large
and messy codebase. To some extent, this can be "fixed" by
re-implementing older things in terms of the newer thing.

This is where the system introspection comes in. By exporting some
sort of observability signal on API requests, we can see when users of
an old ("deprecated") API request have disappeared (or shrunk to an
acceptably low ratio), we can remove the old request. In some sense,
this means that the "lock-step" method is "the gradual change" method,
just with the acceptable ratio of "old to all" > 1.

This does, of course, require more code, as well as more care, as
inevitable change is happening in the system. But, it does mean that
an improvement in a single part can be deployed essentially the moment
it has been implemented (and tested) instead of needing to wait for
the entire system to adapt.

The improvements will not be seen immediately, but by not being gated
on "everything must change at once", it should allow an increase in
the velocity of change.

## Conclusion

What method should you choose? It really depends. For a single-person
project, wher ethe same person writes every single component, and
there are no "external" API users, it's really whatever seems to make
sense.

The larger the distributed system is, the more friction will be
experienced when the lock-step method is used, requiring a painful
coordiation of releases of all components.
