# Factor-67 all-column reserve and square-root thinning report

## Freeze

```text
repository:       gfreund123/riemann
reviewed PR:      #473
reviewed head:    71d6a859ea741fe035de709e8d10ed37301b778e
mass supplement: PR #476 / L-91694
report date:      2026-08-14
```

## Finding

The explicit compact reserve in the reviewed factor-67 proposal divides the
physical columns into an interior estimate starting at `q>=K` and a terminal
estimate at `q>X/4`. The B-spline collar and finite mismatch can still feed
columns `2<=q<K` through multiples `jq>=K`. The displayed `177/K` estimate
therefore did not, by itself, prove all-column native feasibility.

This is a coverage gap in the proof, not a numerical counterexample to SONTR.

## Repair

Write the finite mismatch as adjacent local errors

\[
 \varepsilon_X(n)=E_X(n)-E_X(n+1).
\]

The exact carry is a sum of these cells. Assign cells `n<K` to the exact inner
recursive packet and cells `n>=K` to the current outer mismatch. The frozen
factor-67 bound

\[
 |\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}
\]

then yields, for every physical column,

\[
 |v_q^{\rm out}(E_X)|<\frac{57}{2q\sqrt K},
\]

\[
 |\mathcal D_4v_q^{\rm out}(E_X)|
 <\frac{171}{4q\sqrt K}.
\]

Adding the existing collar bound gives

\[
 |\mathcal D_4v_q(C_X-E_X^{\rm out})|
 <\frac{971}{4q\sqrt K}.
\]

For `2<=q<=X/4`, this is less than

\[
 \frac{129}{\sqrt K}\Omega_X(q).
\]

Use one positive common-parent thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

It leaves the explicit strict reserve

\[
 s_X(q)>\frac{\Omega_X(q)}{\sqrt K+130}
\]

in every nonterminal physical detail column.

## Cost and compatibility

The new thinning is stronger than the original `K/(K+178)` factor for every
`K>=2`, so it cannot hurt the terminal omission proof. Since the root Hall
packet is score-superordinate to `4sqrt(X)` and `K>X/67`, the additional
equality-score loss is below `4290`.

The scaling is applied once to the complete labelled parent measure. It
preserves source ownership, the one common port, and the mass-weighted child
contraction. For the last statement the correct input is `L-91694`, not an
unweighted sum of fiberwise coefficient lists.

## Replay

```bash
cd experiments/X-91723-factor67-all-column-reserve
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_ALL_COLUMN_SQRTK_RESERVE
```

The exact proof-object digest is recorded in `results/verification.json`.

## Honest boundary

```text
new all-column constant algebra                   PROVED EXACT
small-column ownership split                      PROVED ON FROZEN CARRY IDENTITY
new square-root thinning                          PROVED EXACT
bounded score cost                                PROVED EXACT
frozen Hall/port/terminal/direct-integral stack    RECONSTRUCTION REQUIRED
SONTR / NRCT                                       CONDITIONAL PROPOSAL
Riemann Hypothesis                                 UNPROVEN
```
