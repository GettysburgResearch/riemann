# Moving-centre Poisson–Bézout attack

Date: 2026-08-23  
Branch: `research/gpt56-pro/105200-xi-residue-geometry`  
Status: proposed continuation; RH unproved

## Selection after repository resynchronization

The integrated main release and PRs #720, #723, #724, #726, #729 and #730
were compared before extending PR #728. The strongest compatible assets are:

- PR #723: exact finite-window/confluent selectors, shell averaging and Cartan
  collars;
- PR #724: unconditional exterior-square Xi Gram and residue near-collision
  energy;
- PR #726: summable high-derivative coherence tail;
- PR #729: finite quotient-algebra residue spectrum.

The unresolved interface is fixed-low-order, moving-height control of the
actual real residue moments.

## New coordinate

The positive multipole localizer

\[
\Omega_a(x)=
\frac{36}{((x-a)^2+1)((x-a)^2+4)((x-a)^2+9)}
\]

turns all three moments into value-only evaluations at `a+i`, `a+2i`,
`a+3i`. The safe-line main terms have normalized coherence
`1+O(log^-2|a|)`, and the unnormalized defect is `O(log^-4|a|)`.

A weighted integrality lemma shows that a defect-to-second-moment ratio below
`9/25` removes every wrong extremum in the unit interval centered at `a`.
The exact real/nonreal/debt identity isolates the single signed correction
combination that must be `o(log^-3|a|)`.

## Additional unconditional input

The standard positive theta kernel gives a common nonzero anchor `-i` for
every Xi derivative and the explicit fixed-order disk bound

\[
|\Xi^{(m)}(z)|
\le
4\pi^2m!\zeta(3/2)\pi^{-q/2}\Gamma(q/2),
\qquad
q=|\Im z|+11/2.
\]

This closes the common-anchor and generic disk-growth inputs in the latest
PR #723 Cartan handoff.

## Exact frontier

The new conclusion-facing statement is `MCRC105220`, the uniform signed
moving-centre correction estimate. It must be combined with an
entire/confluent passage and the compact finite-height endpoint/winding ledger.
The quartic firewall proves that the uncorrected safe-line coherence cannot
replace this theorem.

No RH claim is made.
