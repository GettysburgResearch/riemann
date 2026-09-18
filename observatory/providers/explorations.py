"""Small, explicit family/sequence providers and bounded point refinement."""
from __future__ import annotations
import importlib.util
import math
import numpy as np


def refine(q, ctx):
    from engine import evaluator
    if q.backend == 'flint':
        if importlib.util.find_spec('flint') is None:
            raise ValueError('Optional python-flint is not installed. Use mpmath or install requirements-flint.txt.')
        # Never silently replace a requested enclosure with a floating estimate.
        from flint import acb, arb, ctx as fctx
        import flint
        if q.function != 'zeta':
            raise ValueError('The optional ball provider currently supports zeta point evaluations only.')
        with fctx.workdps(q.dps):
            s = acb(arb(q.real), arb(q.imag))
            value = s.zeta()
            if not value.is_finite():
                raise ValueError('FLINT returned an indeterminate enclosure (for example at the pole).')
            re = value.real.str(q.dps, radius=True, more=True)
            im = value.imag.str(q.dps, radius=True, more=True)
            # String round-trip must enclose the computed balls, including decimal printing error.
            if not arb(re).contains(value.real) or not arb(im).contains(value.imag):
                raise ValueError('Ball string round-trip did not preserve containment; refusing serialization.')
            details = {'real_ball': re, 'imag_ball': im, 'input_real_ball': s.real.str(q.dps, radius=True, more=True),
                       'input_imag_ball': s.imag.str(q.dps, radius=True, more=True),
                       'library': f'python-flint {flint.__version__}', 'roundtrip_containment_checked': True}
        evidence = 'FLINT point enclosure; not a region/census certificate'
        warnings = ['Enclosure concerns this single input rectangle and zeta value, not a grid cell, contour, root isolation or RH.',
                    'Decimal input and printed output uncertainty are included in the serialized balls. Optional provider requires native FLINT acceptance tests.']
    else:
        s = ctx.mpc(q.real, q.imag)
        value = evaluator(ctx, q.function, s)
        if not ctx.isfinite(value):
            raise ValueError('Point is a pole or the value is nonfinite.')
        low = ctx.clone()
        low.dps = max(20, q.dps-20)
        coarse = evaluator(low, q.function, low.mpc(q.real, q.imag))
        difference = abs(value-ctx.mpc(coarse))
        details = {'real': ctx.nstr(value.real, q.dps), 'imag': ctx.nstr(value.imag, q.dps),
                   'modulus': ctx.nstr(abs(value), q.dps), 'precision_change': ctx.nstr(difference, 12),
                   'coarse_dps': low.dps, 'fine_dps': q.dps}
        evidence = 'ordinary high-precision point scout; not certified'
        warnings = ['A difference between two ordinary precisions is NOT an error bound.',
                    'Input decimal strings reach the evaluator directly; no intermediate binary64 coordinate conversion.']
    return {'series': [], 'events': [], 'point': details, 'evidence': evidence,
            'metrics': details, 'formula': f'{q.function}({q.real} + i({q.imag}))', 'warnings': warnings}


def jacobi(a, odd_n):
    if odd_n <= 0 or odd_n % 2 == 0:
        raise ValueError('Jacobi denominator must be positive and odd')
    a, sign = a % odd_n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if odd_n % 8 in (3, 5):
                sign = -sign
        a, odd_n = odd_n, a
        if a % 4 == odd_n % 4 == 3:
            sign = -sign
        a %= odd_n
    return sign if odd_n == 1 else 0


def kronecker_positive_n(D, n):
    """(D/n) for positive n; sufficient for positive-index character tables."""
    if n <= 0:
        raise ValueError('Expected positive denominator')
    sign = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            sign = -sign
    return sign*jacobi(D, n)


def character_table(D, multiplier=1):
    conductor, modulus = abs(D), abs(D)*multiplier
    # All allowed D are nontrivial fundamental discriminants; conductor=|D|.
    return [0] + [kronecker_positive_n(D, n) if math.gcd(n, modulus)==1 else 0
                  for n in range(1, modulus)]


def family(q, ctx):
    from engine import series, sieve
    ts = np.linspace(q.t_min, q.t_max, q.samples).tolist()
    curves, metadata = [], []
    for D in q.discriminants:
        conductor, modulus = abs(D), abs(D)*q.multiplier
        primitive = character_table(D)
        table = character_table(D, q.multiplier)
        vals = [ctx.dirichlet(ctx.mpc(str(q.sigma), str(t)), table) for t in ts]
        curves.append(series(f'|L(χ_{D},s)| · modulus {modulus}', ts, [float(abs(v)) for v in vals], q.samples))
        # Independently evaluate induction at one point and compare the missing local factors.
        s = ctx.mpc(str(q.sigma), str(ts[len(ts)//2]))
        parent = ctx.dirichlet(s, primitive)
        factor, removed = ctx.mpc(1), []
        for prime in sieve(modulus)[0]:
            if modulus % prime == 0 and conductor % prime != 0:
                factor *= 1-kronecker_positive_n(D, prime)*ctx.power(prime, -s)
                removed.append(prime)
        mismatch = abs(ctx.dirichlet(s, table)-parent*factor)
        metadata.append({'D': D, 'conductor': conductor, 'modulus': modulus,
                         'primitive': q.multiplier==1, 'parity': 0 if D>0 else 1,
                         'character_table': table, 'definition': 'χ_D(n)=(D/n), induced by zeroing nonunits of the displayed modulus.',
                         'central_value_s_half': ctx.nstr(ctx.dirichlet(ctx.mpf('0.5'), table), q.dps),
                         'removed_euler_primes': removed, 'induction_residual_at_midpoint': ctx.nstr(mismatch, 10),
                         'completion_convention': 'Primitive parent: (|D|/π)^((s+parity)/2) Γ((s+parity)/2)L(s). Do not complete an induced member using its larger modulus as conductor.'})
    return {'series': curves, 'events': [], 'members': metadata,
            'metrics': {'members': len(metadata), 'samples_per_member': q.samples},
            'formula': 'Real quadratic Dirichlet families from explicitly listed fundamental discriminants; L_induced(s)=L_primitive(s)∏[p|modulus,p∤conductor](1−χ_D(p)p^(−s)).',
            'warnings': ['Only this bounded quadratic family is implemented; this is not an arbitrary-character database.',
                         'Central values are numerical evaluations at s=1/2, NOT arithmetic ranks or certified vanishing orders.',
                         'Raw t coordinates are shared. No universal random-matrix ensemble or asymptotic unfolding is assumed.',
                         'Completion metadata belongs to the primitive parent. The plotted function is the displayed member, not the completion.'],
            'sources': ['https://dlmf.nist.gov/27.8', 'https://dlmf.nist.gov/25.15']}


def hierarchy(q, ctx):
    from engine import sieve, series
    primes, _ = sieve(q.limit)
    prime_set = set(primes)
    arrays, family_members = [], []
    current = list(range(1, q.limit+1))
    x = list(range(1, q.limit+1))
    for depth in range(q.depth+1):
        if depth:
            # Ranks are 1-based within the previous sequence, not ranks in the integers.
            current = [v for rank, v in enumerate(current, 1) if rank in prime_set]
        members = set(current)
        count, harmonic = 0, 0.0
        counts, sums = [], []
        for i in x:
            if i in members:
                count += 1
                harmonic += 1/i
            counts.append(count)
            sums.append(harmonic)
        label = 'Integers' if depth==0 else f'Prime-index selection ×{depth}'
        arrays.append(series(label+' · reciprocal sum', x, sums, q.buckets))
        family_members.append({'depth': depth, 'count': count, 'harmonic_sum': harmonic,
                               'initial_members': current[:32], 'last_member': current[-1] if current else None,
                               'count_curve': series(label+' · count', x, counts, q.buckets)})
    fractional = np.arange(1, q.limit+1, dtype=float)**(-q.alpha)
    fsums = np.cumsum(fractional).tolist()
    return {'series': arrays, 'events': [], 'families': family_members,
            'fractional': {'alpha': q.alpha, 'series': series(f'Σ[n≤N] n^(−{q.alpha})', x, fsums, q.buckets),
                           'last_index': q.limit, 'last_value_a_N': q.limit**q.alpha,
                           'coordinate': 'N is an INDEX cutoff; a_N=N^alpha. This is not the same x cutoff as the integer-family panels.'},
            'metrics': {'integer_cutoff': q.limit, 'selection_depth': q.depth,
                        'fractional_index_sum': fsums[-1], 'fractional_value_cutoff': q.limit**q.alpha},
            'formula': 'A₀=(1,2,3,…); A_(d+1)={the p-th member of A_d : p prime}. H_d(x)=Σ[a∈A_d,a≤x]1/a. Separate fractional sequence: a_n=n^α.',
            'warnings': ['Every sequence is explicitly constructed. Finite curves do not establish iterated-log asymptotics or an RH equivalence.',
                         'Repeated prime-index selection is NOT the Golomb–Erdős self-sieve or a residue-avoidance sieve.',
                         'Reciprocal sums are floating additions over an exact finite membership sieve. No infinite Euler product or analytic continuation is inferred.']}
