# L-91873 — Small-`q`, radix-four, native `Y_4`, and the endpoint consumer form one audited chain

Claim ID: `L-91873`  
Status: **CANDIDATE-COMPLETE CAPACITY/COST COMPILATION ON FROZEN INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Inputs: PR #499 `L-91822--L-91823`, PR #496 `L-92900`, `T-91820`  
RH status: **unproved**

## 1. Native comparison before estimates

By `L-91870`, the ideal source observation plus the exact finite defect is the
native datum. By `L-91872`, all positive owner packets are realized in one row.
Let `e_X` be the signed finite-realization excess and `u_X` the genuine positive
capacity removed by one thinning and literal omissions.

The two-ledger identity is

\[
 r_X=u_X-e_X.
\tag{L-91873.1}
\]

Slack positivity is proved by all-column domination, not by declaring `e_X`
positive source.

## 2. Every small ordinary column

For retained adjacent-cell mismatch,

\[
 |v_q(E_X^I)|<\frac{57}{2q\sqrt K}
 \qquad(q\ge2),
\tag{L-91873.2}
\]

and

\[
 |\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\tag{L-91873.3}
\]

The collar plus mismatch satisfies

\[
 |\mathcal D_4v_q(C_X-E_X^I)|
 <\frac{971}{4q\sqrt K}.
\tag{L-91873.4}
\]

These estimates include `2<=q<K`; support above `K` does not make those
columns vanish, and the proof sums their actual multiples `jq`.

## 3. Nonterminal and terminal detail feasibility

For every `2<=q<=X/4`,

\[
 \tau_K\left(1+\frac{129}{\sqrt K}\right)
 =\frac{\sqrt K+129}{\sqrt K+130}<1.
\tag{L-91873.5}
\]

The terminal possible overfill is below `4452X^(-3/2)` and the source-owned top
omission supplies more than `5033X^(-3/2)`, leaving

\[
 581X^{-3/2}>0.
\tag{L-91873.6}
\]

Therefore

\[
\boxed{
 r_X^{(4)}(q)=\Omega_X(q)-\Xi_q(d_X)\ge0
 \qquad(q\ge2).
}
\tag{L-91873.7}
\]

Positive radix-four inversion gives the ordinary complement

\[
\boxed{
 r_X^{\rm ord}(q)=
 \sum_{h\ge0}2^hr_X^{(4)}(4^hq)\ge0,
}
\tag{L-91873.8}
\]

so `C_(d_X)<=w_X` in every physical column.

## 4. Direct native `Y_4` price

The exact dual identity is

\[
\boxed{
 J_\Lambda(X)-\mathcal H(d_X)
 =\langle Y_4,r_X^{(4)}\rangle.
}
\tag{L-91873.9}
\]

The source and observation ledgers contain exactly four priced classes:

```text
common square-root thinning     <12012
nonterminal signed comparison      <4
terminal signed comparison      <48972
literal positive omissions         <1
```

Thus, for `X>=10^12`,

\[
\boxed{
 0\le J_\Lambda(X)-\mathcal H(d_X)<60989.
}
\tag{L-91873.10}
\]

Hall cancellation, stopping-line ownership, Target-Lorenz realization, child
placement, label erasure and the one quantizer are internal positive operations
and add no fifth cost class.

## 5. Endpoint consumer

The exact finite dual has the one-sided orientation

\[
 F_\Lambda(X)
 \le J_\Lambda(X)-\mathcal H(d_X).
\tag{L-91873.11}
\]

Hence `F_Lambda(X)=o(log^2X)`. On the frozen unconditional prime-square moat and
Mellin--Landau endpoint inputs, the resulting eventual prime-endpoint sign
excludes every zero with real part greater than one half; the functional
equation gives the proposed RH conclusion.

No bound for `J_Lambda(X)-4sqrt(X)` is used.

```text
q<K columns                         explicitly covered
ordinary q/4q before detail         exact common-row assembly
detail complement                   nonnegative
ordinary complement                 positive inverse
native Y4 charge                    <60989
endpoint orientation                upper bound
RH                                  unproved pending reconstruction
```
