# Various thoughts on automation

This short essay will present some thoughts I have on the "automation
space" and may hopefully serve to give you ideas to improve your
automation situation.

## Why automate?

Why do we automate things? I see a few possible reasons, and usually
more than one of these apply at the same time.

### Repeatability

We want processes to be repeatable. This means that if I do something
today, and Alice does something next week (and, of course, if teh
process hasnöt changed in-between), the end result should be the same
(or, at least, essentially the same).

### Removing toil

We want machines to do our drudge work. It is literally no fun
spending a day clicking buttons in a semi-instrutable web
interface. Or, possibly slightly better, mindlessly copy-pasting code
from a web page or a Word document onto a command line.

Not only does it hinder understanding of what you're doing, it is
tedious and boring, so you are likely to miss a step, or
over/under-paste and thus compromising the repeatability of the process.

### Making things faster

Once you have something that is machine-executable, there's scope for
making the process faster. Or, at least, less prone to be needing done
again.

## Is there a useful middle-ground between "no touch" and "just a check-list"?

A younger me would have said "no". Why settle for something that is
only partially automated? And it's hard to bridge the gaps between the
various automated pieces, so having only a few things completely
devoid of human interaction is no better than having no things devoid
of human interaction.

But, an older, and hopefully wiser, me says taht yes, there's a
tremendous amount of win from having computer support for your
process, even if all steps start out requiring the human touch.

By wrapping your manual process/checklist in machine-supported
execution, you can iteratively chip away at each piece of the
automation problem, changing one (or more, if you happen to be lucky)
step from "a human does it, promted by a machine" to "the machine does
it".

Doing it that way also allows the proces sto grind to a halt, only to
be resumed at a later point. With only the steps that have yet to
complete successfully being done.

## Sequential or DAG, an aside

There are essentially two ways for approaching "here are a bunch of
things taht need to be done". One is listing a bunch of steps, then
start at the first, then do the second, and so on.

This seems like it would be the preferrable approach. It is, after
all, quite easy to reason about.

But, it comes with a few drawbacks. One is that you don't really have
a clear idea of what steps are needed before a specific step can be
done. Or, indeed, if a step needs to have been completed before it is
even safe to try to accomplish a subsequent step.

This means that a purely sequential plan needs to stop at the very
first thing that fails. And then can only be restarted from there.

Whereas in a directed acyclic graph ("DAG"), where each step declares
what steps it explicitly needs to come after, you can continue to do
tasks, as long as all prerequisites of that task have completed
successfully. And by ensuring that your execution randioly picks one
of the "possibel next steps" (rather than deterinistically do the same
thing every time), you can tease out where you have dependencies.

## Making software based on this

With these criteria in mind, I set out to write a "bridging automation
tool". Since naming is oe of the hard problems in computer science, I
have simply called the software "runnable-plans".

### What type of actions do you need?

A plan is composed of zero or more actions. Although, a plan with zero
actions is not actually that interesting, other than as an edge case.

#### Ask the user to do something

The most crucial type of action is "ask the user to do something, then
ask if it went OK".

#### Do something automatically

Since we want the software to be a bridge between "nothing is
automated" and "everything is automated", we clearly need SOMWE way
for the plan to cause external code to be executed. For the purposes
of runnable-plans, an OK exit status means "completed successfully"
and a non-OK exit status means "this failed".

#### Set a variable

And, unfortunately, we also need some way of manipulating
variables. This is because no matter how much we wish we could ignore
state and just do the same thing again and again, when you're  trying
to automate things around computers, you frequently end up having
"almost" the same problem, with just a few  key things that differ.

We thus allow for this, by having an action type that allows some
amount of state-keeping.

### Resuming execution

Since "being able to resume a failed run" is an explicit goal,
runnable-plans allow for this by dumping a state file into a temporary
directory. This file identifies the plan it was started from, saves
the value of all variables, and the completion state ("completed",
"failed", or "pending") and has a special mode to resume the execution
from there.

On resuming execution, all completed actions will stay completed. But,
all failed and pending actions will be marekd as "pending".

### Graphing

It also turns out taht being able to display the DAG that is your
process is a pretty good way to spot either potetial wins, or
potential problems. So, runnable-plans also includes a mode for
displaying just such a graph.
