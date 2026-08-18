## Purpose

Continue PR #593 after the exact threshold/source reconstruction and attack the
surviving critical-saddle and root Bellman frontiers without renaming them as a
proof.

**RH remains unproved.** This successor proves a new unconditional asymptotic
for every native state whose least allowed rough prime is a fixed positive
power of its endpoint.

## Frozen base

```text
base PR:      #593
base branch:  research/gpt56-pro/97700-threshold-flexible-causal-decision
base SHA:     ef5ef2d57540c43afb3749861a1dc96ff7e55b13
compared:     #594 @ ef76157a516c520a0f829ea4ee346c62759743ed
compared:     #591 @ 5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111
annular base: #587 @ 8a0f074c5b96600b461fdd6e23b47ee2162c4a70
```

## New theorem

For the literal native state

```text
F(Y,z)=sum_(P^-(m)>=z) mu(m)m^(-1/2)b(Y/m),
```

fix `theta>0` and assume `Y^theta<=z<=Y`. Uniformly,

```text
F(Y,z)=a sqrt(Y) rho(log Y/log z)+o_theta(sqrt(Y)),
```

where `rho` is the Dickman function. The paper derives `rho` directly from the
rough-product activation simplex and proves positivity through

```text
u rho(u)=integral_(u-1)^u rho(v) dv.
```

Therefore every fixed power-scale state is eventually positive. The earlier
restriction `theta>e^-1` is removed.

## Consequences

- state-wise RBLPTE is proved in every fixed power sector;
- a one-use scalar transport exists there;
- full target-preserving CSHT is not inferred;
- any counterexample sequence must satisfy `log p0/log Y -> 0`;
- the only remaining state is the subpower least-prime harmonic saddle.

## Replay

```bash
cd experiments/X-97900-dickman-power-sector
python3 verify.py --limit 1000000 --output results/verification.json
```

Expected:

```text
PASS_T97900_DICKMAN_POWER_SECTOR_LOCALIZATION
3364c1b018dfabb014f4d7aac52520b9e98a44c0d1c61bfced174ddeae84fecf
```

The finite replay is diagnostic; the theorem is proved analytically.

## Deterministic artifacts

- ZIP: https://drive.google.com/file/d/REPLACE_ZIP_ID/view?usp=drivesdk
- PDF: https://drive.google.com/file/d/REPLACE_PDF_ID/view?usp=drivesdk
- TeX: https://drive.google.com/file/d/REPLACE_TEX_ID/view?usp=drivesdk
- SHA-256 ledger: https://drive.google.com/file/d/REPLACE_SHA_ID/view?usp=drivesdk

## Exact boundary

```text
Dickman simplex identity                     PROVED EXACT
all fixed power-scale states                 PROVED POSITIVE
state-wise RBLPTE on those states            PROVED
scalar one-use transport on those states     PROVED
full target-preserving CSHT                   OPEN
subpower critical core SPCC67                OPEN / RH-BEARING
root RBLPTE67                                OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
