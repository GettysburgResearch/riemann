# L-28009 — Two-contact generalized-prime Selberg reserve

Claim ID: `L-28009`  
Title: In the exact dyadic two-contact Dirichlet system, the generalized-prime Kummer square dominates the complete Selberg forcing pointwise, with a quantitative balanced reserve  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28005`; atomized carry/Kummer identity; elementary binomial monotonicity  
Scope: the complete source-matched row inequality for `A_2=zeta/(1-2^-s)`; no block recurrence or RH claim

## 1. The exact Dirichlet system

Retain

\[
 B_2(s)={1-2^{-s}\over\zeta(s)},
 \qquad
 A_2(s)=B_2(s)^{-1}={\zeta(s)\over1-2^{-s}}.
\]

The inverse coefficients are

\[
 \boxed{a_2(m)=v_2(m)+1>0.}
 \tag{L-28009.1}
\]

The generalized von Mangoldt and Selberg coefficients are

\[
 \Lambda_2=b_2*(a_2\log),
 \qquad
 C_2=b_2*(a_2\log^2)
       =\Lambda_2\log+\Lambda_2*\Lambda_2.
 \tag{L-28009.2}
\]

Explicitly,

\[
 \Lambda_2(q)=\Lambda(q)+(\log2)\mathbf1_{q=2^r}\ge0.
 \tag{L-28009.3}
\]

For integers `n>=2` and `0<=j<=n`, put `k=n-j` and define

\[
 \boxed{
 P_2(n,j)=\sum_{q\le n}\Lambda_2(q)\chi_{n,q}(j),
 }
 \tag{L-28009.4}
\]

\[
 \boxed{
 S_2(n,j)=\sum_{q\le n}C_2(q)\chi_{n,q}(j).
 }
 \tag{L-28009.5}
\]

The theorem is

\[
 \boxed{
 0\le S_2(n,j)\le P_2(n,j)^2
 \qquad(0\le j\le n).
 }
 \tag{L-28009.6}
\]

Unlike the false generalized-prime lift in PR #297 `R-29002`, this statement is
for the exact `b_2/A_2` two-contact system rather than the stronger
opposite-parity `omega_2` system.

## 2. Top-half formulas

For `r=1,2`, define

\[
 H_r(N)=\sum_{N/2<m\le N}a_2(m)(\log m)^r,
 \qquad H_r(0)=H_r(1)=0.
 \tag{L-28009.7}
\]

Since

\[
 \mathbf1*b_2=\varepsilon-\delta_2,
\]

one has

\[
 \mathbf1*\Lambda_2=(\varepsilon-\delta_2)*(a_2\log),
 \qquad
 \mathbf1*C_2=(\varepsilon-\delta_2)*(a_2\log^2).
\]

Applying the floor/carry functional gives exactly

\[
 \boxed{
 P_2(n,j)=H_1(n)-H_1(j)-H_1(k),
 }
 \tag{L-28009.8}
\]

\[
 \boxed{
 S_2(n,j)=H_2(n)-H_2(j)-H_2(k).
 }
 \tag{L-28009.9}
\]

## 3. Dyadic-lift representation

For `1<=t<=N`, let

\[
 \boxed{
 \tau_N(t)=2^{\lfloor\log_2(N/t)\rfloor}t.
 }
 \tag{L-28009.10}
\]

This is the unique dyadic multiple of `t` in `(N/2,N]`.

The pairs

\[
 (t,r),\qquad 0\le r\le v_2(m),\qquad m=2^rt,
\]

show that `a_2(m)` counts the dyadic divisors of `m`.  Mapping each `t<=N` to
its unique top-half dyadic lift gives a bijection and hence

\[
 \boxed{
 H_r(N)=\sum_{t=1}^{N}(\log\tau_N(t))^r
 \qquad(r=1,2).
 }
 \tag{L-28009.11}
\]

Assume by symmetry that `1<=j<=k`.  Pair the `n` numerator lifts with the
`j+k=n` denominator lifts as follows:

\[
 x_t=\tau_n(t),\quad y_t=\tau_k(t)
 \qquad(1\le t\le k),
 \tag{L-28009.12}
\]

and

\[
 x_{k+r}=\tau_n(k+r),\quad y_{k+r}=\tau_j(r)
 \qquad(1\le r\le j).
 \tag{L-28009.13}
\]

Every pair obeys `x_i>=y_i`:

- in (L-28009.12), increasing the endpoint from `k` to `n` cannot decrease the
  largest admissible dyadic multiple;
- in (L-28009.13), `x_(k+r)>n/2>=j>=y_(k+r)`.

Put

\[
 d_i=\log(x_i/y_i)\ge0.
 \tag{L-28009.14}
\]

Equations (L-28009.8)--(L-28009.13) yield the exact paired formulas

\[
 \boxed{P_2(n,j)=\sum_{i=1}^{n}d_i,}
 \tag{L-28009.15}
\]

\[
 \boxed{
 S_2(n,j)=\sum_{i=1}^{n}d_i\log(x_i y_i).
 }
 \tag{L-28009.16}
\]

In particular `P_2>=0` and `S_2>=0`.  Since `x_i,y_i<=n`,

\[
 \boxed{
 S_2(n,j)\le2\log n\,P_2(n,j).
 }
 \tag{L-28009.17}
\]

Thus (L-28009.6) follows whenever

\[
 P_2(n,j)\ge2\log n.
 \tag{L-28009.18}
\]

## 4. The complete interior range

Because `Lambda_2>=Lambda`, Kummer's theorem gives

\[
 P_2(n,j)\ge\log\binom nj.
 \tag{L-28009.19}
\]

For `n>=9` and `3<=j<=n/2`, binomial monotonicity gives

\[
 \binom nj\ge\binom n3
 ={n(n-1)(n-2)\over6}\ge n^2.
 \tag{L-28009.20}
\]

Hence (L-28009.18), and therefore (L-28009.6), holds throughout this complete
range.

The only remaining rows are `j=1`, `j=2`, and

\[
 (n,j)\in\{(6,3),(7,3),(8,3),(8,4)\}.
 \tag{L-28009.21}
\]

## 5. Endpoint neighbor `j=1`

Put

\[
 r=v_2(n),\qquad L=\log n,\qquad \ell=\log2.
\]

The carry row `j=1` selects the divisors of `n`.  Equivalently, (L-28009.8)--
(L-28009.9) give

\[
 P_2(n,1)=L+r\ell,
\]

\[
 S_2(n,1)=L^2+2r\ell L-r\ell^2.
\]

Therefore

\[
 \boxed{
 P_2(n,1)^2-S_2(n,1)=r(r+1)\ell^2\ge0.
 }
 \tag{L-28009.22}
\]

Equality occurs exactly when `n` is odd.

## 6. The complete `j=2` row

Let `e` and `o` be the even and odd members of `{n-1,n}`, and put

\[
 r=v_2(e),\qquad L_e=\log e,
 \qquad L_o=\log o,
 \qquad \ell=\log2.
\]

Direct substitution in the top-half formulas gives

\[
 \boxed{
 \begin{aligned}
 P_2(n,2)^2-S_2(n,2)
 ={}&2L_e(L_o-2\ell)
   +2(r-2)\ell L_o\\
  &+(r^2-3r+6)\ell^2.
 \end{aligned}}
 \tag{L-28009.23}
\]

This is strictly positive.

- If `r=1`, then `o>=5` and the right side factors as
  \[
  2(L_o-2\ell)(L_e-\ell)>0.
  \]
- If `r=2` and `o>=5`, every displayed term is nonnegative and the last is
  positive.  The sole exceptional value `o=3` is `n=4`, where the expression is
  \[
  4\ell(\log3-\ell)>0.
  \]
- If `r>=3`, then `o>=7`, the first two terms are positive, and
  `r^2-3r+6>0`.

Thus every `j=2` row has strict reserve.

## 7. Four finite interior rows

Writing `l_p=log p`, direct use of (L-28009.8)--(L-28009.9) gives

\[
 \begin{aligned}
 R_{6,3}
 &=2l_2(3l_2-2l_3+4l_5)>0,\\
 R_{7,3}
 &=2(l_5l_7-2l_2l_3)>0,\\
 R_{8,3}
 &=4l_2(3l_2-l_3+3l_7)>0,\\
 R_{8,4}
 &=2(2l_2l_5+2l_2l_7+l_5l_7
      -5l_2^2-2l_2l_3)>0,
 \end{aligned}
 \tag{L-28009.24}
\]

where `R_(n,j)=P_2(n,j)^2-S_2(n,j)`.

The signs are elementary:

- `4l_5>2l_3`, so the first bracket is positive;
- `l_5>2l_2` and `l_7>l_3`, proving the second;
- `3l_2>l_3`, proving the third;
- for the fourth, use
  `2l_2l_5>4l_2^2`,
  `2l_2l_7>2l_2l_3`, and
  `l_5l_7>l_2^2`.

This closes all rows and proves (L-28009.6).

## 8. Quantitative balanced reserve

If

\[
 \eta n\le j\le(1-\eta)n,
 \qquad0<\eta\le\frac12,
\]

then

\[
 P_2(n,j)\ge\log\binom nj\ge\eta n\log2.
 \tag{L-28009.25}
\]

Combining this with (L-28009.17) gives

\[
 \boxed{
 S_2(n,j)
 \le {2\log n\over\eta n\log2}\,P_2(n,j)^2.
 }
 \tag{L-28009.26}
\]

Thus for every fixed balanced cone the complete source-matched Selberg forcing
uses only `O_eta(log n/n)` of the generalized-prime Kummer square.  In
particular, for all sufficiently large balanced rows,

\[
 \boxed{
 P_2(n,j)^2-S_2(n,j)
 \ge\frac12P_2(n,j)^2.
 }
 \tag{L-28009.27}
\]

This is an absolute strict reserve for the exact two-contact Dirichlet system.

## 9. Exact null set and source significance

Combining the preceding sections,

\[
 P_2(n,j)^2-S_2(n,j)=0
\]

only for

\[
 j\in\{0,n\},
\]

and for the endpoint-neighbor rows

\[
 j\in\{1,n-1\}
\]

when `n` is odd.  Every other nontrivial row has strict reserve.

The theorem supplies the source-matched inequality which was absent from the
`omega_2` carry route.  It does not yet identify the complete physical block
with a sum of these pointwise rows; that source binding is addressed separately.

## 10. Proof boundary

Closed exactly:

- the top-half representations of the first and second Selberg moments;
- the dyadic-lift pairing;
- nonnegativity of the complete generalized Selberg forcing;
- pointwise domination by the generalized-prime square;
- all endpoint and finite exceptional rows;
- a quantitative balanced reserve tending to one.

Open:

- the complete source-coupled physical/carry localization;
- the lower-scale block recurrence;
- a subpower bottom-charge bound;
- RH.
