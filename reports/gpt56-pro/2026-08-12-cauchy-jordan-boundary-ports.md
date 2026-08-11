# Cauchy–Jordan continuation: compact arithmetic gate and exact boundary ports

## Status

```text
repository: gfreund123/riemann
branch:     research/gpt56-pro/91008-cauchy-square-clark-jordan
PR:         #396
RH:         UNPROVED
```

This report supersedes the frontier section of the earlier weighted-FKG report. It incorporates the repaired large-scale argument, the small-scale scaling theorem, the completed safe-side Stinespring factor, and the exact critical-boundary residue classification.

## 1. All finite Green divisions are positive

For

\[
F_s(n)=\prod_{p\mid n}(1-p^{-s}),
\qquad c_s=\zeta(1+s)^{-1},
\]

weighted Harris–FKG gives, for every nonnegative decreasing test `h`,

\[
\sum_{n\le N}\frac{F_s(n)}n h(n)
\ge
\prod_{p\le N}(1-p^{-1-s})
\sum_{n\le N}\frac{h(n)}n.
\]

Consequently

\[
E_{s,m}(t)
=\sum_n\frac{F_s(n)}n\frac{(t-\log n)_+^m}{m!}
-c_s\frac{t^{m+1}}{(m+1)!}
\ge0
\]

for every integer `m>=0`, and

\[
\frac{Z_s(q)-c_s/q}{q^{m+1}}
=\int_0^\infty e^{-qt}E_{s,m}(t)\,dt
\]

is completely monotone. This includes the full phase-resolved safe-side Hankel hierarchy.

## 2. The Cauchy target is an explicit causal Hardy direct integral

Every storage residual has the exact representation

\[
F_m(u^2/a^2)=\int_0^\infty|\Psi_{m,a,r}(iu)|^2\,dr,
\]

with

\[
\Psi_{m,a,r}(z)
=\sqrt{(m+2)!W_m(r)}\,a^{m+2}
\frac{z}{(z+a\sqrt r)^{m+3}}.
\]

The inverse Laplace transform is a causal exponential polynomial with zero total mass. The target Hilbert space of the desired intertwiner is therefore canonical.

The original three-state all-pass is fixed-orthogonally conjugate to the symmetric square of one two-state rotation. There is only one genuine scalar phase; the neutral coordinate is the mixed symmetric-square state.

## 3. Exact final Green removal

Let

\[
\kappa=\sqrt{275/14}.
\]

After applying the sharp Cauchy numerator to the centered three-Green Jordan channel with `s=2a`, the complete arithmetic measure consists of:

```text
one positive contact of mass 1 at t=0;
positive atoms F_(2a)(n)/n at t=log n, n>=2;
one continuous density.
```

The density is

\[
\boxed{
\mathcal B_{2a,a}(t)
=-c_{2a}+\kappa aE_{2a,0}(t)+4a^2E_{2a,1}(t).
}
\]

There is no further arithmetic boundary port.

Between logarithmic knots the density is concave, and every knot creates an upward jump. Therefore its minima occur at knot left limits.

## 4. Rigorous positive regions

### First logarithmic cell

For every `a>0`,

\[
\mathcal B_{2a,a}(t)>0
\qquad(0\le t\le\log2).
\]

### Explicit large-time region

For every `a>0`,

\[
\mathcal B_{2a,a}(t)>0
\]

once

\[
t>
T(a)=
\frac{[1-\kappa a(1-\log2)-2a^2(\log2)^2]_+}
     {4a^2(1-\log2)}.
\]

### All sufficiently small scales

With `s=2a`, define

\[
e_s(y)=E_{s,0}(y/s),
\qquad I_s(y)=sE_{s,1}(y/s).
\]

Positive-measure Laplace convergence gives

\[
e_s(y)\,dy\Longrightarrow dy,
\qquad I_s(y)\to y
\]

locally uniformly in the integrated variable. The monotonicity of

\[
e_s(y)+(c_s/s)y
\]

upgrades this to a uniform lower bound away from zero; the unit atom controls the origin. Hence there exists `a_0>0` such that

\[
\mathcal B_{2a,a}(t)>0
\qquad(0<a<a_0,\ t\ge0).
\]

This theorem is currently non-effective.

### Every scale `a>=1/3`

The unit atom gives positivity whenever

\[
r_s:=\frac1{s\zeta(1+s)}\le\frac1{\sqrt2}.
\]

The repaired proof shows that

\[
G(s)=s\zeta(1+s)
\]

is strictly increasing for `s>=2/3`. An exact rational lower certificate proves

\[
G(2/3)>1.414214>\sqrt2.
\]

Therefore

\[
\boxed{
\mathcal B_{2a,a}(t)>0
\qquad(a\ge1/3,\ t\ge0).
}
\]

The first version of this argument used an invalid double-counted integral bound. That proof has been removed and replaced by the monotonicity argument plus the exact finite certificate.

## 5. The arithmetic frontier is compact

Combining the small- and large-scale theorems, any unresolved arithmetic Green-removal failure must lie in

\[
\boxed{
a_0\le a<1/3.}
\]

For each such `a`, the time variable is further restricted to

\[
\boxed{\log2<t\le T(a).}
\]

Thus the remaining arithmetic gate is compact in both scale and logarithmic time.

Finite reconnaissance through `N=20,000` at nine representative scales found the minimum of the density at the first knot in every case. This is evidence only, not a proof of the compact middle band.

## 6. Prime-local complete positivity

Adjoining one local Euler factor preserves Green-removed complete monotonicity exactly. If `P` is a finite prime set and `p` is new, then the transformed centered channel satisfies

\[
T_{P\cup\{p\}}
=L_{p,s}T_P
+c_P(L_{p,s}-c_{p,s})
\left(\frac1q+\frac{A+B}{q^2}+\frac{AB}{q^3}\right),
\]

and every factor on the right is completely monotone whenever `T_P` is. No bad local prime factor exists; any remaining arithmetic obstruction is an infinite-tail/base phenomenon.

## 7. The completed safe-side Stinespring factor

Whenever `B_(2a,a)>=0`, the completed rational and beta/Gamma factors and the six Cauchy denominator states are positive convolution channels. The safe transfer therefore has the explicit positive representing measure

\[
\mu_a=r_{2a}*b_{2a}*g_a*\omega_a,
\]

where

\[
\omega_a
=\delta_0
+\sum_{n\ge2}\frac{F_{2a}(n)}n\delta_{\log n}
+\mathcal B_{2a,a}(t)dt.
\]

No existential square root or hidden safe-side port remains.

## 8. Why safe positivity does not yet reach the critical line

The critical Clark ratio corresponds to

\[
q=-\frac12-a+ix,
\]

not to the ordinary Hardy boundary `q=ix`. The positive safe measure encounters the deterministic pole `q=-a` before the critical line, and its positive arithmetic atoms do not possess the required exponential moment. Thus a naïve positive-Laplace continuation is invalid.

The final map must be a conservative scattering, Darboux, or contour-deformation identity retaining every crossed residue.

## 9. Exact residue-port dictionary

A zero

\[
\rho=\frac12+d+i\gamma
\]

creates a denominator pole at

\[
q_\rho=-\frac12+d-2a+i\gamma.
\]

Relative to the critical contour `Re q=-1/2-a`,

\[
\Re q_\rho-(-1/2-a)=d-a.
\]

Therefore the horizontal continuation crosses exactly the zeros with

\[
\boxed{d>a.}
\]

Critical-line zeros remain to the left. The deterministic Cauchy poles crossed are:

```text
q=-a          for every a;
q=-2a         for 0<a<1/2;
q=-4a         for 0<a<1/6.
```

These are finite causal states. Every crossed off-line zero contributes one hyperbolic expanding/contracting port. At its matching ordinate the block degenerates to the negative rank-one witness.

The correct conservative identity must therefore have the form

```text
safe positive source Gram
 = critical Cauchy Gram
 + deterministic stable ports
 + crossed hyperbolic zero ports.
```

Under RH the last term is absent. Proving its absence is RH-equivalent; it cannot be discarded as a contour remainder.

## 10. Exact first storage wavelet

The first stored innovation is

\[
F_1(y)
=-\frac1{(y+1)^2}
+\frac{17}{(y+4)^2}
-\frac{16}{(y+16)^2}.
\]

Its physical kernel is a three-scale `(-1,17,-16)` exponential combination with zero total mass and exactly one sign change. Its stop-loss primitive is nonnegative. This gives a concrete one-switch wavelet for future Abel/transport attacks on the compact middle band.

## Verification

The corrected exact replay is:

```text
PASS_CORRECTED_GREEN_REMOVAL_THRESHOLD
checks: 692
exact cube-root checks: 60
exact partial-fraction checks: 606
rational zeta lower bound: 1.4145820168946852
one-switch root: 1.16460697887362936439290091796
minimum terminal barrier margin: 0.002935310614434756...
```

The older broad replay retains 531 exact weighted-FKG instances and floating density reconnaissance. Its finite scans are not used as analytic proof.

## Final boundary

```text
all finite Green divisions                         PROPOSED COMPLETE
canonical Hardy-square target                      EXACT
minimal two-state all-pass geometry                EXACT
unique arithmetic Green-removal density            EXACT
small-scale density positivity                     PROPOSED COMPLETE
large-scale density positivity a>=1/3              PROPOSED COMPLETE
prime-local preservation                           EXACT
completed safe-side Stinespring factor             EXACT CONDITIONAL ON DENSITY
compact middle arithmetic density                  OPEN
critical conservative contour/Darboux identity     OPEN
crossed hyperbolic port exclusion                   OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
