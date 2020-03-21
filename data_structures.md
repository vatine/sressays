# Data structures and their time complexity for some common operations

This is a rewrite of a thing I wrote back in 2008-or-so.

What this ocument will do is present a couple of common data structures and, for each data structure, look at the time complexity for a couple of common operations. Wehn this document talks about complexity, it will use the "big O" notation, which basically presents a representative function that is within a constant multiplier of dominating the actual time complexity.

For this, we will look at three different operations, "add", "change", and "remove". We will also look at it in three differet positions, "at the start/head", "internally", and "at the end/tail". We will also look at "retrieve the Nth element", for a total of 10 operations.

In some cases, we will denote a time complexity as "amortized", this is a bit of a cop-out, as this is an average over mutiple operations.


|            | head | internal | tail |
+-----+---+------+----+
|      add|        |            |          |
+-----+---+------+----+
|change|        |            |          |
+-----+---+------+----+
|remove|        |            |          |
+-----+---+------+----+
Retrieve Nth: 

## Single-linked list

|            | head | internal | tail |
+-----+---+------+----+
|      add|O(1) | O(n)     | O(n), O(1)  |
+-----+---+------+----+
|change| O(1)|O(n), O(1)|O(n), O(1) |
+-----+---+------+----+
|remove|O(1) | O(n)     | O(n)  |
+-----+---+------+----+
Retrieve Nth: O(n) 

A single-linked list is your typical "keeps one element of data, and a reference to the rest of the list". One subtle refinement is a list header that also keeps a reference to the last element of the list.

For the purpose of changing data, the O(n) is typically what you have if you need to find the list element, but if you already have a reference, it is O(1).

Also note that if you have a reference to the tail, adding another element at the tail is O(1), but removing an element still requires iterating through the entire list.

Single-linked lists are only ordered in so far as "if you iterate through the list without adding or removing data, you are guaranteed it will always be in the same order), but there's no inherent sorting of elements.

## Double-linked list

|            | head | internal | tail |
+-----+---+------+----+
|      add|O(1) | O(n), O(1) | O(n), O(1)  |
+-----+---+------+----+
|change| O(1)|O(n), O(1)|O(n), O(1) |
+-----+---+------+----+
|remove|O(1) | O(n), O(1) | O(n), O(1)  |
+-----+---+------+----+
Retrieve Nth: O(n) 

A double-linked list is similar to a single-linked list, but keeps a reference both to the next, as well as the previous, element. This means that adding an element afer (or before) or removing an element taht you already have a reference to is inherently an O(1) operation.

Similar to the single-linked case, it's possible to have a  list header that references both the head and the tail of the inked list.

Double-linked lists are only ordered in so far as "if you iterate through the list without adding or removing data, you are guaranteed it will always be in the same order), but there's no inherent sorting of elements.

## Vector

|            | head | internal | tail | 
+-----+---+------+----+
|      add|O(n) |O(n)       | AO(1)  |
+-----+---+------+----+
|change| O(1)| O(1)      | O(1)  |
+-----+---+------+----+
|remove|O(n) |O(n)       | O(1)  |
+-----+---+------+----+
Retrieve Nth: O(1)

A vector is a linear segment of memory, allowing O(1) random access to its elements, but in creasing the size MAY incur a copy of all existing elements. If you double the potential size of the vector (and keep a small "vector head" tracking the current capacity), the per-element access time increases by one memory reference, but with careful attention to how you grow the vector (approxiately: "double the capacity every time you need to expand"), the amortised cost of adding one element is O(1), even if you will get ocasionally get O(n) behaviour.

Vectors are only ordered in so far as "if you iterate over the vector, you will only obsereve re-orderings that have been explicitly done".

## "Simple" string

|            | head | internal | tail |
+-----+---+------+----+
|      add|O(n) | O(n)     | O(n), AO(1)|
+-----+---+------+----+
|change| O(1) | O(1)     | O(1)  |
+-----+---+------+----+
|remove| O(n)| O(n)      | O(1)  |
+-----+---+------+----+
Retrieve Nth: O(1)

A "simple" string is not relying on any encoding (so ASCII/ISO-8859-x), and carefully has one character per cell. It is basically a vector of characters and has the same access properties as a vector.

If you need to encode the full range of unicode, this means using UTF-32 and encoding any combining characters using surrogate characters.

If you implement the string with a string header tracking both capacity and start, removing a character at head drops from O(n) (copy the string) to O(1) (bump the start).

Strings have the same ordering guarantees as vectors.

## "Complex" string

|            | head | internal | tail |
+-----+---+------+----+
|      add|O(n) | O(n)     | O(n), AO(1)|
+-----+---+------+----+
|change| O(n) | O(n)     | O(n), AO(1)|
+-----+---+------+----+
|remove| O(n)| O(n)      | O(1)  |
+-----+---+------+----+
Retrieve Nth: O(n)

A "complex" string is a string that has a variable-length encoding, like UTF-8. Exact time complexity of removal of the last character depends on careful implementation. If you can encode where the cahracter starts (or the encoding is sufficiently well-behaved), removal of the last character can be done in constant time (longest possible UTF-8 encoding is, what, 5 bytes?), but changing the last character may require extending the vector in which the complex string has been stored.

With a suitable string header, removing a character at head can be dropped from O(n) to O(1), by advancing the string start past the first character.

Retrieving the Nth character of the string now requires decoding all the characters before it. It is much more efficient to process a complex string by a scheme that iterates over the characters one by one than it is to iterate over a position in the string and indexing it. The former is an O(n) operation, the latter is an O(n ** 2) operation.
