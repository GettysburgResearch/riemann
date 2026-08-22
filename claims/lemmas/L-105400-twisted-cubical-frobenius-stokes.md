# L-105400 — The native Euler source is an exact twisted cubical corner boundary

Claim ID: `L-105400`  
Status: **PROVED EXACT FINITE SOURCE-FUNCTOR THEOREM**  
Created: 2026-08-23  
Depends on: programme PR #727 only  
RH status: **not assumed**

Let `E` be a finite multiset of labelled prime occurrences. Repeated labels,
including the second copy of `67`, remain distinct. Put

\[
\lambda_e=\log p_e,\qquad r_e=e^{-\lambda_e/2}=p_e^{-1/2},
\]

and on functions of logarithmic scale define

\[
(S_a f)(t)=f(t-a),\qquad \Gamma_e=r_eS_{\lambda_e},
\qquad \mathcal E_E=\prod_{e\in E}(I-\Gamma_e).
\]

Let \(D=d/dt\) and \(L=D+\tfrac12\).

## 1. One-prime twisted Stokes identity

For every locally absolutely continuous \(f\),

\[
\boxed{
(I-r_eS_{\lambda_e})f(t)
=
\int_0^{\lambda_e}e^{-u/2}
\,L f(t-u)\,du .
}
\tag{L-105400.1}
\]

Indeed,

\[
\frac d{du}\left(e^{-u/2}f(t-u)\right)
=
-e^{-u/2}Lf(t-u),
\]

and the fundamental theorem of calculus gives the display.

## 2. Exact finite native source

If \(m=|E|\) and \(f\) has the required local weak derivatives, iteration and
Fubini give

\[
\boxed{
\mathcal E_E f(t)
=
\int_{\prod_{e\in E}[0,\lambda_e]}
e^{-\frac12\sum_eu_e}
L^m f\!\left(t-\sum_eu_e\right)
\prod_e du_e .
}
\tag{L-105400.2}
\]

No coefficient has changed. Expanding the left side gives every labelled
squarefree corner once with coefficient

\[
(-1)^{|A|}\prod_{e\in A}p_e^{-1/2}.
\]

Thus the native Euler source is the twisted iterated corner boundary of the
prime box, not a completion, squared source, or positive-child surrogate.

## 3. Activation is a section, not a change of source

If \(f(t)=0\) for \(t<0\), the integrand in (L-105400.2) is supported on

\[
\sum_eu_e\le t.
\]

Hence the physical cutoff is precisely the tropical section of the fixed box.
The source is formed first, activation is imposed second, and physical collapse
is performed last. Duplicate labels remain separate until that final map.

## 4. Geometric owner shellings

For an ordering \(e_1<\cdots<e_m\),

\[
I-\mathcal E_E
=
\sum_{i=1}^m
\Gamma_{e_i}\prod_{h<i}(I-\Gamma_{e_h})
=
\sum_{i=1}^m
\Gamma_{e_i}\prod_{h>i}(I-\Gamma_{e_h}).
\tag{L-105400.3}
\]

These are the least-owner and greatest-owner shellings of the same twisted
corner boundary. Their common refinement is indexed by the least and greatest
selected labels. It is therefore a boundary-stratum identity, not two
different arithmetic sources.

## 5. Completion tangent as a divisor-valued current

For the completion path of PR #719,

\[
E_\tau=A_{1-\tau}E,\qquad
A_c=\prod_{e\in E}(I+cr_eU_e),
\]

one has

\[
\boxed{
\Sigma_\tau=-\partial_\tau E_\tau
=
\sum_{e\in E}
r_eU_eA_{1-\tau,\ne e}E .
}
\tag{L-105400.4}
\]

Thus the tangent is canonically one labelled coefficient per prime divisor.
This is the exact degree-one object used in `L-105401`.

## Scope

The theorem supplies the finite native \(\mathbf F_1\)-type source functor and
its activation/owner compatibility. It does not claim positivity of
\(L^m f\), a cofinal trace estimate, or RH.
