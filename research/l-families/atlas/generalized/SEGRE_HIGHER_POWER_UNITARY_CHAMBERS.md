# Higher-power Segre unitary chambers and an open cubic torus chamber

Status: preregistered bounded higher-power extension; analytic algebraic proofs
and exact replay under construction. No global L-function or RH claim.
Base: 4a317ea5c9d7aa016fba58a1d74746e437329ec7.

## Held-out power-six record

This section is committed before computing the m=6 reciprocal numerator or
its discriminant/chamber table. Powers m=4 and m=5 have already been
constructed in an in-memory exact symbolic scout; those are discovery data,
not held-out predictions.

The general exponential expansion predicts denominator
D_13=product_(j=-6)^6(1-t^j T), generically reduced on the self-dual slice,
with reciprocal numerator degree ten. The reciprocal polynomial M_6(x,z)
has degree five in z. These statements will be proved for every positive m,
not inferred from this control.

Source-derived torsion predictions, before m=6 construction:

- At x=-1, M_6=(-2+z)^2(1+z)^3 and the reduced series is 1/(1-T^3).
- At x=0, M_6=z^2(z-2)(z+2)^2 and the reduced series is
  1/[(1-T)(1+T^2)].
- At x=1, the reduced numerator is 1+63T+T^2 and the denominator
  is (1-T^6)/(1+T). It is not pure.

A deliberately falsifiable extrapolation from the first tables is that
the m=6 purity set is contained in the m=5 purity set and has five
interval components. This is a test question, NOT a theorem.
Five preselected rational membership controls, using the m=5 verdicts
as the provisional m=6 predictions, are

| x | provisional m=6 pure verdict |
|---|---|
| -49/30 | false |
| -3/2 | true |
| -1/2 | true |
| -2/5 | false |
| -1/4 | true |

Every failed prediction must remain visible. No endpoint or rank will be
selected after the m=6 computation to make this record appear successful.

## Separately labeled structural cubic target

At x=-3/2 the cubic numerator from the frozen parent is
P=1-T+(13/8)T^2-T^3+T^4.
Its reciprocal z roots are (1+-sqrt(5/2))/2, both in (-2,2).
The degree-seven universal numerator is
P(1-T)(1+3T/2+T^2).

Prove all seven unit roots are distinct, then use determinant-one unitary
conjugate reciprocity and local uniqueness of roots to obtain an OPEN
two-parameter unitary-torus purity chamber. Every such neighborhood must
contain generic denominator-order-ten inputs. This must be distinguished
from fixed-A self-duality on the original one-parameter slice.
