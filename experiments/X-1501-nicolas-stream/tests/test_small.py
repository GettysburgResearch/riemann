from __future__ import annotations

import json
import math
import subprocess
import tempfile
import unittest
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
BINARY = ROOT / "scan-test-bin"


def primes_up_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b"\x00" * (((n - p*p)//p)+1)
    return [p for p in range(2, n + 1) if sieve[p]]


def read_state(path: Path) -> dict[str, str]:
    return dict(line.strip().split("=", 1) for line in path.read_text().splitlines() if "=" in line)


class NicolasSmallTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([
            "g++", "-O3", "-std=c++17", "-Wall", "-Wextra",
            str(ROOT / "scan.cpp"), "-o", str(BINARY)
        ], check=True)

    @classmethod
    def tearDownClass(cls):
        BINARY.unlink(missing_ok=True)

    def run_scan(self, limit: int, state: Path, result: Path):
        subprocess.run([str(BINARY), str(limit), str(state), str(result), "65536"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return json.loads(result.read_text())

    def test_one_shot_matches_restart(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            one_state, one_result = td / "one.state", td / "one.json"
            split_state = td / "split.state"
            self.run_scan(1_000_000, one_state, one_result)
            self.run_scan(500_000, split_state, td / "half.json")
            self.run_scan(1_000_000, split_state, td / "split.json")
            a, b = read_state(one_state), read_state(split_state)
            for key in ("processed_limit", "last_prime", "k", "minimum_k", "upward_steps", "violations"):
                self.assertEqual(a[key], b[key])
            for key in ("theta", "log_product", "previous_defect", "minimum_defect"):
                self.assertLess(abs(mp.mpf(a[key]) - mp.mpf(b[key])), mp.mpf("1e-28"))

    def test_independent_high_precision_control(self):
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            result = self.run_scan(1_000_000, td / "state", td / "result.json")
            ps = primes_up_to(1_000_000)
            self.assertEqual(len(ps), 78498)
            self.assertEqual(result["k"], 78498)
            self.assertEqual(result["last_prime"], 999983)
            with mp.workdps(80):
                theta = mp.fsum(mp.log(p) for p in ps)
                log_product = mp.fsum(-mp.log1p(-mp.mpf(1)/p) for p in ps)
                defect = log_product - mp.euler - mp.log(mp.log(theta))
                self.assertLess(abs(theta - mp.mpf(str(result["theta"]))), mp.mpf("2e-9"))
                self.assertLess(abs(log_product - mp.mpf(str(result["log_product"]))), mp.mpf("3e-16"))
                self.assertLess(abs(defect - mp.mpf(str(result["log_defect"]))), mp.mpf("5e-17"))
            self.assertEqual(result["floating_violations"], 0)
            self.assertEqual(result["upward_steps_after_k2"], 0)


if __name__ == "__main__":
    unittest.main()
