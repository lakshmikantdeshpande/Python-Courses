def make_delimit_line(list_to_join, delim):
    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError('make_delimit_line(): arg 1 must be a list or a tuple')
    return formatted_line

# line = make_delimit_line(100, ',')
