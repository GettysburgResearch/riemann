"""Exact cube-filter/H-factor identities and complete core regrouping controls.

The quadratic regrouping fixture uses literal rational Jacobi symbols;
it authenticates the universal square-core/mask algebra, not a number-field
large-sieve exponent or a physical zeta bound.
"""
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json
import sys

private = Path(__file__).with_name('_packages')
if private.is_dir():
    sys.path.insert(0, str(private))


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def mu(n):
    fs = factor(n)
    return 0 if any(e > 1 for _, e in fs) else (-1)**len(fs)


def jacobi(n, d):
    require(d > 0 and d % 2 == 1, 'Jacobi denominator must be positive odd.')
    result = 1
    for p, e in factor(d):
        if n % p == 0:
            return 0
        value = pow(n % p, (p-1)//2, p)
        result *= (1 if value == 1 else -1)**e
    return result


def conv(a, b, n):
    return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(n+1)]


def exact():
    local = 0
    h_cases = 0
    for q in (2, 3, 13, 25, 37):
        r = Q(1, q)
        for D in (Q(1, 5), Q(-1, 5)):
            for E in (Q(1, 7), Q(-1, 7)):
                V = W = r
                F = 1/(1-V)+W/(1-W)+E/(1-E)*((1-r)/(1-V)+W)
                F -= D/(1-E)*(1+(q-1)*W*V/(1-V))
                H = (1-V)*(1-W)/(1-D)*F
                expected = (1-r*r)*(1-(1-r)*D-r*E)/((1-E)*(1-D))
                require(H == expected, 'Exact principal Euler specialization failed.')
                h_cases += 1
        for phase in (1, -1):
            cap = 80
            a = phase*q*q
            reg = [Q(1)]+[r if k < 6 else r-a for k in range(1, cap+1)]
            denominator_inverse = [Q(1)]
            for k in range(1, cap+1):
                denominator_inverse.append((1-r)*denominator_inverse[k-1]
                                           +(a*denominator_inverse[k-6] if k >= 6 else 0))
            inverse = [Q(1)]+[denominator_inverse[k]-denominator_inverse[k-1]
                               for k in range(1, cap+1)]
            require(conv(reg, inverse, cap) == [Q(1)]+[Q(0)]*cap,
                    'Complete local regular correction inverse failed.')
            local += cap+1
        for b in (r, -r, Q(0)):
            for tilt in (Q(1), Q(1, 2), Q(1, 3)):
                cap = 40
                original = [b**j for j in range(cap+1)]
                target = [(b*tilt)**j for j in range(cap+1)]
                forward = [Q(1)]+[-(1-tilt)*b**j*tilt**(j-1) for j in range(1, cap+1)]
                inverse = [Q(1)]+[(1-tilt)*b**j for j in range(1, cap+1)]
                require(conv(forward, original, cap) == target, 'Cube resolvent target failed.')
                require(conv(forward, inverse, cap) == [Q(1)]+[Q(0)]*cap,
                        'Cube resolvent inverse failed.')
                local += 2*(cap+1)
    # Every support case of C_{t,k}(J), including zero extensions. Only
    # the zero/nonzero alternatives are needed to authenticate l=2d.
    support_checks = 0
    surviving_even = 0
    for e0 in (0, 1):
        for ell in range(31):
            t = e0+3*ell
            for k in range(4):
                for m in range(31):
                    J = 6*m
                    if t == 0:
                        nonzero = k == 0 or J == 0
                    elif k == 0:
                        nonzero = J == t-1 or (J >= t and t % 6 == 0)
                    elif k == 1:
                        nonzero = J == t or (J > t and (t-1) % 6 == 0)
                    else:
                        nonzero = False
                    if nonzero and t:
                        require(ell % 2 == 0, 'An odd cube shell survived principal frequency.')
                        d = ell//2
                        require(t == 6*d+e0, 'Wrong exact principal tilt exponent.')
                        surviving_even += 1
                    support_checks += 1
    # Literal nonunit/multiplicity core regrouping, with every n power and
    # every n,c shared prime retained. Coefficients are exact rational fixtures.
    cap = 64
    sf = [c for c in range(1, cap+1) if mu(c)]
    groups = {}
    pair_count = 0
    for n in range(1, cap+1):
        fs = factor(n)
        a = 1
        b = 1
        kernel = Q(1)
        for p, e in fs:
            a *= p**(e//2)
            b *= p**(e % 2)
            kernel *= -(1-Q(1, p))*Q(1, p**(2*e-1))
        require(n == a*a*b and mu(b) != 0, 'Full squarefree-core decomposition failed.')
        for c in sf:
            e = gcd(b, c)
            b1, c1 = b//e, c//e
            core = b1*c1
            require(mu(core) != 0 and gcd(b1, c1) == 1, 'Collapsed column not squarefree.')
            key = a, e, core
            groups[key] = groups.get(key, Q(0))+kernel*Q(mu(c), c)
            pair_count += 1
    row_checks = 0
    for d in range(1, 64, 2):
        if not mu(d):
            continue
        direct = Q(0)
        for n in range(1, cap+1):
            kernel = Q(1)
            for p, e in factor(n):
                kernel *= -(1-Q(1, p))*Q(1, p**(2*e-1))
            direct += kernel*sum(Q(mu(c), c)*jacobi(n*c, d) for c in sf)
        grouped = sum(value*jacobi(core, d) for (a, e, core), value in groups.items()
                      if gcd(a*e, d) == 1)
        require(direct == grouped, 'Full grouped quadratic source differs.')
        row_checks += 1
    require(jacobi(9, 3) == 0 and jacobi(1, 3) == 1,
            'Dropped square-part nonunit mask was not rejected.')
    budgets = 0
    for D in (1, 3, 16, 81):
        for P in (1, 5, 25):
            for Z in (16, 256, 4096):
                L = Q(D*D*P, Z)
                for N in (1, 2, 4, 8, 16, 32, 64):
                    first = min(L*N**3, Q(D*Z, N**4))
                    second = min(L*N**3, Q(Z, N**3))
                    require(first**7 <= Q(D**11*P**4, Z), 'Hybrid seventh-power balance failed.')
                    require(second**2 <= D*D*P, 'Hybrid square-root balance failed.')
                    budgets += 2
    return {'principal_Euler_specializations': h_cases,
            'exact_local_filter_and_inverse_coefficients': local,
            'complete_principal_shell_support_cases': support_checks,
            'nonzero_even_shell_cases': surviving_even,
            'unrestricted_n_norm_cap': cap, 'squarefree_c_norm_cap': cap,
            'complete_rational_Jacobi_pairs': pair_count,
            'complete_rational_Jacobi_rows': row_checks,
            'exact_exponent_budget_inequalities': budgets,
            'scope': 'Exact algebra and rational Jacobi mask controls; no analytic exponent certification.'}


def directed():
    from flint import arb, ctx
    import flint
    ctx.prec = 256
    cases = 0
    for q in (2, 3, 5, 13, 25, 37, 193):
        for k in range(1, 9):
            sigma = arb(1)/2+arb(1)/(10**k)
            x = (-sigma*arb(q).log()).exp()
            u = x/q
            v = q*q*x**6
            denominator = 1-x+u-v
            require(denominator > arb(1)/7, 'Uniform local inverse margin failed.')
            zeta_free_majorant = 1+14/(arb(q)*arb(q).sqrt())
            require((1-v)*(1+(u+v)/(1-x)) < zeta_free_majorant,
                    'Forward regular-factor critical resource failed.')
            require((1-v)*(1+(u+v)/denominator) < zeta_free_majorant,
                    'Inverse regular-factor critical resource failed.')
            cases += 1
    return {'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
            'precision_bits': ctx.prec, 'critical_margin_and_resource_cases': cases}


def main():
    result = {'status': 'PASS_FINITE_CUBE_FILTER_COMPONENT_CONTROLS',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'exact': exact(), 'directed': directed()}
    path = Path(__file__).with_name('CUBE_FILTER_CHECKS.json')
    path.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'exact': result['exact'],
                      'directed': result['directed']}))


if __name__ == '__main__':
    main()
