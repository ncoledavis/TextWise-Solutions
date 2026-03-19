def reverse_divide_and_conquer(s: str) -> str:
    if s is None:
        return None
    n = len(s)
    if n <= 1:
        return s
    mid = n // 2
    left = reverse_divide_and_conquer(s[:mid])
    right = reverse_divide_and_conquer(s[mid:])
    return right + left