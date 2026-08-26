# T-106650 — Mesoscopic value–nonnormality gates for more than ninety percent

Claim ID: `T-106650`  
Status: **UNCONDITIONAL EXACT REPARAMETRIZATION + ONE EXPLICIT XI ESTIMATE OPEN**  
Created: 2026-08-26  
Depends on: `T-106630`, `L-106650--L-106651`; pinned
\(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

Retain the mesoscopic Riemann--Siegel packet of `T-106620/T-106630`.  On
subwindow \(I_j\), let

\[
B_{-,j}^{\rm sh}
\]

be the reduced shallow denominator inner factor at height at most \(1/100\).
Choose any source-owned numerator inner subfactor

\[
A_j\mid B_{+,j}.
\]

Let its shallow denominator zeros be \(b_{j,\nu}\), counted with
multiplicity, and define

\[
\mathfrak N_j
=
\mathfrak N(A_j,B_{-,j}^{\rm sh})
\]

by `L-106650`.

## 1. Exact Schur-value form of the live gate

Inner-factor monotonicity and `L-106650` give

\[
\begin{aligned}
\mathcal C_{j,\rm sh}
&=
\operatorname{tr}\!\left(
P_{K_{B_{-,j}^{\rm sh}}}(I-P_{K_{B_{+,j}}})
\right)\\
&\le
\operatorname{tr}\!\left(
P_{K_{B_{-,j}^{\rm sh}}}(I-P_{K_{A_j}})
\right)\\
&=
\sum_\nu |A_j(b_{j,\nu})|^2+\mathfrak N_j.
\end{aligned}
\tag{T-106650.1}
\]

Define `MESOSCHUR106650` by the existence of source-owned \(A_j\) such that

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\displaystyle
\sum_j\left[
 \sum_\nu |A_j(b_{j,\nu})|^2+\mathfrak N_j
\right]
+\mathcal E_{\rm reg}(T)
}{N(T,2T)}
<
\frac{11}{500}.
}
\tag{T-106650.2}
\]

Then `MESOSCHUR106650` implies `MESOTRANS106630`, because the right side of
(T-106650.1) is the exact full-subspace primal transport minimum for the
selected numerator factor.

The deep denominator charge is already bounded by

\[
\left(\frac3{40}+o(1)\right)N(T,2T).
\]

Since

\[
\frac3{40}+\frac{11}{500}=\frac{97}{1000},
\]

the endpoint index inequality and the pinned fifth-derivative input yield

\[
\boxed{
\mathrm{MESOSCHUR}_{106650}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106650.3}
\]

No arbitrary transport matrix remains in this formulation.  The two open
terms are explicit:

```text
spectral matching:
  sum of products of pseudohyperbolic distances
  |A_j(b_jnu)|^2;

collective geometry:
  Frobenius nonnormality departure N_j of
  A_j(S_(B_-,j^sh)).
```

## 2. A stronger frame-conditioned sufficient gate

Assume the simple shallow denominator Gram \(G_j\) satisfies

\[
\alpha_j I\preceq G_j\preceq\beta_j I.
\]

Put

\[
\kappa_j=\frac{\beta_j}{\alpha_j}.
\]

By `L-106651`,

\[
\mathcal C_{j,\rm sh}
\le
\kappa_j\sum_\nu|A_j(b_{j,\nu})|^2.
\]

Hence the stronger but directly checkable condition

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\displaystyle
\sum_j\kappa_j\sum_\nu|A_j(b_{j,\nu})|^2
+\mathcal E_{\rm reg}(T)
}{N(T,2T)}
<
\frac{11}{500}
}
\tag{T-106650.4}
\]

also implies more than \(90\%\).  One may replace \(\kappa_j\) by the explicit
Gershgorin ratio

\[
\frac{1+r_j}{1-r_j}
\]

whenever the row sum \(r_j<1\).

## 3. What this proves and what it does not

`T-106630` exposed the exact primal Cauchy transport.  The present theorem
removes the free matrix \(X_j\) and identifies the precise obstruction to
pointwise pole matching:

\[
\boxed{
\text{canonical shallow loss}
=
\text{numerator values at denominator companions}
+
\text{compression nonnormality}.
}
\]

The first term is source-owned and multiplicative in the explicit companion
zero coordinates.  The second is the coherent clustering debt hidden by every
unwhitened rank-one argument.

Neither term has yet been bounded for the Xi mesoscopic packet at the required
\(11/500\) scale.  Therefore the theorem is a sharper attack surface, not a
claim of the \(90\%\) conclusion.

```text
exact value--nonnormality decomposition             PROVED
frame-conditioned value upper bound                 PROVED
MESOSCHUR106650 / frame gate                         OPEN / 90%-BEARING
ninety percent                                      UNPROVED
density one / RH                                    UNPROVED
```
