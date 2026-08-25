# L-106621 — Constant-scale companion height closes without Rouché rates

Claim ID: `L-106621`  
Status: **PROVED FROM FINITE RANK-ONE HEIGHT MAJORIZATION AND PINNED ZERO INPUTS**  
Created: 2026-08-26  
Depends on: `L-106503`, `T-106590`, `L-106620`  
RH status: **not assumed**

Retain the mesoscopic partition and constants \(\lambda_j\) of `L-106620`.
On each regular finite canonical-product window put

\[
D_j
=
(\Xi+i\lambda_j\Xi')
(\Xi^{(5)}-i\lambda_j\Xi^{(6)})
\]

and reduce common factors.

## 1. Finite companion-height estimate

For a polynomial \(p\), `L-106503` gives

\[
\mathfrak h_+(p+i\lambda p')\le\mathfrak h_+(p),
\]

\[
\mathfrak h_+(p-i\lambda p')
\le\mathfrak h_+(p)+\lambda\deg p.
\]

Applying these two orientations to the endpoint factors yields

\[
\boxed{
\mathfrak h_+(D_j^{\rm red})
\le
\mathfrak h_+(\Xi;I_j)
+\mathfrak h_+(\Xi^{(5)};I_j)
+\lambda_j N_{5,j}
+\mathcal E_{j,\rm end}.
}
\tag{L-106621.1}
\]

Common-factor reduction only decreases the left side.

## 2. Summation over the dyadic window

The functional-equation/Selberg layer cake gives

\[
\sum_j\mathfrak h_+(\Xi;I_j)=O(T)=o(N(T,2T)).
\]

The pinned fifth-derivative proportion and the centered half-strip bound give

\[
\sum_j\mathfrak h_+(\Xi^{(5)};I_j)
\le
\left(\frac3{4000}+o(1)\right)N(T,2T).
\]

Moreover \(\lambda_j\ll1/\log T\) and

\[
\sum_jN_{5,j}=N(T,2T)+o(N),
\]

so

\[
\sum_j\lambda_jN_{5,j}
=O\!\left(\frac{N}{\log T}\right)
=O(T)
=o(N).
\]

Since \(J_T=(\log T)^{O(1)}\), regular subwindow boundaries and collars also
contribute \(o(N)\). Therefore

\[
\boxed{
\sum_j\mathfrak h_+(D_j^{\rm red})
\le
\left(\frac3{4000}+o(1)\right)N(T,2T).
}
\tag{L-106621.2}
\]

This is a quantitative height theorem for the mesoscopic frozen gauge. It
does not require the unknown Rouché threshold of `R-106620`.

## 3. Deep model-space payment

At the fixed pole-height cutoff \(\eta=1/100\), the orthogonal model-space
split gives

\[
\boxed{
\sum_j\mathcal C_{j,>1/100}
\le
\left(\frac3{40}+o(1)\right)N(T,2T).
}
\tag{L-106621.3}
\]

Only the shallow canonical-correlation defect of the explicit frozen-gauge
cross-ratios remains.
