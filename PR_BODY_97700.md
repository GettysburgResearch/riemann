## Purpose

Continue the exact annular-bias/source-no-go reconstruction at PR #587 head
`8a0f074c5b96600b461fdd6e23b47ee2162c4a70` and decide the threshold-flexible
factor-67 causal method at the literal native-source level.

**RH remains unproved.** This successor closes the atomwise owner and residual
ledger, proves a broad asymptotic no-go theorem, refutes `LAPBR67`, and isolates
a critical-saddle global history transport as the surviving frontier.

## Exact results

1. Every native rough occurrence has one ordered first-owner history, exact
   coefficient `prod p^(-1/2)`, activation `X/k`, and cumulative parity.
2. Every threshold split is the positive one-use identity `(r-a)+a=r`.
3. The missing `r-2r^2` source and the general `(R-A)F` residual are absorbed
   explicitly.
4. The root observation is the native annular scalar, not the finite `P61`
   base. At `X=184` the strict difference is `>1.36314`.
5. For every even depth satisfying `L log L=o(log log X)`, the exact stopped
   current is eventually negative.
6. PR #578's adaptive `L=O(log log log X)` large-prime residual `LAPBR67` is
   therefore eventually negative and is refuted.
7. The sector with least prime `p0>=Y^theta`, `theta>e^-1`, is proved positive.
8. The surviving theorem is `CSHT67`, a source-complete Hall transport in the
   critical depth window `k~log log X`.

## Mandatory stress cases

```text
one prime p=67              r-2r^2 > 0 and exact coefficient conservation
X=184                       native scalar differs from P61 base by >1.36
X=67*71*13                  239-atom odd-history target gap >17
two-node thinning           exact current a-r <0
X=32605 / 32606             directed depth-two sign change
X=61841                     depth-two current <-21.3, native scalar >9.5
raw exposure                (r-a)+a=r exactly
```

## Replay

```bash
bash experiments/X-97700-threshold-causal/build_and_replay.sh
```

Expected:

```text
PASS_T97700_DIRECTED_FINITE_STRESS_CASES
PASS_T97700_THRESHOLD_FLEXIBLE_CAUSAL_DECISION
e5aa32da9163ca9f816bd1b66123000ddfddb89d6d6d3841b32facf46862875b
```

## Deterministic mirrors

- ZIP: https://drive.google.com/file/d/1GxMTCHGwniqWqs-vhJkgQMNhD8doyTjA/view?usp=drivesdk
- PDF: https://drive.google.com/file/d/1MSyIYCuadAhjQ0yUM7M72P41lMLYNs_g/view?usp=drivesdk
- LaTeX: https://drive.google.com/file/d/1acRR8_XT0mkKDf18ENt41g950fC2m5_i/view?usp=drivesdk
- SHA-256 ledger: https://drive.google.com/file/d/1-f3bb9rQn73VLtrbY-zWRMezgoTbM23z/view?usp=drivesdk

## Exact boundary

```text
native first-owner ledger                  PROVED EXACT
r-2r^2 / (R-A)F residual                  PROVED EXACT
root equals native annular scalar          PROVED EXACT
raw-exposure conservation                  PROVED EXACT
subcritical threshold-depth positivity     FALSE
LAPBR67                                    FALSE
high-least-prime sector                    PROVED POSITIVE
CSHT67 critical-saddle transport           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVEN
```
