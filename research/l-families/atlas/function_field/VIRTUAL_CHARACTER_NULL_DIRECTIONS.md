# Virtual-character null directions on `USp(4)`

**Status:** DRAFT exact bounded search and all-order compact-group
certificates; independently replay-audited.

**Scope:** `USp(4)` only.  The finite searches below use exact integer
Laurent polynomials and the Weyl constant-term formula.  They do not sample,
integrate numerically, enumerate a finite field, or assert convergence of an
arithmetic family.  `USp(6)` was deliberately not searched: the completed
`USp(4)` panels already reached the resource boundary chosen for this pass.

Run the frozen replay with

```text
python research/l-families/atlas/function_field/virtual_character_null_directions.py --write
python research/l-families/atlas/function_field/virtual_character_null_directions.py --check
python -m unittest tests.test_virtual_character_null_directions
```

## Result in one sentence

After quotienting the tautological `e_1e_3=e_1^2` redundancy, the primitive
coefficient-square null direction is uniquely

\[
B=2e_1^2-e_2^2=\chi_{2\omega _1}-\chi_{2\omega _2},
\]

and it is the only non-central survivor in each frozen low-weight panel; it is
locally isolated in those panels but globally generates an infinite exact
residue-null module.

## 1. The coefficient-square lattice is solved without a search

For `USp(4)`, symplectic reciprocity gives `e_3=e_1`.  Also

\[
\operatorname{Haar}(e_1^2)=1,\qquad
\operatorname{Haar}(e_2^2)=2,\qquad
\operatorname{Haar}(e_1e_3)=1.
\]

Thus a raw coefficient triple `(a,b,c)` has zero first moment precisely when

\[
a+2b+c=0.
\]

Writing `t=-b` and `s=c` gives the full integer lattice

\[
(a,b,c)=t(2,-1,0)+s(-1,0,1).
\]

The second generator is zero as a class function, while the first is `B`.
Consequently every first-moment-null element of
`Z e_1^2 + Z e_2^2 + Z e_1e_3` is an integer multiple of `B`, and hence has
an exactly symmetric Haar pushforward.  In the quotient by class-function
relations, this is one primitive line, not a higher-dimensional cone.

The character identities used by the checker are

\[
e_1^2=1+\chi_{\omega _2}+\chi_{2\omega _1},
\]

\[
e_2^2=2+2\chi_{\omega _2}+\chi_{2\omega _1}+\chi_{2\omega _2},
\]

so subtraction immediately gives the displayed virtual-character formula
for `B`.

## 2. Two mechanisms for exact symmetry

### The central odd sector

Multiplication by the central element `-I` preserves Haar measure.  In `C_2`
fundamental coordinates,

\[
\chi_{a\omega _1+b\omega _2}(-U)=(-1)^a
\chi_{a\omega _1+b\omega _2}(U).
\]

Therefore every integer combination of characters with odd `a` has an
exactly symmetric pushforward and all odd Haar moments vanish.  This is a
graded representation-ring mechanism, not an accidental finite-moment zero.

### The non-central residue sector containing `B`

Put

\[
u=x_1^2+x_1^{-2},\qquad v=x_2^2+x_2^{-2}.
\]

Direct expansion gives

\[
B=-uv.
\]

Every exponent in `B` is congruent to `(2,2)` modulo `4Z^2`.  An odd power
has the same residue.  The `C_2` Weyl density has zero coefficient at all
four possible support points `(\mathord\pm2,\mathord\pm2)` in that residue
class, so the Weyl constant term of every odd power is zero.  Since `B` is a
bounded continuous class function, vanishing of all odd moments is
equivalent to symmetry of its compactly supported pushforward measure.

This mechanism is not confined to one vector.  Both
`u^2+v^2` and `u^2v^2` have exponent support in `4Z^2`; hence every element of

\[
\boxed{
\mathcal N_B
=B\,\mathbb Z[u^2+v^2,u^2v^2]
}
\]

has support in `(2,2)+4Z^2` and therefore has an exactly symmetric Haar law.
These Weyl-invariant integral Laurent polynomials are virtual characters.
Thus `B` is the lowest-degree generator of a certified infinite null module.
No claim is made that this module exhausts every symmetric virtual character.

For `B` itself the same constant-term calculation gives the stronger closed
formula

\[
\operatorname{Haar}(B^{2r})
=\frac{1}{r+1}\binom{2r}{r}^{2},\qquad
\operatorname{Haar}(B^{2r+1})=0.
\]

## 3. Frozen exhaustive panels

The word *exhaustive* below applies only to the explicitly bounded boxes.
Vectors are primitive, identified up to overall sign by requiring their first
nonzero coordinate to be positive, and constrained by the stated `L1` cap.
An exactly symmetric direction must pass every finite odd-moment screen, so
the screens give valid exclusions inside each finite box.  Every survivor is
then upgraded to an all-order certificate by one of the two mechanisms above.

| panel | ordered basis | coefficient/L1 cap | exact odd moments screened | survivors |
|---|---|---:|---:|---|
| square-character span | `1, chi_01, chi_20, chi_02` | `abs(c_i)<=2`, `L1<=5` | `1,3,5,7,9` | only `chi_20-chi_02=B` |
| central extension | preceding basis plus `chi_10, chi_11, chi_30` | `abs(c_i)<=1`, `L1<=4` | `1,3,5,7` | all 13 primitive sign classes in the three-dimensional center-odd box, plus `B` |
| even weight-four extension | first basis plus `chi_21, chi_40` | `abs(c_i)<=1`, `L1<=4` | `1,3,5,7` | only `B` |

Here `chi_ab` means `chi_(a omega_1+b omega_2)`.  The second row contains
exactly `(3^3-1)/2=13` center-odd sign classes.  No mixed central-even/odd
direction survives.  The third row shows that adjoining the next two
center-even irreducibles does not produce another candidate at this cap.

This yields the intended distinction:

- `B` is isolated among non-central directions in the completed low-weight
  boxes and is the unique primitive coefficient-square direction after
  quotienting reciprocity;
- `B` is not isolated in the full representation ring, because
  `mathcal N_B` is an infinite exact-symmetry module; and
- the much larger center-odd graded sector is independently symmetric under
  the group involution `U -> -U`.

## 4. Exactness and stopping boundary

The producer obtains irreducible characters with the existing capped `C_2`
Kostant engine, reconstructs all displayed coefficient identities as Laurent
polynomials, builds the Weyl density exactly, and evaluates each screened
moment as an integer constant term divided by the Weyl order eight.  A separate
positive-root product reconstructs the *complete* density and must agree with
the dependency term by term; the producer then checks its full support, not
only the four smallest representatives, against the forbidden `(2,2) mod 4`
residue.  The test repeats that independent reconstruction.

The run stops at the three declared panels.  It does not extrapolate a
finite-moment coincidence outside them, search higher weights, or test
`USp(6)`.  There are no finite-field claims in this packet.
