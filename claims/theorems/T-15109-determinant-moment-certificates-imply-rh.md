# T-15109 — Proof-producing determinant-moment certificates imply RH

Claim ID: `T-15109`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; MOMENT MATCH OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15128`; identity theorem; standard `det_2` continuity  
Scope: rigorous recovered version of the July 2026 determinant route  
Related counterexample candidates: none

## 1. Finite-rank operator data

Let `K_M=K_M*` be finite-rank operators and assume a directed proof establishes

\[
 \boxed{\|K_M-K\|_2\to0}
 \tag{T-15109.1}
\]

for one self-adjoint `K in S_2`. Let real/complex constants satisfy

\[
 a_M\to a,
 \qquad
 b_M\to b.
 \tag{T-15109.2}
\]

Define

\[
 F_M(w)=e^{a_M+b_Mw}\det{}_2(I+iwK_M),
 \qquad
 F(w)=e^{a+bw}\det{}_2(I+iwK).
 \tag{T-15109.3}
\]

Then `F_M -> F` locally uniformly.

## 2. Logarithmic-derivative certificate

Choose `r>0` so that `xi(1/2+w)` and every sufficiently large `F_M(w)` are
nonzero on `|w|<=r`. Suppose directed analytic estimates prove

\[
 \boxed{
 \sup_{|w|\le r}
 \left|
 b_M+\operatorname{Tr}\!
 \left(iK_M[(I+iwK_M)^{-1}-I]\right)
 -\frac{\xi'}{\xi}(1/2+w)
 \right|\to0.}
 \tag{T-15109.4}
\]

Suppose also

\[
 F_M(0)\to\xi(1/2).
 \tag{T-15109.5}
\]

The trace in (T-15109.4) is well-defined because the bracketed product is trace
class.

Passing to the limit and integrating along paths inside the disk gives

\[
 \log F(w)-\log F(0)
 =\log\xi(1/2+w)-\log\xi(1/2).
\]

Together with (T-15109.5),

\[
 F(w)=\xi(1/2+w)
 \quad(|w|<r).
\]

Both sides are entire, so the identity theorem yields

\[
 \boxed{F(w)\equiv\xi(1/2+w).}
 \tag{T-15109.6}
\]

By self-adjointness of `K`, all zeros lie on the centered imaginary axis; hence
RH follows.

## 3. Equivalent all-moment certificate

Instead of (T-15109.4), it is enough to prove all of the following.

1. For every `m>=2`,
   
   \[
   \boxed{
   \lim_{M\to\infty}\operatorname{Tr}(K_M^m)
   =\frac{(-1)^{m-1}i^{-m}}{(m-1)!}
    \partial_w^m\log\xi(1/2+w)|_{w=0}.}
   \tag{T-15109.7}
   \]

2. There is a common `r>0` and a summable majorant for
   
   \[
   \frac{r^m}{m}|\operatorname{Tr}(K_M^m)|
   \tag{T-15109.8}
   \]
   
   uniformly in `M`.

3. The scalar and linear coefficients agree with the central value and first
   logarithmic derivative.

Then the regularized determinant power series agrees coefficient by coefficient
with `log xi` on `|w|<r`; the majorant permits passage through the infinite sum,
and the preceding proof applies.

A finite set of moment identities is not sufficient.

## 4. Exact finite proof objects

A production certificate should contain:

1. rational/ball finite-rank self-adjoint matrices `K_M`;
2. directed `S_2` Cauchy radii;
3. exact traces `Tr(K_M^m)` or directed intervals for every retained order;
4. a source-independent arithmetic producer for the corresponding central
   coefficients;
5. residual-annihilation identities at the cyclic tensor level;
6. a common analytic tail majorant;
7. central constants and local zero-free disks;
8. an independent final `det_2`/log-derivative replay.

`X-15111` verifies only the exact finite formal algebra and the necessary Hankel
gates. It intentionally does not manufacture the arithmetic moment identity.

## 5. Relationship to the smooth-window residual programme

The determinant theorem is an alternative final consumer. It does not prove the
one-sided LMI

\[
 R_j(c_j)\succeq-\omega_jM_j,
 \qquad \omega_j<s_j.
\]

Conversely, cofinal strict residual LMIs already imply RH without constructing
`K`. The missing arithmetic content cannot be removed by switching consumers;
it must be proved either as the complete signed residual floor or as the
all-order determinant moment identity.

## 6. Nonclaim

No family `K_M` satisfying (T-15109.4) or (T-15109.7)--(T-15109.8) for the
Riemann target has been certified in this branch. Therefore this theorem does
not complete RH.
