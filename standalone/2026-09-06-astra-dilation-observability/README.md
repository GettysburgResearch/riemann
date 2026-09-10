# Dilation observability and source-complete Schur prediction

**Status:** proposed component theorems and bounded directed computation.
**RH is not proved. Independent mathematical and code review is required.**

This is a new research submission, not a Reviewer C verdict. It changes no
canonical claim, trusted formal library, original research branch, or main
file. Proposed repository anchor:
`main@051808c1f8367b4320c52f94b40908eb2173d622`.
Remote publication has **not** been performed in this environment.

## The connection

In the classical discrete Nyman–Beurling Hilbert space, let g be the limiting
orthogonal projection of the constant target chi onto the complete integer
fractional-part dictionary. Integer dilation gives the exact estimate

\[
(2-\sqrt2)\|\chi-g\|^2
\le 1-g(1)\le
(2+\sqrt2)\|\chi-g\|^2.
\]

Thus the full residual is observable on the single interval [1,2), and RH
is equivalent to g(1)=1. The substantive condition is **the limiting
orthogonal projection**. The first finite projection already has g_2(1)=1
while its squared error is 1-log2; a finite cell match is not a certificate.
The packet proves the exact finite leakage term rather than dropping it.

The other main theorem is an arithmetic support obstruction: restricting
the dictionary to indices 2^a 3^b gives distance squared at least 1/52,
although its common Mellin zeros in Re(s)>1/2 are exactly those of the full
dictionary. An explicit three-cell Möbius-dual witness proves this. Shared
zero signature, positive Grams and integer-dilation invariance do not by
themselves establish source completeness.

The surviving constructive route uses positive Schur updates. If delta_N
is the exact squared approximation error, then

\[
\delta_N-\delta_{2N}=z_N^T S_N^{-1}z_N.
\]

Every S_N is positive definite unconditionally. RH would follow from the
new-block gain estimate z_N^T S_N^{-1}z_N >= c delta_N^2 on all sufficiently
large dyadic stages, for one c>0. The weaker exact criterion is divergence of
the sum of normalized gains. **Neither unbounded statement is proved.**

## Reading order

Read [PROOF.md](PROOF.md) for the complete component arguments and the
conditional end-to-end implication, [FRONTIER.md](FRONTIER.md) for the three
closing attempts and their outcomes, and [NUMERICS.md](NUMERICS.md) for the
analytic remainder and interval-computation contract. [SOURCES.md](SOURCES.md)
separates classical input, repository context, reading limits and authorship.
[VALIDATION.md](VALIDATION.md) reports only executed checks.

## Bounded numerical results

The arithmetic computes the **entire infinite Gram sums**, not a truncated
prefix masquerading as the Gram. The table abbreviates directed enclosures
in `verification.json`; displayed decimals are not exact values.

| N | Squared error delta_N | First-cell projection g_N(1) |
|---:|---:|---:|
| 2 | (0.306852819440, 0.306852819441) | exactly 1, by the separate algebraic proof |
| 3 | (0.095747783927, 0.095747783928) | (1.036548936851, 1.036548936852) |
| 4 | (0.065951694215, 0.065951694216) | (0.963067442677, 0.963067442678) |
| 8 | (0.024244525306, 0.024244525307) | (0.950209575732, 0.950209575733) |
| 16 | (0.017936267020, 0.017936267021) | (0.959417347901, 0.959417347902) |

The full Schur gain divided by delta_N^2 lies respectively in
(2.558459770452,2.558459770453), (9.588679393958,9.588679393959), and
(10.732035392425,10.732035392426) at N=2,4,8. These are three finite cases,
**not evidence establishing a uniform lower bound**.

A simpler hoped-for mechanism is actually refuted: the residual coupling
with D_2 g_N is strictly negative at N=8, and that one innovation direction
accounts for less than 0.032 of the full doubling gain there. The correct
object is the full source-complete block, not a presumed positive scalar.

## Replay

Only Python's standard library is required. From any working directory:

```sh
python -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/replay.py --check
python -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/test_replay.py
python -O -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/replay.py --check
python -O -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/test_replay.py
python -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/test_cli_mutations.py
python -O -I -S -B standalone/2026-09-06-astra-dilation-observability/scripts/test_cli_mutations.py
```

The maximum Gram index is fixed at 16. No external dependencies, credentials,
network access, Lean build, remote CI, prime enumeration or zero search are
required or claimed. The analytic proofs and the unbounded frontier are not
machine-proved by this finite replay.
