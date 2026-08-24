# Replay packet

Frozen target: `4863c31dd497ffe69ea400fe29275decf4cb5d29`.

Run:

```bash
python3 symbolic_operator_replay.py
python3 qa_logic_replay.py
```

Expected:

```text
PASS_B_CROSS_C_SYMBOLIC_REPLAY
PASS_B_CROSS_C_QA_LOGIC_REPLAY
```

`symbolic_operator_replay.py` uses exact SymPy arithmetic and no floating-point
evidence. `qa_logic_replay.py` checks fail-closed consequences of exact target
file observations recorded with blob hashes in `FROZEN_FIXTURES.json`.

These scripts do not replace the missing Lean build.
