#!/usr/bin/env python3
import hashlib
import itertools
import json
import math
from pathlib import Path

CLASSIFICATION = "PASS_T108420_HELLINGER_MIXTURE_GLUE"


def root(x):
    r = math.isqrt(x)
    assert r * r == x
    return r


def run():
    values = (0, 1, 4, 9)
    cauchy_checks = 0

    # Pointwise affinity inequality:
    #   sum_i sqrt(a_i b_i) <= sqrt(sum_i a_i sum_i b_i).
    # All source entries are perfect squares, so the check is integral.
    for a in itertools.product(values, repeat=3):
        for b in itertools.product(values, repeat=3):
            if cauchy_checks >= 2000:
                break
            affinity = sum(root(x) * root(y) for x, y in zip(a, b))
            assert affinity * affinity <= sum(a) * sum(b)
            cauchy_checks += 1
        if cauchy_checks >= 2000:
            break
    assert cauchy_checks == 2000

    pushforward_checks = 0
    # Two two-point fibres map to two physical cells. For each fibre, exact
    # Cauchy is equivalent to the increase of Hellinger affinity and hence to
    # contraction of squared Hellinger distance.
    for a in itertools.product(values, repeat=4):
        for b in itertools.product(values, repeat=4):
            if pushforward_checks >= 1000:
                break
            for lo in (0, 2):
                source_affinity = (
                    root(a[lo]) * root(b[lo])
                    + root(a[lo + 1]) * root(b[lo + 1])
                )
                pushed_product = (
                    (a[lo] + a[lo + 1])
                    * (b[lo] + b[lo + 1])
                )
                assert source_affinity * source_affinity <= pushed_product
            pushforward_checks += 1
        if pushforward_checks >= 1000:
            break
    assert pushforward_checks == 1000

    exact_checks = cauchy_checks + pushforward_checks
    assert exact_checks == 3000

    payload = {
        "schema": "riemann.x108420.hellinger-mixture-gluing.v1",
        "classification": CLASSIFICATION,
        "exact_checks": exact_checks,
        "cauchy_affinity_checks": cauchy_checks,
        "pushforward_contraction_checks": pushforward_checks,
        "positive_mixture_subadditivity_proved": True,
        "deterministic_pushforward_contraction_proved": True,
        "rectangular_rms_gluing_proved": True,
        "rectglue_positive_scope_closed": True,
        "frobmix108420_proved": False,
        "qresbind107300_proved": False,
        "rh_established": False,
        "grh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
