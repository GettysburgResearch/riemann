"""Fresh directed first-zero census and elementary global heat-kernel margins.

The actual completed-zeta function is evaluated on EVERY point of each
complex contour segment by acb rectangular input enclosures. A convex
zero-free output rectangle gives a homotopy to an exact rational polygon;
the latter's winding number is computed with Fraction, without angles.
No zero table, source moment JSON, quadrature or fitted model is imported.
The analytic proof consuming this census is GLOBAL_HEAT_POSITIVITY.md.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time


def need(ok, message):
    if not ok:
        raise ValueError(message)


def winding(vertices):
    """Exact signed crossings of the positive real ray."""
    answer = 0
    for (x, y), (u, v) in zip(vertices, vertices[1:]):
        if y <= 0 < v:
            det = x*v-u*y
            need(det != 0, 'Polygon crosses the origin.')
            if det > 0:
                answer += 1
        elif v <= 0 < y:
            det = x*v-u*y
            need(det != 0, 'Polygon crosses the origin.')
            if det < 0:
                answer -= 1
    return answer


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dependency-dir', type=Path)
    ap.add_argument('--bits', type=int, default=256)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    root = Path(__file__).resolve().parent
    dep = args.dependency_dir or root.parent/'eisenstein/_packages'
    sys.path.insert(0, str(dep.resolve()))
    import flint
    from flint import arb, acb, fmpq, ctx
    need(flint.__version__ == '0.9.0', 'Pinned python-flint 0.9.0 required.')
    need(args.bits >= 192, 'Insufficient directed working precision.')
    ctx.prec = args.bits
    started = time.monotonic()

    def A(q):
        q = Q(q)
        return arb(fmpq(q.numerator, q.denominator))

    def exact_mid(x):
        m, e = x.mid().man_exp()
        return Q(int(m)) * (Q(2)**int(e))

    def xi(s):
        return s*(s-1)/2*(-s*arb.pi().log()/2).exp()*(s/2).gamma()*s.zeta()

    point_cache = {}

    def point(z):
        if z not in point_cache:
            f = xi(acb(A(z[0]), A(z[1])))
            need(f.is_finite(), 'Nonfinite endpoint evaluation.')
            point_cache[z] = (exact_mid(f.real), exact_mid(f.imag))
        return point_cache[z]

    def segment_box(z, w):
        re = arb(A((z[0]+w[0])/2), A(abs(z[0]-w[0])/2))
        im = arb(A((z[1]+w[1])/2), A(abs(z[1]-w[1])/2))
        f = xi(acb(re, im))
        if not f.is_finite():
            return None
        p, q = point(z), point(w)
        r = f.real.union(A(p[0])).union(A(q[0]))
        i = f.imag.union(A(p[1])).union(A(q[1]))
        if r.contains(0) and i.contains(0):
            return None
        return r, i

    def census(corners):
        vertices = [point(corners[0])]
        accepted = 0
        max_depth = 0
        margin = None

        def follow(z, w, depth):
            nonlocal accepted, max_depth, margin
            need(depth <= 22, 'Contour coverage refinement limit exceeded.')
            box = segment_box(z, w)
            if box is None:
                mid = ((z[0]+w[0])/2, (z[1]+w[1])/2)
                follow(z, mid, depth+1)
                follow(mid, w, depth+1)
                return
            r, i = box
            distance = max(r.abs_lower(), i.abs_lower())
            need(distance > 0, 'Uncertified zero-free segment.')
            margin = distance if margin is None else min(margin, distance)
            vertices.append(point(w))
            accepted += 1
            max_depth = max(max_depth, depth)

        for z, w in zip(corners, corners[1:]):
            follow(z, w, 0)
        need(vertices[0] == vertices[-1], 'Contour polygon is not closed.')
        return {'winding': winding(vertices), 'segments': accepted,
                'maximum_bisection_depth': max_depth,
                'minimum_output_coordinate_distance': str(margin)}

    # Positive orientation. Bottom height1 is inside the already proved
    # zero-free disk |z|<=4 from the native actual-theta MGF bound.
    rectangle = [(Q(-1, 8), Q(1)), (Q(9, 8), Q(1)),
                 (Q(9, 8), Q(20)), (Q(-1, 8), Q(20)),
                 (Q(-1, 8), Q(1))]
    full = census(rectangle)
    need(full['winding'] == 1, 'The first20 zero census is not one.')
    # A second independently covered contour excludes the first root and
    # exercises the same complete-contour computation with winding zero.
    empty_rectangle = [(Q(-1, 8), Q(1)), (Q(9, 8), Q(1)),
                       (Q(9, 8), Q(10)), (Q(-1, 8), Q(10)),
                       (Q(-1, 8), Q(1))]
    empty = census(empty_rectangle)
    need(empty['winding'] == 0, 'Empty-contour control failed.')

    first = []
    for t in (Q(1413, 100), Q(707, 50)):
        f = xi(acb(A(Q(1, 2)), A(t)))
        need(f.imag.contains(0), 'Functional-symmetry reality check failed.')
        need(not f.real.contains(0), 'Unresolved first-zero sign endpoint.')
        first.append({'height': str(t), 'real_enclosure': str(f.real),
                      'sign': 1 if f.real > 0 else -1})
    need(first[0]['sign'] == -first[1]['sign'], 'First-zero sign change failed.')
    need(Q(707, 50)**2 < 200, 'First-zero upper-square bound failed.')

    # Directed margins used by the analytic proof. No floating arithmetic.
    y = A(Q(1, 50))
    sqpi = arb.pi().sqrt()
    gamma = arb.const_euler()
    I_lower = (-gamma/2-(16*y).log()/2+A(Q(23, 40))
               -sqpi*y.sqrt()/2+y/12-sqpi*y*y.sqrt()/4)
    L = A(2).log()
    prime_majorant = L/A(2).sqrt()*(-L*L/(4*y)).exp()
    prime_majorant += 2*y*L/(L-y)*(L/2-L*L/(4*y)).exp()
    B = 4*sqpi*y.sqrt()+I_lower-gamma-arb.pi().log()-2*prime_majorant
    need(B > A(Q(1, 200)), 'Global small-y positivity margin failed.')
    derivative_bracket = -A(Q(1, 2))+7*sqpi*y.sqrt()/4+y/12
    need(derivative_bracket < 0, 'Small-y endpoint monotonicity failed.')
    C = A(5)/176*A(1).exp()
    large_ratio = C*(A(Q(1601, 4))+1/y)*(-A(Q(799, 4))*y).exp()
    need(large_ratio < A(Q(2, 3)), 'Complete high-zero tail margin failed.')
    need((A(5)/176*16).exp()-1 < 1, 'Actual-theta zero-free disk4 gate failed.')

    # Exact winding regression controls: clockwise, enclosing and empty.
    square = [(Q(1), Q(1)), (Q(-1), Q(1)),
              (Q(-1), Q(-1)), (Q(1), Q(-1)), (Q(1), Q(1))]
    need(winding(square) == 1 and winding(list(reversed(square))) == -1,
         'Exact winding orientation controls failed.')
    need(winding([(x+3, y) for x, y in square]) == 0,
         'Exact winding empty-box control failed.')

    result = {'status': 'PASS', 'scope': 'first20 census and global heat-sign margins',
              'primitive': 'xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2',
              'arithmetic': 'python-flint 0.9.0 acb/arb, outward rectangular balls',
              'bits': args.bits, 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'first20_contour': full, 'empty10_control': empty,
              'first_real_zero_bracket': first,
              'small_y_multiplied_kernel_lower': str(B),
              'small_y_monotonicity_bracket': str(derivative_bracket),
              'large_y_complete_tail_to_first_ratio': str(large_ratio),
              'not_proved': ['complete monotonicity', 'all polynomial quadratic forms',
                             'RH', 'an improved zeta zero-free strip']}
    if args.check:
        old = json.loads(args.check.read_text())
        need(result == old, 'Fresh primitive replay differs from recorded output.')
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'first20_segments': full['segments'],
                      'first20_winding': full['winding'],
                      'small_y_margin': str(B), 'large_y_ratio': str(large_ratio),
                      'seconds': round(time.monotonic()-started, 3)}))


if __name__ == '__main__':
    main()
