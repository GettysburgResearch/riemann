"""Independent full-subset replay and finite/cofinal single activation controls."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMMIT = "39d689b7485a423a1e0323a755ffc6a68ee084ed"
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "arithmetic_arity_scout.py": "d04e1268813f28d220ceae2cdb4207016963ac91",
    "arithmetic_arity.discovery.json": "7354977b10597b10d5a91d7aec293c9fdad8b889",
    "ARITHMETIC_ARITY_PREREGISTRATION.md": "1b87af511ca0c3acfe77c44b402f65f7020f3f86",
}
OWNED = (
    HERE / "SINGLE_NATIVE_ACTIVATION.md",
    HERE / "SINGLE_ACTIVATION_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_single_activation.py",
)
FIXTURE = HERE / "single_native_activation.json"
MAX_BYTES = 4 * 1048576


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen(name):
    need(name in PINS, "declared source")
    ref = f"{COMMIT}:{PREFIX}{name}"
    size = int(subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT))
    need(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    digest = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    need(len(raw) == size and digest == PINS[name], "frozen discovery source mismatch")
    return raw


def source():
    blobs = {name: frozen(name) for name in PINS}
    namespace = {
        "__name__": "authenticated_arity_scout",
        "__file__": str(HERE / "arithmetic_arity_scout.py"),
    }
    exec(  # noqa: S102 - only authenticated frozen executable bytes
        compile(blobs["arithmetic_arity_scout.py"], namespace["__file__"], "exec"),
        namespace,
    )
    module = SimpleNamespace(**namespace)
    discovered = json.loads(blobs["arithmetic_arity.discovery.json"])
    need(
        canonical(module.build()) == canonical(discovered),
        "complete primitive discovery reconstruction",
    )
    return module, discovered


def complete_matrix(r):
    need(type(r) is int and 2 <= r <= 16, "complete enumeration arity")
    counts = defaultdict(lambda: [0] * r)
    coverage = [0] * (r + 1)
    for mask in range(1 << r):
        indices = [i for i in range(r) if mask & (1 << i)]
        k, location = len(indices), sum(indices)
        coverage[k] += 1
        for i in indices:
            counts[k, location][i] += 1
    need(coverage == [comb(r, k) for k in range(r + 1)], "every source subset counted")
    matrix = [[0] * r for _ in range(r)]
    for k in range(1, r + 1):
        locations = sorted(s for band, s in counts if band == k)
        prefix = [0] * r
        mass = comb(r - 1, k - 1)
        for index, s in enumerate(locations):
            prefix = [a + b for a, b in zip(prefix, counts[k, s], strict=True)]
            if index + 1 == len(locations):
                need(prefix == [mass] * r, "all marked band masses")
                continue
            gap = locations[index + 1] - s
            for i in range(r):
                for j in range(r):
                    matrix[i][j] += gap * (
                        mass * (prefix[i] + prefix[j]) - 2 * prefix[i] * prefix[j]
                    )
    return matrix, coverage


def kkt(matrix, activation, slacks):
    r = len(matrix)
    need(type(activation) is list and len(activation) == r, "activation shape")
    need(
        all(type(x) is str for x in activation + slacks),
        "literal rational source values",
    )
    q, slack = list(map(F, activation)), list(map(F, slacks))
    need(len(slack) == r and sum(q) == 1 and all(x >= 0 for x in q), "source simplex")
    action = [sum((F(matrix[i][j]) * q[j] for j in range(r)), F()) for i in range(r)]
    lam = sum((q[i] * action[i] for i in range(r)), F())
    need(slack == [lam - value for value in action], "literal all-coordinate slack")
    need(
        all(s >= 0 and (not q[i] or s == 0) for i, s in enumerate(slack)),
        "all KKT inequalities",
    )
    return lam


def threshold(r, mu, M=F(1)):
    need(type(r) is int and r in (11, 13, 15), "single-activation arity")
    need(
        type(mu) is int and mu > 0 and type(M) in (int, F) and M > 0,
        "positive exact threshold data",
    )
    M = F(M)
    c = comb(2 * r - 2, r - 1)
    t = F(r * r // 4) + F(r, 2)
    D = 4 * r * c * M + F(144, 234) * c * t * t
    eps = min(F(1, 4) / M, F(1, 3) / t, F(mu, 2) / D)
    perturbation = (8 * r * c * M + F(288, 234) * c * t * t) * eps
    need(
        M * eps <= F(1, 4) and 2 * eps * t <= F(2, 3),
        "exact shape and original-kernel domain",
    )
    need(perturbation <= mu < 2 * mu, "strict full inactive margins")
    return {
        "arity": r,
        "M": str(M),
        "mu": mu,
        "C_r": c,
        "T_bound": str(t),
        "epsilon_0": str(eps),
        "inactive_gradient_perturbation_upper": str(perturbation),
        "source_allocations": 1 << r,
        "nonzero_vertex_allocations": 1 << (r - 1),
        "finite_prime_search_performed": False,
    }


def build():
    module, discovered = source()
    verified, special = [], []
    need(discovered["coverage"] == list(range(2, 17)), "full declared arity coverage")
    for original in discovered["panels"]:
        r = original["arity"]
        matrix, coverage = complete_matrix(r)
        need(matrix == original["matrix"], "independent complete matrix equality")
        replay = module.optimize(matrix)
        need(
            all(canonical(replay[key]) == canonical(original[key]) for key in replay),
            "all declared support and KKT values reproduced",
        )
        value = kkt(
            matrix, original["unique_activation"], original["inactive_slacks_Bq"]
        )
        need(str(value) == original["objective"], "literal objective")
        verified.append(
            {
                "arity": r,
                "full_enumeration_coverage": coverage,
                "every_matrix_entry_equal": True,
                "all_reflection_supports": replay["all_reflection_supports_tested"],
                "activation": original["unique_activation"],
                "slacks_Bq": original["inactive_slacks_Bq"],
                "objective": original["objective"],
                "gain_over_uniform": original["gain_over_uniform"],
                "pre_run_hypothesis_survived": original[
                    "central_two_or_three_hypothesis"
                ],
            }
        )
        if r in (11, 13, 15):
            need(
                original["positive_support_zero_based"] == [r // 2],
                "single original-coordinate support",
            )
            mu = min(
                F(s)
                for i, s in enumerate(original["inactive_slacks_Bq"])
                if i != r // 2
            )
            need(
                mu.denominator == 1
                and mu.numerator == {11: 90, 13: 1858, 15: 22274}[r],
                "exact acquired inactive margin",
            )
            special.append(threshold(r, mu.numerator))
    owned = {
        str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }
    return {
        "schema": "riemann.native_six_hour.single_activation.v1",
        "source_commit": COMMIT,
        "source_blobs": PINS,
        "owned_sha256_lf": owned,
        "full_arity_range": list(range(2, 17)),
        "finite_original_kernel_computation": False,
        "panels": verified,
        "cofinal_proof_thresholds": special,
        "all_arity_classification_claim": False,
    }


def check(candidate):
    need(canonical(candidate) == canonical(build()), "exact typed primitive replay")


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(expected, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    else:
        need(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        need(
            canonical(candidate) == canonical(expected), "exact typed primitive replay"
        )
    print("PASS complete arity atlas and single native activation")


if __name__ == "__main__":
    main()
