#!/usr/bin/env python3

def print_fibonacci(length):
    """Print the first `length` Fibonacci numbers as a Python list.

    Examples:
    - length=0 -> prints "[]\n"
    - length=1 -> prints "[0]\n"
    - length=2 -> prints "[0, 1]\n"
    """
    if length <= 0:
        print([])
        return

    seq = [0]
    if length == 1:
        print(seq)
        return

    seq.append(1)
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    print(seq)