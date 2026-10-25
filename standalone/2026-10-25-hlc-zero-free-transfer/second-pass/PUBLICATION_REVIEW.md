# Publication review of the second pass

Date: 25 October 2026. Reviewer: root coordinator.

Status: reviewable, source-dependent research packet. No RH proof or smaller
global zero-free half-plane is accepted by this report. Internal agent
review is not external peer review or formal verification.

## Exact freeze and preservation

Final mathematical commit:
`5c7f4aa542ea2112b7f95fce984a35dfe454cfd6`.

Verified commit tree:
`c1dc2bc564b088eafb4e2c7c5e4be84b2a0f71c4`.

The first mathematical upload was
`3b47783a7c775bc8133f6601cb9bb97b1b38678a`. Independent remote checks
caught a carriage-return control byte in the moving-twist note's equation
(21), which transport had normalized to a line feed. The final freeze
repairs that typesetting byte to the intended literal LaTeX command and
updates the manifest. The complete mathematical content of the other
files is unchanged. The corrected moving-twist bytes were separately
rechecked and authenticated by both reviewers of that note.

The comparison from the original first-pass publication
`00d36f61ae7898846579840e6a68f9a06bd8295c` to the final mathematical
freeze contains exactly 13 added files, all in this second-pass directory.
Every first-pass file and every other repository path remains unchanged.
Main was read at `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

I fetched the final remote tree and compared all 12 manifest-listed files
with their local byte counts and independently computed Git blob hashes.
Every file matched. The manifest itself was separately verified:
2,963 bytes, SHA256
`68f69ad289a722a358b113cdec20db41cf54755bffb2c1bce73cecdf045e3536`,
Git blob `ca948bb86211998ad92e2c147bfb6e9b4b945f8f`.
The exact commit object independently confirms the tree above.

## Load-bearing objects

| File | SHA256 | Verified Git blob |
| --- | --- | --- |
| CAPPED_NATIVE_MOMENT.md | `9201cbf1327472f0f2d51f468ed276d3101e321c5018fefecbad79f34b35d011` | `639cbe39e3c15a5f5d3c5493420d3575ff211f43` |
| UNIFORM_HLC_AUDIT.md | `b346256f95beffb0bb8416cc292533370e9203e92bdacc6e923ce351e4cb0b6b` | `6db6de522955e032e9d49a1a012f45bbade37871` |
| TWO_SIGN_HLC.md | `da49263ae36f47cf1162fd96859a700b9075e8211743d68fdc476d0cc939d73e` | `f06dfb3cc4564d795ea1c5a79cb1323fbd43ca3f` |
| MOVING_TWIST_MOMENT.md | `51490a1139f6a466de69d10faa15570b3b26e67976360fc75f7bcb4374bb629a` | `0efad91ee54db8f7f264614f18d8d2815f028016` |
| FRACTIONAL_NATIVE.md | `46c4cc488a463b5ad0606945280f71fd52b4b3a829f0c836422dc44a3c92d379` | `39a61be22e833912704a4b02d89d0673ea85455d` |
| NATIVE_GAIN.md | `4127becd461de5a845174203d45ad2f9014cbe67709375db9b1b2046021ce453` | `55e01b86b3ac198951789e5ef03babcff5fd17b7` |
| DETECTOR_CONSUMER.md | `8715b0914e7f68f0067f0a07a5b47219f87c12ceb5e694229a85c224af07c62c` | `edd87c95603a09a6e844d9ec823689d3c0014b10` |

The manifest provides the remaining checker and overview identities.
The review-only follow-up commit adds these reports; it does not strengthen
or silently edit any of these mathematical objects.

## Mathematical review by the coordinator

I read all seven mathematical notes and checked their principal identities,
analytic dependencies, parameter ranges and proposed consumers.

### Optimal unmarking

The new projection theorem is independent of the HLC preprint. With
q_i=1/E(U_i^2), the functions U_i and 1-q_i U_i are orthogonal. The
products indexed by subsets form a nondegenerate orthogonal tensor basis.
The triangular expansion identifies exactly the span of admissible
minimum-degree marks. Projecting the constant gives the displayed
alternating coefficients and the Poisson-binomial residual. I checked
both the span equality and the normalization in the finite CRT model.
The coefficient-mass amplification and probability-measure discrepancy
are retained in the correlation transfer.

This verifies a finite-dimensional theorem for arbitrary size from its
proof; the enumerations are separate checks. The exponential-in-band
error alone is not treated as an arithmetic rate in x.

### Quantitative HLC extension

I compared the growing-band audit with the supplied source's good-state
definitions, clean and dirty edge estimates, Fock Schur construction,
global distinctness argument, major-arc scope and final unmarking.
The explicit geometric spacing replaces the fixed-exponent-gap limit.
The local constants are bounded by products of fixed per-band factors;
the planar Fourier estimate is used once, and list symmetrization has
mass one. The corrected Schur parameter choice includes the internal
sqrt(rho) endpoint. The dirty raw norm retains the square root of its
small Schur factor.

The growing absolute edge exponent and affected-edge count are included
in the distinctness argument. Arithmetic root moduli remain subpower,
and major-arc character-conductor exponents remain fixed. The separate
mixed-moment proof bounds the actual binomial expansion coefficients
uniformly in each band before applying Bombieri–Vinogradov. It does not
replace them by a superlogarithmic truncation-order power.

These deductions support the stated logarithmic rate at the imported
source's scope. The separate `REVIEW_UNIFORM_HLC.md` is an independent
check by an agent who did not author that extension. Neither review
reconstructs or certifies the entire external preprint. No numerical
starting threshold or implied constant is certified. The Liouville
appendix is explicitly an anticipated source counterpart, not a novelty
claim.

### Actual native inverse gain

The all-family cap in the exact OpenAI source was independently read.
It includes the finite-order Hecke characters used here. This corrects
the earlier attempted rejection based on an ordinary-zeta-only premise.

The buffered-bin input was checked against Xu–Sang Lemma 6.2 and
Proposition 6.3, including polynomial heights, the fixed finite family
of ray twists/orientations and the order of choices. Its bins round
down, so the global family cap really does imply a<=7/8. Extra zero
masks do not change the primitive zero assignment.

Within each bin, an Euler-normalized holomorphic logarithm is bounded
on the inner disk. Polynomial conductor growth bounds its real part
on the outer disk. Borel–Caratheodory followed by three-circles gives
(log U)^theta with theta<1 on the required contour, hence an arbitrary
small-power reciprocal bound. I checked the disk radii, finite-height
buffer, absence of a principal pole, uniformity over extra masks, and
the external Mellin-tail order chosen after the source height exponent.

The contour is for the exact reciprocal Dirichlet series, so its
coefficient is the original mu_E psi_u. The floor contribution remains
below the computed envelope. The endpoint exponents and their gains are
exact: 79/56 instead of 17/12, and 25/14 instead of 11/6 at r=2.
Separate reviews authenticate these deductions and the explicit inherited
premises. The all-family cap is used, not newly proved or independently
certified.

### Growing-prime and Gauss components

The prime-parameter adapter uses exact Euler-ratio convolution including
every repeated prime power. Its finite-order marks come from coefficient
identities rather than differentiation of an inequality. The explicit
absolute convolution cost and the unresolved full damping remainder
are retained.

The Gauss inverse uses the actual unitary cocycle, its coprimality and
its induced fourth-power row twist. Its finite Heath–Brown identity is
limited to its proved support. The complete outer factor sum and the
signed Fourier return are not suppressed. I checked the two row
decompositions and the corresponding ordinary-component exponents.

I authored the moving-twist estimate and the detector note, so this
paragraph is not an independent review of those objects. Their separate
reports supply independent checks. The native agent contributed to the
moving-twist discussion and explicitly discloses that overlap; the
fractional agent's moving-twist report has no such authorship overlap.

### Consumer and global claim

The new inverse saving begins at r>10/7. The exact old selected-prime
crossing satisfies t_*<=10/7, and the improved long count is
nondecreasing afterward. Thus the minimax count in the specified old
consumer is unchanged, including the separate floor and plain cases.
The general-cap contact identity is also exact.

This prevents the real moment improvement from being reported as a new
zero-free region. At r=3/2 the remaining gap to PR1014's sufficient
exponent is 37/840. The imported B_flat benchmark is unchanged.

## Independent reviews and authorship

- `REVIEW_CAPPED_NATIVE.md`: native agent, independent of the capped proof.
- `REVIEW_FRACTIONAL_NATIVE.md`: native agent, independent of the
  growing-prime and factorial-mark proofs.
- `REVIEW_UNIFORM_HLC.md`: native agent, independent of the HLC audit.
- `REVIEW_MOVING_TWIST.md`: fractional agent, independent of the
  moving-twist proof.
- `REVIEW_MOVING_TWIST_NATIVE.md`: native agent, with intellectual overlap
  disclosed.
- `REVIEW_NATIVE_GAIN.md`: fractional agent, independent of the Gauss
  inverse note and checker.
- `REVIEW_DETECTOR_CONSUMER.md`: HLC agent, independent of the detector
  note, with an additional conditional mathematical check of the capped
  inverse proof.

Each report records exact hashes and remote-commit authentication.
Unaffected objects reviewed at the first mathematical upload are also
byte-identical in the final freeze; the final manifest/tree verification
binds that fact. None of these agents is an external referee.

## Computation

The coordinator independently executed all three new checkers under
isolated Python. Each exited zero. The complete results are in CHECKS.json.

- Optimal marks: complete reduced-residue spaces of moduli 105, 1155 and
  15015; exact moments, all admissible orthogonality conditions, projection
  residuals, perturbation optimality and a rejected coefficient mutation.
- Prime coefficients: 48,000 rational convolution cases, 11,200 binomial
  mark cases and 15 local series controls. Dropping repeated-prime
  corrections is rejected.
- Gauss algebra: 3,000 inverse coefficients, 632 finite Heath–Brown cases
  and 72 row transports over exact synthetic Q(zeta_6). Incorrect twist
  powers and omitted cocycles are rejected. This is not native Gauss data.

Analytic asymptotics are justified by the written arguments and their
explicit source premises, not by these finite computations. No CI result,
formal proof or literature-wide novelty assessment is asserted.

