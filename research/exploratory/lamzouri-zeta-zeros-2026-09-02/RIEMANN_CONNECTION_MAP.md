# Connection map to the Riemann repository

**Status:** structural synthesis, not theorem import. RH remains unproved.

## 1. Core dictionary

| Lamzouri/Axiom object | Riemann analogue | Exact relationship |
| --- | --- | --- |
| total multiplicity `M` | trace / total zero mass | first spectral moment |
| squared-kernel pair sum | Hilbert-Schmidt energy / Gram `tr(G^2)` | second spectral moment |
| simple real points | simple critical-line zero sector | desired positive subspace |
| nonreal conjugate pairs | off-line zero defect sector | horizontal symmetry defect |
| nested Hilbert subspaces | ordered Schur/complement blocks | range decomposition before elimination |
| Bessel inequality | trace-rank / effective-rank bound | averaged rank lower bound |
| differential weight removal | metric/source adapter | converts available pair metric to target kernel metric |
| Montgomery-Taylor extremal | optimal scalar test function | sharp inside current support-one second-moment class |

The most important warning is:

```text
effective rank is not complete capture.
```

Lamzouri controls how large the good sector must be. Riemann's RH-equivalent
operator programs must show that the bad sector is empty.

## 2. A0: canonical explicit-formula source contract

The zeta application depends on exact zero normalization and the BGST
pair-correlation theorem, whose proof ultimately uses explicit-formula
technology. It should consume, not bypass, Riemann's proposed A0 contract:

```text
xi normalization
zero coordinate and multiplicity
Fourier sign and 2 pi convention
prime/power/pole/archimedean terms
test-function support and decay
normalization fingerprint.
```

The new import adds a particularly useful A0 test case: the exact
second-derivative correction must cancel the rational pair weight under the
same Fourier convention used by the canonical explicit formula.

## 3. B0: source, metric, and simple-zero interfaces

Lamzouri supplies an unconditional **positive-density existence theorem** for
simple critical-line zeros. This strengthens the reservoir of possible
cardinal nodes.

It does not supply:

- an explicit cofinal enumeration of certified simple zeros;
- lower bounds for `|Xi'(gamma)|`;
- local separation;
- lower Beurling density in every window;
- a complete evaluation frame;
- uniform inverse-Gram conditioning.

Therefore it helps B0's node-existence side but does not close B0.

## 4. B1 cardinal/radical finite sections

Riemann's cardinal constructions need simple line zeros to define or condition
interpolation vectors. A `67.25%` global proportion says many such nodes
exist, but a cardinal frame needs local geometric control.

A concrete bridge theorem would be:

```text
local Lamzouri energy bound
+ zero separation
+ lower local simple-line density
+ derivative conditioning
  -> a uniform finite-section frame lower bound.
```

The current theorem has only the first ingredient in a global averaged form.

## 5. B2-B4 Schur algebra and kernel-defect classifier

The nested subspaces in the Hilbert proof are structurally parallel to
Riemann's ordered completion-of-squares and Schur-complement blocks.

This suggests extracting an abstract theorem:

```text
flagged Gram operator
+ trace
+ Hilbert-Schmidt control
  -> lower bound on the dimension of the good flag quotient.
```

That theorem could quantify the rank of the visible simple-line block before
Schur elimination.

But B4 is an RH-equivalence because an off-line cardinal direction survives
every positive-complement repair. Lamzouri does not change that fact. Its
second moment permits a complementary bad space of dimension roughly
`(1-C0)N(T)` and is therefore far from a complete zero-dimensional defect
proof.

## 6. B6 conditional two-frame and residual moat

The paper's real/conjugate decomposition gives a natural two-frame model:

```text
real simple sector
versus
multiple-real plus nonreal sector.
```

The useful import is not merely the final cardinality. The full coefficient
expansion in the Hilbert proof may yield quantitative singular-value or
principal-angle information between these sectors. Retaining that information
could sharpen Riemann's two-frame Schur moat.

The current published estimate collapses the spectrum to one trace and one
Hilbert-Schmidt number. Recovering a uniform moat requires more.

## 7. Xi Pick/Loewner and de Branges programs

A high density of simple real zeros is favorable for Pick matrices and
de Branges sampling, but density alone is insufficient. The exact missing
properties are:

```text
local lower density
separation or controlled clustering
evaluation boundedness
frame lower bound
cofinal completeness.
```

One promising research task is to place the rescaled simple zeros into a
Paley-Wiener/de Branges space whose bandwidth matches the support of `eta` and
ask whether the **unspent Bessel coefficients** in Lamzouri's proof imply a
sampling inequality. A bare count does not.

## 8. PR #785: spectral theta-Darboux / Schur extraction

The connection is especially sharp.

PR #785 proves positivity after integrating or summing a complete spectral
Slater family, while its surviving gate is positivity of each Schur
coefficient. Lamzouri likewise obtains positivity of the assembled Hilbert
tensor norm without termwise positivity of off-line kernel terms.

Thus both programs expose the same firewall:

```text
aggregate spectral positivity
does not imply
coefficientwise or directionwise positivity.
```

Lamzouri's theorem should not be cited as a shortcut to the theta-lattice
Schur-extraction gate. It may, however, supply an averaged trace bound for a
large set of coefficient directions.

## 9. PR #786: fixed-detector dichotomy

PR #786 shows that fixed zero-safe detectors either remain RH-equivalent,
require additional zero-summability input, or exhibit unavoidable
oscillation. The Lamzouri theorem is consistent with that diagnosis.

A fixed support-one pair statistic is normalized by `N(T)`. Finitely many, or
even density-zero, off-line zeros disappear in the average. Hence a fixed
detector can prove a proportion theorem while remaining incapable of RH.

The import therefore reinforces rather than evades the fixed-detector
firewall.

## 10. Zero-abscissa and prime-knot/resolvent programs

The repository's Mellin/prime-knot programs are individual-zero sensors: an
off-line zero changes an abscissa or creates a persistent prime-side
oscillation. Lamzouri is an average good-sector theorem.

A potentially productive hybrid is:

```text
one off-line zero
  -> Mellin/Landau propagation across infinitely many scales
  -> localized prime-side witnesses
  -> test against the large Lamzouri simple-line Hilbert sector
  -> contradiction from a uniform frame or Schur moat.
```

The load-bearing missing theorem is the third arrow: average simple-line
density must be upgraded to a locally conditioned frame capable of seeing the
propagated witness.

## 11. Alpoge-Furman finite matrix proof

The Lamzouri and Alpoge-Furman arguments should be formally related.

Proposed equivalence project:

1. define the finite Gram operator attached to the modulated `eta` vectors;
2. identify the finite matrix compression of Weil's Hermitian form;
3. prove that the matrix rank-trace inequality is the finite-dimensional
   projection of Lamzouri's Bessel argument;
4. prove compactness/monotone convergence from finite compressions to the
   Hilbert theorem;
5. compare which formulation retains more quantitative spectral data.

This would unify two new proof architectures rather than maintain parallel
black boxes.

## 12. Formal-v0.1 placement

The import must remain outside the trusted formal release because:

- it postdates the v0.1 source cutoff;
- it uses Lean `4.34.0-rc2`, while Riemann main uses `4.33.0-rc2`;
- exact local replay is pending;
- the two classical analytic inputs are not internally discharged;
- independent semantic review is pending.

The safe first extraction is the abstract finite-multiset Hilbert theorem into
`formal/Experimental/`, with no zeta or RH conclusion.

## 13. Ranked connection priorities

1. **Abstract flagged-Gram theorem.** Extract the Hilbert inequality in a
   reusable operator form.
2. **Matrix-Hilbert equivalence.** Connect it to the finite Weil compression.
3. **Local spectral-data retention.** Avoid collapsing all information to a
   cardinality bound.
4. **Simple-zero frame project.** Determine the exact local density and
   conditioning assumptions needed by B1/B6.
5. **Explicit-formula adapter.** Formalize the BGST metric conversion under A0.
6. **Individual-zero hybrid.** Couple the averaged Hilbert sector to a
   Mellin/Landau off-line-zero propagator.
