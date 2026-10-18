"""Execute each declared all-order negative control under optimized Python."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys


def main():
    here = Path(__file__).resolve().parent
    checker = here / 'verify_all_order.py'
    gates = {
        'wrong_plane_weight': 'positive supporting-plane certificate',
        'wrong_fe_sign': 'fourth reflected conductor exponent',
        'drop_type_ii_cross': 'retained native Type-II constant',
        'dense_subset_lindelof': 'actual dense selected fourth-mean exponent',
        'omit_diagonal_term': 'complete two-term physical norm',
        'old_mellin_shift': 'actual scale-dependent principal shift',
        'erase_power_mask': 'full phase/mask identity base=7, power=6',
        'add_coprimality': 'full phase/mask identity base=2, power=7',
        'erase_fixed_twist': 'full phase/mask identity base=2, power=6',
    }
    results = []
    for mutation, expected in gates.items():
        result = subprocess.run(
            [sys.executable, '-O', str(checker), '--mutation', mutation],
            capture_output=True, text=True, check=False)
        gate = 'CheckFailure: ' + expected
        if result.returncode == 0 or gate not in result.stderr:
            raise ValueError('Mutation did not reject at its expected gate: ' + mutation)
        results.append({'mutation': mutation, 'returncode': result.returncode,
                        'gate': gate})
    report = {
        'status': 'PASS',
        'scope': 'Nine separate optimized negative-control executions; not arithmetic counterexamples',
        'checker_sha256': hashlib.sha256(checker.read_bytes()).hexdigest(),
        'proof_sha256': hashlib.sha256((here / 'ALL_ORDER_BARRIER.md').read_bytes()).hexdigest(),
        'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'mutations': results,
    }
    text = json.dumps(report, indent=2, sort_keys=True) + '\n'
    (here / 'ALL_ORDER_MUTATIONS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
