"""Finite exact controls and strict replay for the fixed quadratic Xi panel."""

import ast
import copy
import hashlib
import importlib.util
import itertools
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/exploratory"
sys.path.insert(0, str(HERE))
PATH = HERE / "xi_quadratic_critical_transport.py"
SPEC = importlib.util.spec_from_file_location("qt", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def unpack(pair):
    return Q(*pair)


def reseal(value):
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return value


class QuadraticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.decode(M.FIXTURE.read_bytes())

    def test_01_full_fresh_reconstruction(self):
        self.assertTrue(M.check_report(self.report))

    def test_02_source_and_runtime_authentication(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 8)
        for binding in M.BINDINGS:
            raw = subprocess.check_output(
                ["git", "show", binding["commit"] + ":" + binding["path"]], cwd=ROOT
            )
            self.assertEqual(
                hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
                binding["sha256_lf"],
            )

    def test_03_exact_quadratic_factorization(self):
        # w=i*v: P/c=-(v-y)(v-(lambda+d))/2.
        for lam, d in ((Q(1), Q(1, 2)), (Q(5), Q(4)), (Q(3), Q(1))):
            q = (lam * lam - d * d) / (2 * lam)
            y = lam - d
            self.assertEqual(y, 2 * lam * q / (lam + d))
            for v in (Q(-1), Q(0), Q(1, 3), Q(2), Q(7)):
                self.assertEqual(
                    -lam * q - v * v / 2 + lam * v, -(v - y) * (v - lam - d) / 2
                )
            self.assertEqual((lam + d) - y, 2 * d)

    def test_04_quadratic_improves_linear_exact_polynomial(self):
        # g(w)=3/8-w^2/2+(1/100)w^3/6; lambda=1.
        # Every one of the five quadratic contours certifies, while the
        # old linear bound already fails from its 2q/lambda term alone.
        lam, q, d, y, c, m3 = Q(1), Q(3, 8), Q(1, 2), Q(1, 2), Q(-1), Q(1, 100)
        for ratio in M.RATIOS:
            r = ratio * y
            self.assertTrue(0 < r < min(y, 2 * d))
            self.assertLess(
                m3 * (y + r) ** 2 * ((y + r) / 6 + lam / 2), abs(c) * r * (d - r / 2)
            )
        delta = 2 * q / lam + m3 / abs(c) * (4 * q * q / (3 * lam) + 2 * q)
        self.assertGreater(delta, Q(1, 2))

    def test_05_large_third_derivative_failure_retained(self):
        for ratio in M.RATIOS:
            y, d, r = Q(1, 2), Q(1, 2), ratio / 2
            self.assertGreater(
                100 * (y + r) ** 2 * ((y + r) / 6 + Q(1, 2)), r * (d - r / 2)
            )

    def test_06_binomial_tail_product_bound(self):
        for j in range(65):
            self.assertLessEqual(
                math.comb(40 + j, 8), math.comb(40, 8) * math.comb(j + 8, 8)
            )

    def test_07_tail_against_independent_exact_formula(self):
        with M.ha.precision(256):
            for h in (Q(1, 16), Q(1, 4), Q(1, 2), Q(3, 4)):
                x = h / M.OUTER
                exact = (
                    Q(math.factorial(8) * math.comb(40, 8))
                    * x**32
                    / (M.OUTER**8 * (1 - x) ** 9)
                )
                bound = M.taylor_tail(Q(1), h)
                self.assertGreaterEqual(bound, exact)
                self.assertLess(bound - exact, (1 + exact) * Q(1, 2**240))

    def test_08_tail_dominates_finite_prefix(self):
        for x in (Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4)):
            prefix = sum((math.comb(n + 8, 8) * x**n for n in range(32, 97)), Q(0))
            self.assertLessEqual(prefix, math.comb(40, 8) * x**32 / (1 - x) ** 9)

    def test_09_frozen_exact_panel(self):
        rows = M.parent_panel()
        records = self.report["records"]
        self.assertEqual(len(rows), len(records))
        for i, (source, record) in enumerate(zip(rows, records)):
            self.assertEqual(record["index"], i)
            self.assertEqual(record["HA_center"], source["center"])
            self.assertEqual(record["HA_radius"], source["radius"])
            raw = json.dumps(source, sort_keys=True, separators=(",", ":")).encode()
            self.assertEqual(
                record["HA_record_sha256"], hashlib.sha256(raw).hexdigest()
            )

    def test_10_critical_certificates_exact_inequality(self):
        for record in self.report["records"]:
            critical = record.get("critical")
            if critical is None:
                continue
            self.assertEqual(unpack(critical["radius"]), Q(1, 2**120))
            for attempt in critical["attempts"]:
                if "left" not in attempt:
                    continue
                a, d, m = [
                    unpack(attempt[k])
                    for k in ("residual", "derivative_lower", "second_upper")
                ]
                eps = Q(1, 2**120)
                self.assertEqual(unpack(attempt["left"]), a + m * eps * eps / 2)
                self.assertEqual(unpack(attempt["right"]), d * eps)
                self.assertEqual(
                    attempt["status"] == "PASS", a + m * eps * eps / 2 < d * eps
                )

    def test_11_all_five_ratios_retained(self):
        expected = [[1, 16], [1, 8], [1, 4], [1, 2], [3, 4]]
        for record in self.report["records"]:
            self.assertEqual([r["ratio"] for r in record["quadratic"]], expected)

    def test_12_precision_schedule_and_stop(self):
        for record in self.report["records"]:
            for item in record["quadratic"] + [record["linear"]]:
                attempts = item["attempts"]
                self.assertEqual(
                    [a["bits"] for a in attempts], list(M.TIERS[: len(attempts)])
                )
                self.assertTrue(all(a["status"] != "PASS" for a in attempts[:-1]))
                if attempts and attempts[-1]["status"] != "PASS":
                    self.assertEqual(len(attempts), 3)

    def test_13_quadratic_strict_guard_fields(self):
        for record in self.report["records"]:
            for item in record["quadratic"]:
                for attempt in item["attempts"]:
                    if "error_upper" in attempt:
                        certified = unpack(attempt["error_upper"]) < unpack(
                            attempt["margin_lower"]
                        )
                        matched = unpack(attempt["parent_displacement_upper"]) < unpack(
                            attempt["radius_lower"]
                        )
                        self.assertEqual(attempt["transport_certified"], certified)
                        self.assertEqual(attempt["parent_matched"], matched)
                        self.assertEqual(
                            attempt["status"] == "PASS", certified and matched
                        )

    def test_14_linear_guard_fields(self):
        for record in self.report["records"]:
            for attempt in record["linear"]["attempts"]:
                if "delta" in attempt and attempt["transport_certified"]:
                    self.assertLess(unpack(attempt["delta"][1]), Q(1, 2))
                if attempt["status"] == "PASS":
                    self.assertTrue(
                        attempt["transport_certified"] and attempt["parent_matched"]
                    )

    def test_15_chosen_third_bound_is_valid_minimum(self):
        for record in self.report["records"]:
            for item in record["quadratic"] + [record["linear"]]:
                for attempt in item["attempts"]:
                    bound = attempt.get("third_derivative")
                    if bound is None or bound["status"] != "PASS":
                        continue
                    choices = [
                        (unpack(bound[k]["upper"]), k)
                        for k in ("direct", "taylor_cauchy")
                        if bound[k]["status"] == "PASS"
                    ]
                    self.assertEqual(
                        min(choices), (unpack(bound["upper"]), bound["chosen_method"])
                    )

    def test_16_no_newton_proof_substitution(self):
        for record in self.report["records"]:
            newton = record["newton"]
            self.assertLessEqual(len(newton["steps"]), 24)
            if newton["status"] == "CONVERGED_SCOUT":
                self.assertEqual((unpack(newton["center"]) * 2**180).denominator, 1)
                correction = newton["steps"][-1]["correction"]
                self.assertLess(max(abs(unpack(x)) for x in correction), Q(1, 2**170))
                self.assertIn("critical", record)

    def test_17_summary_is_full_panel_reduction(self):
        self.assertEqual(M.summary(self.report["records"]), self.report["summary"])

    def test_18_source_and_artifact_payload_seals(self):
        value = copy.deepcopy(self.report)
        seal = value.pop("payload_sha256")
        self.assertEqual(
            hashlib.sha256(
                json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
            seal,
        )
        self.assertEqual(len(value["artifacts"]), 4)
        for path, digest in value["artifacts"].items():
            self.assertEqual(
                hashlib.sha256(
                    (ROOT / path).read_bytes().replace(b"\r\n", b"\n")
                ).hexdigest(),
                digest,
            )

    def test_19_precisions_fail_closed(self):
        for bad in (True, 128, 257, 2048):
            with self.assertRaises(ValueError), M.ha.precision(bad):
                pass

    def test_20_taylor_design_and_radius_caps(self):
        with M.ha.precision(256):
            for args in (
                (1, M.OUTER),
                (1, Q(1, 4), Q(1), 32),
                (1, Q(1, 4), M.OUTER, True),
                (-1, Q(1, 4)),
            ):
                with self.assertRaises(ValueError):
                    M.taylor_tail(*args)

    def test_21_source_domain_is_not_overridden(self):
        with M.ha.precision(256):
            for z in (M.acb(20), M.acb(1100), M.acb(256, -1), M.acb(256, 2)):
                with self.assertRaises(ValueError):
                    M.ha.xi_series(z, 40)

    def test_22_json_types_and_duplicate_keys(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":1.0}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b"[" * 26 + b"0" + b"]" * 26,
        ):
            with self.assertRaises((ValueError, RecursionError)):
                M.decode(raw)

    def test_23_scalar_and_container_caps(self):
        for value in (2**4097, "x" * 4097, [0] * 20001, {"x": 1.5}):
            with self.assertRaises(ValueError):
                M.validate_tree(value)
        with self.assertRaises(ValueError):
            M.decode(b" " * (M.MAX_BYTES + 1))

    def test_24_no_assert_in_acceptance(self):
        self.assertFalse(
            any(
                isinstance(n, ast.Assert) for n in ast.walk(ast.parse(PATH.read_text()))
            )
        )

    def test_25_resealed_semantic_mismatches(self):
        changes = [
            lambda v: v["summary"].update(nodes=25),
            lambda v: v["records"][0]["quadratic"].pop(),
            lambda v: v["contract"].update(primitive="Gaussian surrogate"),
            lambda v: v["records"][0].update(index=True),
        ]
        # Isolate typed canonical mismatch after the actual primitive rebuild
        # has separately been exercised by test01 and the producer replay.
        for change in changes:
            value = copy.deepcopy(self.report)
            change(value)
            with (
                mock.patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.check_report(reseal(value))

    def test_26_literal_source_corruption_rejected(self):
        original = M.oa.read_source
        binding = M.BINDINGS[5]

        def corrupted(row):
            raw = original(row)
            return raw + b"\n" if row == binding else raw

        with (
            mock.patch.object(M.oa, "read_source", side_effect=corrupted),
            self.assertRaises(ValueError),
        ):
            M.authenticate()

    def test_27_local_HA_drift_rejected(self):
        original = Path.read_bytes
        target = ROOT / M.BINDINGS[1]["path"]

        def corrupted(path):
            raw = original(path)
            return raw + b"\n" if path == target else raw

        with (
            mock.patch.object(Path, "read_bytes", corrupted),
            self.assertRaises(ValueError),
        ):
            M.authenticate()

    def test_28_scope_firewalls(self):
        self.assertEqual(self.report["contract"]["arithmetic_class"], "MIXED")
        self.assertIn(
            "no C5/noncommon guarantee", self.report["contract"]["source_quantifiers"]
        )
        self.assertIn("physical capture", self.report["contract"]["exclusions"])

    def test_29_report_type_and_bad_seal(self):
        for bad in ([], None, True, {"payload_sha256": "0" * 64}):
            with self.assertRaises(ValueError):
                M.check_report(bad)

    def test_30_declared_ratio_types(self):
        for bad in (True, Q(1, 3), 1.0):
            with self.assertRaises(ValueError):
                M.quadratic_attempt(None, None, None, bad)

    def test_31_cli_invalid_modes(self):
        for args in ([], ["--check", "--emit"], ["--unknown"]):
            run = subprocess.run(
                [sys.executable, "-B", str(PATH), *args],
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(run.returncode, 0)

    def test_32_source_emit_exact_bytes(self):
        emitted = subprocess.check_output(
            [sys.executable, "-B", str(PATH), "--emit-sources"]
        )
        self.assertEqual(
            emitted.replace(b"\r\n", b"\n"),
            M.MANIFEST.read_bytes().replace(b"\r\n", b"\n"),
        )

    def test_33_complete_outer_cover_geometry(self):
        center = Q(257)
        cells = list(M.outer_cells(center))
        self.assertEqual(len(cells), 256)
        self.assertEqual(
            [(v[0], v[1]) for v in cells],
            [(i, j) for i in range(16) for j in range(16)],
        )
        for i in range(16):
            row = cells[16 * i : 16 * (i + 1)]
            self.assertEqual(row[0][4], -M.OUTER)
            self.assertEqual(row[-1][5], M.OUTER)
            self.assertTrue(all(a[5] == b[4] for a, b in itertools.pairwise(row)))
        self.assertEqual(cells[0][2], center - M.OUTER - M.EPS)
        self.assertEqual(cells[-1][3], center + M.OUTER + M.EPS)
        self.assertTrue(
            all(cells[16 * i][3] == cells[16 * (i + 1)][2] for i in range(15))
        )

    def test_34_outer_cover_complete_outcomes(self):
        for record in self.report["records"]:
            for tier in record["jet_tiers"]:
                if "outer_scalar_bound" not in tier:
                    continue
                outer = tier["outer_scalar_bound"]
                cover = outer["fixed_cover"]
                self.assertEqual(cover["cells_attempted"], 256)
                self.assertEqual(
                    cover["finite_cells"] + len(cover["failed_cells"]), 256
                )
                self.assertEqual(
                    cover["status"] == "PASS", cover["finite_cells"] == 256
                )
                self.assertEqual(len(cover["ordered_cell_stream_sha256"]), 64)
                self.assertIn("direct", outer)

    def test_35_environmental_history_pin_and_tasks(self):
        history = self.report["environmental_attempt_history"]
        self.assertEqual(M.oa.digest(M.canonical(history)), M.BROAD_HISTORY_SHA256)
        self.assertEqual(history["wallcap_seconds"], 30)
        self.assertLessEqual(len(history["entries"]), 546)
        self.assertEqual(
            [e["task_id"] for e in history["entries"]],
            sorted(e["task_id"] for e in history["entries"]),
        )
        for entry in history["entries"]:
            self.assertEqual(entry["task_id"], M.oa.digest(M.canonical(entry["task"])))
            M.native_task(entry["task"])
            M.validate_native_result(entry["outcome"])

    def small_history(self, outcome):
        task = {
            "route": "outer_direct",
            "center": [256, 1],
            "radius": [7, 8],
            "bits": 256,
        }
        return {
            "schema": M.STEM + "-environmental-history-v1",
            "wallcap_seconds": 30,
            "entries": [
                {
                    "task_id": M.oa.digest(M.canonical(task)),
                    "task": task,
                    "outcome": outcome,
                }
            ],
        }

    def test_36_successful_history_requires_fresh_success(self):
        old = {"status": "PASS", "upper": [3, 2]}
        history = self.small_history(old)
        with mock.patch.object(
            M, "BROAD_HISTORY_SHA256", M.oa.digest(M.canonical(history))
        ):
            for fresh in (
                {"status": "PASS", "upper": [2, 1]},
                {"status": "TIMEOUT_UNRESOLVED", "reason": "test"},
            ):
                runner = M.NativeRunner(history)
                with (
                    mock.patch.object(M, "execute_native", return_value=fresh),
                    M.ha.precision(256),
                    self.assertRaises(M.ReplayFailure),
                ):
                    runner.evaluate("outer_direct", Q(256), Q(7, 8))
            runner = M.NativeRunner(history)
            with (
                mock.patch.object(M, "execute_native", return_value=old) as replay,
                M.ha.precision(256),
            ):
                self.assertEqual(runner.evaluate("outer_direct", Q(256), Q(7, 8)), old)
                self.assertEqual(runner.evaluate("outer_direct", Q(256), Q(7, 8)), old)
                self.assertEqual(replay.call_count, 1)
                self.assertEqual(runner.history(), history)

    def test_37_unresolved_history_is_not_a_fresh_failure(self):
        old = {"status": "TIMEOUT_UNRESOLVED", "reason": "historical only"}
        history = self.small_history(old)
        with mock.patch.object(
            M, "BROAD_HISTORY_SHA256", M.oa.digest(M.canonical(history))
        ):
            runner = M.NativeRunner(history)
            with (
                mock.patch.object(
                    M,
                    "execute_native",
                    side_effect=AssertionError("must not silently rewrite history"),
                ),
                M.ha.precision(256),
            ):
                self.assertEqual(runner.evaluate("outer_direct", Q(256), Q(7, 8)), old)
                self.assertEqual(runner.history(), history)
                self.assertNotIn("upper", old)

    def test_38_all_history_tasks_must_be_used(self):
        history = self.small_history({"status": "PASS", "upper": [1, 1]})
        with mock.patch.object(
            M, "BROAD_HISTORY_SHA256", M.oa.digest(M.canonical(history))
        ):
            runner = M.NativeRunner(history)
            with self.assertRaises(ValueError):
                runner.history()
            with M.ha.precision(256), self.assertRaises(M.ReplayFailure):
                runner.evaluate("outer_direct", Q(257), Q(7, 8))

    def test_39_resealed_environmental_mutation_rejected(self):
        history = copy.deepcopy(self.report["environmental_attempt_history"])
        history["entries"][0]["outcome"] = {"status": "PASS", "upper": [0, 1]}
        with self.assertRaises(ValueError):
            M.NativeRunner(history)

    def test_40_native_task_and_outcome_strict_types(self):
        task = self.small_history({"status": "PASS", "upper": [1, 1]})["entries"][0][
            "task"
        ]
        for key, value in (
            ("route", "arbitrary"),
            ("bits", True),
            ("bits", 2048),
            ("center", [20, 1]),
            ("radius", [1, 2]),
        ):
            bad = dict(task)
            bad[key] = value
            with self.assertRaises(ValueError):
                M.native_task(bad)
        for bad in (
            {"status": "FAIL"},
            {"status": "PASS", "upper": [True, 1]},
            {"status": "PASS", "upper": [-1, 1]},
            {"status": "TIMEOUT_UNRESOLVED", "upper": [1, 1]},
        ):
            with self.assertRaises(ValueError):
                M.validate_native_result(bad)

    def test_41_wallcap_is_environmental_and_real_binary(self):
        task = self.small_history({"status": "PASS", "upper": [1, 1]})["entries"][0][
            "task"
        ]
        with mock.patch.object(
            M.subprocess, "run", side_effect=subprocess.TimeoutExpired("test", 30)
        ) as call:
            result = M.execute_native(task)
        self.assertEqual(result["status"], "TIMEOUT_UNRESOLVED")
        self.assertNotIn("upper", result)
        self.assertEqual(call.call_args.args[0][0], sys._base_executable)
        self.assertEqual(call.call_args.kwargs["timeout"], 30)
        self.assertIn("-c", call.call_args.args[0])

    def test_42_success_replay_failure_not_ordinary_math_failure(self):
        self.assertFalse(issubclass(M.ReplayFailure, ValueError))
        self.assertFalse(issubclass(M.ReplayFailure, ZeroDivisionError))
        self.assertFalse(issubclass(M.ReplayFailure, OverflowError))

    def test_43_history_duplicate_and_boolean_cap_rejected(self):
        history = self.small_history({"status": "PASS", "upper": [1, 1]})
        for mutate in (
            lambda h: h["entries"].append(copy.deepcopy(h["entries"][0])),
            lambda h: h.update(wallcap_seconds=True),
        ):
            bad = copy.deepcopy(history)
            mutate(bad)
            with (
                mock.patch.object(
                    M, "BROAD_HISTORY_SHA256", M.oa.digest(M.canonical(bad))
                ),
                self.assertRaises(ValueError),
            ):
                M.NativeRunner(bad)

    def test_44_collection_keeps_nonfinite_attempt_without_bound(self):
        outcome = {"status": "UNRESOLVED_NATIVE", "reason": "nonfinite ball"}
        runner = M.NativeRunner()
        with (
            mock.patch.object(M, "execute_native", return_value=outcome),
            M.ha.precision(256),
        ):
            self.assertEqual(runner.evaluate("outer_direct", Q(256), Q(7, 8)), outcome)
        history = runner.history()
        self.assertEqual(len(history["entries"]), 1)
        self.assertNotIn("upper", history["entries"][0]["outcome"])

    def test_45_postresult_point_obstruction_status(self):
        diagnostic = self.report["postresult_necessary_bound"]
        self.assertEqual([r["index"] for r in diagnostic["records"]], list(range(26)))
        counts = [0] * 5
        for row in diagnostic["records"]:
            self.assertEqual(row["bits"], 1024)
            self.assertEqual(
                [r["ratio"] for r in row["ratios"]],
                [[1, 16], [1, 8], [1, 4], [1, 2], [3, 4]],
            )
            for j, result in enumerate(row["ratios"]):
                if "left_lower" in result:
                    impossible = unpack(result["left_lower"]) >= unpack(
                        result["right_upper"]
                    )
                    self.assertEqual(result["criterion_impossible"], impossible)
                    self.assertEqual(
                        result["status"] == "CRITERION_IMPOSSIBLE", impossible
                    )
                counts[j] += result["criterion_impossible"]
        self.assertEqual(
            [r["count"] for r in diagnostic["impossible_by_ratio"]], counts
        )

    def test_46_independent_rational_point_obstruction_route(self):
        def sqrt_interval(lo, hi):
            scale = 2**256
            low_integer = math.isqrt((lo.numerator * scale**2) // lo.denominator)
            high_integer = math.isqrt((hi.numerator * scale**2) // hi.denominator)
            if Q(high_integer, scale) ** 2 < hi:
                high_integer += 1
            return Q(low_integer, scale), Q(high_integer, scale)

        for source, diagnostic in zip(
            self.report["records"], self.report["postresult_necessary_bound"]["records"]
        ):
            if not any(r["criterion_impossible"] for r in diagnostic["ratios"]):
                continue
            tier = [t for t in source["jet_tiers"] if "q" in t][-1]
            ll, lu = map(unpack, tier["lambda"])
            ql, qu = map(unpack, tier["q"])
            dl, du = sqrt_interval(ll * ll - 2 * lu * qu, lu * lu - 2 * ll * ql)
            yl, yu = 2 * ll * ql / (lu + du), 2 * lu * qu / (ll + dl)
            cu = max(abs(unpack(v)) for v in tier["c"])
            ml = unpack(diagnostic["point_f8_lower"])
            self.assertLessEqual(
                ml,
                unpack(tier["coefficient_modulus_upper_8_to39"][0]) * math.factorial(8),
            )
            for result in diagnostic["ratios"]:
                if not result["criterion_impossible"]:
                    continue
                ratio = unpack(result["ratio"])
                rl, ru = ratio * yl, ratio * yu
                hl = (1 + ratio) * yl
                self.assertTrue(rl > 0 and ru < 2 * dl)
                left_lower = ml * hl * hl * (hl / 6 + ll / 2)
                right_upper = cu * ru * (du - rl / 2)
                self.assertGreaterEqual(left_lower, right_upper)

    def test_47_exact_polynomial_fixture_control(self):
        control = self.report["exact_polynomial_control"]
        self.assertEqual(control["g"], "3/8-w^2/2+w^3/600")
        self.assertEqual(unpack(control["linear_delta"]), Q(243, 320))
        for row in control["quadratic"]:
            r = unpack(row["ratio"]) / 2
            left = Q(1, 100) * (Q(1, 2) + r) ** 2 * ((Q(1, 2) + r) / 6 + Q(1, 2))
            right = r * (Q(1, 2) - r / 2)
            self.assertEqual(unpack(row["left"]), left)
            self.assertEqual(unpack(row["right"]), right)
            self.assertLess(left, right)

    def test_48_certified_real_critical_intervals_are_distinct(self):
        centers = [
            unpack(r["critical"]["center"])
            for r in self.report["records"]
            if r.get("critical", {}).get("simple_real_critical", False)
        ]
        disjoint = all(
            abs(a - b) > Q(1, 2**119) for a, b in itertools.combinations(centers, 2)
        )
        self.assertEqual(
            disjoint, self.report["summary"]["critical_intervals_pairwise_disjoint"]
        )


if __name__ == "__main__":
    unittest.main()
