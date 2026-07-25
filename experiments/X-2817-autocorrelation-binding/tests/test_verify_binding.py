import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x2817_binding", ROOT / "verify_binding.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = VERIFY
SPEC.loader.exec_module(VERIFY)


class BindingTests(unittest.TestCase):
    def make_files(self, root: Path):
        vector = {
            "dyadic_vector": {
                "scale_bits": 3,
                "real_numerators": [3, -2, 1],
                "imag_numerators": [1, 4, -1],
            }
        }
        vpath = root / "vector.json"
        vpath.write_text(json.dumps(vector), encoding="utf-8")
        _data, real, imag, bits, vector_sha = VERIFY.load_vector(vpath)
        values = VERIFY.exact_autocorrelations(real, imag)
        lines = [
            VERIFY.MAGIC,
            "cells 3",
            f"vector_scale_bits {bits}",
            f"autocorr_scale_bits {2 * bits}",
            f"vector_sha256 {vector_sha}",
            f"normalization_sha256 {VERIFY.EXPECTED_NORMALIZATION}",
            "parameter_sha256 synthetic-parameter",
            "cutoff_power10 3",
            "cutoff 1000",
            "carrier_num 5",
            "carrier_den 2",
            "segment_size 10",
            "total_segments 100",
            "a_count 4",
        ]
        lines.extend(
            f"a {lag} {real_num} {imag_num}"
            for lag, (real_num, imag_num) in enumerate(values)
        )
        mpath = root / "manifest.txt"
        mpath.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return vpath, mpath

    def test_exact_binding(self):
        with tempfile.TemporaryDirectory() as tmp:
            vector, manifest = self.make_files(Path(tmp))
            result = VERIFY.verify(vector, manifest)
            self.assertEqual(
                result["status"],
                "EXACT_AUTOCORRELATION_BINDING_VERIFIED",
            )
            self.assertEqual(result["coefficient_count"], 4)

    def test_coefficient_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            vector, manifest = self.make_files(Path(tmp))
            text = manifest.read_text(encoding="utf-8")
            text = text.replace("a 1 ", "a 1 999 ", 1)
            manifest.write_text(text, encoding="utf-8")
            with self.assertRaises(VERIFY.BindingError):
                VERIFY.verify(vector, manifest)

    def test_vector_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            vector, manifest = self.make_files(Path(tmp))
            data = json.loads(vector.read_text(encoding="utf-8"))
            data["dyadic_vector"]["real_numerators"][0] += 1
            vector.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(VERIFY.BindingError, "digest"):
                VERIFY.verify(vector, manifest)

    def test_terminal_lag_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            vector, manifest = self.make_files(Path(tmp))
            text = manifest.read_text(encoding="utf-8").replace("a 3 0 0", "a 3 1 0")
            manifest.write_text(text, encoding="utf-8")
            with self.assertRaises(VERIFY.BindingError):
                VERIFY.verify(vector, manifest)

    def test_raw_sha_binding(self):
        with tempfile.TemporaryDirectory() as tmp:
            vector, manifest = self.make_files(Path(tmp))
            result = VERIFY.verify(vector, manifest)
            VERIFY.verify(vector, manifest, result["manifest_sha256"])
            with self.assertRaisesRegex(VERIFY.BindingError, "raw manifest"):
                VERIFY.verify(vector, manifest, "0" * 64)


if __name__ == "__main__":
    unittest.main()
