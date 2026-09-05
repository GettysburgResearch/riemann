# R-105109 — Bounded selector norm does not control the quotient edge

Claim ID: R-105109

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105106; R-105106; L-105107; L-105109

RH status: **unproved**

## Refuted inference

The following implication is false:

> If the actual interior event topology, target residue data, and optimal
> selector norms remain controlled, then the selector-weighted absolute
> edge envelope remains controlled.

## Exact counterfamily

On the unit disk let

\[
F_s(z)=\exp\!\left(\frac{z^2}{2}-\frac{z^4}{4s}\right),
\qquad
1<s<\frac{5+\sqrt{17}}4.
\tag{R-105109.1}
\]

The first quotient has the fixed complete interior manifest consisting only
of the simple target zero.  Its target principal coefficient and optimal
selector are

\[
q_{1,0}=1,
\qquad
W_{1,s}=1,
\qquad
\tau_1=1.
\tag{R-105109.2}
\]

For the second quotient, let \(\alpha(s)\in(0,1)\) be the unique interior
root of

\[
P_s(x)=x^3-2sx^2+(s^2-3s)x+s^2.
\tag{R-105109.3}
\]

Its complete interior manifest consists of the same simple target zero and
the two simple nontargets \(\pm\sqrt{\alpha(s)}\).  The target coefficient
and optimal selector are

\[
q_{2,0}=1,
\qquad
W_{2,s}(z)=
\frac{\alpha(s)-z^2}
{\alpha(s)(1-\alpha(s)z^2)},
\qquad
\tau_2(s)=\frac1{\alpha(s)}.
\tag{R-105109.4}
\]

As \(s\downarrow1\),

\[
\tau_2(s)\longrightarrow\frac{3+\sqrt5}{2}.
\tag{R-105109.5}
\]

Thus both selector norms stay bounded.  Nevertheless, at the regular
boundary point one,

\[
\frac{F_s}{F_s'}(1)=\frac{s}{s-1},
\qquad
\frac{F_s^2}{F_s'F_s''}(1)
=\frac{s^3}{(s-1)(2s^2-5s+1)},
\tag{R-105109.6}
\]

so both unweighted quotients and both optimally weighted boundary suprema
diverge.  The exterior critical points \(\pm\sqrt s\) approach the unit
circle without entering the complete interior manifest.

## Finite-jet strengthening

The finite-jet exponential gauges in L-105109 preserve any prescribed collection
of interior zeros and jets while forcing \(F'\) or \(F''\) to vanish at a
chosen boundary point.  Hence finite local data cannot certify the missing
edge margin.  This strengthening is deliberately not claimed to preserve
the derivative-event manifest.

## What is not refuted

For both quotients in (R-105109.1), the optimally weighted *full contour*
integral remains exactly one by residues.  The counterfamily does not rule
out cancellation across oriented edges.  It refutes only a closure based on
selector conditioning plus absolute/supremum edge bounds.

The Xi programme therefore still needs an exterior-collar/lower-margin
estimate or a genuinely phase-sensitive edge-cancellation theorem.  No
RCMV104530 or RH conclusion follows.

The moving nontarget locations are not claimed identical, and the zero-free
order-four family is not claimed to model Xi growth.  The refutation is
confined to the stated finite boundary-sup inference.
