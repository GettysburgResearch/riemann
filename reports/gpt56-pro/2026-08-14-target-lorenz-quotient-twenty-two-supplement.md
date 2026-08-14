# Target-Lorenz quotient-twenty-two supplement

## Freeze

```text
repository:       gfreund123/riemann
parent PR:        #468
parent head:      a41f81466f85d52597c97b41505756a8860698d0
successor branch: research/gpt56-pro/91685-target-lorenz-vector-primal-dual
review date:      2026-08-14
```

**RH remains unproved.** This supplement strengthens the low-quotient row
campaign from quotient five to quotient twenty-two and records the exact point
where the stronger one-atom shortcut ceases to work.

## Directed theorem

For every nonvacuous row and every real endpoint in

\[
 \max(67,5j)\le x\le22j,
\]

the directed certificate proves

\[
 Q_x(j)>
 \sum_{d\in\{2,3,5,7,11,13,17,19\}}
 d^{-1/2}Q_{x/d}(j).
\]

All activation walls are integers. Between consecutive walls the difference is
`A log(x)+B`, so integer endpoint signs certify each complete continuum cell.
The replay checks `37,303` endpoints. Its smallest lower interval is

```text
0.0001614750920097278923...
at j=66, x=1452=22j.
```

Because `x/p<j`, no child row is active. If the odd target fits inside atom
`d=1`, row-per-target ordering closes the row. If it does not, the leftmost
producer uses all of atom `1`, and the directed inequality closes the row.
Thus the actual Target-Lorenz row gate holds through quotient twenty-two.

## Exact firewall at quotient twenty-three

At

```text
j=44,
x=1012=23j,
```

the same atom-one difference has a directed upper endpoint below

```text
-0.0003543982654283312355.
```

This does not refute Target-Lorenz. It refutes only the stronger proof that atom
`1` alone pays every odd row. Above quotient twenty-two, later even atoms in the
actual leftmost target submeasure are load bearing.

## Remaining arithmetic choices

```text
sharp route:       certify R_j(U)-O_R^(j) directly;
stronger route:    certify O_T E_R^(j)-E_T O_R^(j);
fail-closed route: produce an exact L-91685 support-function separator.
```

The full determinant is sufficient but not necessary. Only a negative sharp
margin, equivalently its cutoff separator, rules out all common-source
coefficients in the literal source box.

## Replay

```text
PASS_P19_ODD_ROW_PREFIX_THROUGH_QUOTIENT_TWENTY_TWO
b7058883cf97b033f0d22d9864c09b4c73b844746d5878c5f2a2cbb240c6580e

PASS_ATOM_ONE_QUOTIENT_TWENTY_THREE_FIREWALL
138e315bfd1baf5511cf3066efc27aeba4a0cc2bf4090ce1cc8594d114511ff7
```

## Boundary

```text
Target-Lorenz row gate py/j<=22             PROVED
atom-one extension to quotient 23           REFUTED
full Target-Lorenz gate above quotient 22   OPEN
native one-use root crosswalk                OPEN
Riemann Hypothesis                          UNPROVEN
```
