# Adversarial response to PR #405

Date: 2026-08-12  
Frozen review head: `97d40e6574ba54d827fd361c70d550eeb60c9faf`  
Frozen source head: `8d32d9b6353e8b18ec1786ad939803d4d606bf2c`  
Status: **the fatal submitted-composition counterexample is correct; one secondary gap is repaired; one local source-partition interface is strengthened; RH remains unproved**

## 1. Review point accepted

The review's exact identity

\[
 wN(s)N(r)-wM(s)M(r)
 =\bigl(0,12rs(1-r)(1-s)\bigr)
\]

is correct. The complete-proof composition at `4981bcd...` cannot use
one-factor SHARP preservation as an arbitrary-cascade identity.

`R-91304` strengthens the diagnosis. Both matrix families have fixed
simultaneous diagonalizations, so the complete cascade error is explicit. It is
componentwise nonnegative but can grow without a bounded scalar port. The
submitted two-state completion is therefore not repairable by simply enlarging
the old finite slack constant. The live four-state arithmetic semigroup is the
correct state carrier.

## 2. Review point repaired: real-column terminal omission

The review correctly rejected the pointwise extension of the integer-column
endpoint derivative bound. That derivative can approach zero in a partial
last unit cell.

The terminal conclusion nevertheless survives by changing the packet, not by
reasserting the false derivative claim. `L-91329` proves for every complete
integer endpoint atom and every real terminal column

\[
 \overline\Gamma_T(q)>\frac25T^{-3/2}.
\]

The exact discrete top omission of width `W=100000` consequently contributes
more than

\[
 40000X^{-3/2},
\]

which dominates the complete fractional terminal error coefficient `28836`.
Thus the secondary terminal real-column gap in PR #405 is closed by a different,
valid argument.

## 3. Review interface narrowed: native SHARP source at one reset

PR #405 classifies the native endpoint-block interpretation of `L+2R` as wholly
unproved. `L-91330` proves the exact one-reset version without the false
completed cascade.

The SHARP atom splits pointwise as

\[
 w_\Psi
 =(1+\kappa_*)w_{a_*}+(2-\kappa_*)w_1,
\]

with both summands positive and separately labelled. The balanced and reserve
Hall transports use these disjoint source shares and both have no-upward support.
A universal extension of the normalized component-row monotonicity from `a=1`
to every `a>=1` then lifts both transports directly to the exact finite rows.

Hence source duplication is absent **at each individual factor-54 reset
boundary**. This does not yet prove that the positive four-state children
presented by all rough generations assemble into the required recursive source
partition.

## 4. One-new-prime projection is also closed locally

The live branch correctly emphasizes that the rough tree contracts after one
new least prime. In that exact one-prime situation the post-prime SHARP state
has the special form

\[
 \Psi_p=3(1-p^{-1/2})U_{a_p},
 \qquad
 a_p=\frac43(1+p^{-1/2})\in(4/3,3/2).
\]

`L-91331` proves a uniform no-upward Hall margin greater than `1/10` for every
channel parameter in the complete interval `[4/3,3/2]`, and the universal
row-profile theorem lifts that Hall transport directly to every exact finite
row. Hence the local projection after **one** new rough prime is no longer part
of the open theorem.

The remaining issue is the exact all-generation identification: the
least-prime/four-state child measures must be shown to arrive at successive
reset boundaries in precisely this effective channel, with residual even mass,
target shares, Schur packets and score charged once.

## 5. Corrected proof frontier

The corrected DAG is now:

```text
positive four-state rough semigroup                    exact
linear total-variation telescope                       exact
one-reset balanced/reserve atomwise source split       proposed complete
one-reset exact finite-row Hall projection             proposed complete
one-new-prime effective-channel projection              proposed complete
fractional terminal omission                           proposed complete
all-generation child-source compatibility              open
coefficient-one target/capacity and score recurrence   open / RH-bearing
RH                                                     unproved
```

The first remaining theorem is more specific than the review's broad box:

> Show that the exact least-prime four-state child measures arriving at one
> reset are precisely the disjoint inputs of the balanced/reserve projection of
> `L-91330`, with the residual even measures becoming the source state of the
> next reset and every affine target share charged once.

The local source split, exact row lift, and fractional terminal packet no longer
belong to that open theorem.

## 6. Repository hygiene

The review is correct that `L-91320`, `L-91324`, and `L-91325` are duplicated.
The new files use fresh IDs and exact path dependencies. Canonical extraction
should renumber the older collisions before integration.

## 7. Status

```text
submitted full composition at 4981bcd...        false
review's cascade counterexample                  verified
review's pointwise fractional objection          verified
review's terminal conclusion gap                 repaired by L-91329
one-reset native SHARP source partition          strengthened by L-91330
all-generation rough recursion                   open
Riemann Hypothesis                               unproved
```
