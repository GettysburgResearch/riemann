"""Check both recorded primitive passes and the finite BNR26 inequality."""
import argparse
import hashlib
import json
from array import array
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


def independent_prefix(limit):
    """Euler's linear least-prime recursion, distinct from either segmented sieve."""
    mu = array("b", [0]) * (limit + 1)
    mu[1] = 1
    marked = bytearray(limit + 1)
    primes = []
    totals = array("i", [0, 1])
    for n in range(2, limit + 1):
        if not marked[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            multiple = n * p
            if multiple > limit:
                break
            marked[multiple] = 1
            if n % p == 0:
                break
            mu[multiple] = -mu[n]
        totals.append(totals[-1] + mu[n])
    return mu, totals


def exact_bounds(row, bits):
    denominator = 1 << bits
    energy = [Fraction(int(v), denominator) for v in row["E"]]
    mean = [Fraction(int(v), denominator) for v in row["u"]]
    assert energy[0] <= energy[1] and mean[0] <= mean[1]
    smallest_square = 0 if mean[0] <= 0 <= mean[1] else min(x*x for x in mean)
    factor = 2 * (row["N"] + 1)
    return energy, mean, [energy[0] + factor*smallest_square,
                          energy[1] + factor*max(x*x for x in mean)]


def main():
    folder = Path(__file__).resolve().parent
    records = json.loads((folder / "newton-prefix-results-nov18.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true", help="rebuild and repeat both full prime sieves")
    if parser.parse_args().replay:
        with TemporaryDirectory() as temp:
            binary = str(Path(temp) / "newton-prefix")
            subprocess.run(["g++", "-O3", "-std=c++17", str(folder / "newton_prefix_nov18.cpp"),
                            "-lcrypto", "-o", binary], check=True)
            for record in records:
                raw = subprocess.check_output([binary, str(2**32-1), record["method"]], text=True)
                assert json.loads(raw) == record
    assert [r["method"] for r in records] == ["multiply", "divide"]
    assert all(r["bits"] == 64 for r in records)
    cutoffs = [1, 3, 15, 255, 65535, 2**32-1]
    assert all([row["N"] for row in r["rows"]] == cutoffs for r in records)
    mu, totals = independent_prefix(2**20)

    @lru_cache(None)
    def mertens(n):
        if n < len(totals):
            return totals[n]
        # Sum_{d<=n} M(floor(n/d)) = 1 by the divisor-inverse identity.
        result, k = 1, 2
        while k <= n:
            q = n // k
            end = n // q
            result -= (end-k+1)*mertens(q)
            k = end+1
        return result

    joint = []
    for left, right in zip(records[0]["rows"], records[1]["rows"]):
        n = left["N"]
        for field in ("N", "M", "zeros", "max_abs_M", "sha256"):
            assert left[field] == right[field], (n, field)
        assert left["M"] == mertens(n)
        squarefree = sum(mu[d]*(n//(d*d)) for d in range(1, isqrt(n)+1))
        assert n-left["zeros"] == squarefree
        bounds = [exact_bounds(row, 64) for row in (left, right)]
        for a, b in zip(*bounds):
            assert max(a[0], b[0]) <= min(a[1], b[1])
        if n < len(mu):
            assert left["sha256"] == hashlib.sha256(bytes(k+1 for k in mu[1:n+1])).hexdigest()
            scale = 1 << 96
            e_lo = e_hi = u_lo = u_hi = 0
            for k in range(1, n+1):
                den = k*(k+1)
                sq = scale*totals[k]**2
                signed = scale*totals[k]
                e_lo += sq//den
                e_hi -= (-sq)//den
                u_lo += signed//den
                u_hi -= (-signed)//den
            for box, lo, hi in [(bounds[0][0], e_lo, e_hi), (bounds[0][1], u_lo, u_hi)]:
                assert max(box[0], Fraction(lo, scale)) <= min(box[1], Fraction(hi, scale))
        lo = max(b[2][0] for b in bounds)
        hi = min(b[2][1] for b in bounds)
        joint.append((lo, hi))

    assert all(lo > 0 for lo, _ in joint)
    for (prev_lo, _), (_, next_hi) in zip(joint, joint[1:]):
        assert (1+next_hi)**2 <= 4*(1+prev_lo)**3
    final_lo, final_hi = joint[-1]
    assert Fraction(19078, 10000) < final_lo <= final_hi < Fraction(19079, 10000)
    print("Verified five finite Newton transitions.")
    print("Final M", records[0]["rows"][-1]["M"])
    print("Final A is strictly between 1.9078 and 1.9079.")


if __name__ == "__main__":
    main()
