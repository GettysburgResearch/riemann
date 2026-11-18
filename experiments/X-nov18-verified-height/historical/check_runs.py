"""Independently parse the original Platt Arb program's successful intervals."""
import argparse
import hashlib
import json
import re
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

ANCHOR = 3_000_175_332_800
INDEX = 12_363_153_437_138
LOOK = re.compile(r"looking for (\d+)-(\d+)=(\d+) zeros")
DONE = re.compile(r"All (\d+) zeros found in region ([\d.]+) to ([\d.]+) using stat points\.")
MISS = re.compile(r"Missed .+ in region ([\d.]+) to ([\d.]+)\.")


def parse_log(text):
    lines = text.splitlines()
    if not lines or not lines[0].startswith("Command line:- "):
        raise ValueError("Missing original command line")
    binary, precision, first, iterations, step = lines[0].removeprefix("Command line:- ").split()
    if Path(binary).name != "arb_zeta" or int(precision) not in {100,120,128,144,152,160}:
        raise ValueError("Unexpected program or precision")
    first, step = Fraction(first), Fraction(step)
    iterations = int(iterations)
    if (not 0 < iterations or not 0 < step <= 1344 or (step * 512 / 21).denominator != 1
            or int(step * 512 / 21) % 2 != 0 or first.denominator > 64 or first - 3000 < 3_000_000_000_000
            or first + iterations*step + 3000 > 3_000_200_000_000):
        raise ValueError("Invalid grid domain for the pinned historical parameters")
    states, counts = [], None
    for line in lines:
        look, done, missed = LOOK.fullmatch(line), DONE.fullmatch(line), MISS.fullmatch(line)
        if look:
            if counts is not None:
                raise ValueError("Unresolved Turing check")
            high, low, difference = map(int, look.groups())
            if high-low != difference or low <= 0:
                raise ValueError("Inconsistent original Turing bound")
            counts = low, high
        elif done or missed:
            if counts is None:
                raise ValueError("Missing original Turing bound")
            if done:
                number, left, right = done.groups()
                if counts[1] - counts[0] != int(number):
                    raise ValueError("Successful sign and strip counts differ")
            else:
                left, right = missed.groups()
            left, right = Fraction(left), Fraction(right)
            if left != first+len(states)*step or right != left+step:
                raise ValueError("Unexpected original grid interval")
            states.append((left, right, counts if done else None))
            counts = None
    if counts is not None or len(states) != iterations:
        raise ValueError("Incomplete original run")
    return states


def read_all(directory):
    good, failed, digests = [], [], {}
    for path in sorted(directory.glob("*.log")):
        raw = path.read_bytes()
        digests[path.name] = hashlib.sha256(raw).hexdigest()
        for left, right, counts in parse_log(raw.decode("ascii")):
            if counts is None:
                failed.append((left, right))
            else:
                good.append((left, right, counts[0], counts[1]))
    return sorted(good), failed, digests


def frontier(good):
    known = {Fraction(ANCHOR): INDEX}
    for a,b,lo,hi in good:
        for point,value in ((a,lo),(b,hi)):
            if known.setdefault(point,value) != value:
                raise ValueError("Independent original endpoint counts conflict")
    counts = [value for _,value in sorted(known.items())]
    if any(a>b for a,b in zip(counts,counts[1:])):
        raise ValueError("Nonmonotone original strip counts")
    end = Fraction(ANCHOR)
    for left,right,_,_ in good:
        if left > end:
            break
        end = max(end, right)
    return end, known[end]


def decimal(point):
    return str(Decimal(point.numerator)/Decimal(point.denominator))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=Path, default=Path(__file__).parent/"runs")
    parser.add_argument("--count", action="store_true", help="also cross-check historical endpoints with modern FLINT")
    parser.add_argument("--check-chains", action="store_true",
                        help="certify exact counts at both ends of every disjoint-region sign chain")
    args=parser.parse_args()
    good, failed, digests=read_all(args.runs)
    end, count=frontier(good)
    checked_points = set()
    if args.count or args.check_chains:
        checked_points = {(Fraction(ANCHOR), INDEX), (end, count)}
    if args.check_chains:
        # Within a chain, the original sign brackets lie in nonoverlapping
        # successive height intervals, so their witness counts add directly.
        chains = []
        remaining = {}
        for a,b,lo,hi in sorted(set(good)):
            i = remaining.pop(a, None)
            if i is None:
                i = len(chains)
                chains.append([a, lo, b, hi])
            else:
                if chains[i][3] != lo:
                    raise ArithmeticError("Discontinuous chain counts")
                chains[i][2:] = [b, hi]
            # When there are multiple possible predecessors, leaving the
            # other chain open just costs one extra generic endpoint check.
            remaining[b] = i
        for a,lo,b,hi in chains:
            checked_points.update(((a,lo),(b,hi)))
    if checked_points:
        from flint import arb, ctx
        ctx.prec=128
        for point,n in sorted(checked_points):
            result=(arb(point.numerator)/point.denominator).zeta_nzeros()
            if not result.is_exact() or result != n:
                raise ArithmeticError("Generic full-strip count disagrees")
    digest=hashlib.sha256()
    for name,h in sorted(digests.items()):
        digest.update(f"{name}\t{h}\n".encode())
    print(json.dumps({"old_height":ANCHOR,"old_count":INDEX,"contiguous_height":decimal(end),
                      "contiguous_count":count,"new_zeros":count-INDEX,"successful_regions":len(good),
                      "unsuccessful_attempts":len(failed),"transcripts":len(digests),
                      "ordered_transcript_digest":digest.hexdigest(),"modern_counts_rechecked":bool(checked_points),
                      "checked_sign_chain_endpoints":len(checked_points) if args.check_chains else None},
                     indent=2))


if __name__=="__main__":
    main()
