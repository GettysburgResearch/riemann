from __future__ import annotations
import copy, json, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = json.loads((ROOT / "certificates/synthetic.json").read_text())


def run(cert):
    with tempfile.TemporaryDirectory() as td0:
        td = Path(td0)
        (td / "certificates").mkdir()
        (td / "results").mkdir()
        (td / "certificates/synthetic.json").write_text(json.dumps(cert))
        (td / "verify.py").write_text((ROOT / "verify.py").read_text())
        return subprocess.run([sys.executable, str(td / "verify.py")], cwd=td,
                              text=True, capture_output=True)


def test_central():
    p = subprocess.run([sys.executable, str(ROOT / "verify.py")], cwd=ROOT,
                       text=True, capture_output=True)
    assert p.returncode == 0, p.stderr


def test_wrong_schema():
    c = copy.deepcopy(CERT); c["schema"] = "wrong"
    assert run(c).returncode != 0


def test_empty_counts():
    c = copy.deepcopy(CERT); c["prime_counts"] = []
    assert run(c).returncode != 0


def test_zero_count():
    c = copy.deepcopy(CERT); c["prime_counts"][0] = 0
    assert run(c).returncode != 0


def test_boolean_count():
    c = copy.deepcopy(CERT); c["prime_counts"][0] = True
    assert run(c).returncode != 0


def test_wrong_ratio_step():
    c = copy.deepcopy(CERT); c["ratio_denominator_step"] = 1
    assert run(c).returncode != 0


def test_extra_key():
    c = copy.deepcopy(CERT); c["extra"] = 1
    assert run(c).returncode != 0


def test_digest_retained():
    p = subprocess.run([sys.executable, str(ROOT / "verify.py")], cwd=ROOT,
                       text=True, capture_output=True)
    assert p.returncode == 0
    data = json.loads((ROOT / "results/verification.json").read_text())
    assert data["proof_object_sha256"] == "66ed2e6bd1a9fa99bd6566a5baa88850fc569bf83c97c0c3011bcde37a3def1f"
