# M-22101 — Signed balanced-semiprime dispersion attack

Claim ID: `M-22101`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221

## Objective

Prove the sole remaining global estimate from PR #216:

\[
 \boxed{
 [\mathcal O_H^{\mathbb P}(X)]_+=\exp(o(X)),
 }
 \tag{M-22101.1}
\]

or equivalently the unit-block form from `L-22102`.

The method must preserve the signs of the complete piecewise-cubic kernel until
the final contraction. `R-22101` proves that every entrywise absolute route is
exponentially too large.

## 1. Exact finite cell producer

Use `L-22102` to emit once and for all:

```text
cell inequalities Omega_r
cubic coefficient vectors c_r
factor-ratio support
boundary/interior flags
source digest for H
```

All coefficients lie in `Q(log 4)`. A production checker should isolate `log 4`
by one rational interval and perform every cell comparison outward.

## 2. Center before decomposition

Write the weighted prime measure as

\[
 dP=dP_0+d\nu,
 \qquad
 dP_0(y)=e^{y/2}dy.
\]

The complete window satisfies

\[
 H*dP_0=0.
\]

Every Type-II decomposition must therefore be applied to the **centered** form

\[
 \langle H*d\nu,H*d\nu\rangle,
\]

not to the positive prime measure followed by a separate main-term subtraction.
This keeps both linear pole cancellations and the quadratic cell cancellation
exact.

## 3. Balanced factor decomposition

For each cell, partition the fixed ratio range into finitely many smooth boxes

\[
 p\asymp P,
 \qquad
 q\asymp Q,
 \qquad
 P/Q\asymp1.
\]

Apply Heath--Brown or Vaughan identities only after the complete cell vector is
frozen. The output should be a common list of bilinear forms

\[
 \mathcal T_\ell(j)
 =\sum_{m\sim M}\sum_{n\sim N}
  \alpha_m\beta_n W_\ell(m,n;j),
\]

and one final exact coefficient vector `c` such that

\[
 \mathcal O_H(j)=\sum_\ell c_\ell\mathcal T_\ell(j).
\]

No `|T_l|` is taken before this sum.

## 4. Dispersion target

The preferred proof object is a common quadratic majorant

\[
 \boxed{
 \left|
  \sum_\ell c_\ell\mathcal T_\ell(j)
 \right|
 \le
 P(j)+\varepsilon_j\max_{k<j}\mathcal B_H(k),
 }
 \tag{M-22101.2}
\]

where `P` is polynomial and

\[
 \varepsilon_j\to0.
\]

Iteration gives

\[
 \mathcal B_H(j)=\exp(o(j)),
\]

hence RH through `T-21502`.

An equally valid terminal certificate is a direct signed operator estimate

\[
 \left[\sum_\ell c_\ell T_\ell(j)\right]_+
 \le e^{\epsilon j}
\]

for every fixed `epsilon>0` and all sufficiently large `j`.

## 5. Candidate cancellation mechanisms

The repository should pursue only mechanisms that preserve the common cell
vector:

1. **Selberg quadratic forcing.** Insert
   \[
   \Lambda\log+\Lambda*\Lambda=\Lambda_2
   \]
   before factor separation, so the forcing and prime-pair Gram share one
   bilinear decomposition.
2. **Factor-ratio Mellin transform.** Transform the complete cubic kernel, not
   its positive and negative cells separately, and estimate the resulting
   centered prime Dirichlet polynomial.
3. **Dispersion before Cauchy.** Expand the square, subtract the continuous
   density exactly, and apply Cauchy--Schwarz only to the already-centered
   remainder.
4. **Recursive log blocks.** Use the causal Selberg equation to route every
   large block through earlier centered blocks plus a polynomial forcing.
5. **Proof-producing dual weights.** Permit an optimizer to nominate a signed
   combination of cell identities, but rationalize and replay the final dual
   inequality exactly.

## 6. Explicitly rejected shortcuts

- entrywise sieve majorants (`R-22101`);
- shrinking to a diagonal window (`R-22102`);
- finite positive block ladders;
- replacing the centered prime measure by an absolute PNT error;
- assuming square-root cancellation of prime pairs;
- using the long-double data as a sign theorem.

## 7. Serious-resolution boundary

The attack is complete exactly when it produces (M-22101.1) or (M-22101.2).
Every other result is structural preparation.

A proof of the signed estimate would finish the last arrow of PR #216 and prove
RH, subject to independent verification of `T-21502`. No such estimate is
claimed in this methodology card.
