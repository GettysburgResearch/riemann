"""O1 round 2: local (Kazhdan-Patterson / Hoffstein) Hecke relations vs explicit coefficient shapes.
Floating point, finite; direct Gauss sums via a2/eis.py.
(H3) n = 3 (Patterson, unique model): the Hecke relation tau(m) = G1(m,p) tau(mp) forces
     tau(mp)/tau(m) = conj G1(m,p) = chi_p(m)^2 conj gamma_2(p)   [cubic symbol = chi^2 in sextic units].
     Check that Patterson's shape T(n) = conj gamma_2(n) obeys it at composites:  T(mp) / (T(m) conj G1(m,p)) == 1.
(H6) n = 6, (S6) shape T(n) = gamma_{-1}(n) (times a Hecke character).  The Hecke relation
     tau(mp) = G2(m,p) tau(mp^3), G2(m,p) = conj chi_p(m)^2 gamma_2(p), then DEFINES tau(mp^3); check
     tau(mp^3)/tau(m) := T(mp)/(T(m) G2(m,p)) == -chi_p(16) G(p)/alpha(p) * chi_p(m) conj chi_m(p),
     i.e. (S6) <=> cube-index coefficients = mu(p) x (Hecke x ray)(p) x reciprocity sign.
Usage: python3 local_hecke_check.py OUT.json
"""
import sys, os, json, math, cmath, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'a2'))
import eis
Z = [cmath.exp(1j*math.pi*k/3) for k in range(6)]
def chiv(fs, u):
    k = eis.chi(fs, u); return 0 if k is None else Z[k]
def elem(fs):
    n = (1, 0)
    for p in fs: n = eis.mul(n, p)
    return n
def alpha(fs):
    n = elem(fs); z = complex(n[0] - n[1]/2, n[1]*math.sqrt(3)/2); return z/abs(z)
def G(fs): return chiv(fs, (4, 0)).conjugate()*eis.gamma(3, fs)
P = eis.primes_upto(200)
res = {'H3_maxdev': 0, 'H3_cases': 0, 'H6_maxdev': 0, 'H6_cases': 0, 'H6_sign_values': []}
for ms in [[a] for a in P[:6]] + [list(c) for c in itertools.combinations(P[:5], 2)]:
    for p in P[:12]:
        if p in ms or eis.norm(elem(ms + [p])) > 2500: continue
        m = elem(ms)
        # n = 3
        T = lambda fs: eis.gamma(2, fs).conjugate()
        g1 = chiv([p], m).conjugate()**2*eis.gamma(2, [p])        # cubic Gauss sum, numerator m, modulus p
        r3 = T(ms + [p])/(T(ms)*g1.conjugate())
        res['H3_maxdev'] = max(res['H3_maxdev'], abs(r3 - 1)); res['H3_cases'] += 1
        # n = 6
        g2 = chiv([p], m).conjugate()**2*eis.gamma(2, [p])        # G2^{(6)}(m,p): Gauss sum of chi^2, numerator m
        tau3 = eis.gamma(-1, ms + [p])/(eis.gamma(-1, ms)*g2)
        pred = -chiv([p], (16, 0))*G([p])/alpha([p])*chiv([p], m)*chiv(ms, p).conjugate()
        res['H6_maxdev'] = max(res['H6_maxdev'], abs(tau3 - pred)); res['H6_cases'] += 1
        s = chiv([p], m)*chiv(ms, p).conjugate()
        res['H6_sign_values'].append([round(s.real, 6), round(s.imag, 6)])
res['H6_sign_values'] = sorted(set(map(tuple, res['H6_sign_values'])))
json.dump(res, open(sys.argv[1], 'w'), indent=1); print(res)
