# L-102882 — The stopped Vaughan source has one closed Type-I sign and two coherent owner packets

Claim ID: `L-102882`  
Status: **PROVED EXACT SOURCE DECOMPOSITION; COHERENT SUM OPEN**  
Created: 2026-08-24  
Corrected: 2026-08-24  
Depends on: `L-102868--L-102881`  
RH status: **unproved**

For each second owner prime `q`, the literal stopped square-core source has the
coefficient-exact decomposition

\[
\boxed{
\mathcal C_{p,q}
=\mathcal T_{p,q}^{\rm full}
+\mathcal T_{p,q}^{\rm bdry}
+\mathcal B_{p,q}.
}
\tag{L-102882.1}

The three terms have the following exact status.

## 1. Unrestricted Type-I part

`L-102880` proves

\[
\mathcal T_{p,q}^{\rm full}(Y)
=c_+M_{U,q}^2+O_R(Y^{-1/6}),
\qquad c_+>0.
\]

Hence its adverse part is power-saving and is closed in every one-sided
conclusion ledger.

## 2. Smooth-boundary packet

`L-102881` proves that, for every fixed squareclass and every fixed nonzero
owner phase,

\[
|\mathcal T_{p,q}^{\rm bdry}(Y)|
\ll_R(\log(2Y))^2\log\log(3Y).
\]

This closes its local coefficient/energy cost.  It does **not** allow the
boundary fields to be summed source-blindly over all owner squareclasses.

## 3. Balanced Type-II packet

The exact balanced source is `L-102868.3`; it retains the stopped monoids,
Vaughan coefficients, adaptive nonzero owner phases and all six core
variables.

## Exact final coherent statement

Define

```text
SVQDSP102882:
  after exact carrier, source-region, gauge, shared-owner and owner/core-overlap
  recombination, the coherent owner-squareclass sum of

    T_bdry + B_bal

  has subpower logarithmic negative mass in the fixed ratio-eight outer
  observation, uniformly in the stopping prime q.
```

Then

\[
\boxed{
\mathrm{SVQDSP}_{102882}
\Longrightarrow
\mathrm{BQSP}_{102870}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-102882.2}

The unrestricted Type-I sign is no longer part of the open theorem.  The
smooth boundary and balanced Type-II rows share one coherent owner/phase
summation; neither is silently discarded, and no recursive boundary closure is
claimed without that common arithmetic estimate.