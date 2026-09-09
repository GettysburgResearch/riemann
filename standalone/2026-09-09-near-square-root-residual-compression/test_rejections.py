#!/usr/bin/env python3
"""Actual CLI refusal controls; all fixtures are temporary copies."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
NAMES = ["false_RH", "false_upper_bound", "boolean_alias", "float_alias",
         "changed_exponent", "duplicate_JSON", "altered_proof", "extra_file",
         "parent_drift", "removed_prime_powers"]

def seal(root):
    paths = sorted(p for p in root.iterdir() if p.name != "SHA256SUMS")
    (root/"SHA256SUMS").write_text("".join(
        hashlib.sha256(p.read_bytes()).hexdigest()+"  "+p.name+"\n"
        for p in paths if p.is_file()))

def invoke(root, optimized):
    cmd = [sys.executable, "-I", "-S", "-B"]
    if optimized:
        cmd.append("-O")
    cmd += [str(root/"verify.py"), "--check", str(root/"result.json")]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=30)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--optimized", action="store_true")
    ap.add_argument("--part", type=int, choices=(1, 2))
    args = ap.parse_args()
    names = NAMES if args.part is None else NAMES[(args.part-1)*5:args.part*5]
    records = []
    with tempfile.TemporaryDirectory(prefix="riemann-sc-adverse-") as tmp:
        tmp = Path(tmp)
        pristine = tmp/"pristine"
        shutil.copytree(ROOT, pristine)
        good = invoke(pristine, args.optimized)
        if good.returncode:
            raise RuntimeError("pristine copy failed: "+good.stderr)
        for name in names:
            root = tmp/name
            shutil.copytree(ROOT, root)
            obj = json.loads((root/"result.json").read_text())
            if name == "false_RH":
                obj["rh_proved"] = True
            elif name == "false_upper_bound":
                obj["arithmetic_upper_bound_proved"] = True
            elif name == "boolean_alias":
                obj["actual_zeta_norms_computed"] = False
            elif name == "float_alias":
                obj["bounded_panels"] = float(obj["bounded_panels"])
            elif name == "changed_exponent":
                obj["exponents"]["squared_operator_power"] = "-2/5"
            if name in NAMES[:5]:
                (root/"result.json").write_text(json.dumps(obj, indent=2, sort_keys=True)+"\n")
                seal(root)
            elif name == "duplicate_JSON":
                p = root/"result.json"
                p.write_text(p.read_text().replace("{", '{"rh_proved":false,', 1))
                seal(root)
            elif name == "altered_proof":
                with (root/"PROOF.md").open("a") as f:
                    f.write("\nUnsealed altered proof fixture.\n")
            elif name == "extra_file":
                (root/"EXTRA").write_text("not in the exact inventory\n")
                seal(root)
            elif name == "parent_drift":
                p = root/"SOURCES.json"
                source = json.loads(p.read_text())
                source["parent"]["sha"] = "0"*40
                p.write_text(json.dumps(source, indent=2)+"\n")
                seal(root)
            elif name == "removed_prime_powers":
                p = root/"verify.py"
                text = p.read_text()
                before = "if len(fac) != 1:"
                after = "if len(fac) != 1 or next(iter(fac.values())) > 1:"
                if text.count(before) != 1:
                    raise RuntimeError("prime-power mutation target drift")
                p.write_text(text.replace(before, after))
                seal(root)
            bad = invoke(root, args.optimized)
            if bad.returncode == 0:
                raise RuntimeError("accepted altered packet: "+name)
            if "REJECT:" not in bad.stderr:
                raise RuntimeError("not a controlled refusal: "+name+" "+bad.stderr)
            records.append({"case":name, "exit_code":bad.returncode,
                            "diagnostic":bad.stderr.strip()})
    print(json.dumps({"optimized":args.optimized, "part":args.part,
                      "pristine_passed":True, "refusals":records}, indent=2))

if __name__ == "__main__":
    main()
