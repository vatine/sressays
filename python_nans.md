# Python and NaN

Some (well, actually, most) of the time, I am OK with Python design decisions. But, there are a few I do not agree with.

One of them is the treatment of NaN in sets and dicts.

## Some float theory

In the floats used, there's a couple of special values called NaNs, or "not a number". And chief among their properties is that they never compare equal to anything.

This is a pretty important, but also pretty confusing, fact about them. It will also become important later.

## Some dict/set theory

Let's start with dictionaries. Let us further assume that these dictionaries are hash maps (which I think Python documentation explicitly state). Good? Cool.

A hash map has a certain number of slots. Let us call that S (for "size" or "slots"). To store something at a specific key K, we compute the hash of K, then (as our initial probe) check slot `hash(K) % S`.

### The slot is empty?

If we're trying to store something, we're golden. We can just put the key and the value to store and we're good to go.

If we're trying to retrieve something? Not so good, we now have to (somehow) signal "you tried to retrieve a value for key K, but there is no key K in the hash". In Python, this would be a key error exception.

### The slot is not empty?

Again, we're looking at the store case first. So, there's something already in the slot we wanted to go? OK, all stored key/value pairs have both the key and teh value stored. So, we check the key we're trying to store into, and the key in the slot. If they're the same, we're good to go! If not, there are several methods to deal with collisions, but basically, we look a bit more, until we find a slot where the keys test equal, or we find an empty slot.

In the retrieval case, we have a similar story. We foudn a slot? Cool, is it the right key? If so, e have the value, if not, we'll have to continue looking, until we find a key that compares equal, or we end up at an empty slot.

## OK, that's hashes. What about sets?

The simplest implementation of a set is a "keys only" hash. So we can basically think of them as hashes storing empty value.

## But, NaNs?

Notice how we, as we were going through that, kept saying "compares equal"? The very thing that two NaNs cannot do?

Yeah, this leads to some weird edge cases.

## Counting duplicates

NOTE: full code in the file `dupes.py` in this repo.

Let us assume we want to count unique elements in an array. There are, of course, several ways of doing this. The most obvious (for possibly obscure levels of "obvious") is to simply compare each element to each other element in the sequence. This is a straight-forward O(n ** 2) operation, nothing to shie away from.

The basic code looks something like:

```
def count_uniques(seq):
    l = len(seq)

    dupes = 0
    for ix1 in range(l):
        for ix2 in range(ix1 + 1, l):
            if seq[ix1] == seq[ix2]:
                dupes += 1

    return l - dupes
```

So, all good. We now have an easy way of counting duplicates, atht is (essentially) trivil to reason about. The only non-trivial thing in this code is the "use n(n-1)/2 checks" instead of the naive "use n*n" (mostly because this way, we never double-count a dupe, and we never ever compare an element with itself, so all in all, it actually leads to simpler code).

But, quadratic... Not actually a problem for small values of N, but if we were to, say, start having thousands or tens of thousands, dropping it from O(n ** 2) to a more comfortable O(n log n) or even O(n) would be much better.

So, let's look at that as well.

```
def count_uniques(seq):
    uniques = set()
    dupes = 0
    for e in seq:
        if e in uniques:
            dupes += 1
        uniques.add(e)

    return len(seq) - dupes
```

Here, we could probably just return `len(uniques)`, since that should be exactly the same as `len(seq) - dupes`, but we will leave it as-is to match the other function.

This should clearly return the same thing. But, due to a decision at some point in time to not actually do the right thing for NaNs in sets and as hash keys, they don't. Python will consider a specific NaN instance (floats are boxed...) to be "equal" when used as a key, even though they do not compare equal.

Which, on the whole, is a possibly-excusable, but still arguably incorrect design decision.

But, it does mean it's not always 100% safe to go for an algorithmic speed-up in Python, as the built-in data containers have some really rather non/obvious gotchas attached to them.
