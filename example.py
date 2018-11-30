#!/usr/bin/env python3

"""
    Basic Python generator examples.
    The yield statement halts the function and saves it state.
    The function continues from its halted state on successive calls.
"""

def all_even(max):
    n = 0
    while n < max:
        yield n
        n += 2

def fib_generator(nth):
    n = 0
    p = 1
    q = 1
    while n < nth:
        yield p
        old_q = q
        q = p + q
        p = old_q
        n += 1

if __name__ == "__main__":
    print("All even")
    out = ""
    for n in all_even(10):
        out += str(n) + ", "
    print(out[0:len(out)-2])
    print("Fib generator")
    out = ""
    for n in fib_generator(12):
        out += str(n) + ", "
    print(out[0:len(out)-2])