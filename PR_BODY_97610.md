## Hostile reconstruction of PRs #565 and #566

This add-only successor reconstructs the two factor-67 full proposals at their exact heads:

```text
PR #565: 339e3367660f40c74795802a6f8170b15e19b13a
PR #566: 2407b4ffe5024a2e3898922cf0b722d5cf69e496
```

It is designed to stack on PR #577 at exact head:

```text
ae85922195c12a29944e624337bae2167091929b
```

The attached handoff used the now-occupied `97500` namespace. This recovered
publication maps only its repository-facing identifiers and paths to `97610`;
the reviewed heads, mathematical statements and verdicts are unchanged.

### Scientific verdict

Neither reviewed proposal proves global scalar positivity or RH.

What survives exactly:

```text
positive 5:3 unsieved dictionary
scalar reciprocal-zeta Mellin transform
zero-safe finite numerator
conditional Mellin-Landau implication
rough-history parity cocycle
canonical Target-Lorenz theorem in its one-sided orientation
finite positive-operator parity-resummation lemma
finite completed-parity scalar Lorenz primal/dual theorem
```

### PR #565 findings

1. The claimed lower bias `F >= M/40` is false. At `x=184`,

```text
40F(184)-M(184) < -18.1144.
```

2. A corrected 256-bit directed/analytic theorem is proved:

```text
0 <= F <= M                    for 1 <= x < 67,
M/42 <= F <= M/8               for x >= 67.
```

3. The parity-swapped current is not the native same-channel positive restriction.
4. At one rough prime, the proposed recursion returns `F(x)` instead of the native `F(x)-p^(-1/2)F(x/p)`.

### PR #566 findings

1. The child injection lands in a reserve summand disjoint from the Hall-complement scalar `g_v`; it therefore does not imply `g_v >= (Tg)_v`.
2. Preserving target mass and barycenter does not preserve all Hall/Lorenz prefix inequalities.
3. The operator identity is exact, but its domination hypothesis is not proved for the same current appearing in the recursion.

### Repaired frontier

The remaining producer is:

```text
uniform completed-parity scalar Lorenz feasibility CPSL67
+ exact atomwise one-use rough-history recursion
+ residual Hall prefixes after reserve extraction.
```

### Front doors

```text
standalone/2026-08-18-factor67-pr565-pr566-hostile-reconstruction-97610/main.tex
standalone/2026-08-18-factor67-pr565-pr566-hostile-reconstruction-97610/factor67-pr565-pr566-hostile-reconstruction.pdf
standalone/2026-08-18-factor67-pr565-pr566-hostile-reconstruction-97610/PROOF.md
reports/gpt56-pro/2026-08-18-factor67-pr565-pr566-hostile-reconstruction.md
```

### Replay

```bash
cd experiments/X-97610-factor67-hostile-reconstruction
./build_and_replay.sh
```

Expected:

```text
PASS_FACTOR67_SCALAR_AND_OPERATOR_ALGEBRA
PASS_X184_COUNTERCERTIFICATE
PASS_FACTOR67_SOURCE_INTERFACE_FIREWALLS
PASS_REPAIRED_DIRECTED_P61_BIAS
PASS_X_97610_FACTOR67_HOSTILE_RECONSTRUCTION
```

### Exact boundary

```text
repaired finite P61 bias                 PROVED DIRECTED/ANALYTIC
PR #565 source-faithful induction        REFUTED
PR #566 reserve domination               REFUTED AS USED
finite scalar Lorenz primal/dual         PROVED EXACT
uniform CPSL67                           OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
