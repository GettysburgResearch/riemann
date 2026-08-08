# L-32405 — The parity pair absorbs the complete pure-dyadic Selberg forcing

Claim ID: `L-32405`  
Title: At every even two-adic level, the parity-projected generalized-prime atom squared dominates the full same-parity Selberg coefficient, including the odd-odd convolution channel  
Status: **PROPOSED COMPLETE EXACT LOCAL-SOURCE LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26202/L-26205`; `L-32404`  
Scope: pure dyadic coefficient block of the paired source; mixed odd-prime/dyadic carry geometry is separate

## 1. Parity decomposition of the generalized-prime sequence

For the Euler-filtered inverse `A_E` of PR #263,

\[
\Lambda_{\mathcal E}^{\#}(2^k)
=\bigl(1+2^k+2^{k/2+1}\bigr)\log2
=\boxed{(2^{k/2}+1)^2\log2.}
\tag{L-32405.1}
\]

Split this local sequence by the parity of the two-adic exponent. For `r>=1` put

\[
A_r=(2^r+1)^2,
\qquad
B_r=(2^{r-1/2}+1)^2.
\tag{L-32405.2}
\]

Thus

\[
\Lambda_{\rm ev}(2^{2r})=A_r\log2,
\qquad
\Lambda_{\rm odd}(2^{2r-1})=B_r\log2.
\tag{L-32405.3}
\]

PR #263's parity sum keeps only even `v_2` in the Selberg forcing. Since

\[
C=-\Lambda'+\Lambda*\Lambda,
\]

the pure-dyadic coefficient retained at `2^(2r)` is

\[
\boxed{
{C_{\rm ev}(2^{2r})\over(\log2)^2}
=2rA_r
+\sum_{i=1}^{r-1}A_iA_{r-i}
+\sum_{i=1}^{r}B_iB_{r-i+1}.}
\tag{L-32405.4}
\]

The final sum is exactly the odd-odd parity convolution. It is the channel which survives in the forcing even though the individual odd generalized-prime atoms cancel from the parity sum.

## 2. Claim

For every `r>=1`,

\[
\boxed{
C_{\rm ev}(2^{2r})
\le
\Lambda_{\rm ev}(2^{2r})^2.}
\tag{L-32405.5}
\]

Equivalently,

\[
\boxed{
2rA_r
+\sum_{i=1}^{r-1}A_iA_{r-i}
+\sum_{i=1}^{r}B_iB_{r-i+1}
\le A_r^2.}
\tag{L-32405.6}
\]

## 3. Exact small levels

Write `s=sqrt(2)`.

For `r=1`,

\[
C_1=35+12s,
\qquad
A_1^2=81,
\]

so the reserve is

\[
46-12s>0.
\tag{L-32405.7}
\]

For `r=2`,

\[
C_2=267+60s,
\qquad
A_2^2=625,
\]

with reserve

\[
358-60s>0.
\tag{L-32405.8}
\]

For `r=3`,

\[
C_3=1311+252s,
\qquad
A_3^2=6561,
\]

with reserve

\[
5250-252s>0.
\tag{L-32405.9}
\]

Each positivity is immediate after squaring positive rational sides; for example `46^2>2*12^2`.

## 4. Uniform estimate for every higher level

Assume `r>=4` and put

\[
x=2^r\ge16.
\]

Then

\[
A_r=(x+1)^2
\le\left({17\over16}x\right)^2,
\]

so

\[
2rA_r<3rx^2.
\tag{L-32405.10}
\]

For `1<=i<=r-1`,

\[
\sqrt{A_iA_{r-i}}
=(2^i+1)(2^{r-i}+1)
=x+2^i+2^{r-i}+1.
\]

The maximum of `2^i+2^(r-i)` on that interval occurs at an endpoint. Hence

\[
\sqrt{A_iA_{r-i}}
\le x+{x\over2}+3<2x,
\]

and therefore

\[
\sum_{i=1}^{r-1}A_iA_{r-i}<4rx^2.
\tag{L-32405.11}
\]

Likewise

\[
\sqrt{B_iB_{r-i+1}}
=(2^{i-1/2}+1)(2^{r-i+1/2}+1)
=x+2^{i-1/2}+2^{r-i+1/2}+1.
\]

Again the maximum is at an endpoint, where

\[
2^{i-1/2}+2^{r-i+1/2}
\le {x\over\sqrt2}+\sqrt2.
\]

For `x>=16` this is less than `x`; hence the whole displayed square root is less than `2x`, and

\[
\sum_{i=1}^{r}B_iB_{r-i+1}<4rx^2.
\tag{L-32405.12}
\]

Combining (L-32405.10)--(L-32405.12),

\[
C_r<11r x^2.
\tag{L-32405.13}
\]

For every `r>=4`,

\[
11r\le4^r=x^2.
\]

The case `r=4` is `44<=256`, and the inequality then propagates because multiplication of the right side by four dominates the factor `(r+1)/r<2` on the left. Thus

\[
C_r\le x^4\le(x+1)^4=A_r^2,
\]

which proves (L-32405.6).

## 5. Meaning for the exact generalized-source mutation

The single-channel generalized Kummer inequality is false; PR #297 records the exact `(n,j)=(6,2)` mutation. Its defect is created by a mixed source term with odd two-adic valuation.

The parity pair changes the algebra before a sign is taken:

- odd-`v_2` forcing coefficients cancel in `C_++C_-`;
- odd generalized-prime atoms remain available quadratically through the paired energy;
- their odd-odd convolution lands in the even forcing channel.

Equation (L-32405.5) proves that **at every pure dyadic destination** this entire surviving odd-odd forcing is already paid by the corresponding even-parity generalized-prime square.

So the exact `(6,2)` failure is not a pure-dyadic obstruction to the paired source.

## 6. Remaining mixed block

The full paired carry inequality would also contain destinations

\[
2^{2r}m,
\qquad m>1\text{ odd},
\]

created by convolution between the odd-prime generalized-prime sequence and the even dyadic sequence. Equation (L-32405.5) does not sign those mixed carry rows.

A complete paired Kummer theorem must retain the ordinary odd-prime Kummer reserve and prove that the mixed even-dyadic cross terms are absorbed jointly before any rowwise absolute value. That is the next exact algebraic problem.

## 7. Proof boundary

Closed exactly:

- the parity-local generalized-prime weights;
- the complete even-parity pure-dyadic forcing coefficient;
- all-level domination by the corresponding generalized-prime square.

Open:

- the mixed odd-prime/dyadic paired Kummer inequality;
- source-complete physical reflected contraction;
- RH.