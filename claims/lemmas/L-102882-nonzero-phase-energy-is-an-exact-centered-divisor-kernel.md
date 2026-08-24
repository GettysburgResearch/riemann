# L-102882 — Nonzero phase energy is an exact centered divisor kernel

Claim ID: `L-102882`  
Status: **PROVED EXACT HILBERT-VALUED ORTHOGONALITY THEOREM**  
Created: 2026-08-24  
Depends on: `L-102835--L-102865`  
RH status: **not assumed**

Let `H` be a complex Hilbert space and let `(c_b)` be a finitely supported `H`-valued sequence.  For a prime `ell` define

\[
S_{\ell,h}=\sum_b c_b e_\ell(hb^2),
\qquad 1\le h<\ell.
\]

Then

\[
\boxed{
\sum_{h=1}^{\ell-1}\|S_{\ell,h}\|_H^2
=
\sum_{b,b'}\langle c_b,c_{b'}\rangle_H
\left[
\ell\,\mathbf1_{b^2\equiv b'^2\ (\ell)}-1
\right].
}
\tag{L-102882.1}
\]

Indeed

\[
\sum_{h=1}^{\ell-1}e_\ell(hd)
=\ell\mathbf1_{\ell\mid d}-1.
\]

The `-1` is the exact subtraction of the principal additive frequency.  Replacing the nonzero phase sum by the all-phase sum deletes this term and can lose the conclusion-facing cancellation.

## 1. Product-modulus form

Let `ell_1,...,ell_j` be distinct primes and put

\[
S_{\mathbf h}
=\sum_b c_b
\prod_{i=1}^j e_{\ell_i}(h_i b^2),
\qquad 1\le h_i<\ell_i.
\]

Repeated use of (L-102882.1) gives

\[
\boxed{
\sum_{\mathbf h}\|S_{\mathbf h}\|_H^2
=
\sum_{b,b'}\langle c_b,c_{b'}\rangle_H
\prod_{i=1}^j
\left[
\ell_i\mathbf1_{b^2\equiv b'^2\ (\ell_i)}-1
\right].
}
\tag{L-102882.2}
\]

For `j=2`, the kernel expands as

\[
\ell_1\ell_2\mathbf1_{L\mid b^2-b'^2}
-\ell_1\mathbf1_{\ell_1\mid b^2-b'^2}
-\ell_2\mathbf1_{\ell_2\mid b^2-b'^2}
+1,
\]

where `L=ell_1 ell_2`.

## 2. Relation to the live phase packets

The phase fields in `L-102836`, `L-102839` and `L-102865` are obtained from (L-102882.2) after multiplying the coefficients by the literal semiprime-owner and square-core weights.  Therefore every fixed- and product-modulus energy on PR #719 has an exact centered form.

The theorem is especially useful for coherent summation over moduli: the zero frequency is subtracted **before** Cauchy, rather than bounded as part of an all-phase diagonal.

## Scope

The centered kernel can have either sign off the diagonal.  Equation (L-102882.2) is an exact normal form, not a positivity theorem.  Its coherent weighted estimate is proved in `L-102883`; transport to the complete owner-pair current still requires the literal source allocation.
