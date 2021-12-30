def positive_divide(numerator, denominator):
    try:
        res = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise

    if res < 0:
        raise ValueError()

    return res
