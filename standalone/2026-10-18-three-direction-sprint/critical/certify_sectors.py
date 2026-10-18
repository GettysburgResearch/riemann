"""Directed complete Gaussian primitive-ratio coefficients and prime rays.

Requires python-flint==0.9.0. No arithmetic source or certificate is read from
deposited JSON. The complete omitted tail is added to BOTH sides of each ball.
Use --dependency-dir only to point at an already installed python-flint.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time


def require(ok, message):
    if not ok:
        raise ValueError(message)


def numerator_sieve(limit):
    nums = [1]*(limit+1)
    prime = bytearray(b'\x01')*(limit+1)
    prime[:2] = b'\x00\x00'
    ps = []
    for p in range(2, limit+1):
        if prime[p]:
            ps.append(p)
            if p*p <= limit:
                prime[p*p:limit+1:p] = b'\x00'*(((limit-p*p)//p)+1)
            for n in range(p, limit+1, p):
                nums[n] *= 1-p
    return nums, ps


def exact_beta_table(limit, nums, ps):
    corr = [Fraction(1)]*(limit+1)
    for p in ps:
        fac = Fraction(p+1, p+2)
        for n in range(p, limit+1, p):
            corr[n] *= fac
    return [Fraction(0)]+[Fraction(nums[n], n)*corr[n]
                          for n in range(1, limit+1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dependency-dir', type=Path)
    parser.add_argument('--cutoff', type=int, default=16384)
    parser.add_argument('--bits', type=int, default=192)
    parser.add_argument('--skip-rays', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.dependency_dir:
        sys.path.insert(0, str(args.dependency_dir.resolve()))
    import flint
    from flint import arb, ctx
    require(flint.__version__ == '0.9.0', 'Pinned python-flint 0.9.0 required.')
    require(args.cutoff >= 1024 and args.bits >= 128, 'Insufficient replay range.')
    ctx.prec = args.bits
    start = time.monotonic()
    n = args.cutoff
    nums, ps = numerator_sieve(n)
    betas = exact_beta_table(n, nums, ps)

    def ball(q):
        return arb(q.numerator)/q.denominator

    def render(z):
        require(z.is_finite(), 'Nonfinite enclosure.')
        txt = z.str(55, more=True)
        require(arb(txt).contains(z), 'Serialization lost an enclosure.')
        return txt

    logs = [arb(0)]+[arb(j).log() for j in range(1, n+1)]
    broots = [arb(0)]+[ball(betas[j])/arb(j).sqrt() for j in range(1, n+1)]
    sectors = []
    acc = arb(1)
    for s in (1, 2, 3):
        row = arb(0)
        for r in range(s+1, n+1):
            if math.gcd(r, s) == 1:
                u = logs[r]-logs[s]
                row += broots[r]*(-u*u/8).exp()
        acc += 2*broots[s]*row
        tail = arb(0)
        for j in range(1, s+1):
            zz = ((arb(n)/j).log()-2)/arb(8).sqrt()
            tail += abs(ball(betas[j]))*zz.erfc()
        tail *= 2*(arb(1)/2).exp()*(2*arb.pi()).sqrt()
        require(tail > 0, 'Positive whole-ratio tail required.')
        enclosure = acc+arb(0, tail.upper())
        target = {1: (Fraction(-9, 5), Fraction(-17, 10)),
                  2: (Fraction(-4, 5), Fraction(-7, 10)),
                  3: (Fraction(3, 10), Fraction(1, 2))}[s]
        require(enclosure > ball(target[0]) and enclosure < ball(target[1]),
                'Complete infinite sector failed its strict sign/size gate.')
        rec = {'small_cutoff': s, 'finite_ratio_cutoff': n,
               'complete_coefficient_ball': render(enclosure),
               'whole_omitted_ratio_tail_upper': render(tail),
               'strict_rational_gate': [str(q) for q in target]}
        sectors.append(rec)
        print(json.dumps({'sector_finished': rec}), flush=True)

    rays = []
    if not args.skip_rays:
        pairs = ((5, 7), (11, 13), (17, 19))
        max_n = max(q for _, q in pairs)*n
        raynums, _ = numerator_sieve(max_n)
        c0 = 1/(2*(2*arb.pi()).sqrt())
        invsqrt2 = 1/arb(2).sqrt()
        for p, q in pairs:
            pref = c0/arb(p*q).sqrt()*(-((arb(p)/q).log())**2/8).exp()
            for T in (64, 256, 1024):
                L = arb(T)/arb(p*q).sqrt()
                total = arb(0)
                for d in range(1, n+1):
                    ph = ((arb(d)/L).log()*invsqrt2).erfc()/2
                    coeff = arb(raynums[p*d]*raynums[q*d])/(p*q*d**3)
                    total += coeff*ph
                aa = (arb(n)/L).log()
                require(aa > 0, 'Ray-tail cutoff must exceed its center.')
                # integral_a^infinity Phi(-u)du <= phi(a)/a^2.
                tail = (-aa*aa/2).exp()/((2*arb.pi()).sqrt()*aa*aa)
                complete = pref*(total+arb(0, tail.upper()))
                require(complete > 0, 'Complete actual prime-ray sign not positive.')
                rec = {'primes': [p, q], 'horizon': T, 'common_factor_cutoff': n,
                       'complete_ray_ball': render(complete),
                       'whole_omitted_d_tail_upper': render(pref*tail)}
                rays.append(rec)
                print(json.dumps({'ray_finished': rec}), flush=True)

    digest = hashlib.sha256('\n'.join(str(v) for v in nums).encode()).hexdigest()
    result = {'status': 'PASS', 'arithmetic': 'DIRECTED_INTERVAL',
              'python_flint': flint.__version__, 'precision_bits': args.bits,
              'source_numerator_sha256': digest,
              'complete_infinite_sectors': sectors, 'complete_prime_rays': rays,
              'uniform_analytic_theorems_certified_by_this_script': False,
              'elapsed_seconds': time.monotonic()-start}
    out = args.output or Path(__file__).with_name('DIRECTED_CHECKS.json')
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'output': str(out),
                      'elapsed_seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
