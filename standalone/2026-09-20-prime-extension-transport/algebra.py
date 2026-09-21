"""Exact logarithmic Newton-defect and finite Euler-factor checks."""
import json
from math import isqrt

def conv(a, b):
    N = min(len(a), len(b))-1
    out = [0]*(N+1)
    for r in range(1, N+1):
        if a[r]:
            for s in range(1, N//r+1):
                out[r*s] += a[r]*b[s]
    return out

def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def deriv(a, p):
    return [0]+[vp(n, p)*a[n] for n in range(1, len(a))]

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def require(ok, message):
    if not ok:
        raise ValueError(message)

def inverse(a):
    N = len(a)-1
    if a[1] != 1:
        raise ValueError("unit constant coefficient required")
    nu = [0]*(N+1)
    nu[1] = 1
    # Triangular Dirichlet inversion, not prime factorization.
    for n in range(2, N+1):
        nu[n] = -sum(a[d]*nu[n//d] for d in range(2, n+1) if n%d == 0)
    return nu

def curve_trace(m, p):
    if (p < 5 or any(p%d == 0 for d in range(2, isqrt(p)+1))
        or (3*m)%p == 0):
        raise ValueError("odd good prime required")
    constant = m*m*pow(4, -1, p) % p
    points = 1
    for x in range(p):
        value = (x*x*x+constant) % p
        points += 1 if value == 0 else (2 if pow(value, (p-1)//2, p) == 1 else 0)
    return p+1-points

def euler_fixture(N):
    # Exact three-good-prime Euler product from E_17. Other local factors
    # are omitted; this is NOT the global elliptic L-function.
    local = {p:(curve_trace(17, p), p) for p in (5, 7, 11)}
    nu = [0]*(N+1)
    nu[1] = 1
    for p, (ap, bp) in local.items():
        factor = [0]*(N+1)
        factor[1] = 1
        if p <= N:
            factor[p] = -ap
        if p*p <= N:
            factor[p*p] = bp
        nu = conv(nu, factor)
    return inverse(nu), nu, local

def tests():
    counts = dict(defect_coefficients=0, horizon_coefficients=0,
                  local_tail_coefficients=0, endpoints_nonzero=0)
    for Y in (2, 3, 7, 15):
        N = (Y+1)**2
        zeta = [0]+[1]*N
        fixtures = [(zeta, inverse(zeta), (2, 3, 5)),
                    (*euler_fixture(N)[:2], (5, 7, 11))]
        for base, nu, plist in fixtures:
            unit = [0]*(N+1)
            unit[1] = 1
            for tail in (False, True):
                c = [nu[n] if n <= Y else 0 for n in range(N+1)]
                if tail:
                    c[Y+1] += 1
                    c[Y+3] -= 2
                e = sub(unit, conv(base, c))
                v = sub([2*x for x in c], conv(base, conv(c, c)))
                require(v[1:N] == nu[1:N], "full Newton horizon")
                counts["horizon_coefficients"] += N-1
                for p in plist:
                    lam = conv(deriv(base, p), nu)
                    dc = add(deriv(c, p), conv(lam, c))
                    dv = add(deriv(v, p), conv(lam, v))
                    rhs = [2*x for x in conv(e, dc)]
                    require(dv == rhs, "logarithmic defect propagation")
                    require(not any(dc[1:Y+1]), "native initial log constraints")
                    require(dv[N] == 2*e[Y+1]*dc[Y+1], "first omitted endpoint")
                    counts["endpoints_nonzero"] += int(dv[N] != 0)
                    counts["defect_coefficients"] += N
    for ap, bp in ((0, 2), (1, 5), (-2, 7), (0, 1), (1, 0)):
        # nu=1-ap*T+bp*T^2; lambda_k obeys the root-trace recurrence.
        traces = [2, ap]
        for k in range(2, 21):
            traces.append(ap*traces[-1]-bp*traces[-2])
        tail = [0, 0]+traces[2:]
        for k in range(21):
            got = tail[k]-(ap*tail[k-1] if k>=1 else 0)+(bp*tail[k-2] if k>=2 else 0)
            want = (ap*ap-2*bp if k==2 else -ap*bp if k==3 else 0)
            require(got == want, "degree-two local prime-power collapse")
            counts["local_tail_coefficients"] += 1
    require(counts["endpoints_nonzero"] > 0, "endpoint control not exercised")
    point_counts = [[m, p, curve_trace(m,p)] for m in (17,53)
                    for p in (5,7,11,13,19,23)]
    return dict(schema="PET26-algebra-1", **counts, point_counts=point_counts,
                inert_square_sign="negative: -2*b*T^2",
                analytic_claim="none")

if __name__ == "__main__":
    print(json.dumps(tests(), indent=2, sort_keys=True))
