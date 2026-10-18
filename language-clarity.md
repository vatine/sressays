# On language clarity

Let us for a moment consider language clarity. This could be
"configuration language", "programming language", or (possibly) "data
description language". Doesn't matter overmuch, for the general
discussion. This could also be "syntactic clarity" or "semantic clarity".

Language clarity constrains your design space, sometimes in unexpected
ways. And sometimes, language clarity is not as anhered-to as it could
be.

## Clarity in Puppet

Case in point, there's multiple ways of introducing dependencies
between resources in Puppet. You can declare in resource A that it
needs to be done before resource B, or that it notifies resource
B. You can also, in resource B say taht it requires resource A, or
should be notified if resource A is modified. Nice and declarative.

You can also use "dependency arrows", inherently not bad, but the
glyph sequences chosen are sifficiently similar that a quick scan may
mistake one for the other. And this is bad. The sequences? "->" and
"~>" (without the double-quotes).

One example of "not as clear as it could be".

## Clarity in boolean short-cuts

Another came up a while ago, in a discussion. Why is it that C/C++
does not have a short-circuiting "boolean implication"? Well, it
doesn't because no one specified it. And there arguably some really
nice use-cases for it. Let's assume that "boolean implication" is
spelled =>, it would be Real Nice to say something like:

```
  assert( (a != NULL) => (a->prev->next == a) )
```

This is an assert that for any double-linked list, the "next" of the
previous node is the node in question, but only if a is actually a
node (and, as it turns out, not the first node, but, you know...).

However, I would argue that in this specific case, I would prefer to
not have boolean implication as an operator, as while it is fairly
clear in *this* case, what happens if we say something like:

```
  a => b => c => d
```

Assume that our boolean implication evaluates as "true" when the left
side is false, or when both left and right are true (that is, there's
a short-circuit when the left side is false, as we do not need to know
the value on the right side).

Let's try that again, with some actual code:

```
  (a != NULL) => (a->prev != NULL) => (a->prev->next == a)
```

Under what circumstances is a dereferenced? Without sitting down and
drawing truth tables? I mean, the expression looks fairly benign,
right?

The way I would expect a => b => c to be evaluated is as ((a => b) => c), although there is a case to be made for (a => (b => c)) as well. In the former case, there is no "safe" short-cutting for our example. If our `a` is false, then `(a => b)` is true, which in turn requires the evaluation of `c` (as an implication is trivially true when the left hand is true).

Of course, in the second case, short-circuiting would be safe, as the truth value of `(b => c)` does not matter, so with `a' false, then we could have short-circuiting. But, at least I do not read implications that way, but I cannot speak for you.
