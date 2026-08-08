# L-28006 — Binary–ternary pole-preserving prime-annulus bridge

Claim ID: `L-28006`  
Title: A positive-inverse Euler source matched to the binary and ternary scales turns the first averaged-carry commutator into one compact top-six generalized-prime statistic and one exact factor-eighteen carry scalar  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/ARITHMETIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: PR #289 `L-27601/L-27602/L-27604`; `L-28002`

## 1. Pole-matched binary–ternary source

Define

\[
\boxed{
\nu_{2,3}
=\mu*(\varepsilon-\delta_2)
*(\varepsilon-\tfrac13\delta_3).}
\tag{L-28006.1}
\]

Its Dirichlet series is

\[
\boxed{
N_{2,3}(s)
=\frac{E_{2,3}(s)}{\zeta(s)},
\qquad
E_{2,3}(s)
=(1-2^{-s})(1-3^{-s-1}).}
\tag{L-28006.2}
\]

The first factor vanishes at the pole `s=0` of the averaged-carry symbol; the
second vanishes at its pole `s=-1`.  Neither factor vanishes at a nontrivial
zeta zero.

## 2. Positive inverse and generalized prime weights

The inverse series is

\[
A_{2,3}^{\rm ann}(s)
=\frac{\zeta(s)}{(1-2^{-s})(1-3^{-s-1})}.
\]

If `n=2^a3^bm` with `(m,6)=1`, its coefficient is

\[
\boxed{
a_{2,3}^{\rm ann}(n)
=(a+1)\sum_{j=0}^{b}3^{-j}>0.}
\tag{L-28006.3}
\]

The generalized von Mangoldt sequence is

\[
\boxed{
\Lambda_{2,3}^{\rm ann}(q)
=\begin{cases}
2\log2,&q=2^r,\\
(1+3^{-r})\log3,&q=3^r,\\
\log p,&q=p^r,\ p\ne2,3,\\
0,&q\text{ not a prime power}.
\end{cases}}
\tag{L-28006.4}
\]

Every coefficient is nonnegative, and

\[
\boxed{
\nu_{2,3}*(a_{2,3}^{\rm ann}\log^2)
=\Lambda_{2,3}^{\rm ann}\log
+\Lambda_{2,3}^{\rm ann}*\Lambda_{2,3}^{\rm ann}.}
\tag{L-28006.5}
\]

## 3. Compact zeroth carry wavelet

Convolution with the constant-one sequence gives

\[
\boxed{
\mathbf1*\nu_{2,3}
=\varepsilon-\delta_2-	frac13\delta_3+	frac13\delta_6.}
\tag{L-28006.6}
\]

Put

\[
G^{\rm ann}_{2,3}(x)
=\mathbf1_{x\ge1}
-\mathbf1_{x\ge2}
-\tfrac13\mathbf1_{x\ge3}
+\tfrac13\mathbf1_{x\ge6}.
\tag{L-28006.7}
\]

Then `G_ann(x)=0` for `x>=6`, and at scale `m`

\[
\boxed{
Z^{\rm ann}_{n,m}(j)
=G^{\rm ann}_{2,3}(n/m)
-G^{\rm ann}_{2,3}(j/m)
-G^{\rm ann}_{2,3}((n-j)/m).}
\tag{L-28006.8}
\]

For the declared binary and ternary splits, the averaged source row vanishes
whenever

\[
\boxed{n\ge18m-2.}
\tag{L-28006.9}
\]

Moreover

\[
\sum_{j=0}^{5}G^{\rm ann}_{2,3}(j)=0,
\]

so the average-binomial source row is zero for every parent `n>=6`.

## 4. Compact continuum wavelet

Let the averaged continuum carry kernel have transform

\[
K(z)=\zeta(s)R(s),
\qquad
s=z+\frac12,
\qquad
R(s)=\frac{s-1}{s(s+1)}.
\]

The source convolution has transform

\[
\widehat z_{2,3}^{\rm ann}(z)
=E_{2,3}(s)R(s).
\tag{L-28006.10}
\]

Since

\[
R(s)=-\frac1s+\frac2{s+1},
\]

put `a=log2`, `b=log3`.  Exact inversion gives

\[
\boxed{
z_{2,3}^{\rm ann}(u)=
\begin{cases}
2e^{-3u/2}-e^{-u/2},&0\le u<a,\\
-2e^{-3u/2},&a\le u<b,\\
\tfrac13e^{-u/2}-4e^{-3u/2},&b\le u<a+b,\\
0,&u\ge a+b.
\end{cases}}
\tag{L-28006.11}
\]

Thus the complete zeroth carry output is compact on `[0,log6)`.

## 5. First commutator and every zeta zero

Let `U` denote multiplication by the logarithmic variable and define

\[
\mathcal C_{2,3}^{\rm ann}
=\nu_{2,3}*(Uk).
\]

Exactly as in the general commutator identity,

\[
\boxed{
\widehat{\mathcal C_{2,3}^{\rm ann}}(z)
=-E_{2,3}(s)R(s)\frac{\zeta'}{\zeta}(s)
-E_{2,3}(s)R'(s).}
\tag{L-28006.12}
\]

At a nontrivial zero `rho` of multiplicity `m_rho`, the residue is

\[
\boxed{
-m_\rho E_{2,3}(\rho)R(\rho)\ne0.}
\tag{L-28006.13}
\]

Every off-line zero therefore survives as a simple pole.

## 6. Exact top-six generalized-prime statistic

For `X>6`, the compact coordinate has vanished and convolution with the
generalized-prime measure gives

\[
\boxed{
\begin{aligned}
\mathcal C_{2,3}^{\rm ann}(\log X)
=\frac1{\sqrt X}\Bigg[&
\sum_{X/2<q\le X}
\Lambda_{2,3}^{\rm ann}(q)
\left(\frac{2q}{X}-1\right)\\
&-\sum_{X/3<q\le X/2}
\Lambda_{2,3}^{\rm ann}(q)\frac{2q}{X}\\
&+\sum_{X/6<q\le X/3}
\Lambda_{2,3}^{\rm ann}(q)
\left(\frac13-\frac{4q}{X}\right)
\Bigg].
\end{aligned}}
\tag{L-28006.14}
\]

The endpoint `q=X/2` belongs to the middle band, `q=X/3` to the last band, and
`q=X/6` contributes through the terminal jump and is excluded from the open
last interval.

The extra generalized-prime contribution at powers of `2` and `3` is
`O(log X/sqrt X)` on this annulus, so it does not change the polynomial or
subpower growth exponent of the ordinary prime-power statistic.

## 7. Exact continuum–discrete boundary

For a completely additive formal logarithm `ell`, define the continuum and
discrete commutator scalars exactly as in PR #289, with `nu_(2,3)` in place of
`omega_2`.  Put

\[
B_\ell(Y)=\sum_{n\le Y}n\Lambda_\ell(n).
\]

The universal row comparison and the divisor identity (L-28006.6) give

\[
\boxed{
\begin{aligned}
\mathcal R_X^{\rm cont}-\mathcal R_X^{\rm disc}
=\frac{2}{X(X+1)}\Bigl[&
B_\ell(X)-2B_\ell(X/2)-B_\ell(X/3)\\
&+2B_\ell(X/6)-\ell(3)
\Bigr].
\end{aligned}}
\tag{L-28006.15}
\]

For `ell=log`, the prime number theorem gives

\[
\boxed{
\mathcal R_X^{\rm cont}-\mathcal R_X^{\rm disc}
=\frac49+o(1).}
\tag{L-28006.16}
\]

Thus the physical and discrete commutators have the same local growth exponent,
with a completely explicit bounded boundary.

## 8. Exact factor-eighteen carry representation

For every integer `X>=6`, the averaged zeroth source row is zero.  Differentiating

\[
\nu_{2,3}*a_{2,3}^{\rm ann}=\varepsilon
\]

gives

\[
\nu_{2,3}\log
=-\Lambda_{2,3}^{\rm ann}*\nu_{2,3}.
\]

Hence

\[
\boxed{
\mathcal R_X^{\rm disc}
=\frac1{X+1}
\sum_{j=0}^{X}
\sum_{m\le X}
\Lambda_{2,3}^{\rm ann}(m)
Z^{\rm ann}_{X,m}(j).}
\tag{L-28006.17}
\]

Every row with `X>=18m-2` vanishes on the declared binary–ternary source.  The
pole-preserving physical scalar has therefore been mapped exactly to one finite
factor-eighteen carry transition plus the bounded boundary (L-28006.15).

## 9. Second commutator

Let

\[
C_{2,3}^{\rm ann}
=\nu_{2,3}*(a_{2,3}^{\rm ann}\log^2)
\ge0.
\]

Then

\[
\boxed{
\nu_{2,3}*(U^2k)
=U^2z_{2,3}^{\rm ann}
+2\lambda_{2,3}^{\rm ann}*(Uz_{2,3}^{\rm ann})
+C_{2,3}^{\rm ann}*z_{2,3}^{\rm ann}.}
\tag{L-28006.18}
\]

The first commutator detects every zero; the second contains the coefficientwise
nonnegative generalized Selberg forcing on the same compact top-six source.

## 10. Proof boundary

Closed exactly or with the PNT only for the displayed limit:

1. positive inverse and generalized-prime source;
2. compact top-six continuum wavelet;
3. noncancellation of every zeta zero;
4. explicit prime-annulus statistic;
5. exact continuum/discrete boundary and its `4/9` limit;
6. exact factor-eighteen carry scalar;
7. the second-commutator Selberg bridge.

Open:

1. a subpower pointwise or local-energy estimate for (L-28006.14);
2. a strict independent-frequency recurrence on the finite transition;
3. RH.
