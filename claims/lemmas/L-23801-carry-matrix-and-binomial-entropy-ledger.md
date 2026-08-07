# L-23801 — Exact carry matrix and binomial-entropy ledger

Claim ID: `L-23801`  
Title: Average prime-power carries in one binomial row give an exact nonnegative matrix factorization of the logarithmic prime ramp  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-07  
Issue: #238  
Scope: finite algebra; no asymptotic carry theorem

## 1. Carry matrix

For integers

\[
2\le q\le n,
\]

write

\[
n=kq+r,\qquad 0\le r<q,
\]

and define

\[
\boxed{
\beta_{nq}
=\frac{k(q-1-r)}{n+1}
=\frac{\lfloor n/q\rfloor\,[q-1-(n\bmod q)]}{n+1}.}
\tag{L-23801.1}
\]

Put `beta_(nq)=0` for `q>n`. Every entry is nonnegative and

\[
\beta_{nn}=\frac{n-1}{n+1}>0.
\tag{L-23801.2}
\]

The useful floor-sum form is

\[
\boxed{
\beta_{nq}
=\left\lfloor\frac nq\right\rfloor
 -\frac2{n+1}\sum_{j=0}^{n}
  \left\lfloor\frac jq\right\rfloor.}
\tag{L-23801.3}
\]

Indeed

\[
\sum_{j=0}^{n}\left\lfloor\frac jq\right\rfloor
=\frac{qk(k-1)}2+k(r+1),
\]

and substitution gives (L-23801.1).

## 2. Exact average carry identity

Define

\[
G_n=\frac1{n+1}\sum_{j=0}^{n}\log\binom nj.
\tag{L-23801.4}
\]

For a prime `p`, Legendre's formula gives

\[
v_p\binom nj
=\sum_{a\ge1}
 \left(
  \left\lfloor\frac n{p^a}\right\rfloor
 -\left\lfloor\frac j{p^a}\right\rfloor
 -\left\lfloor\frac{n-j}{p^a}\right\rfloor
 \right).
\]

Averaging in `j`, using symmetry of `j` and `n-j`, and then (L-23801.3), yields

\[
\frac1{n+1}\sum_{j=0}^{n}v_p\binom nj
=\sum_{a\ge1}\beta_{n,p^a}.
\tag{L-23801.5}
\]

Therefore

\[
\boxed{
G_n
=\sum_{p^a\le n}\Lambda(p^a)\beta_{n,p^a}.}
\tag{L-23801.6}
\]

This is an exact finite factorization. No prime-number theorem enters.

## 3. Entropy bounds

For `0<=x<=1`, let

\[
H(x)=-x\log x-(1-x)\log(1-x).
\]

The elementary type bounds give

\[
nH(j/n)-\log(n+1)-2
\le\log\binom nj
\le nH(j/n).
\tag{L-23801.7}
\]

Composite trapezoidal comparison for the concave function `H`, together with
`integral_0^1 H(x)dx=1/2`, gives the review-safe estimates

\[
\boxed{
\frac n2-C\log(n+1)
\le G_n\le\frac n2}
\tag{L-23801.8}
\]

for one absolute constant `C`. The weaker explicit lower bound

\[
G_n\ge\frac n2-\log(n+1)-3
\tag{L-23801.9}
\]

is sufficient for the proposal.

The upper inequality in (L-23801.8) is load bearing for a nonnegative carry
**cover**, while the lower inequality is load bearing for a nonnegative carry
**packing**.

## 4. Prime ramp

For an integer endpoint `X>=2`, put

\[
w_X(q)=q^{-1/2}\log(X/q),\qquad 2\le q\le X,
\tag{L-23801.10}
\]

and define the complete prime-power ramp

\[
\boxed{
\mathcal P(X)
=\sum_{q=p^a\le X}\Lambda(q)w_X(q).}
\tag{L-23801.11}
\]

If a real vector `d=(d_2,...,d_X)` satisfies

\[
d_n\ge0,
\qquad
\sum_{n=q}^{X}d_n\beta_{nq}\le w_X(q)
\quad(2\le q\le X),
\tag{L-23801.12}
\]

then (L-23801.6) and `Lambda>=0` give

\[
\boxed{
\sum_{n=2}^{X}d_nG_n\le\mathcal P(X).}
\tag{L-23801.13}
\]

If instead `e_n>=0` and

\[
\sum_{n=q}^{X}e_n\beta_{nq}\ge w_X(q)
\quad(2\le q\le X),
\tag{L-23801.14}
\]

then

\[
\boxed{
\mathcal P(X)\le\sum_{n=2}^{X}e_nG_n.}
\tag{L-23801.15}
\]

Thus a two-sided nonnegative carry sandwich gives a prime-ramp estimate with no
Möbius sign on the final inequality.

## 5. Proof boundary

Closed exactly:

- the carry matrix;
- the average Legendre/Kummer factorization;
- the entropy row bounds;
- the packing and covering implications.

Open:

- a sharp nonnegative carry packing/covering sandwich;
- the cofinal prime-ramp estimate;
- RH.