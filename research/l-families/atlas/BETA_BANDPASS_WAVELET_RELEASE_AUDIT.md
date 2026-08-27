# Beta band-pass and curve-wavelet successor: release audit

Status: **audited exploratory successor; exact claims are separated from
open RH-strength estimates**

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

## 1. Commit ledger

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

At the audited theorem head:

- all eight new producers and the amended rho-wavelet predecessor producer
  passed normally and under optimized Python;
- all 78 tests in the nine relevant modules passed in both modes;
- Ruff lint passed on all seventeen changed producer/test Python files;
- Ruff format check passed on all seventeen;
- the new Markdown packets contain no embedded control bytes;
- local Markdown links from the two successor front doors resolve;
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

## 6. Refuted shortcuts

1. **BASEWAVE as an easier gate:** false; it is exactly PRIMCAR.
2. **Arbitrarily deep fixed notching kills the max zero mode:** false; the
   max cusp forces a positive linear leakage coefficient.
3. **A hidden local correction Euler product is the analytic obstruction:**
   false for the complete source; it collapses to one.
4. **The complete affine function-field theorem transfers to positive
   genus unchanged:** false; unit-circle Frobenius residues appear.
5. **Termwise Adams extraction survives the native phase tensor:** false on
   the universal phase/incidence block.
6. **Wick centering lowers that universal separation rank:** false.

## 7. Open gates

Direct beta architecture:

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
- complete common relative selected/unselected complex;
- global equivariance of resonant and constant cleanup;
- correspondence-level Adams inversion or a source-specific sparse adapter;
- uniform Betti/conductor and signed trace estimates;
- CYSEL, WCADD, WCKUM, and principal-member individualization.

RH and GRH remain open.
