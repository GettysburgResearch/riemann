# T104530 handoff — genuine derivative-proportion transfer

## Binding correction

The `c<1` comparison in `L-104517` is not a proportion-transfer theorem.  Its
saddle analysis independently proves both adjacent high derivatives to be
`100%` real-rooted in the box.  `R-104513` withdraws that interpretation while
retaining the high-band theorem at its actual scope.

## Read order

1. `R-104513`
2. `L-104522`
3. `L-104523`
4. `L-104524`
5. `T-104530`
6. `X-104530`
7. the report

## Exact new implication

At the real zeros `c` of `Xi^(k)`, put

```text
rho_c = Xi^(k-1)(c) / Xi^(k+1)(c),
C_k   = (-sum rho_c)_+^2 / [R_k sum rho_c^2].
```

Then

```text
C_k >= (1+c)/2
AND
line proportion at level k >= p
AND
adjacent total-zero counts asymptotically agree

  -> line proportion at level k-1 >= c p.
```

The antecedent `p` is load bearing.  Changing `p` changes the conclusion
linearly, and the theorem does not prove `p` independently.

## Mean/variance form

If the residue distribution has negative mean `-mu` and second moment `nu`,
then

```text
c = 2 mu^2/nu - 1.
```

Equivalently, for squared coefficient of variation `v^2<1`,

```text
c = (1-v^2)/(1+v^2).
```

## Exact open theorem

```text
RCMV104530:

M1_k(T)^2 > (1/2+delta) R_k(T) M2_k(T)
```

for at least one fixed derivative level, where

```text
M1_k = -sum Xi^(k-1)(c)/Xi^(k+1)(c),
M2_k =  sum |Xi^(k-1)(c)/Xi^(k+1)(c)|^2
```

over the real zeros of `Xi^(k)`.

## New route to M1

`L-104524` proves for every finite polynomial approximation that the sum over
all critical residues equals minus the centred second moment of the complete
root cloud.  For symmetric Xi approximants, the real-critical first moment is
therefore:

```text
complete horizontal root variance
+ explicit nonreal-critical residue correction.
```

This leaves two focused analytic tasks:

1. show the nonreal-critical correction is lower order;
2. control `M2` by a mollified critical-point or phase-velocity mean value.

## Relation to the last-defect route

`RCMV104530` is a genuine partial-descent theorem and may be attacked
independently of the all-or-nothing gates `PRES104518` and `HARG104521`.
A positive result at one level converts any known derivative-line proportion
into a new lower-order proportion.  A uniform family with a nonvanishing
product of constants would supply a full cascade.

## Status

```text
residue-coherence transfer       PROVED EXACT
line proportion p is load bearing PROVED BY FORM OF THE IMPLICATION
critical-residue first-moment identity PROVED EXACT
RCMV104530                       OPEN
PRES104518 / HARG104521          OPEN
RH                               UNPROVED
```
