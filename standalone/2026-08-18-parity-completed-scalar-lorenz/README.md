# Parity-completed scalar Lorenz reconstruction

This directory is the standalone front door for `T-97400`.

## Controlling result

```text
literal completed-parity source
  -> exact finite scalar Lorenz primal/dual
  -> CPSL67 (uniform producer, OPEN)
  -> R_X=5c_X(2)+3c_X(3) >= 0 eventually
  -> exact reciprocal-zeta Mellin transform
  -> Landau
  -> RH.
```

The manuscript proves every displayed interface except the uniform arithmetic inequality `CPSL67`. The earlier `L-96651` reserve theorem is superseded: it stated but did not prove this global capacity condition.

## Files

- `main.tex` — complete arXiv-style source;
- `PROOF.md` — readable standalone reconstruction;
- `references.bib` — bibliography;
- `HOSTILE_REVIEW.md` — falsification and reconstruction order;
- `REMOTE_ARTIFACTS.md` — Google Drive PDF/ZIP/TeX mirrors;
- repository-level `T97400_*` ledgers — dependency, interface and adversarial-response tables;
- `experiments/X-97400-independent-reconstruction/` — independent executable and retained finite result.

## Status

```text
complete unconditional proof of RH    NO
strongest exact result                CPSL67 -> RH
first unsupported arrow               uniform CPSL67
accepted proof                         NO
Riemann Hypothesis                     UNPROVEN
```
