def count_non_dupes_on2(seq):
    """Return the count of unique elements in the sequence. 
       Here, unique means that for any two elements e1, e2 in the sequencee, e1 != e2.
       This uses an inefficient, but "obviously correct" O(n ** 2) algorithm.
    """

    l = len(seq)

    dupes = 0
    for ix1 in range(l):
        for ix2 in range(ix1 + 1, l):
            if seq[ix1] == seq[ix2]:
                dupes += 1

    return l - dupes


def count_non_dupes_on(seq):
    """Return the count of unique elements in the sequence. 
       Here, unique means that for any two elements e1, e2 in the sequencee, e1 != e2.
       This uses a more efficient set-based methoid that should be somewhere
       between O(1) and O(n log n) (depending mostly on set membership lookup).
    """

    uniques = set()
    dupes = 0
    for e in seq:
        if e in uniques:
            dupes += 1
        uniques.add(e)

    return len(seq) - dupes


def compare_non_dupes(seq):
    slow = count_non_dupes_on2(seq)
    fast = count_non_dupes_on(seq)

    print(f"slow saw {slow} uniques\nfast saw {fast} uniques")

nan1 = float("NaN")
nan2 = float("NaN")

print("Just different floats")
compare_non_dupes([1.0, 2.0, 3.0, 4.0, 5.0])

print("\n\nJust floats")
compare_non_dupes([1.0, 2.0, 3.0, 4.0, 5.0, 1.0, 2.0, 3.0, 4.0, 5.0])

print("\n\nSingle NaN")
compare_non_dupes([nan1, 1.0, 2.0, 3.0, 4.0, 5.0])

print("\n\nTwo NaNs (1)")
compare_non_dupes([nan1, nan2, 1.0, 2.0, 3.0, 4.0, 5.0])

print("\n\nTwo NaNs (2)")
compare_non_dupes([nan1, nan1, 1.0, 2.0, 3.0, 4.0, 5.0])

print("\n\nJust NaNs")
compare_non_dupes([nan1, nan2, nan1, nan2, nan1, nan2])

