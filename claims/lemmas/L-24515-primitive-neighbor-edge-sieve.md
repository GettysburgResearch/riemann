# L-24515 — Fixed-ratio primitive-neighbor edges have sieve density `O(1/log X)`

Claim ID: `L-24515`  
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
\tag{L-24515.1}
\]

Let `E_X` denote the number of ordered edges, counted with the finite
`(a,b,sign)` multiplicity. Then

\[
\boxed{
E_X\ll_{\eta_0,\eta_1,A}\frac{X}{(\log X)^2}+\sqrt X.
}
\tag{L-24515.2}
\]

Compared with the `O(X/log X)` vertex count, the harmful fixed-ratio edge
family has one additional sieve logarithm.

## 1. Proper prime powers

There are `O(sqrt X)` prime powers `p^r<=X` with `r>=2`. For fixed
`d,a,b` and a sign, equation (L-24515.1) determines at most one `q`, and
conversely. Hence all edges with a proper prime-power endpoint contribute

\[
O_A(\sqrt X).
\tag{L-24515.3}
\]

## 2. Prime--prime edges

It remains to count primes `d` for which

\[
q=\frac{ad\mp1}{b}
\tag{L-24515.4}
\]

is prime and lies in the declared interval. The divisibility condition restricts
`d` to at most one residue class modulo `b/(a,b)`. On that class, `d` and
`(ad\mp1)/b` are two distinct primitive affine-linear forms. The classical
Selberg/Brun upper-bound sieve for two nonproportional primitive linear forms
gives

\[
\#\{d\asymp X:d\text{ prime},\ (ad\mp1)/b\text{ prime}\}
\ll_{a,b,\eta_0,\eta_1}\frac{X}{(\log X)^2}.
\tag{L-24515.5}
\]

Summing the finitely many `(a,b,sign)` choices and adding (L-24515.3) proves
(L-24515.2).

## 3. First-sweep consequence

Suppose a balanced source has excesses `0<=e_d<=C X^{-1/2}` and diagonal
masses `A_d>=A_0>0`. A full diagonal sweep sends at most
`C/(A_0 sqrt X)` through each unit-weight primitive edge. Thus the total new
positive mass on other fixed-ratio rows is

\[
\boxed{
O_{C,A_0,\eta_0,\eta_1,A}
\left(\frac{\sqrt X}{(\log X)^2}+1\right).
}
\tag{L-24515.6}
\]

This is one logarithm smaller than the crude mass of a full fixed-ratio prime
band.

## 4. Remaining all-order obligation

An edge count controls one generation, not arbitrary repeated concentration. A
complete contraction still needs a nonbacktracking affine-path sieve, a stable
bounded-overlap component solve, or a weighted Schur estimate using the
favorable noncoprime entries.

## Dependency boundary

The only imported ingredient is the classical two-dimensional upper-bound
sieve. No prime-pair lower bound, Hardy--Littlewood conjecture, or RH input is
used.

## Status boundary

This lemma proves first-generation sparsity. It does not by itself prove signed
excess transport or RH.
