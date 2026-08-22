# L-104523 — Residue moments, phase bias and the critical-extrema interface

Claim ID: `L-104523`  
Status: **PROVED EXACT INTERFACE**  
Created: 2026-08-22  
Depends on: `L-104502`, `L-104510`, `L-104522`  
RH status: **not assumed**

Let

\[
F_k=F^{(k)},
\qquad
E_{k-1,\lambda}=F_{k-1}-i\lambda F_k,
\qquad \lambda>0.
\]

At a simple real zero `c` of `F_k`, put

\[
\rho_c={F_{k-1}(c)\over F_{k+1}(c)}.
\]

## 1. Residue and phase-velocity dictionary

At `c`,

\[
E_{k-1,\lambda}(c)=F_{k-1}(c),
\qquad
E_{k-1,\lambda}'(c)=-i\lambda F_{k+1}(c).
\]

Therefore

\[
\boxed{
{d\over dt}\arg E_{k-1,\lambda}(t)\bigg|_{t=c}
=-{\lambda\over\rho_c}.
}
\tag{L-104523.1}
\]

Thus:

```text
rho_c < 0  <=> positive Hermite--Biehler phase crossing <=> good extremum;
rho_c > 0  <=> negative Hermite--Biehler phase crossing <=> wrong extremum.
```

The coherence statistic of `L-104522` is therefore an inverse-phase-velocity
coherence statistic.  It measures whether the real-axis crossings share one
common positive orientation carrier or are dominated by incoherent reversals.

## 2. Discrete residue moments are local contour observables

Let `D_c` be pairwise disjoint small positively oriented circles, each
containing exactly one simple real zero `c` of `F_k` and no zero of
`F_(k+1)`. Then

\[
\boxed{
\rho_c
={1\over2\pi i}
\int_{\partial D_c}
{F_{k-1}(z)\over F_k(z)}\,dz.
}
\tag{L-104523.2}
\]

Moreover, since

\[
{F_{k+1}\over F_k}
\left({F_{k-1}\over F_{k+1}}\right)^2
={F_{k-1}^2\over F_kF_{k+1}},
\]

the residue at `c` is `rho_c^2`, and hence

\[
\boxed{
\rho_c^2
={1\over2\pi i}
\int_{\partial D_c}
{F_{k-1}(z)^2\over F_k(z)F_{k+1}(z)}\,dz.
}
\tag{L-104523.3}
\]

Summing the local circles gives exact contour representations of the two
moments entering `L-104522`.  The circles are essential: a large global contour
also encloses the poles at zeros of `F_(k+1)` and requires their explicit
subtraction.

## 3. Xi critical-extrema moments

For `F_k=Xi^(k)`, define on a regular height interval

\[
\mathcal M_{1,k}(T)
=-\sum_{\substack{|c|<T\\F_k(c)=0}}
{F_{k-1}(c)\over F_{k+1}(c)},
\]

\[
\mathcal M_{2,k}(T)
=\sum_{\substack{|c|<T\\F_k(c)=0}}
\left|{F_{k-1}(c)\over F_{k+1}(c)}\right|^2,
\]

where the sums run over simple real zeros and common-zero events are retained
in a separate multiplicity ledger.

Put

\[
\boxed{
\mathfrak C_k(T)
={\mathcal M_{1,k}(T)_+^2
 \over R_k(T)\mathcal M_{2,k}(T)}.
}
\tag{L-104523.4}
\]

Then `L-104522` says that `mathfrak C_k(T)>1/2` is exactly the threshold at
which the derivative line-zero count yields a positive proportion at the
preceding derivative.

## 4. Mean-value formulation

A sufficient asymptotic input is the pair of estimates

\[
\mathcal M_{1,k}(T)
\ge \mu_k R_k(T)(1+o(1)),
\]

\[
\mathcal M_{2,k}(T)
\le \nu_k R_k(T)(1+o(1)),
\]

with

\[
\boxed{
\mu_k^2>{\nu_k\over2}.
}
\tag{L-104523.5}
\]

Then

\[
\mathfrak C_k(T)
\ge {\mu_k^2\over\nu_k}+o(1)
>{1\over2}+o(1),
\]

and the explicit transfer constant is

\[
\boxed{
c_k={2\mu_k^2\over\nu_k}-1>0.
}
\tag{L-104523.6}
\]

This is a discrete mean-value problem at the real critical points of the actual
Xi derivative.  It is structurally aligned with the Conrey--Ghosh relative-
extrema programme, but it asks for signed inverse-curvature moments rather than
a global percentage or an unsigned value moment.

## 5. Why this is noncircular

`mathcal M_1` and `mathcal M_2` are defined entirely from the values of
`Xi^(k-1), Xi^(k), Xi^(k+1)` at the **already assumed real zeros of Xi^(k)**.
They do not count the unknown real zeros of `Xi^(k-1)` and do not contain the
parent line proportion as a hidden term.

The implication

```text
line proportion p at level k
+ residue coherence C>1/2
-> line proportion (2C-1)p at level k-1
```

is therefore a genuine two-input theorem.

## 6. Immediate analytic routes

Two concrete attacks remain:

1. **Mollified critical-point moments.** Evaluate `M_1` and `M_2` through
   small-contour residues and mollified mean values of adjacent Xi derivatives.
2. **Phase-velocity sampling.** Use (L-104523.1) and a source-qualified
   Voorhoeve/Pick estimate to control the first two inverse phase-velocity
   moments at real crossings.

No all-order Pick positivity or RH input is assumed.
