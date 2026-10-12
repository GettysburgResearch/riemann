#!/usr/bin/env python3
"""Audit frozen source inputs and exact scalar guards for EXPLICIT_ETA.md.

This does not replay the continuum quadrature or machine-prove the analytic
uniform modulus. It imports the reviewed full source enclosure explicitly.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys

import flint
from flint import arb, ctx

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
OLD = REPO/'research/exploratory/2026-10-10-four-hour-wave/operators'
sys.path.insert(0, str(OLD))
from enclose_analytic_upper import Source

FROZEN = {
    'enclose_analytic_upper.py': 'b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b',
    'source_convolution.py': 'd53aa6c4e9c0e33d26c2327305bc1aa0ae9adef035ea4437ccd2a19b23bbf014',
    'enclose_residual.py': 'e03d92bb09c1250b4a93e485aba6cc85bf2a4309b00e6d9217dbfbd39887cc92',
    'enclose_exact_primitive_synthesis.py': '009ae7df8ef5acdea2be122602d8c239eb0a36ac56563bf76640469926b8a011',
    'directed_residual_codim14_trial100.json': '9213accb90caa99e17172f620c3946ab638542eaf0523dfba89ab8f870d2016a',
    'directed_exact_synthesis_codim14_trial100.json': 'df598c783ec412941cfd13f3c07cb3054ae3ad32a613320318a5915ffcbe3551',
    'OPEN_WINDOW_PROPAGATION.md': '2ddf5a57e16c8b931b19299591cd2a9b99b280e8a13e3ebd0035d57630030d3c',
}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit('FAIL: '+message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def endpoint_q(value: arb) -> Q:
    need(value.is_finite() and value.is_exact(), 'finite exact native endpoint')
    mantissa, exponent = value.man_exp()
    return Q(int(mantissa))*Q(2)**int(exponent)


def interval(value: str) -> tuple[Q,Q]:
    x = arb(value)
    return endpoint_q(x.lower()), endpoint_q(x.upper())


def exact_positive_ldl(matrix: list[list[Q]]) -> list[Q]:
    n = len(matrix)
    need(all(len(row) == n for row in matrix), 'square exact rational matrix')
    need(all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)),
         'exact rational Hermitian real symmetry')
    lower = [[Q(i == j) for j in range(n)] for i in range(n)]
    diagonal = []
    for i in range(n):
        pivot = matrix[i][i]-sum((lower[i][k]**2*diagonal[k] for k in range(i)), Q(0))
        need(pivot > 0, 'strict exact rational LDL pivot '+str(i))
        diagonal.append(pivot)
        for j in range(i+1,n):
            numerator = matrix[j][i]-sum((lower[j][k]*lower[i][k]*diagonal[k]
                                         for k in range(i)), Q(0))
            lower[j][i] = numerator/pivot
    return diagonal


def robust_scalar_gate(data: dict, epsilon: Q) -> tuple[Q,list[Q]]:
    u = data['source_U_receipt']['U_matrix_balls']
    r = data['R_matrix_balls']
    n = 14
    need(len(u) == len(r) == n and all(len(row) == n for row in u+r),
         'complete source U/R inventory')
    raw = []
    for i in range(n):
        row = []
        for j in range(n):
            ulo,uhi = interval(u[i][j]); rlo,rhi = interval(r[i][j])
            row.append((ulo-Q(15,8)*rhi, uhi-Q(15,8)*rlo))
        raw.append(row)
    midpoint = [[(raw[i][j][0]+raw[j][i][0]+raw[i][j][1]+raw[j][i][1])/4
                 for j in range(n)] for i in range(n)]
    radius = [[(raw[i][j][1]+raw[j][i][1]-raw[i][j][0]-raw[j][i][0])/4
               for j in range(n)] for i in range(n)]
    row_budget = max(sum(row,Q(0)) for row in radius)
    robust = [[midpoint[i][j]-(row_budget+epsilon if i == j else 0)
               for j in range(n)] for i in range(n)]
    # Every admitted exact symmetric source matrix is >= midpoint-row_budget*I.
    return row_budget, exact_positive_ldl(robust)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE/'eta_certificate.json')
    args = parser.parse_args()
    ctx.prec = 256
    need(flint.__version__ == '0.9.0' and flint.__FLINT_VERSION__ == '3.6.0',
         'frozen directed audit backend')
    for name, expected in FROZEN.items():
        need(digest(OLD/name) == expected, 'frozen source identity '+name)
    data = json.loads((OLD/'directed_residual_codim14_trial100.json').read_text())
    synthesis = json.loads((OLD/'directed_exact_synthesis_codim14_trial100.json').read_text())
    need(data['status'] == 'DIRECTED_FULL_SOURCE_LOWER_ACCEPT_PENDING_ANALYTIC_REVIEW'
         and data['producer_sha256'] == FROZEN['enclose_residual.py']
         and data['source_U_receipt']['source_sha256'] == FROZEN['enclose_analytic_upper.py'],
         'exact imported reviewed complete scalar source receipt')
    need(data['total_panels'] == len(data['coverage']) == 696
         and data['precision_bits'] == 256 and data['gauss_order'] == 80
         and data['epsilon'] == '2^-60', 'frozen complete continuum parameters')
    source_u = data['source_U_receipt']
    need(source_u['removed_sine_modes'] == 11 and source_u['trial_modes'] == 100
         and source_u['complement_dimension'] == 14, 'native codimension14 source')
    coefficients = source_u['exact_trial_z_coefficients_balls']
    need(len(coefficients) == 114 and all(len(row) == 14 for row in coefficients),
         'complete fixed raw-basis coefficient inventory')
    sums = [sum((arb(row[j]).abs_upper() for row in coefficients),arb(0)) for j in range(14)]
    C = Q(10**7)
    need(all(value < C.numerator for value in sums), 'strict directed full coefficient C bound')
    epsilon0 = Q(1,10**11)
    row_budget,pivots = robust_scalar_gate(data,epsilon0)

    source = Source()
    need(source.cb.abs_upper() < arb(1)/2 and 0 < source.p2 < arb(3)/5
         and 0 < source.q2 < arb(1)/2, 'complete native source constants')
    need(source.log2 < arb(7)/10, 'native logarithm bound')
    need((arb(3)/5).exp() < 2 and (arb(8)/5).exp() < 5,
         'uniform exact rational exponential guards')
    need(arb.pi() < arb(22)/7 and arb.pi() > arb(333)/106,
         'native strict rational pi guards')
    need(Q(710)*(Q(10001,10000))**2 < Q(72)*Q(333,106)**2,
         'exact rational uniform complement guard')

    trace_b = Q(15,8)*sum((interval(data['R_matrix_balls'][i][i])[1] for i in range(14)),Q(0))
    need(trace_b < Q(1,4), 'complete frozen scalar residual trace reserve')
    need(synthesis['status'] == 'DIRECTED_EXACT_PRIMITIVE_SYNTHESIS_ACCEPT'
         and synthesis['producer_sha256'] == FROZEN['enclose_exact_primitive_synthesis.py']
         and synthesis['baseline']['residual_receipt_sha256'] == FROZEN['directed_residual_codim14_trial100.json']
         and synthesis['baseline']['removed_sine_modes'] == 11
         and len(synthesis['exact_Gz_squared_norm_balls']) == 14,
         'reviewed exact complete native synthesis import')
    synthesis_upper = interval(synthesis['synthesis_trace_ball'])[1]
    need(synthesis_upper < Q(3,4), 'complete frozen synthesis trace reserve')

    eta = Q(1,10**36); epsilon = Q(1,2*10**11)
    matrix_modulus = Q(2*10**10)*C*C
    trace_b_modulus = Q(15,8)*14*Q(3*10**8)*C*C
    synthesis_modulus = Q(7000)*C*C
    need(eta <= Q(1,10000), 'radius lies in protected no-prime3 cap')
    need(epsilon0-matrix_modulus*eta >= epsilon,
         'uniform finite effective lower reserve after full modulus')
    need(trace_b+trace_b_modulus*eta < 1, 'uniform full residual M=1')
    need(synthesis_upper+synthesis_modulus*eta < 1, 'uniform complete synthesis K=1')
    theta = epsilon/(2+epsilon)
    delta = min(epsilon/4,theta*Q(6,5)/2)
    need(theta == Q(1,400000000001) and delta == Q(1,800000000000),
         'exact quantitative native primitive constant')

    source_paths = [HERE/'EXPLICIT_ETA.md',Path(__file__).resolve()]
    source_paths += [OLD/name for name in FROZEN]
    source_paths += [OLD/name for name in [
        'CODIMENSION_14_REFINEMENT.md','WINDOW_FAMILY_TO_LOG3.md',
        'NATIVE_WINDOW_CERTIFICATE_FRAME.md','COMPLETE_XI_KERNEL_BINDING.md',
        'NATIVE_WINDOW_FINAL_CERTIFICATE.md','EXACT_PRIMITIVE_SYNTHESIS.md',
        'QUANTITATIVE_PRIMITIVE_COMPLETION.md']]
    source_paths += [OLD.parent/'literature'/name for name in [
        'COMPLETED_NATIVE_LOWER_INDEPENDENT_REVIEW.md',
        'EXACT_PRIMITIVE_SYNTHESIS_INDEPENDENT_REVIEW.md']]
    result = {
        'status':'PASS_SOURCE_BOUND_EXPLICIT_NATIVE_ETA_AUDIT',
        'eta_exact':str(eta), 'upper_length_exact':str(1+eta),
        'native_primitive_delta_exact':str(delta), 'theta_exact':str(theta),
        'continuity_scope':'Every real0<L<=1+eta and every complex native L2 test; compact primitive norm only.',
        'coefficient_C_exact':str(C),
        'directed_column_absolute_sum_balls':[value.str(50,more=True) for value in sums],
        'complete_coefficient_rows':114, 'native_tests':14,
        'scalar_gate_initial_epsilon_exact':str(epsilon0),
        'scalar_gate_uniform_epsilon_exact':str(epsilon),
        'fresh_fraction_scalar_LDL_pivots_positive':len(pivots),
        'fresh_scalar_matrix_row_radius_exact':str(row_budget),
        'matrix_length_modulus_exact':str(matrix_modulus),
        'maximum_matrix_variation_exact':str(matrix_modulus*eta),
        'scalar_residual_trace_upper_exact':str(trace_b),
        'scalar_residual_trace_modulus_exact':str(trace_b_modulus),
        'complete_synthesis_trace_upper_exact':str(synthesis_upper),
        'complete_synthesis_trace_modulus_exact':str(synthesis_modulus),
        'uniform_M_exact':'1', 'uniform_K_exact':'1', 'uniform_primitive_gap_exact':'6/5',
        'rounding':'Native Arb outward bounds for source constants/coefficient balls, exact dyadic endpoints and Fraction-only LDL/radius guards.',
        'native_source_constants_freshly_recomputed':True,
        'old_full_continuum_integral_replayed_here':False,
        'old_full_source_receipt_explicitly_imported':True,
        'analytic_uniform_kernel_and_projection_moduli_machine_proved':False,
        'moving_prime2_derivative_jump_included_in_analytic_modulus':True,
        'moving_Cholesky_or_Galerkin_coefficients_used':False,
        'midpoint_coefficients_used':False,
        'L2_spectral_gap_claimed':False, 'RH_proved':False,
        'source_sha256':{str(path.relative_to(REPO)):digest(path) for path in source_paths},
        'python_flint_version':flint.__version__, 'flint_version':flint.__FLINT_VERSION__,
    }
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['status'],'ETA',str(eta),'DELTA',str(delta),flush=True)


if __name__ == '__main__':
    main()
