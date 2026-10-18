"""Complete finite critical energy for a compact ordinary-zeta detector.

psi(u)=(1-|u|/log2)_+. The full infinite arithmetic source up to horizon T
has only n<=2T. Its log-scale amplitude is piecewise linear with explicitly
known slope jumps; all cells are integrated exactly by polynomial formulas.
Selected prime rays include EVERY possible common factor d, since compact
support supplies an exact finite endpoint. Requires python-flint==0.9.0.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import time


def require(ok, why):
    if not ok:
        raise ValueError(why)


def arithmetic(limit):
    nums = [1]*(limit+1)
    flags = bytearray(b'\x01')*(limit+1)
    flags[:2] = b'\x00\x00'
    ps = []
    for p in range(2, limit+1):
        if flags[p]:
            ps.append(p)
            if p*p <= limit:
                flags[p*p:limit+1:p] = b'\x00'*((limit-p*p)//p+1)
            for n in range(p, limit+1, p):
                nums[n] *= 1-p
    return nums, ps


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dependency-dir', type=Path)
    ap.add_argument('--bits', type=int, default=256)
    ap.add_argument('--max-horizon', type=int, default=262144)
    ap.add_argument('--prime-sector-horizons', type=int, nargs='*', default=[65536, 262144])
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    if args.dependency_dir:
        sys.path.insert(0, str(args.dependency_dir.resolve()))
    import flint
    from flint import arb, ctx
    require(flint.__version__ == '0.9.0', 'Pinned python-flint required.')
    require(args.bits >= 192 and args.max_horizon >= 64, 'Insufficient replay range.')
    require(all(64 <= T <= args.max_horizon for T in args.prime_sector_horizons),
            'Prime sector beyond complete source horizon.')
    ctx.prec = args.bits
    started = time.monotonic()
    Tmax = args.max_horizon
    nums, ps = arithmetic(2*Tmax)
    h = arb(2).log()

    def text(z):
        require(z.is_finite(), 'Nonfinite interval.')
        out = z.str(60, more=True)
        require(arb(out).contains(z), 'Serialization lost an enclosure.')
        return out

    # Independent trial-factor checks include prime powers and shared primes.
    exact_cases = 0
    for n in range(1, min(5000, 2*Tmax)+1):
        k = n
        val = 1
        p = 2
        while p*p <= k:
            if k % p == 0:
                val *= 1-p
                while k % p == 0:
                    k //= p
            p += 1
        if k > 1:
            val *= 1-k
        require(val == nums[n], 'Arithmetic numerator sieve disagrees with factorization.')
        exact_cases += 1

    def bn(n):
        return arb(nums[n])/(arb(n)*arb(n).sqrt())

    checkpoints = {Tmax, *args.prime_sector_horizons,
                   *(T for T in (1, 2, 5, 17, 64) if T <= Tmax)}
    j = 64
    while j <= Tmax:
        checkpoints.add(j)
        j *= 4
    f = arb(0)
    slope = arb(0)
    energy = arb(0)
    complete = {}
    endpoint_values = {}
    for k in range(1, 2*Tmax):
        jump = bn(k)
        if k % 2 == 0:
            jump -= 2*bn(k//2)
        if k % 4 == 0:
            jump += bn(k//4)
        slope += jump/h
        dt = (arb(k+1)/k).log()
        nxt = f+slope*dt
        energy += dt*(f*f+f*nxt+nxt*nxt)/3
        f = nxt
        if (k+1) % 2 == 0 and (k+1)//2 in checkpoints:
            T = (k+1)//2
            require(energy > 0, 'Complete critical energy not positive.')
            rec = {'horizon': T, 'all_source_modes_through': 2*T,
                   'all_log_cells': 2*T-1,
                   'complete_energy': text(energy), 'endpoint_amplitude': text(f),
                   'omitted_source_and_physical_tail': 'exactly zero'}
            complete[T] = energy
            endpoint_values[T] = f
            print(json.dumps({'complete_energy_finished': rec}), flush=True)

    # Direct nodal evaluation independent of the slope-jump recurrence.
    nodal = []
    for T in (1, 2, 5, 17, 64):
        if T > Tmax:
            continue
        direct = arb(0)
        for n in range(max(1, (T+1)//2), 2*T+1):
            # The tent is exactly zero outside [T/2,2T].
            if 2*n < T or n > 2*T:
                continue
            logratio = (arb(n)/T).log()
            direct += bn(n)*(1-abs(logratio)/h)
        # Independently assemble the cumulative piecewise-linear expression.
        using_hinges = arb(0)
        for n in range(1, 2*T+1):
            z = arb(0)
            if n < 2*T:
                z += (arb(2*T)/n).log()
            if n < T:
                z -= 2*(arb(T)/n).log()
            if 2*n < T:
                z += (arb(T)/(2*n)).log()
            using_hinges += bn(n)*z/h
        require(direct.overlaps(using_hinges), 'Independent tent-source nodal assembly mismatch.')
        require(direct.overlaps(endpoint_values[T]),
                'Slope-jump endpoint disagrees with direct complete source.')
        nodal.append({'horizon': T, 'direct_node': text(direct),
                      'independent_hinge_node': text(using_hinges),
                      'slope_jump_node': text(endpoint_values[T])})

    def integrate_affine_product(left, right, f0, g0, df, dg):
        length = right-left
        return length*(f0*g0+(f0*dg+g0*df)*length/2+df*dg*length*length/3)

    def overlap(T, p, q, d, delta):
        # For q/p<=2 the overlap has three (possibly degenerate) segments.
        # The larger-ratio case is needed for independent full-Gram checks.
        if q >= 4*p:
            return arb(0)
        if 2*T <= d*q:
            return arb(0)
        stop = (arb(T)/(d*p)).log()
        ans = arb(0)
        if q > 2*p:
            left = delta-h
            right = stop if T < 2*d*p else h
            return integrate_affine_product(left, right,
                      (h-left)/h, (left-delta+h)/h, -1/h, 1/h)
        left = delta-h
        right = stop if T < d*p else arb(0)
        ans += integrate_affine_product(left, right,
                    (left+h)/h, (left-delta+h)/h, 1/h, 1/h)
        if T <= d*p:
            return ans
        left = arb(0)
        right = stop if T < d*q else delta
        ans += integrate_affine_product(left, right,
                    (h-left)/h, (left-delta+h)/h, -1/h, 1/h)
        if T <= d*q:
            return ans
        left = delta
        right = stop if T < 2*d*p else h
        ans += integrate_affine_product(left, right,
                    (h-left)/h, (h+delta-left)/h, -1/h, -1/h)
        return ans

    gram_checks = []
    for T in (1, 2, 5, 17):
        if T > Tmax:
            continue
        direct_gram = arb(0)
        pairs = 0
        for q in range(1, 2*T+1):
            for p in range(1, q+1):
                value = bn(p)*bn(q)*overlap(T, p, q, 1, (arb(q)/p).log())
                direct_gram += value*(1 if p == q else 2)
                pairs += 1
        require(direct_gram.overlaps(complete[T]),
                'Independent complete full-Gram integration disagrees with log cells.')
        gram_checks.append({'horizon': T, 'all_unordered_pairs': pairs,
                            'direct_complete_gram': text(direct_gram),
                            'piecewise_linear_energy': text(complete[T])})

    sectors = []
    for T in args.prime_sector_horizons:
        S = math.isqrt(T)
        selected = [p for p in ps if S <= p <= 3*S//2]
        total = arb(0)
        rays = 0
        common_terms = 0
        for qi, q in enumerate(selected):
            for p in selected[:qi]:
                delta = (arb(q)/p).log()
                ray = arb(0)
                for d in range(1, (2*T)//q+1):
                    # These exact source numerators retain all common primes.
                    coeff = arb(nums[p*d]*nums[q*d])/(p*q*d**3)
                    ray += coeff*overlap(T, p, q, d, delta)
                    common_terms += 1
                ray /= arb(p*q).sqrt()
                total += 2*ray
                rays += 1
        require(rays > 0 and total > 0, 'Actual complete prime sector not positive.')
        complement = complete[T]-total
        rec = {'horizon': T, 'prime_interval': [S, 3*S//2],
               'prime_count': len(selected), 'unordered_rays': rays,
               'ordered_rays': 2*rays, 'all_common_factor_terms': common_terms,
               'complete_signed_prime_sector': text(total),
               'complete_signed_complement': text(complement),
               'complement_strictly_negative': bool(complement < 0),
               'all_common_factor_tail': 'exactly zero beyond floor(2T/q)'}
        sectors.append(rec)
        print(json.dumps({'complete_prime_sector_finished': rec}), flush=True)

    result = {'status': 'PASS', 'arithmetic': 'DIRECTED_INTERVAL',
              'python_flint': flint.__version__, 'precision_bits': args.bits,
              'kernel': 'psi(u)=(1-|u|/log2)_+',
              'complete_energy': [{'horizon': T, 'ball': text(v)}
                                  for T, v in sorted(complete.items())],
              'independent_source_nodes': nodal,
              'independent_full_gram_checks': gram_checks,
              'complete_prime_sectors': sectors,
              'exact_coefficient_cases': exact_cases,
              'source_numerator_sha256': hashlib.sha256(
                  ','.join(map(str, nums)).encode()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'global_critical_bound_certified_by_this_script': False,
              'elapsed_seconds': time.monotonic()-started}
    out = args.output or Path(__file__).with_name('TENT_ENERGY_CHECKS.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'output': str(out),
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
