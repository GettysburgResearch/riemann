# L-90417 — Complete residue carry covariance is a Jordan-2 GCD square

Claim ID: `L-90417`  
Title: Averaging parent and split residues over one complete common period turns the centered carry Gram into an exact Jordan-totient square and gives a polylogarithmic deterministic-to-diagonal bound  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: elementary residue counting, Jordan inversion, and Cauchy--Schwarz  
Scope: the fully periodized residue ensemble; it is not the fixed-endpoint PIG measure and does not prove PIG or RH

## 1. The residue carry variable

For an integer `d>=2` and residues `u,v`, define

\[
 X_d(u,v)=\mathbf1_{\,v\bmod d>u\bmod d}.
 \tag{L-90417.1}
\]

This is exactly the carry indicator

\[
 \left\lfloor\frac Nd\right\rfloor
 -\left\lfloor\frac jd\right\rfloor
 -\left\lfloor\frac{N-j}{d}\right\rfloor
\]

when `u=N` and `v=j`, because the indicator is one precisely when `j mod d>N mod d`.

Let `d,e>=2`, put

\[
 g=(d,e),
 \qquad
 L=[d,e],
\]

and average `u,v` independently and uniformly over `Z/LZ`.

The one-variable mean is

\[
 \boxed{
 p_d:=\mathbb E X_d=\frac{d-1}{2d}.
 }
 \tag{L-90417.2}
\]

## 2. Exact joint count

Write

\[
 d=gD,
 \qquad
 e=gE.
\]

For compatible residues modulo `d,e`, first fix the shared residues `r,s mod g` of `u,v`. If `s>r`, the number of lifts satisfying `v_d>u_d` is

\[
 \frac{D(D+1)}2,
\]

while if `s<=r` it is

\[
 \frac{D(D-1)}2.
\]

The corresponding counts for modulus `e` are obtained by replacing `D` with `E`. There are `g(g-1)/2` pairs with `s>r` and `g(g+1)/2` pairs with `s<=r`. Dividing the resulting count by `L^2=(gDE)^2` and subtracting `p_dp_e` gives

\[
 \boxed{
 \operatorname{Cov}(X_d,X_e)
 =\frac{(d,e)^2-1}{4de}.
 }
 \tag{L-90417.3}
\]

In particular, centered carries at coprime moduli are exactly orthogonal in the complete residue ensemble.

## 3. Jordan-2 factorization

Let `a_d` be finitely supported complex coefficients on `2<=d<=D_0`. Define the periodized centered field

\[
 Z(u,v)=\sum_{d=2}^{D_0}a_d(X_d(u,v)-p_d).
 \tag{L-90417.4}
\]

Equation (L-90417.3) gives

\[
 \mathbb E|Z|^2
 =\frac14\sum_{d,e}
 a_d\overline{a_e}
 \frac{(d,e)^2-1}{de}.
 \tag{L-90417.5}
\]

Use the Jordan identity

\[
 n^2=\sum_{q\mid n}J_2(q).
\]

The subtraction of one removes exactly the `q=1` term, so

\[
 \boxed{
 \mathbb E|Z|^2
 =\frac14\sum_{q=2}^{D_0}J_2(q)
 \left|
 \sum_{\substack{d\le D_0\\q\mid d}}
 \frac{a_d}{d}
 \right|^2.
 }
 \tag{L-90417.6}
\]

This is an exact positive Jordan-2 Bohr square. It is the residue-probability counterpart of the Jordan-totient positive energies that occur in the corrected Farey/analytic-totient lineage.

## 4. Elementary polylogarithmic operator bound

For one `q`, Cauchy--Schwarz with weights `1/d` gives

\[
 \left|\sum_{q\mid d}\frac{a_d}{d}\right|^2
 \le
 \left(\sum_{q\mid d}\frac{|a_d|^2}{d}\right)
 \left(\sum_{q\mid d}\frac1d\right).
 \tag{L-90417.7}
\]

Since

\[
 \sum_{\substack{d\le D_0\\q\mid d}}\frac1d
 \le\frac{1+\log D_0}{q},
\]

summing (L-90417.7) against `J_2(q)` yields

\[
 \begin{aligned}
 \mathbb E|Z|^2
 &\le\frac{1+\log D_0}{4}
 \sum_{d=2}^{D_0}\frac{|a_d|^2}{d}
 \sum_{q\mid d}\frac{J_2(q)}q.
 \end{aligned}
 \tag{L-90417.8}
\]

Now `J_2(q)/q<=q`, and

\[
 \frac{\sigma(d)}d
 =\sum_{r\mid d}\frac1r
 \le1+\log d.
\]

Therefore

\[
 \boxed{
 \mathbb E|Z|^2
 \le\frac14(1+\log D_0)^2
 \sum_{d=2}^{D_0}|a_d|^2.
 }
 \tag{L-90417.9}
\]

No multiplicativity or sign condition on `a_d` is used.

## 5. Comparison with the independent diagonal model

The diagonal variance is

\[
 \operatorname{Var}(X_d)
 =p_d(1-p_d)
 =\frac{d^2-1}{4d^2}
 \ge\frac3{16}.
 \tag{L-90417.10}
\]

Hence

\[
 \boxed{
 \mathbb E|Z|^2
 \le\frac43(1+\log D_0)^2
 \sum_d|a_d|^2\operatorname{Var}(X_d).
 }
 \tag{L-90417.11}
\]

Thus a deterministic coefficient packet in the completely residue-randomized carry geometry is controlled, with only a squared-logarithmic loss, by its independent diagonal/Rademacher benchmark.

This is a genuine PMB theorem in the periodized geometry.

## 6. Connection and limitation

The theorem explains why complete-period/Farey/Jordan energies are benign:

```text
complete residue averaging
 -> coprime orthogonality
 -> Jordan-2 positive squares
 -> polylogarithmic spectral norm.
```

The actual PIG block is not this ensemble. It freezes one parent endpoint and averages only the admissible split coordinate, with finite endpoint and incomplete-period effects. Those effects can create large correlations even for coprime moduli; `R-90416` gives an exact witness.

Accordingly, replacing the true block by (L-90417.6) would erase the same local boundary that the first Farey/Mertens cell detects.

## 7. Proof boundary

Closed exactly here:

1. the complete-residue mean and covariance;
2. exact coprime orthogonality;
3. Jordan-2 square factorization;
4. elementary squared-log operator bound;
5. periodized deterministic-to-diagonal comparison.

Open:

1. control of incomplete-period/fixed-endpoint covariance;
2. a valid transfer to the PIG block measure;
3. PIG and RH.
