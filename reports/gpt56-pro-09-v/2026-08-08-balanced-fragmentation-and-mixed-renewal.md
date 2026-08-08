# Balanced fragmentation continuation of the carry route

Agent: `gpt56-pro-09-v`  
Date: 2026-08-08  
Issue: #238  
PR: #247  
Status: **SERIOUS CONDITIONAL ARCHITECTURE; ONE SIGN THEOREM OPEN; RH NOT PROVED**

## 1. Outcome

The Gamma coupling was not upgraded to an independent convolution factor. The
compactness theorem correctly shows that sharp scalar FGCM collapses back to the
canonical Möbius–Riesz factor GCF.

The productive continuation is instead the atomized Pascal coordinate. The
branch now contains:

1. an exact Möbius-derived node divergence for the critical ramp;
2. an exact equivalence between carry saturation and balanced fragmentation;
3. its balanced-superadditive Farkas dual;
4. an unconditional positive packing with main constant `4 log 2`;
5. an explicit binary–ternary exact signed flow;
6. the weaker weighted-negative-variation theorem `BTF` as the preferred hinge;
7. a stronger frozen `31/32` one-third plus `1/32` half renewal `MPR` as an
   alternative concrete producer;
8. directed finite verification and large reconnaissance, both explicitly
   scoped below theorem level.

There is no genuine unconditional RH proof on this branch.

## 2. Exact divergence theorem

For

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

define

\[
U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
\qquad
R_X(m)=U_X(m)-U_X(m+1).
\]

For a split flow `d_(n,j)`, put

\[
(\partial d)_m
=\sum_jd_{m,j}
 -\sum_{n>m}(d_{n,m}+d_{n,n-m}).
\]

The exact carry load is

\[
L_q(d)=\sum_m(\partial d)_m\lfloor m/q\rfloor.
\]

Möbius inversion and summation by parts give

\[
w_X(q)=\sum_mR_X(m)\lfloor m/q\rfloor.
\]

Therefore

\[
\boxed{
L_q(d)=w_X(q)\text{ for every }q
\iff
\partial d=R_X\text{ on nodes }m\ge2.}
\]

This is the central simplification: the full carry matrix is one finite
fragmentation-divergence problem.

## 3. Farkas dual

For a fixed balance reserve, let the split generators be

\[
g_{n,j}=e_n-e_j-e_{n-j}.
\]

A zero-slack positive flow exists exactly when `R_X` belongs to their positive
cone. Farkas duality gives the alternative

\[
\sum_mR_X(m)\varphi_m\ge0
\]

for every sequence satisfying

\[
\varphi_n\ge\varphi_j+\varphi_{n-j}
\]

on all retained balanced splits. This is exactly the signed common-cell dual of
BCT. It gives reviewers both a primal construction target and a scalar
counterexample interface.

## 4. Unconditional progress: one positive pass

The first differences

\[
a_X(n)=w_X(n)-w_X(n+1)
\]

are nonnegative. Assigning `a_X(n)` to the central split of row `n` is always
feasible because each atomized carry coefficient is `0` or `1`:

\[
L_q\le\sum_{n\ge q}a_X(n)=w_X(q).
\]

The central entropy then gives

\[
\boxed{
\sum_na_X(n)\log\binom n{\lfloor n/2\rfloor}
=4(\log2)\sqrt X+O(\log^2X).}
\]

Thus the route has an unconditional positive prime-ramp theorem with constant
`4 log 2`. Among all fixed one-pass split ratios the constant is `4H(u)` and is
maximized at one half. The remaining gap is exactly the reuse of residual carry
capacity needed to raise `log 2` to `1`.

## 5. Explicit descending producers

For a probability law `pi_n` on balanced children, the descending recurrence

\[
d_X(n)=R_X(n)+
\sum_{m>n}d_X(m)[\pi_m(n)+\pi_m(m-n)]
\]

satisfies `partial d_X=R_X` identically. If its coefficients are nonnegative,
it is an exact zero-slack carry packing.

### Preferred weaker theorem: BTF

The concurrent binary–ternary producer uses the frozen half/half law and permits
signed coefficients. Its open theorem is the weighted negative-variation bound

\[
\sum_n\sqrt n\,(-d_X(n))_+=X^{o(1)}.
\]

The branch supplies a conditional repair from this ledger to a positive packing
and the sharp prime ramp. That repair must be reconstructed independently; in
particular, taking the positive part of an exact signed flow is not by itself a
feasible packing.

### Stronger alternative: MPR

The asymmetric law

\[
\pi_n=\frac{31}{32}\delta_{\max(1,\lfloor n/3\rfloor)}
      +\frac1{32}\delta_{\lfloor n/2\rfloor}
\]

has a single open pointwise theorem

\[
\boxed{d_X(n)\ge0\quad(2\le n\le X).}
\]

If true, it gives exact zero-slack BCT directly. Pure halving fails at a finite
endpoint, and pure one-third splitting also eventually fails in reconnaissance;
the mixture must therefore be treated as one recombined renewal.

A directed `Decimal` checker certifies the frozen recurrence at `X=4096`. A
separate standard-library scan reports no negative coefficient at the listed
endpoints through `10^8`. Neither computation is a cofinal proof.

## 6. Continuum warning

For a fixed self-similar branching law `pi`, the formal continuum renewal has
Laplace transform

\[
\widehat f(s)=
\frac{s-1}
{(s-\tfrac32)^2\zeta(s-1)[1-M_\pi(s)]},
\]

where

\[
M_\pi(s)=\int
[\alpha^{s-1}+(1-\alpha)^{s-1}]d\pi(\alpha).
\]

For the asymmetric mixed producer,

\[
M_\pi(s)=
\frac{31}{32}
\left[3^{1-s}+(2/3)^{s-1}\right]
+rac1{32}2^{2-s}.
\]

The fixed renewal changes the `2`--`3` geometry but does not cancel generic
zeta zeros. Large finite positivity therefore cannot be extrapolated by a
phase-blind estimate. A proof of MPR must be genuinely strip sensitive, or BTF
must exploit lattice cancellation not visible in pointwise continuum
positivity.

## 7. Full conditional RH deduction

Either of the following is sufficient:

1. BTF with its complete positive-repair ledger; or
2. the stronger MPR pointwise sign.

Then the atomized valuation identity gives

\[
\sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}
\log\frac X{p^a}
\ge4\sqrt X-X^{o(1)}.
\]

At `X=N^2`, the exact square-screw formula yields

\[
\Psi(2\log N)\le N^{o(1)}.
\]

Critical square sampling propagates this upper envelope to the half-line. The
one-sided Laplace identity for `xi'/xi`, the upper-envelope Landau theorem, and
functional-equation symmetry then imply RH.

Every arrow after the signed-flow theorem is already isolated on the branch.
The accepted-proof boundary remains the signed-flow theorem itself.

## 8. Canonical review order

Follow `M-23803`. In particular, review canonical IDs `L-23810` through
`L-23815`, then `T-23803`, and treat duplicate temporary paths listed in
`M-23803` as superseded.

## 9. Final classification

```text
exact carry and entropy identities               PROPOSED EXACT
exact Möbius divergence                          PROPOSED EXACT
balanced-fragmentation/Farkas equivalence         PROPOSED EXACT
unconditional 4 log(2) packing                   PROPOSED EXACT
binary–ternary exact signed flow                 PROPOSED EXACT
BTF weighted negative variation                  OPEN / LOAD BEARING
MPR pointwise mixed-renewal sign                  OPEN / STRONGER ALTERNATIVE
conditional deduction to RH                      COMPLETE PROPOSAL
accepted proof of RH                              NO
```

The branch is now easier to review and more concrete than generic BCT, but it is
not yet a genuine unconditional RH proposal.
