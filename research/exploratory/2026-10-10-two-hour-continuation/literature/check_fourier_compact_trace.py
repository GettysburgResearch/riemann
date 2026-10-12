"""Literal finite sextic trace under a radial Fourier-compact positive test.

The finite Poisson formula is proved in FOURIER_COMPACT_BALANCED_TRACE.md.
No asymptotic generalized-moment estimate is claimed.
"""
from itertools import combinations
from pathlib import Path
from math import isqrt
import argparse
import hashlib
import json
from flint import arb, acb, ctx


def require(ok, label):
    if not ok:
        raise ArithmeticError(label)


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c-b*d


def conjugate(z):
    a, b = z
    return a-b, -b


def norm(z):
    a, b = z
    return a*a-a*b+b*b


UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]


def source_primes():
    primes = []
    for seed in [(-2, -3), (1, -3), (-2, 3), (1, 6)]:
        for generator in (seed, conjugate(seed)):
            q = norm(generator)
            require(q in (7, 13, 19, 31), 'literal native prime norm')
            require(all(q % d for d in range(2, isqrt(q)+1)), 'prime residue field')
            a, b = generator
            require(a % 3 == 1 and b % 3 == 0, 'primary generator')
            root = -a * pow(b, -1, q) % q
            require((root*root+root+1) % q == 0, 'native omega residue')
            lookup = {(a+b*root) % q: i for i, (a, b) in enumerate(UNITS)}
            table = [None] + [lookup[pow(x, (q-1)//6, q)] for x in range(1, q)]
            gamma = acb(0)
            for x in range(1, q):
                # Literal source e(x/pi), not an arbitrary finite-field additive character.
                angle = arb(table[x])/6-arb(generator[1]*x)/q
                gamma += acb(0, 2*arb.pi()*angle).exp()
            gamma /= arb(q).sqrt()
            require((gamma*gamma.conjugate()).real.contains(1), 'primitive Gauss norm')
            require(gamma.abs_lower() > arb('0.999999999999'), 'nonzero Gauss factor')
            primes.append(dict(generator=generator, q=q, root=root,
                               table=table, gamma=gamma, charge=(q-1)//6))
    require(len({(p['q'], p['root']) for p in primes}) == 8, 'eight prime ideals')
    return primes


def exponent(p, z):
    residue = (z[0]+z[1]*p['root']) % p['q']
    return p['table'][residue]


def representatives(maxnorm):
    # Exact norm inequalities put every orbit inside this box.
    radius = isqrt((4*maxnorm)//3)+1
    require(3*radius*radius > 4*maxnorm, 'complete lattice box')
    out = []
    count = 0
    for a in range(-radius, radius+1):
        for b in range(-radius, radius+1):
            z = (a, b)
            if not 0 < norm(z) <= maxnorm:
                continue
            count += 1
            orbit = [mul(u, z) for u in UNITS]
            require(len(set(orbit)) == 6, 'free nonzero unit orbit')
            if z == min(orbit):
                out.append(z)
    require(count == 6*len(out), 'complete radial orbit partition')
    return out


def run():
    ctx.prec = 192
    root = Path('/workspace/.riemann-research/moment-sources/914/standalone')
    source = root/'2026-10-10-sextic-moment-conductor-core'/'A2_COMPLETION.md'
    require(hashlib.sha256(source.read_bytes()).hexdigest() ==
            'd99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad',
            'pinned literal first-Poisson source')
    primes = source_primes()
    omega = acb(-arb(1)/2, arb(3).sqrt()/2)
    zeta = [acb(a)+b*omega for a, b in UNITS]
    h, radius = 40, arb(1)/4
    total = acb(0)
    wrong_crt = acb(0)
    wrong_minus = acb(0)
    records = []
    kept = killed = frequencies = 0
    for indices in combinations(range(8), 4):
        ps = [primes[i] for i in indices]
        conductor = (1, 0)
        for p in ps:
            conductor = mul(conductor, p['generator'])
        nq = norm(conductor)
        require(nq == ps[0]['q']*ps[1]['q']*ps[2]['q']*ps[3]['q'], 'CRT conductor norm')
        # Fourier support is H*N(h)/N(conductor)<1/4.
        maxnorm = (nq-1)//160
        phase = []
        for i, p in enumerate(ps):
            other = (1, 0)
            for j, pp in enumerate(ps):
                if i != j:
                    other = mul(other, pp['generator'])
            e = exponent(p, other)
            require(e is not None, 'coprime local CRT complement')
            phase.append(p['gamma']*zeta[e])
        allocations = []
        for left in combinations(range(4), 2):
            signs = [1 if i in left else -1 for i in range(4)]
            charge = sum(s*p['charge'] for s, p in zip(signs, ps)) % 6
            if charge:
                killed += 1
                continue
            kept += 1
            correct = plain = no_minus = acb(1)
            for i, (sgn, p) in enumerate(zip(signs, ps)):
                if sgn == 1:
                    correct *= phase[i]
                    plain *= p['gamma']
                    no_minus *= phase[i]
                else:
                    sigma = (-1)**p['charge']
                    correct *= sigma*phase[i].conjugate()
                    plain *= sigma*p['gamma'].conjugate()
                    no_minus *= phase[i].conjugate()
            allocations.append((signs, correct, plain, no_minus))
        value = value_plain = value_minus = acb(0)
        complete_orbits = representatives(maxnorm)
        sums = [[arb(0), arb(0)] for _ in allocations]
        active = 0
        for z in complete_orbits:
            es = [exponent(p, z) for p in ps]
            if None in es:
                continue
            active += 1
            distance = (arb(h*norm(z))/nq).sqrt()
            area = (2*radius*radius*(distance/(2*radius)).acos() -
                    distance/2*(4*radius*radius-distance*distance).sqrt())
            require(area > 0, 'strict interior Fourier overlap')
            psi = 4*arb(3).sqrt()*area/(2*arb.pi()**2*radius**4)
            for out, (signs, *_rest) in zip(sums, allocations):
                e = -sum(s*x for s, x in zip(signs, es)) % 6
                a, b = UNITS[e]
                out[0] += 6*a*psi
                out[1] += 6*b*psi
        for (a, b), (_signs, coefficient, plain, no_minus) in zip(sums, allocations):
            charsum = acb(a)+b*omega
            value += coefficient*charsum
            value_plain += plain*charsum
            value_minus += no_minus*charsum
        # 2! on each ordered side; source Poisson amplitude H/sqrt(Nq).
        scale = arb(4*h)/arb(nq).sqrt()
        value *= scale
        value_plain *= scale
        value_minus *= scale
        total += value
        wrong_crt += value_plain
        wrong_minus += value_minus
        frequencies += 6*active
        require(value.imag.contains(0), 'full balanced radial conductor is real')
        records.append(dict(prime_indices=list(indices), conductor=list(conductor),
                            conductor_norm=nq, neutral_allocations=len(allocations),
                            complete_unit_orbits=len(complete_orbits),
                            active_unit_orbits=active, leading_ball=value.real.str(50, more=True)))
    require(len(records) == 70 and kept+killed == 420, 'all distinct prime faces')
    require(total.imag.contains(0), 'real full leading remainder')
    require(arb(3916) < total.real < arb(3917), 'nonzero compact-Fourier leading witness')
    require(abs(wrong_crt.real-total.real) > 1, 'omitting CRT reciprocity phase changes answer')
    require(abs(wrong_minus.real-total.real) > 1, 'omitting local chi(-1) changes answer')
    require(any(arb(r['leading_ball']) > 1 for r in records), 'positive conductor terms')
    require(any(arb(r['leading_ball']) < -1 for r in records), 'negative conductor terms')
    # An explicit smooth disk mollification of radius delta changes the finite
    # sum by less than this uniform bound, and preserves its support index set.
    delta = arb('1e-12')
    maxq = max(r['conductor_norm'] for r in records)
    require(maxq*(2*delta+4*delta**2) < arb(1)/4, 'no new dual lattice norm after mollification')
    smooth_error = 8640*delta*sum(arb(r['conductor_norm']).sqrt() for r in records)
    require(smooth_error < arb('0.001'), 'paid genuine Schwartz mollification')
    proof = Path(__file__).with_name('FOURIER_COMPACT_BALANCED_TRACE.md')
    return dict(status='DIRECTED_LITERAL_FOURIER_COMPACT_TRACE_PASS', precision_bits=192,
                source_commit='0cc0428fedbbfc340044c7451b3d392c1da9a103',
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
                D=30, H=h, test='4*(2*J1((pi/sqrt(3))*sqrt(x))/((pi/sqrt(3))*sqrt(x)))^2',
                Fourier_support_norm='1/4', distinct_prime_sets=70,
                neutral_allocations=kept, killed_allocations=killed,
                active_dual_frequencies=frequencies,
                leading_remainder_ball=total.real.str(50, more=True),
                wrong_CRT_ball=wrong_crt.real.str(50, more=True),
                wrong_minus_ball=wrong_minus.real.str(50, more=True),
                Schwartz_mollifier_radius='1e-12', smooth_error_bound=smooth_error.str(50, more=True),
                records=records, imported_Poisson_analysis_independently_rebuilt=False,
                asymptotic_generalized_moment_bound_proved=False, rh_proved=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))
