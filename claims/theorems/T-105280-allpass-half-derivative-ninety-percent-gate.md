# T-105280 — Adjacent all-pass half-derivative gate for ninety percent

Claim ID: `T-105280`  
Status: **PROVED EXACT IMPLICATION; AHXFER105280 OPEN**  
Created: 2026-08-24  
Depends on: L-105280--L-105282; T-105220; R-105280  
RH status: unproved

Let \(F_k=\Xi^{(k)}\) and let \(R_k(T)\) be the real-zero count in compatible
regular windows.  For each adjacent pair, form the companion all-pass quotient
\(U_{k,T}\) of L-105281, including the one-unit Rolle carrier and the exact
endpoint ledger.  Put

\[
\mathfrak H_K(T)
=
\sum_{k=1}^K
\|U_{k,T}\|_{\dot H^{1/2}}^2.
\tag{1}
\]

L-105281 and the finite-window endpoint accounting give

\[
\boxed{
R_0(T)
\ge
R_K(T)-\mathfrak H_K(T)-O(K)-o(N(T)).
}
\tag{2}
\]

The `O(K)` term contains the two horizontal endpoint phases and confluent
regularization; it is negligible for fixed \(K\), and for growing \(K(T)\)
whenever \(K=o(N)\).

## Ninety-percent gate

Suppose

\[
\frac{R_K(T)}{N(T)}\ge p_K-o(1)
\]

and

\[
\boxed{
\limsup_{T\to\infty}
\frac{\mathfrak H_K(T)}{N(T)}
<p_K-0.9.
}
\tag{3}
\]

Then

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}>0.9.
}
\tag{4}
\]

## Density-one gate

If \(K=K(T)\) satisfies

\[
p_{K(T)}\to1,
\qquad
K(T)=o(N(T)),
\qquad
\mathfrak H_{K(T)}(T)=o(N(T)),
\]

then

\[
\boxed{
\frac{N_0(T,2T)}{N(T,2T)}\to1.
}
\tag{5}
\]

This remains weaker than RH.

## Source budget and exact open interface

L-105282 proves that the carrier-free polynomial Wick model has normalized
half-derivative energy tending to zero superfactorially; already at degree
four the conservative two-orientation source budget is below \(1/1700\).

The single conclusion-facing interface is

```text
AHXFER105280:
  transfer the frozen Dirichlet half-derivative energy to the adjacent
  companion all-pass boundary quotient U_(k,T), including the physical
  half-order normalization, horizontal/vertical contour transport,
  endpoint phases, and all near-real Blaschke factors, with total loss
  below p_K-0.9 (or o(1) for density one).
```

R-105280 proves that an ordinary trace/HS or L2 transfer cannot establish this
interface: a near-line phase slip has arbitrarily small L2 mass but one unit of
winding.  A successful proof must preserve the half derivative, or replace it
by an equivalent Carleson/Dirichlet-energy or zero-repulsion theorem.

```text
companion winding identity                 PROVED EXACT
wrong extrema = negative adjacent winding  PROVED EXACT
H^(1/2) winding payment                    PROVED EXACT
frozen Wick H^(1/2) budget                 PROVED
ordinary L2 shortcut                       REFUTED
AHXFER105280                                OPEN / RECORD-BEARING
ninety percent / density one / RH          UNPROVED
```
