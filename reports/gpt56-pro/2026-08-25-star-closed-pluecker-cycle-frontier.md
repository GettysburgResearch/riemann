# Star-closed Plücker-cycle continuation

## Result

The minimum-owner/equal-pair gauge correction of `L-102961` has two orthogonal pieces:

```text
radial star;
row-zero cycle.
```

The radial star is now closed without an arithmetic estimate.

Its vertex potential is

\[
s_1=s_2=1/k,
\qquad
s_i=-2/[k(k-2)]\ (i\ge3),
\]

which is nonincreasing along the ordered prime labels and has zero sum. Hence

\[
\sum_i s_iC_i
={1\over k}\sum_{i<j}(s_i-s_j)(C_i-C_j)
\]

with every active coefficient nonnegative and every active edge directed from a smaller prime to a larger prime. The common-mother Wronskian theorem therefore orients the complete native endpoint term pointwise. The squared endpoint term is already polylogarithmic.

## Exact cycle normal form

The remaining row-zero cycle is

\[
c={1\over(k-1)(k-2)}
\sum_{3\le i<j\le k}R_{ij},
\]

where

\[
R_{ij}=2e_{12}+2e_{ij}-e_{1i}-e_{1j}-e_{2i}-e_{2j}.
\]

Every coefficient in this rectangle expansion is positive. Each `R_ij` is a sum of two elementary four-label Plücker bipartitions.

Thus the concentrated-owner route has been reduced from an arbitrary owner curl to one uniform positive family of symmetric four-label rectangles.

## Frontier

```text
PLC103020:
  the order-inverting row-zero Pluecker rectangle current has subpower
  logarithmic negative mass after exact middle-Euler and boundary
  recombination.
```

Then

```text
PLC103020
 -> COCURL102980
 -> OICP102960
 -> HMO102940
 -> RH.
```

The canonical equal-pair route `BCI102990` remains parallel.

```text
radial star current       CLOSED ONE-SIDED
row-zero cycle formula    PROVED EXACT
positive rectangle mix    PROVED EXACT
PLC103020                 OPEN / RH-BEARING
BCI102990                 OPEN / RH-BEARING
RH                         UNPROVED
```