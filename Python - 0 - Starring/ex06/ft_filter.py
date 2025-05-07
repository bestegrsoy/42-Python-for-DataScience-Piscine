def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable for which
    function returns true.
    If function = None, Python's filter() function returns elements
    according to the truth value.
    Otherwise, if the given function(x) is true, that element is returned.
    """
    try:
        if not hasattr(iterable, '__iter__'):
            raise TypeError("iterable must be an iterable object")
        if function is not None and not callable(function):
            raise TypeError("function must be callable or None")

        if function is None:
            return (x for x in iterable if x)
        return (x for x in iterable if function(x))

    except Exception as e:
        raise e
