"""Exact finite checks for adaptive pressure assembly; not a P7/zero replay."""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import itertools
import json
from math import factorial, isqrt
from pathlib import Path

ALPHA, BETA, ELL = Q(1, 500), Q(19, 5000), 6


def require(value, message):
    if not value:
        raise ValueError(message)


def psi(t):
    t = Q(t)
    require(t >= 0, 'non-PSD spectral input')
    return (t-1)**2 if t <= 2 else 2*t-3


def sqrt_bounds(q, bits=256):
    q = Q(q)
    require(q >= 0 and bits > 0, 'invalid square root')
    scale = 1 << bits
    n = isqrt(q.numerator*scale*scale//q.denominator)
    lo = Q(n, scale)
    hi = lo if lo*lo == q else Q(n+1, scale)
    require(lo*lo <= q <= hi*hi, 'root enclosure')
    return lo, hi


def h0_bounds(terms=40):
    require(terms >= 2 and terms % 2 == 0, 'even Taylor cutoff required')
    c = sum(((-1)**j*Q(1, 2**j*factorial(2*j))
             for j in range(terms+1)), Q())
    s = sum(((-1)**j*Q(1, 2**j*factorial(2*j+1))
             for j in range(terms+1)), Q())
    ec = Q(1, 2**(terms+1)*factorial(2*terms+2))
    es = Q(1, 2**(terms+1)*factorial(2*terms+3))
    require(s-es > 0 and c-ec > 0, 'positive trigonometric division')
    # Complete alternating-series intervals: C in [c-ec,c], S in [s-es,s].
    return Q(3, 2)-c/(s-es), Q(3, 2)-(c-ec)/s


def decimal(q, places, upper=False):
    scale = 10**places
    n, d = q.numerator*scale, q.denominator
    k = -((-n)//d) if upper else n//d
    sign = '-' if k < 0 else ''
    k = abs(k)
    return sign + str(k//scale) + '.' + str(k % scale).zfill(places)


def enclosure(lo, hi, places=24):
    require(lo <= hi, 'reversed interval')
    a, b = decimal(lo, places), decimal(hi, places, True)
    require(Q(a) <= lo <= hi <= Q(b), 'decimal widening')
    return [a, b]


def constants():
    h0lo, h0hi = h0_bounds()
    slo, shi = sqrt_bounds(1+4*(ELL+1)*BETA)
    xlo, xhi = (1+slo)/2, (1+shi)/2
    require(BETA*h0lo > ALPHA and xlo > 1, 'positive gain regime')
    # H increases in H0 and decreases in x, since beta*H0 > alpha.
    fun = lambda x, h: (x*h-ALPHA)/(x-BETA)
    lo, hi = fun(xhi, h0lo), fun(xlo, h0hi)
    rlo, rhi = sqrt_bounds(Q(726237, 700000))
    clo, chi = 2*rlo-1+Q(2603,700000), 2*rhi-1+Q(2603,700000)
    oldlo = (h0lo-Q(279,140000))/(1-clo/280)
    oldhi = (h0hi-Q(279,140000))/(1-chi/280)
    base269lo = (1345000*h0lo-2680)/1340003
    base269hi = (1345000*h0hi-2680)/1340003
    kap = 1/(1+(ELL+1)*BETA)
    m = 1000000
    den = 1-kap*(BETA-(1+ELL*BETA)/m)
    finite_lo = (h0lo-kap*ALPHA*(1-Q(1,m)))/den
    finite_hi = (h0hi-kap*ALPHA*(1-Q(1,m)))/den
    require(lo > Q('0.6730441804347018'), 'new strict threshold')
    require(hi < Q('0.6730441804347019'), 'upper numeric calibration')
    require(oldhi < Q('0.6730096522791370'), 'old calibration')
    require(lo-oldhi > Q('0.0000345281555648'), 'strict improvement')
    require(finite_lo > Q('0.673043') > oldhi, 'fixed-cap improvement')
    require(Q('0.67') < h0lo < h0hi < Q('0.68'), 'H0 scale')
    # Check scalar derivative and optimum polynomial without floating point.
    a = (ELL+1)*BETA
    require(xlo*xlo-xlo-a <= 0 <= xhi*xhi-xhi-a, 'optimum root')
    return {
        'alpha':str(ALPHA), 'beta':str(BETA), 'window_loss':ELL,
        'h0':enclosure(h0lo,h0hi),
        'old_269':enclosure(base269lo,base269hi),
        'old_280':enclosure(oldlo,oldhi),
        'optimal_x':enclosure(xlo,xhi),
        'optimal_threshold':enclosure(xlo*xlo,xhi*xhi),
        'new_proportion':enclosure(lo,hi),
        'proportion_gain_over_280':enclosure(lo-oldhi,hi-oldlo),
        'percentage_point_gain_over_280':enclosure(100*(lo-oldhi),100*(hi-oldlo)),
        'fixed_outer_size':m, 'fixed_threshold':'1',
        'fixed_outer_proportion':enclosure(finite_lo,finite_hi),
        'sqrt_bits':256, 'alternating_cutoff':40,
    }


def greedy(points, alpha, beta, ell, c):
    """Incremental first crossings; the last unfinished block is separate."""
    require(alpha >= 0 and beta > 0 and ell >= 1 and c > 0, 'parameters')
    require(all(a <= b for a,b in zip(points, points[1:])), 'unordered points')
    start, pressure, blocks = 0, beta*(1-ell), []
    for j in range(len(points)):
        if j == start:
            pressure = beta*(1-ell)
        else:
            pressure += beta-alpha*(points[j]-points[j-1])
        if pressure >= c:
            blocks.append((start,j+1))
            start = j+1
    return blocks, (start,len(points))


def direct_blocks(points, alpha, beta, ell, c):
    """Independent direct span evaluation rather than incremental pressure."""
    blocks, start = [], 0
    while start < len(points):
        hits = [end for end in range(start+1,len(points)+1)
                if beta*(end-start-ell)-alpha*(points[end-1]-points[start]) >= c]
        if not hits:
            break
        end = hits[0]
        blocks.append((start,end))
        start = end
    return blocks,(start,len(points))


def check_partition(points, alpha, beta, ell, c, independent=True):
    closed, rest = greedy(points,alpha,beta,ell,c)
    if independent:
        require((closed,rest) == direct_blocks(points,alpha,beta,ell,c),
                'first crossing implementation mismatch')
    allblocks = closed+([rest] if rest[0] != rest[1] else [])
    flat = [j for a,b in allblocks for j in range(a,b)]
    require(flat == list(range(len(points))), 'missing/repeated point')
    raw_sum, cut_sum = Q(), Q()
    for i,(a,b) in enumerate(allblocks):
        span = points[b-1]-points[a]
        p = beta*(b-a-ell)-alpha*span
        if i < len(closed):
            require(c <= p < c+beta, 'crossing or overshoot')
            require(all(beta*(j-a+1-ell)-alpha*(points[j]-points[a]) < c
                        for j in range(a,b-1)), 'not first crossing')
        else:
            require(p < c, 'invalid unfinished block')
        raw_sum += beta*(b-a)-alpha*span
        if i:
            cut_sum += points[a]-points[allblocks[i-1][1]-1]
    span = points[-1]-points[0] if points else Q()
    raw = beta*len(points)-alpha*span
    require(raw == raw_sum-alpha*cut_sum, 'cut-gap accounting')
    require(raw <= len(closed)*(c+(ell+1)*beta)+c+ell*beta,
            'global raw-pressure bound')
    return len(closed)


def partition_controls():
    total, successes, native, cap_cases = 0, 0, 0, 0
    alphabet = (Q(0),Q(1),Q(5))
    for ell in (1,2):
        for length in range(8):
            for gaps in itertools.product(alphabet, repeat=length):
                points = [Q()]
                for g in gaps:
                    points.append(points[-1]+g)
                successes += check_partition(points,Q(1,4),Q(1,2),ell,Q(1))
                total += 1
    check_partition([], ALPHA,BETA,ELL,Q(1))
    profiles = [(Q(0),),(Q(1),),(Q(3,2),),(Q(2),),(Q(3),),
                (Q(0),Q(1),Q(5)),(Q(1),)*300+(Q(10000),)+(Q(0),)*300,
                (Q(1),Q(0),Q(2),Q(1),Q(30))]
    for profile in profiles:
        for c in (Q(1),Q(21,20),Q(263,250)):
            points = [Q()]
            for j in range(1800):
                points.append(points[-1]+profile[j % len(profile)])
            check_partition(points,ALPHA,BETA,ELL,c,independent=False)
            # Direct checking of a shorter prefix covers tails and first hits.
            check_partition(points[:650],ALPHA,BETA,ELL,c)
            native += 1
    # Every outer offset: no gap may be charged more than M-1 times.
    for size in range(0,41):
        for m in range(1,12):
            charge = [0]*max(0,size-1)
            for offset in range(m):
                used = 0
                for a in range(offset,size-m+1,m):
                    used += m
                    for j in range(a,a+m-1):
                        charge[j] += 1
                require(size-used <= 2*m, 'outer discarded-point budget')
            require(all(v <= m-1 for v in charge), 'outer span charge')
            cap_cases += 1
    return {'exhaustive_small_gap_lists':total,
            'closed_blocks_in_small_tests':successes,
            'native_constant_profiles':native,
            'outer_size_offset_panels':cap_cases,
            'these_are_zeta_zero_configurations':False}


def spectral_controls():
    spectral, pinched = 0,0
    # Rational spectra with four nonnegative eigenvalues summing to four.
    walsh = ((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
    pairings = (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
    for a in range(17):
        for b in range(17-a):
            for c in range(17-a-b):
                eig = [Q(v,4) for v in (a,b,c,16-a-b-c)]
                energy = sum(((v-1)**2 for v in eig),Q())
                defect = sum((psi(v) for v in eig),Q())
                if energy <= 1:
                    require(defect >= energy, 'small-energy envelope')
                else:
                    require(defect+1 >= 0 and (defect+1)**2 >= 4*energy,
                            'global square-root envelope')
                gram = [[sum((Q(walsh[i][k]*walsh[j][k],4)*eig[k]
                              for k in range(4)),Q()) for j in range(4)] for i in range(4)]
                require(all(gram[i][i] == 1 for i in range(4)), 'unit diagonal')
                for partition in pairings:
                    rhs = sum((psi(1+gram[i][j])+psi(1-gram[i][j])
                               for i,j in partition),Q())
                    require(defect >= rhs, 'two-by-two pinching')
                    pinched += 1
                spectral += 1
    # Independent scalar checks of concavity-to-subadditivity on perfect squares.
    ph = lambda x: x if x <= 1 else 2*sqrt_bounds(x)[0]-1
    scalar = 0
    for i in range(21):
        for j in range(21):
            a,b = Q(i*i,16),Q(j*j,16)
            l,r = sqrt_bounds(a+b)
            upper_sum = a+b if a+b <= 1 else 2*r-1
            # Perfect-square a,b make ph exact. With a+b a square, upper is exact.
            require(ph(a)+ph(b) >= upper_sum or
                    ph(a)+ph(b)+1 >= 0 and (ph(a)+ph(b)+1)**2 >= 4*(a+b),
                    'scalar subadditivity')
            scalar += 1
    return {'four_point_spectra':spectral,'exact_pinching_panels':pinched,
            'scalar_subadditivity_panels':scalar,
            'these_are_native_gram_computations':False}


def reconstruct():
    require(ALPHA == Q(1,500) and BETA == Q(19,5000) and ELL == 6,
            'wrong imported pressure normalization')
    return {'schema':'adaptive-pressure-v1',
            'status':'PROPOSED_DEDUCTION_FROM_EXPLICIT_INPUTS',
            'rh_proved':False,'seven_gap_replayed':False,
            'external_analytic_inputs_reproved':False,
            'native_zero_computation':False,
            'constants':constants(),
            'partitions':partition_controls(),
            'spectral_controls':spectral_controls()}


def reject_float(_):
    raise ValueError('floating JSON numbers are not accepted')


def unique_pairs(pairs):
    out = {}
    for k,v in pairs:
        if k in out:
            raise ValueError('duplicate JSON key')
        out[k] = v
    return out


def load(path):
    return json.loads(path.read_text(encoding='utf-8'),
                      object_pairs_hook=unique_pairs,
                      parse_float=reject_float, parse_constant=reject_float)


def canonical(data):
    return json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=True)


def compare(path, expected):
    # Serialized typed equality avoids Python's True == 1 alias.
    require(canonical(load(path)) == canonical(expected),
            'receipt differs from complete exact reconstruction')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path)
    g.add_argument('--check',type=Path)
    a = p.parse_args()
    result = reconstruct()
    if a.write:
        a.write.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    else:
        compare(a.check,result)
    print('PASS_ADAPTIVE_FINITE_DEDUCTION_NOT_A_P7_OR_ZETA_REPLAY')


if __name__ == '__main__':
    main()
