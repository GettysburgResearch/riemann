# R-30501 — The terminal atomic boundary norm is macroscopic

Claim ID: `R-30501`  
Title: A stopped critical power already has linear square-root atomic boundary norm, so the PR #304 terminal-commutator estimate cannot be obtained from the declared positive endpoint layer cake  
Status: **EXACT REFUTATION OF THE LOAD-BEARING NORM IDENTIFICATION IN PR #304**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Dependencies: PR #286 `L-28402`; elementary alternating-series and Möbius inversion  
Scope: the asserted polylogarithmic atomic divisor-source norm in `L-30403/T-30401`

## 1. The stopped pure-power boundary

Fix an integer endpoint `N` and the stopped critical power

\[
p_N(n)=n^{-1/2}\mathbf 1_{n\le N}.
\tag{R-30501.1}
\]

Let `mathscr C` be the infinite shifted central operator and `mathscr C_N` its
finite zero-extended version from PR #286.  Their cutoff difference is

\[
G_N(q):=(\mathscr Q_Np)(q)
=\sum_{2kq-1>N}(2kq-1)^{-1/2}
 -\sum_{(2k+1)q>N}((2k+1)q)^{-1/2}.
\tag{R-30501.2}
\]

The finite output endpoint is

\[
M=\left\lfloor\frac{N+1}{2}\right\rfloor.
\tag{R-30501.3}
\]

Every divisor-source realization used by the adjacent-commutator map has the
form

\[
G_N(q)=\sum_{\substack{m\le M\\q\mid m}}\sigma_N(m).
\tag{R-30501.4}
\]

The source is unique, by Möbius inversion on multiples:

\[
\sigma_N(m)=\sum_{k\le M/m}\mu(k)G_N(mk).
\tag{R-30501.5}
\]

## 2. Exact top-cell formula

Assume

\[
\frac N3<q\le\frac N2.
\tag{R-30501.6}
\]

Then the first omitted shifted-even index is `k=2`, whereas the first omitted
odd index is `k=1`.  Consequently

\[
\boxed{
\sqrt q\,G_N(q)
=-\frac1{\sqrt3}
 +\sum_{k\ge2}
 \left[
  (2k-q^{-1})^{-1/2}-(2k+1)^{-1/2}
 \right].
}
\tag{R-30501.7}

Separate the unshifted alternating limit:

\[
\sqrt q\,G_N(q)=L+R_q,
\tag{R-30501.8}
\]

where

\[
L=1-\eta(1/2)-2^{-1/2}
\tag{R-30501.9}
\]

and

\[
R_q=\sum_{k\ge2}
\left[(2k-q^{-1})^{-1/2}-(2k)^{-1/2}\right]\ge0.
\tag{R-30501.10}
\]

## 3. A completely elementary negative moat

The alternating series gives

\[
\eta(1/2)>
1-\frac1{\sqrt2}+\frac1{\sqrt3}-\frac12
 +\frac1{\sqrt5}-\frac1{\sqrt6}.
\tag{R-30501.11}
\]

Therefore

\[
L<
\frac12+\frac1{\sqrt6}-\frac1{\sqrt3}-\frac1{\sqrt5}.
\tag{R-30501.12}
\]

The rational square checks

\[
\frac{577}{1000}<\frac1{\sqrt3},
\qquad
\frac{447}{1000}<\frac1{\sqrt5},
\qquad
\frac1{\sqrt6}<\frac{409}{1000}
\tag{R-30501.13}
\]

give

\[
\boxed{L<-\frac1{10}.}
\tag{R-30501.14}
\]

By the mean-value theorem, with `z=1/q<=1/2`,

\[
R_q
\le\frac1{2q}
\sum_{k\ge2}(2k-1/2)^{-3/2}.
\tag{R-30501.15}
\]

The decreasing-integral bound gives

\[
\begin{aligned}
\sum_{k\ge2}(2k-1/2)^{-3/2}
&\le (7/2)^{-3/2}
 +\int_2^\infty(2x-1/2)^{-3/2}\,dx\\
&=\left(\frac27\right)^{3/2}
 +\left(\frac27\right)^{1/2}<1,
\end{aligned}
\tag{R-30501.16}
\]

because `162<343`. Hence, for every `q>=10`,

\[
R_q<\frac1{20}.
\tag{R-30501.17}
\]

Combining (R-30501.14) and (R-30501.17),

\[
\boxed{
G_N(q)<-\frac1{20\sqrt q}
\qquad
\left(\frac N3<q\le\frac N2,\ q\ge10\right).
}
\tag{R-30501.18}
\]

No zeta-zero estimate, prime theorem, or numerical limit is used.

## 4. Linear atomic norm

For `q` in (R-30501.18), one has `q>M/2`.  Thus no multiple `2q` lies below
`M`, and the unique source identity (R-30501.4) reduces to

\[
\boxed{\sigma_N(q)=G_N(q).}
\tag{R-30501.19}
\]

For `N>=120`, the interval contains at least `N/12` integers. Therefore

\[
\boxed{
\sum_{m=2}^{M}\sqrt m\,|\sigma_N(m)|
\ge\frac N{240}.
}
\tag{R-30501.20}
\]

This directly contradicts a polylogarithmic estimate for the atomic norm of the
complete stopped-power boundary source.

## 5. The positive endpoint layer cake cannot be normed separately

PR #301 resolves the critical target as

\[
q^{-1/2}\log(X/q)
=\sum_{Y=q}^{X-1}\log\frac{Y+1}{Y}\,q^{-1/2}.
\tag{R-30501.21}
\]

Every coefficient is positive.  If each stopped-power boundary is placed in a
positive boundary cone and charged by the atomic norm before endpoint
recombination, then (R-30501.20) and

\[
\log(1+1/Y)\ge\frac1{2Y}
\]

give a fixed positive cost for every `Y>=120`.  The accumulated cost is
`Omega(X)`, not polylogarithmic.

Equivalently, the top-cell source coordinates in (R-30501.18) are negative.
Positive Peano coefficients at an internal jet label do not become a positive
divisor source merely by tensor notation.

## 6. Consequences for PRs #301 and #304

The following assertions are unavailable:

```text
positive stopped-power jet source
 -> positive divisor-source coordinate;

PR #286 boundary capacity norm
 = sum_m sqrt(m)|sigma_m| = polylog(X);

terminate every boundary source independently
 -> polylog Cycle Debt.
```

There are only two possible interpretations of the former boundary label:

1. it is the actual divisor source consumed by `Phi`; then its norm is linear by
   (R-30501.20);
2. it is only an internal Peano/quotient label; then no exact carry-module map to
   `Phi` has been supplied.

Either interpretation rejects `L-30403.6--9` and the resulting proof claim in
`T-30401`.

## 7. What survives

The following remain exact and valuable:

- the shifted analytic `6/7` contraction of PR #286;
- the adjacent-tree identity `L_q(E_h)=1_(q|h+1)`;
- the `O(sqrt(h))` capacity bound for one commutator;
- the exact stopped-power endpoint telescope;
- the necessity of recombining endpoint layers and divisor sources before any
  positive part or capacity norm.

A corrected proof must preserve the full logarithmic endpoint cancellation and
control a signed Haar/commutator ledger.  It cannot terminate the stopped-power
layers independently.

## 8. Exact verdict

```text
terminal adjacent-commutator identity             VERIFIED
atomic norm of one stopped critical boundary      OMEGA(N)
polylog atomic boundary claim in L-30403           FALSE
positive stopped-layer termination                FALSE AS DERIVED
PR #304 as a complete proof of RH                  REJECTED
Riemann Hypothesis                                 UNPROVED
```
