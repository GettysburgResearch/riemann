"""O1 exact-rational exponent ledger (sympy).  All exponents are log_D; X = D (dual column norm),
rows of the dual  calH = D^eta  with eta = 2 - rho  (Poisson in the primal row u, H = D^rho).
Target after Poisson (normalised):  E(calH, X) = (1/X) sum_{N h <= calH} |B_h(X)|^2  <<  X^{1+eps}.
Ladder law (RUNG_STRENGTH):  sigma = 1/2 + c*rho/2, c = 1 - 1/m (m = order of the row symbol).
Pipelines (each returns the minimal admissible rho):
  direct(kappa)        : E << calH + X + (calH X)^kappa                       (no reflection)
  reflect(a, kappa)    : row-conductor N(h)^a reflection (dual length X' = calH^a/X, isometric),
                         then  E << calH + X' + (calH X')^kappa ; best of reflecting or not
  rs_index(a)          : Rankin-Selberg over all Fourier indices k, N k <= calH^a, by positivity
  primal(kappa)        : large sieve on the primal Moebius sums: sum_u |A_u|^2 << (H + D + (HD)^kappa) D
kappa = 1/2 means an optimal (M + N) large sieve; kappa = 2/3 is Heath-Brown / BGL.
Run: python3 ledger.py  (prints the table used in README.md; asserts the headline numbers).
"""
from sympy import Rational as Q, Symbol, solve, Max, Min, simplify, nsimplify
eta = Symbol('eta', positive=True)

def rho_from_eta_max(eta_max):
    return Max(1, 2 - eta_max)   # rho >= 1 always (calH <= X is needed by the term calH)

def sigma(c, rho): return Q(1, 2) + c*rho/2

def direct(kappa):
    # (eta + 1) kappa <= 1  and eta <= 1
    em = Min(1, 1/kappa - 1)
    return rho_from_eta_max(em)

def reflect(a, kappa, mandatory=False):
    # if reflecting: X' = a*eta - 1 (log); need X' <= 1 and (eta + X') kappa <= 1 and eta <= 1
    # i.e. eta <= 2/a and eta*(1+a) - 1 <= 1/kappa.  Not reflecting: direct(kappa).
    em_ref = Min(1, Q(2)/a, (1/kappa + 1)/(1 + a))
    em_dir = Min(1, 1/kappa - 1)
    return rho_from_eta_max(em_ref if mandatory else Max(em_ref, em_dir))

def rs_index(a):
    # E << calH^a (positivity: all indices of norm <= calH^a), need a*eta <= 1
    return rho_from_eta_max(Q(1)/a)

def primal(kappa):
    # (H D)^kappa <= H  <=>  rho >= kappa/(1-kappa) ; also rho >= 1
    return Max(1, kappa/(1 - kappa))

rows = []
def add(name, c, rho, label):
    s = sigma(c, rho); rows.append((name, c, rho, s, label)); return s

cub, quart, sext = Q(2, 3), Q(3, 4), Q(5, 6)
k_bgl, k_opt = Q(2, 3), Q(1, 2)
# cubic family (target of O1)
s1 = add('cubic: direct cubic LS on absorbed dual, BGL/HB kappa=2/3', cub, direct(k_bgl), 'PROPOSED (bookkeeping)')
s2 = add('cubic: 6-fold Kubota FE (row conductor N(h)^4) + BGL', cub, reflect(4, k_bgl), 'PROPOSED (imports Kubota FE)')
s3 = add('cubic: 6-fold Kubota FE, then optimal LS only after it', cub, reflect(4, k_opt, True), 'PROPOSED (model)')
s4 = add('cubic: Rankin-Selberg over index k=h^4 (positivity)', cub, rs_index(4), 'PROPOSED')
s5 = add('cubic: primal Heath-Brown cubic LS on mu-coefficients', cub, primal(k_bgl), 'PROPOSED (bookkeeping)')
s6 = add('cubic: hypothetical conductor-N(h)^2 reflection keeping cubic twist + BGL', cub, reflect(2, k_bgl), 'HEURISTIC (no such reflection known)')
s7 = add('cubic: (S6) sextic theta, quadratic post-twist, optimal LS', cub, reflect(2, k_opt), 'CONDITIONAL on (S6) (LEVERAGE sec.5)')
s8 = add('cubic: LS_kappa=1/2 for absorbed coefficients (no reflection)', cub, direct(k_opt), 'CONDITIONAL on LS_1/2')
# quartic test bed over Q(i): absorption into 4-fold Gauss sum, Kubota numerator h^3
q1 = add('quartic: direct quartic LS (BGL)', quart, direct(k_bgl), 'PROPOSED')
q2 = add('quartic: 4-fold Kubota FE (row conductor N(h)^3) + BGL', quart, reflect(3, k_bgl), 'PROPOSED (imports Kubota FE)')
q3 = add('quartic: 4-fold Kubota FE, then optimal LS only after it', quart, reflect(3, k_opt, True), 'PROPOSED (model)')
q4 = add('quartic: hypothetical GL(2) quartic theta, quadratic post-twist', quart, reflect(2, k_opt), 'CONDITIONAL (EP shape contradicts)')
# sextic Oct 5 family for calibration
o1 = add('sextic (Oct 5): cubic theta, quadratic twist, optimal LS', sext, reflect(2, k_opt), 'IMPORTED (Oct 5)')

# kappa needed (direct pipeline, cubic family): sigma(kappa) = 3/2 - 1/(3 kappa) for kappa >= 1/2
kap = Symbol('kappa', positive=True)
sig_k = simplify(sigma(cub, 3 - 1/kap))
need = {t: solve(sig_k - t, kap)[0] for t in (Q(5, 6), Q(7, 8), Q(11, 12), Q(1))}

# general Kubota row-conductor exponent under absorption, n-fold cover, absorbing Gauss sum of order n:
# r = h^{1 + n/2} mod n-th powers  ->  a(n) = (1 + n/2) mod n
a_of_n = {n: (1 + n//2) % n for n in (4, 6, 10)}

if __name__ == '__main__':
    w = max(len(r[0]) for r in rows)
    print('%-*s  %5s  %6s  %7s  %s' % (w, 'pipeline', 'c', 'rho', 'sigma', 'label'))
    for name, c, rho, s, lab in rows:
        print('%-*s  %5s  %6s  %7s  %s' % (w, name, c, rho, s, lab))
    print('\ncubic family, direct pipeline: sigma(kappa) =', sig_k)
    for t, v in need.items(): print('  sigma =', t, ' needs kappa =', v)
    print('Kubota row-conductor exponent a(n) under absorption:', a_of_n)
    print('degree tax (reflect a, optimal LS): rho >= max(1, 2 - 2/a):',
          {a: reflect(a, k_opt, True) for a in (2, 3, 4, 6)})
    assert s1 == 1 and s2 == 1 and s3 == 1 and s5 == Q(7, 6) and s6 == Q(8, 9) and s7 == Q(5, 6)
    assert s4 == Q(13, 12) and q2 == Q(65, 64) and q3 == Q(1, 2) + Q(3, 4)*Q(4, 3)/2 and q4 == Q(7, 8) and o1 == Q(11, 12)
    assert need[Q(5, 6)] == Q(1, 2) and need[Q(7, 8)] == Q(8, 15) and need[Q(11, 12)] == Q(4, 7) and need[Q(1)] == Q(2, 3)
    assert a_of_n == {4: 3, 6: 4, 10: 6}
    print('all asserts passed')
