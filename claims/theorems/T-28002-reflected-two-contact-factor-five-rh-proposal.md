# T-28002 — Reflected two-contact factor-five proposal for RH

Claim ID: `T-28002`  
Title: Localizing the reflected Selberg identity for the positive dyadic generalized-prime system to its exact two-contact carry block would prove RH  
Status: **FULL CONDITIONAL PROPOSAL — ONE PHYSICAL TRANSFERENCE THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Cross-route inputs: PRs #226, #241, #247, #269; `L-28005`  
Scope: source-specific global composition; RH is not claimed proved

## 1. Dirichlet system

Let

\[
 A_2(s)={\zeta(s)\over1-2^{-s}}
 =\sum_{n\ge1}a_2(n)n^{-s},
 \qquad
 a_2(n)=v_2(n)+1>0.
\]

Its inverse is

\[
 B_2(s)={1-2^{-s}\over\zeta(s)}
 =\sum_{n\ge1}b_2(n)n^{-s},
\]

where

\[
 b_2=(\varepsilon-\delta_2)*\mu.
\]

The generalized von Mangoldt coefficients are

\[
 \Lambda_2(n)
 =\Lambda(n)+(\log2)\mathbf1_{n=2^r}
 \ge0.
\]

Every zero of `zeta` in the open critical strip remains an uncancelled pole of
`B_2` and of `-A_2'/A_2`.

## 2. Exact source properties

The same source has four exact structures.

### 2.1 Two-contact carry collapse

For every binomial parent and split,

\[
 \sum_{q=2}^{n}b_2(q)\chi_{n,q}(j)
 =-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
\tag{T-28002.1}

### 2.2 Positive inverse and generalized primes

Every `a_2(n)` and every `Lambda_2(n)` is nonnegative.

### 2.3 Reflected Hermitian square

The generalized reflected Selberg identity gives, with independent frequencies,

\[
 C_2(\sigma;t,-u)-C_2(\sigma;t)-C_2(\sigma;-u)
 =2L_2(\sigma+it)L_2(\sigma-iu),
\]

and on the diagonal

\[
 2|L_2(\sigma+it)|^2,
 \qquad L_2=-A_2'/A_2.
\tag{T-28002.2}

### 2.4 Factor-five carry localization

The exact dyadic wavelet analysis of PR #269 shows that the potentially negative
logarithmic Kummer rows are confined to

\[
 2m\le n<5m,
\]

while the actual generalized-prime carry profile has a uniform strict Schur
reserve after a finite boundary.

## 3. Sole theorem — RTCT

The **Reflected Two-Contact Transference theorem**, abbreviated `RTCT`, is the
following finite production statement.

For an unbounded sequence of compact safe-window orders `K` and every
sufficiently large logarithmic support block, construct one source-bound map

\[
 \mathcal J_K:
 \mathcal H_{\rm phys,K}
 \longrightarrow
 \mathcal H_{\rm carry,K}
\]

with these properties:

1. `mathcal H_phys,K` is the complete independent-frequency reflected normal
   block for `A_2`, including every translate cross term;
2. `mathcal H_carry,K` is the complete generalized-prime carry block generated
   by the two-contact wavelet;
3. all quotient cells `2m<=n<5m` and every finite boundary row are present;
4. the exact product-six and fixed-ratio Mertens mutations are present;
5. the physical source coefficients are the actual `b_2,a_2,Lambda_2` data;
6. the map intertwines the source rows exactly;
7. the physical Gram dominates the pullback carry Gram up to a remainder
   `E_K`:
   \[
   G_{\rm phys,K}
   \succeq
   \mathcal J_K^*G_{\rm carry,K}\mathcal J_K-E_K;
   \]
8. the strict carry Schur reserve survives with one absolute constant;
9. every current-scale remainder with a free macroscopic variable is closed by
   high-order Euler cancellation;
10. all remaining rows enter a strict lower logarithmic scale;
11. the complete remainder exponent `epsilon_K` tends to zero.

The theorem must be source-specific.  A generic bounded operator between two
finite spaces is not an `RTCT` certificate.

## 4. Conditional contraction

Under `RTCT`, the carry-space factor-five theorem and its strict Schur reserve
bound the complete physical transition block by

\[
 \boxed{
 \mathcal E_K(J)
 \le
 \exp[(\epsilon_K+o_K(1))J]
 \left[
  1+\max_{u\le(1-\delta)J+O_K(1)}
   \mathcal E_K(u)
 \right],
 }
\tag{T-28002.3}

for one fixed `delta>0`.

Scale iteration and `epsilon_K->0` give subexponential energy for the complete
`b_2` source.

## 5. Scalar consumer

Define

\[
 \mathcal R_2(X)
 =\sum_{n\le X}{b_2(n)\over\sqrt n}\log{X\over n}.
\tag{T-28002.4}

The established shell/Riesz consumer gives

\[
 \mathcal R_2(X)=X^{o(1)}.
\]

Its Mellin transform is

\[
 \int_1^\infty\mathcal R_2(X)X^{-z-1}dX
 ={(1-2^{-z-1/2})/\zeta(z+1/2)-1\over z^2}.
\tag{T-28002.5}

The numerator factor cannot cancel a zero with `Re(z)>0`.  Hence the subpower
bound excludes every zeta zero to the right of the critical line; functional
equation symmetry gives RH.

## 6. Why this route is narrower than generic BTP

The source is fixed and completely explicit:

```text
inverse source            b_2=(epsilon-delta_2)*mu;
positive coefficient law  a_2(n)=v_2(n)+1;
generalized primes         Lambda + one positive dyadic copy;
carry image                two endpoint contacts;
negative transition cells  only 2,3,4;
physical square            exact reflected modulus square.
```

The missing theorem is the exact localization/congruence of one Dirichlet
system, not an arbitrary balanced packet norm.

## 7. Automatic rejection tests

Reject a proposed `RTCT` proof if it:

1. uses one vertical frequency instead of independent frequencies;
2. omits any translate cross term;
3. changes `a_2`, `b_2`, or `Lambda_2` between the physical and carry sides;
4. applies the carry reserve without an exact source intertwiner;
5. omits any row in `2m<=n<5m`;
6. treats `4m<=n<5m` as automatically positive;
7. takes absolute values before dyadic recombination;
8. omits the bottom two-contact charge;
9. lacks a strict lower-scale destination;
10. fails the fixed-ratio Mertens mutation.

## 8. Exact status

```text
positive generalized-prime Dirichlet system   proposed exact
finite eta-to-two-contact filter               proposed exact
two-contact carry collapse                     proposed exact
reflected Hermitian identity                   proposed exact
factor-five carry localization/reserve         imported proposed exact
RTCT physical-to-carry transference            OPEN / RH-BEARING
RTCT -> subpower b_2 source -> RH               complete conditional chain
Riemann Hypothesis                              UNPROVED
```
