# L-102883 — Coherent centered double-phase energy over dyadic prime families

Claim ID: `L-102883`  
Status: **PROVED UNCONDITIONAL GLOBAL PHASE-PACKING THEOREM**  
Created: 2026-08-24  
Depends on: `L-102882`  
RH status: **not assumed**

Let `P_1` and `P_2` be disjoint finite prime families contained in dyadic intervals

\[
L_i\le\ell<2L_i,
\qquad i=1,2,
\]

and let `(c_b)` be a finitely supported Hilbert-valued sequence on

\[
B\le b<2B.
\]

Define

\[
S_{\ell_1,\ell_2;h_1,h_2}
=\sum_b c_b
 e_{\ell_1}(h_1b^2)e_{\ell_2}(h_2b^2)
\]

and the naturally weighted nonzero-phase energy

\[
\boxed{
\mathcal E
=\sum_{\ell_1\in P_1}\sum_{\ell_2\in P_2}
{1\over\ell_1\ell_2}
\sum_{h_1=1}^{\ell_1-1}
\sum_{h_2=1}^{\ell_2-1}
\|S_{\ell_1,\ell_2;h_1,h_2}\|^2.
}
\tag{L-102883.1}
\]

Put

\[
M_1=\sum_b\|c_b\|,
\qquad
M_2^2=\sum_b\|c_b\|^2.
\]

Then

\[
\boxed{
\begin{aligned}
\mathcal E
\ll{}&
{L_1L_2\over
 \log(2L_1)\log(2L_2)}M_2^2\\
&+M_1^2
\prod_{i=1}^2
\left(1+{\log(2B)\over\log(2L_i)}\right).
\end{aligned}}
\tag{L-102883.2}
\]

The implied constant is absolute.

## Proof

For an integer `d`, define the centered divisor count

\[
K_i(d)
=\sum_{\ell\in P_i}
\left(\mathbf1_{\ell\mid d}-{1\over\ell}\right).
\]

Dividing the exact identity `L-102882.2` by `ell_1 ell_2` and summing the moduli gives

\[
\boxed{
\mathcal E
=\sum_{b,b'}
\langle c_b,c_{b'}\rangle
K_1(b^2-b'^2)K_2(b^2-b'^2).
}
\tag{L-102883.3}
\]

For `b=b'`, the classical Chebyshev prime-count bound gives

\[
|K_i(0)|\le \#P_i\ll {L_i\over\log(2L_i)}.
\]

This yields the first term of (L-102883.2).

For `b\ne b'`, one has `0<|b^2-b'^2|<4B^2`.  The number of primes in `P_i` dividing this integer is at most

\[
{\log(4B^2)\over\log L_i},
\]

while

\[
\sum_{\ell\in P_i}{1\over\ell}
\ll {1\over\log(2L_i)}.
\]

Consequently

\[
|K_i(b^2-b'^2)|
\ll
1+{\log(2B)\over\log(2L_i)}.
\]

Using

\[
|\langle c_b,c_{b'}\rangle|
\le\|c_b\|\|c_{b'}\|
\]

and summing proves the second term.

## Square-core corollary

For the literal one-octave square-core coefficients

\[
c_b={d_b\over b\sqrt Q}\,v_b,
\qquad |d_b|\le Y^{o(1)},
\qquad \|v_b\|\le1,
\]

one has

\[
M_1^2\ll {Y^{o(1)}\over Q},
\qquad
M_2^2\ll {Y^{o(1)}\over QB}.
\]

Hence

\[
\boxed{
\mathcal E
\ll {Y^{o(1)}\over Q}
\left[
1+{L_1L_2\over
B\log(2L_1)\log(2L_2)}
\right].
}
\tag{L-102883.4}
\]

In particular the complete coherent weighted double-phase packet is subpower in the long-core range

\[
B\ge L_1L_2.
\]

This closes the **global weighted core-phase transform** in that range; it is stronger than adding the fixed-quadruple estimates of `T-102870`.

## Scope

The weights `1/(ell_1 ell_2)` in (L-102883.1) are essential.  Applying the theorem to the complete balanced owner current requires an exact source allocation which keeps the selected owner weights attached to the coherent phase family.  A fixed-pair cancellation which spends those weights against phase cardinality first cannot then reuse them here.

Thus (L-102883.4) closes the long-core weighted phase row and exposes the remaining owner-allocation/short-core coupling; it does not by itself prove `BQSP102870`.
