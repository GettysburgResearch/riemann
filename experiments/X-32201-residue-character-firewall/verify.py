from __future__ import annotations

import hashlib
import json


def gadd(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return (x[0] + y[0], x[1] + y[1])


def gmul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x: tuple[int, int]) -> tuple[int, int]:
    return (x[0], -x[1])


POW_I = [(1, 0), (0, 1), (-1, 0), (0, -1)]
EXP5 = {1: 0, 2: 1, 4: 2, 3: 3}


def chi5(j: int, n: int) -> tuple[int, int]:
    r = n % 5
    if r == 0:
        return (0, 0)
    return POW_I[(j * EXP5[r]) % 4]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    m = n
    count = 0
    d = 2
    while d * d <= m:
        if m % d == 0:
            e = 0
            while m % d == 0:
                m //= d
                e += 1
            if e >= 2:
                return 0
            count += 1
        d += 1
    if m > 1:
        count += 1
    return -1 if count % 2 else 1


def run() -> dict[str, object]:
    orthogonality = 0
    for j in range(4):
        for k in range(4):
            total = (0, 0)
            for r in (1, 2, 3, 4):
                total = gadd(total, gmul(chi5(j, r), gconj(chi5(k, r))))
            assert total == ((4, 0) if j == k else (0, 0))
            orthogonality += 1

    inverse_rows = 0
    for j in range(4):
        for n in range(1, 257):
            total = (0, 0)
            for d in range(1, n + 1):
                if n % d:
                    continue
                term = gmul((mobius(d), 0), gmul(chi5(j, d), chi5(j, n // d)))
                total = gadd(total, term)
            assert total == ((1, 0) if n == 1 else (0, 0))
            inverse_rows += 1

    dft_rows = 0
    vectors = [
        {1: (1, 0), 2: (2, 1), 3: (-1, 2), 4: (3, -2)},
        {1: (0, 0), 2: (1, -1), 3: (1, 1), 4: (-2, 0)},
    ]
    for vector in vectors:
        coeffs: list[tuple[int, int]] = []
        for j in range(4):
            total = (0, 0)
            for r in (1, 2, 3, 4):
                total = gadd(total, gmul(chi5(j, r), vector[r]))
            coeffs.append(total)
        for r in (1, 2, 3, 4):
            total = (0, 0)
            for j in range(4):
                total = gadd(total, gmul(gconj(chi5(j, r)), coeffs[j]))
            assert total[0] % 4 == 0 and total[1] % 4 == 0
            assert (total[0] // 4, total[1] // 4) == vector[r]
            dft_rows += 1

    result: dict[str, object] = {
        "schema": "X-32201-residue-character-firewall-v1",
        "classification": "PASS_EXACT_MOD5_CHARACTER_AND_DIRICHLET_INVERSE_ALGEBRA",
        "checks": {
            "character_orthogonality": orthogonality,
            "dirichlet_inverse_rows": inverse_rows,
            "dft_inversion_rows": dft_rows,
            "mod2_nonprincipal_characters": 0,
        },
        "proof_boundary": (
            "finite character/convolution algebra only; no GRH, residue contraction, "
            "CBVR, or RH proof"
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["result_sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
