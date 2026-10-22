# L-26205 — Odd-row/even-column carry is an exact half-scale copy

Claim ID: `L-26205`  
Title: The dyadic carry matrix contains an exact isometric half-scale subsystem; only odd-column leakage obstructs recursive packing  
Status: **PROPOSED EXACT LEMMA — COMPLETE DIGITAL ALGEBRA, ODD-LEAKAGE ESTIMATE OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #244 carry matrix; `L-26201`, `T-26201`  
Scope: exact lower-scale mechanism for a prospective Parity Blocker Descent proof

## 1. Pointwise digital duplication

For integers

\[
n\ge1,
\qquad1\le q\le n,
\qquad0\le j\le n,
\]

and `epsilon in {0,1}`, the carry indicators satisfy

\[
\boxed{
\chi_{2n+1,\,2q}(2j+\epsilon)
=
\chi_{n,q}(j).
}
\tag{L-26205.1}

Indeed, write

\[
n=qk+r,\qquad0\le r<q,
\]

and

\[
j=qa+s,\qquad0\le s<q.
\]

Then

\[
(2n+1)\bmod(2q)=2r+1
\]

and

\[
(2j+\epsilon)\bmod(2q)=2s+\epsilon.
\]

For either value of `epsilon`,

\[
2s+\epsilon>2r+1
\quad\Longleftrightarrow\quad
s>r.
\]

This is precisely the lower carry condition. Thus every lower carry cell is
duplicated into the adjacent even and odd physical positions of the parent row.

## 2. Exact average and Hermitian isometry

Averaging (L-26205.1) over the `2n+2` parent positions gives

\[
\boxed{
\beta_{2n+1,\,2q}=\beta_{nq}.
}
\tag{L-26205.2}

For every finite complex coefficient vector `(x_q)_(q<=n)`,

\[
\boxed{
\begin{aligned}
&{1\over2n+2}
\sum_{J=0}^{2n+1}
\left|
\sum_{q=1}^n x_q\chi_{2n+1,\,2q}(J)
\right|^2\\
&\qquad=
{1\over n+1}
\sum_{j=0}^{n}
\left|
\sum_{q=1}^n x_q\chi_{nq}(j)
\right|^2.
\end{aligned}}
\tag{L-26205.3}

The same equality holds for every polarized cross term. The digital lift is
therefore an exact Hermitian isometry, not merely a coefficient identity.

## 3. Half-scale lift of a packing vector

Let `Y>=2` and let `d=(d(n))_(2<=n<=Y)` be any nonnegative vector. Define its
odd-row lift to endpoint `X=2Y+1` by

\[
\boxed{
(\mathcal L_2d)(2n+1)
=2^{-1/2}d(n),
\qquad
(\mathcal L_2d)(N)=0
\quad\text{for all other }N.
}
\tag{L-26205.4}

Then for every `2<=q<=Y`,

\[
\boxed{
\sum_{N=2q}^{2Y+1}
(\mathcal L_2d)(N)\beta_{N,\,2q}
=
2^{-1/2}
\sum_{n=q}^{Y}d(n)\beta_{nq}.
}
\tag{L-26205.5}

The logarithmic target scales as

\[
\boxed{
\begin{aligned}
w_{2Y+1}(2q)
={}&2^{-1/2}w_Y(q)\\
&+{1\over\sqrt{2q}}
\log\left({2Y+1\over2Y}\right).
\end{aligned}}
\tag{L-26205.6}

Consequently, if `d` is feasible at endpoint `Y`, then every even parent
column has nonnegative residual

\[
\boxed{
\begin{aligned}
s_{2Y+1}^{\uparrow}(2q)
={}&2^{-1/2}s_Y(q)\\
&+{1\over\sqrt{2q}}
\log\left({2Y+1\over2Y}\right).
\end{aligned}}
\tag{L-26205.7}

The last term is an explicit positive endpoint forcing. Its unweighted sum over
`q<=Y` is `O(Y^{-1/2})`.

Thus the even-column half of the carry problem descends exactly from scale
`2Y+1` to scale `Y`.

## 4. The sole digital obstruction: odd-column leakage

The lifted vector also contributes to odd columns. Define

\[
\boxed{
\mathcal O_{Y,d}(r)
=
2^{-1/2}
\sum_{n=r}^{Y}
 d(n)\beta_{2n+1,\,2r+1},
\qquad1\le r\le Y.
}
\tag{L-26205.8}

There is no analogue of (L-26205.2) reducing this coefficient to one lower
carry row. In a nonnegative packing, one must prove

\[
\mathcal O_{Y,d}(r)
\le w_{2Y+1}(2r+1)
\tag{L-26205.9}

or remove the excess by an explicitly signed correction before positivity is
restored.

This odd-column leakage is the exact remaining digital channel. It may not be
ignored merely because the even-column subsystem is perfect.

## 5. Connection to the dyadic source

For odd `m`, the dyadic source has valuation layers

\[
b_2(m)=\mu(m),
\qquad
b_2(2m)=-2\mu(m),
\qquad
b_2(4m)=\mu(m),
\]

and it vanishes on higher powers of two. With zero padding outside the active
constraint range, the signed slack is

\[
\Pi_2(X)
=
\sum_{\substack{m\le X\\m\text{ odd}}}
\mu(m)
[s_X(m)-2s_X(2m)+s_X(4m)].
\tag{L-26205.10}

It pairs precisely one odd-column channel with the two even descendants in
(L-26205.7). The production geometry suggested by the parity comb is therefore

```text
one odd parent column
+ two exact even descendants
-> one dyadic second difference.
```

The even terms already descend to half scale. A proof of PBD needs only a signed
identity controlling the odd leakage in this same Möbius-weighted combination.

## 6. Odd-Leakage Descent research target

A production **Odd-Leakage Descent** theorem should start from the canonical
lower-scale greedy vector, apply the lift (L-26205.4), include every correction
required to restore feasibility on odd columns, and emit an exact signed
identity of the form

\[
\Pi_2(2Y+1)
=
\Pi_2(Y)
+\mathcal E_Y,
\tag{L-26205.11}

or a one-sided half-scale inequality, with

\[
|\mathcal E_Y|\le C\log^A(2Y).
\tag{L-26205.12}

Equations (L-26205.11)--(L-26205.12) are a target, not a theorem proved in this
file. A production proof must specify:

1. the exact odd-column residual;
2. every feasibility correction;
3. all three dyadic valuation layers;
4. the bottom charges at `2` and `3`;
5. equality before absolute values.

Such an identity would imply the PBD recurrence of `T-26201`.

## 7. Review mutations

A checker for a future odd-leakage certificate must reject:

```text
use beta_(2n,2q)=beta_(n,q)
omit one of the duplicated positions 2j or 2j+1
replace endpoint 2Y+1 by 2Y without its correction row
ignore odd-column contributions
take absolute values before the three dyadic valuation layers recombine
route an odd child above Y
```

## 8. Proof boundary

Closed exactly:

- pointwise digital duplication;
- averaged carry and Hermitian isometry;
- half-scale lift of every even column;
- explicit endpoint forcing;
- localization of the remaining obstruction to odd-column leakage.

Open:

- Odd-Leakage Descent;
- PBD/DSS;
- RH.
