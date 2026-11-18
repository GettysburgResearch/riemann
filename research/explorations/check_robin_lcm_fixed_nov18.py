"""Certify floor(log lcm(1,...,N))=N and Robin signs up to an index bound."""
import argparse
from math import isqrt

from flint import arb, ctx


def events(limit):
    prime = bytearray(b"\x01") * (limit + 1)
    prime[:2] = b"\x00\x00"
    powers = {}
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            prime[p * p::p] = bytes((limit - p * p) // p + 1)
            q = p * p
            while q <= limit:
                powers[q] = p
                q *= p
    for q in range(2, limit + 1):
        if prime[q]:
            yield q, q
        elif q in powers:
            yield q, powers[q]


def census(limit):
    ctx.prec = 160
    psi = arb(0)
    log_abundancy = arb(0)
    count = 0
    positive = []
    first, last = [], []
    previous = 1
    def inspect(stop):
        nonlocal count
        if psi < previous or psi >= stop:
            return
        assert psi >= previous and psi < stop
        n = psi.floor().unique_fmpz()
        assert n is not None
        n = int(n)
        if psi <= 1:
            return
        ratio = log_abundancy - arb.const_euler() - psi.log().log()
        assert ratio > 0 or ratio < 0
        if ratio > 0:
            positive.append(n)
        count += 1
        if len(first) < 8:
            first.append(n)
        last.append(n)
        del last[:-8]
    for q, p in events(limit):
        inspect(q)
        psi += arb(p).log()
        log_abundancy += (arb(p - 1) / (p * (q - 1))).log1p()
        previous = q
    inspect(limit + 1)
    print(f"N <= {limit}; count = {count}; positive = {positive}")
    print(f"first = {first}; last = {last}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("limit", type=int, nargs="?", default=10**7)
    census(parser.parse_args().limit)
