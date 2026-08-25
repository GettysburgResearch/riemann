# Guarded cohomology-conjecture inference

**Status:** exact protocol, exact finite-data no-go, and certified
small-coefficient candidates. No genus-two cohomology or eigenform
identification is claimed.

The replay is `guarded_cohomology_conjecture_inference.py`; the focused tests
are `tests/test_guarded_cohomology_conjecture_inference.py`. The generator
reads genus-one and genus-two fixtures protected by both an externally pinned
file digest and their internal canonical payload hash, but it does not
enumerate a field or query a modular-form database.

## 1. The inference contract

The tool treats the following operations as logically separate.

1. **Character decomposition.** Expand the detector on a maximal torus and
   perform exact highest-weight subtraction. This is representation algebra.
2. **Weight envelope.** State only weight bounds that follow *conditionally*
   from a named geometric adapter and purity hypothesis. This is not a
   cohomological decomposition.
3. **Ambiguity accounting.** Return every continuation allowed by the finite
   observations and the declared algebraic envelope. Never return only the
   prettiest fit.
4. **Recurrence audit.** Test a Frobenius-power recurrence only on powers of
   one characteristic. Values at three different primes are not a recurrence
   test.
5. **Identification gate.** Attach an automorphic or cohomological name only
   when an exact trace identity, exact geometric adapter, one-dimensional
   target space, and unique normalization are all present.

The genus-one tenth moment passes this gate. All three genus-two channels fail
it. This asymmetry is intentional.

## 2. Exact three-point ambiguity theorem

Let values be known at `q=3,5,7` and set

\[
 V(X)=(X-3)(X-5)(X-7)=X^3-15X^2+71X-105.
\]

Suppose the unique quadratic interpolant `P0` has integral coefficients. For
every `D>=3`, the complete set of integral polynomials of degree at most `D`
having the same three values is

\[
 \boxed{P_0(X)+V(X)Q(X),\qquad Q\in\mathbb Z[X],\quad
        \deg Q\le D-3.}
\]

This is an equality, not merely a supply of counterexamples. If `P-P0`
vanishes at the three integers, its successive division by the three monic
linear factors stays in `Z[X]`. Conversely, every displayed polynomial has
the same samples. Thus the ambiguity lattice has rank `D-2`.

For a character of local-system weight `w`, the normalized integer controls
used here are

\[
 T_\lambda(q)=
 {q^{w/2}\over q(q-1)}
 \sum_{D\in\mathcal H_5(q)}\chi_\lambda(D).
\]

The source-locked means give the following complete certificates.

| channel | exact samples at `3,5,7` | minimal cap used | `P0(X)` | complete ambiguity | nominated `Q` |
|---|---:|---:|---|---|---|
| `chi_(0,3)` | `74, 614, 2386` | 4 | `154X^2-962X+1574` | `P0+V(a+bX)` | `15+X` |
| `chi_(2,2)` | `37, 213, 621` | 3 | `29X^2-144X+208` | `P0+aV` | `2` |
| `chi_(0,4)` | `-19, -51, -99` | 3 | `-2X^2-1` | `P0+aV` | `0` |

Consequently, none of

\[
 T_{0,3}=q^4-2q-1,
 \qquad
 T_{2,2}=2q^3-q^2-2q-2,
 \qquad
 T_{0,4}=-(2q^2+1)
\]

is forced by the three fields. This remains true even inside the displayed
small degree envelopes.

### A positive statement about coefficient simplicity

The generator exhausts the complete integral coefficient `L1` ball up to the
norm of each nominated polynomial. It certifies:

| channel | coefficient dimension | vectors checked | minimum `L1` | all minimizers |
|---|---:|---:|---:|---|
| `chi_(0,3)` | 5 | 681 | 4 | `(-1,-2,0,0,1)` |
| `chi_(2,2)` | 4 | 2,241 | 7 | `(-2,-2,-1,2)` |
| `chi_(0,4)` | 4 | 129 | 3 | `(-1,0,-2,0)` |

Hence each nominated formula is the **unique minimum-`L1` integral
continuation** within its stated cap. The certificate is global within that
cap: a polynomial of smaller norm must lie in the exhausted ball. This gives
a rigorous reason to nominate the formulas. It does not prove that arithmetic
chooses the smallest-coefficient representative.

Monomial support is a different complexity measure, and the replay audits it
separately:

| channel | minimum support | all minimum-support coefficient vectors | is nominee support-minimal? |
|---|---:|---|---|
| `chi_(0,3)` | 3 | nominee and `(1574,-962,154,0,0)` | yes, but not uniquely |
| `chi_(2,2)` | 3 | `(208,-144,29,0)` | **no**; nominee has support 4 |
| `chi_(0,4)` | 2 | nominee only | yes, uniquely |

Thus `chi_(2,2)` is a particularly useful guardrail: the proposed cubic is
coefficient-small, not support-sparse. The protocol never conflates the two.

This distinction is the central output of the packet:

```text
finite values + exact complexity certificate = disciplined conjecture
finite values + no all-q trace argument       != theorem
```

## 3. Exact detector decomposition

The source fixture supplies invariant polynomials in

\[
 t=\operatorname{Tr}(U),\qquad e=e_2(U),\qquad U\in USp(4).
\]

The new replay independently expands those polynomials as two-variable
Laurent polynomials and performs virtual highest-weight subtraction using the
bounded Kostant `C2` engine. It recovers

\[
 \chi_{0,3}=V_{(3,3)},\qquad
 \chi_{2,2}=V_{(4,2)},\qquad
 \chi_{0,4}=V_{(4,4)}
\]

with multiplicity one and zero residual. Here the pairs are highest weights in
the `e` basis. Their representation/local-system weights are respectively
`6,6,8`.

Conditionally, if the monic-quintic quotient is first identified with the
intended smooth marked stack and the corresponding local system is pure of
weight `w`, the replay records only the conservative Deligne upper bounds

\[
 \operatorname{wt} H_c^i\le w+i,\qquad 0\le i\le6.
\]

It does not infer which degrees occur, whether a term is Tate, Eisenstein,
endoscopic, or cuspidal, or the multiplicity of any such term. The stack
adapter is presently absent, so even these bounds are explicitly conditional
metadata rather than a result about the monic-quintic family.

## 4. Genus-one positive control

For elliptic curves, the exact `SU(2)` decomposition is

\[
 a^{10}=
 42q^5P_0+90q^4P_2+75q^3P_4+35q^2P_6+9qP_8+P_{10},
\]

where `P_m=Tr(Sym^m H^1)`. The exact stack trace identity gives

\[
 \sum_{[E]/\mathbb F_q}{P_{10}(a_E,q)\over|Aut_q(E)|}
 =-1-\Theta_{12}(q).
\]

Using the source-locked tenth stack moments and the four lower boundary
channels, the protocol isolates:

| `q` | locked tenth stack moment | isolated `P10` sum | boundary-removed `Theta12(q)` |
|---:|---:|---:|---:|
| 3 | 20,708 | -253 | 252 |
| 5 | 584,874 | -4,831 | 4,830 |
| 7 | 4,714,408 | 16,743 | -16,744 |

The label `Ramanujan Delta` is accepted for structural reasons:

* the detector character has been isolated exactly;
* the elliptic-stack trace formula is an imported exact theorem;
* the local-system/modular-weight map gives weight `10+2=12`;
* `dim S_12(SL(2,Z))=1`; and
* its normalized generator is unique.

The three displayed numbers are not what licenses the name. Without the last
four facts, the same protocol would refuse it.

As a symbolic control, the known rank-two packet has Frobenius weight 11 and

\[
 s_r=\tau(p)s_{r-1}-p^{11}s_{r-2},\qquad s_0=2.
\]

The replay verifies this at extension degrees `1,2,3` for `p=3` using the
already implemented theorem-supplied recurrence. This is not presented as new
finite-field evidence.

## 5. Genus-two refusal and recurrence no-go

For each genus-two channel, the tool has only one value at each of three
different characteristics. A proposed pure rank-two packet would have a
recurrence of the schematic form

\[
 s_r=A_p s_{r-1}-\delta_p s_{r-2}.
\]

Neither rank two, the purity weight, the determinant exponent, nor its phase
is inferred from the `C2` character identity. The replay therefore records
this only as a formal schema with an undetermined determinant.

Testing it requires repeated extensions of the *same* `p`. Cross-prime values
at `3,5,7` provide three unrelated `A_p` values and do not test this recurrence
at all. Every genus-two recurrence audit therefore returns

```text
INSUFFICIENT_SAME_CHARACTERISTIC_EXTENSION_DATA
available extension degrees: [1]
missing extension degrees: [2,3]
```

Likewise, all three proposed genus-two names are refused because the packet
lacks:

* an exact identification of the monic odd-quintic measure with the intended
  marked stack/local system;
* an exact family trace formula in that normalization;
* a proved one-dimensional target channel; and
* a uniquely normalized generator.

The exact `C2` character identity satisfies only the first, representation-
algebra stage of the protocol.

## 6. What evidence would change the verdict?

The next useful inputs are sharply defined.

1. **Geometric adapter.** Prove the measure comparison, including the marked
   Weierstrass point, hyperelliptic involution, affine quotient, and stack
   weights.
2. **One same-characteristic tower.** Obtain exact values at `p,p^2,p^3` for
   a channel. Values at `p,p^2` test the determinant predicted by a weight;
   the third value tests the resulting order-two recurrence.
3. **Cohomology multiplicities.** Supply a theorem-backed list of the possible
   Tate, elliptic, endoscopic, and Siegel pieces for the exact local system.
   Only then can subtraction be structural rather than fitted.
4. **An additional independent field.** A fourth `q` kills the cubic
   vanishing direction but still does not identify a modular form or test a
   Frobenius-power recurrence.

The recommended first proof target remains the primitive trace-average lemma
behind `chi_(0,3)`. If it yields `q^4-2q-1`, the formula becomes an all-field
theorem through arithmetic, not an inference-engine promotion.

Each channel also exports a machine-readable candidate record. Its allowed
claim is exactly “unique minimum-`L1` integral continuation in the declared
degree cap, matching `q=3,5,7`.” It explicitly forbids promotion to an all-`q`
theorem, Tate-only decomposition, named eigenpacket, or Frobenius recurrence,
and lists the evidence needed to unlock each promotion. This is intended as a
safe input contract for later automated conjecture-generation agents.

## 7. Resource and claim firewalls

* Finite fields enumerated: none.
* Frozen observations consumed: exactly `q=3,5,7`.
* Database queries: none.
* Largest exact coefficient lattice ball: 2,241 vectors.
* Exact character engine: operation-capped; three channels only.
* Wall-clock guard: 3 seconds.
* Optimized mode is tested separately so correctness does not depend on
  Python `assert` statements.
* No claimed Siegel/elliptic eigenform, motive, global Euler product,
  number-field transfer, RH, or GRH consequence.
