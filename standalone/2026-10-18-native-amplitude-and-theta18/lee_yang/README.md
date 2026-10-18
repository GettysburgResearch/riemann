# Original theta moments through degree 18 on a connected ferromagnetic tree

**New proposed finite theorem:** a 281-spin zero-field ferromagnetic Ising
model with 280 strictly positive edges realizes every moment of the original
theta law through degree 18. The characteristic function of its weighted
spin observable has only real zeros by the finite weighted Lee–Yang theorem.

The full proof and normalization are in [PROOF.md](PROOF.md). The exact
target is the complete theta density, including every theta index and the
whole time domain. The checker regenerates its moments through degree 20
with outward integer intervals. An optimizer output is never accepted as a
moment target or as a root.

This reaches the degree-18 target that remained open after the degree-16
construction in [PR #974](https://github.com/GettysburgResearch/riemann/pull/974).
The new graph has a 14-spin core chain with unequal positive observable
weights, 266 leaves, and one zero-weight hub. One core edge has correlation
0.22713565209564776; the other twelve have correlation exactly 10^-8.
The hub and its incident edges are included in the actual probability law.

| Certified quantity | Result |
|---|---:|
| Matched even moments | 2, 4, 6, 8, 10, 12, 14, 16, 18 |
| Odd moments | All zero by spin-flip symmetry |
| Vertices / edges | 281 / 280 |
| Couplings | Every edge satisfies 10^-9 < J < 1/4 |
| Active coordinates / box radius | 9 / 10^-30 |
| Residual displacement β | Less than 2.843·10^-41 |
| Whole-box contraction bound L | Less than 4.312·10^-12 |
| Covariance of the first two weighted core spins | Between 1/60 and 17/1000 |
| Standardized moment-20 discrepancy | Between 0.450 and 0.451 |

The standardized observable has variance exactly one and support in
(−10,10). To obtain the original theta moments, multiply all observable
weights by the exact square root of the theta variance, leaving every
coupling fixed. The checker also separately encloses the direct raw
moment-20 discrepancy and its cumulant expression. Both certify the
finite endpoint rather than an all-order identification with xi.

## Replay

Use standard Python 3 from this directory:

```sh
sha256sum --check SHA256SUMS
python3 certify_chain.py --check chain_certificate.json
```

The checker uses the Python standard library only. It reconstructs all
theta source bounds, computes and verifies an exact rational inverse,
checks the Jacobian on the entire root box, proves strict invariance and
contraction, and runs an exact 128-configuration control. The receipt
includes every source interval, every tail bound, and the hashes of all
load-bearing computational inputs.

The proof uses the unchanged directed arithmetic primitive from PR #886,
whose exact source hash is authenticated by the checker. It extends the
six-index theta integration from PR #974 to moment 20. The new chain
recurrence and the new root have separate identities; the earlier packet
is unchanged. [VALIDATION.md](VALIDATION.md) records these dependencies
and the distinction between replay and an independent arithmetic backend.

## What remains open

RH is not proved. The finite model does not match theta moment 20; its
certified discrepancy is positive. Reaching one fixed degree, even with an
actual connected ferromagnet and strict parameter margins, does not provide
the unbounded sequence of moment realizations required by the all-order
Lee–Yang route. The next mathematical task is a construction or extension
mechanism that preserves admissibility and reaches increasing orders.

[EXPLORATION.md](EXPLORATION.md) records which searches failed and what
changed in the successful architecture. Floating scout files are kept out
of this proof packet. The certificate depends only on the rational center,
the complete source replay, the polynomial identities, and the strict
acceptance conditions.
