# Target-Hall residual source and fixed-67 contraction

Date: 2026-08-13  
Live parent: PR `#399` at `22d7f2f3f3668f664c09708838f6a738e4398eef`  
Integrated producer source: PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Working PR: `#424`  
Verdict: **major exact reduction and candidate complete factor-54 composition; RH remains unproved**

## 1. The conceptual mistake removed

A Hall-projected finite row was being treated as one indivisible object.  That
made recursive type stability appear to require carrying every matched Hall
edge, its next-prime color and its row correction through all later generations.

The correct decomposition is:

```text
target-bearing positive residual source measure
+
target-null positive matched-edge row bonus.
```

For target transport `t_(o,e)` from an odd node `o` to a no-larger even node
`e`, define

```text
c_e = a_e - sum_o t_(o,e)/T(e).
```

Then exactly:

```text
T(c) = signed target;
S(c) >= signed score;
signed row = R(c) + sum_(o,e)t_(o,e)[R(e)/T(e)-R(o)/T(o)].
```

The final sum is coefficientwise nonnegative by normalized row monotonicity.
Thus `c` is the hereditary source; the final sum is current-generation packing.

This is `L-91545`.

## 2. Both binary branches become ordinary positive source types

The target-exact survival/hazard producer of `L-91452/L-91454` has been
transplanted from PR `#416` onto the live PR `#399` descendant.  Applying
`L-91545` gives positive residual measures `c_s,c_h` satisfying

```text
T(c_s)+T(c_h)=T_parent;
S(c_s)+S(c_h)>=S_parent;
R_parent=R(c_s)+R(c_h)+B_s+B_h,
B_s,B_h>=0.
```

The matched Hall edges no longer appear in the recursive state.

## 3. Arithmetic provenance is no longer needed after entry

Both residual measures are positive paired kernel types at the parent endpoint.
Apply the same deterministic split

```text
theta(n)=1_(n<=X/67)
```

to each.  Endpoint monotonicity gives positive target, score and row residuals;
both children are at `X/67`; and their target weights sum to at most one.

Consequently the proof no longer uses:

```text
an ordered survival product over all rough primes;
unique-next-prime color transport after Hall;
variable-p affine normalization of the hazard child;
repeated Hall projections in later generations.
```

Only the fixed scale-67 affine functor and one-use quantizer remain.  This is
`L-91547`.

## 4. Exact auxiliary results banked on PR #424

```text
L-91540  hereditary paired positive kernel branching;
T-91541  actual-packet target-normalized consumer;
L-91542  exact scalar transfer normal form between arithmetic and binary splits;
L-91543  first asymmetric post-entry contraction;
L-91544  prime-uniform target-normalized row density;
L-91545  Hall residual source + target-null row bonus;
T-91546  candidate complete composition with hostile audit ledger;
L-91547  symmetric fixed-67 contraction of both residual types.
```

The normative post-entry route is now `L-91545 -> L-91547 -> T-91541`; the
older asymmetric placement in `L-91543` is retained as a valid but unnecessary
alternative.

## 5. Verification

Retained exact replays include:

```text
PASS_SURVIVAL_HAZARD_BINARY_RETURN             54 checks
PASS_BINARY_BRANCH_CHANNEL_PROJECTION          38 checks
PASS_PAIRED_KERNEL_TYPED_BRANCHING           2011 checks
PASS_BINARY_TRANSFER_NORMAL_FORM               12 checks
PASS_HALL_RESIDUAL_HEREDITARY_SOURCE        18004 checks
```

The new Hall residual replay uses exact `Fraction` arithmetic on 1000 finite
Hall networks and checks target exactness, score superordination and two
independent row bonuses.

These replays certify finite algebra and imported diagnostics.  They do not
replace a merged directed arithmetic replay.

## 6. Remaining audit after the fixed-67 simplification

The live frontier is now the following fixed diagram:

```text
current P61/P79 terminal signed channel
  -> transplanted target-Hall survival/hazard producer
  -> positive residual sources c_s,c_h + positive row bonuses
  -> fixed 67 split of c_s and c_h
  -> fixed affine lift / one sum-before-quantize collar
  -> target-normalized branching loss recurrence.
```

The mandatory checks are:

1. rerun the directed survival/hazard Hall margins and row monotonicity on the
   merged live tree;
2. check the fixed-67 affine scaling against the exact typed loss definition;
3. check the target-null binary correction and Hall row bonuses consume one
   common endpoint port, not one per type;
4. reconstruct the native loss recurrence term by term against PR `#352`.

No variable-prime recursive theorem remains.

## 7. Scientific boundary

```text
abstract Hall residual source theorem              PROVED
recursive type stability                           CLOSED
post-entry contraction of every target source      CLOSED
candidate complete factor54 reset                   WRITTEN
merged producer/loss audit                          OPEN
Riemann Hypothesis                                  UNPROVED
```
