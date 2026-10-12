"""Exact local controls for the actual paired fourth-slot Euler factor."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def need(ok, label):
    if not ok:
        raise ArithmeticError(label)


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def conjugate(x):
    a, b = x
    return a-b, -b


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def factor(x, q):
    return F(1)-F(x[0], q), -F(x[1], q)


def run():
    here = Path(__file__).parent
    source = here/'PRIME_SLOT_CANCELLATION.md'
    need(hashlib.sha256(source.read_bytes()).hexdigest() ==
         'd37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13',
         'frozen source phases and full reciprocal-pair factorization')
    units = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
    counts = 0
    strict = 0
    for q in (7, 13, 19, 31):
        for a, u, v in product(units, repeat=3):
            left = [mul(a, u), mul(a, v)]
            slots = left+[conjugate(z) for z in left]
            pairs = (F(1), F(0))
            for i in range(4):
                for j in range(i+1, 4):
                    pairs = mul(pairs, factor(mul(slots[i], slots[j]), q))
            same = norm(factor(mul(mul(a, a), mul(u, v)), q))
            mixed = norm(factor(mul(u, conjugate(v)), q))
            explicit = same*F(q-1, q)**2*mixed
            bound = (1-F(1, q*q))**2*mixed
            need(pairs == (explicit, 0), 'all six source pair factors exactly reunited')
            need(explicit <= bound <= mixed, 'exact principal reciprocal bound')
            need(explicit > 0, 'nonzero eligible local pair factor')
            strict += explicit < bound
            counts += 1
    # Literal eta=1 at u=1, actual prime norm7, with arbitrary source Mellin phases.
    # Two phases +-i/sqrt7 give A1=0. Conjugate phases with cos(theta)=sqrt7/8 give A2=1/4.
    k11, k12, k22 = F(1), F(3, 4), F(1, 2)
    determinant = k11*k22-k12*k12
    need(determinant == -F(1, 16), 'positive local diagonals do not imply PSD')
    singles1, singles2 = F(8, 7), F(25, 28)
    c11, c12, c22 = k11/singles1**2, k12/(singles1*singles2), k22/singles2**2
    cd = c11*c22-c12*c12
    need((c11, c12, c22, cd) ==
         (F(49, 64), F(147, 200), F(392, 625), -F(2401, 40000)),
         'exact collision congruence retains local negative determinant')
    proof = here/'PAIRED_FREQUENCY_COLLISION.md'
    return dict(status='PASS_EXACT_PAIRED_FREQUENCY_COLLISION_CONTROLS',
                exact_six_pair_controls=counts, strict_triangle_controls=strict,
                actual_prime_norms=[7, 13, 19, 31], local_Euler_determinant=str(determinant),
                local_collision_matrix=[[str(c11), str(c12)], [str(c12), str(c22)]],
                local_collision_determinant=str(cd),
                proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                classical_global_reciprocal_zeta_proof_rebuilt=False,
                full_independent_frequency_trace_proved=False,
                generalized_moment_proved=False, rh_proved=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    print(json.dumps(result, indent=2))
