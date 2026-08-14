# Fractional-string renormalization and the near-cut frontier

Date: 2026-08-14  
Branch: `research/gpt56-pro/92300-fractional-string-renormalization`  
Parent: PR #460 at `db9a767e312d9928f5ef827762dcb4ef95494af0`  
Status: draft research; **RH remains unproved**

## Executive result

The safe Xi impedance has a universal renormalization limit:

\[
\frac{\log(x/2\pi)}{2x}Z(x^2u)
\longrightarrow\sqrt u.
\]

More accurately, its first correction is another passive fractional power
`u^(alpha_x)`, with

\[
\alpha_x=\frac12-rac1{2\log(x/2\pi)}.
\]

The complete fixed-order Loewner/Hankel hierarchy therefore becomes positive
on the high safe axis.  A projected-zero frame gives a proposed growing-order
version through

\[
n\ll\sqrt{\frac{\log x}{\log\log x}}.
\]

The same analysis exposes the exact remaining geometry: an off-line zero of
height `b` and depth `a` becomes a pole at distance `asymp a/b` from the
negative cut of the limiting fractional string.  It survives in a shrinking
near-cut boundary layer invisible to compact-subset asymptotics.

## 1. Fractional power background

For

\[
p(t)=\frac{(\xi'/\xi)(1/2+\sqrt t)}{\sqrt t},
\qquad Z=1/p,
\]

sectorial Stirling and absolute Euler convergence give

\[
\frac{2x}{\ell_x}p(x^2u)
=u^{-\alpha_x}\left[1+O_K(\ell_x^{-2})+O_K((x\ell_x)^{-1})\right],
\]

where `ell_x=log(x/2pi)`.  Thus the high-axis source is not merely close to a
positive function; it is close to the complete-Bernstein power family.

The positive-string measure is explicit:

\[
u^\alpha=\frac{\sin\pi\alpha}{\pi}
\int_0^\infty\frac{u}{u+s}s^{\alpha-1}ds.
\]

## 2. Exact beta-Hankel law

The derivative moments of the limiting admittance are

\[
c_k(\alpha)=\frac{(\alpha)_k}{k!}.
\]

The relevant Hankel matrix is the moment matrix of

\[
\frac{\sin\pi\alpha}{\pi}q^\alpha(1-q)^{-\alpha}dq
\quad(0<q<1).
\]

Its Selberg determinant is explicit.  At `alpha=1/2`,

\[
\det C_n=2^{-n(2n-1)}.
\]

This identifies the exact universal local object behind all fixed-order
high-axis Xi Loewner matrices.

## 3. Growing order

In scaled squared-pole coordinates, replace each off-line conjugate pair by
its real projection.  Zeros with ordinates in `[x,2x]` produce a positive
moment frame on `q in [1/5,1/2]`.  Moving Fekete bands and Riemann--von Mangoldt
supply the lower moat

\[
\lambda_{\min}(P_{n,x})
\gg\frac{x\log x}{n^2}
\exp[-C n^2\log(n+1)].
\]

The conjugate-pair projection error is quadratic in the critical-strip depth:

\[
\|E_{n,x}\|\ll n^4\frac{\log x}{x}.
\]

Therefore the actual Hankel matrix remains positive whenever

\[
n^2\log(n+1)\le c\log x.
\]

This theorem is proposed complete pending independent review of the band
counts, frame conditioning and global perturbation sum.

## 4. Exact delayed-witness firewall

A finite system with `N` positive real poles and one tiny conjugate pair can
pass every Hankel order through `N+1` and fail exactly at `N+2`.

For the retained rational control

```text
real poles: 1,2,4,8,16,32
complex pair: 100+i, 100-i
pair weight: 10^-12
safe point: t=1
```

orders one through seven are strictly positive, while order eight has the
exact negative determinant recorded in `R-92300`.

This shows that the huge verified critical reserve may postpone the first
full-determinant failure.  It does not by itself remove a sparse off-line pair.

## 5. Relation to Claude's two-thirds theorem

Claude's paper explicitly states that its bandwidth-one first-two-moment
certificate cannot distinguish a sparse exceptional population from no
exceptional population.  The fractional-string result is the safe-axis,
all-order analogue:

```text
fixed interpolation complexity
    -> universal passive background;

single high off-line pair
    -> shrinking near-cut boundary layer.
```

Thus the correct next step is not another fixed derivative or another global
moment.  It is a boundary-layer-resolving positive transfer.

## 6. New final target

`NCFSC` asks for a positive string representation of the renormalised Xi
impedance uniformly down to distance `O(1/x)` from the negative cut.  Any such
source-ordered construction excludes an off-line pole at its natural scale.

Candidate mechanisms:

1. nonconfluent safe Loewner packets geometrically adapted to the cut;
2. a Krein-string Schur complement of the eta/bridge/gamma Julia cascade;
3. a pair-adapted rational microscope with exact positive source norm;
4. a Hardy/Poisson-Fock realization of the homogeneous fractional string plus
   a controlled arithmetic perturbation.

## Verification

The retained replay checks:

- the central-binomial determinant through order eight;
- the exact delayed failure after seven positive orders;
- high-precision convergence toward the drifting fractional-power background.

Verdict:

```text
PASS_FRACTIONAL_STRING_RENORMALIZATION
```

The replay is not a proof of the analytic uniformity, the growing-order result,
NCFSC, complete Bernstein passivity or RH.

## Exact boundary

```text
fractional-string scaling                       PROPOSED COMPLETE
beta-Hankel determinant                         EXACT
growing-order high-axis positivity              PROPOSED COMPLETE
arbitrarily delayed finite-order failure        EXACT
near-cut positive-string completion             OPEN / RH-EQUIVALENT
Riemann Hypothesis                              UNPROVED
```
