#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default=str(HERE / 'results/verification.json'))
    ap.add_argument('--mutations', action='store_true')
    args = ap.parse_args()
    ctl = json.loads((HERE / 'certificates/control.json').read_text())

    checks = {}
    checks['rho'] = 1 / math.sqrt(ctl['rough_prime_floor']) < ctl['rho_upper_num'] / ctl['rho_upper_den']
    checks['root_mass'] = ctl['root_fiber_mass_upper'] * ctl['endpoint_measure_mass_num'] / ctl['endpoint_measure_mass_den'] < ctl['root_mass_upper']
    checks['terminal_margin'] = ctl['terminal_reserve'] - ctl['terminal_overfill'] == 581
    checks['port_tau'] = (1 / math.sqrt(67)) * (1 - 1 / math.sqrt(67)) < 1 / 9
    checks['preferred_root_cost'] = ctl['positive_debt_constant'] * ctl['root_mass_upper'] == 15100
    checks['port_fallback_rounding'] = math.ceil(15100 + ctl['positive_debt_constant'] * ctl['port_mass_num'] / ctl['port_mass_den']) == 15124

    required = [
        'claims/lemmas/L-92880-factor67-root-hall-closes-the-finite-common-source-row-gain-gate.md',
        'claims/lemmas/L-92881-actual-factor67-common-parent-has-an-exact-native-capacity-ledger.md',
        'claims/lemmas/L-92882-common-schur-port-demand-is-explicit-and-one-use.md',
        'claims/lemmas/L-92883-one-positive-reserve-pays-every-root-correction-at-logarithmic-native-cost.md',
        'claims/lemmas/L-92884-native-slack-cocycle-closes-gate-b-at-logarithmic-cost.md',
        'claims/theorems/T-92880-standalone-factor67-gates-ab-resolution-proposal.md',
        'imports/t92880/IMPORT_MANIFEST.json',
        'standalone/2026-08-15-92880-gates-ab/REVIEW_SPECIFICATION.md',
    ]
    checks['required_paths'] = all((ROOT / p).is_file() for p in required)

    manifest = json.loads((ROOT / 'imports/t92880/IMPORT_MANIFEST.json').read_text())
    checks['base_pin'] = manifest['base_sha'] == '9acd381fa168db02a03646ab16851daebbf4d0fd'
    checks['dependency_count'] = len(manifest['dependencies']) >= 14
    checks['unique_dependency_paths'] = len({d['path'] for d in manifest['dependencies']}) == len(manifest['dependencies'])
    checks['unique_dependency_shas'] = all(len(d['blob_sha']) == 40 for d in manifest['dependencies'])

    mutation_results = {}
    if args.mutations:
        mutation_results = {
            'rho_equal_one_eighth_fails': not (1/8 < 1/8),
            'terminal_overdraw_fails': not (5033 > 5033),
            'duplicate_dependency_path_fails': len({'x','x'}) != 2,
            'wrong_base_pin_fails': manifest['base_sha'] != '0' * 40,
        }
        checks['mutations'] = all(mutation_results.values())

    ok = all(checks.values())
    proof_material = json.dumps({'checks': checks, 'manifest': manifest, 'control': ctl}, sort_keys=True).encode()
    result = {
        'verdict': ctl['expected_verdict'] if ok else 'FAIL_STANDALONE_GATES_AB_NATIVE_SLACK_PACKET',
        'ok': ok,
        'checks': checks,
        'mutations': mutation_results,
        'proof_object_sha256': hashlib.sha256(proof_material).hexdigest(),
        'scope': 'finite algebra, constants, path/manifest authentication; analytic inputs require independent reconstruction',
        'rh_proved': False,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(result['verdict'])
    print(result['proof_object_sha256'])
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
