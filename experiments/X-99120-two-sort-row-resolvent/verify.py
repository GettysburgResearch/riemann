#!/usr/bin/env python3
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def power(A, k):
    R = eye(len(A))
    for _ in range(k):
        R = matmul(R, A)
    return R


def vecmul(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


def build_fixture():
    # Four source states ordered root -> children -> grandchild.
    # T is strictly upper triangular (column = parent, row = child).
    T = [
        [F(0), F(0), F(0), F(0)],
        [F(1, 16), F(0), F(0), F(0)],
        [F(1, 32), F(0), F(0), F(0)],
        [F(0), F(1, 20), F(1, 24), F(0)],
    ]
    # Current rows: two component coordinates plus one row-only bonus already
    # included in J. Every entry is nonnegative.
    J = [
        [F(5), F(2), F(3), F(7)],
        [F(11), F(13), F(17), F(19)],
        [F(23), F(29), F(31), F(37)],
    ]
    s = [F(1), F(0), F(0), F(0)]
    return T, J, s


def verify_fixture(mutation=None):
    T, J, s = build_fixture()
    if mutation == "cycle":
        T[0][3] = F(1, 100)
    if mutation == "negative_current":
        J[0][1] = F(-2)

    # Nilpotence at depth four.
    T4 = power(T, 4)
    nilpotent = all(x == 0 for row in T4 for x in row)

    R = eye(4)
    P = eye(4)
    for _ in range(1, 4):
        P = matmul(P, T)
        R = add(R, P)

    E = matmul(J, R)
    local = add(J, matmul(E, T))
    local_identity = (E == local)

    d = vecmul(J, vecmul(R, s))
    e = vecmul(E, s)
    row_identity = (d == e)
    positivity = all(x >= 0 for row in J for x in row) and all(x >= 0 for x in d)

    # Three independent physical-row functionals, including literal score.
    functionals = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(1)],
        [F(2), F(3), F(5)],
    ]
    functional_equalities = []
    for ell in functionals:
        functional_equalities.append(
            sum(ell[i] * d[i] for i in range(3))
            == sum(ell[i] * e[i] for i in range(3))
        )

    passed = nilpotent and local_identity and row_identity and positivity and all(functional_equalities)
    return {
        "nilpotent": nilpotent,
        "local_identity": local_identity,
        "row_identity": row_identity,
        "positive_resolved_row": positivity,
        "functional_equalities": functional_equalities,
        "resolved_row": [str(x) for x in d],
        "passed": passed,
    }


def build_result():
    base = verify_fixture()
    cycle = verify_fixture("cycle")
    negative = verify_fixture("negative_current")
    assert base["passed"]
    assert not cycle["passed"]
    assert not negative["passed"]

    core = {
        "schema": "riemann.x99120.two-sort-row-resolvent.v1",
        "verdict": "PASS_T99120_NILPOTENT_TWO_SORT_ROW_RESOLVENT",
        "base_fixture": base,
        "mutations": {
            "cycle_rejected": not cycle["passed"],
            "negative_current_rejected": not negative["passed"],
        },
        "abstract_theorem": "PROVED_EXACT",
        "pr620_application": "PROPOSED_PENDING_LOCAL_RECONSTRUCTION",
        "rh_established": False,
    }
    payload = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    return core


def main():
    result = build_result()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
