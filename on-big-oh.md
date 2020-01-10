# A brief digression on Big O

## Definitions

"Big-O" is commonly used in computer science and mathematics, to indicate approximate growth of something as the input grows. The notation is (essentially) `O(f(n))`, for some function `f`. The actual function wrapper is often elided and you'll see things like `O(n)`, `O(n log n)` and occasionally `O(1)`.

When we say "an algorithm is in O(f(n))", we usually refer to run-time. And what we mean is, in a strict sense, "the run-time of the algorithm is g(n), such that there is an m that for all i > m, g(i) <= k * (f(i)". This is frequently (and borderline incorrectly) started as "g(n) is essentially k * f(n) + C".

We typically restrict the fuctions under consideration to "non-decreasing functions" (that is, for any n, m; n < m, we have f(n) <= f(m)). We normally consider n to be in the positive integers and we consider f(n) >= 0 (if we didn't, O(n log n) would not be valid, as any log 1 is 0, and we do want O(n log n) to be valid)

## Equivalence of various O

With this in mind, we can start looking at what "is O(f(n))" actually means. We can easily see that it denotes function growth. We can also see that a specific O is a set (of functions, some of which may be constant). We can also see that, as an example, O(1) is a subset of O(log n) which in turn is a subset of O(n). We typically refer to the set of functions as "the complexity class" and by convention say that an algorithm's complexity falls in the smallest such complexity class. We normally also choose the representative function to be the "simplest" function that generates the class.

We can now see if we can determine if two complexity classes are equivalent.  The best way to do that is to reason about the functions that fall within a complexity class. For this, we will consider two functions, f and g, and their corresponding complexity classes, O(f) and O(g).

They're clearly equivalent if for any function that is in O(f), it is also in O(g) and vice versa. So, O(f) and O(g) ar ethe same, if O(f) is a subset of O(g) and O(g) is a subset of O(f).

# But what about constant complexity classes?

Let us look at a few constant complexity classes. Let's pick O(0), O(1) and O(2).

First, let's see what the set of O(1) looks like. It is all functions f(n), where we can find a constant k, such that we can find a point beyond which f(n) <= k * 1 (or, just "k", since we can simplify).

Then, let's look at O(2). If we can find a k for O(2), we can clearly find a k for O(1), just pick 2k.

But what about O(0)? It is also clearly constant. But, only functions f(n) = 0 will work, as 0 * k is always 0.

We can thus relax in the knowledge that O(0) is strictly smaller than O(1) and we can't actually find any algorithm that runs in O(0), as all algorithms will take at least one instant of time.
