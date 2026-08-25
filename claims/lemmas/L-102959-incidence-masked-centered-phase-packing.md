# L-102959 — Centered phase packing is stable under arbitrary source-incidence masks

Claim ID: `L-102959`  
Status: **PROVED UNCONDITIONAL MASKED HILBERT-VALUED PHASE THEOREM**  
Created: 2026-08-25  
Depends on: `L-102882--L-102883`; `L-102956`  
RH status: **not assumed**

Let \((c_n)\) be a finitely supported sequence in a complex Hilbert space with

\[
1\le n\le Z.
\]

The purpose of this theorem is to retain owner, discrepancy, gcd, shell, or Boolean-incidence conditions as literal diagonal masks on the physical integer sequence.

## 1. One prime family

Let \(\mathcal P\subset[L,2L)\) be a finite prime family. For each \(\ell\in\mathcal P\), let

\[
m_\ell:\{1,\ldots,Z\}\to\mathbf C,
\qquad |m_\ell(n)|\le1.
\]

Put

\[
S_{\ell,h}
=
\sum_n m_\ell(n)c_n e_\ell(hn),
\qquad1\le h<\ell.
\]

Then exact nonzero-phase orthogonality gives

\[
\boxed{
\begin{aligned}
\mathcal E_m
&:=
\sum_{\ell\in\mathcal P}{1\over\ell}
\sum_{h=1}^{\ell-1}\|S_{\ell,h}\|^2\\
&=
\sum_{n,r}\langle c_n,c_r\rangle
\sum_{\ell\in\mathcal P}
 m_\ell(n)\overline{m_\ell(r)}
\left(\mathbf1_{\ell\mid n-r}-{1\over\ell}\right).
\end{aligned}
}
\tag{L-102959.1}
\]

Put

\[
M_1=\sum_n\|c_n\|,
\qquad
M_2^2=\sum_n\|c_n\|^2.
\]

For \(n=r\), the masked kernel has modulus at most \(\#\mathcal P\). For \(n\ne r\), the mask has modulus at most one and the number of primes in \([L,2L)\) dividing \(n-r\) is at most \(\log(2Z)/\log(2L)\). Hence

\[
\boxed{
\mathcal E_m
\ll
{L\over\log(2L)}M_2^2
+
M_1^2
\left(1+{\log(2Z)\over\log(2L)}\right).
}
\tag{L-102959.2}
\]

The bound is uniform in the complete family of masks.

## 2. Two prime families

Let \(\mathcal P_i\subset[L_i,2L_i)\), and let

\[
m_{\ell_1,\ell_2}(n)
\]

be arbitrary complex masks of modulus at most one. Define

\[
S_{\ell_1,\ell_2;h_1,h_2}
=
\sum_n m_{\ell_1,\ell_2}(n)c_n
 e_{\ell_1}(h_1n)e_{\ell_2}(h_2n).
\]

Then

\[
\boxed{
\begin{aligned}
\mathcal E_{12,m}
&:=
\sum_{\ell_1\in\mathcal P_1}
\sum_{\ell_2\in\mathcal P_2}
{1\over\ell_1\ell_2}
\sum_{h_1=1}^{\ell_1-1}
\sum_{h_2=1}^{\ell_2-1}
\|S_{\ell_1,\ell_2;h_1,h_2}\|^2\\
&\ll
{L_1L_2\over\log(2L_1)\log(2L_2)}M_2^2\\
&\qquad+
M_1^2
\prod_{i=1}^2
\left(1+{\log(2Z)\over\log(2L_i)}\right).
\end{aligned}
}
\tag{L-102959.3}
\]

The same conclusion holds for one family with the diagonal \(\ell_1=\ell_2\) deleted.

## 3. Source-incidence application

The masks may be chosen to encode, separately or jointly:

```text
minimum-owner identity;
co-owner octave;
largest internal discrepancy prime;
Boolean factorization support;
marked-67 status;
clean owner/core incidence;
common-gcd and renewal strata;
source-owned terminal or shell labels.
```

Thus inserting the literal source-incidence assignment into the **physical-product** centered phase transform creates no new divisor-count or phase-cardinality loss. The only quantities left to establish are the source-specific \(M_1,M_2\) bounds after all literal owner weights are allocated once.

## Scope

This theorem closes the mask-versus-physical-phase noncommutation at the analytic kernel level. It does not prove that the selector-tied Boolean source has subpower \(M_1\), nor does it justify spending an owner weight in two different Cauchy steps.