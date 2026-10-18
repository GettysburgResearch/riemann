#!/usr/bin/env python3
"""Exact finite regressions for a WRITTEN analytic argument, not a proof assistant.

No actual Hecke values, zeta zeros, or asymptotic analytic estimates are computed.
Only Fraction/integer arithmetic is used; checks survive python -O.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MUTATIONS = (
    'lost_replica_floor', 'upper_threshold_count', 'moving_density_loss',
    'insufficient_line_buffer', 'touching_log_boundary', 'omit_small_cores',
    'erased_nonunit_mask', 'zero_tail_height', 'fixed_order_substitution',
)

def density(s: F) -> F:
    if s <= F(11, 12):
        return 1-(2*s-1)*(36*(2*s-1)-6*(6*s-2)+3)/(36*(2*s-1)*(3-2*s)-24*s+2)
    return 1-(8*s*s-10*s+3)/(1-24*(1-s)**2)

def factor(n: int) -> dict[int, int]:
    d: dict[int, int] = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            d[q] = d.get(q, 0)+1
            n //= q
        q += 1
    if n > 1:
        d[n] = d.get(n, 0)+1
    return d

def divisors(n: int) -> list[int]:
    ds = [1]
    for q, e in factor(n).items():
        ds = [d*q**j for d in ds for j in range(e+1)]
    return sorted(ds)

def sf_divisors(n: int) -> list[int]:
    ds = [1]
    for q in factor(n):
        ds += [d*q for d in ds]
    return sorted(ds)

def moment_mask(n: int, p: int) -> F:
    result = F(1)
    for q in factor(n):
        result *= F(q, q-1)**p
    return result

def run(mutation: str | None = None) -> dict:
    counts: Counter[str] = Counter()
    def need(group: str, condition: bool, message: str) -> None:
        counts[group] += 1
        if not condition:
            raise ValueError(f'{group}: {message}')

    raw = (ROOT/'DENSITY_CERTIFICATE.json').read_bytes()
    cert = json.loads(raw)
    theta, floor = F(31, 32), F(1, 6)
    gamma, eta, buf = F(1, 400), F(1, 100000), F(1, 100000)
    rows = [(F(s), F(g)) for s, g in cert['rows']]
    need('certificate', len(rows) == 53, 'all inherited thresholds must remain')
    need('certificate', rows[0][0] == F(3, 4), 'first threshold')
    need('certificate', rows[-1][0] == F(121, 125), 'last threshold')
    need('certificate', F(cert['theta']) == theta and F(cert['floor']) == floor, 'input pins')
    margins = []
    for i, (s, g) in enumerate(rows):
        need('density', density(s) == g, f'wrong density at row {i}')
        need('density', F(1, 2) < s < theta and 0 <= g <= 1, 'density domain')
        if i+1 < len(rows):
            need('density', s < rows[i+1][0], 'strict threshold ordering')
            assigned = rows[i+1][1] if mutation == 'upper_threshold_count' else g
            need('selected_count', assigned == g, 'a middle class is counted at its LOWER threshold')
            mg = floor+4*theta-max(g, floor)-4*rows[i+1][0]
            margins.append(mg)
            need('margin', mg > gamma, 'fixed middle margin')
            # This coefficient is valid for every real p>0 after H<=D^(p/4).
            effective = theta-(rows[i+1][0]+buf+(max(g-floor, F(0))+2*eta)/4)
            need('uniform_budget', effective >= gamma/8, 'losses erase the middle saving')
    need('certificate', [str(x) for x in margins] == cert['middle_margins'], 'full margin report')
    need('certificate', min(margins) == F('9387546301/3528153375000'), 'minimum')
    need('margin', floor+4*theta-(1+4*rows[0][0]) == F(1, 24), 'good margin')
    need('uniform_budget', theta-(rows[0][0]+buf+(1-floor+2*eta)/4) >= gamma/8, 'good budget')
    need('margin', floor-rows[-1][1] == F(313, 91446) > gamma, 'terminal gap')
    need('uniform_budget', rows[-1][1]-floor+2*eta < -gamma/2, 'terminal series must converge')
    need('uniform_budget', buf+eta/2 < gamma/8, 'fixed line/density loss')
    left = 1-(2*F(11,12)-1)*(36*(2*F(11,12)-1)-6*(6*F(11,12)-2)+3)/(36*(2*F(11,12)-1)*(3-2*F(11,12))-24*F(11,12)+2)
    right = 1-(8*F(11,12)**2-10*F(11,12)+3)/(1-24*(1-F(11,12))**2)
    need('density', left == right, 'density branches must agree')

    # Affine margins: positive at both endpoints or zero only at excluded delta=0.
    delta_max = F(1, 1024)
    for s in [theta]+[x[0] for x in rows]:
        at = []
        for d in [F(0), delta_max]:
            R, ro, rt, ri = 2-s-d/8, 2-s-d/4, 2-s-d, 1-d/8
            if mutation == 'touching_log_boundary':
                rt = ro
            at.append([R-ro, ro-rt, rt-ri, ri, 2-ro, 2*ri-ro, 1-s-d])
        for j in range(7):
            need('disc_intervals', at[0][j] >= 0 and at[1][j] > 0,
                 f'disc margin {j} fails on the whole delta interval')
        for d in [F(1, 4096), F(1, 2048), delta_max]:
            ro, rt, ri = 2-s-d/4, 2-s-d, 1-d/8
            # log(ro/rt)>= (ro-rt)/ro; log(ro/ri)<1 follows from ro<2ri.
            need('three_circles', (ro-rt)/ro >= 3*d/8 >= d/10,
                 'three-circle interpolation gap')

    # Density epsilon is fixed ONCE, including as p varies.
    for p in [F(1), F(3,2), F(2), F(4), F(16), F(128)]:
        used_eta = eta/p if mutation == 'moving_density_loss' else eta
        need('fixed_quantifiers', used_eta == eta, 'uncontrolled density constant at eta/p')

    # Uniform asymptotic identities: with ell=exp(m), not fitted samples of D.
    line_constant = F(20 if mutation == 'insufficient_line_buffer' else 100)
    rate_power = 3-line_constant/20  # p delta^-2 * t^-delta/10, t>=sqrt(L)/2.
    need('asymptotic_algebra', rate_power <= -1,
         'large-core reciprocal loss fails to vanish uniformly')
    need('asymptotic_algebra', line_constant == 100, 'declared explicit contour schedule')
    for ell, m in [(F(1000),F(10)),(F(10000),F(15)),(F(1000000),F(20))]:
        d = line_constant*m/ell
        p = ell/m
        need('schedule_identities', p*d*d**-2 == p/d, 'positive powers algebra')
        need('schedule_identities', p*d**-2 == ell**3/(line_constant**2*m**3), 'exact uniform prefactor')
        need('schedule_identities', (ell/m**2)*d == line_constant/m, 'explicit smaller range')
    # Exponents of L in every residual are strictly <3/4; log-powers have fixed degrees.
    residual_terms = {'small_count':F(1,2), 'moving_envelope':F(1,2),
                      'height_integral':F(0), 'mask_mass':F(0),
                      'dyadic_log':F(0), 'finite_constants':F(0)}
    for name, power in residual_terms.items():
        need('asymptotic_algebra', power < F(3,4), f'{name} not absorbed by exp(L^3/4)')
    rho = F(0) if mutation == 'zero_tail_height' else F(1, 1000000)
    need('tail_contract', rho > 0, 'constant-height tail cannot absorb log(D)')
    need('tail_contract', 2*rho > 0, 'exp(2rho log U) must dominate a quadratic in log U')
    need('tail_contract', 2*4 == 8, 'D^2 tail when logD<=4(logU)^2')

    # Synthetic complete core partition, explicitly not actual zeros.
    small_cutoff = 16
    full = set(range(1, 101))
    small = set() if mutation == 'omit_small_cores' else set(range(1,small_cutoff))
    large = {a for a in full if a >= small_cutoff}
    need('coverage', not small & large and small | large == full,
         'small fixed cores cannot be discarded')
    for j in range(54):
        assigned = ('good' if j == 0 else ('terminal' if j == 53 else 'middle'))
        need('coverage', assigned in ('good','middle','terminal'), 'finite class labels')

    # Literal integer sixth-power decomposition and nonunit-mask algebra.
    for u in range(1, 257):
        a = b0 = 1
        for q,e in factor(u).items():
            a *= q**(e%6)
            b0 *= q**(e//6)
        need('row_identity', a*b0**6 == u and all(e<6 for e in factor(a).values()), 'full decomposition')
    for a,b0 in [(1,1),(1,2),(2,2),(6,6),(4,2),(9,3),(6,2),(3,2)]:
        for n in range(1, 17):
            from math import gcd
            lhs = int(gcd(a*b0**6,n)==1)
            rhs = int(gcd(a,n)==1)*(1 if mutation == 'erased_nonunit_mask' else int(gcd(b0,n)==1))
            need('nonunit_mask', lhs == rhs, 'original nonunit zero lost')

    # Real-order proof is in the paper; these are exact integer-order Euler fixtures.
    for p in [1,2,4,8,12]:
        for n in range(1,65):
            conv = F(0)
            for d in sf_divisors(n):
                term = F(1)
                for q in factor(d):
                    term *= F(q,q-1)**p-1
                conv += term
            need('mask_divisor', conv == moment_mask(n,p), 'nonnegative Euler expansion')
        N=64
        direct=sum((moment_mask(n,p) for n in range(1,N+1)),F(0))
        rearranged=F(0)
        for d in range(1,N+1):
            if any(e>1 for e in factor(d).values()):continue
            gd=F(1)
            for q in factor(d):gd*=F(q,q-1)**p-1
            rearranged+=gd*(N//d)
        need('mask_average', direct==rearranged, 'whole finite mask average')

    # A singleton fixed core can have B replicas; retaining only H^g for g<1/6 fails.
    for B in [2,3,5,10]:
        H=B**6
        count=sum(b**6<=H for b in range(1,B+1))
        model_bound = 1 if mutation == 'lost_replica_floor' else B
        need('replica_floor', count <= model_bound, 'H^(1/6) repeated family was deleted')

    # Fixed-p constants do not imply growing-p uniformity: at p^2=ell, log C_p=L.
    # This exact normalized exponent identity needs no numerical exp/log calculation.
    toy_extra_power = F(0) if mutation == 'fixed_order_substitution' else F(1)
    need('quantifier_countermodel', toy_extra_power == 1,
         'exp(exp(p^2)) becomes D, not D^o(1), on the moving diagonal')
    need('target_gap', theta-F(1,2) == F(15,32), 'critical gap is not removed')
    need('localization', F(1,20000) < gamma/32, 'advertised localization constant too large')

    return {'status':'PASS','finite_predicates':sum(counts.values()),
            'checks_by_group':dict(sorted(counts.items())),
            'thresholds':len(rows),'middle_classes':len(rows)-1,'all_classes':len(rows)+1,
            'minimum_middle_margin':str(min(margins)),
            'moving_line_constant':str(line_constant),
            'uniform_large_core_log_power':str(rate_power),
            'density_certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'actual_Hecke_values_or_zeros':0,
            'scope':'Exact finite algebra and proof-interface regressions; not asymptotic or analytic certification.'}

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mutation',choices=MUTATIONS)
    args=ap.parse_args()
    print(json.dumps(run(args.mutation),indent=2,sort_keys=True))

if __name__=='__main__':
    main()
