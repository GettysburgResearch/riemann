# L-28010 — Dyadic-lift source capacity and positive reserve factorization

Claim ID: `L-28010`  
Title: The two-contact generalized-prime reserve has an explicit parent-to-child capacity matching and a termwise positive balanced factorization  
Status: **PROPOSED COMPLETE SOURCE-BOUND FINITE THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28009`; PR #303 source-flow capacity distinction  
Scope: explicit source binding for the pole-canceling transverse carry sector; no boundary recurrence or RH claim

## 1. Why a source-capacity theorem is needed

PR #303 identifies the distinction between

```text
formal positive source mass
```

and

```text
an actual incoming edge/parent capacity which can pay that source.
```

The two-contact system of `L-28009` admits an exact capacity manifest.  No
Farkas existence theorem is needed on one carry row.

Fix

\[
 n=j+k,
 \qquad1\le j\le k,
\]

and use the dyadic lift

\[
 \tau_N(t)=2^{\lfloor\log_2(N/t)\rfloor}t.
\]

The top-half inverse coefficients satisfy

\[
 \sum_{N/2<m\le N}a_2(m)\Phi(m)
 =\sum_{t=1}^{N}\Phi(\tau_N(t))
\tag{L-28010.1}
\]

for every function `Phi`.

## 2. Explicit parent/child matching

Create `n` matched pairs:

\[
 (x_t,y_t)=(\tau_n(t),\tau_k(t))
 \qquad(1\le t\le k),
\tag{L-28010.2}
\]

and

\[
 (x_{k+r},y_{k+r})
 =(\tau_n(k+r),\tau_j(r))
 \qquad(1\le r\le j).
\tag{L-28010.3}
\]

Every `x_i` is an actual term in the parent top-half source and every `y_i` is
an actual term in one of the two child top-half sources.  Moreover

\[
 \boxed{x_i\ge y_i.}
\tag{L-28010.4}
\]

For the first family this follows from endpoint monotonicity of `tau`.  For the
second,

\[
 x_{k+r}>n/2\ge j\ge y_{k+r}.
\]

Thus the map is a literal no-double-spend capacity matching: every child term is
paired to one distinct parent term of at least the same size.

Put

\[
 d_i=\log(x_i/y_i)\ge0.
\tag{L-28010.5}
\]

Then the generalized-prime carry profile and its complete Selberg forcing are
exactly

\[
 \boxed{P_2(n,j)=\sum_i d_i,}
\tag{L-28010.6}
\]

\[
 \boxed{S_2(n,j)=\sum_i d_i\log(x_i y_i).}
\tag{L-28010.7}
\]

The first equation is the total logarithmic parent capacity left after every
child demand has been paid.  The second is the complete second-moment charge of
the same matched transport.

## 3. Exact reserve factorization

Let

\[
 R_2(n,j)=P_2(n,j)^2-S_2(n,j).
\]

Equations (L-28010.6)--(L-28010.7) give the identity

\[
 \boxed{
 R_2(n,j)
 =\sum_i d_i
   \left[P_2(n,j)-\log(x_i y_i)\right].
 }
\tag{L-28010.8}

This is an exact source-bound factorization; no row amplitude has been detached
from its source.

If

\[
 n\ge9,
 \qquad3\le j\le k,
\]

then

\[
 P_2(n,j)\ge\log\binom nj\ge2\log n
\]

and `x_i,y_i<=n`.  Hence every individual bracket in (L-28010.8) is
nonnegative:

\[
 \boxed{
 P_2(n,j)-\log(x_i y_i)\ge0.
 }
\tag{L-28010.9}

Therefore the complete balanced interior reserve has the literal square
realization

\[
 \boxed{
 R_2(n,j)
 =\sum_i
 \left[
  \sqrt{d_i}
  \sqrt{P_2(n,j)-\log(x_i y_i)}
 \right]^2.
 }
\tag{L-28010.10}

No abstract Schur complement, principal angle, compactness argument, or
unspecified source-flow completion is involved.

## 4. Quantitative moat

If

\[
 \eta n\le j\le(1-\eta)n,
\]

then

\[
 P_2(n,j)\ge\eta n\log2.
\]

Since `log(x_i y_i)<=2log n`, (L-28010.8) gives

\[
 \boxed{
 R_2(n,j)
 \ge
 \left(1-{2\log n\over\eta n\log2}\right)
 P_2(n,j)^2.
 }
\tag{L-28010.11}

Thus the actual source-bound reserve approaches the entire generalized-prime
square uniformly on every fixed balanced cone.

## 5. Endpoint and finite boundary

The rows outside Section 3 are not hidden in a generic positivity assertion.
`L-28009` gives their exact forms:

- `j=1`: `R_2=r(r+1)log^2(2)`;
- `j=2`: the explicit three-case formula `L-28009.23`;
- `(6,3),(7,3),(8,3),(8,4)`: the four explicit positive logarithmic forms
  `L-28009.24`.

These rows form a finite source-bound boundary table.  Equality occurs only at
trivial splits and at `j=1,n-1` for odd `n`.

## 6. Relationship to the physical RH-bearing boundary

The matching above closes the **pole-canceling transverse carry sector** of the
two-contact system: the complete first and second logarithmic moments have an
actual parent-capacity assignment and an explicit positive reserve.

It does not delete the unweighted `m=1` source.  That coordinate is absent from
both logarithmic moments and is precisely the two-contact / bottom-charge
boundary retained in `L-28007` and PR #269 `L-26904`.

A valid full proof must therefore combine:

```text
transverse logarithmic sector
    -> closed here by explicit capacity and reserve;

unweighted two-contact boundary
    -> retained in the physical independent-frequency block
    -> routed by a strict lower-scale recurrence.
```

The theorem prevents a reviewer or future proposal from treating the
transverse source capacity as an unproved exercise.  The only surviving source
capacity is the explicitly isolated unweighted boundary coordinate.

## 7. Proof boundary

Closed exactly:

- a bijective no-double-spend parent/child source matching;
- the complete first- and second-moment ledgers on that matching;
- an exact reserve decomposition;
- a termwise square factorization on the complete balanced interior;
- a quantitative reserve tending to one;
- the finite endpoint table interface.

Open:

- localization of the unweighted two-contact boundary in the physical block;
- a strict lower-scale boundary recurrence;
- a subpower bottom-charge estimate;
- RH.
