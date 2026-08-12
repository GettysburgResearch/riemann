# T-91520 — Logarithmic one-node annular exhaustion would prove RH

Claim ID: `T-91520`  
Status: **FULL CONDITIONAL RH PROPOSAL / SOURCE-ORDERED LOG IDENTIFICATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91520/L-91521`, `R-91520`; `T-91404`  
RH status: **unproved**

## 1. Fixed node and dyadic annuli

Fix

\[
 \eta=1,
 \qquad
 a_j=2^{-j-1}.
\]

Let

\[
 \Lambda_j^{\rm hyp}
 =\Lambda_{a_j,a_{j-1}}^{\rm ann}(1)
\]

be the additive crossed-zero Green mass of the `j`-th horizontal annulus.
Then

\[
 \Lambda_j^{\rm hyp}\ge0,
\]

and it vanishes exactly when that annulus contains no crossed zero.

## 2. Arithmetic multiplicative innovation

Let

\[
 \mathfrak S_j^{\rm arith}
\]

be the explicit coefficient-one multiplicative source innovation assembled
from:

```text
the one-Green completed Xi quotient at the fixed node;
the dyadic Jordan prime innovation;
the gamma/pole factor;
the eta/dyadic pole bridge when the hard endpoint is used;
the deterministic stable channel.
```

Every scalar input is a safe real-axis Xi, zeta, eta, gamma, or Laplace value.
Let

\[
 \mathscr L_j^{\rm arith}
\]

be its source-ordered log determinant. It must be defined before the model
factorization; defining it from the desired target output is circular.

## 3. Logarithmic One-Node Annular Exhaustion (`LONAIE_j`)

Construct a canonical one-node factorization of the arithmetic innovation into

\[
 \mathfrak S_j^{\rm arith}
 \longrightarrow
 \mathfrak S_j^{\rm crit}
 \odot
 \mathfrak S_j^{\rm st}
 \odot
 \mathfrak S_j^{\rm hyp}
 \odot
 \mathfrak E_j,
\]

where `odot` denotes coefficient-one multiplicative composition, such that

\[
\boxed{
 \mathscr L_j^{\rm arith}
 =\mathscr L_j^{\rm crit}
  +\mathscr L_j^{\rm st}
  +\Lambda_j^{\rm hyp}
  +\mathscr L_j^{\rm aux}.
}
\tag{T-91520.1}

\]

Prove the exhaustion identity

\[
\boxed{
 \mathscr L_j^{\rm arith}
 =\mathscr L_j^{\rm crit}
  +\mathscr L_j^{\rm st}.
}
\tag{T-91520.2}

\]

with

\[
 \mathscr L_j^{\rm aux}\ge0.
\]

Then

\[
 \Lambda_j^{\rm hyp}=0,
 \qquad
 \mathscr L_j^{\rm aux}=0.
\]

This is `LONAIE_j`.

## 4. Completion to RH

If `LONAIE_j` holds for every `j`, then every term in

\[
 \Lambda_{a_J}(1)
 =\sum_{j=1}^J\Lambda_j^{\rm hyp}
\]

vanishes. Hence there are no zeros with

\[
 \Re s>\frac12+a_J
\]

for any `J`, and RH follows as `J` tends to infinity.

## 5. Relation to the norm-exhaustion route

The parent `ONAIE_j` asks for an isometric source-to-model map and exact norm
exhaustion. `LONAIE_j` asks only for the determinant/Green potential at one
node. It retains less output geometry:

```text
no all-carrier Gram;
no delay packet;
no independent orientation matrix;
no inherited Blaschke weight;
one additive scalar per annulus.
```

A proof still requires a canonical source factorization. `R-91520` shows that
one safe scalar value or source positivity alone is insufficient.

## 6. Quantitative hostile test

By `L-91521`, any nonzero annular output obeys

\[
 \Lambda_j^{\rm hyp}
 \ge
 \sum_{\zeta\in Z_j}
 m_\zeta
 \frac{4\Re\zeta}
      {|1+\overline\zeta|^2}.
\]

Thus an approximate source exhaustion with an error smaller than this moat
would already exclude a prescribed finite annular zero packet. The exact
all-annulus theorem requires zero error.

## 7. Exact boundary

```text
additive hyperbolic log telescope                   EXACT
zero-by-zero Green mass                            EXACT
one-node log determinant target                    EXPLICIT
scalar source positivity alone                     INSUFFICIENT
LONAIE source-ordered log exhaustion               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
