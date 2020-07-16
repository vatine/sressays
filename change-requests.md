# What makes for a good pull request / change list / patch?

For the remainder of this document, I'll use the short-term "PR" for
"change submitted to someone else for review, possibly approval and
eventual merging". Nonetheless, the concept transcend specific version
control tools.

## "What" and "why"

A good change should show what has changed, and why the change(s) have
been made. In many cases, the "what" is implicit in the diff from old
to new. But the "why" can frequently be opaque. And having that "why"
is quite handy, if/when you go back to look at changes down the line.

The "why" could be as simple as "fixes bug #n" or "adds feature
requested in <link>", but having it gives some context for the review,
as well as helping future viewers of the PR.

## Difference in concerns for "code" and "config"

For code, frequently all that's needed is a description along the
lines of "adds feature X" or "fixes bug Y" (or "adds tests for
...."). More information is usually good, but just having a reference
to the document where the feature is described, the bug is described,
or just a simple "refactor X/Y/Z" is usually enough to motivate why a
certain change was submitted, approved, and merged.

But once you start keeping configuration under version control
l(and, yes, you really want to do this), a description along the lines
of "set frobnitz to true" is, frankly, just restating what's already
in the diff and doesn't tell us _why_ the frobnitz should be true.

Instead, something like "when the frobnitz is disabled, the smurples
groink in the night and as no smurples should groink, we enable the
frobnitz" would tell us both what, and why. However, just a link to a
bug/ticket/issue where the investigation happens (and is sufficiently
detailed to give context to a future reader) is really enough.

## Make it easy to approve

### As a requester

As someone requesting a change, make it easy for the reviewer(s) to
approve. This means that the code/config should (as far as possible)
be correct. Any code should be tested. It should follow the style
guide and the style of surrounding code. It should motivate why it
exists and in general it should be obvious why this request should be
merged and that it is safe to do so.

### As a project owner

You should have automatic style checks. You should run all relevant
tests. In short, make it easy for the requester to make it easy for
reviewer(s) to approve.
