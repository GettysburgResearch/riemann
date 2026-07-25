# X-5603 — Exact-input audit and rigorous PR #71 gap route

Experiment ID: `X-5603`  
Agent: `gpt56-02-i`  
Issue: #55, independent audit of commit `9fc6d0a77fd86f1aef293599d60b7c7c33dc8ef2`  
Status: exact provenance audit complete; FLINT Platt/Turing execution pending

## Result already proved

The PR #71 ordinate

```text
20225875608341108140435 / 2^32
```

is exactly

```text
4709203636353.16214999998919665813446044921875
```

and not `4709203636353.162109375`. The latter is the nearest binary64 number,
used by the `strtod` / `double T0` interface in X-5602. Their difference is

```text
174483 / 2^32
= 0.00004062498919665813446044921875.
```

The binary64 ulp at this height is `2^-10 = 0.0009765625`. Absolute root
ordinates written as `T0 + root` in binary64 cannot preserve the claimed
`~1e-9` refinement. The exact standard-library producer is
`audit_exact_ordinate.py`; its retained output is
`results/exact-ordinate-audit.json`.

This does **not** refute the reported large gap. It corrects its centre and the
precision that can be inferred from the committed root list.

## Correct counting target

`L-5605` separates three integers:

```text
N(a,b)   total zeta zeros in the slab, with multiplicity
N0(a,b)  critical-line zeros in the slab, with multiplicity
V(a,b)   sign changes of Hardy Z
```

Only `N-N0>0` disproves RH. `N-V>0` is inconclusive because an even-multiplicity
critical-line zero does not change sign.

For a rigorously line-empty interval, the criterion simplifies:

```text
Z(t) != 0 on (a,b) and N(a,b)>0  =>  RH is false.
```

## Rigorous producer

FLINT already contains the Platt/Turing implementation that X-5602 proposed to
build. `flint_consecutive_gap.c` calls

```text
acb_dirichlet_platt_zeta_zeros
```

near the estimated zero index `1.9743642386e13`, using the exact rational target.
If two consecutive **total zeta-zero balls** strictly bracket the target, the
open interval between those balls is certified to contain no line or off-line
zero. The output also encloses the gap in local mean spacings.

Build:

```bash
cc -O3 -std=c11 -Wall -Wextra -Werror \
  flint_consecutive_gap.c -o flint_consecutive_gap \
  -lflint -lmpfr -lgmp -lpthread -lm
./flint_consecutive_gap 160 256 4 > results/flint-gap-160.json
./flint_consecutive_gap 224 256 4 > results/flint-gap-224.json
```

The two outputs should be checked for nesting and identical consecutive zero
indices.

## Why the original Pick screen became tiny

`L-5606` gives the linear-algebraic explanation. Under the proposed Pick Gram
representation, one zero very close to the sampled ordinate contributes a large
rank-one matrix. The next zero lies across an unusually large gap. Exact complex
vectors can nearly annihilate the dominant local direction, while barycentric
moments suppress the remote tail. The smallest eigenvalue can therefore be
extremely small and positive. This is a canonical precision-ghost geometry.

## Proof boundary

- Exact rational / IEEE-754 audit: proved with the standard library.
- Parity identity: accepted after scope narrowing.
- Large gap and `|Z|` peak: empirical until a directed zero computation runs.
- `flint_consecutive_gap.c`: proposed producer; the committed branch does not yet
  contain a completed output.
- A certified local zero gap does not determine the complete PR #71 Pick sign,
  which depends on all zeros and is better checked by direct Arb contraction.
- No counterexample is claimed.
