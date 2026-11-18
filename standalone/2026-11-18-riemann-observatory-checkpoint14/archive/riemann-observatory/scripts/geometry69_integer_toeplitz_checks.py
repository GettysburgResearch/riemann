"""Exact evaluation of the reciprocal-root trace form in the geometry69 audit."""

from fractions import Fraction


def reciprocal_trace_form(q, coefficients):
    """Build K from descending coefficients of a monic integral polynomial."""
    degree = len(coefficients) - 1
    if degree < 1 or type(q) is not int or q < 1:
        raise ValueError("Require degree >= 1 and positive integer q")
    if any(type(a) is not int for a in coefficients):
        raise ValueError("Require integer coefficients")
    constant = coefficients[-1]
    if coefficients[0] != 1 or constant == 0:
        raise ValueError("Require monicity and nonzero constant coefficient")

    powers = [q**k for k in range(degree + 1)]
    for k in range(degree + 1):
        if coefficients[degree - k] * powers[k] != constant * coefficients[k]:
            raise ValueError("Polynomial fails q-reciprocity")

    traces = [degree]
    for k in range(1, degree):
        partial = sum(coefficients[j] * traces[k - j] for j in range(1, k))
        traces.append(-k * coefficients[k] - partial)
    matrix = [
        [powers[min(i, j)] * traces[abs(i - j)] for j in range(degree)]
        for i in range(degree)
    ]
    return traces, matrix


def exact_inertia(matrix):
    """Return (positive, negative, zero) by rational congruence pivots."""
    work = [[Fraction(entry) for entry in row] for row in matrix]
    positive = negative = zero = 0
    while work:
        size = len(work)
        diagonal_pivot = next((i for i in range(size) if work[i][i]), None)
        if diagonal_pivot is not None:
            p = diagonal_pivot
            pivot = work[p][p]
            positive += int(pivot > 0)
            negative += int(pivot < 0)
            remaining = [i for i in range(size) if i != p]
            work = [
                [work[i][j] - work[i][p] * work[p][j] / pivot for j in remaining]
                for i in remaining
            ]
            continue

        pair = next(
            ((p, q) for p in range(size) for q in range(p + 1, size) if work[p][q]),
            None,
        )
        if pair is None:
            zero += size
            break
        p, q = pair
        pivot = work[p][q]
        positive += 1
        negative += 1
        remaining = [i for i in range(size) if i != p and i != q]
        work = [
            [
                work[i][j] - (work[i][p] * work[q][j] + work[i][q] * work[p][j]) / pivot
                for j in remaining
            ]
            for i in remaining
        ]
    return positive, negative, zero


def main():
    cases = [
        ("one root, negative reciprocal factor", 1, [1, -1], (1, 0, 0)),
        ("singular pure", 4, [1, -4, 4], (1, 0, 1)),
        ("nonsquare pure", 2, [1, 0, -2], (2, 0, 0)),
        ("two complex off-circle pairs", 4, [1, 0, 17, 0, 16], (2, 2, 0)),
        ("repeated off-circle pair", 4, [1, -10, 33, -40, 16], (1, 1, 2)),
        ("zero Schur diagonal, nonzero row", 1, [1, -4, 5, -4, 1], (3, 1, 0)),
        ("positive proper leading blocks", 100, [1, -21, 200, -2100, 10000], (3, 1, 0)),
    ]
    for description, q, coefficients, expected in cases:
        traces, matrix = reciprocal_trace_form(q, coefficients)
        assert exact_inertia(matrix) == expected
        rank = expected[0] + expected[1]
        leading = [row[:rank] for row in matrix[:rank]]
        assert exact_inertia(leading) == (*expected[:2], 0)
        if description == "positive proper leading blocks":
            assert traces == [4, 21, 41, 2961]
            assert all(abs(traces[i]) < 4 * 10**i for i in range(1, 4))
            assert exact_inertia([row[:3] for row in matrix[:3]]) == (3, 0, 0)
        print(f"{description}: {expected}")

    assert exact_inertia([[0, 1], [1, 0]]) == (1, 1, 0)
    assert exact_inertia([[2, 0], [0, 0]]) == (1, 0, 1)
    try:
        reciprocal_trace_form(4, [1, 0, 1])
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid reciprocity accepted")
    print("Exact congruence checks passed.")


if __name__ == "__main__":
    main()
