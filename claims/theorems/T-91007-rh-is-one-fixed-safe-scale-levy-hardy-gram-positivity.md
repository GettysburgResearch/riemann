# T-91007 — RH is one fixed safe-scale Lévy–Hardy Gram positivity theorem

Claim ID: `T-91007`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT FIXED-SCALE CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: main `T-91006` (CJHI proposal), `L-91030`, `L-91031`, `L-91032`, `L-91033`, and Suzuki's screw criterion  
RH status: **unproved**

## 1. Statement

Fix one arbitrary scale

\[
 a_0>\frac12.
\]

Let

\[
 \mathfrak I=(\{+,-\}\times\mathbb R)\sqcup\{\star\}.
\]

For `(epsilon,x)`, let `F_(epsilon,x)` be the causal or anti-causal wavelet of
`L-91031` at scale `a_0`; let `F_star=b_(a_0)` be the bridge of `L-91032`.
Define

\[
 \boxed{
 \mathbb K_{a_0}(i,j)=
 \iint G_\zeta(t,u)F_i(t)\overline{F_j(u)}dtdu.
 }
 \tag{T-91007.1}
\]

Then, subject to independent review of the form-core theorem,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_{a_0}\succeq0
 \text{ on every finite subset of }\mathfrak I.
 }
 \tag{T-91007.2}
\]

Any one fixed `a_0>1/2` is complete.  The quantifier over scale is removed.

## 2. RH gives an explicit Lévy Gram

Under RH,

\[
 \nu_\zeta=
 \sum_\gamma\frac{m_\gamma}{\gamma^2}\delta_\gamma
\]

is positive and, for every mean-zero test,

\[
 \mathbb K_{a_0}(i,j)=
 \int\widehat F_i(\lambda)
 \overline{\widehat F_j(\lambda)}d\nu_\zeta(\lambda).
 \tag{T-91007.3}
\]

For the two Hardy families,

\[
 \boxed{
 \mathbb K_{a_0}((\epsilon,x),(\delta,y))=
 \sum_\gamma m_\gamma
 \Psi_{a_0}^\epsilon(\gamma-x)
 \overline{\Psi_{a_0}^\delta(\gamma-y)}.
 }
 \tag{T-91007.4}
\]

The bridge entries arise from the same Gram formula.  Hence every finite
matrix is positive semidefinite.

## 3. Fixed-scale positivity recovers the entire screw form

Assume the right side of (T-91007.2).  Positivity holds on the algebraic span
of the indexed tests.  `L-91032` proves that this span is dense in

\[
 \mathcal H_{\eta,0}
 =\{f\in L^2(e^{\eta|t|}dt):\int f=0\}
\]

for any `1<eta<2a_0`.  The screw form is continuous in that norm, so it is
nonnegative on all of `H_(eta,0)`, in particular on Suzuki's compact smooth
mean-zero test space.  Suzuki's theorem gives RH.

No terminal-pair selection, zero interpolation, Gram inversion, growing
support or cofinal scale hierarchy is used in this implication.

## 4. The previous recurrence is only one diagonal

For the causal diagonal,

\[
 \boxed{
 \mathbb K_{a_0}((+,x),(+,x))
 =a_0^4\mathcal R_x(a_0),
 }
 \tag{T-91007.5}
\]

where `R_x(a)` is the three-square residual in `T-91005`.

Thus the normalized Cauchy recurrence observes only

\[
 \operatorname{diag}\mathbb K_{a_0}.
\]

The cross-carrier, causal/anti-causal and bridge entries are the polarization
needed to recover the complete screw/Weil form.

The radical replacement is

```text
all scale-by-scale scalar gates
    -> one fixed-scale matrix kernel;

terminal-pair isolation
    -> Hardy-Wiener completeness;

moving prime cutoffs and asymptotics
    -> absolutely convergent fixed Euler entries.
```

## 5. Fixed safe-scale prime-side form

Every indexed test is a finite one-sided exponential-polynomial combination
with rates among `a_0,2a_0,4a_0`.  Its Guinand–Weil entry has the form

\[
 \boxed{
 \mathbb K_{a_0}(i,j)=
 \mathbb K_{\Gamma,\mathrm{pole}}(i,j)
 -2\Re\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}\mathcal W_{i,j}(\log n),
 }
 \tag{T-91007.6}
\]

with

\[
 \mathcal W_{i,j}(t)=O_{i,j}(\operatorname{poly}(t)e^{-a_0t}).
\]

Since `a_0>1/2`, the prime series converges absolutely.  Each entry is also a
finite algebraic combination of safe `-zeta'/zeta` derivatives in `Re(s)>1`,
plus explicit rational/polygamma terms.

The remaining sign is therefore the fixed source-explicit domination

\[
 \boxed{
 \mathbb K_{\Gamma,\mathrm{pole}}
 \succeq
 \mathbb K_{\mathrm{prime}}
 }
 \tag{T-91007.7}
\]

on the complete two-Hardy-channel carrier space.

## 6. Completion of main's CJHI target

Main's `T-91006` isolates the Cauchy–Jordan Hardy Intertwiner as the final open
compatibility theorem.  The present stack makes both sides of that proposed
intertwiner explicit:

```text
source environment:
  prime-power compound-Poisson bosonic Fock product system;

source polarization:
  full phase-vector and Wiener-Itô chaos kernels;

output environment:
  causal and anti-causal rational Hardy channels;

output completion:
  one bridge vector;

completed reserve:
  gamma/pole scattering channel.
```

A conclusion-producing proof is the construction of one positive-metric
isometry

\[
 \boxed{
 \mathcal U:
 \mathcal H_{\Gamma,\mathrm{pole}}
 \oplus\Gamma_s(L^2(\nu_a))
 \longrightarrow
 \mathcal H_{\mathrm{Hardy}}\oplus\mathcal E
 }
 \tag{T-91007.8}
\]

whose transfer kernel is `mathbb K_(a_0)`.  If it is constructed,
(T-91007.7) is automatic and RH follows.

Conversely, positivity of `mathbb K_(a_0)` supplies a Kolmogorov/Stinespring
factorization.  Thus this conservative colligation target is exactly sharp,
not a weaker sufficient condition.

## 7. Countable reduction and finite countercertificates

Continuity in the carriers implies rational carriers suffice.  Every finite
entry has an absolutely convergent Euler expression and an elementary tail
bound.  Consequently

\[
 \boxed{
 \neg\mathrm{RH}
 \Longrightarrow
 \begin{array}{c}
 \text{one finite rational carrier/orientation packet},\\
 \text{one finite prime-power cutoff},\\
 \text{one strictly negative directed eigenvalue interval}.
 \end{array}
 }
 \tag{T-91007.9}
\]

No negative Riemann-data matrix is claimed to have been found.

## 8. Exact boundary

Closed, subject to independent review:

```text
one arbitrary fixed safe scale a_0>1/2 is complete;
RH -> explicit Lévy Gram;
fixed-scale Gram PSD -> full Suzuki screw positivity -> RH;
Cauchy residual is one diagonal;
all entries are absolutely Eulerian;
false RH has a finite rational-carrier finite-prime matrix witness;
CJHI reduced to one explicit conservative Poisson-Fock/Hardy colligation.
```

Open:

```text
construction of that completed colligation;
unconditional fixed-scale cross-Gram PSD;
Riemann Hypothesis.
```
