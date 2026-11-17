#!/usr/bin/env python3
"""SKEPTIC replay for C2 (independent of zoo_common.py): rigorous argument-principle certificate.

Method (different from the investigator's Krawczyk test):
  For a closed axis-parallel rectangle R and a function F holomorphic on a neighbourhood of R, given by an
  Arb enclosure routine F(ball) valid for every point of the input ball, split the boundary into segments
  (adaptively).  For each segment S the enclosure B = F(S) must exclude 0 (real or imaginary part of the
  rectangle B excludes 0).  Then F(S) lies in an open half-plane through 0, so the continuous change of
  arg F along S lies in (-pi, pi) and equals Arg(F(b)/F(a)) (principal value).  Summing the Arb enclosures
  of these principal arguments gives an enclosure of 2*pi*(number of zeros in R, with multiplicity).
  Certified if that enclosure divided by 2*pi contains exactly one integer.
"""
import flint
from flint import acb, arb


def _excludes0(B):
    return bool(B.real > 0 or B.real < 0 or B.imag > 0 or B.imag < 0)


def seg_ball(a, b):
    """Arb ball containing the axis-parallel segment from a to b (python complex / exact floats)."""
    mx, my = (a.real + b.real) / 2, (a.imag + b.imag) / 2
    rx, ry = abs(b.real - a.real) / 2, abs(b.imag - a.imag) / 2
    return acb(arb(mx, rx), arb(my, ry))


def winding(F, x0, x1, y0, y1, nseg=16, maxdepth=14):
    corners = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]
    total = arb(0)
    nevals = 0
    stack = []
    for k in range(4):
        a, b = corners[k], corners[(k + 1) % 4]
        for j in range(nseg):
            stack.append((a + (b - a) * j / nseg, a + (b - a) * (j + 1) / nseg, 0))
    fcache = {}

    def Fpt(z):
        if z not in fcache:
            fcache[z] = F(acb(z.real, z.imag))
        return fcache[z]
    while stack:
        a, b, dep = stack.pop()
        B = F(seg_ball(a, b)); nevals += 1
        if _excludes0(B):
            fa, fb = Fpt(a), Fpt(b)
            total += (fb / fa).arg()
        else:
            if dep >= maxdepth:
                return dict(ok=False, reason='segment enclosure contains 0', seg=[str(a), str(b)], nevals=nevals)
            m = (a + b) / 2
            stack.append((a, m, dep + 1)); stack.append((m, b, dep + 1))
    w = total / (2 * arb.pi())
    n = round(float(w.mid()))
    ok = bool(w.rad() < 0.5 and abs(float(w.mid()) - n) + float(w.rad()) < 0.5)
    return dict(ok=ok, count=n, enclosure=w.str(10), nevals=nevals)


def winding_taylor(Fser, x0, x1, y0, y1, nseg=16, maxdepth=12):
    """Same certificate, but segment enclosures by a rigorous Taylor (mean-value) form:
    for a segment with centre c and half-length l,  F(c+w) in F(c) + w F'(c) + disc(M l^2 / 2),
    |w| <= l, where M >= sup |F''| over the whole rectangle R (one Arb series evaluation on the
    rectangle ball; Taylor remainder: |F(c+w)-F(c)-wF'(c)| <= |w|^2/2 sup_R |F''|, R convex).
    Fser(z, n) must return Arb enclosures [F(z), F'(z), ..., F^{(n-1)}(z)/(n-1)!] (Taylor coefficients)
    valid for every point of the input ball z."""
    Rball = acb(arb((x0 + x1) / 2, (x1 - x0) / 2), arb((y0 + y1) / 2, (y1 - y0) / 2))
    c3 = Fser(Rball, 3)
    M = 2 * abs(c3[2]).upper()             # sup |F''| <= 2 * sup |coefficient of w^2|
    corners = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]
    total = arb(0)
    nevals = 0
    stack = []
    for k in range(4):
        a, b = corners[k], corners[(k + 1) % 4]
        for j in range(nseg):
            stack.append((a + (b - a) * j / nseg, a + (b - a) * (j + 1) / nseg, 0))
    cache = {}

    def P(z):
        if z not in cache:
            cache[z] = Fser(acb(z.real, z.imag), 2)
        return cache[z]
    while stack:
        a, b, dep = stack.pop()
        c = (a + b) / 2
        l = abs(b - a) / 2
        f0, f1 = P(c); nevals += 1
        w = acb(arb(0, l), arb(0, l))      # covers the segment offsets (and more)
        rem = M * arb(l) ** 2 / 2
        B = f0 + w * f1 + acb(arb(0, rem), arb(0, rem))
        if _excludes0(B):
            fa, fb = P(a)[0], P(b)[0]
            total += (fb / fa).arg()
        else:
            if dep >= maxdepth:
                return dict(ok=False, reason='segment enclosure contains 0', M=float(M), nevals=nevals)
            stack.append((a, c, dep + 1)); stack.append((c, b, dep + 1))
    wnd = total / (2 * arb.pi())
    n = round(float(wnd.mid()))
    ok = bool(wnd.rad() < 0.5 and abs(float(wnd.mid()) - n) + float(wnd.rad()) < 0.5)
    return dict(ok=ok, count=n, enclosure=wnd.str(10), nevals=nevals, M_bound_F2=float(M))
