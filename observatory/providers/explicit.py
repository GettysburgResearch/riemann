"""One Gaussian Weil explicit formula, with conventions and omissions exposed.

h(t)=exp(-a*t*t)*cos(b*t), H(u)=integral_R h(t)exp(-i*u*t)dt.
See docs/EXPLICIT_FORMULA.md for the exact infinite identity and scope.
"""
from __future__ import annotations
import math
from functools import lru_cache
import numpy as np
from scipy.special import digamma


def transform(a, b, u):
    """Unnormalized angular-frequency Fourier transform of the even test h."""
    u = np.asarray(u)
    return math.sqrt(math.pi/a)/2*(np.exp(-(u-b)**2/(4*a))+np.exp(-(u+b)**2/(4*a)))

@lru_cache(maxsize=12)
def quadrature(cutoff, order):
    # At most unit-length panels; tests compare independent integration and order.
    breaks = np.linspace(0, cutoff, math.ceil(cutoff)+1)
    nodes, weights = np.polynomial.legendre.leggauss(order)
    half = np.diff(breaks)/2
    t = ((breaks[:-1]+breaks[1:])[:, None]/2+half[:, None]*nodes).ravel()
    w = (half[:, None]*np.broadcast_to(weights, (len(half), len(weights)))).ravel()
    return t, w, np.real(digamma(0.25+0.5j*t))

def gamma_integral(a, bs, cutoff, order):
    t, w, psi = quadrature(cutoff, order)
    return np.cos(np.asarray(bs)[:, None]*t) @ (w*np.exp(-a*t*t)*psi)/math.pi

def prime_powers(cutoff):
    from engine import sieve
    primes, _ = sieve(cutoff)
    rows = []
    for prime in primes:
        n, power = prime, 1
        while n <= cutoff:
            rows.append((n, prime, power, math.log(prime)))
            n *= prime
            power += 1
    return sorted(rows)

def explicit(q, ctx):
    from engine import series
    bs = np.linspace(q.b_min, q.b_max, q.samples)
    pp = prime_powers(q.prime_cutoff)
    ns = np.array([v[0] for v in pp], dtype=float)
    logs, weights = np.log(ns), np.array([v[3] for v in pp])/np.sqrt(ns)
    gammas_mp = [ctx.im(ctx.zetazero(k)) for k in range(1, q.zero_count+1)]
    gammas = np.array([float(g) for g in gammas_mp])
    gweights = 2*np.exp(-q.a*gammas**2)
    spectral_parts = np.cos(bs[:, None]*gammas)*gweights
    zsum = spectral_parts.sum(axis=1)
    band = spectral_parts[:, q.band_first-1:q.band_last].sum(axis=1)
    pole = 2*math.exp(q.a/4)*np.cosh(bs/2)
    logpi = -math.log(math.pi)/(2*math.pi)*transform(q.a, bs, 0)
    arch = gamma_integral(q.a, bs, q.gamma_cutoff, q.quadrature_order)
    # Loop over b avoids a large prime-count x screen-width temporary.
    psum = np.array([np.dot(weights, transform(q.a, b, logs))/math.pi for b in bs])
    rhs = pole+logpi+arch-psum
    focus = q.focus_b
    fpole = 2*math.exp(q.a/4)*math.cosh(focus/2)
    flogpi = -math.log(math.pi)/(2*math.pi)*float(transform(q.a, focus, 0))
    farch = float(gamma_integral(q.a, [focus], q.gamma_cutoff, q.quadrature_order)[0])
    check_order = q.quadrature_order+8
    fcheck = float(gamma_integral(q.a, [focus], q.gamma_cutoff, check_order)[0])
    prime_terms = -weights*transform(q.a, focus, logs)/math.pi
    zero_terms = gweights*np.cos(focus*gammas)
    fprime, fzero = math.fsum(prime_terms.tolist()), math.fsum(zero_terms.tolist())
    frhs = math.fsum([fpole, flogpi, farch, fprime])
    cutoffs = sorted(set([max(2, q.prime_cutoff//4), max(2, q.prime_cutoff//2), q.prime_cutoff]))
    ladder = [{'prime_cutoff': c, 'prime_term': math.fsum(prime_terms[ns<=c].tolist())} for c in cutoffs]
    zero_ladder = [{'zero_count': k, 'zero_term': math.fsum(zero_terms[:k].tolist())}
                   for k in sorted(set([2, max(2, q.zero_count//2), q.zero_count]))]
    return {
        'series': [series(label, bs.tolist(), values.tolist(), q.samples) for label, values in [
            ('Selected numerical zero sum Z_K', zsum), ('Pole + logπ + gamma − prime sum', rhs),
            ('Finite discrepancy RHS − Z_K', rhs-zsum), ('Selected zero-band contribution', band),
            ('Pole terms', pole), ('−logπ term', logpi), ('Gamma integral, truncated', arch), ('−Prime-power sum, truncated', -psum)]],
        'events': [{'x0': focus, 'x1': focus, 'kind': 'focused log-center b', 'status': 'selected'}],
        'focus': {'b': focus, 'x': math.exp(focus), 'pole': fpole, 'logpi': flogpi,
                  'gamma': farch, 'prime': fprime, 'rhs': frhs, 'zeros': fzero,
                  'discrepancy': frhs-fzero, 'quadrature_order_change': fcheck-farch,
                  'prime_terms': [{'n': row[0], 'prime': row[1], 'power': row[2], 'log_prime': row[3],
                                   'contribution': float(v)} for row, v in zip(pp, prime_terms)],
                  'zero_terms': [{'index': i+1, 'gamma': ctx.nstr(g, q.dps),
                                  'contribution': float(zero_terms[i])} for i, g in enumerate(gammas_mp)]},
        'cutoff_checks': {'prime': ladder, 'zeros': zero_ladder},
        'boundaries': {'prime_powers': f'All p^k <= {q.prime_cutoff}, including prime powers k>1.',
                       'zeros': f'First {q.zero_count} mpmath indexed positive critical-line ordinates, mirrored with factor 2; approximate, no census certificate.',
                       'gamma_integral': f'Even integral restricted to |t| <= {q.gamma_cutoff}; composite Gauss–Legendre order {q.quadrature_order} per unit-length panel.',
                       'trivial_zeros': 'Already encoded by the gamma factor in this completed-zeta convention; DO NOT add a separate trivial-zero sum.',
                       'prime_tail_bound': None, 'zero_tail_bound': None, 'gamma_tail_bound': None,
                       'rounding_bound': None, 'quadrature_error_bound': None},
        'metrics': {'focus_discrepancy': frhs-fzero, 'prime_powers_used': len(pp), 'zero_pairs_used': len(gammas),
                    'focus_quadrature_change': fcheck-farch, 'max_sampled_discrepancy': float(np.max(abs(rhs-zsum)))},
        'formula': 'h(t)=exp(−a t²) cos(bt); H(u)=∫h(t)e^(−iut)dt. Σρ h((ρ−1/2)/i)=2e^(a/4)cosh(b/2)−log(π)H(0)/(2π)+(1/(2π))∫h(t)Re ψ(1/4+it/2)dt−(1/π)Σn Λ(n)H(log n)/√n.',
        'warnings': ['This is one specified Gaussian Weil identity, NOT a fitted prime/zero relationship. The infinite identity uses ALL nontrivial zeros with multiplicity; off-line zeros require the complex argument (ρ−1/2)/i.',
                     'The displayed zero side contains only the returned approximate critical-line zeros. No global RH assumption or certified completeness is used to relabel that finite list.',
                     'All five omitted/error budgets are UNKNOWN (null), not zero. Agreement of finite sides is a diagnostic, not a certificate or proof.',
                     'Working digits affect the numerical zero ordinates; transforms, digamma integration, curves and residuals use binary64. Increasing digits does not certify the residual.',
                     'Changing quadrature order is a numerical consistency check, not a rigorous error enclosure. Smooth tests have no prime endpoint half-weight: every p^k<=N is included.'],
        'sources': ['https://dlmf.nist.gov/25.4', 'https://dlmf.nist.gov/25.2',
                    'https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.digamma.html']}
