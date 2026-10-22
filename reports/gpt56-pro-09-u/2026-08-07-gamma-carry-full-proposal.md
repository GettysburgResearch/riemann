# Full proposal: finite Gamma–carry packing for RH

Agent: `gpt56-pro-09-u`  
Date: 2026-08-07  
Issue: #238  
Parent branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: **FULL PROPOSED PROOF WITH ONE FINITE POSITIVE-MINORANT THEOREM; RH NOT CLAIMED**

## 1. Step back

The repository's live arithmetic routes now agree on one point: after Type-I and
endpoint terms are removed, the remaining obstruction is a signed reciprocal-
zeta/Möbius correlation. The reflected Selberg, BTP, fixed-ratio Mertens,
analytic-totient, prime-energy, and square-screw formulations all retain that
same core.

The carry programme offers a potentially shorter coordinate system. Its exact
finite identity converts every prime-power weight into nonnegative average carry
counts and binomial entropies. The parent branch correctly weakened pointwise
triangular-inverse positivity to a nonnegative packing problem, but it did not
identify the sharp packing geometry.

This pass identifies both:

1. a canonical global Gamma/carry convolution factor;
2. a weaker finite-horizon positive-minorant theorem that is all the RH proof
   actually needs.

## 2. Exact continuum object

The continuum carry kernel is

\[
K(x)={\lfloor x\rfloor(\lfloor x\rfloor+1-x)\over x}.
\]

It has exact Mellin transform

\[
\int_1^\infty K(x)x^{-s-2}dx
={s\zeta(s+1)\over(s+1)(s+2)}
\]

and exact mass `1/2` at `s=0`.

The normalized logarithmic density

\[
p(t)=2e^{-t}K(e^t)
\]

is an explicit probability law. One realization is

```text
P(M=m)=1/[m(m+1)],
V~Beta(2,1),
X=M(M+1)/(M+V),
T=log X.
```

The sharp logarithmic target is the `Gamma(2,1/2)` law. Dividing its transform
by the carry transform produces

\[
A(s)={(s+1)(s+2)
\over8s(s+1/2)^2\zeta(s+1)}.
\]

Its exact physical inverse is the Möbius–Riesz density

\[
\begin{aligned}
a(t)=\sum_{n\le e^t}{\mu(n)\over n}
\bigg[&1-{7\over8}e^{-(t-\log n)/2}\\
&-{3\over16}(t-\log n)e^{-(t-\log n)/2}\bigg].
\end{aligned}
\]

Global positivity of this density is the cleanest possible certificate: it says
that the carry variable is an additive convolution factor of an independent
`Gamma(2,1/2)` variable.

## 3. The weaker finite theorem

Global factorization is stronger than necessary. At level `X`, put

\[
T_X=\log(X/2),
\qquad
\kappa(t)=e^{-t/2}K(e^t).
\]

The finite Gamma–carry minorant theorem `FGCM` asks only for a nonnegative
profile `b_X` on `[0,T_X]` such that

\[
(8e^{\cdot/2}b_X)*\kappa(t)\le t
\qquad(0\le t\le T_X),
\]

and

\[
1-\int b_X\le X^{-1/2+o(1)},
\qquad
X^{-1}\int e^tb_X(t)dt\le X^{-1/2+o(1)}.
\]

The profile may depend on `X`, retain slack, and recombine complete quotient
layers. It need not be the truncation of one globally positive Möbius inverse.
This is the exact positive-LP-minorant weakening requested by the repository
review.

## 4. Exact finite packing

Given `b_X`, define

\[
d_X(n)=8\sqrt X\int_n^{n+1}
y^{-2}b_X(\log(X/y))dy.
\]

The finite carry coefficient satisfies exactly

\[
\beta_{nq}=K_-((n+1)/q),
\]

and this endpoint sample is the minimum of `K(y/q)` over `[n,n+1]`. Therefore

\[
\sum_{n=q}^Xd_X(n)\beta_{nq}
\le q^{-1/2}\log(X/q)
\]

with no discretization remainder.

The two `FGCM` mass budgets and the entropy lower bound give

\[
\sum_n d_X(n)G_n
\ge4\sqrt X-X^{o(1)}.
\]

Hence the complete prime-power ramp satisfies the same lower bound.

## 5. RH deduction

At `X=N^2`, the exact square-screw formula is

\[
\Psi(2\log N)
=4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N).
\]

The carry packing gives

\[
\Psi(2\log N)\le N^{o(1)}.
\]

The unconditional derivative bound propagates this upper envelope between
adjacent square samples. The upper-envelope form of Landau's one-sign theorem
then excludes every pole of `xi'/xi` to the right of the critical line.
Functional-equation symmetry gives RH.

## 6. Why this proposal is genuinely new

The proposal does not:

- assert the exact triangular carry inverse is pointwise positive;
- require a full Heath--Brown packet dictionary;
- use a generic Farey-spacing estimate;
- assume a positive-Hankel stop-loss adjoint;
- import the affine central-block gate;
- smooth away fixed off-line modes.

It asks for one finite, nonnegative scalar convolution packing with an explicit
sharp mass budget. All consequences after that certificate are exact.

## 7. Falsifiability and production

A global GCF proof can be rejected by one exact negative density value. On each
quotient interval the density has at most one interior critical point.

A finite `FGCM` producer must emit:

```text
nonnegative rational cell masses
complete carry-reset manifest
outward convolution inequalities
mass deficit
exponential first moment
cofinal X^o(1) rate.
```

Finite successful levels are evidence only. A proof needs a symbolic recurrence,
reflected square, quotient-layer invariant, or another cofinal construction.

## 8. Connection to BTP and reflected Selberg

The canonical quotient retains `1/zeta(s+1)`, so the balanced Möbius core has not
vanished. `FGCM` is a scalar positive-minorant projection of that core.

A proof may specialize reflected Selberg or BTP to this shape-two carry profile,
but it need not control every packet coordinate. This is the potential gain:
all Type-I and endpoint bookkeeping has already collapsed into one finite
convolution budget.

## 9. Exact status

```text
L-23804 carry Mellin/probability law      PROPOSED COMPLETE
L-23805 quotient/density identities       PROPOSED COMPLETE
L-23807 finite minorant implication        PROPOSED COMPLETE
FGCM cofinal positive minorants            OPEN / RH-BEARING
L-23806 global-factor special case         PROPOSED COMPLETE
T-23801 full deduction to RH               PROPOSED COMPLETE
X-23801 exact normalization replay         PASS
Riemann Hypothesis                         NOT PROVED
```

This is the final review package: a full proof architecture with one explicit,
falsifiable finite arithmetic theorem and no hidden residual estimate.
