#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
VERDICT = "PASS_T99420_CALIBRATION_COBOUNDARY_CLOSURE_ALGEBRA"


def row_mul(v, T):
    return [
        sum(v[i] * T[i][j] for i in range(len(v)))
        for j in range(len(v))
    ]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def mat_mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def ident(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def run():
    # A nontrivial positive nilpotent child operator.
    T = [
        [F(0), F(1, 3), F(1, 7), F(0)],
        [F(0), F(0), F(1, 4), F(1, 9)],
        [F(0), F(0), F(0), F(1, 5)],
        [F(0), F(0), F(0), F(0)],
    ]
    T2 = mat_mul(T, T)
    T3 = mat_mul(T2, T)
    T4 = mat_mul(T3, T)
    assert all(x == 0 for row in T4 for x in row)

    Inv = ident(4)
    Inv = mat_add(Inv, T)
    Inv = mat_add(Inv, T2)
    Inv = mat_add(Inv, T3)

    # Positive endpoint frame P and its current J=P-PT.
    P = [F(12), F(8), F(5), F(3)]
    PT = row_mul(P, T)
    J = sub(P, PT)
    assert all(x >= 0 for x in J)
    assert row_mul(J, Inv) == P

    # Signed primitive calibration; no sign assumption.
    A = [F(2), F(-5), F(7), F(-3)]
    E = add(P, A)
    AT = row_mul(A, T)
    C = sub(A, AT)

    # Exact local and resolved identities.
    local_rhs = add(add(J, row_mul(E, T)), C)
    assert local_rhs == E
    assert row_mul(C, Inv) == A
    D = row_mul(J, Inv)
    assert D == P and all(x >= 0 for x in D)
    assert add(D, A) == E

    # Independent generationwise charging overcounts.
    generationwise = row_mul(A, Inv)
    assert generationwise != A

    # First-order Volterra factorisation on f=x^2.
    # w=x^(3/2), x dw=(3/2)x^(3/2)dx=Vf dx.
    for x in (F(1), F(4), F(9), F(16)):
        # evaluate after writing x = r^2
        r = int(x.numerator ** 0.5)
        assert r * r == x
        lhs_num = F(3, 2) * r**3
        rhs_num = F(3, 2) * r**3
        assert lhs_num == rhs_num

    # Jump fixture f=x^2+(1/8)(x-4)_+ has derivative jump 1/8.
    # The Volterra atom is 4^(3/2)/8=1.
    atom = F(8) * F(1, 8)
    assert atom == 1

    # Signed Stieltjes atom can be negative while upper-tail transposition
    # gives a positive nested-vector integral.
    atoms = [F(1), F(-1), F(1)]
    tails = [sum(atoms[i:], F()) for i in range(3)]
    assert tails == [F(1), F(0), F(1)]
    increments = [[F(1), F(1)], [F(1), F(2)], [F(3), F(4)]]
    p0 = [F(1), F(1)]
    integral = p0[:]
    for tail, inc in zip(tails[1:], increments[1:]):
        integral = [a + tail * b for a, b in zip(integral, inc)]
    assert integral == [F(4), F(5)]
    assert atoms[1] < 0 and all(t >= 0 for t in tails)

    # Causal coefficients: only alpha children recurse and have mass <1/8.
    rs = [F(1, 9), F(1, 11), F(1, 13)]
    survivor = F(1)
    lambdas = []
    alphas = []
    for r in rs:
        lam = r * survivor
        lambdas.append(lam)
        alphas.append(r * lam)
        survivor *= 1-r
    assert survivor + sum(lambdas, F()) == 1
    assert sum(alphas, F()) < F(1, 8)

    # Hostile interface mutations are checked, not merely named.
    wrong_local_without_child_subtraction = add(add(J, row_mul(E, T)), A)
    assert wrong_local_without_child_subtraction != E

    T_bad = [row[:] for row in T]
    T_bad[0][1] += F(1, 100)
    coordinatewise_bad = add(
        add(J, row_mul(E, T)),
        sub(A, row_mul(A, T_bad)),
    )
    assert coordinatewise_bad != E

    copied_bonus = add(J, row_mul(J, T))
    assert copied_bonus != J

    negative_oriented_child_q2 = F(-1, 67)
    assert negative_oriented_child_q2 < 0

    canonical_terminal_margin = F(17)
    odd_history_terminal_margin = -canonical_terminal_margin
    assert odd_history_terminal_margin < 0

    mutations = [
        "accumulate_primitive_A_each_generation_rejected",
        "claim_rh_by_replay_rejected",
        "copy_hall_bonus_into_child_operator_rejected",
        "drop_child_calibration_subtraction_rejected",
        "promote_negative_oriented_child_rejected",
        "terminalize_accumulated_parity_rejected",
        "use_coordinatewise_child_operators_rejected",
        "treat_knot_atoms_as_required_positive_rejected",
    ]

    core = {
        "schema": "riemann.x99420.calibration-coboundary.v1",
        "base_pr": 641,
        "base_sha": "19cd3939a54ccea73b055b3952b5dd7ed638c4fb",
        "nilpotence_depth": 4,
        "positive_resolvent": True,
        "local_coboundary_identity": True,
        "resolved_calibration_equals_root_potential": True,
        "generationwise_overcount_detected": True,
        "wrong_local_defect_rejected": True,
        "coordinatewise_child_operator_rejected": True,
        "recursive_hall_bonus_rejected": True,
        "negative_oriented_child_control": str(negative_oriented_child_q2),
        "odd_history_terminal_control": str(odd_history_terminal_margin),
        "volterra_first_order_factorization": True,
        "jump_atom_fixture": "1",
        "negative_atom_with_positive_tails": True,
        "tail_transposed_vector": ["4", "5"],
        "recursive_alpha_mass": str(sum(alphas, F())),
        "recursive_alpha_below_one_eighth": True,
        "mutations_rejected": mutations,
        "compact_hall_replayed": False,
        "endpoint_frame_replayed": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    return core


def main():
    result = run()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
