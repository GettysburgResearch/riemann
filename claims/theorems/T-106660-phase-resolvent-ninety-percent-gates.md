# T-106660 — Optimized-phase and resolvent scalar gates for more than ninety percent

Claim ID: `T-106660`  
Status: **UNCONDITIONAL EXACT SCALAR REDUCTIONS + ONE XI ESTIMATE OPEN**  
Created: 2026-08-26  
Depends on: `T-106590`, `T-106620`, `T-106650`, `L-106660--L-106661`; pinned
\(R_5/N>997/1000-o(1)\) input  
RH status: **unproved**

Retain the mesoscopic frozen Riemann--Siegel packets \(U_{5,j}\) and the
height split at

\[
\eta=\frac1{100}.
\]

The complete deep denominator charge has already been paid by

\[
\left(\frac3{40}+o(1)\right)N(T,2T).
\]

Let \(B_{-,j}^{\rm sh}\) be the reduced shallow denominator factor, let

\[
m_j=\deg B_{-,j}^{\rm sh},
\]

and let \(\mathcal C_{j,\rm sh}\) be its exact canonical-correlation defect
against the complete numerator factor.

## 1. One complex scalar per block

Let \(B_{+,j}\) be the complete reduced numerator inner factor and define
the derived shallow all-pass symbol

\[
U_{5,j}^{\rm sh}
=
\omega_{0,j}B_{+,j}\overline{B_{-,j}^{\rm sh}}.
\]

Put

\[
\Delta_j^{\rm sh}
=
\frac1{2\pi}
\int_{\mathbb R}
\beta_{-,j}^{\rm sh\,\prime}(t)U_{5,j}^{\rm sh}(t)\,dt.
\tag{T-106660.1}
\]

`L-106660` gives the exact domination

\[
\boxed{
\mathcal C_{j,\rm sh}
\le
m_j-|\Delta_j^{\rm sh}|.
}
\tag{T-106660.2}
\]

Equivalently,

\[
m_j-|\Delta_j^{\rm sh}|
=
\min_{\theta\in\mathbb R}
\frac1{4\pi}
\int
\beta_{-,j}^{\rm sh\,\prime}(t)
|1-e^{i\theta}U_{5,j}^{\rm sh}(t)|^2\,dt.
\tag{T-106660.3}
\]

The complete carrier-free arithmetic cross-ratio

\[
U_{5,j}
=
\frac{R_{0,j}C_{5,j}}{C_{0,j}R_{5,j}}
\]

determines \(B_{+,j}\), \(B_{-,j}^{\rm sh}\), and hence this one complex
scalar on every subwindow. The deep co-analytic factor is omitted here
because its charge has already been paid by the height split.

Define `MESOPHASE106660` by

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\displaystyle
\sum_j\left(m_j-|\Delta_j^{\rm sh}|\right)
+\mathcal E_{\rm meso,reg}(T)
}{
N(T,2T)
}
<
\frac{11}{500}.
}
\tag{T-106660.4}
\]

Then

\[
\boxed{
\mathrm{MESOPHASE}_{106660}
\Longrightarrow
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-106660.5}
\]

This scalar gate is stronger than the exact canonical gate but strictly weaker
than using the unrotated phase mean block by block.

## 2. Rational resolvent gate

Choose any predeclared positive numbers \(\tau_j\). Let \(G_j\) be the
confluent denominator Cauchy Gram and let \(D_j\) be the complete numerator
value/jet matrix of `L-106650`. Put

\[
H_j=D_j^*G_jD_j
\]

and

\[
\mathcal Q_j
=
(1+\tau_j)
\operatorname{tr}
\left[
H_j(G_j+\tau_jH_j)^{-1}
\right].
\tag{T-106660.6}
\]

By `L-106661`,

\[
\boxed{
\mathcal C_{j,\rm sh}\le\mathcal Q_j.
}
\tag{T-106660.7}
\]

Therefore the condition

\[
\boxed{
\limsup_{T\to\infty}
\frac{
\sum_j\mathcal Q_j+\mathcal E_{\rm meso,reg}(T)
}{
N(T,2T)
}
<
\frac{11}{500}
}
\tag{T-106660.8}
\]

also implies (T-106660.5). This is `MESORES106660`.

The regularized determinant

\[
\mathcal P_j
=
\frac{
\log\det(G_j+\tau_jH_j)-\log\det G_j
}{
\log(1+\tau_j)
}
\tag{T-106660.9}
\]

may replace \(\mathcal Q_j\) throughout. This is `MESODET106660`.

## 3. Relation to the preceding fronts

The exact hierarchy is now

```text
canonical shallow charge
    = primal Cauchy minimum                         T-106630
    = value sum + nonnormality                      T-106650
   <= optimized cross-trace scalar                  L-106660
   <= unrotated denominator phase mean              L-106514

canonical shallow charge
   <= rational resolvent scalar                     L-106661
   <= explicit finite matrix certificate.
```

The optimized phase route removes every free transport matrix, every explicit
frame constant, and the separate nonnormality ledger. The resolvent route
retains the complete geometry but packages it into one positive inverse or
determinant scalar.

## 4. Boundary

No favorable Xi estimate in (T-106660.4), (T-106660.8), or (T-106660.9) has
been proved. In particular:

```text
stale phase-mean equality in L-106611             CORRECTED
phase optimization and exact slack                PROVED
rational resolvent completion                      PROVED
MESOPHASE106660 / MESORES106660 / MESODET106660   OPEN / 90%-BEARING
ninety percent                                     UNPROVED
density one / RH                                   UNPROVED
```

The theorem is a stricter and more auditable scalar reduction. It is not a
claim that ninety percent has been established.
