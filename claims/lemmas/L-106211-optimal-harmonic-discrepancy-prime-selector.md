# L-106211 — Optimal harmonic discrepancy-prime selector

Claim ID: `L-106211`  
Programme aliases: `LFAM1.HARMONIC_DISCREPANCY_SELECTOR`, `LFAM2.ONE_PHASE_EXPONENTIAL_RACE`, `STRESS.OPTIMAL_SOURCE_PHASE_ALLOCATION`  
Status: **PROVED EXACT SOURCE SELECTOR AND SHARP ATOMIC COST**  
Created: 2026-08-26  
Depends on: prime Ramanujan orthogonality and the clean incidence partition  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let \(N\ne M\) be one clean physical interaction after common-core extraction.
Let \(\Delta(N,M)\) be the nonempty set of **distinct numerical prime
moduli** dividing exactly one of \(N,M\). Repeated labelled copies of the same
prime—most importantly the two marked copies of \(67\)—are combined before the
selector is formed. They may not be counted as independent phase directions.

For \(p\in\Delta\), define

\[
a_p=\frac1{p-1},
\qquad
H_\Delta=\sum_{q\in\Delta}\frac1{q-1},
\qquad
w_p=\frac{a_p}{H_\Delta}.
\tag{L-106211.1}
\]

Because

\[
-\sum_{h=1}^{p-1}e_p(h(N-M))=1
\]

for every \(p\in\Delta\), and \(\sum_pw_p=1\),

\[
\boxed{
1
=
-\sum_{p\in\Delta}
w_p\sum_{h=1}^{p-1}e_p(h(N-M)).
}
\tag{L-106211.2}
\]

This is a one-phase identity. It does not multiply two complete phase
families and therefore does not create the bilateral
\((\ell-1)(\rho-1)\) atomic factor corrected on the live branch.

## 1. Sharp atomic normalization

For a scalar or Hilbert atom \(z\), the squared phase cost is

\[
\sum_{p\in\Delta}(p-1)w_p^2\|z\|^2
=
\boxed{
\frac{\|z\|^2}{H_\Delta}.
}
\tag{L-106211.3}
\]

For arbitrary complex \(u_p\) with \(\sum_pu_p=1\),

\[
1
\le
\left(\sum_p(p-1)|u_p|^2\right)
\left(\sum_p\frac1{p-1}\right),
\]

so (L-106211.3) is the unique minimum.

If \(\ell<\rho\) are the two smallest discrepancy primes, then

\[
\boxed{
H_\Delta^{-1}
\le
\frac{(\ell-1)(\rho-1)}{\ell+\rho-2}
<
\ell-1.
}
\tag{L-106211.4}
\]

The selector is atomically cheaper than the deterministic least-prime
allocation and dramatically cheaper than a bilateral product frame.

## 2. One global random ordering

Give every distinct numerical prime modulus \(p\) an independent exponential
clock of rate
\(a_p=1/(p-1)\). Then

\[
\boxed{
\mathbb P\!\left(p
\text{ is the first clock in }\Delta\right)
=
\frac{a_p}{\sum_{q\in\Delta}a_q}
=
w_p.
}
\tag{L-106211.5}
\]

Thus the selector is the expectation of one global random prime ordering.
It is not a pair-adaptive choice of modulus made after observing a
hypothetical bad term. A repeated labelled prime uses the same clock and the
same phase coordinate; splitting it into independent clocks would be a false
source-multiplicity gain.

## Scope

The theorem solves coefficientwise phase selection and the atomic
normalization. The global sum still requires a martingale, signed
dispersion, or trace theorem before the selector fibres are squared.
