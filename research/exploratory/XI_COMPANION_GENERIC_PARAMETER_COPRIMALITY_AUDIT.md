# Independent review: generic native Xi companion coprimality

Verdict: PASS for corrected scientific release
d76a1a8eb8ec40b19a351af95439b9a6514bee87.
This accepts the written analytic argument after review, not a
machine-certified theorem or a numerical assertion about Xi zeros.

Review date: 2026-08-31.
Original scientific commit: 1baecc1e463677fc175f3ff35a1576a942b39869.
Original authoring base: cce5552c9de8a6ec0206977fdd7119a7fab3d874.
Resident scientific import: 02717f763bf4dceb930724ce4c32262308095bc4.
Resident correction import: c895b61434f0c142a07c1c5239da8fd6d90a2c95.

Root contributed the proposed Wronskian strategy and one polynomial control.
Root's post-freeze verification is therefore additional checking, not the
sole independence claim. A separate non-author reviewer read the complete
source, found the prose defect below, and independently accepted the exact
corrected identity. The five scientific files retain their frozen contents;
this separate audit supplies acceptance without rewriting their proposed
status or changing their seals.

## 1. Exact accepted theorem

For the actual unrescaled f=Xi, g=f^(5), and one fixed positive constant
lambda, retain the reduced meromorphic companions

    Theta_h=(h-i lambda h')/(h+i lambda h'),  h=f,g.

Define W=f g'-f'g and the set

    Z={b in C+: W(b)=0, f'(b)g'(b)!=0,
                    f(b)/(i f'(b)) is positive real},
    E={f(b)/(i f'(b)): b in Z}.

There is a genuine common upper-half-plane zero exactly when lambda is in
E; pointwise, the common zero is precisely a witness b in Z with that
parameter. E is at most countable, and its image restricted to any fixed
closed b-disc is finite. These statements are unconditional.

Neither E's emptiness nor a member is established. Discrete W zeros do not
make their parameter image discrete, locally finite, or avoid a prescribed
countable sequence. The complement has full Lebesgue measure and is dense,
but no explicit good rational or physical lambda_j is selected.

Under the ADDITIONAL two-component inner premise, and lambda outside E,
the maximal common inner divisor is constant. The reduced numerator and
denominator are pure Blaschke products with infinite total zero height.
For every fixed L>0, each bare zero-start low-pass trace is infinite.
These conditional conclusions do not hold merely because a parameter
avoids E; innerness remains an independent hypothesis. RH is sufficient
for that premise, not proved here.

## 2. Load-bearing proof checks

1. At every complex zero of h of multiplicity r, both raw companions have
   exactly order r-1. Their nonzero leading coefficients have ratio -1.
   Internal cancellation cannot create a companion zero, including at
   multiple off-real zeros. A stationary point with nonzero h gives +1.

2. A genuine companion zero has h=i lambda h' with h' nonzero and
   denominator 2i lambda h' nonzero. Applying this to f and g gives the
   necessity of every condition defining Z. Conversely, W=0 and the
   stated derivative and parameter conditions give both genuine zeros.
   Neither raw numerator vanishing nor W=0 alone is sufficient.

3. The actual positive even superexponentially decreasing kernel supplies
   f^(j)(0)=i^j mu_j and strictly positive mu_0,mu_6. Consequently

       W(0)=-mu_0 mu_6<0.

   Thus W is nonzero entire. Isolated-zero compactness gives finitely many
   zeros, with finite multiplicities, in each closed disc. Their countable
   union and parameter images prove the cardinality assertions without RH
   or an optional growth bound.

4. W=R_f g'-f'R_g. At a genuine common zero this bounds the minimum of the
   two companion zero orders by ord(W). Unequal orders give equality;
   equal orders can cancel to larger W order. The exact excess-order
   control verifies why unconditional equality or simplicity is false.

5. At b=iy, the literal derivative phases give
   W(iy)=-[h h^(6)-h' h^(5)]<=-mu_0 mu_6<0, by NA's positive-kernel
   covariance identity. The exceptional points cannot lie on that axis.
   Even real-entire symmetry sends b to -conjugate(b), with the SAME
   positive lambda and nonzero derivatives. The points are distinct.

6. Under innerness, GH's actual continuation and axis limits exclude the
   singular factors and prove infinite height for both unreduced products.
   An inner divisor of a pure Blaschke product is pure. Outside E it has
   no zeros and is therefore a unimodular constant. No unproved height
   subtraction or product approximation is needed.

7. LP then applies to each reduced product with its literal boundary dx
   and unitary Fourier conventions. Its conclusion is for bare [0,L]
   traces. Arbitrary shifted or shrinking bands are not included.

8. CP's pure, coprime, infinite-height example with global corrected
   capture below 1/9 remains a valid obstruction. Neither coprimality nor
   infinite bare trace gives corrected physical capture divergence.
   The actual outer metric and adjoint value jets have not disappeared.

The main gate remaining for the physical source is not this generic
classification. It is a statement about the prescribed lambda_j, actual
off-axis reduced numerator values/jets, and the corrected physical operator
with its retained high-T geography and omitted directions.

## 3. Correction and frozen-source provenance

The original finite-control table was correct, but two following ordinal
references described different rows after insertion of the real-rooted
control. The non-author reviewer flagged both contradictions. The new
release replaces ordinals with explicit polynomial names.

The correction changes exactly the proof and fixture: seven added and
five removed lines. Only the proof artifact hash and payload seal change
in the fixture. After removing those seals, the scientific JSON is exactly
unchanged. Producer, manifest and tests have identical LF bytes.
The original identity remains in history; acceptance is for d76a1a8e,
not for the original contradictory prose. No amendment or parent rewrite
was used.

All six primitive proof notes are pinned by full commit, path, Git blob
and LF SHA-256: NA, GH, XL, LP, CP, and L-106620. Their imports were read
and authenticated. No ancestor code or actual Xi numeric values are
executed by this producer.

## 4. Finite verification, subordinate to the analytic proof

Root read all five files and the exact correction delta. On the corrected
source, 32 tests passed normally (6.167 seconds) and under -O
(6.143 seconds), along with both producer checks, Ruff check/format,
control-character checks and the full authoring-base whitespace check.

A separate transient exact symbolic reconstruction passed in BOTH modes:

- All eight reported derivative-linked rows plus 60 held-out point/parameter
  rows: 68 rows and 340 raw-companion/W order checks. Symbolic polynomial
  cancellation independently checked the reduced orders and values.
- Forty-eight additional complex internal-cancellation rows at two
  nonnative Gaussian-rational points, all multiplicities one through eight
  and three different positive parameters.
- Six nonnative positive even atomic moment models checked the phase
  nonvanishing identity; these are not actual Xi moment evaluations.
- Twenty-nine independently resealed hostile reports were rejected by
  ACTUAL fresh complete reconstruction in each mode, without mocking or
  caching build_report.
- Six literal source bindings, four artifact seals, all five frozen files,
  the unchanged scientific correction payload, and four exact LF
  report/manifest emissions per replay passed.

The non-author reviewer separately passed the 32 tests in both modes,
both checks and four LF emissions. It reconstructed all eight complete
linked records, 24 cancellation records and three moment records using
symbolic algebra and repeated division by z-b. Its additional controls
included 16 linked held-outs, eight cancellation held-outs, and stationary
nonzero, genuine pole and unequal-common-order cases. It rejected 134
hostile checks per mode, including 48 resealed reports: seven through
actual fresh reconstruction and 41 against cached complete reconstruction.
Those categories are explicitly distinct.

Finite controls, source hashes and test counts do not machine-prove
entireness, countability, inner-factor purity or infinite trace.

## 5. Exact release identities

Frozen Git blobs:

- Proof: 797f7b581580ad5a441c7702015c64a53eca6f4d.
- Producer: 221de506538d0f9e37d31b126c334f90335086f8.
- Fixture: cd7a0ec0544261f4543b5df566e205cbe9d05b61.
- Sources: 0114f1f3fa62b3d242e399085993eecb5f4439e5.
- Tests: d4505e82125a86561b4d72105a6ed8a8b262fa13.

Fixture LF SHA-256:
2977ce0527f5b1df4bef8070e7b9f461981f6fe97188a9b3dcd5cfbbe2a42e94

Payload SHA-256:
6ab64cba1e802008bdb51fb4d5e9a595877153ed696b6bd3bfc301d6f9efaae2

The independent frozen-release obligation is satisfied. RH, native
high-T capture, prescribed parameter avoidance, open parameter stability
and external publication priority remain unproved.
