# T-5602 — Universal parity obstruction: no smooth zero-statistic has first-order sensitivity to RH failure

Claim ID: T-5602
Title: The off-critical quadruple is invariant under `eta -> -eta`, so every
symmetric functional of the zeros responds evenly, and only non-smooth
(counting) functionals can detect a displacement at first order
Status: PROPOSED
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: the functional equation `xi(s) = xi(1-s)` and the reflection
`zeta(\bar s) = \overline{zeta(s)}`
Scope: every RH criterion expressed as a function of the multiset of nontrivial
zeros
Related counterexample candidates: none — this claim says which *kinds* of
candidate can exist

## Statement

Let `rho_0 = 1/2 + eta + i gamma` with `eta` real and `gamma` real, and let

\[
 \mathcal Q(\eta)=\{\,\rho_0,\;1-\rho_0,\;\overline{\rho_0},\;1-\overline{\rho_0}\,\}
 =\left\{\tfrac12+\eta+i\gamma,\;\tfrac12-\eta-i\gamma,\;
          \tfrac12+\eta-i\gamma,\;\tfrac12-\eta+i\gamma\right\}
\]

be the quadruple that the functional equation and the reflection principle force
to accompany it.  Then

\[
 \boxed{\;\mathcal Q(-\eta)=\mathcal Q(\eta)\quad\text{as multisets.}\;}
\]

Consequently, let `F` be **any** functional of the multiset `Z` of nontrivial
zeros of `zeta` — a linear statistic `sum_rho H(rho)`, a Li coefficient, a Weil
quadratic form, an `n`-level correlation, a determinant, anything at all.  Write
`F(\eta)` for its value when one quadruple sits at displacement `eta` and the
rest of `Z` is held fixed.  Then

\[
 \boxed{\;F(-\eta)=F(\eta)\quad\text{identically.}\;}
\]

In particular, if `F` is differentiable at `eta = 0`,

\[
 \boxed{\;\left.\frac{dF}{d\eta}\right|_{\eta=0}=0 .\;}
\]

**No smooth statistic of the zeros has first-order sensitivity to an
off-critical displacement.**  Detection is at best `O(\eta^2)`, with the
constant given by `\tfrac12 F''(0)`.

## Proof

Reading the four elements of `\mathcal Q(-\eta)` in the order
`(2,1,4,3)` reproduces the four elements of `\mathcal Q(\eta)`:

\[
 \tfrac12-\eta+i\gamma,\;\;\tfrac12+\eta-i\gamma,\;\;
 \tfrac12-\eta-i\gamma,\;\;\tfrac12+\eta+i\gamma .
\]

Multiplicities match because the map is a bijection of the four labels.  Hence
`\mathcal Q(-\eta)` and `\mathcal Q(\eta)` are the same multiset, and any
functional of the multiset takes the same value on both.  Differentiability
then forces the odd part of `F` to vanish, so `F'(0) = 0`. ∎

The two inputs are exactly the two symmetries of `zeta`: `xi(s) = xi(1-s)`
supplies `rho \mapsto 1-rho`, and `zeta(\bar s) = \overline{zeta(s)}` supplies
`rho \mapsto \bar rho`.  Nothing else is used.

## Why this is stronger than L-5604

`L-5604` derived the quadratic response for the D-0801 family and attributed it
to `g` being real on the real axis.  That attribution is correct but not the
root cause: the pairing `h(\gamma+i\eta) + h(\gamma-i\eta)` already kills every
odd order, whether or not `h` is real, and the pairing is present because the
quadruple is.  The obstruction therefore has nothing to do with the test
function, the normalization, the cutoff, or the family.  It is a symmetry of the
zero set.

Concretely, this covers:

| criterion | why it is covered |
|---|---|
| Weil positivity, `D-0001`/`D-0701`/`D-0801` | `sum_rho g(z_rho)` |
| Li coefficients, `lambda_n = sum_rho [1-(1-1/rho)^n]` | `sum_rho H(rho)` |
| any `n`-level density or pair-correlation statistic | symmetric in `Z` |
| `xi`-passivity, matched-pole Pick conditions | determined by `Z` through the Hadamard product |
| Robin's criterion, through its explicit-formula representation | ditto |

## The escape, and it is the only one

The hypothesis that fails for a *zero-counting* functional is
differentiability.  Let

\[
 N_{\rm off}(\sigma)=\#\{\rho\in Z:\ \operatorname{Re}\rho>\sigma\},
 \qquad \sigma>\tfrac12 .
\]

`N_off` is still an even function of `eta` — T-5602 applies — but it is a step
function: it jumps from `0` to `2` the instant `|eta| > \sigma-\tfrac12`.  Its
"sensitivity" is not `O(\eta^2)`; it is infinite in the sense that *any*
nonzero displacement is detected once the contour is placed inside it, and the
detection is exact rather than a small perturbation of a large number.

\[
 \boxed{\;\text{Only non-smooth (counting) functionals of the zeros can detect
 an arbitrarily small off-critical displacement.}\;}
\]

Operationally that means the argument principle: count zeros in a rectangle by
`\frac1{2\pi i}\oint \frac{\xi'}{\xi}`, or count sign changes of the
Riemann–Siegel `Z(t)` on the critical line and compare with `N(t)` via Turing's
method.  A deficit of even one sign change is a proof that RH fails.

This is not a new algorithm — it is how RH has actually been verified
computationally, to height `3.0000175\times10^{12}` by Platt–Trudgian.  What is
new here is the *reason* it is the only game in town, and the quantitative
comparison in the next section.

## The cost comparison the project has never made

| route | work | what it achieves |
|---|---|---|
| D-0801 at `c = 10^{11}` | `4.12\times10^{9}` prime-power terms, 316 s | detects `eta > 3\times10^{-2}` at one carrier (`L-5604`) |
| Riemann–Siegel + Turing at the same height | `\sim\sqrt{T/2\pi}\approx 8.7\times10^{5}` terms per evaluation, a few evaluations per zero | detects **any** `eta > 0`, for every zero in the window |

The explicit-formula route spends about `10^{4}` times more arithmetic to obtain
a test that cannot see anything a real counterexample could plausibly be.  The
asymmetry is structural: the prime sum needs `c \ge T/2\pi` terms merely to
*resolve* individual zeros (C-5601), while Riemann–Siegel needs
`\sqrt{T/2\pi}` per evaluation, a square root fewer.

## Analytic domain audit

- The quadruple is the orbit of `rho_0` under the group generated by
  `s \mapsto 1-s` and `s \mapsto \bar s`; both map nontrivial zeros to
  nontrivial zeros.
- For `eta = 0` the orbit degenerates to `\{1/2+i\gamma, 1/2-i\gamma\}` with
  multiplicity two, and the statement is vacuous but true.
- For `gamma = 0` (a real zero off the line) the orbit degenerates to
  `\{1/2\pm\eta\}`, again `\eta`-even.
- No analyticity, no contour, and no numerical input is used anywhere.

## Gap audit

1. The claim holds "with the rest of `Z` held fixed".  A real failure of RH
   would perturb neighbouring zeros as well, and `F` is a function of the whole
   set; the statement is about the response to one quadruple, which is the
   right linearization but not a scenario.
2. `F(-\eta) = F(\eta)` does **not** say `F` is insensitive — only that its
   sensitivity is even.  A functional with enormous `F''(0)` relative to its
   noise floor would still be an excellent detector.  `L-5604` is where that
   ratio is measured for D-0801, and it is bad; T-5602 explains why no
   reformulation *of that kind* will rescue it.
3. Non-smooth functionals evade the differentiability conclusion but not the
   evenness; that is harmless, since a counting function does not need an odd
   part to be decisive.
4. The cost table compares arithmetic operations, not rigor: a certified
   Riemann–Siegel evaluation needs its own error analysis, and a certified
   Turing bound needs `S(t)` control.  Those are real work, but they are
   `\sqrt{T}`-scale work.
5. Nothing here says RH is true or false, and nothing here excludes a
   counterexample.  It classifies the ways one could be found.

## Adversarial tests

1. Take `F(Z) = \sum_\rho g(z_\rho)` for an explicit `g` and an explicit
   quadruple, and evaluate at `\pm\eta` numerically; the two must agree to
   working precision.
2. Take an asymmetric `H` (not even in the Weil coordinate) and confirm that the
   quadruple sum is still `\eta`-even — the evenness comes from the orbit, not
   from `H`.
3. Take `F` = number of zeros with `\operatorname{Re}\rho > 1/2 + 10^{-6}` and
   confirm it is even in `\eta` and discontinuous at `|\eta| = 10^{-6}`.
4. Perturb two quadruples at once and confirm evenness in each displacement
   separately.

## Remaining uncertainty

The proof is a two-line orbit computation and I am confident in it.  What I am
less sure of is the exhaustiveness of the table above: I have checked Weil, Li,
and `n`-level statistics explicitly, and asserted the rest by the general
argument, which is sound provided those criteria really are functionals of the
zero multiset alone.  For Robin's criterion in particular the reduction goes
through the explicit formula for `psi(x)`, and somebody should confirm that
route rather than take my word for it.

## Suggested next attack

Build the counting route.  The repository has no capability to evaluate `zeta`
at all, and by this theorem that is the only family of methods with unbounded
sensitivity.  A Riemann–Siegel `Z(t)` evaluator with double-double phases (the
`L-5601` machinery transfers directly), sign-change counting, Gram-point
bookkeeping and a Turing-method zero count would give the project its first
genuine counterexample *detector*, at a cost per zero that is the square root of
what the prime side pays.  `X-5602` is that experiment.
