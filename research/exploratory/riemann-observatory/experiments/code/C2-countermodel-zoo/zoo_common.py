#!/usr/bin/env python3
"""Shared tools for the C2 countermodel zoo (Riemann Observatory).

Status: EXPLORATORY code. Rigour statement: functions named `krawczyk_*` return a certificate only when
all arithmetic is done in Arb ball arithmetic (python-flint) and the inclusion test succeeds; everything
else (scans, Newton polishing) is NON-RIGOROUS and only produces candidate points.

Certificate used (complex Krawczyk test; standard, see e.g. Rump, Acta Numerica 19 (2010) sect. 13, or
Moore-Kearfott-Cloud, Introduction to Interval Analysis, SIAM 2009, ch. 8):
  Let f be holomorphic on a neighbourhood of the closed axis-parallel square D = z0 + [-r,r] + i[-r,r].
  Let B be an Arb ball (rectangle) containing f'(D), and Y a complex number.  Put
        K = z0 - Y f(z0) + (1 - Y B) (D - z0).
  If K is contained in the interior of D then f has exactly one zero in D, and it lies in K.
  Proof: for z in D, f(z) = f(z0) + (z - z0) A_z with A_z = int_0^1 f'(z0 + u(z - z0)) du in conv f'(D) ⊂ B
  (B is convex), so g(z) = z - Y f(z) lies in K ⊂ D; Brouwer gives a fixed point, i.e. a zero (Y != 0 is
  forced, since Y = 0 gives K ⊇ D - z0 + z0 = D).  If z1 != z2 were two zeros, 0 = (z1 - z2) A with
  A in B; then A = 0 and 1 ∈ 1 - Y B, whence K contains a translate of D, impossible inside int D.
"""
import flint
from flint import acb, arb, acb_series


def ball(x, y, r):
    """Closed square z0 + [-r,r] + i[-r,r] as an Arb complex ball (x, y, r given as decimal strings/floats)."""
    return acb(arb(x, r), arb(y, r))


def krawczyk(fd, z0, r, Y=None):
    """Rigorous Krawczyk test.

    fd(z) must return (f(z), f'(z)) as Arb acb balls enclosing the true values for every point of the input
    ball z.  z0 is a python complex (exact binary midpoint used), r > 0 a float.
    Returns dict(ok=bool, K=acb enclosure or None, info=str).
    """
    x0, y0 = arb(z0.real), arb(z0.imag)   # exact binary floats
    zc = acb(x0, y0)
    D = acb(arb(z0.real, r), arb(z0.imag, r))
    f0, d0 = fd(zc)
    _, B = fd(D)
    if Y is None:
        q = 1 / d0
        Y = acb(q.real.mid(), q.imag.mid())
    K = zc - Y * f0 + (1 - Y * B) * (D - zc)
    ok = bool(D.real.contains_interior(K.real) and D.imag.contains_interior(K.imag))
    return dict(ok=ok, K=K, D=D, f0=f0, B=B)


def certify_zero(fd, z0, radii=(1e-3, 1e-5, 1e-8, 1e-12, 1e-20), want_off_line=0.5):
    """Try Krawczyk on a sequence of shrinking squares around z0 (should already be a good approximation).

    Returns the tightest successful certificate dict with fields
      ok, re_lo, re_hi, im_lo, im_hi (as decimal strings), radius_used, off_line (bool: Re-enclosure excludes
      want_off_line), and the side on which it lies.
    The FIRST successful square proves existence+uniqueness in that square; smaller squares refine.
    """
    best = None
    first = None
    for r in radii:
        try:
            res = krawczyk(fd, z0, r)
        except Exception as e:  # noqa
            continue
        if res['ok']:
            K = res['K']
            rec = dict(ok=True, radius_used=r,
                       re_mid=K.real.mid().str(30, radius=False), re_rad=float(K.real.rad()),
                       im_mid=K.imag.mid().str(30, radius=False), im_rad=float(K.imag.rad()),
                       re_lo=K.real.lower().str(25, radius=False), re_hi=K.real.upper().str(25, radius=False),
                       im_lo=K.imag.lower().str(25, radius=False), im_hi=K.imag.upper().str(25, radius=False))
            if want_off_line is not None:
                c = arb(want_off_line)
                rec['off_line'] = bool(K.real > c or K.real < c)
                rec['re_minus_half_lower_bound'] = (K.real - c).lower().str(15, radius=False)
            if first is None:
                first = dict(rec)
            best = rec
            # refine centre using the enclosure midpoint for the next (smaller) radius
            z0 = complex(float(K.real.mid()), float(K.imag.mid()))
    if best is None:
        return dict(ok=False)
    best['uniqueness_square_radius'] = first['radius_used']
    return best


def newton_polish(fd, z, steps=40, tol=1e-25):
    """NON-RIGOROUS Newton iteration on ball midpoints. Returns complex (python) or None."""
    zc = acb(z.real, z.imag)
    for _ in range(steps):
        f, d = fd(zc)
        step = f / d
        zc = acb(zc.real.mid(), zc.imag.mid()) - acb(step.real.mid(), step.imag.mid())
        if abs(complex(step)) < tol:
            break
    f, _ = fd(zc)
    return complex(float(zc.real.mid()), float(zc.imag.mid())), abs(complex(f))


def series_eval(F, z):
    """Evaluate (F(z), F'(z)) where F maps an acb_series (length 2) to an acb_series."""
    s = acb_series([z, 1], prec=2)
    c = F(s).coeffs()
    while len(c) < 2:
        c.append(acb(0))
    return c[0], c[1]


def scan_minima(fval, sig_grid, t_grid):
    """NON-RIGOROUS: local minima of |f| on a rectangular grid (python floats). Returns list of (s, |f|)."""
    import numpy as np
    A = np.zeros((len(sig_grid), len(t_grid)))
    for i, sg in enumerate(sig_grid):
        for j, tt in enumerate(t_grid):
            A[i, j] = abs(complex(fval(acb(sg, tt))))
    mins = []
    for i in range(len(sig_grid)):
        for j in range(1, len(t_grid) - 1):
            v = A[i, j]
            nb = [A[i, j - 1], A[i, j + 1]]
            if i > 0:
                nb += [A[i - 1, j], A[i - 1, j - 1], A[i - 1, j + 1]]
            if i < len(sig_grid) - 1:
                nb += [A[i + 1, j], A[i + 1, j - 1], A[i + 1, j + 1]]
            if v <= min(nb):
                mins.append((complex(sig_grid[i], t_grid[j]), v))
    return mins


def winding_number(fval, corners, n_per_edge=400):
    """NON-RIGOROUS argument-principle count of zeros inside the polygon `corners` (python complex list),
    using midpoint evaluations. Returns float (should be near an integer)."""
    import cmath
    pts = []
    for a, b in zip(corners, corners[1:] + corners[:1]):
        for k in range(n_per_edge):
            pts.append(a + (b - a) * k / n_per_edge)
    vals = [complex(fval(acb(p.real, p.imag))) for p in pts]
    tot = 0.0
    for u, v in zip(vals, vals[1:] + vals[:1]):
        tot += cmath.phase(v / u)
    return tot / (2 * cmath.pi)


def versions():
    import sys, mpmath, numpy
    return dict(python=sys.version.split()[0], python_flint=flint.__version__, mpmath=mpmath.__version__,
                numpy=numpy.__version__)
