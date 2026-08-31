# Focused validation ledger

```text
Scope: continuation files in this standalone packet only.
No repository-wide CI, source-branch rerun, or RH/GRH validation is claimed.
```

## Authoring executions

The theorem-producing authoring versions of the three exact replays were run
as follows.

Normal Python:

```bash
python -B ternary_change_of_rings_replay.py --prime 65521
python -B ternary_change_of_rings_replay.py --prime 65537
python -B cycle_index_alternant_replay.py
python -B stable_layer_head_replay.py
```

Optimized Python:

```bash
python -B -O ternary_change_of_rings_replay.py --prime 65521
python -B -O cycle_index_alternant_replay.py
python -B -O stable_layer_head_replay.py
```

All executions passed. The two chain-level primes produced the same rank
profile. The Python sources also passed `python -m py_compile`.

The JSON files committed beside the scripts are the frozen outputs of those
authoring executions. The committed scripts are compact review-facing forms
of the same literal algorithms. This continuation commit does not claim a
byte-level source/output seal: independent review should execute the committed
bytes and compare their mathematical outputs with the frozen JSON and theorem
statements.

## Expected exact chain-level profile

At both primes 65521 and 65537:

```text
rank d1(W), internal 2 = 205
rank d2(W), internal 2 = 45
rank d1(W), internal 3 = 1000
rank d2(W), internal 3 = 1095
rank d2(W), internal 4 = 6625
rank d3(W), internal 4 = 3030
rank(C tensor B_1,2 -> B_1,3) = 65
rank(horizontal map at E^1_(2,1,4)) = 1105
rank(d2 transgression modulo W-boundaries) = 65
```

The derived first ambient dimensions are 162 quadratic equations and 1720
cubic linear syzygies.

## Expected exact cycle-index profile

The replay must:

1. reproduce all three conjugacy-class numerators at each of four declared
   diagonal panels;
2. match every coefficient with the complete `GL3 x S3` Chow-Tor table;
3. recover the trivial, sign and standard isotypic Euler polynomials by
   character inversion;
4. match the explicit cycle alternant at the generic panel `(2,3,5)`.

The exact expected values are in `cycle_index_alternant_replay.json`.

## Expected stable-head profile

The replay must recover every term in the large-part heads of the committed
layers 3, 4, 5 and 6, then produce the period-four consequences

```text
[e_14] corr_7 = 2
[e_16] corr_8 = 2.
```

The exact term dictionaries are in `stable_layer_head_replay.json`.

## Review boundary

The finite replays certify the declared matrices, ranks and symbolic term
comparisons. The all-parameter cycle-index and stable-head statements depend
on their written proofs. The canonical-top note proves the intrinsic line and
comparison protocol but does not claim that the accepted 379-term vector has
already been projected coefficientwise.
