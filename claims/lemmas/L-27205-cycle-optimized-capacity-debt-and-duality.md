# L-27205 — Cycle-optimized capacity debt and duality

Claim ID: `L-27205`  
Title: The complete signed fragmentation error is one cycle-optimized negative-capacity debt with an exact bounded-superadditive dual  
Status: **PROPOSED EXACT FINITE/ASYMPTOTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26205`, `L-27203`, `L-27204`; finite LP duality  
Scope: arbitrary exact signed balanced fragmentation of the prime-ramp target; no RH assumption

## 1. Balanced split columns and the capacity metric

Fix `0<eta<1/2` and an endpoint `X`. For every unordered eta-balanced split

\[
e=(n,j),\qquad
2\le n\le X,\qquad
\eta n\le j\le n/2,
\]

put

\[
\chi_e(q)
=\left\lfloor\frac nq\right\rfloor
 -\left\lfloor\frac jq\right\rfloor
 -\left\lfloor\frac{n-j}{q}\right\rfloor
\in\{0,1\}.
\tag{L-27205.1}
\]

Define the positive capacity weight

\[
\boxed{
\omega_e
=\sum_{q=2}^{n}\frac{\chi_e(q)}{\sqrt q}.}
\tag{L-27205.2}
\]

Because every integer

\[
\max(j,n-j)<q\le n
\]

is a carry, there is a constant `c_eta>0`, depending only on `eta`, such that

\[
\boxed{
c_\eta\sqrt n\le\omega_e\le2\sqrt n.}
\tag{L-27205.3}
\]

The upper bound is the elementary estimate
`sum_(q<=n)q^(-1/2)<=2sqrt(n)`. For the lower bound, the terminal interval has
at least `eta n-O(1)` elements and each has weight at least `n^(-1/2)`; the
finitely many small parents are absorbed into `c_eta`.

## 2. Exact baseline plus negative-debt identity

Let `d=(d_e)` be any real eta-balanced split flow whose complete carry loads
are the prime-ramp target

\[
\boxed{
L_q(d):=\sum_e d_e\chi_e(q)
=w_X(q):=q^{-1/2}\log(X/q)
\qquad(2\le q\le X).}
\tag{L-27205.4}
\]

Define

\[
K_X
=\sum_{q=2}^{X}\frac{w_X(q)}{\sqrt q}
=\sum_{q=2}^{X}\frac{\log(X/q)}q
=O((\log X)^2).
\tag{L-27205.5}
\]

Interchanging the finite sums gives the exact signed identity

\[
\boxed{
\sum_e d_e\omega_e=K_X.}
\tag{L-27205.6}
\]

Put

\[
\mathcal N_\omega(d)
=\sum_e\omega_e(-d_e)_+,
\qquad
\|d\|_\omega
=\sum_e\omega_e|d_e|.
\tag{L-27205.7}
\]

Then

\[
\boxed{
\|d\|_\omega
=K_X+2\mathcal N_\omega(d).}
\tag{L-27205.8}
\]

Thus every exact signed solution has the same positive baseline. All excess
total variation is exactly twice its weighted negative split mass.

## 3. Cycle-optimized debt

Let `r_X=r^(w_X)` be the exact target divergence of `L-26205`. Use the
canonical balanced tree solution and fundamental-cycle matrix of `L-27204`:

\[
d(z)=d_X^{\rm tree}+C_\eta z,
\qquad
\partial d(z)=r_X.
\tag{L-27205.9}
\]

Every exact eta-balanced solution occurs uniquely in this form. Define

\[
\boxed{
\mathfrak N_\eta(X)
=\min_z
 \sum_e\omega_e[-d_X^{\rm tree}-C_\eta z]_+ .}
\tag{L-27205.10}
\]

This is a finite linear programme. Its minimum is attained. Moreover,

\[
\boxed{
\mathfrak N_\eta(X)=0
\quad\Longleftrightarrow\quad
\text{MFT holds at }X.}
\tag{L-27205.11}
\]

Indeed zero debt is exactly a nonnegative exact flow. Conversely, an MFT flow
is an admissible zero-debt point.

The ternary counterexample of `R-27201` proves only that one particular cycle
coordinate has positive debt. It gives no lower bound for the optimized quantity
(L-27205.10).

## 4. Exact dual

Let `B_eta` be the node-divergence matrix, whose split column is

\[
B_\eta e=e_n-e_j-e_{n-j}.
\]

Write a signed flow as `d=p-n`, with `p,n>=0`. The primal form of
(L-27205.10) is

\[
\min\ \omega^Tn
\quad\text{subject to}\quad
B_\eta p-B_\eta n=r_X,
\qquad p,n\ge0.
\tag{L-27205.12}
\]

Finite LP duality gives

\[
\boxed{
\mathfrak N_\eta(X)
=
\max_F\left[-\sum_{m=1}^{X}r_X(m)F(m)\right],}
\tag{L-27205.13}
\]

where the maximum is over all real potentials satisfying, on every allowed
split,

\[
\boxed{
0\le
F(n)-F(j)-F(n-j)
\le\omega_{n,j}.}
\tag{L-27205.14}
\]

The lower inequality is balanced superadditivity. The upper inequality is the
capacity normalization which prevents arbitrary rescaling.

Consequently an exact dual potential with value `D` proves

\[
\mathfrak N_\eta(X)\ge D,
\]

while a primal cycle vector with debt `D` proves

\[
\mathfrak N_\eta(X)\le D.
\]

This gives a fail-closed finite certificate on both sides.

## 5. Entropy error is controlled by capacity variation

For one split put

\[
\ell_e=\log\binom nj,
\qquad
c_e=\sum_{q=2}^{n}\chi_e(q).
\]

The corrected balanced entropy theorem `L-27203` gives

\[
|\ell_e-c_e|\le C_\eta\sqrt n.
\tag{L-27205.15}
\]

Together with (L-27205.3), this yields a constant `A_eta` such that

\[
\boxed{
|\ell_e-c_e|\le A_\eta\omega_e.}
\tag{L-27205.16}
\]

For an exact signed flow, Legendre--Kummer and (L-27205.4) give

\[
\sum_e d_e\ell_e
=
\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a},
\tag{L-27205.17}
\]

whereas

\[
\sum_e d_ec_e
=
\sum_{q=2}^{X}q^{-1/2}\log(X/q).
\tag{L-27205.18}
\]

Therefore

\[
\boxed{
\left|
\sum_{p^a\le X}
 \frac{\Lambda(p^a)}{\sqrt{p^a}}
 \log\frac X{p^a}
-
\sum_{q=2}^{X}q^{-1/2}\log(X/q)
\right|
\le
A_\eta\bigl(K_X+2\mathcal N_\omega(d)\bigr).}
\tag{L-27205.19}
\]

Taking the optimal flow gives the same bound with
`mathfrak N_eta(X)`.

## 6. A strictly weaker closing theorem

Exact MFT asks for

\[
\mathfrak N_\eta(X)=0.
\]

For the RH deduction it is enough to prove the strictly weaker estimate

\[
\boxed{
\mathfrak N_\eta(X)=X^{o(1)}.}
\tag{L-27205.20}
\]

Indeed `K_X=O(log^2 X)` and

\[
\sum_{q=2}^{X}q^{-1/2}\log(X/q)
=4\sqrt X+O(\log X).
\]

Hence (L-27205.19) gives the sharp prime-ramp estimate with subpower error.

A deterministic binary, ternary, mixed, or state-dependent signed producer is
therefore sufficient if only its **negative capacity debt**, after cycle
optimization, is subpower. Positivity of every coefficient and a subpower bound
for the full absolute producer are unnecessary.

## 7. Proof boundary

Closed exactly:

- the source-adapted capacity metric;
- baseline plus twice-negative-debt identity;
- cycle-coordinate primal;
- bounded-superadditive dual;
- exact relation to MFT;
- capacity control of the balanced entropy error;
- subpower cycle debt implies the sharp prime ramp.

Open:

- `mathfrak N_eta(X)=X^o(1)` for the actual Möbius target;
- a cofinal primal producer or dual upper theorem;
- RH.
