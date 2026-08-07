# L-15115 — The universal Finsler slope is a Loewner residue form, with an exact root-node parity count

Claim ID: `L-15115`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15107`, `L-15114`  
Scope: simple real target roots and the geometry of the scalar threshold directions  
Related counterexample candidates: none

## 1. Setup

Let

\[
 \lambda_1<\cdots<\lambda_n
\]

be distinct real nodes, let every `p_i` be nonzero, and normalize

\[
 \sum_i p_i=1.
\]

Define

\[
 \Omega(s)=\prod_{i=1}^n(\lambda_i-s),
 \qquad
 P(s)=\sum_i p_i\frac{\Omega(s)}{\lambda_i-s}.
 \tag{L-15115.1}
\]

Assume that `P` has `n-1` simple real roots

\[
 r_1<\cdots<r_{n-1}.
\]

The universal slope of the target-pinned pencil is

\[
 B_p=\operatorname{diag}(1/p_i)-\eta\eta^{\mathsf T},
 \qquad
 \eta=(1,\ldots,1)^{\mathsf T}.
 \tag{L-15115.2}
\]

## 2. Loewner identity for the slope

Put

\[
 q(s)=s+\frac{\Omega(s)}{P(s)}.
 \tag{L-15115.3}
\]

Then

\[
 \boxed{B_p=-L(q),}
 \tag{L-15115.4}
\]

where `L(q)` is the confluent Loewner matrix at the nodes.

### Proof

At a node, `Omega(lambda_i)=0`, so

\[
 q(\lambda_i)=\lambda_i.
\]

Thus every off-diagonal entry of `-L(q)` equals `-1`, which is the off-diagonal entry of `B_p`.

For the diagonal, differentiate:

\[
 q'(s)=1+\frac{\Omega'(s)P(s)-\Omega(s)P'(s)}{P(s)^2}.
\]

At `s=lambda_i`,

\[
 \Omega'(\lambda_i)
 =-\frac{P(\lambda_i)}{p_i},
\]

so

\[
 -q'(\lambda_i)
 =\frac1{p_i}-1=(B_p)_{ii}.
\]

This proves (L-15115.4) entrywise. QED.

## 3. Root-residue diagonalization

At a root `r_k`, the rational function `q` has residue

\[
 \frac{\Omega(r_k)}{P'(r_k)}
\]

in the `(s-r_k)^{-1}` convention. Therefore (L-15115.4) and the divided-difference calculation give

\[
 \boxed{
 B_p
 =\sum_{k=1}^{n-1}v_k\ell_k\ell_k^{\mathsf T},
 \qquad
 v_k=\frac{\Omega(r_k)}{P'(r_k)},
 \qquad
 \ell_k(i)=\frac1{\lambda_i-r_k}.}
 \tag{L-15115.5}
\]

The Cauchy vectors are independent. Hence

\[
 \operatorname{Inertia}(B_p)
 =\left(
   \#\{k:v_k>0\},
   \#\{k:v_k<0\},
   1
  \right).
 \tag{L-15115.6}
\]

On the other hand, `L-15107` gives

\[
 \operatorname{Inertia}(B_p)=(n_+-1,n_-,1),
 \tag{L-15115.7}
\]

where

\[
 n_+=\#\{i:p_i>0\},
 \qquad
 n_-=\#\{i:p_i<0\}.
\]

Consequently

\[
 \boxed{
 \#\left\{k:\frac{\Omega(r_k)}{P'(r_k)}>0\right\}=n_+-1,
 \qquad
 \#\left\{k:\frac{\Omega(r_k)}{P'(r_k)}<0\right\}=n_-.}
 \tag{L-15115.8}
\]

This is the root-coordinate form of the universal-slope inertia theorem.

## 4. Exact root-node parity identity

For each root `r_k`, let

\[
 j_k=\#\{i:\lambda_i<r_k\}
 \in\{0,1,\ldots,n\}.
 \tag{L-15115.9}
\]

Because

\[
 \operatorname{sign}\Omega(r_k)=(-1)^{j_k},
\]

and `P` has leading coefficient `(-1)^(n-1)`, one has

\[
 \operatorname{sign}P'(r_k)=(-1)^k.
\]

Therefore

\[
 \boxed{
 \operatorname{sign}v_k=(-1)^{j_k-k}.}
 \tag{L-15115.10}
\]

Combining with (L-15115.8) yields the exact global parity count

\[
 \boxed{
 \#\{k:j_k-k\text{ is odd}\}=n_-,
 \qquad
 \#\{k:j_k-k\text{ is even}\}=n_+-1.}
 \tag{L-15115.11}
\]

This is a correct replacement for the false gap-parity converse. It allows roots on outer rays and multiple roots in one node gap, but constrains the total parity defect of their ordered locations.

### Example

For the counterexample

\[
 \lambda=(-1,0,1),
 \qquad
 p=(-1,3,-1),
 \qquad
 r=(-\sqrt3,\sqrt3),
\]

one has

\[
 j_1=0,
 \qquad
 j_2=3.
\]

Thus both `j_k-k` are odd, matching `n_-=2`. The identity explains exactly how two outer-ray roots coexist with zero same-sign interior gaps.

## 5. Threshold orientation

The arithmetic residue line of `L-15114` is

\[
 w_k(c)=w_k(0)+cv_k.
 \tag{L-15115.12}
\]

Thus the roots with `j_k-k` even supply lower bounds on `c`, while those with `j_k-k` odd supply upper bounds, up to the sign convention in `w_k(0)`:

\[
 v_k>0\Rightarrow c>-w_k(0)/v_k,
 \qquad
 v_k<0\Rightarrow c<-w_k(0)/v_k.
 \tag{L-15115.13}
\]

The number of lower and upper threshold families is determined exactly by the sign count of the target coefficients:

\[
 \boxed{
 \#\{\text{positive-slope thresholds}\}=n_+-1,
 \qquad
 \#\{\text{negative-slope thresholds}\}=n_-.}
 \tag{L-15115.14}
\]

This identifies which target-root locations can control each endpoint of the Finsler interval without computing the slope matrix inertia separately.

## 6. Relationship to gap parity

Gap parity is a local endpoint-sign lower bound. Equation (L-15115.11) is a global identity valid after all roots are known to be simple and real.

Neither implies the false statement that every root not locally forced is nonreal. Instead:

- gap parity gives mandatory roots in certain gaps;
- the universal-slope identity counts the total parity mismatch of all root locations, including outer rays;
- the arithmetic source values determine whether the lower and upper threshold families overlap.

These are three distinct layers and should not be conflated.

## 7. Gap audit

1. The theorem assumes every target root is simple and real.
2. `j_k` counts roots relative to nodes, not zeros of the limiting `Xi` function.
3. The parity identity constrains a count, not individual locations.
4. It does not prove scalar feasibility; it only orients the affine residue slopes.
5. For symmetric targets, the identities can be paired further under `r -> -r`, but no extra conclusion is used here.