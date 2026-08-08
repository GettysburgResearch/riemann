from __future__ import annotations
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(root: Path):
    return subprocess.run([sys.executable, str(root / "verify.py")], cwd=root,
                          text=True, capture_output=True)


def clone():
    td = Path(tempfile.mkdtemp())
    shutil.copytree(ROOT, td / "x")
    return td / "x"


def test_main_passes():
    p = run(ROOT)
    assert p.returncode == 0, p.stderr


def test_order_mutation_rejected():
    x = clone()
    c = json.loads((x / "certificates/synthetic.json").read_text())
    c["orders"] = [1]
    (x / "certificates/synthetic.json").write_text(json.dumps(c))
    p = run(x)
    assert p.returncode != 0


def test_endpoint_mutation_rejected():
    x = clone()
    c = json.loads((x / "certificates/synthetic.json").read_text())
    c["V"] = 0
    (x / "certificates/synthetic.json").write_text(json.dumps(c))
    p = run(x)
    assert p.returncode != 0


def test_ratio_mutation_rejected_or_changes_control():
    x = clone()
    c = json.loads((x / "certificates/synthetic.json").read_text())
    c["ratio_numerator"] = 1
    (x / "certificates/synthetic.json").write_text(json.dumps(c))
    p = run(x)
    if p.returncode == 0:
        data = json.loads((x / "results/synthetic-verification.json").read_text())
        assert data["first_cell_increment"] != 2


def test_fixed_log_mutation_changes_range_but_passes():
    x = clone()
    c = json.loads((x / "certificates/synthetic.json").read_text())
    c["q0"] = 3
    (x / "certificates/synthetic.json").write_text(json.dumps(c))
    p = run(x)
    assert p.returncode == 0, p.stderr


def test_result_has_digest():
    p = run(ROOT)
    assert p.returncode == 0
    data = json.loads((ROOT / "results/synthetic-verification.json").read_text())
    assert len(data["proof_object_sha256"]) == 64


def test_higher_difference_is_distinct():
    p = run(ROOT)
    assert p.returncode == 0
    data = json.loads((ROOT / "results/synthetic-verification.json").read_text())
    assert data["geometric_differences"]["2"] != data["first_cell_increment"]


def test_reconstruction_has_zero_mismatches():
    p = run(ROOT)
    assert p.returncode == 0
    data = json.loads((ROOT / "results/synthetic-verification.json").read_text())
    assert all(v["mobius_mismatches"] == 0 for v in data["reconstruction"].values())
