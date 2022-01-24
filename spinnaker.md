# Spinnaker considered harmful

## No enforced single source of truth

It is eminently easy to mess up a spinnaker installation by having
multiple halyard installations interacting with a single spinnaker. In
a non-distributed work environment, this may be less obvious ("just
log onto the halyard host").

However, having multiple halyards interacting with a single spinnaker
deployment quickly ends up in a weirdly skewed configuration. And
there's nothing inherent to halyard(spinnaker from stopping this (even
the presence of a per-halyard UUID would potentially help here).

## Not driven by declarative manifests

Halyard is configured in an incredibly stateful way. To the point that
it even has a "diff the state that is local to the state that is
presumed to be remote" (note, the remote state actually does not seem
to check the remote configuration, but insteasd checks if any state
mutation commands have been given).

## UI operations may reflect stale configuration

If you reconfigure Spinnaker, UI operations may reflect a previous
configuration state. This is probably because the UI sends "full" API
requests to various Spinnaker backends (that is, "start a build with
these build credentials", rather than have the builder knowing what
credentials it should use).

## The "hal" CLI command and the halyard daemon are not designed for distributed operation

With the existence of a state-keeping "halyard" daemon, and a separate
"hal" CLI command for interacting with the daemon and mutating
configuration state, one would assume that all file contents necessary
for affecting state changes (saya key file when adding a CI account)
would be passed as data.

From observation, what actually seems to be passed is a file
path. This means that the "halyard" daemon by necessity needs to run
on the same machine (or, at least with the same distributed file
system available in the same path) for successful state mutation.
