# Beta band-pass and curve-wavelet successor: release audit

Status: **audited release-sized exploratory atlas; exact identities,
conditional implications, method boundaries, and open RH-strength
estimates are separated explicitly**

Frozen parent:

- draft PR #757;
- commit \(b870366141fe8d5f43d5b81f6e50a67d2a888070\);
- title: “Explore beta RH gates, generalized rho panels, and Adams masks”.

Single entry point:
[BETA_BANDPASS_WAVELET_FIVE_MINUTE_HANDOFF.md](BETA_BANDPASS_WAVELET_FIVE_MINUTE_HANDOFF.md).

Programme scope:
[Programme I #736](https://github.com/gfreund123/riemann/issues/736),
[Programme II #737](https://github.com/gfreund123/riemann/issues/737), and
[Programme VI #741](https://github.com/gfreund123/riemann/issues/741).

## 0. Current-head synthesis

The original audit below remains provenance for the first release
slice. The branch subsequently grew into four review lanes. The current
front door is
[FFPS_MOVING_SUPPORT_CARRIER_PHASE_DIAGRAM.md](function_field/FFPS_MOVING_SUPPORT_CARRIER_PHASE_DIAGRAM.md).

The strongest exact continuation results are:

1. **Sharp centered carrier duality.** For every compact normalized
   carrier derivative,

   \[
    (\log X+S_X)^3\mathcal E_Q(X)
    \ge12\left|\sum_{n\le X}{\beta(n)\over\sqrt n}\right|^2.
   \]

   The constant is optimal, with an exact Pythagorean
   Mertens-plus-shape decomposition and signed-autocorrelation second
   moment.

2. **All-support parabolic criterion.** For every arbitrary prescribed
   schedule \(1\le S_X<\infty\),

   \[
    \mathrm{RH}
    \Longleftrightarrow
    (\log X+S_X)^3\mathcal E_{S_X}(X)=X^{o(1)}.
   \]

   This is an RH equivalence, not a proof of its arithmetic estimate.
   The width power \(3\) is the unique scale-balanced exponent for the
   two proved mechanisms.

3. **Exact curve-zeta calibration.** The same carrier construction on
   \(1/Z_C(u)\) gives an exact coefficient-square energy and is
   equivalent to the reciprocal roots lying on the Weil circle. Weil
   RH is imported, not reproved.

4. **Function-field channel exposure.** The divisor-wavelet pilot
   isolates a genuine twisted \(L\)-channel; the marked-place packets
   identify two-place recurrences, an elliptic three-place channel,
   higher Tate notches, and all-mark exterior-character structure.

5. **Corrected Adams obstruction.** The native gluing problem is the
   crossed marked-place source graph under partial Frobenius. Local
   Artin--Schreier/incidence blocks remain valid inside fixed marked
   blocks. A signed pushforward or correspondence-level construction
   remains open.

6. **Spectral firewalls.** Chirality, compact carrier zeros, and finite
   spectral-factor surgery are not determined by the positive energy.
   Positivity, diagonal interpolation, or a pretty compact zero set
   cannot close the beta problem without new source arithmetic.

Three independent agents rederived the centered-moment theorem,
all-support renormalization, projected finite-abscissa bound, and
critical exponent trichotomy. The final packet passes normal and
optimized replay, 16 focused tests in both modes, Ruff, source-blob
provenance, delimiter/control-byte checks, and Git whitespace checks.

## 1. Commit ledger

### Original release slice

| commit | packet |
|---|---|
| \(cd272c4ea\) | correct the BASEWAVE/PRIMCAR hierarchy |
| \(05aaabe69\) | fixed band-pass beta energy ladder |
| \(afd49590f\) | assembled one-variable wavelet and Perron bridge |
| \(e87f2392f\) | complete genus-zero function-field shadow |
| \(e39031369\) | native partial-Frobenius/rank verdict |
| \(9465ba540\) | formatting-only replay normalization |
| \(3dbf13f6d\) | bilateral Perron and forced cusp-leakage theorem |
| \(8ab56eff1\) | infinite dyadic smoother and subpower spectral localization |
| \(18056756f\) | all-curve Frobenius-residue extension |
| \(b631040b7\) | critical-scale beta localization theorem |

### Aggressive continuation

| commit | packet |
|---|---|
| \(009672434\) | Frobenius channel filter calculus |
| \(7904141d6\) | critical beta Fourier-lattice compression |
| \(d478172e1\) | duplicate-67 scale-filter firewall |
| \(82ff58f07\) | ternary relative native rank |
| \(7a54822cb\) | Boolean evaluation Frobenius residues |
| \(8192514ed\) | audited theorem-boundary tightening |
| \(3778eb0f5\) | critical beta spectral-witness principle |
| \(ece0694b2\) | coherent first-lattice-harmonic firewall |
| \(1e0c42aaf\) | small-prime rough critical preconditioner |
| \(9c95eb368\) | Frobenius extension-tower aliasing |
| \(63b279e4b\) | Boolean Frobenius tomography trilemma |
| \(d1af01313\) | sharp truncated rough-conditioning frontier |
| \(31c0e730f\) | single-harmonic maximal phase transport |
| \(67c8981c9\) | sharp rough one-harmonic normal form |
| \(1e1b274ec\) | two-place extension recurrence spectroscopy |
| \(6e57525d6\) | elliptic three-place channel |
| \(fad8ce2c4\) | endpoint sampling square-root frontier |
| \(8dd144c69\) | four-place universal Tate notch |
| \(02555b216\) | function-field divisor-wavelet factorization |
| \(d95a52129\) | dyadic beta-bridge renormalization |
| \(11552aea8\) | rough Witt-conditioning frontier |
| \(3a1d92b57\) | truncated beta zero-tube residue law |
| \(be6e62c63\) | six-place Tate-notch stratification |
| \(2d4e06ccc\) | coherent-color Witt wavelet |
| \(121b7f205\) | all-mark exterior tower |
| \(3bae32791\) | multicolor rough-Witt phase surface |
| \(02c2b7237\) | cyclic-phase coherent-color collapse |
| \(fc7ee1304\) | beta-kernel spectral nonalignment |
| \(3658d4c31\) | zero-free beta-energy ladder compression |
| \(b0892f2ac\) | carrier chirality separation |
| \(46536ba7e\) | compact carrier zero flip |
| \(011ad6d3f\) | zero-surgery invariant correction |
| \(731398930\) | signed beta Gram geometry |
| \(4fd2b0cd5\) | marked-place bifrobenius gluing correction |
| \(46ea68808\) | tilted-tent renormalization flow |
| \(85f4c3823\) | fixed-support beta microscope |
| \(d30994d59\) | critical moving-order beta criterion |
| \(b5db69dff\) | twisted function-field wavelet channel |
| \(9c6dea170\) | annular primitive beta normal form |
| \(e66721ab7\) | finite compact spectral-factor surgery |
| \(db37529e4\) | moving-order phase boundary |
| \(52577ce7f\) | uniform moving-carrier beta criterion |
| \(19f274c93\) | variational probability-carrier optimum |
| \(3667da851\) | curve-zeta probability-carrier calibration |
| \(69a1ead02\) | moving-support beta-energy phase diagram |

## 2. Claim ledger

| claim | grade |
|---|---|
| \(u=1\) BASEWAVE is predicatewise PRIMCAR | **PROVED EXACT** |
| corrected AUXCOLOR/WAVE conditional implications | **PROVED AS LOGICAL IMPLICATIONS; PREMISES OPEN** |
| every fixed finite band-pass rung is RH-equivalent | **PROVED FROM PINNED BV/MELLIN--LANDAU INPUTS** |
| complete beta energy equals one assembled \(N\)-wavelet | **PROVED EXACT** |
| \(N=1\) is the complete diagonal | **PROVED EXACT FROM RATIO SUPPORT \(16<67\)** |
| complete local correction Euler product is one | **PROVED EXACT** |
| safe-line Perron--Fourier identity | **PROVED BY ABSOLUTE DIRICHLET CONVERGENCE AND BV FOURIER DECAY** |
| bilateral double-Perron identity retains the notch | **PROVED AS ITERATED TRUNCATED PERRON INVERSION** |
| Barnes collapse creates the max cusp | **PROVED EXACT BY RESIDUES** |
| max cusp refills every nonzero notch linearly | **PROVED EXACT FROM THE ABSOLUTE-LAG IDENTITY** |
| compact infinite dyadic smoother is \(C^\infty\) and right-half-plane zero-free | **PROVED** |
| tail beyond \(e^{\kappa\sqrt{\log X}}\) is at most \(X^{1-\kappa^2/\log2+o(1)}\) | **PROVED FROM THE EXACT STAIR ENVELOPE AND TRIVIAL BETA BOUND** |
| energy inside \(e^{\sqrt{(\log2)(\log X)}}\) is RH-equivalent | **PROVED FROM THE FIXED-KERNEL CRITERION** |
| tail beyond \(T_\theta(X)=e^{(\log X)^{1/2+\theta}}\), fixed \(0<\theta<1/2\), is superpower small | **PROVED UNCONDITIONALLY FROM THE TRIVIAL BETA BOUND** |
| complete affine function-field shadow has cubic Euler notch | **PROVED EXACT** |
| affine complete shells decay exponentially | **PROVED BY CAUCHY** |
| all-curve zeta factorization with finite deletions | **PROVED EXACT** |
| fixed joint-offset coefficient sequences, hence fixed-ratio shells, have Frobenius exponential-polynomial form | **PROVED BY PARTIAL FRACTIONS AND CAUCHY** |
| universal native phase/incidence rank is \(m\) or \(Q-1\) | **PROVED EXACT** |
| natural phase and diagonal fail independent partial Frobenius | **PROVED BY COBBOUNDARY DEGREE AND SUPPORT** |
| low-frequency beta estimate, contour shift, or RH | **NOT PROVED** |
| incomplete function-field theorem or full relative sheaf complex | **NOT PROVED** |

### Continuation claims

| claim | grade |
|---|---|
| carrier total and first moments recover the complete beta prefix | **PROVED EXACT** |
| centered support-energy constant \(12\) and parabolic extremizer | **PROVED EXACT** |
| Pythagorean Mertens-plus-shape decomposition | **PROVED EXACT** |
| signed autocorrelation second moment \(-2B(X)^2\) | **PROVED EXACT** |
| projected finite-abscissa Laplace carrier inequality | **PROVED EXACT** |
| comparable weights and multiscale probes cannot beat \(L^{3/2}\) from the same abstract data | **PROVED IN THE ABSTRACT INFORMATION CLASS** |
| raw energy at support \(X^{\gamma+o(1)}\) excludes zeros beyond \(1/2+3\gamma/2\) | **PROVED FOR FIXED \(\gamma\ge0\)** |
| width-renormalized energy implies RH for arbitrary finite support | **PROVED** |
| width-renormalized parabolic energy is RH-equivalent for every schedule \(S_X\ge1\) | **PROVED** |
| width exponent \(p<3\) admits unconditional dilution schedules | **PROVED** |
| all-support RH forward theorem at \(p>3\) | **NOT PROVED** |
| variational parabolic density uniquely minimizes derivative energy | **PROVED EXACT** |
| carrier chirality or compact zero set follows from energy | **REFUTED** |
| finite compact spectral-factor surgery classification | **PROVED EXACT IN THE STATED CLASS** |
| curve-zeta parabolic energy criterion | **PROVED EXACT; WEIL RH IMPORTED** |
| divisor-wavelet function-field pilot exposes a twisted \(L\)-channel | **PROVED IN THE COMPLETE PILOT** |
| crossed marked-place graph obstructs the naive partial-Frobenius split | **PROVED** |
| signed pushforward/correspondence repair of the native gluing | **OPEN** |
| beta-energy estimate in an RH-bearing region or RH | **NOT PROVED** |

## 3. Exact replay commands

Run each command normally and with optimized Python:

~~~text
python -B research/l-families/atlas/function_field/ffps_primitive_rho_tilt_convolution_isomorphism.py --check
python -B research/l-families/atlas/function_field/ffps_basewave_primcar_identity.py --check
python -B research/l-families/atlas/function_field/ffps_bandpass_beta_energy_ladder.py --check
python -B research/l-families/atlas/function_field/ffps_assembled_beta_perron_fourier_bridge.py --check
python -B research/l-families/atlas/function_field/function_field_basewave_shadow.py --check
python -B research/l-families/atlas/function_field/ffps_native_partial_frobenius_verdict.py --check
python -B research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py --check
python -B research/l-families/atlas/function_field/ffps_infinite_dyadic_box_bandpass_smoother.py --check
python -B research/l-families/atlas/function_field/function_field_basewave_curve_extension.py --check
~~~

Continuation front-door replays:

~~~text
python -B research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py --check
python -B research/l-families/atlas/function_field/ffps_uniform_moving_carrier_beta_criterion.py --check
python -B research/l-families/atlas/function_field/ffps_variational_probability_carrier_optimum.py --check
python -B research/l-families/atlas/function_field/function_field_mobius_carrier_calibration.py --check
python -B research/l-families/atlas/function_field/ffps_function_field_beta_divisor_wavelet_pilot.py --check
python -B research/l-families/atlas/function_field/ffps_marked_place_bifrobenius_gluing_gate.py --check
python -B research/l-families/atlas/function_field/ffps_beta_gram_sign_geometry.py --check
python -B research/l-families/atlas/function_field/ffps_compact_kernel_finite_spectral_factor_surgery.py --check
~~~

Focused test modules:

~~~text
tests.test_ffps_primitive_rho_tilt_convolution_isomorphism
tests.test_ffps_basewave_primcar_identity
tests.test_ffps_bandpass_beta_energy_ladder
tests.test_ffps_assembled_beta_perron_fourier_bridge
tests.test_function_field_basewave_shadow
tests.test_ffps_native_partial_frobenius_verdict
tests.test_ffps_bandpass_assembled_perron_leakage
tests.test_ffps_infinite_dyadic_box_bandpass_smoother
tests.test_function_field_basewave_curve_extension
~~~

Continuation front-door test modules:

~~~text
tests.test_ffps_moving_support_carrier_phase_diagram
tests.test_ffps_uniform_moving_carrier_beta_criterion
tests.test_ffps_variational_probability_carrier_optimum
tests.test_function_field_mobius_carrier_calibration
tests.test_ffps_function_field_beta_divisor_wavelet_pilot
tests.test_ffps_marked_place_bifrobenius_gluing_gate
tests.test_ffps_beta_gram_sign_geometry
tests.test_ffps_compact_kernel_finite_spectral_factor_surgery
~~~

At the full continuation head:

- all 51 changed bounded producers passed normally and under optimized
  Python;
- all 447 tests in the 50 changed focused modules passed in both modes;
- Ruff lint and format passed on all 101 changed Python files;
- all 56 changed Markdown packets contain no forbidden control bytes;
- local links from the two successor front doors resolve;
- the moving-support packet has balanced inline/display math
  delimiters and independently rederived constants;
- the working diff passes the Git whitespace check.

## 4. Independent checks performed

The assembled beta packet was independently rederived in two coordinates:

1. direct ordered beta pairs versus unique
   \((i,j,g,a,b)\) coordinates;
2. the displayed collapsed \(N\)-divisor-\(H_N\) wavelet.

At toy exceptional prime \(5\) and cap \(72\), both give the same exact
522-dimensional radical vector and digest over 2,209 ordered pairs. The
literal collapsed replay uses 430 primitive products and 1,271 nonzero
orientations. A second audit at toy primes \(7\) and \(11\) found the same
normalization.

The Perron audit independently checked:

- \(s=(1+z)/2\);
- both Fourier signs;
- the exceptional \((1-x)^2(1-y)^2\) factor;
- absolute convergence exactly for \(\Re z>1\);
- the BV lemma needed for integrable Fourier inversion;
- the positive smooth-prefix mixture.

The native rank packet uses both the Fourier Gram and centered-incidence
coordinates. The function-field packets use Euler factorization and
coefficient recurrences, not curve or polynomial enumeration.

## 5. Computation boundary

This pass deliberately avoids heavy computation.

- Largest exact matrix dimension: 24.
- Largest function-field coefficient bidegree: 35.
- Field sizes in the finite recurrence replay: \(3,5,7\).
- Beta pair caps: 72 in the assembled replay and 40 in the band-pass replay.
- Zeta zeros enumerated: 0.
- Curves, points, closed points, polynomials, conductors, and
  \(L\)-functions enumerated: 0.
- Arithmetic is integer, rational, radical-basis, or symbolic except for
  small displayed approximations already fenced as replay output.

The continuation preserves that discipline. Its final carrier packet
uses no beta terms, primes, zeta zeros, random samples, or quadrature.
The full 447-test sweep completes in under one minute per Python mode on
this machine; no high-rank enumeration was introduced.

## 6. Refuted shortcuts

1. **BASEWAVE as an easier gate:** false; it is exactly PRIMCAR.
2. **Arbitrarily deep fixed notching kills the max zero mode:** false; the
   max cusp forces a positive linear leakage coefficient.
3. **A hidden local correction Euler product is the analytic obstruction:**
   false for the complete source; it collapses to one.
4. **The complete affine function-field theorem transfers to positive
   genus unchanged:** false; unit-circle Frobenius residues appear.
5. **Large internal \(QI-J\) rank is marked-place Adams separation
   rank:** false; the tensor axes were different.
6. **The natural raw source is already a marked-place external
   product:** false; the crossed core-selection/evaluation graph
   obstructs it.
7. **Wick centering lowers the internal \(QI-J\) rank:** false.
8. **Positive energy determines carrier chirality or compact zeros:**
   false; exact zero flips and spectral-factor surgeries preserve the
   autocorrelation.
9. **Widening an unrenormalized carrier always preserves an RH
   criterion:** false; raw energy has a cubic trivial-dilution escape.

## 7. Open gates

Direct beta architecture:

- arithmetic control of the exact nonnegative carrier-shape defect;
- improvement of the \(3\gamma/2\) raw-energy wedge using translated
  beta-convolution structure rather than abstract support data;
- an RH-bearing beta-energy estimate for either the raw subpower carrier
  or the width-renormalized parabolic carrier;
- signed beta energy inside the critical window
  \(e^{\sqrt{(\log2)(\log X)}}\);
- bilateral Perron boundary control without reciprocal-zeta absolute values;
- sharp endpoint recovery if one works through smooth positive prefix
  mixtures;
- an assembled reflection/differential estimate before the max cusp.

Function-field architecture:

- one incomplete owner/Boolean restriction;
- nontrivial cores and harmonic sieve averaging;
- cancellation or inverse design among named Frobenius residue channels;
- comparison with zero statistics only after the source adapter is exact.

Sheaf/amplifier architecture:

- actual physical residue occupancy;
- complete common signed selected/unselected pushforward;
- removal or geometric realization of the crossed marked-place graph;
- global equivariance of resonant and constant cleanup;
- correspondence-level Adams inversion or a source-specific sparse adapter;
- uniform Betti/conductor and signed trace estimates;
- CYSEL, WCADD, WCKUM, and principal-member individualization.

RH and GRH remain open.
