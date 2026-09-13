#!/usr/bin/env python3
"""Actual CLI refusals and independent exact tests; no native zero replay."""
from __future__ import annotations
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("njt_check", ROOT / "check.py")
if spec is None or spec.loader is None:
    raise RuntimeError("unable to load checker")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def command(folder: Path) -> subprocess.CompletedProcess[str]:
    args = [sys.executable, "-I", "-S", "-B"]
    if sys.flags.optimize:
        args.append("-O")
    args += [str(folder / "check.py"), "--check", str(folder / "result.json")]
    return subprocess.run(args, capture_output=True, text=True, timeout=90, cwd=folder)


def reseal(folder: Path) -> None:
    members = sorted(p for p in folder.iterdir() if p.name != "HASHES.json")
    hashes = {p.name: sha256(p.read_bytes()).hexdigest() for p in members if p.is_file()}
    (folder / "HASHES.json").write_text(json.dumps({"algorithm": "sha256", "files": hashes},
                                                    indent=2, sort_keys=True) + "\n", encoding="utf-8")


class TestNJT(unittest.TestCase):
    def test_01_pristine_actual_cli(self) -> None:
        r = command(ROOT)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("PASS", r.stdout)

    def test_02_independent_subsets(self) -> None:
        for factors in ((Q(1, 3), Q(2, 5), Q(3, 7)),
                        (Q(0), Q(1, 4), Q(1, 4), Q(1, 4)),
                        tuple(Q(1, n) for n in range(2, 9))):
            self.assertEqual(mod.polynomial(factors), mod.subset_coefficients(factors))

    def test_03_equalities_and_perturbations(self) -> None:
        # Additional cutoffs, beyond the receipt's seven designated values.
        for Y in (4, 6, 8):
            for u in (Q(1, 3), Q(1, 2)):
                mod.arithmetic_instance(Y, u, False)
                mod.arithmetic_instance(Y, u, True)

    def test_04_typed_parser(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            for text in ('{"a":1,"a":2}', '{"a":1.0}', '{"a":NaN}'):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    mod.read_json(path)
        self.assertNotEqual(mod.canonical({"value": 1}), mod.canonical({"value": True}))

    def test_05_resealed_actual_cli_refusals(self) -> None:
        cases = ("false_rh", "false_native_feasibility", "bool_count", "changed_degree",
                 "duplicate_key", "broken_energy_code", "broken_budget_code", "extra_file",
                 "unresealed_source_drift")
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                folder = Path(tmp) / "packet"
                shutil.copytree(ROOT, folder)
                target = folder / "result.json"
                result = json.loads(target.read_text(encoding="utf-8"))
                if case == "false_rh":
                    result["rh_proved"] = True
                elif case == "false_native_feasibility":
                    result["unbounded_native_feasibility_proved"] = True
                elif case == "bool_count":
                    result["version"] = True
                elif case == "changed_degree":
                    result["budgets"]["fixed_F5_forbidden_raw_degree"] = 1024
                if case in ("false_rh", "false_native_feasibility", "bool_count", "changed_degree"):
                    target.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                elif case == "duplicate_key":
                    old = target.read_text(encoding="utf-8")
                    target.write_text('{"rh_proved":false,' + old[1:], encoding="utf-8")
                elif case == "broken_energy_code":
                    path = folder / "check.py"
                    text = path.read_text(encoding="utf-8")
                    old = "full_energy += cumulative * cumulative / (B + 2)"
                    self.assertEqual(text.count(old), 1)
                    text = text.replace(old, "full_energy += cumulative * cumulative / (B + 2) + 1")
                    path.write_text(text, encoding="utf-8")
                elif case == "broken_budget_code":
                    path = folder / "check.py"
                    text = path.read_text(encoding="utf-8")
                    old = "m = (j + 1) * (10 + R * (j + 3))"
                    self.assertEqual(text.count(old), 1)
                    text = text.replace(old, "m = (j + 1) * (10 + R * (j + 2))")
                    path.write_text(text, encoding="utf-8")
                elif case == "extra_file":
                    (folder / "unexpected.txt").write_text("unexpected inventory", encoding="utf-8")
                elif case == "unresealed_source_drift":
                    path = folder / "ARITHMETIC.md"
                    path.write_text(path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
                if case not in ("extra_file", "unresealed_source_drift"):
                    reseal(folder)
                r = command(folder)
                self.assertNotEqual(r.returncode, 0, case + " accepted\n" + r.stdout + r.stderr)
                self.assertIn("REFUSED", r.stderr)
                if case == "broken_energy_code":
                    self.assertIn("full physical/reciprocal energy mismatch", r.stderr)
                if case == "broken_budget_code":
                    self.assertIn("integer half-budget identity", r.stderr)
                print("REFUSAL_EXECUTED", case, flush=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
