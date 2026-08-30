# Independent audit: finite-height cofinal Hardy source capture

Status: PASS WITH PURE-DENOMINATOR, FIXED-CONFIGURATION AND LOW-PASS BOUNDARIES.
Review date: 2026-08-31.
Programme: #763; continuation of the earlier actual-Xi metric work.

## Exact scientific state

Reviewed source: 90e8dff3d184cbfe59974969ca89615856c33c51.
Authoring base: 5852e785a24a2d30a8ba6c742e3650a7f6438567.
Unchanged programme import: 2ead930226e8d45e9a9f49efdfb5fa5c8a91cb26.
This audit does not change any of the five scientific files.

| Artifact | Frozen Git blob |
|---|---|
| HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md | 72ac1f93b6fb0a74200ed2cc7e8399a4a10064c2 |
| hardy_cofinal_finite_height_source_capture.py | 3392d7ba4e166038e33bc39cdbb99b739576ee5d |
| hardy_cofinal_finite_height_source_capture.json | 48e74bbf5d6f641348a71a4e899d89838294ef99 |
| hardy_cofinal_finite_height_source_capture.sources.json | 3e37d97dd584617b8805bdc3d4c342cc8d4bb40c |
| tests/test_hardy_cofinal_finite_height_source_capture.py | d6e4536a72a46ff246bf43a12a6f94c23e28113f |

The first four artifacts are in research/exploratory/.
Fixture LF-normalized SHA-256:
8e12fc7143d24e5bf8464818c5f0ca82929d2c23eea118498303eded2409f0cc.
Canonical payload seal:
d24be1ae5ffcfe27d8e1cd76565b712cc5c5b94287439ae4e68d14ae636278ed.

Nine frozen note/review bindings are checked by original commit, raw Git
blob identity and LF SHA-256. They retain the original translation and
all-inner sources, the actual-Xi count source and its reviews, and the
historical height, native-partition and total-charge context. The latter
three are not promoted to a proved native global-height theorem.

## Accepted theorem and its proof

The [source note](HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md) fixes
the unitary Fourier convention with inverse kernel exp(ixt)/sqrt(2pi).
Let B be a pure finite or infinite Blaschke product, with multiplicities
included and finite S=sum Im(b). No denominator singular factor is allowed.
The numerator U can be any inner function. Write M=K_B and
P_U=M_U M_U* for projection onto U H2.

For measurable I contained in [0,L], the literal operators are

    T_I = ||Pi_I M_U P_M||_HS^2,
    C_I = ||Pi_I P_U P_M||_HS^2.

They are different. The result is

    0 <= C_I <= T_I <= 2 L S.

For U=1 the sharper 2 |I| S bound holds. No such general-U width bound
is asserted. The theorem costs the upper frequency endpoint L, not the
width of a distant shrinking band.

For finite denominators, integration of the exponential/confluent basis
gives A*G+GA=-c*c. Consequently its evaluation-kernel diagonal is decreasing,
with k_M(0)=2S and derivative a negative square. This proves the low-pass
bound. Hardy multiplication is causal:

    Pi_[0,L] M_U = Pi_[0,L] M_U Pi_[0,L].

It is not a commutation statement for a sharp band, and is not an identity
for the projection P_U. Summing the causal contraction over a denominator
orthonormal basis proves T_I<=2LS.

Multiplier-adjoint coinvariance gives M_U* K_B contained in K_B.
Thus A_U=M_U*|K_B is a contraction and
Pi_I P_U|K_B=(Pi_I M_U|K_B) A_U. The Hilbert--Schmidt ideal inequality
proves C_I<=T_I without a numerator-rank restriction.

For nested finite divisors B_m exhausting the entire pure Blaschke divisor,
the union of K_(B_m) is dense in K_B. Compatible orthonormal bases and
nonnegative series therefore give

    C_I(B_m,U) increases to C_I(B,U),
    T_I(B_m,U) increases to T_I(B,U),

and Hilbert--Schmidt convergence after insertion of the input projections.
No unbounded inverse Gram is assigned a trace. B, U and I are fixed.
Geographic disk exhaustion is covered only when each closed disk contains
finitely many zeros; a general Blaschke sequence can accumulate on the
real boundary inside a bounded disk.

The finite literal-source interface is preserved. In column-kernel
coordinates, A=J_U*, C=J_O*, R_c=CA=AC and G_O=C*GC. Therefore

    tr(G_O^-1 R_c* H_I R_c)
      = tr(G^-1 A* H_I A)
      = ||Pi_I P_U E G^-1/2||_HS^2.

The outer metric is retained before congruence. There is no global
bounded inverse outer-operator assumption. Confluent HT4 coordinates
retain their i^r phase conjugation.

## The exact unpaid tail and a quantitative countercontrol

The classical orthogonal splitting
K_B=K_(B_m) direct-sum B_m K_(B/B_m) gives exactly

    C_I(B,U)-C_I(B_m,U)
      = ||Pi_I P_U M_(B_m) P_(K_(B/B_m))||_HS^2.

This tends to zero for the fixed finite-height configuration. The bare
inner-multiplied tail has the quantitative bound 2L S_tail by causality.
The same bound for the physical source projection is false.

The packet uses the compatible source O=1, N=U, D=B, R=U-B, with

    V(z)=(z-i)/(z+i),
    b=2+i/4,
    U(z)=(z-i/2)/(z+i/2),  B=V b_b.

Radius 3/2 retains i and omits b. Projecting the normalized omitted
vector V k_b onto U H2 gives, after dividing by sqrt(2 Im b),

    (24+64i)/73 exp(-t)
    + (4/73-32i/219) exp(-t/2)
    + (49-64i)/73 exp(-(1/4+2i)t).

The origin squared modulus is 745/657>1. The exact derivative majorant
4195/876 gives real amplitude at least 75/73 throughout
0<=t<=24/4195. Hence for every 0<L<=24/4195,

    C_[0,L](B,U)-C_[0,L](V,U)
       >= 2L Im(b) (75/73)^2 > 2L Im(b).

Both reviewers reconstructed this by subtracting the rank-one projection
onto K_U, independently of the producer's division/residue algorithm.
The omitted input has total norm squared one, and the projected total
norm squared is 649/657. Thus the local amplitude increase is fully
consistent with the global projection contraction.

This refutes the stated constant-one tail-height replacement, not every
possible source-tail inequality and not a claim about actual Xi zeros.

## Infinite countercontrols and native boundary

A denominator exp(i tau z) has zero zero-height sum but model space
L2(0,tau). Any positive-length subinterval has infinite projection trace.
This proves why a singular denominator cannot be hidden in S.

The pure Blaschke example b_j=16*2^j+i has O(log R) zero count and
genus-zero numerator/denominator growth O(log^2 R), but infinite trace on
every positive-width bounded band when U=1. Its normalized kernels have
Gram operator at most 5/4, so projection onto any finite span dominates
4/5 times their rank-one sum. Removing a finite geographic part leaves
infinite omitted-source trace. Upper bounds on count and growth alone
therefore do not pay this tail.

Conversely b_j=2^j+i*2^(-j) has S=1 and infinite rank. Its bounded-band
trace is finite by the theorem, while its U=1 total charge is infinite.
None of these controls reproduces the actual Xi theta kernel.

The accepted actual-Xi packet supplies small normalized traces for
finite geographic windows, with a band endpoint of order log T and
width of order 1/(T log T). The present low-pass theorem is not a
replacement for that shrinking-width estimate. Actual global finite
height, a pure native denominator, compatible cofinal numerators and
outer-normalized jets, quantitative approximation/boundary/source-tail
control and the required order of limits remain separate obligations.

## Independent replay and primary-source check

The root read the complete note, producer, manifest and tests, authenticated
the fixture and all primitive/current identities, and ran 30 tests normally
and under Python -O: 1.163s and 1.140s, both PASS. Both producer checks,
Ruff lint/format and the full authoring-base-to-source whitespace check pass.

A separate root implementation reconstructed seven complex/confluent Grams,
all published principal minors, the Lyapunov and origin-height identities,
the full rank-one leakage projection and its norms, three finite outer/source
trace congruences, and 24 indicator/height/lacunary controls. The same
independent reconstruction passed -O.

The independent peer read all five source files and nine dependencies.
Its 30 tests in each mode and both producers passed. Additional checks
covered seven Grams with 71 principal minors, three literal source cases
including confluence, six actual smoothly weighted frequency congruences,
lacunary rows through rank 64, 36 dyadic growth bounds and 54 adversarial
controls in each mode. No author coordination or scientific edits occurred.

Strict canonical JSON, duplicate/nonfinite/type rejection, source Git
identity, current-artifact hashes and the payload seal govern acceptance.
The controls retain degree 4, panel 8, 16-bit input, 1024-bit internal
rational and 524288-byte bounds. Finite replay is not an analytic proof
of the infinite limits.

The root visually checked the complete relevant printed pages 8, 11 and 12
of [Fricain--Hartmann--Ross](https://arxiv.org/pdf/1605.07418v2).
Equation (2.12) states the decomposition; equations (2.30)--(2.36) retain
the half-plane Hardy model and disk/half-plane unitary correspondence.
Their Fourier variable uses a different 2pi convention, so the packet's
constants are justified by its own fixed-convention integral identities,
not copied across conventions. The PDF workflow was read-only.

Reproduction:

~~~text
python -B tests/test_hardy_cofinal_finite_height_source_capture.py
python -B -O tests/test_hardy_cofinal_finite_height_source_capture.py
python -B research/exploratory/hardy_cofinal_finite_height_source_capture.py --check
python -B -O research/exploratory/hardy_cofinal_finite_height_source_capture.py --check
~~~

No native Xi cofinal-capture theorem, total-charge or free-energy estimate,
critical-line percentage, reverse-Rolle descent, RH/GRH result or external
novelty claim is accepted.
