# Genus-two integral split locus in the frozen coefficient histograms

**Status:** exact bounded histogram transform, with theorem-import and
polarization firewalls.

**Scope:** the already-frozen monic squarefree quintic families at
`q=3,5,7`. The calculation visits the complete signed `(a_D,b_D)` histogram;
it enumerates no finite field, curve, or family member.

**Exact source:**
`research/l-families/atlas/function_field/balanced_control_family_scan.json`,
including its payload digest and complete-member ledger digests. The replay
also checks that the upstream producer still matches the source lock embedded
in that fixture.

**What was actually run:** integer discriminant and parity tests on 251
histogram atoms, exact Newton transforms through power 24, exact `Fraction`
aggregations, and deterministic normal/optimized tests. The guarded transform
counts every source-atom classification, atom-power step, detector-fiber/state
visit, tail pass, orbit-bucket visit, and output-ledger row and remains strictly
below 20,000 work units. Source parsing and constant-size dictionary
bookkeeping are outside that explicitly stated counter. There is no floating
point or random sampling.

**Smallest remaining gap:** an arithmetic count of integral trace-pair
multiplicities for general odd `q`, followed separately by an explicitly
imported Honda--Tate/Tate and polarization analysis if an isogeny or Jacobian
interpretation is wanted.

## 1. The exact polynomial predicate

Use the coefficient normalization

\[
 P(T)=1+aT+bT^2+qaT^3+q^2T^4.
\]

Set

\[
 \Delta=a^2-4b+8q.
\]

If `Delta=d^2` and `d` has the parity of `a`, put

\[
 r=\frac{-a-d}{2},\qquad s=\frac{-a+d}{2}.
\]

Then direct multiplication gives

\[
 \boxed{P(T)=(1-rT+qT^2)(1-sT+qT^2)},
 \qquad r+s=-a,\quad rs=b-2q.
\]

Conversely, any such integral factorization gives
`Delta=(r-s)^2`. Thus the complete classification is:

- `split_repeated`: `Delta=0`; here `r=s=-a/2` and the factor is
  repeated;
- `split_distinct`: `Delta>0` is a square with the correct parity; and
- `no_integral_q_elliptic_form_factorization`: every other case.

The last label is intentionally narrower than “nonsplit over `Z`.” It means
only that no factorization with both constant terms `+q` exists. For example,
the frozen `q=5`, `(a,b)=(0,-10)` row has

\[
 P(T)=1-10T^2+25T^4=(1-5T^2)^2,
\]

so it certainly factors over `Z`, but not into the `+q` elliptic-form
quadratics classified above.

For every split atom in the locked histograms, the replay also checks
`r^2<=4q` and `s^2<=4q`, so the two displayed quadratics have integral
Hasse-admissible elliptic-form trace data. The packet itself does not use that
inequality as an elliptic-curve realization theorem. The script reconstructs
all five coefficients from the two factors rather than trusting the
discriminant alone.

The monic reciprocal convention used elsewhere in this directory is the
reversal

\[
 X^4+aX^3+bX^2+qaX+q^2=(X^2-rX+q)(X^2-sX+q),
\]

so no sign convention changes between the two presentations.

## 2. Complete frozen census

An “atom” below is one signed coefficient pair `(a_D,b_D)` in the complete
source histogram. It is not a curve, an orbit, or a moduli point. Member
counts retain the source's uniform monic-squarefree-quintic weighting.

| `q` | repeated atoms / members | distinct split atoms / members | without integral `+q` elliptic-form factors: atoms / members | all split member fraction |
|---:|---:|---:|---:|---:|
| 3 | `0 / 0` | `9 / 27` | `23 / 135` | `1/6` |
| 5 | `3 / 15` | `20 / 690` | `58 / 1795` | `141/500` |
| 7 | `3 / 84` | `30 / 3486` | `105 / 10836` | `85/343` |

The committed JSON contains every split signed atom with its multiplicity,
`Delta`, integral trace pair, exact factorization, `B`, `F`, first two echo
coordinates, and any bounded cyclotomic certificate. A digest of the full
251-atom classification ledger binds the omitted complement rows as well.

These three fractions are a finite census. They are not values of a claimed
all-`q` formula, and the packet deliberately does not interpolate them.

## 3. `B` and `F` see geometry only imperfectly

The two coefficient controls admit exact discriminant coordinates:

\[
 \boxed{
 B=\frac{2qa^2-b^2}{q^2}
   =\frac{2\Delta}{q}-\frac{(b-4q)^2}{q^2}
 }
\]

and

\[
 \boxed{
 F=\frac{qa^2-b^2}{q^2}
   =\frac{\Delta}{q}-\frac{(b-2q)^2}{q^2}-4.
 }
\]

These identities explain why both controls correlate with trace collision,
but neither records whether `Delta` is a square. Exact detector fibers make
the loss visible:

| `q` | `B` fibers / mixed / members in mixed fibers | `F` fibers / mixed / members in mixed fibers | complete-echo fibers / mixed / members in mixed fibers |
|---:|---:|---:|---:|
| 3 | `14 / 1 / 12` | `12 / 1 / 24` | `17 / 1 / 12` |
| 5 | `33 / 3 / 246` | `24 / 6 / 700` | `39 / 1 / 6` |
| 7 | `55 / 5 / 2898` | `53 / 5 / 2856` | `67 / 2 / 924` |

A mixed fiber contains at least one integral `+q` elliptic-form split state
and at least one state without such a factorization. A fiber containing only
`split_repeated` and `split_distinct` labels is deliberately not counted as a
split-boundary collision. Thus no listed scalar detector is an exact indicator
of this locus.

The JSON also records, by factorization type, exact member means, sign
contingencies, and covariance with the split-locus indicator. These are finite
correlations, not causal or asymptotic statements.

## 4. Even the complete balanced echo does not recover splitting

For the Frobenius-power controls `B_r`, the exact order-four recurrence shows
that the infinite echo sequence is determined by `(B_1,B_2)`. The replay
independently obtains `B_1,...,B_8` by Newton identities and compares them with
that recurrence on every source atom.

The mixed echo fibers in the preceding table are therefore stronger than
collisions at a finite truncation: they are collisions of the complete
balanced echo. In particular, adding higher `B_r` cannot separate states on
opposite sides of the integral `+q` elliptic-form split criterion. This is a
detector limitation, not a claim that their full Frobenius polynomials agree.

## 5. Cyclotomic normalized spectra cross the split boundary

For each atom the script looks for an even `n<=24` such that the powered
Frobenius polynomial is exactly

\[
 (X-q^{n/2})^4.
\]

This is a positive certificate that every normalized Frobenius root is an
`n`-th root of unity. Failure to find such an `n` is only bounded
nondetection, not proof of a noncyclotomic spectrum.

The certified twist-quotiented states are:

| `q` | `(a_D^2,b_D)` | integral `+q` elliptic-form classification at `q` | members | least even certificate power |
|---:|:---:|:---|---:|---:|
| 3 | `(0,0)` | no integral `+q` elliptic-form factors | 12 | 8 |
| 3 | `(9,6)` | distinct split | 6 | 12 |
| 5 | `(0,-10)` | no integral `+q` elliptic-form factors | 1 | 2 |
| 5 | `(0,0)` | no integral `+q` elliptic-form factors | 50 | 8 |
| 5 | `(0,10)` | repeated split | 5 | 4 |
| 5 | `(25,15)` | no integral `+q` elliptic-form factors | 24 | 10 |
| 7 | `(0,0)` | no integral `+q` elliptic-form factors | 336 | 8 |
| 7 | `(0,14)` | repeated split | 42 | 4 |

So “normalized root-of-unity spectrum” and “integral elliptic factorization
over the ground field” are genuinely different predicates. The `q=5` state
`(25,15)` is also a useful check that a short periodic-echo list need not
exhaust the cyclotomic certificates.

## 6. Extreme and tail behavior

The minimum `F` atoms reproduce three different Frobenius shapes:

| `q` | minimum `F` | members at the minimum | split classification |
|---:|---:|---:|:---|
| 3 | `-8/3` | 6 | distinct split |
| 5 | `-116/25` | 10 | repeated split |
| 7 | `-282/49` | 42 | no integral `+q` elliptic-form factors |

Thus the negative tail is not uniformly an endoscopic or collision-wall
phenomenon. The JSON records, for both `B` and `F`, exact split-locus,
repeated-locus, minimum-fiber, and absolute-extreme shares of absolute moments
of orders `2,4,6,8,10,12`. It also records the full `F<-4` contingency and the
`B=+-4` endpoint contingencies. These calculations are cheap histogram sums;
they do not posit a tail law.

## 7. What the aggregated orbit data identify

The source proves that its affine action sends `a_D` to `+-a_D` and fixes
`b_D`; hence the split predicate is constant on an affine orbit. For the mixed
`B` buckets needed here, however, the committed balanced fixture retains only
the grouped orbit counts, although separate endpoint records elsewhere retain
some individual representatives. Several `B` fibers mix the two sides of the
`+q` elliptic-form split criterion among `(a_D^2,b_D)` states. The exact
split-orbit assignment inside those fibers has therefore been discarded.

The replay reports:

- exact member-weighted and signed-atom-weighted split counts;
- exact split-orbit contributions from `B` buckets homogeneous in splitting
  type; and
- rigorous lower and upper bounds in each mixed bucket, using only that an
  orbit has between `1` and `q(q-1)` members.

It does not invent a uniform-orbit count. Recovering the exact orbit-weighted
law where the bounds remain non-singleton would require a per-orbit invariant
table or a new member/orbit enumeration, both outside this task. In fact the
aggregate constraints already force exact totals for the first two fields:

| `q` | split affine-orbit count | uniform-orbit fraction | status |
|---:|---:|---:|:---|
| 3 | `5` | `5/29` | forced exactly by the aggregates |
| 5 | `38` | `19/66` | forced exactly by the aggregates |
| 7 | `86..88` | `86/349..88/349` | not identifiable inside two mixed `B` buckets |

The `q=7` interval survives a stronger audit using every retained orbit-size
and state-total constraint. Globally there are 12 orbits of size 21 and 337 of
size 42. Each of the two ambiguous buckets, `J=-100` and `J=-4`, must contain
exactly two size-21 orbits. Assigning those two orbits to the split or
complement states realizes the endpoint alternatives independently, so all
three totals `86,87,88` remain compatible with the retained aggregates. The
interval therefore reflects genuinely discarded assignment data, not merely
the producer's coarser `1..q(q-1)` bound.

## 8. Isogeny and polarization firewall

The word “endoscopic” in the filename is an operational label for the
integral `+q` elliptic-form quadratic-factor locus. The packet itself proves
only this particular polynomial factorization.

Turning that factorization into the statement that an abelian surface lies in
an `F_q` product isogeny class uses Honda--Tate/Tate theory. That theorem is
not imported or reproved here, so the JSON labels it as an interpretation
target. Even after such an import:

- an unpolarized isogeny to `E_1 x E_2` does not identify the canonical
  principal polarization with the product polarization;
- it does not make the smooth genus-two curve a product;
- it does not by itself exhibit elliptic quotient maps or curve
  involutions; and
- failure of the integral `+q` elliptic-form criterion at `q` does not prove
  geometric simplicity, because decomposition may appear after a finite
  extension.

No family-level endoscopic monodromy component, Honda--Tate realization
classification, principal-polarization theorem, all-`q` frequency, or
equidistribution law is asserted. Nothing here has an RH or GRH consequence.

## 9. Replay

```text
python research/l-families/atlas/function_field/genus2_endoscopic_split_locus.py --check
python -m unittest tests.test_genus2_endoscopic_split_locus -v
python -O -m unittest tests.test_genus2_endoscopic_split_locus -v
```

The output payload locks the exact input payload and member ledgers, the input
producer, this producer, this note, and the focused test by LF-normalized
SHA-256. The output then hashes its own canonical payload.
