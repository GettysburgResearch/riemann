# CV/XD through completed L-function families: first exact hybrid-moment packet

Date: 2026-08-24  
Branch: `research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments`  
Base: PR #719 at `20e6bc5d961f00818fac86c9252e2535c5d9821a`  
Programmes: #743, #736, #737  
RH status: **unproved**

## 1. Motivation

The programme is based on the possibility that the missing theorem is not most
naturally visible in the isolated zeta function. A broader family may reveal a
moment law, a geometric trace or an exponential-sum mechanism that has no
transparent one-function formulation.

This pass therefore does not merely apply a generic large sieve to the current
CV/XD packet. It first constructs a family whose principal member is
coefficient-exactly the native common-mother detector and then asks what the
complete family moment does to the actual semiprime-squareclass obstruction.

## 2. Starting arithmetic object

PR #719 reduces the carrier-recombined physical obstruction to clean products

\[
N=P c^2,\qquad M=Qd^2,
\]

where `P,Q` are largest-two-prime semiprime owner squareclasses and the core
coefficients come from one stopped-Vaughan packet. Equal products, pair
diagonals, common square cores, shared owners, owner/core overlaps, first
chaos, zero phases and fixed-pair owner weights have already been treated.

The remaining difficulty is coherent summation over distinct owner
squareclasses.

## 3. Exact family completion

For every odd prime `ell != 67`, the branch constructs a family
`\mathcal F_(chi,ell)` with Mellin transform

\[
\widehat\Phi_*(z)
{(1-\ell^{-s})(1-\chi(67)67^{-s})\over L(s,\chi)},
\qquad s=z+\frac12.
\]

For the principal character, the missing Euler factor in
`L(s,chi_0)` cancels the ramified completion exactly, leaving

\[
\widehat\Phi_*(z){1-67^{-s}\over\zeta(s)}.
\]

Thus the family contains the literal native detector as its principal member.
No approximate Euler repair and no detector chosen after a hypothetical zero
is used.

## 4. What the moment actually does

Complete character orthogonality turns

\[
P c^2\quad\hbox{against}\quad Qd^2
\]

into the congruence

\[
Pc^2\equiv Qd^2\pmod\ell.
\]

If `QP^(-1)` is a nonsquare modulo `ell`, the owner pair vanishes exactly. If
it is a square, the full collision is only

\[
c\equiv \pm\tau d\pmod\ell.
\]

The family moment therefore converts the original physical identity-point
sum into two linear core-collision lines while retaining all existing nonzero
additive phases.

The equal-product diagonal is already subpower by PR #719. The new analytic
object is the weighted off-diagonal sum on those two lines.

## 5. Why the full family matters

Quadratic characters satisfy

\[
\chi(Pc^2)=\chi(P),
\]

so they erase the core. This exactly explains the reciprocity collapse already
recorded on PR #719.

General characters instead give

\[
\chi(Pc^2)=\chi(P)\chi^2(c).
\]

Only the principal and quadratic channels have `chi^2=1`. Every other channel
retains a multiplicative core phase.

In a finite field, combining that phase with one nontrivial additive phase
gives an exact Gauss norm `sqrt(Q)`. On a complete collision line, every
nonresonant additive phase sums to `-1`, while the only large lines are the
explicit resonances

\[
\pm\alpha\tau+\beta=0.
\]

This is the first concrete mechanism found in the L-family programme that is
absent from a quadratic-only lift.

## 6. Function-field mirror

The same packet is ported to `F_q[T]`:

- polynomial Möbius reciprocal coefficients;
- ramified principal completion;
- complete character moment;
- square/nonsquare owner-ratio classification;
- two core-collision lines in the residue field;
- nonquadratic Gauss cancellation.

The finite algebra is exact. The open geometric theorem is to identify the
trace sheaf of the actual incomplete Möbius/Vaughan line sums and prove a
purity/monodromy estimate outside explicitly resonant strata.

A useful function-field proof must end with a named number-field
exponential-sum or trace-formula target. Known function-field RH is not itself
a transfer theorem.

## 7. Binding no-go

Exact squareclass separation is not enough.

If `K` owner packets are made pairwise orthogonal in a family feature space,
the family dimension is at least `K`. Uniform positivity then bounds the
principal member only after paying that dimension. Large conductor
diagonalization can therefore be power-lossy even when the diagonal energy is
small.

Likewise, coefficients concentrated on one collision line saturate the
congruence occupancy bound. The density `1/ell` is not cancellation.

The live route must use the inherited additive phases, nonquadratic core
characters, a positive amplifier or a genuine trace/moment estimate.

## 8. New conclusion-facing theorem

For a predeclared weighted family and amplifier, define the principal leverage

\[
\Lambda_X
=
\sum_\ell w_{\ell,\chi_0}|A_{\ell,\chi_0}|^2
\]

and the total logarithmic family energy

\[
\mathfrak M(Y)
=
\int_2^Y
\sum_{\ell,\chi}
w_{\ell,\chi}|A_{\ell,\chi}|^2
|\mathcal F_{\chi,\ell}(X)|^2
{dX\over X}.
\]

The exact implication is

```text
PLEV106000:  Lambda_X >= X^(-o(1))
AND
HCLM106000:  M(Y)=Y^o(1)
->
native common-mother L2 energy is subpower
->
native negative mass is subpower
->
fixed reviewed Mellin--Landau consumer
->
RH.
```

Neither open premise is proved. This is an alternative family-moment
closure of the same common-mother frontier; it does not assert the separately
named `BQSP102870` estimate.

## 9. Recommended next passes

### A. Number-field hybrid moment

Freeze one dyadic PR #719 stopped-Vaughan block and expand the two surviving
collision lines completely. Classify:

- the two principal/quadratic exceptional channels;
- additive resonances;
- core-discrepancy versus pure-owner residuals;
- ramified and marked-67 sectors;
- the exact large-sieve or shifted-convolution cost.

The target should be a bound for the literal weighted line packet, not a
generic character sum.

### B. Function-field trace object

For quadratic characters over `F_q[T]` or a hyperelliptic family, construct
the sheaf corresponding to the weighted line sum. Determine whether the
desired saving is:

- memberwise by purity;
- averaged by monodromy;
- false on a resonant subfamily;
- or equivalent to an additional trace estimate.

### C. Trace-formula handoff

Only after the coefficient packet is frozen should Petersson, Kuznetsov,
spectral reciprocity or a relative trace formula be selected. The chosen
formula must place the actual owner/core pair on its diagonal and preserve the
principal leverage.

## 10. Replay

```text
PASS_X_106000_CVXD_LFAMILY_SQUARECLASS_MOMENTS
exact_checks=376476
proof_object_sha256=a23b1c5a739a5634593df8c6ec750a857dd8690e79c31fc8b195f0859c2786d1
```

The replay checks exact finite algebra only.

## 11. Current boundary

```text
native principal member in completed family      PROVED EXACT
reciprocal-L transform and finite-factor safety   PROVED EXACT
character moment and two-line reduction           PROVED EXACT
nonquadratic core visibility                      PROVED EXACT
finite-field Gauss prototype                      PROVED EXACT
function-field algebraic mirror                   PROVED EXACT
uniform separation shortcut                       REFUTED
HCLM106000 hybrid number-field moment             OPEN / RH-BEARING
FFHCLM106003 geometric function-field moment      OPEN / EXPLORATORY
Riemann Hypothesis                                UNPROVED
```
