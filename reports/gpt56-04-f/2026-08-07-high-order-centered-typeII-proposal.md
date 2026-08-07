# High-order centered Type-II proposal after the positive review

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Frozen review input: PR #158 at `7902480c92a34e8ca5788e8e1e844ac3727e3a4e`  
Imported arithmetic source: PR #216 at `b76eef1b769584aa9d66d082bfc6634126f986a2`  
Status: **PROPOSED PENDING INDEPENDENT REVIEW; RH NOT CLAIMED PROVED**

## Executive result

The latest review verified the repaired analytic and finite-Gram front half but
correctly rejected an undeclared Vaughan/Heath--Brown “Type-II estimate.”

This pass closes the missing **finite architecture**:

1. ordinary-prime and full-von-Mangoldt safe blocks are polynomially equivalent;
2. both use the same adjoint/normal geometry, not the rejected product geometry;
3. high-order compact safe windows provide an exact finite null-mode quotient;
4. the truncated Heath--Brown identity, tuple coefficients, and deterministic
   Type-I/Type-II partition are finite and exact;
5. signed tuples are grouped into a finite destination-packet dictionary before
   Gram Cauchy--Schwarz;
6. all cross packets reduce to a finite vector of positive self-energies;
7. scalar, finite-vector, and tensor strict-scale-contraction composition is
   proved;
8. an increasing-order theorem states the exact coefficient-rate condition that
   would force RH.

The sole remaining proposed arithmetic theorem is the centered packet estimate
`CP(K)` in `M-15112`. It includes useful companion construction, transition
residuals, terminal Type-I packets, centered Type-II estimates, and the
vanishing coefficient-rate limit.

## 1. Prime/full-`Lambda` bridge

For the fixed compact safe window `H`,

\[
 Q_H^\Lambda-Q_H^{\mathbb P}
 =\sum_{k\ge2}\sum_p{\log p\over p^{k/2}}
 H(x-k\log p).
\]

On a block `[J,J+1]`, the prime-square layer is `O_H(J)` by elementary integral
comparison, and all layers `k>=3` are absolutely summable. Therefore

\[
 \sup_{J\le x\le J+1}
 |Q_H^\Lambda(x)-Q_H^{\mathbb P}(x)|
 \ll_H1+J.
\]

Hence

\[
 \mathcal B_J^\Lambda
 \le2\mathcal B_J^{\mathbb P}+O_H(J^2)
\]

and conversely. Polynomial and `exp(o(J))` growth are equivalent for the two
sources.

Both blocks are exact localized normal forms

\[
 \langle H,\mathcal P^*\chi_J\mathcal P H\rangle.
\]

This is the adjoint/factor-ratio orientation verified in PR #216.

## 2. High-order null quotient

For `m>=1`, define

\[
 H^{[m]}
 =\Delta_0^{m-1}\Delta_{1/2}^{m-1}H.
\]

Its transform has order-`m` zeros at both boundary points and remains zero-free
in the open counterexample strip. The block kernel annihilates

\[
 u^rdu,
 \qquad
 u^re^{u/2}du,
 \qquad0\le r<m,
\]

in each leg.

This proves an exact rule: any source-bound companion certified in that finite
null space may be subtracted independently from one packet without changing the
Gram.

It does **not** prove that a finite cutoff packet is itself equal to a global
polynomial pole model. Truncated Möbius factors and first-crossing cutoffs create
shifted step boundaries and compact transitions. Those residuals remain inside
`CP(K)` unless separately estimated.

## 3. Exact finite Heath--Brown packet

For order `K`, endpoint `X`, and `V=X^(1/K)`, put

\[
 \mu_V(n)=\mu(n)1_{n\le V}.
\]

For every `n<=X`,

\[
 \Lambda(n)
 =\sum_{j=1}^K(-1)^{j-1}{K\choose j}
  (\mu_V^{*j}*\log*1^{*(j-1)})(n).
\]

Every tuple has the exact coefficient

\[
 (-1)^{j-1}{K\choose j}
 \mu(d_1)\cdots\mu(d_j)\log q.
\]

A deterministic first-crossing rule assigns it to Type I or Type II. Type-I
packets receive either a reduced-complexity or terminal flag. No term is hidden
under a conventional label.

Tuple contributions sharing one destination are recombined across all identity
indices with their exact signed binomial coefficients before any absolute value
or Gram bound. The resulting finite packet self-energies form the auxiliary
vector.

## 4. The exact closure theorem

Let `E_(K,tau)(J)` be the finite vector of signed-packet self-energies. If

\[
 E_{K,\tau}(J)
 \le a_{K,\tau}(J)
 +\sum_\upsilon b_{K,\tau\upsilon}(J)
  \max_{k\le(1-\delta_K)J+O_K(1)}E_{K,\upsilon}(k)
\]

with subexponential coefficients, then every row energy is `exp(o(J))`.

A tensor version is proved as well. If the logarithmic scale weights satisfy

\[
 \sum_s\theta_s\alpha_s<1,
\]

then finite products of lower-scale auxiliary energies remain subexponential.
No adjacent-block coefficient smaller than one is required.

## 5. Increasing-order quantitative route

At fixed order, allow a coefficient loss

\[
 e^{\epsilon_KJ}.
\]

If the strict scale reserve is `delta_K`, then the row exponent is at most

\[
 {\epsilon_K\over\delta_K}.
\]

Every high-order safe window detects the same rightmost-zero exponent, so

\[
 2\Theta_\zeta
 \le{\epsilon_K\over\delta_K}.
\]

A family satisfying

\[
 {\epsilon_K\over\delta_K}\to0
\]

proves RH. The tensor version replaces `delta_K` by `1-kappa_K`.

## 6. Exact regression

`X-15125` checks:

- the truncated Heath--Brown identity for `K=3,V=4,X=64` on a symbolic
  completely-additive prime-log basis;
- exact tuple expansion and the deterministic first-crossing partition;
- independent subtraction of declared null modes in a finite Gram;
- equality of direct and recombined energies;
- the finite-vector Cauchy bound;
- a three-component strict-scale-contraction recurrence.

Retained values:

```text
Heath-Brown coefficient mismatches  none
Type-I tuples                       30
Type-II tuples                      41
partition failures                  none
null-mode energies                  0, 0
direct / recombined Gram            202 / 202
finite-vector bound                 570
main proof SHA-256
3dc50743f1b3b435e2d9b969c5a1191ef0a94e89a4f4ccd17a2b211e6d91dea0
partition proof SHA-256
fb68b871d6c8cbf984ee018d5bf9d7ddef374811a5dce5b604af8215cadfe22f
tests                               10/10 PASS
```

This is exact algebraic regression only. It does not test `CP(K)` on Riemann
data.

## 7. Exact remaining theorem

For an unbounded sequence of orders `K`, prove that the complete signed packet
vector satisfies a linear or tensor strict-scale-contraction estimate whose
coefficient rate tends to zero relative to the contraction reserve.

The estimate must preserve:

1. signed binomial packets before absolute values;
2. certified null companions only;
3. every shifted-boundary and cutoff transition residual;
4. adjoint/factor-ratio normal geometry;
5. every reduced-complexity and terminal Type-I packet;
6. every Type-II, divisor, Möbius, log, and prime-power packet;
7. exact support destinations and coefficient rates.

A standard large-sieve citation without this ledger does not prove the theorem.

## SERIOUS RESOLUTION PATH

```text
high-order compact safe window
-> exact full-Lambda / ordinary-prime normal energy
-> exact finite Heath-Brown coefficient packet
-> certified null-mode quotient
-> signed Type-I/II destination packets
-> finite auxiliary-energy vector
-> vanishing-rate strict scale contraction
-> rightmost-zero exponent zero
-> RH.
```

All arrows except `CP(K)` are explicit.

## Status boundary

```text
Heath-Brown coefficient bookkeeping:   COMPLETE, proposed pending review
Type-I/II tuple partition:              COMPLETE, proposed pending review
Null-mode centering mechanism:          COMPLETE, proposed pending review
Useful packet companion construction:  OPEN inside CP(K)
Transition and terminal Type-I bounds:  OPEN inside CP(K)
Finite auxiliary closure schema:        COMPLETE, proposed pending review
Scale-contraction composition:          COMPLETE, proposed pending review
Centered packet analytic estimate:      OPEN / RH-BEARING
Riemann Hypothesis:                     NOT CLAIMED PROVED
```
