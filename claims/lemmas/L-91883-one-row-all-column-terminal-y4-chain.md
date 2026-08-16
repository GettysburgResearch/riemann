# L-91883 — The one native two-sorted row closes every column, has native `Y_4` cost below `60989`, and feeds the one-sided endpoint consumer

Claim ID: `L-91883`  
Status: **CANDIDATE-COMPLETE CAPACITY/COST COMPILATION ON FROZEN ANALYTIC INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-91882`; frozen all-column retained-cell estimate, terminal omission, sparse radix-four dual, exact finite dual, prime-square moat, Mellin–Landau consumer  
RH status: **unproved**

Assume `X>=10^12` and keep the row identifier `rid_X` of `L-91882`.

## 1. Signed observation and positive unused capacity

Let `e_X` be the signed retained-cell, bulk-collar, and terminal excess use of the same row. Let `u_X>=0` be genuine unused native capacity from literal omissions and the one common thinning. Define

\[
r_X=u_X-e_X.
\tag{L-91883.1}
\]

No positivity is assigned to `e_X`. Slack positivity is proved columnwise.

## 2. Every physical column, including `q<K`

The retained adjacent-cell identity sums the actual multiples `jq` belonging to retained complete cells. Therefore, for every `q>=2`,

\[
|v_q(E_X^I)|
<
\frac{57}{2q\sqrt K},
\tag{L-91883.2}
\]

and

\[
|\mathcal D_4v_q(C_X-E_X^I)|
<
\frac{971}{4q\sqrt K}.
\tag{L-91883.3}
\]

These bounds include the entire range `2<=q<K`.

For every nonterminal column,

\[
\frac{|e_X^{(4)}(q)|}{\Omega_X(q)}
<
\frac{129}{\sqrt K}.
\tag{L-91883.4}
\]

Thus

\[
\tau_K\left(1+\frac{129}{\sqrt K}\right)
=
\frac{\sqrt K+129}{\sqrt K+130}<1.
\tag{L-91883.5}
\]

## 3. Terminal reserve

The fixed top omission removes more than

\[
5033X^{-3/2}
\]

from every potentially overfilled terminal column. The complete possible terminal overfill is below

\[
4452X^{-3/2}.
\]

Hence the same row retains

\[
\boxed{581X^{-3/2}>0.}
\tag{L-91883.6}
\]

Above retained support its response is zero.

Therefore

\[
\boxed{
r_X^{(4)}(q)=\Omega_X(q)-\Xi_q(d_X)\ge0
\qquad(q\ge2).
}
\tag{L-91883.7}
\]

The finite positive radix-four inverse gives

\[
\boxed{
r_X^{\rm ord}(q)
=
\sum_{h\ge0}2^hr_X^{(4)}(4^hq)\ge0.
}
\tag{L-91883.8}
\]

Thus the same realized row satisfies

\[
\Xi(d_X)+r_X^{(4)}=\Omega_X,
\qquad
\Gamma(d_X)+r_X^{\rm ord}=w_X.
\tag{L-91883.9}
\]

## 4. Direct native `Y_4` price

Exact native duality gives

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X)
=
\langle Y_4,r_X^{(4)}\rangle\ge0.
}
\tag{L-91883.10}
\]

The identity channels have zero finite-realization comparison. The complete charge ledger is

```text
one common square-root thinning        <12012
nonterminal signed bulk comparison     <4
terminal signed comparison             <48972
literal positive omissions             <1
identity anchor/bonus comparison        =0
auxiliary port                          =0
--------------------------------------------
total                                  <60989.
```

The thinning estimate follows from the elementary unconditional bound

\[
J_\Lambda(X)<16(\log2)\sqrt X.
\]

Therefore

\[
\boxed{
0\le
J_\Lambda(X)-\mathcal H(d_X)
<60989
=o(\log^2X).
}
\tag{L-91883.11}
\]

No estimate of `J_Lambda(X)-4sqrt(X)` is used.

## 5. Endpoint consumer

Ordinary feasibility and the exact finite dual give the one-sided orientation

\[
F_\Lambda(X)
\le
J_\Lambda(X)-\mathcal H(d_X).
\tag{L-91883.12}
\]

The frozen unconditional prime-square occupancy theorem then forces eventual negativity of the prime endpoint. The frozen Mellin pole audit and Landau one-sign theorem exclude zeros with real part greater than one half; the functional equation supplies the candidate RH conclusion.

## 6. Boundary

```text
same row in producer and capacity proof         exact
same row in capacity proof and Y4 price          exact
all q<K columns                                  covered
terminal reserve                                 581 X^-3/2
native deficit                                   <60989
endpoint orientation                             upper bound
forbidden benchmark bridge                       absent
Riemann Hypothesis                               unproved pending reconstruction
```
