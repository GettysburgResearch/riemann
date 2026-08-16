# L-91884 — The live coupling has all-column native slack below 60989 and feeds the one-sided endpoint consumer

Claim ID: `L-91884`  
Status: **CANDIDATE-COMPLETE NATIVE CAPACITY/COST THEOREM ON FROZEN ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-16  
Inputs: `L-91822`, `L-91823`, `L-93785`, `T-91820`, `L-91882--L-91883`  
RH status: **unproved**

For `X>=10^12`, the constructed row is nonnegative.

## 1. Small ordinary columns

The retained-cell estimates hold for every `q>=2`, including `2<=q<K`:

\[
|v_q(E_X^I)|<\frac{57}{2q\sqrt K},
\]

\[
|\mathcal D_4v_q(E_X^I)|<\frac{171}{4q\sqrt K}.
\]

The bulk collar plus retained mismatch satisfies

\[
|\mathcal D_4v_q(C_X-E_X^I)|<\frac{971}{4q\sqrt K}.
\]

The anchored identity block has zero finite/continuum discrepancy.

## 2. Nonterminal and terminal detail

For `2<=q<=X/4`,

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)=\frac{\sqrt K+129}{\sqrt K+130}<1.
\]

The terminal top omission leaves

\[
(5033-4452)X^{-3/2}=581X^{-3/2}>0.
\]

Therefore

\[
\Xi_q(d_X)\le\Omega_X(q)\qquad(q\ge2).
\]

Positive radix-four inversion gives

\[
C_q(d_X)\le w_X(q)\qquad(q\ge2).
\]

## 3. Direct native cost

The exact native dual and the one-use observation ledger give

```text
common thinning                  <12012
nonterminal signed comparison       <4
terminal signed comparison       <48972
literal positive omissions          <1
port/base                             0
--------------------------------------
native deficit                    <60989
```

Thus

\[
\boxed{0\le J_\Lambda(X)-\mathcal H(d_X)<60989=o(\log^2X).}
\tag{L-91884.1}
\]

No estimate of `J_Lambda(X)-4sqrt(X)` is used.

## 4. Endpoint orientation

The exact finite dual gives the upper bound

\[
F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X).
\]

On the frozen prime-square moat and Mellin--Landau inputs, this supplies the proposed RH conclusion. Those analytic inputs and the new arithmetic coupling remain independent reconstruction obligations.