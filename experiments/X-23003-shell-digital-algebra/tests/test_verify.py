from __future__ import annotations
import copy, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = json.loads((ROOT / "certificates/synthetic.json").read_text())


def run(cert):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        (td / "certificates").mkdir()
        (td / "results").mkdir()
        (td / "certificates/synthetic.json").write_text(json.dumps(cert))
        (td / "verify.py").write_text((ROOT / "verify.py").read_text().replace(
            'ROOT = Path(__file__).resolve().parent',
            'ROOT = Path(__file__).resolve().parent'))
        return subprocess.run([sys.executable, str(td / "verify.py")], cwd=td,
                              text=True, capture_output=True)


def test_central():
    p = subprocess.run([sys.executable, str(ROOT / "verify.py")], cwd=ROOT,
                       text=True, capture_output=True)
    assert p.returncode == 0, p.stderr


def test_wrong_schema():
    c = copy.deepcopy(CERT); c["schema"] = "wrong"
    assert run(c).returncode != 0


def test_bad_endpoint():
    c = copy.deepcopy(CERT); c["N"] = 2
    assert run(c).returncode != 0


def test_bad_source_ratio():
    c = copy.deepcopy(CERT); c["ratio_source"]["numerator"] = 2
    assert run(c).returncode != 0


def test_bad_target_ratio():
    c = copy.deepcopy(CERT); c["ratio_target"]["denominator"] = 1
    assert run(c).returncode != 0


def test_bad_point():
    c = copy.deepcopy(CERT); c["ratio_test_points"][0] = 0
    assert run(c).returncode != 0


def test_extra_key():
    c = copy.deepcopy(CERT); c["extra"] = 1
    assert run(c).returncode != 0


def test_digest_retained():
    p = subprocess.run([sys.executable, str(ROOT / "verify.py")], cwd=ROOT,
                       text=True, capture_output=True)
    assert p.returncode == 0
    data = json.loads((ROOT / "results/verification.json").read_text())
    assert data["proof_object_sha256"] == "1fedcc71674943b736fc0b80a51be664372f58f58576bafceb5cf2c287a2df9c"
