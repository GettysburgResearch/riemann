# T-90902 — A direct central Q4 energy criterion for RH

Claim ID: `T-90902`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the exact filtered-Chebyshev formula of PR #362 (`T-90404`); the classical Mellin transform of \(\psi(x)-x\); von Koch under RH  
RH status: **unproved**

## 1. The central Q4 wavelet

Let

\[
 E(x)=\psi(x)-x
\]

and define

\[
 \boxed{
 F_4(x)=E(4x)-2E(2x)-4E(x)+8E(x/2).
 }
\tag{T-90902.1}
\]

The linear terms cancel, so equivalently

\[
 F_4(x)=\psi(4x)-2\psi(2x)-4\psi(x)+8\psi(x/2).
\tag{T-90902.2}
\]

For an even integer central split, the own compact Q4 innovation of PR #362 satisfies

\[
 I_\circ(n,n/2)=F_4(n)-4\log4,
\tag{T-90902.3}
\]

before the delayed logarithmic gauge.  Thus (T-90902.1) is the exact one-dimensional central consumer of the corrected Q4 source.

The function is constant on every quarter-cell \([m/4,(m+1)/4)\).  In prime-annulus form,

\[
 F_4(x)=
 3\!\sum_{n\le x/2}\!\Lambda(n)
 -5\!\sum_{x/2<n\le x}\!\Lambda(n)
 -\!\sum_{x<n\le2x}\!\Lambda(n)
 +\!\sum_{2x<n\le4x}\!\Lambda(n).
\tag{T-90902.4}
\]

## 2. Exact quarter-cell energy

For quarter-aligned endpoints \(X<Y\), put

\[
 \mathcal C_4[X,Y]
 =\int_X^Y\frac{|F_4(x)|^2}{x^2}\,dx.
\tag{T-90902.5}
\]

Then

\[
 \boxed{
 \mathcal C_4[X,Y]
 =4\sum_{m=4X}^{4Y-1}
 \frac{|F_4(m/4)|^2}{m(m+1)}.
 }
\tag{T-90902.6}
\]

This is a positive, exact finite arithmetic statistic on every logarithmic block.

## 3. Zero-safe Mellin multiplier

For \(\Re s>1\),

\[
 \mathcal E(s):=\int_1^\infty E(x)x^{-s-1}\,dx
 =-\frac{\zeta'(s)}{s\zeta(s)}-\frac1{s-1}.
\tag{T-90902.7}
\]

Scaling (with only entire lower-boundary corrections) gives

\[
 \int_1^\infty F_4(x)x^{-s-1}\,dx
 =M_4(s)\mathcal E(s)+B_4(s),
\tag{T-90902.8}
\]

where \(B_4\) is entire and

\[
 \boxed{
 M_4(s)=4^s-2\,2^s-4+8\,2^{-s}
 =(4^s-4)(1-2^{1-s}).
 }
\tag{T-90902.9}
\]

If \(1/2<\Re s<1\), neither factor in (T-90902.9) can vanish: taking absolute values would force \(\Re s=1\).  Therefore every off-line zeta zero in the right half of the critical strip survives the filter.

## 4. RH implies polynomial block energy

Under RH, von Koch gives

\[
 E(x)=O(\sqrt x\log^2(2x)).
\]

Hence

\[
 F_4(x)=O(\sqrt x\log^2(2x))
\]

and, for \(J\ge1\),

\[
 \boxed{
 \int_{e^J}^{e^{J+1}}
 \frac{|F_4(x)|^2}{x^2}\,dx
 =O(J^4).
 }
\tag{T-90902.10}
\]

## 5. Polynomial block energy implies RH

Assume that for some fixed constants \(C,B\),

\[
 \boxed{
 \int_{e^J}^{e^{J+1}}
 \frac{|F_4(x)|^2}{x^2}\,dx
 \le C(1+J)^B
 \qquad(J\ge J_0).
 }
\tag{T-90902.11}
\]

For every \(\sigma>1/2\), Cauchy--Schwarz on each logarithmic block gives

\[
 \int_{e^J}^{e^{J+1}}
 |F_4(x)|x^{-\sigma-1}\,dx
 \ll (1+J)^{B/2}e^{-(\sigma-1/2)J},
\tag{T-90902.12}
\]

which is summable.  Therefore the Mellin transform in (T-90902.8) is holomorphic on \(\Re s>1/2\).

If \(\rho\) were a zeta zero with \(\Re\rho>1/2\), then \(\mathcal E(s)\) would have a pole at \(s=\rho\), and (T-90902.9) would not vanish there.  The entire term \(B_4\) cannot cancel that pole.  Contradiction.  Functional-equation symmetry then gives RH.

Thus

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal C_4[e^J,e^{J+1}]
 =O((1+J)^B)
 \text{ for some finite }B.
 }
\tag{T-90902.13}
\]

Under RH one may take \(B=4\).

## 6. Relation to the reviewed Q4 gap

The specialist review on PR #371 correctly records that the old global `PIG => RH` assembly is incomplete.  The criterion above does **not** use that assembly.  It proves the reverse implication directly from the central filtered-Chebyshev scalar and its zero-safe Mellin multiplier.

What remains open is the arithmetic estimate (T-90902.11), or a rigorous bridge from any proposed positive Q4 block measure to this central energy.  Neither is supplied here.
