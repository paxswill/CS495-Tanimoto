
def jaccard_index(a, b, sets=False):
    """Compute the Jaccard index of two sets.

    If sets is False, a and b are converted to sets before operating on
    them. If sets is True, both and and b are not converted to sets and
    are assumed to meet the definition of a set. sets may be a tuple of
    boolean values, representing a and b respectively.
    """
    real_a = a
    real_b = b
    try:
        if sets[0]:
            real_a = frozenset(a)
        if sets[1]:
            real_b = frozenset(b)
    except TypeError:
        if not sets:
            real_a = frozenset(a)
            real_b = frozenset(b)
    return len(real_a.intersection(real_b)) / len(real_a.union(real_b))

def jaccard_distance(a, b, sets=False):
    """Compute the Jaccard distance of two sets

    This is simply 1 minus the Jaccard index. See the documentation for
    the jaccard_index function for an explanation of the arguments.
    """
    return 1 - jaccard_index(a, b, sets)

