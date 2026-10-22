# L-23824 — Zero-cost weighted prime-tail transport

Claim ID: `L-23824`  
Title: Weighted upper-tail domination of a signed prime residual gives an exact feasible carry correction at zero objective cost; one scalar tail charge handles the general case  
Status: **PROPOSED COMPLETE FINITE TRANSPORT THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: PR #248 `L-24508`, `L-24520`; exact finite transport algebra  
Scope: signed ordinary-prime carry constraints; proper prime powers are restored separately at `O(log^2 X)` cost

## 1. Ordered prime residual

Let

\[
2\le p_1<p_2<\cdots<p_m
\tag{L-23824.1}
\]

be ordinary primes, put

\[
x_i=\log p_i>0,
\]

and let

\[
r=(r_1,\ldots,r_m)\in\mathbb R^m
\tag{L-23824.2}
\]

be a signed constraint residual. Positive `r_i` is a violated prime constraint;
negative `r_i` is available slack.

Define the logarithmically weighted residual masses

\[
\mu_i=x_i r_i
\tag{L-23824.3}
\]

and their upper tails

\[
\boxed{
R_j=\sum_{i=j}^m\mu_i.}
\tag{L-23824.4}
\]

## 2. Weighted tail domination

Assume

\[
\boxed{
R_j\le0
\qquad(1\le j\le m).}
\tag{L-23824.5}
\]

Then every positive weighted atom can be matched to negative weighted mass at
a strictly larger prime.

A constructive proof is obtained by scanning the primes from right to left.
Keep a queue of unused negative weighted capacities. When `mu_i>0`, condition
(L-23824.5) says the total unused negative capacity to the right is at least
`mu_i`; split `mu_i` among those capacities. Thus there are numbers

\[
\alpha_{ij}\ge0,
\qquad i<j,
\tag{L-23824.6}
\]

such that

\[
\sum_{j>i}\alpha_{ij}=(\mu_i)_+,
\qquad
\sum_{i<j}\alpha_{ij}\le(-\mu_j)_+.
\tag{L-23824.7}
\]

No analytic estimate enters this coupling.

## 3. One weighted transfer has zero objective cost

Fix `i<j` and one weighted amount `alpha=alpha_(ij)`. Put

\[
t=\frac\alpha{x_i},
\qquad
u=\alpha\left(\frac1{x_i}-\frac1{x_j}\right)\ge0.
\tag{L-23824.8}
\]

### 3.1 Prime-to-prime incidence block

The exact constant carry block of `L-24520`, taken with the sign which transports
residual upward, changes the two prime rows by

\[
\Delta r_i=-t,
\qquad
\Delta r_j=+t,
\tag{L-23824.9}
\]

and changes no other prime row. Its objective change is

\[
\Delta J_1=t(x_j-x_i)
=\alpha\left(\frac{x_j}{x_i}-1\right).
\tag{L-23824.10}
\]

### 3.2 Single-prime endpoint block

Use the exact block from endpoint `1` to `p_j` to reduce the destination by
`nu`:

\[
\Delta r_j=-\nu.
\tag{L-23824.11}
\]

Its objective change is

\[
\Delta J_2=-\nu x_j
=-\alpha\left(\frac{x_j}{x_i}-1\right).
\tag{L-23824.12}
\]

Combining the two blocks gives

\[
\boxed{
\Delta r_i=-\frac\alpha{x_i},
\qquad
\Delta r_j=+\frac\alpha{x_j},}
\tag{L-23824.13}
\]

so the weighted residual changes by

\[
\Delta\mu_i=-\alpha,
\qquad
\Delta\mu_j=+\alpha.
\tag{L-23824.14}
\]

Most importantly,

\[
\boxed{\Delta J_1+\Delta J_2=0.}
\tag{L-23824.15}
\]

Thus logarithmically weighted mass can be transported to a larger prime at
exactly zero prime objective cost. The raw residual amount is allowed to change;
this is what removes the density mismatch between prime locations.

Because both endpoints are ordinary primes, no third ordinary-prime or proper
prime-power row is altered by these two incidence blocks.

## 4. Exact zero-cost feasibility theorem

Apply (L-23824.13) for every coupling amount in (L-23824.6). Every positive
weighted residual is removed and every destination stays within its available
negative weighted capacity. Therefore the corrected residual `r^new` satisfies

\[
\boxed{
r_i^{\rm new}\le0
\qquad(1\le i\le m),}
\tag{L-23824.16}
\]

while

\[
\boxed{
J_{\mathbb P}(b^{\rm new})=J_{\mathbb P}(b).}
\tag{L-23824.17}
\]

No sign condition on the physical carry coordinate is required by the signed
consumer `L-24508`.

Consequently, a weighted upper-tail theorem is already a proof-producing carry
certificate, not merely a distributional analogy.

## 5. General residual and the least top boundary charge

For arbitrary `r`, define

\[
\boxed{
\mathcal B(r)
=\max_{1\le j\le m}(R_j)_+.}
\tag{L-23824.18}
\]

Choose one additional prime `P>p_m` and append the residual

\[
r_P=-\frac{\mathcal B(r)}{\log P}.
\tag{L-23824.19}
\]

Every weighted upper tail of the augmented vector is nonpositive:

\[
R_j-\mathcal B(r)\le0,
\qquad
-\mathcal B(r)\le0.
\]

Section 4 then makes all old and new prime residuals nonpositive at zero
additional transport cost.

The negative boundary residual (L-23824.19) is created by one endpoint block at
objective cost exactly `mathcal B(r)`. Hence

\[
\boxed{
\text{there is an exact signed feasible correction with objective loss }
\le\mathcal B(r).}
\tag{L-23824.20}
\]

Within the class consisting of zero-cost weighted transports plus one top
boundary atom, this charge is minimal: any boundary atom must reduce every
upper tail by at least the maximum in (L-23824.18).

This is the weighted Skorokhod reflection of the finite prime residual.

## 6. Fixed-ratio shell charge

For two endpoints `Y<X`, let

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p)
\tag{L-23824.21}
\]

be the ordinary-prime residual of the parabolic seed and define the shell
residual

\[
\boxed{
s_{X,Y}(p)
=r_X(p)-\mathbf1_{p\le Y}r_Y(p).}
\tag{L-23824.22}
\]

Its exact weighted shell-tail charge is

\[
\boxed{
\mathcal B_{X,Y}
=\max_{z}
\left(
\sum_{z\le p\le X}(\log p)s_{X,Y}(p)
\right)_+,}
\tag{L-23824.23}
\]

where the maximum runs over the finite prime set and the empty tail.

Equation (L-23824.20) gives a signed feasible correction of the complete shell
with objective loss at most `mathcal B_(X,Y)`.

This is the exact finite arithmetic counterpart of the continuum shell order in
`L-23823`. The continuum theorem says the main measure has no positive upper
tail; `mathcal B_(X,Y)` records only the finite prime-sampling and floor
remainder that must still be controlled.

## 7. Mutation resistance

- The theorem accepts arbitrarily high source rank and arbitrary sign patterns.
- It requires no reflected reserve.
- Positive and negative residuals are coupled before taking a positive part.
- The logarithmic prime objective is preserved exactly, so the first-cell
  Mertens mode is not erased by an unweighted transport.
- A nonnegative monotone cover is never formed.

## 8. Proof boundary

Closed exactly:

1. weighted monotone coupling under upper-tail domination;
2. exact zero-cost implementation by carry incidence blocks;
3. a finite feasible signed correction;
4. the least one-boundary weighted charge;
5. the fixed-ratio shell-charge interface.

Open:

1. a subpolynomial bound for the actual shell charges `mathcal B_(X,Y)` on a
   cofinal scale chain;
2. the prime-ramp estimate;
3. RH.
