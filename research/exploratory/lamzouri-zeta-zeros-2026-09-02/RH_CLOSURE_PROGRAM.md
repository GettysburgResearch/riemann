# RH closure program: what must be added

**Status:** speculative proof architecture with explicit gates.
**RH remains unproved.**

## 1. Why the current theorem cannot imply RH

The theorem is normalized by `N(T)`. Suppose RH fails because of one
functional-equation quartet, or finitely many quartets. Their contribution to
a fixed-support global average can vanish as `T -> infinity`.

Even the stronger statement

\[
\frac{N_0^s(T)}{N(T)}\to1
\]

would allow finitely many off-line zeros. Therefore:

```text
positive proportion  != RH
density one           != RH
all sufficiently high zeros on the line + finite verification = RH.
```

A complete route must either be effective and local at every sufficiently
large height or propagate one off-line zero into infinitely many
non-dilutable witnesses.

## 2. The operator diagnosis

Let `G_T` denote the Gram operator implicit in the Hilbert proof. The available
information is morally:

\[
\operatorname{tr}G_T\asymp N(T),
\qquad
\operatorname{tr}(G_T^2)\le C_{\rm MT}N(T)+o(N(T)).
\]

This controls stable rank:

\[
\mathrm{srank}(G_T)
=
\frac{(\operatorname{tr}G_T)^2}{\operatorname{tr}(G_T^2)}
\gtrsim C_0N(T).
\]

RH requires a qualitatively different conclusion:

```text
the horizontal defect space has dimension zero.
```

No bound on stable rank strictly below full rank can establish that.

## 3. Architecture H1 - local growing-support Hilbert amplifier

Target theorem:

> For every sufficiently high local zero window and every nonreal rescaled
> zero in that window, there is an admissible kernel whose defect contribution
> is bounded below by a fixed amount, while the prime-side pair energy is
> uniformly smaller than the resulting contradiction threshold.

Required chain:

```text
support-parameterized Hilbert theorem
-> local pair correlation in every window
-> support radius growing with the height/window
-> quantitative horizontal defect penalty
-> no nonreal zero in any sufficiently high window
-> certified finite verification below the threshold
-> RH.
```

The hardest gate is a pair-correlation or explicit-formula estimate uniform
for growing support. Current support-one asymptotics are not enough.

### Failure mode to exclude

A growing entire kernel can amplify an off-line point, but it simultaneously
lengthens the prime-side Dirichlet polynomial and worsens all error terms. The
proof must show a genuine net gain, not merely growth on the zero side.

## 4. Architecture H2 - higher-moment spectral collapse

Generalize the Hilbert construction to obtain a positive operator whose
Schatten moments are accessible from `k`-point zero correlations.

Desired theorem:

\[
\operatorname{tr}(G_T^j)
=
\operatorname{tr}(G_T)+o(N(T))
\quad
\text{for all }2\le j\le p(T),
\]

with enough uniformity that the spectrum is forced toward `{0,1}` and the
defect rank becomes `o(1)` in each local window.

Chain:

```text
higher tensor Hilbert identities
-> unconditional k-point correlation / prime moments
-> moment control with p(T) -> infinity
-> local defect rank < 1
-> defect rank = 0
-> RH above T0
-> finite verification below T0.
```

A global `o(N(T))` defect is insufficient. The integer-rank conclusion needs
local or effective bounds below one.

## 5. Architecture H3 - simple-line sampling frame plus B4 classifier

Use Lamzouri's simple critical-line zeros as nodes for Riemann's cardinal and
de Branges spaces.

Required theorem:

> In every cofinal normalized window, a selected set of simple critical-line
> zeros forms a sampling frame with a uniform lower frame bound, and the
> corresponding evaluation/derivative weights have controlled condition
> number.

Then:

```text
Lamzouri good-sector theorem
-> local lower density and separation
-> uniform simple-zero sampling frame
-> complete form/metric capture
-> B4 off-line cardinal direction survives positive complement
-> contradiction from a proved nonnegative kernel floor
-> RH.
```

### Present gap

A global count does not imply lower Beurling density or a frame floor. Large
local holes and small `Xi'(gamma)` can destroy conditioning. This route needs
new local information, not a repackaging of `67.25%`.

## 6. Architecture H4 - Mellin/Landau propagation hybrid

Riemann's abscissa and prime-knot programs convert one off-line zero into
persistent arithmetic oscillation across scales. Combine that individual
sensor with Lamzouri's large Hilbert good sector.

Candidate chain:

```text
off-line zero rho0
-> pole/abscissa defect in a Mellin transform
-> infinitely many scale-localized prime-side witnesses
-> expansion in a uniformly conditioned simple-line frame
-> positive Hilbert/Schur energy contradiction
-> RH.
```

This route avoids the finite-exception dilution by propagating one zero before
averaging.

The missing theorem is a source-admissible transducer from the Mellin witness
to the Lamzouri/Weil Hilbert metric with a uniform lower bound.

## 7. Architecture H5 - conjugation-odd horizontal energy

The abstract proof splits real and nonreal sectors. Instead of converting that
split immediately into cardinality, retain the conjugation-odd norm.

Seek an exact identity or inequality

\[
\mathcal E_T
=
\mathcal E_T^{\rm real}
+
\mathcal E_T^{\rm horizontal},
\qquad
\mathcal E_T^{\rm horizontal}\ge0,
\]

where a zero at horizontal displacement `delta` contributes at least
`Phi(delta log T)`.

If `Phi` grows sufficiently fast, the BGST energy budget could give strong
zero-density bounds away from the line. To reach RH one would still need:

- local uniformity;
- control as `delta -> 0`;
- an integer exclusion step;
- finite verification.

This is nevertheless the most direct new theorem suggested by the proof.

## 8. Architecture H6 - coefficientwise lift

PR #785 shows that aggregate spectral positivity leaves a coefficientwise
Schur gate. Lamzouri's Hilbert norm has the same aggregate structure.

A very ambitious target is to refine the tensor norm into a positive sum of
source-admissible coefficient blocks:

\[
\|F\|^2=\sum_\lambda E_\lambda,
\qquad
E_\lambda\ge0,
\]

with each off-line zero forcing one explicit block to violate a theta/Weil
coefficient inequality.

This would connect:

```text
Hilbert pair energy
-> Schur-resolved energies
-> theta-lattice coefficient positivity
-> de Branges/Weil criterion
-> RH.
```

The repository already contains an exact firewall showing that generic
spectral positivity does not imply coefficient positivity. Arithmetic source
structure must enter before this lift can work.

## 9. A concrete first theorem to attack

The best immediate RH-facing theorem is not "improve 67.25%." It is:

### Local horizontal-energy extraction theorem

For the exact Lamzouri admissible kernel and every finite
conjugation-invariant multiset, prove a strengthened inequality

\[
2M-\#\mathrm{SimpleReal}
\le
\mathcal E_K
-
\mathcal H_K,
\]

where `H_K` is an explicit nonnegative sum that vanishes exactly on simple
real points and quantitatively increases with multiplicity and imaginary
displacement.

Questions:

1. Is such an `H_K` already present as discarded Bessel coefficient mass?
2. Can it be expressed without choosing a Gram-Schmidt basis?
3. Does it admit a Schur-complement or reproducing-kernel formula?
4. Can the BGST metric estimate it, or only the total energy?
5. Does a planted off-line quartet force a uniform positive `H_K` after
   localization?

A positive answer would turn the proof from a counting mechanism into a
horizontal-defect energy theorem.

## 10. Required firewalls

Any claimed RH closure must answer all of these:

1. **Finite exception firewall:** why can one off-line zero not disappear in a
   normalized limit?
2. **Density-one firewall:** where is the integer step from `o(N)` bad zeros to
   zero bad zeros?
3. **Support firewall:** which theorem permits the growing or localized test
   family?
4. **Prime-side firewall:** are all longer Dirichlet-polynomial and endpoint
   errors controlled?
5. **Aggregate/coefficient firewall:** why does a positive total norm imply the
   sign of the needed direction?
6. **Frame firewall:** where are local density, separation, and derivative
   conditioning proved?
7. **Formal-input firewall:** are Riemann-von Mangoldt and BGST internal
   theorems or merely parameters?
8. **Finite-height firewall:** how are all zeros below the asymptotic threshold
   certified?

## 11. Assessment

The most promising near-term path is:

```text
retain horizontal/spectral information discarded by the cardinality estimate
+ connect it to Riemann's Schur/cardinal metrics
+ combine with an individual-zero Mellin propagation theorem.
```

The most direct purely pair-correlation route would require local,
growing-support, higher-moment estimates substantially stronger than the
current input. That is a legitimate research program, but its central analytic
gate is at least RH-strength and must be stated explicitly.
