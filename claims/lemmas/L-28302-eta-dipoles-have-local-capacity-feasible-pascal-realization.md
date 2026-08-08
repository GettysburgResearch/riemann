# L-28302 — Eta dipoles have a local capacity-feasible Pascal realization

Claim ID: `L-28302`  
Title: Every finite eta boundary pair splits into positive residual mass and an admissible central-to-sibling switch with the exact logarithmic objective cost  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Dependencies: `L-28301`; PR #290 `L-28302` sibling-switch identity  
Scope: one-generation source/Pascal dictionary; no all-generation debt estimate

## 1. Finite eta source

For an integer cutoff `K>=1`, put

\[
 a_k={1\over2k},
 \qquad
 c_k={1\over2k+1},
 \tag{L-28302.1}
\]

and define the finite source

\[
 \mathfrak b_K
 =\sum_{k=1}^{K}
 \left[a_k e_{2k}-c_k e_{2k+1}\right],
 \tag{L-28302.2}
\]

where `e_h` is a formal unit divisor-source atom at the half-scale node `h`.

The exact decomposition is

\[
 \boxed{
 \mathfrak b_K
 =\sum_{k=1}^{K}(a_k-c_k)e_{2k}
 +\sum_{k=1}^{K}c_k(e_{2k}-e_{2k+1}).
 }
 \tag{L-28302.3}
\]

Every residual coefficient is positive and

\[
 0<c_k<a_k.
 \tag{L-28302.4}
\]

## 2. Exact sibling-switch image

At the even parent `4k`, compare the central split

\[
 [2k+2k]
\]

with the nearest sibling split

\[
 [(2k-1)+(2k+1)].
\]

For every carry base `q`, direct floor subtraction gives

\[
 \boxed{
 \chi_{4k,2k-1}(q)-\chi_{4k,2k}(q)
 =\mathbf1_{q\mid2k}-\mathbf1_{q\mid2k+1}.
 }
 \tag{L-28302.5}
\]

Thus the divisor transform of the source dipole

\[
 e_{2k}-e_{2k+1}
\]

is exactly the carry change of one central-to-sibling switch.

The matching entropy and von-Mangoldt objective change is

\[
 \boxed{
 \log{\binom{4k}{2k-1}\over\binom{4k}{2k}}
 =\log{2k\over2k+1}.
 }
 \tag{L-28302.6}
\]

Therefore a switch of amount `c_k` has exact negative objective cost

\[
 -c_k\log{2k+1\over2k}.
 \tag{L-28302.7}
\]

## 3. Local capacity feasibility

Interpret the positive source coefficient `a_k` as the available central amount
at the corresponding event.  Because `c_k<a_k`, the switch of amount `c_k` is
locally admissible and leaves the nonnegative central residual

\[
 a_k-c_k={1\over2k(2k+1)}.
 \tag{L-28302.8}
\]

No cumulative inversion or signed edge amount is needed at one generation.
The complete finite dictionary is

```text
even source a_k at node 2k
    -> sibling switch c_k at parent 4k
    + residual source a_k-c_k at node 2k.
```

The total residual mass and objective cost are

\[
 \rho_K=\sum_{k=1}^{K}(a_k-c_k),
 \tag{L-28302.9}
\]

\[
 \mathfrak c_K
 =\sum_{k=1}^{K}c_k\log{2k+1\over2k}.
 \tag{L-28302.10}
\]

Termwise,

\[
 c_k\log{2k+1\over2k}
 <a_k-c_k.
 \tag{L-28302.11}
\]

Hence

\[
 \boxed{
 \rho_K+\mathfrak c_K<2\rho_K<1
 }
 \tag{L-28302.12}
\]

for every finite `K`, and passage to the limit recovers `L-28301`.

## 4. Positive input measures

Let `mu` be any finite nonnegative source measure.  Tensoring (L-28302.3) with
`mu` gives a positive residual source and a nonnegative family of sibling-switch
amounts.  The source mass is multiplied by `rho_K`; the exact logarithmic
objective paid by the switch family is at most `c_K mu(total)`.

Thus the eta boundary transition is capacity-feasible **before** taking a norm
whenever the incoming state is represented by nonnegative central source mass.
This is the finite state augmentation missing from a scalar convolution factor.

## 5. What remains

The lemma closes the local event dictionary but not the global cascade.  A full
BJPR proof must additionally show:

1. every endpoint/Peano jet enters this nonnegative central source cone;
2. repeated destinations are recombined without creating a negative source
   coordinate;
3. the finite bottom and residue-state collars have polylogarithmic forcing;
4. the local reserve survives the exact finite cutoff and source normalization.

Those are now finite state-typing questions.  The eta dipole itself no longer
requires an unbounded cumulative sibling-switch schedule.

## 6. Proof boundary

Closed exactly:

- finite eta source decomposition;
- exact central/sibling carry image;
- exact entropy/von-Mangoldt cost;
- local capacity feasibility `c_k<a_k`;
- strict finite residual-plus-cost constant below one;
- extension to every nonnegative incoming source measure.

Open:

- positivity of the complete propagated endpoint-jet state;
- all-generation BJPR;
- Cycle Debt and RH.
