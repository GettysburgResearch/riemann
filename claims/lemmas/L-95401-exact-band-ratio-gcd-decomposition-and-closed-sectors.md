# L-95401 — Exact band, ratio and gcd decomposition closes the diagonal, near-diagonal and large-gcd sectors

Claim ID: `L-95401`  
Status: **PROPOSED COMPLETE ELEMENTARY DECOMPOSITION/BOUND THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95400`; PR #573 exact six-band source  
Scope: exact pair geometry and source-blind closed sectors; no separated coprime cancellation

## 1. Annular packet and FOCC square

Put

\[
G_X(m)
=
\frac{(\log m)J_0(m/X)+(\log2)J_1(m/X)}{\sqrt m}.
\tag{L-95401.1}
\]

Then

\[
\mathcal A(X)
=
\sum_{X/1024<m\le X\atop m\ \mathrm{odd}}
\mu(m)G_X(m).
\tag{L-95401.2}
\]

Write

\[
\mathcal D_A(X)=\sum_mG_X(m)^2
\]

and

\[
\boxed{
\mathcal X_A(X)
=2\sum_{m<n}\mu(m)\mu(n)G_X(m)G_X(n).
}
\tag{L-95401.3}
\]

Thus

\[
\boxed{
|\mathcal A(X)|^2=\mathcal D_A(X)+\mathcal X_A(X).
}
\tag{L-95401.4}
\]

Only odd squarefree cores contribute.

## 2. Exact dyadic activation geometry

Define the ten bands

\[
I_j(X)=\left(X2^{-j-1},X2^{-j}\right],
\qquad 0\le j\le9.
\tag{L-95401.5}
\]

On each band, `J_0,J_1` are fixed cubic polynomials with coefficients in `Q(sqrt(2))`. If

\[
m\in I_i(X),\qquad n\in I_j(X),\qquad m<n,
\]

then necessarily `i>=j` and

\[
\boxed{
1<\frac nm<2^{i-j+1}\le1024.
}
\tag{L-95401.6}
\]

Thus every surviving pair has bounded multiplicative ratio. The full correlation is the finite direct sum of the 55 band pairs

\[
0\le j\le i\le9.
\]

No tail or unbounded ratio remains.

## 3. Uniform annular bounds

PR #573 gives the safe bounds

\[
|K_0(x)|<512,
\qquad
|K_1(x)|<512.
\]

The absolute coefficient mass of the scale filter is

\[
1+\frac78+\frac7{32}+\frac1{64}=\frac{135}{64}.
\]

Therefore

\[
|J_0(x)|,|J_1(x)|<1080.
\tag{L-95401.7}
\]

On the annulus, `m>X/1024`, so

\[
\boxed{
|G_X(m)|
\le
34560\frac{\log(2X)}{\sqrt X}.
}
\tag{L-95401.8}
\]

Consequently

\[
\boxed{
\mathcal D_A(X)
\le
34560^2\log^2(2X).
}
\tag{L-95401.9}
\]

The annularizer improves the parent diagonal from `O(log^3 X)` to
`O(log^2 X)`.

## 4. Near-diagonal sector

For `H>=1`, define

\[
\mathcal N_H(X)
=
2\sum_{0<n-m\le H}
\mu(m)\mu(n)G_X(m)G_X(n).
\]

There are at most `XH` ordered pairs before imposing oddness or squarefreeness. Hence

\[
\boxed{
|\mathcal N_H(X)|
\le
2\cdot34560^2 H\log^2(2X).
}
\tag{L-95401.10}
\]

Thus every polylogarithmic-width near diagonal is already polylogarithmic without using Möbius cancellation.

## 5. Large-gcd sector

For `H>=2`, define

\[
\mathcal G_H(X)
=
2\sum_{m<n\atop (m,n)\ge X/H}
\mu(m)\mu(n)G_X(m)G_X(n).
\]

The number of such pairs is at most

\[
\sum_{d\ge X/H}
\left\lfloor\frac Xd\right\rfloor^2
\le
X^2\sum_{d\ge X/H}\frac1{d^2}
\le2XH.
\]

Therefore

\[
\boxed{
|\mathcal G_H(X)|
\le
4\cdot34560^2H\log^2(2X).
}
\tag{L-95401.11}
\]

Every polylogarithmic large-gcd sector is also closed source-blindly.

## 6. Exact gcd/common-divisor coordinates

For a surviving odd-squarefree pair, write

\[
d=(m,n),
\qquad
m=da,
\qquad
n=db.
\]

Then

\[
a,b,d\ \text{are odd squarefree and pairwise coprime},
\]

and

\[
\boxed{
\mu(m)\mu(n)=\mu(a)\mu(b).
}
\tag{L-95401.12}
\]

The common divisor carries no Möbius sign. The activation constraints become

\[
\frac{X}{1024a}<d\le\frac Xa,
\qquad
\frac{X}{1024b}<d\le\frac Xb.
\tag{L-95401.13}
\]

For `a<b`, a nonempty interval forces

\[
\boxed{b<1024a.}
\tag{L-95401.14}
\]

The remaining correlation is therefore an exact finite-ratio coprime Type-II form in `(a,b)`, averaged over a sign-free common divisor `d`.

## 7. Small reduced-variable Type I sector

In the gcd coordinates of Section 6, restrict first to `a<=H`.  For fixed
`a<b<1024a`, the number of admissible common divisors is at most `X/b`.
Using (L-95401.8), the absolute contribution is bounded by

\[
2\cdot34560^2\log^2(2X)
\sum_{a\le H}
\sum_{a<b<1024a}\frac1b.
\]

The inner harmonic interval has uniformly bounded mass, so

\[
\boxed{
|\mathcal T_{a\le H}(X)|
\ll H\log^2(2X).
}
\tag{L-95401.15}
\]

Thus every polylogarithmic small-`a` Type I sector is also closed without
Möbius cancellation.

## 8. Final balanced separated small-gcd core

Fix

\[
H=(\log(2X))^B
\]

for any fixed `B`. By (L-95401.10) and (L-95401.11), the only nontrivial sector is

\[
\boxed{
\begin{gathered}
X/1024<m<n\le X,\\
n-m>H,\\
(m,n)<X/H.
\end{gathered}
}
\tag{L-95401.16}
\]

Equivalently, in gcd coordinates,

\[
\boxed{
\begin{gathered}
(a,b)=1,
\quad H<a<b<1024a,\\
d<X/H,
\quad d(b-a)>H,\\
(a,d)=(b,d)=1,
\end{gathered}
}
\tag{L-95401.17}
\]

with all three variables odd squarefree.

This is the exact balanced separated small-gcd annular core. No same-core, near-diagonal, high-common-divisor, remote-ratio or inactive-band term remains.

## 9. Boundary

```text
ten exact activation bands                 CLOSED
all ratios                                 <=1024 EXACT
annular diagonal                           O(log^2 X)
polylog near diagonal                      CLOSED ABSOLUTELY
polylog large-gcd sector                   CLOSED ABSOLUTELY
polylog small-a Type I sector               CLOSED ABSOLUTELY
common-divisor sign cancellation           EXACT
separated small-gcd coprime core           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
