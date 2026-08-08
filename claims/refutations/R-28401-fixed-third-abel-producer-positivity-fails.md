# R-28401 — Fixed third-Abel producer positivity fails

Claim ID: `R-28401`  
Title: The binary–ternary producer has an exact negative third cumulative kernel at endpoint 520  
Status: **EXACT REFUTATION OF A STRONGER SURROGATE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #284  
Frozen target: PR #279 `L-27801`  
Scope: the claimed all-endpoint nonnegativity of the third cumulative producer kernel; no verdict on the source-specific critical producer

## 1. Frozen producer

For endpoint `X`, target `w`, and the Möbius function `mu`, put

\[
U(m)=\sum_{k\le X/m}\mu(k)w(mk),
\qquad
r(m)=U(m)-U(m+1).
\]

The frozen binary–ternary descending producer uses

\[
a_3(m)=\lceil m/3\rceil,
\quad b_3(m)=m-a_3(m),
\quad a_2(m)=\lfloor m/2\rfloor,
\quad b_2(m)=m-a_2(m),
\]

and recursively

\[
A(m)=r(m)+I(m),
\]

where each processed parent sends `A(m)/2` to each child of both displayed splits.

For a third Abel prefix, take

\[
 w_Q(q)=\binom{Q-q+2}{2}\mathbf 1_{2\le q\le Q}.
\]

The quantity called `S_X(n,Q)` in `L-27801` is exactly the resulting coefficient `A(n)`.

## 2. Exact counterexample

At

\[
\boxed{X=Q=520,\qquad n=15,}
\]

the exact rational recurrence gives

\[
\boxed{A(15)=-\frac{91}{256}<0.}
\]

Moreover this is the least coefficient at that endpoint.

The computation uses only:

```text
integer Möbius values through 520;
integer binomial coefficients;
fractions with power-of-two denominators;
the frozen four-child descending recurrence.
```

`X-28401` reconstructs the value from scratch with Python's standard library and `fractions.Fraction`.

## 3. Scope of the refutation

The exact statement

\[
S_X(n,Q)\ge0
\quad\text{for all finite }X,Q,n
\]

is false. Consequently a proof of producer positivity cannot proceed by combining:

```text
fixed third-prefix kernel positivity
+
nonnegative third differences of the critical source
```

at all endpoints.

This does **not** refute:

- positivity of the actual critical producer;
- an Abel order increasing with the endpoint;
- a source-bound collar theorem with compensating signed boundary channels;
- the central-cascade route of PR #280;
- a higher-order or renormalized boundary-jet contraction.

## 4. Structural lesson

The first negative third-prefix value occurs far beyond the finite scan through 80. Higher fixed Abel orders postpone the first observed negative endpoint but do not remove the reciprocal-zeta mechanism. Thus finite-order smoothing is not by itself a cofinal proof method.

The replacement attack on this branch separates:

```text
strictly contracting analytic shifted-lattice bulk
from
finite cutoff boundary jets carrying the arithmetic obstruction.
```

No fixed cumulative-order sign is assumed in that attack.

## 5. Proof boundary

Exact here:

- the source and producer match the frozen definitions;
- `A(15)=-91/256` at `Q=520`;
- the universal third-prefix positivity assertion is false.

Open:

- the source-specific boundary-jet recurrence;
- DCCS;
- RH.
