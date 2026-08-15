# L-91862 — The two-sorted realization has one all-column nonnegative capacity complement

Claim ID: `L-91862`  
Status: **PROPOSED COMPLETE ALL-COLUMN THEOREM ON FROZEN ANALYTIC INPUTS — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-91861`; frozen `L-91733`, `L-91111`, terminal omission, positive radix-four inverse  
RH status: **unproved**

## 1. Complements of the one realized row

For the row `d_X` with identifier `rid_X` from `L-91861`, define

\[
e_X^{(4)}(q)=\Omega_X(q)-\Xi_q(d_X),
\qquad
e_X^{\rm ord}(q)=w_X(q)-\Gamma_q(d_X).
\tag{L-91862.1}
\]

These are signed response comparisons until nonnegativity is proved. They are not arithmetic source packets.

## 2. The Hall-bonus channel creates no comparison error

The exact retained ideal row is the sum of the residual-source row and `B_X`. The realization uses the same `B_X` through `I_bonus`. Hence

\[
[I_{\rm bonus}B_X]-B_X=0
\tag{L-91862.2}
\]

in every row, ordinary, detail, and literal-score observation. The anchored identity block has the same property. Thus the complete finite/continuum and intrinsic collar comparison is exactly the bulk comparison.

## 3. Every nonterminal physical column

The retained adjacent-cell mismatch and the bulk collar obey the frozen bound

\[
\left|e_X^{\rm bulk}(q)\right|
<\frac{971}{4q\sqrt K}
\qquad(q\ge2).
\tag{L-91862.3}
\]

The derivation includes all multiples `jq>=K`, so it covers the entire range `2<=q<K`. For `2<=q<=X/4`,

\[
\frac{|e_X^{\rm bulk,(4)}(q)|}{\Omega_X(q)}
<\frac{129}{\sqrt K}.
\tag{L-91862.4}
\]

The ideal total row uses at most the native detail target. Since every channel is thinned by the same `tau_K`,

\[
\Xi_q(d_X)
<\tau_K\left(1+\frac{129}{\sqrt K}\right)\Omega_X(q)
=\frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q)
<\Omega_X(q).
\tag{L-91862.5}
\]

Thus all nonterminal complements are strictly positive.

## 4. Terminal annulus

The top omission is made before Hall and therefore removes the same original fibre from both sorts. The complete possible terminal overfill is bounded by

\[
4452X^{-3/2},
\]

while the omitted positive endpoint interval removes more than

\[
5033X^{-3/2}.
\]

The margin is

\[
\boxed{581X^{-3/2}>0.}
\tag{L-91862.6}
\]

The bulk collar in the two-sorted construction is no larger than the frozen full-source collar, and the identity bonus channel contributes no finite-realization error. Common thinning only decreases use. Above retained support the response is zero.

Therefore

\[
\boxed{e_X^{(4)}(q)\ge0\quad(q\ge2).}
\tag{L-91862.7}
\]

## 5. Ordinary complement from the same detail complement

The finite positive radix-four inverse gives

\[
\boxed{
e_X^{\rm ord}(q)
=\sum_{h\ge0}2^he_X^{(4)}(4^hq)\ge0.
}
\tag{L-91862.8}
\]

Consequently the same row `d_X` satisfies the exact capacity equalities

\[
\boxed{
\Xi(d_X)+e_X^{(4)}=\Omega_X,
\qquad
\Gamma(d_X)+e_X^{\rm ord}=w_X.
}
\tag{L-91862.9}
\]

No branchwise inequality, child capacity promotion, or positive-source interpretation of the signed comparison is used.

## 6. Boundary

```text
bonus and anchored comparison error          exactly zero
all q<K columns                              covered
nonterminal strict reserve                   exact on frozen bounds
terminal reserve                             581 X^-3/2
one detail complement                        same realized row
ordinary complement                          positive inverse of same vector
source provenance of complements             not asserted
Riemann Hypothesis                           unproved
```
