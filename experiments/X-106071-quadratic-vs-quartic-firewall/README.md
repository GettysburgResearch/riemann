# X-106071 — Quadratic versus quartic occupancy firewall

This replay authenticates the finite algebra behind `R-106071`, `L-106074`
and `L-106075`.

Run from the repository root:

```bash
python experiments/X-106071-quadratic-vs-quartic-firewall/verify.py \
  --output experiments/X-106071-quadratic-vs-quartic-firewall/results/verification.json
```

Expected verdict:

```text
PASS_X_106071_QUADRATIC_VS_QUARTIC_FIREWALL
checks=7472
sha256=145e8e6e7fa3cc38c75fef3083ede2a6dfdb7feba6f441222e0605921315d9a7
```

## Checked exactly

- character orthogonality in its residue-Gram form;
- quadratic scaling of the family moment;
- quartic scaling of the matched owner-pair tensor;
- explicit many-owner one-residue counterexamples to a uniform
  quartic-to-quadratic adapter;
- the fact that a partial core matching does not bound the number of owner
  packets in one cell;
- at most two core roots for one owner and residue;
- Hilbert Cauchy closure of every bounded owner-crowding cell.

## Not checked

The replay does not prove the high-crowding owner assembly `HQORO106071`, the
global physical occupancy theorem `BPOE103300`, the fixed Mellin consumer, or
RH.  It is a finite exact rejection certificate for the retracted first
`T-106070` proposal and a mutation detector for the corrected frontier.