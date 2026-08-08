# L-28004 — The central-split eta source collapses to a sparse Mersenne boundary

Claim ID: `L-28004`  
Title: Pairing the reciprocal-eta source with one central carry row gives `+1` at every parent except the dyadic Mersenne endpoints  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-28002`  
Scope: exact source/carry pairing and cascade telescope; no asymptotic bound

## 1. Central source response

Let `b` be the coefficient sequence of `1/eta(s)` and let

\[
 Y_n(j)=\sum_{q=2}^{n}b(q)\chi_{n,q}(j)
 =D(n)-D(j)-D(n-j)
\]

be the exact carry image from `L-28002`, where

\[
 D(x)=2^{\lfloor\log_2x\rfloor+1}-1
 \qquad(x\ge1),
 \qquad D(0)=0.
\]

Put

\[
 j_n=\left\lfloor{n\over2}\right\rfloor
\]

and define the central response

\[
 y_n=Y_n(j_n).
\tag{L-28004.1}

Then

\[
 \boxed{
 y_n=
 \begin{cases}
 1,&n\ne2^r-1\quad(r\ge2),\\[1mm]
 1-2^{r-1},&n=2^r-1\quad(r\ge2).
 \end{cases}}
\tag{L-28004.2}

### Proof

If `n=2m` is even, the top dyadic scale of `n` is twice the top dyadic scale
of `m`.  Therefore

\[
 D(2m)-2D(m)=1.
\]

If `n=2m+1` is odd and `m+1` stays in the same dyadic block as `m`, then

\[
 D(2m+1)-D(m)-D(m+1)=1.
\]

The only exception is

\[
 m=2^{r-1}-1,
 \qquad n=2^r-1,
\]

when `m+1` enters the next dyadic block.  Direct substitution gives

\[
 D(2^r-1)-D(2^{r-1}-1)-D(2^{r-1})
 =1-2^{r-1}.
\]

This proves (L-28004.2).

## 2. Sparse pairing formula

Let `c_n` be any finitely supported real central-split coefficient sequence.
Its carry load is

\[
 v(q)=\sum_{n\ge q}c_n\chi_{n,j_n}(q).
\]

Pairing with the complete reciprocal-eta source gives

\[
 \begin{aligned}
 \sum_{q\ge2}b(q)v(q)
 &=\sum_{n\ge2}c_n y_n\\
 &=\sum_{n\ge2}c_n
   -\sum_{r\ge2}2^{r-1}c_{2^r-1}.
 \end{aligned}
\]

Hence

\[
 \boxed{
 \sum_{q\ge2}b(q)v(q)
 =\sum_{n\ge2}c_n
  -\sum_{P\in\{2,4,8,\ldots\}}P\,c_{2P-1}.
 }
\tag{L-28004.3}

The complete Möbius/eta source therefore sees only:

1. the total central coefficient mass;
2. one explicit charge at each Mersenne parent `2P-1`.

No other row survives.

## 3. Exact central-cascade telescope

Let a finite central cascade begin from a target sequence `r_0` and put

\[
 c_j(n)=r_j(n)-r_j(n+1),
 \qquad
 r_{j+1}=r_j-Bc_j,
\]

where `B` is the central carry matrix.  Suppose the cascade terminates with
`r_J=0`.  Pairing each residual identity with `b` and summing in `j` gives

\[
 \boxed{
 \sum_{q\ge2}b(q)r_0(q)
 =\sum_{j=0}^{J-1}
 \left[
  \sum_{n\ge2}c_j(n)
  -\sum_{P}P\,c_j(2P-1)
 \right].
 }
\tag{L-28004.4}

Since each first-difference sum telescopes,

\[
 \sum_{n\ge2}c_j(n)=r_j(2),
\]

and therefore

\[
 \boxed{
 \sum_{q\ge2}b(q)r_0(q)
 =\sum_{j=0}^{J-1}r_j(2)
  -\sum_{j=0}^{J-1}\sum_P
   P\,[r_j(2P-1)-r_j(2P)].
 }
\tag{L-28004.5}

This is an exact sparse boundary representation of the full reciprocal-eta
Riesz coordinate.

## 4. Why this is a global reduction

The left side of (L-28004.5), for the critical logarithmic target, has Mellin
transform containing

\[
 {1\over\eta(s)}
 ={1\over(1-2^{1-s})\zeta(s)}.
\]

A subpower bound for it excludes every off-line zeta pole.  Equation
(L-28004.5) shows that the complete source can be attacked without a dense
Möbius packet:

```text
all central rows
 -> total mass
    plus
    O(log X) Mersenne boundary charges per stage.
```

The difficult arithmetic has been compressed into the interaction of these
sparse dyadic charges across the support-halving cascade.  This is a materially
smaller object than generic BTP, WSTS, or a complete balanced Gram.

The identity does not by itself bound the charges.  In particular, taking
absolute values in the double sum would lose the coherent eta signs.

## 5. Review mutations

A valid continuation must retain:

- the exceptional rows `3,7,15,31,...`;
- the exact charge `P` at row `2P-1`;
- every cascade stage until support exhaustion;
- the product-six mutation from `R-28001`;
- the finite Euler factor `1-2^(1-s)` in the Mellin consumer.

Deleting the Mersenne boundary turns the RH-bearing source into the false
constant row `y_n=1`.

## 6. Proof boundary

Closed exactly:

- the central response formula;
- the sparse source pairing;
- the all-stage Mersenne boundary telescope;
- the reciprocal-eta interpretation.

Open:

- a subpower estimate for the complete signed Mersenne ledger;
- a reflected or Pascal-cycle boundary recurrence;
- RH.
