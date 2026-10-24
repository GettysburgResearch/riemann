# Second pass: signed diagonal cancellation and quartic moments

Date: 23 October 2026.

**Status: proposed component mathematics. No smaller global zero-free
half-plane is proved in this directory.** The inherited, externally
source-qualified benchmark remains
`B_flat = 0.874886647039964...`, from
[Liu, arXiv:2610.26835v1, Theorem 17.1](https://arxiv.org/html/2610.26835v1).
This packet does not independently certify that preprint or the complete
OpenAI quasi-Riemann-hypothesis argument.

This is an additive second pass after PR #1020's first mathematical
freeze, `c4332e23826a6c36b86e4f64cbde6cc1a0f641a0`, and its review commit,
`f90384d57777ea94897542807b577e5b2e502372`. The earlier files and review
remain unchanged. A separate exact-commit review accompanies this pass.

## 1. A cancellation with the finite cutoff retained

[SIGNED_SQUARE_CLASS_DIAGONAL.md](SIGNED_SQUARE_CLASS_DIAGONAL.md) treats
the square-class part of the reflected, signed inverse expression in the
basic `C=d'=j=1` component, for good squarefree reflected rows and
fixed punctures only. The diagonal
is defined after retaining the common cutoff from the original completed
columns. It is not identified with the whole inverse moment.

Under the stated fixed Dedekind-zeta reciprocal bound at a boundary
`beta>2/3`, its physical contribution is bounded by

\[
 \bigl(D^{1-3\delta}H^{2\delta}+D^\beta\bigr)(DH)^\epsilon,
 \qquad 0<\delta<1/5.
\]

The mechanism is explicit. On the common-index residue, the signed
divisor series contains `1/zeta_E(1+tau)`. Its zero cancels the pole at
`tau=0` of the inserted cutoff's Mellin transform. Moving that contour
leaves the finite-boundary contribution `D^beta`. Replacing the cutoff
by an unrestricted Euler product would not justify this conclusion.

For example, `delta=1/7` gives

\[
 D^{4/7}H^{2/7}+D^\beta.
\]

For `beta>=4/5`, this component fits an `H` bound once
`H>=D^(beta+c)`, with an arbitrary fixed positive gap `c` and appropriately
small losses. The fixed-cusp identities needed to keep the common signed
variable untwisted are proved in
[FIXED_CUSP_REINDEXING.md](FIXED_CUSP_REINDEXING.md).

**Remaining requirements:** the nonsquare correlations of this same
cutoff-retained expression, and the powerful-row/overlap/puncture
reassembly outside the stated component. Neither is supplied by the
convergent scale sums alone. The `K+N` quadratic large-sieve estimate has
an operator contribution of size `N`; canceling a diagonal does not
delete that contribution.

## 2. A positive quartic mean, with its exact numerator

[POSITIVE_PRIMITIVE_ANGULAR_M2.md](POSITIVE_PRIMITIVE_ANGULAR_M2.md) proves
the fixed-angular, fixed-level bound

\[
 \sum_{0<Nk\le K}|\psi(k,\sigma+it;\xi,v)|^2
 \ll (1+|t|)^A K,
 \qquad \sigma\ge1+\delta,\quad \xi=\alpha^{\pm1},
\]

uniformly on fixed compact real strips. A Dirac resolvent estimate,
two components of one Fourier column, and a Bessel Wronskian give
polynomial spectral-height control. Exact local completion then gives
the squarefree-column mean `K^(1+epsilon)`, including all numerator
valuations. External punctures have the explicit additional cost

\[
 (NQ)^\epsilon\sum_{f\mid Q}(Nf)^{3-2\sigma}.
\]

The source is **DDHL v5**, whose Fourier formula already has the correct
matrix order `K Phi`. This packet makes no new-erratum claim about that
version. The older reversed-order formula must not be used to infer that
the two Bessel components have different arithmetic coefficients.

The direct quartic inverse nevertheless needs `psi(k^3)`, because

\[
 \mu(c)\gamma_4(c)\overline{\chi_c(k)}
 =\alpha(c)\overline{g_4(k^3,c)/\sqrt{Nc}}.
\]

Positivity only transfers the displayed mean to a cutoff of size `K^3`.
At `K=D^2/H`, that would give `D^5/H^2`, which does not improve the
required inverse estimate. The needed sparse cube-indexed mean is not
proved here.

## 3. What a completed inverse estimate would deliver

[FULL_INVERSE_CONSUMER.md](FULL_INVERSE_CONSUMER.md) gives the precise
implication from a **full**, all-row sextic inverse bound valid for
`H>=D^(a+c)` to a zero-free boundary

\[
 B_{\rm new}=\frac12+\frac{5a}{12}.
\]

If the missing estimates supplied `a=7/8`, this would give `83/96`.
If they supplied `a=B_flat`, it would give approximately
`0.864536102933318`. These are conditional targets, not results of the
diagonal estimate. Iteration to `6/7` requires the full implication for
every fixed finite-order coefficient character, not just the principal
member.

## 4. Checks and review scope

- `check_signed_reflection_local.py` checks the exact local paired Euler
  identities and residue table used by the signed-diagonal calculation.
- `check_positive_angular.py` checks cleared Dirac matrix identities,
  Bessel-column algebra, and the primitive-completion exponents.
- `check_quartic_orientation.py` computes finite Gauss sums exactly in
  `Z[i][zeta_p]`. It checks both quartic orientations and every row in
  eleven prime fields, and produces counterexamples to the incorrect
  first-power numerator transfer.

Their saved reports describe finite coverage. They do not certify
analytic continuation, imported theorems, the remaining correlations,
or a better global zero-free bound. Independent agent review is recorded
separately from these finite checks and is not external peer review or
formal proof verification.
