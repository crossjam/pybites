def is_armstrong(n: int) -> bool:
    digits = [int(c) for c in str(n)]
    return sum([d ** len(digits) for d in digits]) == n
