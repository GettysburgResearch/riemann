# Joint paired-native cancellation gate (`92940`)

**Status:** **PROPOSED / OPEN PRODUCER**  
**Base:** PR #500 at `d73c1e7a1a482cac31581211a84db43cc34c824e`  
**Reviewed siblings:** PR #505 at `1113fe6d...`; PR #507 at `dfaa70cd...`  
**RH:** unproved

## Result

The orientation bit is mathematically real, but its actual child block has negative aggregate ordinary response at `q=2`. Therefore it cannot be implemented as separately nonnegative physical child rows. The cancellation must occur jointly with the finite-forcing overcapacity before the construction enters the unpaired positive physical-row cone.

## Claims

```text
R-92940  exact negative-coordinate obstruction
L-92940  necessary joint physical interface
M-92940  proposed open joint compiler
T-92940  conditional recovery of one-shot interface
O-92940  sibling-repair disposition
```

## Replay

```bash
cd experiments/X-92940-joint-native-cancellation-gate
python3 verify.py --output results/verification.json
```

Expected:

```text
PASS_T92940_JOINT_NATIVE_CANCELLATION_GATE
b106f71b96a2515bee9f4eecf6df97d6daa90d6f77271125941ac031efbbf9f3
```

The replay proves the local sign obstruction and checks the corrected interface contract. It does not construct the joint compiler, rerun frozen analytic estimates, or prove RH.
