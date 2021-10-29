def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """

    if number < base:
        return number
    else:
        return dec_to_base(number // base, base) * 10 + dec_to_base(number % base, base)
