# L-102956 — Centered phase packing holds directly for literal physical products

Claim ID: `L-102956`  
Status: **PROVED UNCONDITIONAL HILBERT-VALUED PHASE THEOREM**  
Created: 2026-08-25  
Depends on: `L-102882--L-102883`  
RH status: **not assumed**

Let `(c_n)` be a finitely supported sequence in a complex Hilbert space, with

\[
1\le n\le Z.
\]

For a prime `ell` and `1<=h<ell`, put

\[
S_{\ell,h}
=
\sum_n c_n e_\ell(hn).
\]

No squareclass representation of `n` is assumed.

## 1. One prime family

Let `P` be a finite prime family contained in

\[
L\le\ell<2L.
\]

Define

\[
\mathcal E_P
=
\sum_{\ell\in P}\frac1\ell
\sum_{h=1}^{\ell-1}
\|S_{\ell,h}\|^2.
\]

Exact additive orthogonality gives

\[
\boxed{
\mathcal E_P
=
\sum_{n,m}
\langle c_n,c_m\rangle
K_P(n-m),
}
\tag{L-102956.1}
\]

where

\[
K_P(d)
=
\sum_{\ell\in P}
\left(
\mathbf1_{\ell\mid d}-\frac1\ell
\right).
\]

Put

\[
M_1=\sum_n\|c_n\|,
\qquad
M_2^2=\sum_n\|c_n\|^2.
\]

For `d=0`,

\[
K_P(0)\le \#P\ll {L\over\log(2L)}.
\]

For `0<|d|<Z`, the number of primes in `P` dividing `d` is at most

\[
\frac{\log(2Z)}{\log(2L)},
\]

and

\[
\sum_{\ell\in P}\frac1\ell\ll\frac1{\log(2L)}.
\]

Therefore

\[
\boxed{
\mathcal E_P
\ll
{L\over\log(2L)}M_2^2
+
M_1^2
\left(
1+{\log(2Z)\over\log(2L)}
\right).
}
\tag{L-102956.2}

## 2. Two prime families

Let `P_1,P_2` lie in dyadic intervals `L_i<=ell<2L_i`. Define

\[
S_{\ell_1,\ell_2;h_1,h_2}
=
\sum_n c_n
 e_{\ell_1}(h_1n)
 e_{\ell_2}(h_2n)
\]

and

\[
\mathcal E_{12}
=
\sum_{\ell_1\in P_1}
\sum_{\ell_2\in P_2}
{1\over\ell_1\ell_2}
\sum_{h_1=1}^{\ell_1-1}
\sum_{h_2=1}^{\ell_2-1}
\|S_{\ell_1,\ell_2;h_1,h_2}\|^2.
\]

Repeated orthogonality gives

\[
\boxed{
\mathcal E_{12}
=
\sum_{n,m}
\langle c_n,c_m\rangle
K_{P_1}(n-m)K_{P_2}(n-m).
}
\tag{L-102956.3}

Consequently

\[
\boxed{
\begin{aligned}
\mathcal E_{12}
\ll{}&
{L_1L_2\over
 \log(2L_1)\log(2L_2)}M_2^2\\
&+
M_1^2
\prod_{i=1}^2
\left(
1+{\log(2Z)\over\log(2L_i)}
\right).
\end{aligned}
}
\tag{L-102956.4}

The same-family off-diagonal sum `ell_1!=ell_2` obeys the same estimate: its
kernel is

\[
K_P(d)^2-
\sum_{\ell\in P}
\left(\mathbf1_{\ell\mid d}-\frac1\ell\right)^2,
\]

and the deleted square has no larger diagonal or divisor-count scale.

## 3. Square-core coefficient corollary

Suppose, after equal-product collapse, the literal physical products carry
coefficients

\[
c_n={d_n\over b\sqrt Q}v_n,
\qquad
B\le b<2B,
\qquad
|d_n|\le Z^{o(1)},
\qquad
\|v_n\|\le1,
\]

with representation multiplicity `Z^(o(1))`. Then

\[
M_1^2\ll {Z^{o(1)}\over Q},
\qquad
M_2^2\ll {Z^{o(1)}\over QB}.
\]

Equations (L-102956.3)--(L-102956.4) give

\[
\boxed{
\mathcal E_{12}
\ll
{Z^{o(1)}\over Q}
\left[
1+{L_1L_2\over
B\log(2L_1)\log(2L_2)}
\right].
}
\tag{L-102956.5}

All additional `log Z` factors are absorbed in `Z^(o(1))`.

## Meaning

The centered phase theorem may be applied **after physical product formation**.
Multipliers such as an owner product inside `n=P b^2` do not have to be erased
or treated as fixed: they are part of the literal integer `n` in
(L-102956.1)--(L-102956.4).

This repairs the scalar-core limitation identified in `R-102875` at the phase
energy level. A separate source-allocation theorem is still required to turn
the minimum-owner cross form into the weighted energy (L-102956.3) with every
owner weight used once.
