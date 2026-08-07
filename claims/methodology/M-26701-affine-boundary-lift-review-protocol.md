# M-26701 — Review protocol for the affine Green boundary lift

Claim ID: `M-26701`  
Title: Fail-closed production and review protocol for ABLC  
Status: **PROPOSED METHODOLOGY**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: `L-26701`, `L-26702`, `T-26701`

## Objective

Produce a proof-grade cofinal family satisfying
\[
\mathcal C_X=X^{o(1)}
\]
and consume it through the explicit affine oversupport construction.

## Required finite ledger at each endpoint

```text
endpoint X and one certified prime Y in (X,2X)
complete duplicate-free prime-power list Q_X
parabolic benchmark b_X^(0)
all carry responses v_q(b_X^(0))
target w_X(q)
one signed feasible vector b_X
least-charge or certified upper charge C_X
pointwise inequalities b_X >= b_X^(0)-C_X
all old response inequalities
constant oversupport block
proof that no q<=X divides Y
new boundary response at Y
formal/interval objective identity
prime-ramp equivalence digest
```

## Three licensed construction paths

### A. Canonical Green

Emit
\[
G_X,\quad r_X,\quad T_X=G_X^{-1}r_X,\quad F_X,\quad b_X^G,
\]
and certify
\[
C_X^G
=
\max_m(F_X(m)-F_X(m-1))_+.
\]

A symbolic theorem may estimate the maximum edge directly. It need not estimate
the full Green energy.

### B. Constraint-dipole assisted

Emit an exact adjacent flow \(H\) with
\[
V_Xb_X^H\le w_X.
\]
The flow may remain signed and may have a large separate objective ledger.
Acceptance requires only
\[
\max_m(b_X^{(0)}(m)-b_X^H(m))_+=X^{o(1)}.
\]

Every same-scale prime-power cluster and every child constraint must be included.
A one-row or ordinary-prime-only flow is rejected.

### C. Direct minimax/dual

Produce primal and dual interval certificates for the LP in `L-26702`.
The dual must use the exact monotone-additive divisor potential
\[
Y_y(n)=\sum_{q\mid n}y_q
\]
and must include the logarithmic ray.

## Automatic rejection

Reject a packet that:

1. uses a composite oversupport boundary without accounting for old divisors;
2. clips negative coordinates independently;
3. omits proper prime powers;
4. changes the sign of the Green slope;
5. proves only a finite floating ladder;
6. replaces maximum edge control by aggregate slack without a theorem;
7. deletes the von-Mangoldt dual ray;
8. loses the \(2/3\) Möbius-shell mutation;
9. uses a boundary charge larger than a fixed power while claiming ABLC;
10. changes the inherited prime-ramp normalization.

## Preferred fresh proof attack

The most promising composition is:

```text
canonical Green solution
-> exact constraint-dipole cluster solve
-> use continuum tail-majorization to orient the remaining flow
-> certify only the maximum downward displacement
-> absorb it by the affine prime-boundary lift.
```

This is weaker than completing the full signed transport and weaker than
bounding the complete Green energy.
