# L-24511 — Fixed-ratio primitive-neighbor edges have sieve density `O(1/log X)`

Claim ID: `L-24511`  
Status: `PROPOSED — proof from the standard two-dimensional upper-bound sieve`  
Scope: balanced primitive-neighbor graph  
Issue: #245

Fix constants

\[
0<\eta_0<\eta_1<1,
\qquad A\ge1.
\]

Let `V_X` be the prime powers in `[eta_0 X,eta_1 X]`. Join ordered vertices
`d,q in V_X` when, for some integers `1<=a,b<=A` and one sign,

\[
\boxed{ad-bq=\pm1.}
\tag{L-24511.1}
\]

Let `E_X` denote the number of ordered edges, counted with the finite
`(a,b,sign)` multiplicity.

Then

\[
\boxed{
E_X\ll_{\eta_0,\eta_1,A}\frac{X}{(\log X)^2}+\sqrt X.
}
\tag{L-24511.2}
\]

In particular, compared with the `O(X/log X)` upper bound for vertices, the
harmful fixed-ratio edge family has one additional sieve logarithm.

## 1. Proper prime powers

The number of prime powers `p^r<=X` with `r>=2` is `O(sqrt X)`. For fixed
`d,a,b` and a sign, equation (L-24511.1) determines at most one `q`.
Likewise, for fixed `q,a,b` it determines at most one `d`. Therefore all edges
having at least one proper prime-power endpoint contribute

\[
O_A(\sqrt X).
\tag{L-24511.3}
\]

## 2. Prime--prime edges

It remains to count primes `d` for which

\[
q=\frac{ad\mp1}{b}
\tag{L-24511.4}
\]

is also prime and lies in the declared interval. The divisibility condition
`b|(ad\mp1)` restricts `d` to at most one residue class modulo
`b/(a,b)`; after that restriction, both `d` and `(ad\mp1)/b` are distinct
primitive affine-linear forms in one integer variable.

They have no fixed prime divisor: any exceptional local obstruction merely
removes the residue class and decreases the count. The standard Selberg/Brun
upper-bound sieve for two distinct primitive linear forms therefore gives

\[
\#\left\{d\asymp X:
 d\text{ prime},\ (ad\mp1)/b\text{ prime}
\right\}
\ll_{a,b,\eta_0,\eta_1}\frac{X}{(\log X)^2}.
\tag{L-24511.5}
\]

There are only `2A^2` choices of `(a,b,sign)`. Summing (L-24511.5) and adding
(L-24511.3) proves (L-24511.2).

## 3. First-sweep consequence

Suppose a balanced correction source has excesses

\[
0\le e_d\le C X^{-1/2}
\]

and diagonal masses `A_d>=A_0>0`. A full diagonal sweep sends at most

\[
\frac{C}{A_0\sqrt X}
\]

through each unit-weight primitive edge. Hence the total positive mass created
on other fixed-ratio prime-power rows is at most

\[
\boxed{
O_{C,A_0,\eta_0,\eta_1,A}
\left(
\frac{\sqrt X}{(\log X)^2}+1
\right).
}
\tag{L-24511.6}
\]

This is one logarithm smaller than the crude `O(sqrt X/log X)` mass of an
entire fixed-ratio prime band.

## 4. What remains for a full contraction

An edge count controls one correction sweep but not arbitrary repeated mass
concentration. A complete proof still needs one of:

1. a nonbacktracking affine-path sieve with enough logarithmic gain at every
   generation;
2. a bounded-overlap component decomposition with a stable exact solve on each
   exceptional component;
3. a weighted Schur estimate using the full favorable noncoprime entries.

The exact determinant reduction in `L-24503` is what makes these sieve targets
finite-dimensional: all coefficients `a,b` are bounded on a fixed ratio band.

## Dependency boundary

The only imported ingredient is the classical two-dimensional upper-bound
sieve for two nonproportional primitive affine-linear forms. No lower-bound
prime-pair theorem, Hardy--Littlewood conjecture, or RH input is used.

## Status boundary

This lemma proves sparsity of the first harmful fixed-ratio edge generation. It
does not by itself prove PNC or RH.
