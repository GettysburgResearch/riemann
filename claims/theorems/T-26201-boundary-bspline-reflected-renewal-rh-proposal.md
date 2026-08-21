# T-26201 — Boundary-B-spline reflected-renewal proposal for RH

Claim ID: `T-26201`  
Title: A source-specific reflected contraction for the aligned boundary B-spline forces the reciprocal-zeta Hardy exponent to vanish  
Status: **FULL PROPOSAL — GAP/BLOCKED ONLY AT `L-26203`; RH NOT PROVED**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`–`L-26203`; fixed-ratio shell Hardy/Mellin transfer; the zeta functional equation

## 1. Exact RH detector

Fix `R>=0` and use the positive compact exponential B-spline signal

\[
 U_R(t)=
 \sum_{n\ge1}\frac{\mu(n)}{\sqrt n}
 \mathcal B_R(t-\log n).
 \tag{T-26201.1}
\]

Its Laplace transform is

\[
 \boxed{
 \widehat U_R(z)
 =\frac{(1-2^{-z})^{R+2}
        (1-\sqrt2\,2^{-z})^{R+1}}
       {z^{R+2}(z-\frac12)^{R+1}
        \zeta(z+\frac12)}.}
 \tag{T-26201.2}
\]

The numerator zeros lie only on `Re z=0` and `Re z=1/2`. Therefore no zero of
`zeta(s)` with

\[
 \frac12<\Re s<1
 \tag{T-26201.3}
\]

is canceled by the boundary multiplier.

The signal is a fixed-ratio Möbius shell: its window is nonzero, compact, and
supported on a multiplicative interval of ratio `2^(2R+3)`. It retains the
coherent Mertens mode rather than averaging it away.

## 2. Consequence of `BSRC`

Put

\[
 B=\frac14\log2,
 \qquad
 \delta=\frac34\log2.
 \tag{T-26201.4}
\]

Assume `L-26203`, so for some fixed `R,M` one has

\[
 \mathcal E_{R,M}(J)
 \le C(1+J)^A
 +\theta\left[
  1+\max_{u\le J-\delta}
  \mathcal E_{R,M}(u)
 \right],
 \qquad 0<\theta<1,
 \tag{T-26201.5}
\]

where every graph energy is integrated over a block of length `B`.

Absorb the finitely many initial blocks into one constant. Iteration over the
fixed strict delay `delta` gives

\[
 \boxed{
 \mathcal E_{R,M}(J)=O_{R,M}((1+J)^{A+1}).}
 \tag{T-26201.6}
\]

Covering `[0,X]` by `O(X/B)` short blocks yields

\[
 \int_0^X|U_R(t)|^2dt=\exp(o(X)).
 \tag{T-26201.7}
\]

The asymptotic version `L-26203.8` yields the same conclusion by first choosing
one order for which the final contraction constant is strictly below one.

## 3. Hardy continuation

Equation (T-26201.7) implies

\[
 e^{-\sigma t}U_R(t)\in L^2(0,\infty)
 \qquad(\sigma>0).
 \tag{T-26201.8}
\]

Paley-Wiener/Hardy theory for one-sided Laplace transforms therefore makes
`widehat U_R` holomorphic in every half-plane `Re z>sigma`; hence throughout

\[
 \boxed{\Re z>0.}
 \tag{T-26201.9}
\]

The identity (T-26201.2), initially valid in its absolute-convergence
half-plane, extends there by uniqueness.

If `rho` were a nontrivial zeta zero with `Re rho>1/2`, then

\[
 z_\rho=\rho-\frac12
 \tag{T-26201.10}
\]

would lie in `Re z>0`. The boundary numerator is nonzero at `z_rho` by
Section 1, so the right side of (T-26201.2) would have an uncancelled pole. This
contradicts (T-26201.9).

Thus

\[
 \zeta(s)\ne0
 \qquad(\Re s>1/2).
 \tag{T-26201.11}
\]

Functional-equation and conjugation symmetry give the reflected exclusion, and
all nontrivial zeros lie on the critical line:

\[
 \boxed{\mathrm{RH}.}
 \tag{T-26201.12}
\]

## 4. Independent carry replay

For `R=0`, equation `L-26201.34` identifies the detector with a dyadically
filtered differential image of the exact carry profile `mathfrak C`. Hence the
same theorem also gives the square-root carry/entropy minorant and the exact
prime-ramp lower bound through the retained carry-Möbius inversion.

This is a replay, not an additional assumption. The direct Hardy argument in
Sections 1--3 is the shortest consumer.

## 5. Why the proposal is not the frozen conditional-Hankel proof

The proof spine is now

```text
exact carry-Mobius inversion
-> positive compact exponential B-spline
-> eta-aligned finite forcing
-> exact parity renewal
-> Peano boundary B-spline expansion
-> source-specific reflected graph contraction BSRC
-> subexponential fixed-ratio shell energy
-> RH.
```

The false implication

```text
alternating derivatives
-> conditional Hankel PSD
```

is nowhere used.

## 6. Exact review boundary

The deductions in this theorem are complete conditional on `L-26203`.
`L-26203` is presently open. Therefore:

```text
boundary B-spline construction      PROPOSED EXACT
aligned source and digital renewal  PROPOSED EXACT
Peano boundary expansion            PROPOSED EXACT
BSRC source contraction             OPEN / RH-BEARING
conditional deduction to RH         COMPLETE
Riemann Hypothesis                   UNPROVED
```

A reviewer should focus on the finite source LMI `L-26203.11`. Failure of that
LMI rejects the proposal without affecting the exact carry, B-spline, or renewal
identities.
