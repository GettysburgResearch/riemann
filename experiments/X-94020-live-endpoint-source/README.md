# X-94020 — Live Target–Lorenz endpoint/source registry

This replay instantiates the source-level objects omitted by the synthetic PR
#508 fixture.  It does **not** claim the remaining joint native coupling is
feasible and does not establish RH.

## Frozen base

```text
PR #508
4ae97dffd1f76ed3244b8f3028560ffa80663caf
```

## Generated proof objects

```text
results/certificates/native_source_registry_536.json
results/certificates/finite_endpoint_registry_536.json
results/certificates/terminal_leaf_67_13.json
results/certificates/causal_weights_871.json
results/certificates/outer_two_channel_cells.json
results/verification.json
```

They contain, respectively:

- every squarefree native occurrence through `X=536`, its `P_61` part, rough
  history, first owner, parity and channel coefficients;
- every literal finite endpoint occurrence `(m,k)` through `X=536`;
- all 229 active `P_61` atoms of the hostile leaf `(p,y)=(67,13)`;
- all 132 nonduplicating terminal-prime `beta/gamma` records at endpoint 871;
- all 66 directed outer two-channel cell certificates.

## Replay

```bash
python3 verify.py --output /tmp/x94020.json
cmp /tmp/x94020.json results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile generate.py verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_LIVE_ENDPOINT_SOURCE_TREE_AND_JOINT_CANCELLATION_GATE
```

## Scope

```text
live endpoint/source marginal and owners      EXACT / GENERATED
outer x<67 two-channel positivity             DIRECTED EXACT
real terminal P61 leaf and path weights       EXACT / GENERATED
finite-forcing beta/gamma allocation          EXACT FORMULA / GENERATED
branchwise actual-child positivity            FALSE / EXACT q=2 SEPARATOR
joint native Target-Lorenz coupling           OPEN
Riemann Hypothesis                            UNPROVEN
```
