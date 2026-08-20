# L-99721 — The free labelled first-owner energy has polylogarithmic size

Claim ID: `L-99721`  
Status: **PROVED EXACT FINITE BOUND**  
Created: 2026-08-20  
Depends on: `L-99720`  
RH status: **not assumed**

Work in the free labelled subset-source space with the root atom of norm one. Then

\[
\left\|\prod_{h>i}(I-r_hU_h)f\right\|^2=\prod_{h>i}(1+r_h^2),
\]

and the two owner labels in `(I-U_i)g` are orthogonal, so

\[
\|(I-U_i)g\|^2=2\|g\|^2.
\]

With `lambda_i=r_i s_{i-1}`, the unweighted first-owner current energy is

\[
\mathcal E_{\rm owner}=
\sum_{i=1}^{k}2\lambda_i^2\prod_{h>i}(1+r_h^2).
\]

Since `s_{i-1}<=1`,

\[
\lambda_i^2\le r_i^2.
\]

The reverse telescoping identity

\[
\sum_{i=1}^{k}r_i^2\prod_{h>i}(1+r_h^2)
=\prod_{i=1}^{k}(1+r_i^2)-1
\]

gives

\[
\boxed{
\mathcal E_{\rm owner}
\le2\left[\prod_{i=1}^{k}(1+r_i^2)-1\right].
}
\tag{L-99721.1}
\]

For rough primes, `r_i^2=1/p_i`, hence

\[
\mathcal E_{\rm owner}
\le2\left[\prod_{p\in\mathcal P}\left(1+\frac1p\right)-1\right]
\le2\left[\prod_{p\in\mathcal P}\left(1-\frac1p\right)^{-1}-1\right].
\tag{L-99721.2}
\]

Standard partial Euler-product bounds make this polylogarithmic in the largest active scale. No branch-count, leaf-count, or absolute Möbius mass appears.
