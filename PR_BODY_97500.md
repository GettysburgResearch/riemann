## Purpose

Continue PR #576 at exact head `0f6ea6eae813c1d867ae50744cf5fd57e2720bb7`
and solve the literal source-identity part of its repaired frontier.

**RH remains unproved.** This PR proves that a raw parity recursion and a safe
contracted recursion are related by an exact nonlocal resolvent. It supplies the
missing positive paired-source identity, and proves that no universal
source-local one-channel positive current can perform the same contraction.

## Main results

1. `L-97500`: exact raw-to-contracted resolvent
   `g=(I+T)(I+R)^(-1)b=b+(T-R)f`.
2. `R-97500`: two-node exact separator `g_parent=t-r<0` for every `t<r`;
   any exact current has all-depth alternating support.
3. `L-97501`: positive paired-source repair
   `C=B+(R-T)S child`, plus contracted children `TS child`, retaining every raw
   coefficient and owner exactly.
4. `L-97502`: contracted child mass only relocates raw scalar exposure; it does
   not reduce it. The repaired P61 interval needs raw child fraction `<=4/21`.
5. `T-97500`: exact reduction to the nonlocal Bellman inequality `NCBI67`.

## Replay

```bash
python3 experiments/X-97500-resolvent-transfer/verify.py
python3 -m pytest -q experiments/X-97500-resolvent-transfer/tests
```

Expected:

```text
PASS_T97500_RAW_CONTRACTED_RESOLVENT_AND_TWO_CHANNEL_SOURCE_REPAIR
5cd6ea67db8bb335c3d349917ff2b7d739fba83a99231efac27939ae5eb3e9b0
```

## Deterministic Drive mirror

- ZIP: https://drive.google.com/file/d/1nzFQFMnxuJqosd1noenv6sfOx01Cp4fo/view?usp=drivesdk
- PDF: https://drive.google.com/file/d/1lEA75cIo6U7DonfyTeocOmfpWC0_wSdB/view?usp=drivesdk
- LaTeX: https://drive.google.com/file/d/1tUWrJSBs9IId58JNA1ZWMnH8Xh2p3vaq/view?usp=drivesdk
- SHA-256 ledger: https://drive.google.com/file/d/17RUOlVduM1Cf82WWN9lr8lW6ACR4AReN/view?usp=drivesdk

```text
ZIP SHA-256: 9c1fc18a13d9cb5dcd7b50083ecbfda433c948af7b69fa14490c0eb90678b672
PDF SHA-256: c625ebe6090bb9ab061eca8c0dd4e6944cfebfddfc111fd5d5742498c023e31c
TeX SHA-256: 9617372a1f31289abc0580e8b3793e58eafe5128858a14f5e7475eeafb726cc7
```

## Scientific boundary

```text
repaired P61 bias                         retained from #576
literal positive paired-source identity  proved exact
raw coefficient preservation             proved exact
local one-channel safe current            refuted in general
nonlocal Bellman current NCBI67           open / RH-bearing
Riemann Hypothesis                        unproved
```
