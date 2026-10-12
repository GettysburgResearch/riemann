# Directed refined-prefix and complete tail-moment guards

Status: directed finite guard packet. Execution and independent review scope
are recorded in the named receipt and separate review notes.
Scope: 111 refined low-zero intervals, the actual degree-six logarithmic
Gamma/zeta jet, three complete tail-moment intervals, and exact whole-family
guards for the two-pair analytic construction. This is no companion sector,
finite slab, or RH certificate.
Exact dependencies: the explicitly imported complete simple native census in
[NATIVE_SLAB_CERTIFICATE.md](NATIVE_SLAB_CERTIFICATE.md), the complete actual
product in [THEOREM.md](THEOREM.md), and the separately reviewed analytic
lemmas [MOMENT_NORM_TRANSPORT.md](MOMENT_NORM_TRANSPORT.md) and
[SEXTIC_ABSORPTION.md](SEXTIC_ABSORPTION.md).
What was actually run: native FLINT complete count at 8192, all 222 refined
Hardy-Z endpoint signs at 224 bits, the degree-six native Gamma/zeta jet,
and exact rational inequalities covering the entire resulting moment box.
Smallest remaining gap for a new finite sector: cover the complete auxiliary
parameter family and verify the full residual-transfer predicate throughout
the desired domain. No such computation is part of this packet.

## 1. Primitive refinement and inherited census contract

The source is `Xi(z)=xi(1/2+i*z)`. The earlier native packet contains 8049
ordered disjoint intervals, each of width `2^-24`, below `R=8192`. Its native
Hardy-Z sign changes saturate the FLINT complete count, under that packet's
explicitly imported historical finite Gram/Rosser contract. Saturation gives
the complete simple real zero census; the historical verification is not
reproduced here or in the earlier packet.

`produce_refined_prefix.py` produces candidates for the first 111 zeros,
which are exactly the retained original intervals below 256. The candidates
are explicitly unproved. `check_refined_prefix_moments.py` requires each new
interval to have exact width `2^-80`, to lie strictly inside its corresponding
original unique-root interval, and to give strict opposite signs for the
actual Hardy function

\[
 Z(t)=e^{i\theta(t)}\zeta(1/2+it),\qquad
 \theta(t)=\operatorname{Im}\log\Gamma(1/4+it/2)-t\log\pi/2.
\tag{RP1}
\]

It also requires the directed enclosure of the imaginary part of the
expression in (RP1) to contain zero. The exact real source identity supplies
Hardy-Z reality; a finite enclosure containing zero alone is not its proof.
Nesting and the imported unique-root contract identify each refined sign
change with the same source root. The other 7938 intervals are retained
unchanged. Their endpoint signs are **not** replayed by this checker; their
complete simple census status is imported from the named previous packet.
The checker checks all original ordered interval geometry, re-evaluates the
FLINT complete count 8049 at 8192, and checks every direct source hash in the
imported native receipt. This does not reproduce its historical count proof.

## 2. Exact normalization of the complete tail moments

The directed native Taylor jet uses

\[
 s=1/2+iz,\qquad
 \Xi(z)=\frac{s(s-1)}2\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{RP2}
\]

At 224 bits, `acb_series` truncation capacity seven supplies coefficients
through degree six. The checker verifies the strict seed `Xi(0)>1/4` and
checks the enclosures against the exact even-real identities. It then forms
the logarithmic jet of `Xi(z)/Xi(0)` and subtracts the whole finite census:

\[
 t_k=-k[z^{2k}]\log\frac{\Xi(z)}{\Xi(0)}
       -\sum_{j=1}^{8049}\gamma_j^{-2k},\qquad k=1,2,3.
\tag{RP3}
\]

The complete product makes (RP3) the exact paired unknown-tail moment
`sum_(Re rho>8192) m_rho/rho^(2k)`, including every zero beyond the census.
This identity is an analytic dependency, not an independently authenticated
infinite product in the finite checker. Each `gamma_j` ball uses the full
root interval: the 111 refined intervals and the 7938 original intervals.
No root midpoint is substituted into (RP3).

All three moments are strictly positive in their directed enclosures. For
readability only, their approximate values and enclosure widths are

| Moment | Approximate midpoint | Approximate width |
|---|---:|---:|
| `t1=a1` | `1.5879043364e-4` | `6.10e-13` |
| `t2` | `7.2442586164e-13` | `8.79e-18` |
| `t3` | `6.3598590068e-21` | `1.32e-22` |

The receipt stores the exact rational endpoints; these rounded values are
never used by an acceptance predicate.

## 3. Whole native parameter guards

Write `l_k,u_k` for the exact lower and upper moment endpoints. For the fixed
integer `K=6905`, the checker requires all four strict rational guards

\[
 K u_3^2<l_2^3,\qquad u_2^3<2K l_3^2,\qquad
 l_1^2>2K u_2,\qquad u_2/K<R^{-4}.
\tag{RP4}
\]

The first two put **every** point of the entire rectangular source enclosure
strictly inside the two-positive-pair moment cone in (SA2). The third gives
a strictly positive Gaussian coefficient throughout that family. By (SA4),
the fourth makes every artificial real root lie strictly beyond 8192.
It therefore excludes the artificial multiple roots from any protected
disk of radius below the complete census height. These are guard checks;
they do not evaluate or cover the companion quotients over the family.

With the exact classical strip `A=1/2`, the checker also verifies the positive
rational phase constants `c1,c2,c3` in (MN4) and records the complete bounds

\[
 S_{2k}\le u_k/c_k\quad(k=1,2,3),\qquad
 S_8\le u_3/(c_3R^2).
\tag{RP5}
\]

These retain the full unknown tail. Their validity imports the separately
proved complete norm lemma; the finite receipt distinguishes those analytic
dependencies from the primitive computations it actually performs.

## 4. Reproduction and frozen source identities

The machine files are `produce_refined_prefix.py`,
`refined_prefix_candidates.json`, `check_refined_prefix_moments.py`, and
`refined_prefix_moments.json`. Candidate input, producer, checker, displayed
analytic dependencies, inherited source data, imported receipt, and this
document are hashed in the accepted receipt. The receipt also records the
native Arb/acb/series extension and shared-library hashes. These are the
displayed direct source bindings, not a claim that every transitive
dependency is hashed.

Run from the repository root:

```bash
source /workspace/.riemann-tools/activate.sh
python research/exploratory/2026-10-10-four-hour-wave/xi/outer-ray/check_refined_prefix_moments.py --output /tmp/refined-prefix-replay.json
```

`python -O` may replace `python`; every acceptance test uses an explicit
`need` branch, never a removable Python assertion. The `--output` argument
preserves the official receipt during independent replay. Both modes use
the same native arithmetic implementation; no separate arithmetic backend
or published historical count computation is reproduced.
