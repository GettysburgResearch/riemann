# L-28006 — Explicit two-contact wavelet synthesis and carry reserve

Claim ID: `L-28006`  
Title: The positive dyadic Dirichlet system synthesizes its complete generalized-prime Kummer profile from exact factor-five two-contact wavelets and leaves an explicit interior square  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: `L-28005`; atomized carry/Kummer identity  
Scope: exact carry-space source and Schur algebra; no physical transference

## 1. Scaled two-contact wavelet

Let

\[
 b_2=(\varepsilon-\delta_2)*\mu
\]

and, for integers `1<=m<=n`, define

\[
 \boxed{
 Y_{n,m}(j)
 =\sum_{k\le n/m}b_2(k)\chi_{n,mk}(j).
 }
\tag{L-28006.1}

The divisor-prefix identity

\[
 \sum_{k\le x}b_2(k)\lfloor x/k\rfloor
 =\mathbf1_{x=1}
\]

gives, pointwise,

\[
 \boxed{
 \begin{aligned}
 Y_{n,m}(j)
 ={}&\mathbf1_{m\le n<2m}\\
 &-\mathbf1_{m\le j<2m}
 -\mathbf1_{m\le n-j<2m}.
 \end{aligned}}
\tag{L-28006.2}

This is an exact compact carry wavelet.  Its negative support is confined to the
two child windows, and its parent term is present only in the first quotient
cell.

## 2. Positive inverse synthesis

Let

\[
 a_2(m)=v_2(m)+1>0
\]

be the convolution inverse of `b_2`, and define

\[
 \boxed{
 P_n(j)=\sum_{m\le n}a_2(m)\log m\,Y_{n,m}(j).
 }
\tag{L-28006.3}

Since

\[
 b_2*(a_2\log)=\Lambda_2,
\]

finite convolution and (L-28006.1) give

\[
 \boxed{
 P_n(j)=\sum_{q\le n}\Lambda_2(q)\chi_{n,q}(j).
 }
\tag{L-28006.4}

Every summand on the right is nonnegative.

Using

\[
 \Lambda_2(q)=\Lambda(q)+(\log2)\mathbf1_{q=2^r},
\]

Legendre--Kummer gives the explicit formula

\[
 \boxed{
 P_n(j)
 =\log\binom nj
  +(\log2)\,v_2\!\binom nj
 =\log\left(2^{v_2(\binom nj)}\binom nj\right)
 \ge0.
 }
\tag{L-28006.5}

Thus the signed wavelets in (L-28006.2), when synthesized with the actual
positive inverse coefficients, are exactly a nonnegative generalized-binomial
profile.

## 3. Exact bottom two-contact source

At `m=1`, (L-28006.2) becomes

\[
 \boxed{
 Y_{n,1}(j)
 =-\mathbf1_{j=1}-\mathbf1_{j=n-1}
 }
\tag{L-28006.6}

for `n>=2`, with multiplicity two at `n=2,j=1`.

For `n>=3`,

\[
 {1\over n+1}\sum_{j=0}^{n}Y_{n,1}(j)^2
 ={2\over n+1}.
\tag{L-28006.7}

At the two contacts,

\[
 P_n(1)=P_n(n-1)
 =\log n+(\log2)v_2(n).
\]

Put

\[
 L_2(n)=\log n+(\log2)v_2(n).
\tag{L-28006.8}

Then

\[
 \boxed{
 {1\over n+1}\sum_jY_{n,1}(j)P_n(j)
 =-{2L_2(n)\over n+1}.
 }
\tag{L-28006.9}

## 4. Exact Schur reserve

The orthogonal projection of `P_n` onto the two-contact source is

\[
 -L_2(n)Y_{n,1}.
\]

Since this projection agrees with `P_n` at the two endpoint contacts and
vanishes in the interior,

\[
 \boxed{
 \begin{aligned}
 {1\over n+1}\sum_{j=0}^{n}P_n(j)^2
 ={}&{2L_2(n)^2\over n+1}\\
 &+{1\over n+1}\sum_{j=2}^{n-2}P_n(j)^2.
 \end{aligned}}
\tag{L-28006.10}

The second term is a literal nonnegative interior square and is strictly
positive for every sufficiently large row.  No abstract principal-angle or
compactness argument is needed at carry-space level.

Equivalently, the Schur complement of the two-contact coordinate is exactly

\[
 \boxed{
 {1\over n+1}\sum_{j=2}^{n-2}P_n(j)^2.
 }
\tag{L-28006.11}

## 5. Factor-five localization interface

For fixed `m`, the wavelet in (L-28006.2) is pointwise:

- nonnegative when `m<=n<2m`;
- nonpositive when `2m<=n<4m`;
- a pure child-window difference when `n>=4m`.

The binomial monotonicity argument of PR #269 proves that its potentially
negative logarithmic pairing is exhausted by

\[
 2m\le n<5m.
\]

Equation (L-28006.5) adds only the nonnegative dyadic valuation correction.
Therefore the same factor-five ledger applies to the actual generalized-prime
profile, with the strict reserve (L-28006.11) available in the identical metric.

## 6. Significance

The reflected physical block of `L-28005` and the carry reserve above use the
same arithmetic data:

```text
coefficient law      a_2(n)=v_2(n)+1;
inverse source       b_2=(epsilon-delta_2)*mu;
generalized primes   Lambda_2;
reflected square     |A_2'/A_2|^2;
carry profile        P_n;
bottom source        exact two contacts.
```

The sole missing bridge is a source-bound localization of the physical
independent-frequency block into the wavelet synthesis (L-28006.3), retaining
every quotient-cell and translate cross term.

## 7. Proof boundary

Closed exactly:

- the scaled two-contact wavelet;
- positive inverse synthesis;
- explicit generalized-binomial profile;
- bottom source norm and cross term;
- exact interior Schur square;
- compatibility with the factor-five carry ledger.

Open:

- physical-to-carry transference;
- lower-scale contraction of the transition block;
- RH.
