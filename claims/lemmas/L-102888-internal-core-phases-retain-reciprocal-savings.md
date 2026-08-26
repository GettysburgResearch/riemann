# L-102888 — Internal core phases retain reciprocal prime or core-length savings

Claim ID: `L-102888`  
Status: **PROVED EXACT PHASE/NORMALIZATION THEOREM**  
Created: 2026-08-24  
Depends on: `L-102885--L-102886`; `L-102883`  
RH status: **not assumed**

Retain one coprime reduced cross packet

\[
N=Pc^2,\qquad M=Qd^2,\qquad(c,d)=1
\]

after the common-square extraction.  Every coefficient contains the literal
core factors \(c^{-1}\) and \(d^{-1}\).

For a dyadic stopped-Vaughan or smooth-boundary block, choose on each physical
side one core variable interval on which the selected internal phase acts.
Write their lengths as \(C_N\) and \(C_M\).  The fixed-block additive
orthogonality theorem has the form

\[
\sum_{h=0}^{\ell-1}\|F_{\ell,h}\|_2^2
\ll_\phi
\left(1+\frac{\ell}{C}\right)E,
\tag{L-102888.1}
\]

where \(E\) is the corresponding unphased coefficient energy.  Common factors
are extracted before applying this formula.

## 1. One nontrivial reduced core

Assume

\[
c>1,\qquad d=1,
\]

and put \(\ell=P^+(c)\), \(c=\ell c_0\).  Use the nonzero
\(\ell\)-phase on the \(M\)-field.  The Ramanujan identity and Cauchy give

\[
\begin{aligned}
|\mathcal C_{\ell}|
&\le
\sqrt{\ell}\,
\frac1\ell E_N^{1/2}
\left[
\left(1+\frac{\ell}{C_M}\right)E_M
\right]^{1/2}\\
&=
\boxed{
\left(
\frac1\ell+\frac1{C_M}
\right)^{1/2}
E_N^{1/2}E_M^{1/2}.
}
\end{aligned}
\tag{L-102888.2}
\]

Thus a one-sided core discrepancy retains either reciprocal-prime gain or
reciprocal variable-length gain; the phase cardinality never creates a
positive power of \(\ell\).

## 2. Two nontrivial reduced cores

Assume

\[
c>1,\qquad d>1.
\]

Put

\[
\ell_c=P^+(c),\qquad
\ell_d=P^+(d).
\]

The primes are distinct.  Use the nonzero \(\ell_d\)-phase on the
\(N\)-field and the nonzero \(\ell_c\)-phase on the \(M\)-field.  After
factoring \(c=\ell_c c_0\), \(d=\ell_d d_0\), double Cauchy gives

\[
\boxed{
|\mathcal C_{\ell_c,\ell_d}|
\ll_\phi
\left[
\left(\frac1{\ell_d}+\frac1{C_N}\right)
\left(\frac1{\ell_c}+\frac1{C_M}\right)
\right]^{1/2}
E_N^{1/2}E_M^{1/2}.
}
\tag{L-102888.3}
\]

Both zero frequencies are absent and both literal internal-prime weights have
been used exactly once.

## 3. Adaptive variable choice

For a balanced block

\[
U_1V_1M\asymp\sqrt Y,
\]

the phase may be placed on the largest available variable interval.  Hence

\[
\max(U_1,V_1,M)\gg Y^{1/6}.
\tag{L-102888.4}
\]

No lower bound for the external owner \(q\) is inferred from this relation.
For a smooth-boundary block, the phase is placed on the largest support-active
factor after the stopped monoid and common factors are retained.

## 4. Source and energy scope

The choice of \(\ell_c,\ell_d\) depends only on the corresponding reduced
physical core.  It is therefore a source-owned label, unlike a
pair-dependent arbitrary discrepancy selection.

The free stopped-Vaughan energy and equal-product multiplicity remain
\(Y^{o(1)}\) by `L-102883`.  Equations (L-102888.2)--(L-102888.3) supply
additional reciprocal gains inside the coherent physical restriction.

They do not by themselves sum different owner squareclasses.  The final
coherent theorem must retain the equal-core packet together with these
internally phased unequal-core packets.
