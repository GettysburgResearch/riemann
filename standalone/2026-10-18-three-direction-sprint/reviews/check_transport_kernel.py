"""Complete finite transport-kernel controls, with directed log evaluation.

All physical cells are represented by exact integer jump events. References
are actual squarefree old inputs of opposite parity; this checker does not
replace the asymptotic reference-density theorem or projection estimates.
"""
from bisect import bisect_left
from collections import defaultdict
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time


def trial_mu(n):
    out, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            out = -out
            if n % p == 0: return 0
        p += 1
    return -out if n > 1 else out


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dependency-dir', type=Path, required=True)
    ap.add_argument('--prefix', type=int, default=257)
    args = ap.parse_args()
    sys.path.insert(0, str(args.dependency_dir.resolve()))
    import flint
    from flint import arb, ctx
    if flint.__version__ != '0.9.0': raise ValueError('pinned python-flint required')
    ctx.prec = 256
    began = time.monotonic()
    Y, checks = args.prefix, 0
    ps = [p for p in range(Y//2+1, Y+1) if prime(p)]
    mu = [0]+[trial_mu(n) for n in range(1, Y+1)]
    B = 4*(isqrt(Y)+1)
    references = {}
    for a in range(1, Y+1):
        for b in range(a+1, min(Y, a+B)+1):
            if mu[a] and mu[b] and (a+b) % 2:
                references.setdefault(a*b, (a, b))
    products = sorted(references)
    plan = []
    for i, p in enumerate(ps):
        for ell in ps[i+1:]:
            N = p*ell
            index = bisect_left(products, N)
            choices = products[max(0, index-1):min(len(products), index+1)]
            M = min(choices, key=lambda m: abs(m-N))
            a, b = references[M]
            plan.append((N, M, a, b))
    if not plan: raise ValueError('empty target sector')
    G = max(abs(N-M) for N, M, _, _ in plan)
    if not (1 <= G <= Y*Y//8): raise ValueError('finite gap outside lemma range')
    if len({N for N, _, _, _ in plan}) != len(plan): raise ValueError('target collision')
    events = defaultdict(F)
    logpart = arb(0)
    end = 2*Y*Y
    for N, M, a, b in plan:
        assert Y*Y <= 4*N <= 4*Y*Y and M == a*b and abs(N-M) <= G
        assert mu[a] and mu[b] and (a+b) % 2 and abs(a-b) <= B
        checks += 2
        logpart += (arb(2)/N)*(arb(N)/M).log()
        for d, sign in [(N, 1), (M, -1)]:
            for j in range(1, end//d+1):
                events[j*d] += F(2*sign, N*j)
        for target, _, _, _ in plan:
            assert M % target != 0, 'reference creates a target denominator'
            checks += 1
    bound = arb(120)*(G+1)/(Y*Y)
    pos, amplitude, energy = 0, logpart, arb(0)
    max_upper = arb(0)
    for event, delta in sorted(events.items()):
        assert abs(amplitude) < bound
        checks += 1
        energy += (event-pos)*amplitude**2
        max_upper = max(max_upper, abs(amplitude).upper())
        amplitude += arb(delta.numerator)/delta.denominator
        pos = event
    energy += (end-pos)*amplitude**2
    max_upper = max(max_upper, abs(amplitude).upper())
    assert abs(amplitude) < bound
    assert energy < arb(28800)*(G+1)**2/(Y*Y)
    checks += 2
    # Reconstruct selected complete physical nodes directly from both floors.
    for x in [Y, 2*Y, Y*Y//4, Y*Y, end]:
        direct = logpart
        for N, M, _, _ in plan:
            hn = sum((F(1, j) for j in range(1, x//N+1)), F(0))
            hm = sum((F(1, j) for j in range(1, x//M+1)), F(0))
            v = F(2, N)*(hn-hm)
            direct += arb(v.numerator)/v.denominator
        via_events = logpart
        total = sum((delta for event, delta in events.items() if event <= x), F(0))
        via_events += arb(total.numerator)/total.denominator
        assert (direct-via_events).contains(0)
        checks += 1
    def text(x):
        out = x.str(65, more=True)
        assert arb(out).contains(x)
        return out
    result = {'status': 'PASS_COMPLETE_FINITE_TRANSPORT_CONTROLS', 'prefix': Y,
              'target_pairs': len(plan), 'reference_pair_count': len(references),
              'maximum_gap': G, 'balanced_width': B,
              'complete_physical_range': [0, end], 'exact_jump_events': len(events),
              'pointwise_absolute_upper': text(max_upper), 'full_energy': text(energy),
              'lemma_pointwise_upper': text(bound), 'checks': checks,
              'plan': [list(record) for record in plan],
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'elapsed_seconds': time.monotonic()-began,
              'native_projection_or_full_remainder_bound_proved_by_computation': False}
    Path(__file__).with_name('TRANSPORT_KERNEL_CONTROLS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'plan'}), flush=True)


if __name__ == '__main__': main()
