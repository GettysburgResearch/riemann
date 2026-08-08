# L-28014 — Eta-preconditioned shift factorization and strict Jordan-bank contraction

Claim ID: `L-28014`  
Title: Exact eta preconditioning collapses the shifted central lattice defect to a sparse dyadic derivative operator of norm at most `6/31` on the critical power-log bank  
Status: **PROPOSED COMPLETE EXACT THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28001`; PR #286 `L-28401/L-28402`; elementary binomial-series calculus  
Scope: complete lattice-shift and analytic-boundary factorization; no bound for the reciprocal-eta source itself

## 1. Shifted and unshifted central operators

For a finitely supported sequence `f` on the positive integers define

\[
 (\mathcal U f)(q)
 =\sum_{k\ge1}\bigl[f(2kq)-f((2k+1)q)\bigr],
\tag{L-28014.1}
\]

and

\[
 (\mathcal C f)(q)
 =\sum_{k\ge1}\bigl[f(2kq-1)-f((2k+1)q)\bigr].
\tag{L-28014.2}
\]

All sums are finite.  Their difference is the one-lattice-step endpoint
commutator

\[
 \boxed{
 (\mathcal E f)(q)
 :=(\mathcal C-\mathcal U)f(q)
 =\sum_{k\ge1}\bigl[f(2kq-1)-f(2kq)\bigr].
 }
\tag{L-28014.3}

The unshifted dilation sequence is

\[
 a(1)=0,
 \qquad
 a(n)=(-1)^n\quad(n\ge2),
\]

so its Dirichlet symbol is

\[
 \sum_{n\ge1}{a(n)\over n^s}=1-\eta(s).
\tag{L-28014.4}

Consequently `I-U` has symbol `eta(s)`.

## 2. Reciprocal-eta divisor collapse

Let `b_eta` be the coefficient sequence of `1/eta(s)`.  By `L-28001`, if

\[
 n=2^r m,
 \qquad m\text{ odd},
\]

then

\[
 b_\eta(n)
 =\begin{cases}
   \mu(m),&r=0,\\[1mm]
   2^{r-1}\mu(m),&r\ge1.
  \end{cases}
\tag{L-28014.5}

Let `1` denote the constant-one Dirichlet sequence.  Since

\[
 {\zeta(s)\over\eta(s)}
 ={1\over1-2^{1-s}}
 =\sum_{r\ge0}{2^r\over(2^r)^s},
\]

one has coefficientwise

\[
 \boxed{
 \sum_{d\mid h}b_\eta(d)
 =\begin{cases}
   h,&h\text{ is a power of two},\\
   0,&\text{otherwise}.
  \end{cases}}
\tag{L-28014.6}

This is the exact source cancellation which removes every non-dyadic divisor
from the lattice commutator.

## 3. Sparse preconditioned shift

On finite sequences put

\[
 \mathcal B=(I-\mathcal U)^{-1},
 \qquad
 \mathcal K=\mathcal B\mathcal E.
\tag{L-28014.7}

Expanding `B` with the coefficients (L-28014.5), interchanging finite sums, and
using (L-28014.6) gives

\[
\begin{aligned}
 (\mathcal Kf)(q)
 &=\sum_{d\ge1}b_\eta(d)
   \sum_{k\ge1}
   \bigl[f(2kdq-1)-f(2kdq)\bigr]\\
 &=\sum_{h\ge1}
   \left(\sum_{d\mid h}b_\eta(d)\right)
   \bigl[f(2hq-1)-f(2hq)\bigr].
\end{aligned}
\]

Therefore

\[
 \boxed{
 (\mathcal Kf)(q)
 =\sum_{r\ge0}2^r
  \bigl[f(2^{r+1}q-1)-f(2^{r+1}q)\bigr].
 }
\tag{L-28014.8}

The complete divisor cloud has collapsed to the Mersenne-adjacent dyadic rows.
No estimate or truncation enters this identity.

Since `C=U+E`, equations (L-28014.7)--(L-28014.8) give the exact factorization

\[
 \boxed{
 I-\mathcal C
 =(I-\mathcal U)(I-\mathcal K).
 }
\tag{L-28014.9}

Thus the shifted cascade differs from the reciprocal-eta cascade only through
the sparse operator `K`.

## 4. Dirichlet–Taylor action

Fix

\[
 \tau\ge\frac12.
\]

For `x>1`, the binomial expansion in (L-28014.8) is absolutely convergent and
gives

\[
 \boxed{
 \mathcal K[x^{-\tau}]
 =\sum_{\ell\ge1}k_{\tau,\ell}x^{-\tau-\ell},
 }
\tag{L-28014.10}

where

\[
 \boxed{
 k_{\tau,\ell}
 ={(\tau)_\ell\over\ell!}
  {2^{-\tau-\ell}\over1-2^{1-\tau-\ell}}
 >0.
 }
\tag{L-28014.11}

Indeed, the contribution of one dyadic row `r` is

\[
 2^r(2^{r+1}x)^{-\tau}
 \left[
  \left(1-{1\over2^{r+1}x}\right)^{-\tau}-1
 \right],
\]

and summation in `r` gives the geometric denominator in (L-28014.11).

Since

\[
 x^{-\tau}\log x=-\partial_\tau x^{-\tau},
\]

termwise differentiation gives the complete Jordan companion

\[
 \boxed{
 \mathcal K[x^{-\tau}\log x]
 =\sum_{\ell\ge1}
  \left[
   k_{\tau,\ell}\log x
   -\partial_\tau k_{\tau,\ell}
  \right]
  x^{-\tau-\ell}.
 }
\tag{L-28014.12}

Thus `K` is strictly upper triangular in the power-log basis: every output has
at least one additional inverse power.

## 5. Critical Jordan coefficient space

Put

\[
 R={1\over16}.
\]

For `sigma>=1/2`, let `A_(sigma,R)` consist of the convergent power-log series

\[
 f(x)=\sum_{m\ge0}(u_m+v_m\log x)x^{-\sigma-m}
\tag{L-28014.13}

with norm

\[
 \boxed{
 \|f\|_{\sigma,R}
 =\sum_{m\ge0}R^m\bigl(|u_m|+8|v_m|\bigr).
 }
\tag{L-28014.14}

The series represents an analytic function for `x>R^{-1}`.  Equations
(L-28014.10)--(L-28014.12) define `K` coefficientwise on this space.

For `tau>=1/2`, put

\[
 \kappa_\tau
 =\sum_{\ell\ge1}k_{\tau,\ell}R^\ell,
 \qquad
 D_\tau
 =\sum_{\ell\ge1}|\partial_\tau k_{\tau,\ell}|R^\ell.
\tag{L-28014.15}

We now prove uniform explicit bounds for both rows.

## 6. Exact bound for the positive row

Set

\[
 d=1-{R\over2}={31\over32},
 \qquad
 c={1\over2d}={16\over31},
 \qquad
 t=2^{-\tau}.
\tag{L-28014.16}

Summing first over `ell` in (L-28014.11) gives

\[
 \kappa_\tau
 =\sum_{r\ge0}2^{r-(r+1)\tau}
  \left[
   \left(1-{R\over2^{r+1}}\right)^{-\tau}-1
  \right].
\tag{L-28014.17}

For `0<=z<=R/2`,

\[
 (1-z)^{-\tau}-1
 \le \tau z(1-z)^{-\tau-1}
 \le \tau z d^{-\tau-1}.
\tag{L-28014.18}

Hence

\[
 \kappa_\tau
 \le {\tau R\over2d}
       {c^\tau\over1-t}
 ={\tau c^\tau\over31(1-t)}.
\tag{L-28014.19}

Elementary calculus gives

\[
 \tau c^\tau\le1
 \qquad(\tau\ge1/2),
\]

and

\[
 t\le2^{-1/2}<{3\over4}.
\]

Therefore

\[
 \boxed{
 \kappa_\tau\le{4\over31}.
 }
\tag{L-28014.20}

## 7. Exact bound for the derivative row

For one fixed dyadic index `r`, write

\[
 z_r={R\over2^{r+1}},
 \qquad
 W_r=2^{r-(r+1)\tau}.
\]

The coefficient of degree `ell` before summing in `r` is

\[
 W_r{(\tau)_\ell\over\ell!}z_r^\ell.
\]

Its logarithmic derivative in `tau` is

\[
 \sum_{h=0}^{\ell-1}{1\over\tau+h}-(r+1)\log2.
\]

Taking the absolute value before summing and using the positive generating
series gives

\[
\begin{aligned}
 D_\tau
 \le\sum_{r\ge0}W_r\Bigg\{
 &[-\log(1-z_r)](1-z_r)^{-\tau}\\
 &+(r+1)\log2\big[(1-z_r)^{-\tau}-1\big]
 \Bigg\}.
\end{aligned}
\tag{L-28014.21}

Use

\[
 -\log(1-z)\le{z\over d}
\]

and (L-28014.18).  Since

\[
 \sum_{r\ge0}t^{r+1}={t\over1-t},
 \qquad
 \sum_{r\ge0}(r+1)t^{r+1}={t\over(1-t)^2},
\]

one obtains

\[
 D_\tau
 \le {1\over31}c^\tau
 \left[
  {1\over1-t}
  +{\tau\log2\over(1-t)^2}
 \right].
\tag{L-28014.22}

Now

\[
 {1\over1-t}\le4,
 \qquad
 {1\over(1-t)^2}\le16,
 \qquad
 \log2<{3\over4},
\]

and both `c^tau` and `tau c^tau` are at most one.  Therefore

\[
 \boxed{
 D_\tau\le{16\over31}.
 }
\tag{L-28014.23}

## 8. Strict contraction

For an input monomial without a logarithm, (L-28014.20) is the complete output
row norm.  For a logarithmic input, (L-28014.12) and the weight eight in
(L-28014.14) give the normalized row bound

\[
 \kappa_\tau+{D_\tau\over8}
 \le {4\over31}+{2\over31}
 ={6\over31}.
\]

Summing over all input coefficients yields

\[
 \boxed{
 \|\mathcal Kf\|_{\sigma,R}
 \le {6\over31}\|f\|_{\sigma,R}
 \qquad(\sigma\ge1/2).
 }
\tag{L-28014.24}

Consequently

\[
 \boxed{
 \|(I-\mathcal K)^{-1}\|
 \le{1\over1-6/31}
 ={31\over25}.
 }
\tag{L-28014.25}

The lattice-shift correction is therefore not merely lower order: it is a
uniform strict contraction on the complete critical power-log Jordan bank.

## 9. Resolvent consequence

Combining (L-28014.9) and (L-28014.25),

\[
 \boxed{
 (I-\mathcal C)^{-1}
 =(I-\mathcal K)^{-1}(I-\mathcal U)^{-1}
 =(I-\mathcal K)^{-1}\mathcal B.
 }
\tag{L-28014.26}

Thus every pole or exponential obstruction of the shifted cascade comes from
the reciprocal-eta factor `B`; the lattice shift contributes only the bounded
analytic dressing `(I-K)^(-1)`.

In particular, if

\[
 p=\varepsilon-3\delta_2+2\delta_4,
\]

then `p*b_eta=b_2`, and the solution of

\[
 (I-\mathcal C)r=p
\]

is exactly

\[
 \boxed{
 r=(I-\mathcal K)^{-1}b_2.
 }
\tag{L-28014.27}

The complete shifted boundary cascade is a bounded dressing of the exact
RH-bearing two-contact source.  No additional lattice-stability theorem is
needed.

## 10. Consequences for the live proof graph

This theorem closes, at the stated analytic-bank scope:

1. accumulation of the `2kq-1` shift commutator;
2. every positive-order power/Peano jet exported by finite Euler summation;
3. all faster Taylor channels;
4. the distinction between shifted and unshifted central cascades.

It also proves a sharp status statement:

```text
shifted lattice / cutoff instability     not an independent RH obstruction;
reciprocal eta or filtered b_2 source     the sole surviving analytic channel.
```

The theorem does **not** bound `B` or `b_2`.  Since `1/eta(s)` and
`(1-2^-s)/zeta(s)` retain every off-line zeta pole, such a bound remains
RH-bearing.  No pole has been canceled or estimated away here.

## 11. Proof boundary

Closed exactly:

- reciprocal-eta divisor collapse;
- sparse dyadic formula for the preconditioned shift;
- exact operator factorization;
- exact power and power-log coefficient formulas;
- explicit row bounds `4/31` and `16/31`;
- strict operator contraction `6/31`;
- bounded resolvent dressing and equation (L-28014.27).

Open:

- a subpower bound for the reciprocal-eta/two-contact source;
- the source-convolved reflected Selberg boundary recurrence;
- RH.
