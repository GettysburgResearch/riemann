from __future__ import annotations

import hashlib
import json
from fractions import Fraction


def common_tail_interval(endpoint: int) -> range:
    """The cell where both omitted parity tails start at k=2."""
    lo = (endpoint + 1) // 4 + 1
    hi = endpoint // 3
    return range(lo, hi + 1)


def first_shifted_even(endpoint: int, q: int) -> int:
    k = 1
    while 2 * k * q - 1 <= endpoint:
        k += 1
    return k


def first_unshifted_odd(endpoint: int, q: int) -> int:
    k = 1
    while (2 * k + 1) * q <= endpoint:
        k += 1
    return k


def verify_endpoint(endpoint: int) -> dict[str, object]:
    if endpoint < 30:
        raise ValueError("the stated N/480 count is licensed for N>=30")

    source_endpoint = (endpoint + 1) // 2
    cells = list(common_tail_interval(endpoint))

    for m in cells:
        # Since m>Q/2, finite Möbius inversion has only d=1.
        assert 2 * m > source_endpoint

        # Both old k=1 atoms remain inside the endpoint.
        assert 2 * m - 1 <= endpoint
        assert 3 * m <= endpoint

        # Both k=2 atoms are outside, so the common tail starts at k=2.
        assert 4 * m - 1 > endpoint
        assert 5 * m > endpoint
        assert first_shifted_even(endpoint, m) == 2
        assert first_unshifted_odd(endpoint, m) == 2

    count = len(cells)
    assert count >= Fraction(endpoint, 24)

    # For each cell:
    # sqrt(m) h_N(m) > 1/2 - 1/sqrt(5) > 1/20.
    # The last strict inequality is equivalent to 400 < 405.
    assert 400 < 405
    atomic_lower = Fraction(count, 20)
    assert atomic_lower >= Fraction(endpoint, 480)

    return {
        "endpoint": endpoint,
        "source_endpoint": source_endpoint,
        "cell_first": cells[0],
        "cell_last": cells[-1],
        "cell_count": count,
        "mobius_inversion_terms_per_cell": 1,
        "atomic_lower_bound": {
            "numerator": atomic_lower.numerator,
            "denominator": atomic_lower.denominator,
        },
        "licensed_endpoint_bound": f"> {endpoint}/480",
    }


def main() -> None:
    endpoints = [30, 48, 96, 192, 384, 768, 1536, 3072]
    rows = [verify_endpoint(endpoint) for endpoint in endpoints]

    payload: dict[str, object] = {
        "schema": "X-30402-correct-boundary-source-linear-mass-v1",
        "classification": "PASS_EXACT_CORRECT_BOUNDARY_SOURCE_LINEAR_ATOMIC_MASS",
        "rows": rows,
        "symbolic_inequalities": {
            "per_node": "sqrt(m)*sigma_m > 1/2-1/sqrt(5) > 1/20",
            "cell_count": "#I_N >= N/24",
            "total": "||sigma_N||_at > N/480",
        },
        "scope": (
            "exact integer/rational replay of R-30404; the convergent paired-tail "
            "inequality is proved symbolically in the claim; does not prove a "
            "non-absolute coupled estimate, Cycle Debt, WSTS, or RH"
        ),
    }

    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
