#!/usr/bin/env python3
"""Fresh source-bound eta audit followed by exact trace-priced completion."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
FROZEN = {
    'EXPLICIT_ETA.md': '55895ae36d87322cdc4ca3424027bcc63e5a020a0803650a7d2e21d215352ff8',
    'check_eta.py': 'b056bc4411acec38a6e81b8c085b8c04d393acc26c1eed931da2b9e604909d70',
    'results/eta.normal.json': '08540515ea0b484bab3d26cb7fe0cda46a746135d3c8faea4977e5f40046ded4',
}


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    for name, digest in FROZEN.items():
        need(sha(HERE / name) == digest, ('frozen eta input', name))
    with tempfile.TemporaryDirectory(prefix='riemann-trace-priced-eta-') as tmp:
        out = Path(tmp) / 'fresh-eta.json'
        command = [sys.executable, '-B']
        if sys.flags.optimize:
            command.append('-O')
        command += [str(HERE / 'check_eta.py'), '--output', str(out)]
        subprocess.run(command, cwd=REPO, check=True, capture_output=True, text=True)
        fresh = json.loads(out.read_text())
    saved = json.loads((HERE / 'results/eta.normal.json').read_text())
    need(fresh == saved, 'entire frozen eta receipt equals fresh audit')
    for name, digest in fresh['source_sha256'].items():
        need(sha(REPO / name) == digest, ('actual frozen source', name))
    eta = Q(fresh['eta_exact'])
    epsilon = Q(fresh['scalar_gate_initial_epsilon_exact']) - Q(fresh['matrix_length_modulus_exact']) * eta
    need(epsilon == Q(1, 125000000000), 'complete existing uniform epsilon8e-12')
    m_upper = Q(fresh['scalar_residual_trace_upper_exact']) + Q(fresh['scalar_residual_trace_modulus_exact']) * eta
    k_upper = Q(fresh['complete_synthesis_trace_upper_exact']) + Q(fresh['complete_synthesis_trace_modulus_exact']) * eta
    M = Q(1, 2000)
    K = Q(13, 25)
    kappa = Q(fresh['uniform_primitive_gap_exact'])
    need(m_upper < M and k_upper < K and kappa == Q(6, 5), 'strict trace-priced source caps')
    root_cap = Q(9, 500)
    need(M * K * kappa < root_cap ** 2, 'exact radical upper cap')
    denominator_cap = epsilon + M + K * kappa + 2 * root_cap
    delta = Q(9, 5) * epsilon
    need(denominator_cap < Q(2, 3), 'complete trace denominator below2/3')
    need(delta * denominator_cap <= epsilon * kappa, 'exact improved primitive reserve')
    need(delta == Q(9, 625000000000), 'exact native eta constant')
    old_epsilon = Q(fresh['scalar_gate_initial_epsilon_exact'])
    old_delta = Q(9, 5) * old_epsilon
    need(old_delta * (old_epsilon + M + K * kappa + 2 * root_cap) <= old_epsilon * kappa, 'original L1 trace-priced reserve')
    physical_epsilon = Q(1, 20000000000)
    for physical_M, physical_K, physical_kappa, cap, multiplier in [
        (Q(1), Q(3, 5), Q(1, 2), Q(11, 20), Q(1, 5)),
        (Q(1, 2), Q(3, 5), Q(1, 2), Q(2, 5), Q(3, 10)),
    ]:
        need(physical_M * physical_K * physical_kappa < cap ** 2, 'conditional physical radical cap')
        need(multiplier * (physical_epsilon + physical_M + physical_K * physical_kappa + 2 * cap) <= physical_kappa, 'conditional physical exact reserve')
    source_hashes = dict(fresh['source_sha256'])
    for path in [HERE / 'TRACE_PRICED_COMPLETION.md', Path(__file__), HERE / 'results/eta.normal.json']:
        source_hashes[str(path.relative_to(REPO))] = sha(path)
    return {
        'status': 'PASS_SOURCE_BOUND_TRACE_PRICED_NATIVE_ETA_AUDIT',
        'eta_exact': str(eta), 'upper_length_exact': str(1 + eta),
        'epsilon_exact': str(epsilon), 'M_exact': str(M), 'K_exact': str(K),
        'kappa_exact': str(kappa), 'native_primitive_delta_exact': str(delta),
        'scalar_dual_uniform_upper_exact': str(m_upper),
        'synthesis_uniform_upper_exact': str(k_upper),
        'radical_upper_exact': str(root_cap),
        'denominator_upper_exact': str(denominator_cap),
        'original_L1_delta_exact': str(old_delta),
        'fresh_complete_eta_audit_replayed': True,
        'native_continuum_quadrature_replayed': False,
        'analytic_continuity_moduli_machine_proved': False,
        'conditional_physical_reserves_exact': ['1/100000000000', '3/200000000000'],
        'physical_native_gate_replayed': False,
        'physical_new_sign_claimed': False,
        'native_L2_gap_claimed': False,
        'RH_proved': False,
        'source_sha256': source_hashes,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['status'], result['native_primitive_delta_exact'])
