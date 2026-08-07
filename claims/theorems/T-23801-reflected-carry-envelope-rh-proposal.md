# T-23801 — Reflected carry-envelope proposal for RH

Claim ID: `T-23801`  
Title: A two-contact reflected contraction of the finite carry-packing deficit implies the Riemann hypothesis  
Status: **FULL PROPOSED PROOF — `L-23803` IS THE EXPLICIT ADVERSARIAL HINGE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `D-23801`, `L-23801`, `L-23802`, proposed `L-23803`; PR #158 high-order Euler theorem; PR #226 reflected Selberg identity; PR #202 square-screw/Landau transfer  
Scope: full arithmetic proposal; RH is not claimed independently verified

## 1. Finite front door

For every integer `X>=2`, form the carry matrix `B_X`, the prime ramp `w_X`,
and the average binomial entropy values `G_n`. Define the optimal finite packing

\[
 \mathsf C_X
 =\max\left\{
 \sum_{n=2}^Xd(n)G_n:
 d\ge0,\ B_X^Td\le w_X
 \right\}.
 \tag{T-23801.1}
\]

Every term is finite. The coefficients `beta_(nq)` are rational; `w_X` and
`G_n` are finite logarithmic expressions. No zeta zero, contour, operator
domain, or infinite prime tail occurs in the statement.

By the exact carry--Legendre identity,

\[
 \boxed{
 \sum_{q=p^k\le X}\Lambda(q)w_X(q)
 \ge\mathsf C_X.}
 \tag{T-23801.2}
\]

Define the finite deficit

\[
 \mathfrak D_X=(4\sqrt X-\mathsf C_X)_+.
 \tag{T-23801.3}
\]

## 2. Exact curvature reformulation

The Möbius-tail transform of `D-23801` associates to `w_X` a scalar profile
`F_X` such that the exact triangular inverse is

\[
 c_X(n)=(n+1)\Delta^2F_X(n).
 \tag{T-23801.4}
\]

Every positive packing is an admissible convex profile `P`, and

\[
 \sum n d(n)
 =6P(2)+2\sum_{j=4}^XP(j).
 \tag{T-23801.5}
\]

Thus the RH problem is converted into a finite geometric assertion:
construct an admissible convex sub-profile whose area misses the continuum
`4 sqrt(X)` value by only `X^o(1)`.

Exact Carry Saturation would assert `P=F_X`; it is not required.

## 3. Reflected two-contact theorem

Assume `L-23803`: for one fixed `delta in (0,1/3)` and every sufficiently large
fixed packet order `K`,

\[
 \mathfrak D_X
 \le
 X^{2/K+o_K(1)}
 \left[
 1+
 \max_{Y\le X^{1-\delta}e^{O_K(1)}}
 \mathfrak D_Y
 \right].
 \tag{T-23801.6}
\]

The asserted rate comes from the exact reflected Selberg Hermitian square and
the fact that a scalar convex-envelope terminal face has at most two free
contact endpoints. No balanced row is removed by assuming `BTP(K)`.

## 4. Scale contraction

Put

\[
 \vartheta
 =\limsup_{X\to\infty}
 \frac{\log(1+\mathfrak D_X)}{\log X}.
 \tag{T-23801.7}
\]

For fixed `K`, take logarithms in (T-23801.6), divide by `log X`, and pass to a
limsup. The `O_K(1)` endpoint shift disappears and gives

\[
 \vartheta
 \le\frac2K+(1-\delta)\vartheta.
 \tag{T-23801.8}
\]

Hence

\[
 \boxed{
 \vartheta\le\frac{2}{K\delta}.}
 \tag{T-23801.9}
\]

Because (T-23801.9) holds for arbitrarily large fixed `K`,

\[
 \boxed{\vartheta=0.}
 \tag{T-23801.10}
\]

Equivalently,

\[
 \boxed{
 \mathsf C_X
 \ge4\sqrt X-X^{o(1)}.}
 \tag{T-23801.11}
\]

## 5. Prime ramp and square screw

Equations (T-23801.2) and (T-23801.11) give

\[
 \sum_{q=p^k\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq
 \ge4\sqrt X-X^{o(1)}.
 \tag{T-23801.12}
\]

Insert this in the exact square-screw formula. At `X=N^2`,

\[
 (-\Psi(2\log N))_+=N^{o(1)}.
 \tag{T-23801.13}
\]

The exact rightmost-zero exponent theorem then gives

\[
 \Theta_\zeta
 =\limsup_{N\to\infty}
 \frac{
 \log(1+(-\Psi(2\log N))_+)
 }{2\log N}
 =0.
 \tag{T-23801.14}
\]

Functional-equation symmetry implies

\[
 \boxed{\mathrm{RH}.}
 \tag{T-23801.15}
\]

## 6. Independent entropy proof

A proof object need not optimize the exact values `G_n`. It is enough to
produce a feasible packing with

\[
 \sum n d(n)\ge8\sqrt X-X^{o(1)},
 \tag{T-23801.16}
\]

and

\[
 \sum d(n)(\log(n+1)+3)=X^{o(1)}.
 \tag{T-23801.17}
\]

Then `L-23801` gives (T-23801.12) directly. This provides a fail-closed
certificate interface independent of LP optimality.

## 7. Relationship to the repository's arithmetic core

The proposal does not deny the balanced Möbius firewall. It scalarizes it.

```text
balanced Heath--Brown/Möbius packet
        -> exact Möbius curvature of the carry profile
        -> finite convex obstacle
        -> reflected Hermitian energy
        -> two-contact lower-scale recurrence.
```

The first critical Farey/Mertens cell remains present as a fixed-ratio mutation
of the obstacle residual. The proposal succeeds only if that mutation receives
the same vanishing exponent.

This differs from generic `BTP(K)`: only one scalar functional needed for the
prime-ramp lower bound is controlled. It also differs from full Carry
Saturation: a nonnegative near-saturating minorant is sufficient.

## 8. Decisive review order

1. Verify `D-23801.13`--`D-23801.26` independently.
2. Verify the carry/Legendre identity and entropy consumer `L-23801`.
3. Verify the primal/dual and convex-obstacle formulation `L-23802`.
4. Reconstruct the exact packet-to-obstacle map in `L-23803`.
5. Enumerate same-scale terminal contact faces at `K=6`, `K=8`, and symbolic
   `K`.
6. Search for a face with three or more free contact coordinates.
7. Verify that no balanced class is removed by the withdrawn `L-23203`
   induction.
8. Verify the first-cell Mertens mutation.
9. Replay the scale-contraction and square-screw normalization.

A single valid three-contact same-scale face rejects the proposed `2/K` rate.
A complete two-contact dictionary verifies the only new closing theorem.

## 9. Exact status

```text
carry/Mobius curvature algebra             proposed exact
finite packing LP and entropy consumer     proposed exact
reflected Selberg Hermitian identity       imported proposed exact
high-order free-variable Euler closure     imported proposed complete
two-contact carry-obstacle theorem         new proposed hinge
scale contraction to RH                    complete conditional deduction
accepted proof of RH                       NO
```
