"""Is the observed law  t* ~ K/(N log c)  arithmetic, or would any source give the 1/N?

t* = min { x^T Q x : eta^T x = 1 } = the monic degree-2N orthogonal-polynomial norm
(L-16006(b)).  For the arithmetic Weil form it decays like 1/N at fixed cutoff.  Compare
against controls whose sources are NOT arithmetic:

  (A) psi(x) = arctan(x/b)  -- a Pick function, so its Loewner matrix is PSD (Loewner)
  (B) psi(x) = sum over a FINITE pole set  -- L-16006(c) predicts t* -> 0 fast and hits
      exactly 0 once 2N reaches the number of atoms
  (C) psi(x) = sum over MANY poles at the zeta ordinates (a caricature of the Weil source)
  (D) psi(x) = x/(1+x^2)-type and a random smooth odd source, as shape controls

If every control also gives t* ~ 1/N, the 1/N is universal and only the 1/log c is
arithmetic.  If the controls differ, the exponent itself carries information.

HIGH-PRECISION FLOAT (mpmath).
"""
import mpmath as mp
from mpmath import mpf, nstr, matrix, lu_solve


def loewner(psi, dpsi, N, dps):
    mp.mp.dps = dps
    nodes = [mpf(k) for k in range(-N, N + 1)]
    n = len(nodes)
    Q = matrix(n, n)
    for i in range(n):
        for j in range(n):
            Q[i, j] = dpsi(nodes[i]) if i == j else (psi(nodes[i]) - psi(nodes[j])) / (nodes[i] - nodes[j])
    return Q


def tstar(Q):
    d = Q.rows
    x = lu_solve(Q, matrix([1] * d))
    return 1 / sum(x[i] for i in range(d))


GAM = [mpf(v) for v in ['14.1347251417', '21.0220396388', '25.0108575801', '30.4248761259',
                        '32.9350615877', '37.5861781588', '40.9187190121', '43.3270732809',
                        '48.0051508812', '49.7738324777', '52.9703214777', '56.4462476971',
                        '59.3470440026', '60.8317785246', '65.1125440481', '67.0798105295',
                        '69.5464017112', '72.0671576745', '75.7046906991', '77.1448400689',
                        '79.3373750202', '82.9103808541', '84.7354929805', '87.4252746131',
                        '88.8091112076', '92.4918992706', '94.6513440405', '95.8706342282',
                        '98.8311942182', '101.317851006']]


def pole_src(poles, weights):
    def psi(x):
        return sum(a * (1 / (m - x) + 1 / (-m - x)) for m, a in zip(poles, weights))
    def dpsi(x):
        return sum(a * (1 / (m - x) ** 2 + 1 / (-m - x) ** 2) for m, a in zip(poles, weights))
    return psi, dpsi


SRC = {}
for b in (1, 5, 20):
    SRC[f"(A) arctan(x/{b})   [Pick]"] = (lambda x, b=b: mp.atan(x / b), lambda x, b=b: (1 / mpf(b)) / (1 + (x / b) ** 2))
SRC["(B) 6 poles 11..51 [finite]"] = pole_src([mpf(v) for v in [11, 19, 27, 35, 43, 51]], [mpf(1)] * 6)
SRC["(C) 30 zeta ordinates"] = pole_src(GAM, [mpf(1)] * len(GAM))
SRC["(C') 30 zeta ord., wt 1/mu"] = pole_src(GAM, [1 / m for m in GAM])
SRC["(D) x/(1+x^2/100)  [Pick-ish]"] = (lambda x: x / (1 + x ** 2 / 100), lambda x: (1 - x ** 2 / 100) / (1 + x ** 2 / 100) ** 2)
SRC["(D') log((1+x/30)/(1-x/30))"] = (lambda x: mp.log((1 + x / 30) / (1 - x / 30)),
                                       lambda x: (1 / mpf(30)) * (1 / (1 + x / 30) + 1 / (1 - x / 30)))

NS = [2, 4, 6, 8, 10, 12, 14, 16]
print("t* and the diagnostic product t* * N.  A flat t**N column means the 1/N law holds.")
print(f"{'source':>32} | " + " | ".join(f"N={N:<2}".rjust(11) for N in NS))
print("-" * (34 + 14 * len(NS)))
for name, (psi, dpsi) in SRC.items():
    cells = []
    for N in NS:
        try:
            Q = loewner(psi, dpsi, N, 40 + 8 * N)
            ts = tstar(Q)
            mp.mp.dps = 25
            cells.append(nstr(ts * N, 4).rjust(11))
        except Exception:
            cells.append("     -     ")
    print(f"{name:>32} | " + " | ".join(cells))

print()
print("Same sources, raw t* (to see the decay shape rather than the product):")
print(f"{'source':>32} | " + " | ".join(f"N={N:<2}".rjust(11) for N in NS))
print("-" * (34 + 14 * len(NS)))
for name, (psi, dpsi) in SRC.items():
    cells = []
    for N in NS:
        try:
            Q = loewner(psi, dpsi, N, 40 + 8 * N)
            ts = tstar(Q)
            mp.mp.dps = 25
            cells.append(nstr(ts, 4).rjust(11))
        except Exception:
            cells.append("     -     ")
    print(f"{name:>32} | " + " | ".join(cells))
