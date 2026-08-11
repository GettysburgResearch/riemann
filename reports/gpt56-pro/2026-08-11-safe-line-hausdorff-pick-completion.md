# Single-safe-line Hausdorff/Pick completion

**Date:** 2026-08-11  
**Base:** PR #389 head `cde084ee1f82f7cd750f2b80843b772f177c45fe`  
**Branch:** `research/gpt56-pro/91001-safe-line-hausdorff-pick`  
**RH status:** **unproved**

## Main advance

The normalized one-safe-line scalars

\[
 a_k(x)=\mathfrak S_k(x)/(k+2)!
\]

form a Hausdorff moment sequence under RH:

\[
 a_k(x)=\int_0^1\lambda^k\,d\nu_x(\lambda),
 \qquad
 \lambda=(1+(\gamma-x)^2)^{-1}.
\]

This gives an exact hierarchy of positive beta finite differences, shifted beta-Hankel sum-of-squares matrices, and Bernstein spectral cells. It also packages every order into one Stieltjes/Pick function

\[
 \mathcal A_x(w)=\sum_{k\ge0}a_k(x)w^k.
\]

A matching off-line pair at depth `y` creates an uncancellable pole at

\[
 w=1-y^2\in(3/4,1).
\]

Thus RH is equivalent to unit-disc holomorphy of `A_x` for every centre, or equivalently to coefficient root growth at most one. The analytic radius records zero depth exactly. The reverse implication needs no terminal-pair selection: every individual off-line zero produces its own pole.

## One square-root generating transform

All integer orders sum exactly to

\[
 \mathcal G_s(w)=\frac{
  (2-w)\mathscr X(s+1)-w\mathscr X'(s+1)
  -2\sqrt{1-w}\,\mathscr X(s+\sqrt{1-w})
 }{w^2},
 \qquad \mathscr X=-\xi'/\xi.
\]

The corresponding all-order Euler weight is

\[
 \sum_{k\ge0}\frac{e^{-t}P_k(t)}{(k+2)!}w^k
 =\frac{(2-w+wt)e^{-t}-2\sqrt{1-w}e^{-t\sqrt{1-w}}}{w^2}.
\]

This series is directly absolutely Eulerian exactly throughout the centered disk `|w|<3/4`, because there `Re sqrt(1-w)>1/2`. At `w=3/4` the moving sample reaches `Re(s)=1`; for real `w>3/4` it enters the critical strip. The RH-detecting poles live precisely in the remaining annulus `3/4<w<1`.

## Source-side interface

The beta finite difference

\[
 D_{k,m}=\sum_{j=0}^m(-1)^j\binom mj a_{k+j}
\]

still uses one absolutely convergent Euler line. Its prime weight is

\[
 \Pi_{k,m}(t)
 =\sum_{j=0}^m(-1)^j\binom mj
 \frac{P_{k+j}(t)}{(k+j+2)!},
\]

with the exact Laguerre/Gamma representation

\[
\begin{aligned}
 e^{-t}\Pi_{k,m}(t)
 ={}&\frac{m!}{\sqrt\pi(k+m+2)!}
 \int_0^\infty q^{k+1/2}e^{-q-t^2/(4q)}\\
 &\cdot L_m^{(k+2)}(q)
 \left(1-\frac{t^2}{2q}\right)dq.
\end{aligned}
\]

So Hausdorff differences in derivative order are generalized-Laguerre filters of the first-Hermite heat family.

## Exact firewall

Every nontrivial zero coordinate satisfies

\[
 |1-z^2|>3/4.
\]

Therefore holomorphy on any fixed disk of radius at most `3/4` is unconditional and cannot detect RH. A fixed radius `R<1` excludes only zero depths greater than `sqrt(1-R)`. The cofinal radial limit `R->1` is essential.

## Verification

The retained replay returns

```text
PASS_SINGLE_SAFE_LINE_HAUSDORFF_PICK_COMPLETION
checks: 1270
```

It checks exact finite-difference kernels, line positivity, target parity, 741 exact Bernstein partition cases, synthetic shifted beta-Hankel and Pick matrices, an interior pole at `0.9271`, coefficient root growth toward `1/0.9271`, five high-precision Laguerre/Gamma identities, the square-root Euler generating function, and the exact radial threshold `3/4`.

## Honest frontier

Closed, subject to independent review:

```text
RH -> Hausdorff moment sequence;
all beta finite-difference kernels;
shifted beta-Hankel and Bernstein SOS structure;
unit-disc Stieltjes/Pick representation;
off-line depth -> uncancellable interior pole;
depth-resolved analytic-radius theorem;
Laguerre source transform;
closed square-root all-order transform;
sharp absolute-Euler radius 3/4;
fixed-radius 3/4 firewall.
```

Open:

```text
unconditional prime-side Hausdorff differences;
unconditional shifted beta-Hankel or Pick positivity;
unit-disc Stieltjes continuation through 3/4<|w|<1;
Riemann Hypothesis.
```