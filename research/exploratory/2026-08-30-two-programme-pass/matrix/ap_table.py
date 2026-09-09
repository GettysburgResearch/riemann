"""Exact a_p table for 11a1 (y^2 + y = x^3 - x^2 - 10x - 20), good primes
p <= 100000, by exact point counting over F_p via quadratic-residue tables.

a_p = -sum_x chi(4x^3 - 4x^2 - 40x - 79)  (complete the square in y).
EXACT_RATIONAL integers; every value verified against |a_p| <= 2 sqrt(p).
Writes matrix/ap_table_11a1.json. rh_established = false.
"""
import json
import sys
import time

LIMIT = 100000
BAD = 11


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, n + 1) if s[i]]


def a_p(p):
    if p == 2:
        # direct count of y^2 + y = x^3 + x^2 + 1 over F_2  (mod-2 reduction)
        n = 0
        for x in range(2):
            for y in range(2):
                if (y * y + y - (x ** 3 - x ** 2 - 10 * x - 20)) % 2 == 0:
                    n += 1
        return 2 + 1 - (n + 1)
    qr = bytearray(p)          # qr[v] = 1 iff v is a nonzero square mod p
    for x in range(1, (p + 1) // 2):
        qr[(x * x) % p] = 1
    s = 0
    for x in range(p):
        v = (4 * x * x * x - 4 * x * x - 40 * x - 79) % p
        if v == 0:
            continue
        s += 1 if qr[v] else -1
    return -s


def main():
    t0 = time.time()
    primes = [p for p in sieve(LIMIT) if p != BAD]
    tab = {}
    for i, p in enumerate(primes):
        ap = a_p(p)
        assert ap * ap <= 4 * p, f"Hasse violated at {p}: {ap}"
        tab[str(p)] = ap
        if i % 400 == 0:
            print(f"  p={p} a_p={ap}  ({time.time()-t0:.0f}s)", flush=True)
    known = {2: -2, 3: -1, 5: 1, 7: -2, 13: 4, 17: -2, 19: 0, 23: -1, 97: -7}
    for p, v in known.items():
        assert tab[str(p)] == v, f"mismatch at {p}"
    with open("matrix/ap_table_11a1.json", "w") as f:
        json.dump({"curve": "11a1: y^2 + y = x^3 - x^2 - 10x - 20",
                   "bad_prime_excluded": BAD, "limit": LIMIT,
                   "method": "exact point count via QR table; Hasse checked",
                   "arithmetic_class": "EXACT_RATIONAL",
                   "rh_established": False, "a_p": tab}, f)
    print(f"done: {len(tab)} good primes <= {LIMIT} in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
