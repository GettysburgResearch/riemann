# CANDIDATES.md — counterexample candidates

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31.

## Current candidates

**None.**

No `Z-####` candidate has been produced by the 2026-07-31 session, and none was found while reading the current
branch set. The session's results are structural and negative; nothing in them is evidence for or against RH.

## Candidates explicitly ruled out

| would-be candidate | why it is not one |
|---|---|
| Nonreal roots of the finite interpolation polynomial `P` | These exist in abundance below `alpha_c` (`R-16001`), but they sit at `\|Im w\| >= 1.56`, far outside the RH strip `\|Im w\| < 1/2`, and they move **away** from the real axis as the approximation improves — the benign behaviour Hurwitz predicts. They are truncation/aliasing artefacts of a finite model, not zeros of `Xi`. |
| A non-hyperbolic Jensen polynomial `J_{d,n}` | The reachable window is empty: hyperbolicity is a theorem for all `d <= 9e24`, all `n`. See `O-16002`. |
| `float64` roots reported inside the critical strip | Numerical artefacts. At `\|Im w\| ~ 0.43` under double precision; they vanish entirely at 150 digits. See `NEGATIVE_RESULTS.md` T-3. **This is the shape a false positive takes in this project — treat any such report with maximum suspicion.** |

## Standing requirements

Any future `Z-####` entry must meet README §9 in full: exact region or exact witness, zero-existence certificate,
off-critical-line certificate, nontriviality and singularity exclusion, and a multiplicity/zero-count statement
that claims no more than the method certifies. A decimal approximation is never a certificate.
