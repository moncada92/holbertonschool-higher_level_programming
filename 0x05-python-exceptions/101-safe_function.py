#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = None
    try:
        result = fct(*args)
    except BaseException as err:
        sys.stderr.write("Exception: {}\n".format(err))
    finally:
        return result
