# L-105641 — The current–Turán contraction profile has a universal exponential envelope

Claim ID: `L-105641`  
Status: **PROVED EXACT UNIVERSAL SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-105620`, `L-105624`  
RH status: **not assumed**

## 1. Total height and physical scale

Let `Phi` be any positive even source satisfying the hypotheses of
`L-105620`. For a total analytic height `H>0`, put

\[
R_H(\xi)
={H e^{-H\xi}\Lambda_2(\xi)\over j_H(\xi)},
\qquad \xi\ge0,
\tag{L-105641.1}
\]

where

\[
j_H=\widehat J_H.
\]

For a microscope based at height `b>=0` with physical scale `h>0`, the total
height is

\[
H=b+h
\]

and the actual profile is

\[
\boxed{
r_{b,h}(\xi)={h\over H}R_H(\xi).}
\tag{L-105641.2}
\]

No zero-location or log-concavity assumption is needed for the envelope below.
Log-concavity is used separately in `L-105624` to prove monotonicity in `xi`.

## 2. Exact conditional-law formula

Use the exterior-square conditional law of `L-105624`. At sum frequency
`xi>=0`, let `X_xi>0` have density proportional to

\[
x^2\Phi(\xi/2+x)\Phi(\xi/2-x).
\]

Put

\[
U_\xi={\xi\over2}+X_\xi,
\qquad
V_\xi={\xi\over2}-X_\xi.
\]

The positive exponential divided difference is

\[
H_H(u,v)
={e^{2Hu}-e^{2Hv}\over2H(u-v)}.
\]

Since `u+v=xi`, one has the exact factorization

\[
\boxed{
H_H(U_\xi,V_\xi)
=e^{H\xi}
 {\sinh(2HX_\xi)\over2HX_\xi}.
}
\tag{L-105641.3}

The current/exterior-square identity of `L-105624` is

\[
\mathbb E H_H(U_\xi,V_\xi)
=e^{H\xi}{j_H(\xi)\over H\Lambda_2(\xi)}.
\]

Cancelling the common exponential gives

\[
\boxed{
{j_H(\xi)\over H\Lambda_2(\xi)}
=
\mathbb E
 {\sinh(2HX_\xi)\over2HX_\xi}.
}
\tag{L-105641.4}

Therefore

\[
\boxed{
R_H(\xi)
=
{e^{-H\xi}\over
 \displaystyle\mathbb E
 {\sinh(2HX_\xi)\over2HX_\xi}}.
}
\tag{L-105641.5}

This is an exact probabilistic normal form for the canonical source
contraction.

## 3. Universal exponential cap

For every real `z`,

\[
{\sinh z\over z}\ge1,
\]

with strict inequality for `z!=0`. Hence

\[
\boxed{
0<R_H(\xi)\le e^{-H\xi}
\qquad(\xi\ge0).
}
\tag{L-105641.6}

For a nondegenerate positive exterior-square source the inequality is strict.
In the base/scale variables,

\[
\boxed{
0<r_{b,h}(\xi)
\le {h\over b+h}e^{-(b+h)\xi}.
}
\tag{L-105641.7}

Thus the current-normalized first chaos is not merely a contraction in
`[0,1]`; it carries a universal exponential frequency envelope determined by
the complete analytic height.

## 4. Explicit higher-chaos reserve

The elementary inequality

\[
{\sinh z\over z}\ge1+{z^2\over6}
\]

gives the stronger exact bound

\[
\boxed{
R_H(\xi)
\le
{e^{-H\xi}\over
 1+{2\over3}H^2\mathbb E[X_\xi^2]}.
}
\tag{L-105641.8}

This is the conditional-law version of the positive `Lambda_4` reserve in
`L-105620`. No lower bound for `E[X_xi^2]` is asserted here.

## 5. Xi specialization

For the standard Xi source, `L-105640` proves uniform strong log-concavity and
`L-105624` proves that `R_H` is nonincreasing. Consequently the actual Xi
profile has all three properties

```text
0 < R_H <= exp(-H xi);
R_H nonincreasing in xi;
R_H has a strict higher-chaos denominator reserve.
```

These properties are unconditional and source-side. They do not imply the
pointwise physical differential-microscope sign after multiplication by the
variable Xi-prime all-pass phase.

## 6. Scope

The envelope is an exact source theorem. It does not exclude a boundary-near
anti-inner factor: a model-space vector associated with a zero at depth `y`
can concentrate at frequencies of order `1/y`, where the exponentially
weighted charge becomes small. That mechanism is quantified in `L-105642--
L-105643`.