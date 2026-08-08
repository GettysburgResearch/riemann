from fractions import Fraction
import hashlib
import json


def v2(n):
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def scale(c, a):
    if c >= 0:
        return (c * a[0], c * a[1])
    return (c * a[1], c * a[0])


def mul(a, b):
    values = (
        a[0] * b[0],
        a[0] * b[1],
        a[1] * b[0],
        a[1] * b[1],
    )
    return (min(values), max(values))


def square(a):
    if a[0] >= 0:
        return (a[0] * a[0], a[1] * a[1])
    if a[1] <= 0:
        return (a[1] * a[1], a[0] * a[0])
    return (Fraction(0), max(a[0] * a[0], a[1] * a[1]))


def reduced_log_interval(y, terms=64):
    # 1 <= y < 2.  log y = 2 atanh((y-1)/(y+1)).
    assert Fraction(1) <= y < Fraction(2)
    z = (y - 1) / (y + 1)
    z2 = z * z
    term = z
    total = Fraction(0)
    for i in range(terms):
        total += term / (2 * i + 1)
        term *= z2
    lower = 2 * total
    remainder = 2 * term / ((2 * terms + 1) * (1 - z2))
    return (lower, lower + remainder)


def log_interval(x, terms=64):
    assert x > 0
    y = Fraction(x)
    k = 0
    while y >= 2:
        y /= 2
        k += 1
    while y < 1:
        y *= 2
        k -= 1

    log2 = reduced_log_interval(Fraction(2), terms)
    logy = reduced_log_interval(y, terms)
    if k >= 0:
        return add(scale(k, log2), logy)
    return add(scale(k, (log2[1], log2[0])), logy)


def reserve_and_endpoint_intervals(n):
    even = n if n % 2 == 0 else n - 1
    odd = n - 1 if n % 2 == 0 else n
    r = v2(even)

    le = log_interval(even)
    lo = log_interval(odd)
    ell = log_interval(2)

    reserve = add(
        add(
            scale(2, mul(le, sub(lo, scale(2, ell)))),
            scale(2 * (r - 2), mul(ell, lo)),
        ),
        scale(r * r - 3 * r + 6, square(ell)),
    )

    endpoint = add(log_interval(n), scale(v2(n), ell))
    return reserve, endpoint


def main():
    rows = []
    for n in range(4, 16):
        reserve, endpoint = reserve_and_endpoint_intervals(n)
        margin32 = sub(scale(32, reserve), square(endpoint))
        assert margin32[0] > 0, (n, margin32)
        row = {
            "n": n,
            "margin32_lower": str(margin32[0]),
        }
        if n == 4:
            margin16 = sub(scale(16, reserve), square(endpoint))
            assert margin16[0] > 0, margin16
            row["margin16_lower"] = str(margin16[0])
        rows.append(row)

    result = {
        "finite_rows": rows,
        "rows_checked": len(rows),
        "log_interval_terms": 64,
        "verdict": "PASS_EXACT_TWO_CONTACT_ENDPOINT_RESERVE",
    }
    proof_object = json.dumps(
        result, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    result["proof_object_sha256"] = hashlib.sha256(proof_object).hexdigest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
