import RiemannFormal.Arithmetic.FixedRows
import RiemannFormal.Arithmetic.HalfDivisor
import RiemannFormal.Arithmetic.SourceIdentities
import RiemannFormal.Arithmetic.Wavelet
import RiemannFormal.MellinLandau.FixedDetectorAssembly

-- Exact fixed-row algebra.
#print axioms RiemannFormal.Arithmetic.FixedRows.rows23_no_common_zero
#print axioms RiemannFormal.Arithmetic.FixedRows.fiveThree_nonzero

-- Generic first-owner helper, deliberately not the canonical L-99601 theorem.
#print axioms RiemannFormal.Arithmetic.SourceIdentities.scalarFirstOwnerExpansion_eq_finiteEulerProduct

-- Exact source firewalls and reviewed finite fixtures.
#print axioms RiemannFormal.Arithmetic.SourceIdentities.duplicate67_same_prime_distinct_labels
#print axioms RiemannFormal.Arithmetic.SourceIdentities.duplicate67_parity_fixture
#print axioms RiemannFormal.Arithmetic.SourceIdentities.native_one_prime_ne_contracted_two_child
#print axioms RiemannFormal.Arithmetic.SourceIdentities.raw_cutoff_ne_rn_child_16_4_4
#print axioms RiemannFormal.Arithmetic.SourceIdentities.rn_density_times_capacity_eq_response_16_4_4
#print axioms RiemannFormal.Arithmetic.SourceIdentities.response_capacity_coefficients_differ_16_4_4
#print axioms RiemannFormal.Arithmetic.SourceIdentities.normalized_p_inv_ne_p_inv_sqrt

-- Exact API boundary: direct role inequalities plus explicit reconstruction.
#print axioms RiemannFormal.Arithmetic.native_ne_auxiliary
#print axioms RiemannFormal.Arithmetic.response_ne_capacity
#print axioms RiemannFormal.Arithmetic.signedObservation_ne_auxiliaryPositive
#print axioms RiemannFormal.Arithmetic.rebuildAtRole_coefficient
#print axioms RiemannFormal.Arithmetic.FixedArithmeticDetector.asConstantMoving_queryIndependent

-- Half-divisor finite coefficient and arithmetic-function scope.
#print axioms RiemannFormal.Arithmetic.HalfDivisor.etaCoeff_antidiagonal
#print axioms RiemannFormal.Arithmetic.HalfDivisor.eta_mul_eta
#print axioms RiemannFormal.Arithmetic.HalfDivisor.genericOneFieldConvolution

-- Generic finite wavelet helpers and type firewall.
#print axioms RiemannFormal.Arithmetic.Wavelet.fourTapValues_geometric
#print axioms RiemannFormal.Arithmetic.Wavelet.threeTap_minimal
#print axioms RiemannFormal.Arithmetic.Wavelet.affine_nuisance_sign_flip
#print axioms RiemannFormal.Arithmetic.Wavelet.fourTap_shift
#print axioms RiemannFormal.Arithmetic.Wavelet.finite_sum_by_parts
#print axioms RiemannFormal.Arithmetic.Wavelet.K0_ne_K1

-- Non-circular arithmetic-side consumer packages.  These conclude only finite data.
#print axioms RiemannFormal.MellinLandau.fixedFiveThreeArithmeticInput_spec
#print axioms RiemannFormal.MellinLandau.fixedRows23ArithmeticInput_spec
