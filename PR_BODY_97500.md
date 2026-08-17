## Purpose

Continue from the corrected P61/source-interface frontier in PR #576 and attack
the remaining parity recursion itself. This is not a second review of #565 or
#566. It proves the exact natural-versus-thinned resolvent identities, shows
where the positive-operator resummation consumes a stronger current than its
source theorem produces, and replaces the crude source-mass adaptive depth by a
nontrivial critical-row depth.

**RH remains unproved.**

## Freeze

```text
cutoff UTC:        2026-08-17T22:46:53Z
main:              f789265569013ebff254b082c2e0428970bdaf57
base PR #576:      0f6ea6eae813c1d867ae50744cf5fd57e2720bb7
PR #566:           2407b4ffe5024a2e3898922cf0b722d5cf69e496
parity audit #561: db9bdc63c855c6ddf664b763d748f8155a6a2c67
fixed-depth #568:  3a70470e3a8bbd60e0b7387ea46fd391cfb1d2e2
adaptive #569:     739ab0d9ab4975829dbed780670b1a4a56ca672e
Lorenz LP #575:    265c481ebd02807ab7d9a95cb0cf905a22c1876f
```

## New exact source theorem

Let `R` be the natural least-prime child operator, so the actual cumulative
parity source satisfies

```text
(I+R)F=b.
```

For any proposed contractive child operator `A`, the current required by

```text
(I+A)F=g_A
```

is exactly

```text
g_A = b-(R-A)F.
```

Thus a thinned `<1/8` operator does not turn the current into a local P61 Hall
packet. It leaves an all-depth signed residual `(R-A)F` that must be reconstructed
source-for-source.

The M-matrix premise is exactly

```text
g_A-A g_A = (I-A^2)F >= 0.
```

It is a global two-step parity-residual inequality, not a consequence of
injecting the child into a disjoint reserve.

## Exact disposition of PR #566

The abstract lemma `L-96652` is correct. Its two possible source
interpretations are not:

1. If `T=R`, then `g=b` and `g-Tg=(I-R^2)F` is precisely the depth-two current.
   The directed source artifact gives

   ```text
   5 B_(2,200000)(2)+3 B_(2,200000)(3)
   < -62.7181678185658877324.
   ```

   Hence the premise fails on the actual natural operator.

2. If `T=A` is the factor-67 contractive operator, then the consumed recursion
   needs `g_A=b-(R-A)F`. The published reserve injection does not derive this
   all-depth residual current. PR #576's reserve-versus-Hall-complement fixture
   is the finite-dimensional shadow of this exact missing term.

## New adaptive-depth theorem

For every even `L`,

```text
C_L(A)=sum_(j=0)^(L-1)(-A)^j g_A=(I-A^L)F.
```

Every fixed even depth for the natural operator is ruled out by the PR #561/#568
asymptotic. PR #569's source-mass depth uses `sum p^-1/2`; at the root it
eventually exceeds the complete rough-tree depth and becomes full expansion.

The critical row instead carries one factor `1/p` per rough prime. This packet
uses the exact annular P61 base from PR #576 and proves a genuinely
source-complete positive block. Set

```text
Z_X=(log X)^(1/4),
z=sum_(p0<=p<=Z_X) 1/p,
L=smallest even integer >=8(z+1).
```

For every admissible least-prime state `p0`, the exact current from histories of
length `<L` using only primes `p<=Z_X` is strictly positive for all sufficiently
large `X`. The proof keeps the literal finite-P61 annular packet `b(X/m)`, uses
`b(Y)=a*sqrt(Y)+O(1)`, Bonferroni positivity in the critical weights `1/p`, and
shows the complete source error is `X^o(1)` against a main term
`>>sqrt(X)/log Z_X`.

The depth is only `O(log log log X)`, while the full rough depth is
`~log X/log log X`.

## Sharp remaining theorem

The exact surviving producer is `LAPBR67`: prove nonnegativity of the
complementary depth-`L` current containing at least one rough prime larger than
`(log X)^(1/4)`, uniformly at every admissible state. The small-prime cube,
including all activation and finite-P61 remainders, is already closed.

```text
natural/thinned residual identity              PROVED EXACT
PR #566 natural M-matrix instantiation          FALSE
PR #566 contractive source identity             UNPROVEN / RESIDUAL OMITTED
all fixed even depths                           FALSE
source-weight adaptive depth                    VALID BUT ASYMPTOTIC FULL EXPANSION
exact small-prime critical cube                 PROVED POSITIVE
LAPBR67                                         OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```

## Replay

```bash
python3 experiments/X-97500-parity-resolvent/verify.py \
  --output experiments/X-97500-parity-resolvent/results/verification.json
sha256sum -c experiments/X-97500-parity-resolvent/SHA256SUMS
```

Expected:

```text
PASS_T97500_PARITY_RESOLVENT_AND_CRITICAL_DEPTH
```
