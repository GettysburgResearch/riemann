"""Exact finite controls for SNE26; NOT a theta-energy or RH certificate."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
COUPLING_FACTOR = 1


def need(ok, message):
    if not ok:
        raise ValueError(message)


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    a = zeros(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def tp(a):
    return [list(x) for x in zip(*a)]


def plus(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(a, c):
    return [[x * c for x in r] for r in a]


def mm(a, b):
    return [[sum((x * y for x, y in zip(r, c)), F(0)) for c in tp(b)] for r in a]


def prod(*aa):
    a = aa[0]
    for b in aa[1:]:
        a = mm(a, b)
    return a


def inv(a):
    n = len(a)
    w = [list(r) + e for r, e in zip(a, eye(n))]
    for j in range(n):
        k = next((k for k in range(j, n) if w[k][j]), None)
        need(k is not None, 'singular matrix')
        w[j], w[k] = w[k], w[j]
        q = w[j][j]
        w[j] = [x / q for x in w[j]]
        for k in range(n):
            if k != j:
                q = w[k][j]
                w[k] = [x - q*y for x, y in zip(w[k], w[j])]
    return [r[n:] for r in w]


def fn2(a):
    return sum((x*x for r in a for x in r), F(0))


def diag(v):
    a = zeros(len(v))
    for i, x in enumerate(v):
        a[i][i] = F(x)
    return a


def spd(a):
    need(a == tp(a), 'not symmetric')
    b = [r[:] for r in a]
    for j in range(len(b)):
        p = b[j][j]
        need(p > 0, 'not strictly positive')
        for i in range(j + 1, len(b)):
            for k in range(j + 1, len(b)):
                b[i][k] -= b[i][j] * b[j][k] / p


def blocks(t, d):
    a = [r[:d] for r in t[:d]]
    b = [r[d:] for r in t[:d]]
    c = [r[:d] for r in t[d:]]
    dd = [r[d:] for r in t[d:]]
    return a, mm(b, tp(b)), mm(tp(c), c), fn2(dd)


def energy(data, g, lam=F(0)):
    spd(g)
    a, r, q, d0 = data
    w = inv(g)
    return (tr(prod(g, a, w, tp(a))) + COUPLING_FACTOR*tr(mm(g, r))
            + tr(mm(w, q)) + d0 + lam*(tr(g)+tr(w)-2*len(g)))


def gradient(data, g, lam):
    a, r, q, _ = data
    w = inv(g)
    return plus(plus(prod(a, w, tp(a)), r), plus(
        scale(prod(w, plus(prod(tp(a), g, a), q), w), -1),
        scale(plus(eye(len(g)), scale(mm(w, w), -1)), lam)))


def direct_energy(t, g, lam):
    h = eye(len(t))
    for i, row in enumerate(g):
        h[i][:len(g)] = row
    return tr(prod(h, t, inv(h), tp(t)))+lam*(tr(g)+tr(inv(g))-2*len(g))


def geo_coeffs(data, b, powers, lam):
    a, r, q, d0 = data
    bi = inv(b)
    a0 = prod(tp(b), a, tp(bi))
    r0 = prod(tp(b), r, b)
    q0 = prod(bi, q, tp(bi))
    p0 = mm(tp(b), b)
    p1 = mm(bi, tp(bi))
    out = [(d0-2*len(b)*lam, 0)]
    for i, hi in enumerate(powers):
        out += [(r0[i][i]+lam*p0[i][i], hi),
                (q0[i][i]+lam*p1[i][i], -hi)]
        for j, hj in enumerate(powers):
            out.append((a0[i][j]**2, hi-hj))
    need(all(c >= 0 for c, k in out[1:]), 'nonpositive geodesic coefficient')
    return out


def direct_jets(data, g, v, a2, lam):
    a, r, q, _ = data
    w = inv(g)
    w1 = scale(prod(w, v, w), -1)
    w2 = plus(scale(prod(w, v, w, v, w), 2), scale(prod(w, a2, w), -1))
    j1 = tr(plus(prod(v, a, w, tp(a)), prod(g, a, w1, tp(a))))
    j1 += tr(mm(v, r))+tr(mm(w1, q))+lam*(tr(v)+tr(w1))
    j2 = tr(plus(plus(prod(a2, a, w, tp(a)),
                         scale(prod(v, a, w1, tp(a)), 2)), prod(g, a, w2, tp(a))))
    j2 += tr(mm(a2, r))+tr(mm(w2, q))+lam*(tr(a2)+tr(w2))
    return j1, j2


def qpair(q):
    q = F(q)
    return [str(q.numerator), str(q.denominator)]


def reconstruct():
    counts = {'whole_block': 0, 'geodesic_values': 0, 'gradient_and_hessian': 0,
              'global_scalar_brackets': 0, 'triangular_partitions': 0,
              'volterra_full_kernel': 0, 'regularized_embedding': 0, 'primitive_error_transport': 0}
    payload = []
    for n in range(3, 7):
        t = [[F(((i+2)*(j+5)+i-2*j)%11-5, 3) for j in range(n)] for i in range(n)]
        for d in range(1, min(n, 4)):
            data = blocks(t, d)
            b = eye(d)
            for i in range(d):
                b[i][i] = F(i+2, i+1)
                for j in range(i):
                    b[i][j] = F((i+2*j)%3-1, 4)
            powers = [i-1 for i in range(d)]
            g = mm(b, tp(b))
            for lam in (F(1, 16), F(1, 2), F(1)):
                e = energy(data, g, lam)
                need(e == direct_energy(t, g, lam), 'full/complement identity')
                counts['whole_block'] += 1
                cs = geo_coeffs(data, b, powers, lam)
                for x in (F(1, 2), F(2, 3), F(1), F(3, 2), F(2)):
                    gx = prod(b, diag([x**h for h in powers]), tp(b))
                    need(energy(data, gx, lam) == sum((c*x**k for c, k in cs), F(0)),
                         'geodesic exponent identity')
                    counts['geodesic_values'] += 1
                v = prod(b, diag(powers), tp(b))
                a2 = prod(b, diag([h*h for h in powers]), tp(b))
                j1, j2 = direct_jets(data, g, v, a2, lam)
                need(j1 == sum((c*k for c, k in cs), F(0)), 'first jet')
                need(j2 == sum((c*k*k for c, k in cs), F(0)), 'second jet')
                lg = gradient(data, g, lam)
                need(j1 == tr(mm(lg, v)), 'normalized gradient')
                need(j2 >= 2*lam*sum(h*h for h in powers), 'strong convexity')
                need(tr(prod(g, lg, g, lg)) >= 0, 'gradient square')
                counts['gradient_and_hessian'] += 1
                if n == 4 and d == 2:
                    payload.append({'lambda':qpair(lam), 'energy':qpair(e),
                                    'jet1':qpair(j1), 'jet2':qpair(j2)})
            # Exact nesting of a fixed similarity with identity and smaller penalty.
            if d+1 < n:
                gg = eye(d+1)
                for i in range(d):
                    gg[i][:d] = g[i]
                bigdata = blocks(t, d+1)
                need(energy(bigdata, gg) == energy(data, g), 'embedding energy')
                need(energy(bigdata, gg, F(1, 2**(d+1))) <=
                     energy(data, g, F(1, 2**d)), 'regularized monotonicity')
                counts['regularized_embedding'] += 1
    # Exact full-matrix perturbations test the complete primitive-error transport.
    for n in (3,4,5):
        t = [[F((2*i+3*j)%7-3,4) for j in range(n)] for i in range(n)]
        tb = [[t[i][j]+F((i+j)%3-1,128) for j in range(n)] for i in range(n)]
        for d in range(1,n):
            real, approx = blocks(t,d), blocks(tb,d)
            b=eye(d)
            for i in range(d):
                b[i][i]=F(i+3,2)
                if i: b[i][i-1]=F(1,3)
            g=mm(b,tp(b));w=inv(g)
            l1=lambda a:sum((abs(x) for row in a for x in row),F(0))
            diff=lambda a,b:plus(a,scale(b,-1))
            ea,er,eq=[l1(diff(real[i],approx[i])) for i in range(3)]
            ed=abs(real[3]-approx[3]);a=l1(approx[0])
            gn=max(sum(abs(x) for x in row) for row in g)
            wn=max(sum(abs(x) for x in row) for row in w)
            kap=gn*wn
            ef=kap*(2*a*ea+ea*ea)+l1(g)*er+l1(w)*eq+ed
            ez=4*kap*a*ea+2*kap*ea*ea+gn*er+wn*eq
            for lam in (F(1,8),F(1)):
                need(abs(energy(real,g,lam)-energy(approx,g,lam))<=ef,
                     'complete primitive energy error')
                dl=diff(gradient(real,g,lam),gradient(approx,g,lam))
                need(tr(prod(g,dl,g,dl))<=ez*ez, 'complete gradient error')
                counts['primitive_error_transport']+=1

    # Scalar full-complement problems: exact stationary solutions and certificates.
    for r, q, lam, optimum_g in ((F(1),F(1),F(1),F(1)),
                                (F(1),F(7),F(1),F(2)),
                                (F(3),F(15),F(1),F(2))):
        data = ([[F(0)]], [[r]], [[q]], F(0))
        optimum = energy(data, [[optimum_g]], lam)
        need(gradient(data, [[optimum_g]], lam) == [[F(0)]], 'scalar stationary')
        for g in (F(1,8),F(1,3),F(1,2),F(1),F(3,2),F(2),F(4),F(8)):
            gg = [[g]]
            lg = gradient(data, gg, lam)
            upper = energy(data, gg, lam)
            lower = upper-tr(prod(gg,lg,gg,lg))/(4*lam)
            need(lower <= optimum <= upper, 'global scalar gap certificate')
            counts['global_scalar_brackets'] += 1
    # Finite upper-triangular partition scaling, using an independently expanded norm.
    for n in range(2, 9):
        t = [[F((i+2*j)%7-3, 5) if i<=j else F(0) for j in range(n)] for i in range(n)]
        for width in (1, 2, 3):
            group = [i//width for i in range(n)]
            m = 1+max(group)
            pinched = sum((t[i][j]**2 for i in range(n) for j in range(n)
                           if group[i] == group[j]), F(0))
            for eps in (F(1,2), F(1,3), F(1,7)):
                s = [eps**(m-1-group[i]) for i in range(n)]
                transformed = sum(((s[i]*t[i][j]/s[j])**2 for i in range(n)
                                   for j in range(n)), F(0))
                exact = pinched+sum((eps**(2*(group[j]-group[i]))*t[i][j]**2
                        for i in range(n) for j in range(n) if group[i]<group[j]), F(0))
                need(exact == transformed, 'nest partition scaling')
                need(exact <= pinched+eps**2*fn2(t), 'full offdiagonal bound')
                counts['triangular_partitions'] += 1
    # Actual continuous Volterra kernel integral; no uncomputed within-cell term.
    volterra = []
    for m in range(1, 21):
        for eps in (F(1,2), F(1,3), F(1,5)):
            direct = sum((F(1,2*m*m) if i==j else
                          (eps**(2*(i-j))/m**2 if i>j else F(0))
                          for i in range(m) for j in range(m)), F(0))
            formula = F(1,2*m)+sum(((m-k)*eps**(2*k)/m**2 for k in range(1,m)), F(0))
            need(direct == formula, 'complete Volterra kernel')
            need(formula <= F(1,2*m)+eps**2/2, 'Volterra spectral-mass control')
            counts['volterra_full_kernel'] += 1
            if m in (1,4,16) and eps == F(1,3):
                volterra.append({'m':m, 'epsilon':qpair(eps), 'energy':qpair(formula)})
    # A normal matrix already has positive real-part spectral mass.
    t = zeros(6)
    for k in (0,2,4):
        t[k][k+1],t[k+1][k] = F(-2),F(2)
    t[4][4] = t[5][5] = F(1)
    need(fn2(t) == 26 and tr(mm(t,t)) == -22, 'normal spectral control')
    need(mm(t,tp(t)) == mm(tp(t),t), 'normality')
    need(fn2(scale(plus(t,tp(t)),F(1,2))) == 2, 'real-part defect identity')
    return {'status':'PROPOSED_COMPONENTS_BOUNDED_CONTROLS', 'rh_proved':False,
            'native_theta_energy_evaluated':False, 'native_asymptotic_bound_proved':False,
            'finite_optimizer_gap_is_spectral_gap':False, 'counts':counts,
            'block_examples':payload, 'volterra_complete_examples':volterra,
            'normal_control':{'dimension':6, 'energy':26, 'negative_square_trace':22,
                              'real_part_square_mass':2},
            'independent_mathematical_review':False}


def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(',',':'), ensure_ascii=True)


def strict_load(path):
    def pairs(items):
        d = {}
        for k, v in items:
            need(k not in d, 'duplicate key')
            d[k] = v
        return d
    def forbidden(x):
        raise ValueError('floating or nonfinite JSON is forbidden')
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_float=forbidden, parse_constant=forbidden)


def authenticate():
    manifest = ROOT/'SHA256SUMS'
    need(manifest.is_file() and not manifest.is_symlink(), 'missing/linked manifest')
    entries = {}
    for line in manifest.read_text().splitlines():
        digest, name = line.split('  ', 1)
        need(len(digest)==64 and all(x in '0123456789abcdef' for x in digest), 'hash format')
        need(name == Path(name).name and name not in entries and name != 'SHA256SUMS', 'manifest path')
        entries[name] = digest
    present = {p.name for p in ROOT.iterdir()}
    need(present == set(entries)|{'SHA256SUMS'}, 'unexpected/missing inventory')
    for name, digest in entries.items():
        p = ROOT/name
        need(p.is_file() and not p.is_symlink(), 'not a regular file')
        need(hashlib.sha256(p.read_bytes()).hexdigest() == digest, 'source/receipt drift')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', type=Path, required=True)
    args = ap.parse_args()
    authenticate()
    actual = reconstruct()
    need(canonical(strict_load(args.check)) == canonical(actual), 'reconstructed payload mismatch')
    print('PASS_BOUNDED_CONTROLS '+hashlib.sha256(canonical(actual).encode()).hexdigest())


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError, ZeroDivisionError) as e:
        print('REJECT: '+str(e), file=sys.stderr)
        sys.exit(1)
