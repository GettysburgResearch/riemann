# R-103120 — Beta normalization does not cancel the QPTI owner mode

Claim ID: `R-103120`  
Status: **EXACT IMPLICATION FIREWALL; QPTI NOT REFUTED**  
Created: 2026-08-26  
Depends on: `L-103120`, binding `R-103110`, `L-102959`; PR #756 physical-squareclass contract  
RH status: **unproved**

The Euler–Beta formula might suggest that canonical pair averaging cancels the
semiprime-owner main term before any arithmetic estimate is used.  It does
not.

## 1. Every fixed live core retains a full owner polynomial

Fix a squarefree core `c` with `k=omega(c)`.  Its contribution to
(L-103120.2) is

\[
\boxed{
\mathscr E_c(s)
=
{\mu(c)\over\binom{k+2}{2}}
\left(\prod_{r\mid c}z_r(s)^2\right)
\sum_{\substack{p<q\\(pq,c)=1}}z_p(s)z_q(s).
}
\tag{R-103120.1}
\]

For real `s>1/2`, all `z_p(s)` are positive.  Therefore

\[
\operatorname{sgn}\mathscr E_c(s)=\mu(c)
\]

whenever at least two owner primes are available.  In particular, a
squarefree two-prime core—already outside the root and first-chaos sectors—has

\[
\boxed{
\mathscr E_c(s)>0.
}
\tag{R-103120.2}
\]

The factor `1/binom(k+2,2)` divides one occurrence among its legal owner pairs;
it does not annihilate the owner polynomial.

## 2. The Beta integral has the same mode coefficient

Expanding (L-103120.5), the coefficient of

\[
\prod_{r\mid c}z_r^2
\]

is

\[
2(-1)^k
\int_0^1(1-\theta)\theta^k\,d\theta
\sum_{p<q}z_pz_q
=
{\mu(c)\over\binom{k+2}{2}}
\sum_{p<q}z_pz_q.
\tag{R-103120.3}
\]

Thus there is no hidden endpoint, Beta, or distinct-owner cancellation of a
fixed core layer.

## 3. Consequence for fibrewise estimates

A proof which applies the fixed-owner zero-moment estimate and then takes
absolute values before summing owner products necessarily retains the positive
quantity

\[
\sum_{p<q}|z_pz_q|.
\]

At the physical critical line its finite-prime-box truncations are unbounded;
canonical pair normalization does not change that fact.  The same-occurrence
multiplicity bound of `L-102747` cannot pay this cross-occurrence owner sum.
This is the arithmetic version of the operator gap in `R-103110`.

Likewise, an arbitrary incidence-mask phase theorem such as `L-102959` still
requires source-specific `M_1,M_2` control.  The Beta coefficient alone does
not supply those bounds.

## 4. What a valid closure must do

The signs in (R-103120.1) occur in the **core** variable.  Therefore a valid
QPTI proof must retain at least one of the following until after physical
owner summation:

```text
Möbius-signed recombination of different core layers;
a source-faithful bilinear dispersion correlating different owner fibres;
a connected character/Kummer family with the varying-core sign retained,
  followed by an affordable principal-member individualization;
an exact positivity identity for the complete owner–core transform,
  not for each owner fibre separately.
```

This agrees with PR #756's requirement to retain the full physical
squareclasses `P*c^2,Q*d^2`, correlate fibres before squaring, preserve the
varying-conductor signed recombination, control Wick contractions, and isolate
the principal member.

## Scope

The nonzero fixed-core mode is not a counterexample to QPTI.  Cancellation
between different Möbius core layers may still prove the theorem.  The result
only rules out a combinatorial or source-blind owner-collapse proof.
