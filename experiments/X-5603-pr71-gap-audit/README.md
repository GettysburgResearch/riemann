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

## Rigorous producers

FLINT already contains the Platt/Turing implementation that X-5602 proposed to
build.

### Consecutive total-zero check

`flint_consecutive_gap.c` calls

```text
acb_dirichlet_platt_zeta_zeros
```

near the estimated zero index `1.9743642386e13`, using the exact rational target.
If two consecutive **total zeta-zero balls** strictly bracket the target, the
open interval between those balls is certified to contain no line or off-line
zero.

### Direct counterexample predicate

`flint_line_gap_discrepancy.c` composes two directed computations:

1. `acb_dirichlet_platt_hardy_z_zeros` returns consecutive critical-line zero
   balls bracketing the target;
2. exact dyadic endpoints `a<b` are placed strictly between those balls;
3. `acb_dirichlet_zeta_nzeros` computes the total zero counts `N(a)` and `N(b)`
   with multiplicity.

The interior is rigorously critical-line-empty, so

```text
N(b)-N(a) > 0
```

is precisely the `L-5605` finite RH-disproof predicate. A zero discrepancy
certifies only that this exact interior slab is empty of all zeta zeros.

Build:

```bash
cc -O3 -std=c11 -Wall -Wextra -Werror \
  flint_consecutive_gap.c -o flint_consecutive_gap \
  -lflint -lmpfr -lgmp -lpthread -lm
cc -O3 -std=c11 -Wall -Wextra -Werror \
  flint_line_gap_discrepancy.c -o flint_line_gap_discrepancy \
  -lflint -lmpfr -lgmp -lpthread -lm

./flint_consecutive_gap 128 128 4 > results/flint-total-gap-128.json
./flint_line_gap_discrepancy 128 128 4 > results/flint-discrepancy-128.json
```

The workflow runs both producers at 128 and 192 bits and requires stable indices,
integer counts, classifications, and nested zero balls. Trusted-base trigger PR
`#92` launches the workflow.

## Why the original Pick screen became tiny

`L-5606` gives the linear-algebraic explanation. Under the proposed Pick Gram
representation, one zero very close to the sampled ordinate contributes a large
rank-one matrix. The next zero lies across an unusually large gap. Exact complex
vectors can nearly annihilate the dominant local direction, while barycentric
moments suppress the remote tail. The smallest eigenvalue can therefore be
extremely small and positive. This is a canonical precision-ghost geometry.

## Verification completed locally

```text
2 standard-library exact tests pass
exact-ordinate JSON regenerates byte-for-byte
Python compile checks pass
```

FLINT could not be installed in the local container because the package gateway
returned `503`, so no directed zero result is claimed locally.

## Proof boundary

- Exact rational / IEEE-754 audit: proved with the standard library.
- Parity identity: accepted after scope narrowing.
- Large gap and `|Z|` peak: empirical until a directed zero computation runs.
- Both FLINT programs are proposed producers; no completed output is committed.
- A certified local zero gap does not determine the complete PR #71 Pick sign,
  which depends on all zeros and is better checked by direct Arb contraction.
- A positive line-gap discrepancy would require independent backend reproduction
  and code/API audit before candidate promotion.
- No counterexample is claimed.
