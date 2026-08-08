# M-26202 — Affine–continuum frontier for the carry proof

Claim ID: `M-26202`  
Title: After exact Green equality and zero-charge continuum transport, the remaining theorem is a finite arithmetic deformation with one subpower boundary charge  
Status: **FULL PROPOSAL / ONE SOURCE-SPECIFIC FINITE THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-26201`--`L-26205`; PR #271 `L-26701/L-26702`; PR #265 `L-26202`; PR #269 `L-26201/L-26205`; PRs #229/#234 fixed-ratio shell firewall  
Scope: corrected review packet; RH is not claimed proved

## 1. Exact state after the latest cross-branch work

The carry route now has three exact layers.

### 1.1 Signed equality

The endpoint-projected Green solve emits a unique source-bound state

\[
V_Xb_X^G=w_X
\]

on every prime-power row. Its complete all-integer correction is supplied by
the Möbius–Poisson factorization of `L-26201`.

### 1.2 Physical positivity

There are two exact ways to impose physical nonnegativity after the signed solve:

1. Green–Skorokhod clipping and contact ledgers (`L-26202/L-26203`);
2. one affine block ending at a prime in `(X,2X)` (`L-26204`, importing PR
   #271).

The affine block is the sharper proof consumer. If

\[
C_X^G=\max_m(b_X^{(0)}(m)-b_X^G(m))_+,
\]

then it gives directly

\[
P_X\ge J_X(b_X^{(0)})-C_X^G\log X.
\]

It also dominates the prefix-Skorokhod debt up to the explicit factor two in
`L-26204.20`.

### 1.3 Continuum transport

The exact parabolic continuum defect has zero mass and is tail-majorized by its
negative slack. `L-26205` therefore constructs a positive ordered
 defect-to-slack coupling which cancels the complete continuum residual with
nonnegative objective gain.

Hence the continuum least affine charge is exactly zero.

The obstruction is not a continuum sign or mass imbalance. It is the finite
integer/divisor realization of this ordered coupling.

## 2. Minimal load-bearing theorem

The remaining theorem is the following **Finite Arithmetic Green Deformation**
statement, abbreviated `FAGD`.

For every `epsilon>0` and every sufficiently large integer `X`, construct an
explicit potential `H_X` and put

\[
b_X^H(m)=b_X^G(m)+H_X(m-1)-H_X(m).
\tag{M-26202.1}
\]

The certificate must verify

\[
\boxed{
V_Xb_X^H\le w_X
}
\tag{M-26202.2}
\]

and

\[
\boxed{
C_X(H):=\max_{2\le m\le X}
       (b_X^{(0)}(m)-b_X^H(m))_+
\le C_\epsilon X^\epsilon.
}
\tag{M-26202.3}
\]

No sign condition on `b_X^H` is required. The affine prime-boundary lift of
`L-26204` turns it into a nonnegative finite carry certificate and pays only
`C_X(H) log X=X^o(1)`.

Thus

\[
\boxed{
\mathrm{FAGD}
\Longrightarrow
P_X\ge4\sqrt X-X^{o(1)}
\Longrightarrow
\mathrm{RH}.
}
\tag{M-26202.4}

The implication is complete. `FAGD` is not proved.

## 3. Required source grammar

A production deformation may combine the Green, dipole, quotient-cell, and
dyadic coordinates, but it must remain source bound.

It must export:

```text
complete prime-power manifest;
complete all-integer Green extension h_X(q);
Möbius charge gamma_X(m);
quotient-cell partition with shared boundaries;
every adjacent-flow or interval-block endpoint;
all divisor incidences of every endpoint;
final signed residual in every prime-power row;
maximum downward displacement C_X(H);
one oversupport prime and its boundary charge;
formal objective replay;
fixed-ratio and dyadic mutations.
```

Equal arithmetic destinations and neighboring quotient-cell boundaries must be
recombined before any positive part or maximum is taken.

## 4. Candidate construction

The proposed construction has four stages.

### 4.1 Green orthogonal purge

Apply PR #240 `L-23820` to remove the complete Green-orthogonal residual at
exactly zero objective cost. Arbitrary source rank, including the same-sign
Möbius cube, is permitted.

### 4.2 Cellwise signed balayage

Apply PR #240 `L-23821` inside complete quotient cells. Cell-interior source
rank is replaced by its total and logarithmic moments at zero objective cost.
Common endpoints of neighboring cells cancel before estimates.

### 4.3 Ordered finite transport

Use the continuum quantile coupling of `L-26205` as the transport order. Lift
its pairs to exact integer incidence dipoles through the Möbius–Poisson charge
ledger. Jointly solve the bounded consecutive-prime-power clusters; every
remaining positive child lies at scale at most `(X+1)/2`.

The proof-facing recurrence is

\[
 C_X(H)
 \le C\log^A(2X)
    +\sum_\beta\omega_\beta C_{Y_\beta},
\qquad
Y_\beta\le{X+1\over2},
\qquad
\sum_\beta\omega_\beta\le1.
\tag{M-26202.5}
\]

This recurrence implies `C_X(H)=O(log^(A+1) X)` by dyadic scale induction.

Equation (M-26202.5) is a proposed construction target, not an established
identity.

### 4.4 Affine finish

Apply `L-26204` once. The oversupport prime absorbs every remaining physical
negative coordinate without changing an old constraint.

## 5. Mandatory arithmetic mutations

A claimed proof must survive all of the following.

### 5.1 Logarithmic dual ray

PR #271 shows that

\[
y_q=\Lambda(q)/\log X
\]

is a feasible dual witness. It may not be removed, damped, or declared
Green-orthogonal. Its contraction is the normalized prime-ramp discrepancy.

### 5.2 Fixed-ratio Mertens shell

The exact `2/3` shell of PRs #229/#234 must appear in the scalar ledger or be
transported through an explicit all-ratio causal filter. An unsigned bound is
invalid.

### 5.3 Dyadic two-contact source

PR #269 proves the exact identity

\[
\sum_q
 [\mu(q)-\mathbf1_{2\mid q}\mu(q/2)]\chi_{n,q}(j)
 =-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
\]

The same branch gives an exact half-scale isometry on the even columns. A finite
transport proof must export the corresponding two-contact/bottom-charge scalar
and must account for the remaining odd-column leakage.

### 5.4 Same-sign high-rank cubes

No source-rank, face-count, or endpoint-count bound is permitted. The Green
orthogonal purge and two-moment balayage act on the complete signed aggregate.

## 6. Automatic rejection conditions

Reject a proposed `FAGD` certificate if it:

```text
sets undeclared non-prime-power Green coordinates to zero;
takes positive parts before complete quotient-cell recombination;
uses a live-variable Euler or cell-selection rule;
omits an interval endpoint or one of its prime-power divisors;
uses a composite oversupport endpoint in place of the prime lift;
claims that continuum tail order alone proves the finite divisor transport;
drops the logarithmic dual ray;
loses the fixed-ratio Mertens shell;
ignores the dyadic odd-column leakage;
pays a factor X^c with fixed c>0;
promotes a finite numerical ladder to the cofinal theorem.
```

## 7. Exact status

```text
Green equality and all-integer decoder        PROPOSED EXACT
Green-Skorokhod finite ledgers                 PROPOSED EXACT
prime oversupport affine completion            PROPOSED EXACT
comparison of affine and Skorokhod debts       PROPOSED EXACT
continuum ordered zero-charge transport        PROPOSED EXACT
finite FAGD / recurrence (M-26202.5)           OPEN / RH-BEARING
FAGD -> prime ramp -> RH                       COMPLETE CONDITIONAL CHAIN
Riemann Hypothesis                             NOT PROVED
```

The present branch is therefore not an unconditional proof packet. It is a
hardened proposal whose remaining statement is one explicit finite arithmetic
transport, rather than an arbitrary sandwich, generic Green norm, or bounded
source-rank assertion.
