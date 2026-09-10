# The unconditional 90% through the reverse-Rolle descent

```text
Status:            PROVED EXACT (T-109200 descent bookkeeping, T-109201 shifted-Gram mesh
                   asymptotics), NUMERICAL RECORD (X-109202), REFUTATION (R-109203).
                   RH remains unproved. No zero-proportion theorem is proved here.
Scope:             the 90% gate of issue #744 / PRs #720, #726, #731, #772, #777
                   (min(U_+,U_-)/N < 99/2000 for the K = 31 derivative mesh).
Exact sources or dependencies:
                   L-108301 (PR #777 @ 399410ba), T-107401 (PR #772 @ 93726d7);
                   Riemann-Siegel formula; Xi(t) = A(t) Z(t); mpmath 1.3.0.
What was actually run:
                   scripts/mesh.py at heights [100,160], [1000,1048] (70 digits) and [5000,5024] (80 digits)
                     - zeros of Xi^{(K)} from Cauchy-circle Taylor expansions, residue signs,
                       certified zeros, Gram control (outputs/mesh_*.log, *.json);
                   scripts/gramshift2.py at T = 10^4 (16 phases, 600 points), 10^6 (8 phases, 400 points),
                   10^8 (phases 0 and pi/2, 300 points)
                     - descent efficiency of the mesh theta = delta + j*pi
                       (outputs/gs_1e4.log, gs_1e6.log, gs_1e8.log).
Smallest remaining gap:
                   none for the refutation; the limiting statement uses the observed
                   efficiency (~0.6) at the phase pi/2, which the K = 31 mesh visits near 10^15.
```

## Result in one paragraph

The descent inequality of PR #777 certifies exactly the zeros of `Ξ` that appear as sign
changes of `Ξ` between consecutive zeros of `Ξ^{(K)}` (Theorem 1). For `t ≫ K²` those
zeros form the Gram mesh shifted by an explicit phase `δ_K(t)` (Theorem 2), which for
`K = 31` sweeps through all values as `t` grows and reaches the Gram points only as
`t → ∞`. The descent's yield is therefore a shifted Gram's-law success rate: `0.75–0.80`
at the Gram phase and `≈0.55–0.60` at the phase `π/2`, at heights `10^4`, `10^6` and `10^8`
(Section 3); with the actual zeros of `Ξ^{(31)}` it is `39%` at height `10^2`, `89.7%` at
`10^3` (where `δ_{31} = 0.03π`, matching the Gram's-law rate `89.5%` there) and `61.5%` at
`5·10^3` (where `δ_{31} = 0.72π`), Section 4. The gate needs a minority residue fraction below
`0.0495`, i.e. sign changes on more than 90–95% of the mesh; it fails by a factor
between 2 and 10 at every height tested, and its limsup over `T` is at least `0.35`.
The "remaining theorem" of the programme is a false statement, not a missing lemma.

Read `PROOF.md`.

## Replay

```bash
cd standalone/2026-09-02-ninety-percent-descent/scripts
python3 gramshift2.py 10000 600 16      # ~4 minutes
python3 gramshift2.py 1000000 400 8     # ~3 minutes
python3 mesh.py 100 160 5,11,21,31 70   # ~2 minutes
python3 mesh.py 1000 1048 5,11,21,31 70 # ~5 minutes
```

All arithmetic is `NON_DIRECTED_HIGH_PRECISION` (mpmath); the theorems do not depend on
it. The scripts enumerate zeros of `Ξ` and `Ξ^{(K)}` in the stated windows only.
