"""Entire literal native critical R2 with Fourier-compact radial smoothing."""
from collections import Counter
from itertools import product, combinations
from pathlib import Path
import argparse
import hashlib
import json
from flint import arb, acb, ctx
import check_fourier_compact_trace as face


def psi(n, denominator):
    distance = (arb(40*n)/denominator).sqrt()
    radius = arb(1)/4
    area = (2*radius**2*(distance/(2*radius)).acos()-
            distance/2*(4*radius**2-distance**2).sqrt())
    face.require(area > 0, 'strict compact Fourier support')
    return 4*arb(3).sqrt()*area/(2*arb.pi()**2*radius**4)


def run():
    ctx.prec = 192
    here = Path(__file__).parent
    face.require(hashlib.sha256((here/'check_fourier_compact_trace.py').read_bytes()).hexdigest() ==
                 'dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598',
                 'frozen literal prime-face helper')
    source_root = Path('/workspace/.riemann-research/moment-sources/914/standalone/2026-10-10-sextic-moment-conductor-core')
    source_hashes = {'A2_COMPLETION.md':
        'd99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad',
        'CONDUCTOR_SECTORS.md':
        'c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983'}
    for name, expected in source_hashes.items():
        face.require(hashlib.sha256((source_root/name).read_bytes()).hexdigest() == expected,
                     'literal source identity and sector ' + name)
    primes = face.source_primes()
    omega = acb(-arb(1)/2, arb(3).sqrt()/2)
    zeta = [acb(a)+b*omega for a, b in face.UNITS]
    gamma = {}
    for i, p in enumerate(primes):
        for e in range(1, 6):
            ans = acb(0)
            for a in range(1, p['q']):
                angle = arb(e*p['table'][a])/6-arb(p['generator'][1]*a)/p['q']
                ans += acb(0, 2*arb.pi()*angle).exp()
            ans /= arb(p['q']).sqrt()
            face.require((ans*ans.conjugate()).real.contains(1), 'all nonprincipal Gauss norms')
            gamma[i, e] = ans
    critical = Counter()
    leading = Counter()
    all_tuples = 0
    product_diagonals = 0
    critical_diagonals = 0
    for t in product(range(8), repeat=4):
        left, right = Counter(t[:2]), Counter(t[2:])
        g1 = g2 = 1
        for i, p in enumerate(primes):
            r, s = left[i], right[i]
            if r+s == 1:
                g1 *= p['q']
            if r+s == 2 and (r-s) % 6:
                g2 *= p['q']
        iscritical = g1 != 1 and g1*g1*g2 > 40**2
        isdiagonal = left == right
        all_tuples += 1
        product_diagonals += isdiagonal
        critical_diagonals += iscritical and isdiagonal
        if not iscritical:
            continue
        exponents = tuple((left[i]-right[i]) % 6 for i in range(8))
        principal = tuple(i for i in range(8)
                          if left[i]+right[i] and exponents[i] == 0)
        key = exponents, principal
        critical[key] += 1
        if len(set(t)) == 4:
            leading[key] += 1
    face.require((all_tuples, product_diagonals, critical_diagonals) == (4096, 120, 0),
                 'exact all-column census and disjoint product diagonal')
    face.require(sum(critical.values()) == 3696 and len(critical) == 1092,
                 'complete actual critical sector')
    face.require(sum(leading.values()) == 1680, 'complete leading subface')
    old_critical = old_leading = (0, 0)
    old_rows = [(a, b) for a in range(-8, 9) for b in range(-8, 9)
                if 0 < face.norm((a, b)) <= 40]
    face.require(len(old_rows) == 150 and 3*8**2 > 4*40, 'independent complete old row ball')
    for (es, masks), multiplicity in critical.items():
        trace = [0, 0]
        for row in old_rows:
            residues = [face.exponent(p, row) for p in primes]
            active = [i for i, e in enumerate(es) if e] + list(masks)
            if any(residues[i] is None for i in active):
                continue
            e = sum(es[i]*residues[i] for i in range(8) if es[i]) % 6
            a, b = face.UNITS[e]
            trace[0] += a
            trace[1] += b
        old_critical = tuple(x+mult*y for x, mult, y in
                             zip(old_critical, [multiplicity]*2, trace))
        old_leading = tuple(x+mult*y for x, mult, y in
                            zip(old_leading, [leading[es, masks]]*2, trace))
    face.require((old_critical, old_leading) == ((1176, 0), (456, 0)),
                 'generic masks/exponents reconstruct both exact old signed witnesses')
    cache = {}
    def weighted_orbits(denominator):
        if denominator not in cache:
            rows = []
            for h in face.representatives((denominator-1)//160):
                es = [face.exponent(p, h) for p in primes]
                rows.append((es, psi(face.norm(h), denominator)))
            cache[denominator] = rows
        return cache[denominator]
    total = lead = wrong_mask = acb(0)
    neutral = killed = 0
    neutral_ordered = 0
    records = []
    for (es, masks), multiplicity in sorted(critical.items()):
        if sum(e*p['charge'] for e, p in zip(es, primes)) % 6:
            killed += 1
            continue
        neutral += 1
        neutral_ordered += multiplicity
        support = [i for i, e in enumerate(es) if e]
        face.require(support, 'critical primitive part nonprincipal')
        q = (1, 0)
        for i in support:
            q = face.mul(q, primes[i]['generator'])
        nq = face.norm(q)
        gauss = acb(1)
        for i in support:
            other = (1, 0)
            for j in support:
                if i != j:
                    other = face.mul(other, primes[j]['generator'])
            residue = face.exponent(primes[i], other)
            face.require(residue is not None, 'primitive CRT factor')
            gauss *= gamma[i, es[i]]*zeta[(es[i]*residue) % 6]
        value = unmasked = acb(0)
        divisors = []
        for size in range(len(masks)+1):
            for selected in combinations(masks, size):
                d = (1, 0)
                for i in selected:
                    d = face.mul(d, primes[i]['generator'])
                nd = face.norm(d)
                local = 0
                for i in support:
                    exponent = face.exponent(primes[i], d)
                    face.require(exponent is not None, 'principal mask coprime to conductor')
                    local += es[i]*exponent
                a = b = arb(0)
                for residues, weight in weighted_orbits(nd*nq):
                    if any(residues[i] is None for i in support):
                        continue
                    exponent = -sum(es[i]*residues[i] for i in support) % 6
                    x, y = face.UNITS[exponent]
                    a += 6*x*weight
                    b += 6*y*weight
                summand = (-1)**size*zeta[local % 6]*(acb(a)+b*omega)/nd
                value += summand
                if size == 0:
                    unmasked += summand
                divisors.append(dict(prime_indices=list(selected), divisor_norm=nd))
        value *= arb(40)*gauss/arb(nq).sqrt()
        unmasked *= arb(40)*gauss/arb(nq).sqrt()
        total += multiplicity*value
        wrong_mask += multiplicity*unmasked
        lead += leading[es, masks]*value
        records.append(dict(exponents=list(es), principal_mask=list(masks),
                            primitive_conductor=list(q), primitive_norm=nq,
                            multiplicity=multiplicity, leading_multiplicity=leading[es, masks],
                            mask_divisors=divisors, row_trace_ball=value.str(50, more=True)))
    face.require((neutral, killed, neutral_ordered) == (178, 914, 568),
                 'full exact zero-charge projector')
    face.require(total.imag.contains(0) and lead.imag.contains(0), 'real total and leading trace')
    face.require(arb(8852) < total.real < arb(8853), 'strict full Fourier-compact native sign')
    face.require(arb(3916) < lead.real < arb(3917), 'independent generic full-sector leading reconstruction')
    face.require(abs(wrong_mask.real-total.real) > 1, 'principal zero masks materially retained')
    remainder = total-lead
    return dict(status='DIRECTED_FULL_SIGNED_COMPACT_NATIVE_PASS', precision_bits=192,
                D=30, H=40, tuple_count=all_tuples, critical_tuple_count=sum(critical.values()),
                critical_character_groups=len(critical), neutral_character_groups=neutral,
                killed_character_groups=killed, neutral_critical_ordered_tuples=neutral_ordered,
                critical_product_diagonals=critical_diagonals,
                full_signed_R2_ball=total.real.str(50, more=True),
                leading_R2_ball=lead.real.str(50, more=True),
                remaining_critical_ball=remainder.real.str(50, more=True),
                wrong_principal_mask_R2_ball=wrong_mask.real.str(50, more=True),
                Fourier_support_norm='1/4', records=records,
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                proof_sha256=hashlib.sha256((here/'FULL_SIGNED_COMPACT_WITNESS.md').read_bytes()).hexdigest(),
                face_helper_sha256=hashlib.sha256((here/'check_fourier_compact_trace.py').read_bytes()).hexdigest(),
                source_hashes=source_hashes, old_spatial_signed_R2=old_critical,
                old_spatial_leading_R2=old_leading,
                imported_Poisson_analysis_independently_rebuilt=False,
                asymptotic_generalized_moment_proved=False, rh_proved=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'records'}, indent=2))
