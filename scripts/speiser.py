"""
speiser.py -- certified zero counting for zeta', i.e. Speiser's criterion.

Agent: claude-01
Implements: the computational side of C-0002 / X-0008.

SPEISER'S THEOREM (1935).  The Riemann hypothesis is equivalent to

    zeta'(s) has no zeros in the open strip  0 < Re(s) < 1/2.

This is a completely different object from everything else in the repository.
It replaces the question "are the zeros of zeta on the line?" -- which needs
either a count of zeros in a box straddling the line (T-0001), or a match
between two counts (L-0004) -- with the question "is a certain region EMPTY?".
An empty region is the easiest thing an argument principle can certify: the
winding number is 0 and nothing has to be located.

And the failure mode is the best possible: **a single certified zero of zeta'
with 0 < Re(s) < 1/2 disproves RH**, and certifying it is exactly the
interval-Newton test of L-0007 pointed at that zero.

HOW zeta' IS COMPUTED

From eta(s) = (s-1) zeta(s):  eta' = zeta + (s-1) zeta', so

    zeta'(s) = eta'(s)/(s-1) - eta(s)/(s-1)^2 ,

valid on any ball avoiding s = 1.  Both eta and eta' are available as certified
Taylor-model enclosures (L-0006), so zeta' is too, and the winding machinery of
L-0002 applies verbatim.

CAUTION.  Speiser's equivalence is a global statement.  Certifying the strip
empty up to height T does NOT prove RH up to height T by itself -- what the
local version buys needs the Levinson-Montgomery quantitative form, which this
agent has not verified.  See the CITATION FLAG in X-0008.  The refutation
direction, however, is clean: a zero of zeta' strictly inside 0 < Re s < 1/2 is
incompatible with RH.
"""

from __future__ import annotations

import sys

from flint import acb, arb

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import certzeta as cz  # noqa: E402

__all__ = ["zeta_prime_ball", "zeta_prime_point"]


def _centre_radius(B: acb):
    c = acb(arb(B.real.mid()), arb(B.imag.mid()))
    r = max(float(B.real.rad()), float(B.imag.rad()))
    return c, r


def zeta_prime_ball(B: acb) -> acb:
    """Certified enclosure of zeta' over the ball B (which must avoid s = 1).

    Uses the Taylor-model enclosures of eta and eta' when B has a positive
    radius, and the exact point routine when it does not."""
    c, r = _centre_radius(B)
    if (B - 1).abs_lower() <= arb(2) ** (-cz.ctx.prec // 2):
        raise ValueError("ball touches s = 1")
    if r == 0.0:
        e, ep = cz.eta_and_deta(c)
    else:
        e = cz.eta_taylor_ball(c, r)
        ep = cz.eta_deriv_ball(c, r)
    return ep / (B - 1) - e / (B - 1) ** 2


def zeta_prime_point(s: acb) -> acb:
    e, ep = cz.eta_and_deta(s)
    return ep / (s - 1) - e / (s - 1) ** 2
