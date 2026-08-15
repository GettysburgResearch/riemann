# L-93782 — Row 66 is the unique extremal certificate row, and the compact/tail join is exact

Claim ID: `L-93782`  
Status: **PROVED DIRECTED EXTREMALITY AND EXACT DOMAIN PARTITION**  
Created: 2026-08-15  
Depends on: `L-91781`, `L-93781`  
Replay: `X-93780-target-lorenz-directed-tail`  
RH status: **unproved**

## 1. Directed row-66 extremality

For each row `j`, let `m_j` be the global lower endpoint returned by the
published analytic lower-envelope certificate on `x>=166000`. A directed
upper enclosure of the row-66 envelope at `x=166000` is

\[
M_{66}^{up}<26.786653212345144.
\]

The nearest competing row is row 65, whose complete directed lower bound is

\[
m_{65}>28.241619047675702.
\]

Therefore

\[
\boxed{
\min_{2\le j\le65}m_j-M_{66}^{up}
>1.454965835330558>1.45.
}
\tag{L-93782.1}
\]

Thus row 66 is the unique global extremal **certificate row**, and its minimum
is owned by the tail boundary `x=166000`.

This is intentionally not stated as the stronger pointwise ordering
`Theta_j(x)>=Theta_66(x)` for every common `x`. The finite all-row directed
certificate is the theorem actually proved.

## 2. Exact half-open join

The frozen compact theorem `L-91781` has the literal real domain

\[
67\le x=py<166000.
\]

`L-93781` has the literal real domain

\[
x=py\ge166000.
\]

These sets are disjoint, their union is every admissible `x>=67`, and the
boundary belongs exactly once, to the directed tail theorem. At that boundary
the determinant lower endpoint is the positive number in `L-93781.1`.
Hence there is neither an omitted real cell nor a duplicated boundary
assumption.

The compact claim and retained result are frozen by Git blobs

```text
L-91781: 2c16327c6653009667fa06ddbb24628ff583c0fe
result:   2fda156232fc9d4e9ae36066870b613270161166
```

and the tail starts exactly at the compact exclusive endpoint `166000`.
