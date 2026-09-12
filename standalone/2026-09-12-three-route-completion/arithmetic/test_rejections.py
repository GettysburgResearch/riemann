"""Replay pristine and report-corruption cases through the actual checker CLI."""

import copy
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory


def run() -> None:
    base = Path(__file__).resolve().parent
    original = json.loads((base / "results.json").read_text(encoding="utf-8"))
    mutations = {}
    changed = copy.deepcopy(original)
    changed["trace_panels"][0]["S_N"]["upper"] = "0"
    mutations["wrong_trace_endpoint"] = json.dumps(changed)
    changed = copy.deepcopy(original)
    changed["coverage"]["complete_output_column_norms"] = True
    mutations["boolean_coverage_alias"] = json.dumps(changed)
    changed = copy.deepcopy(original)
    del changed["limitations"]
    mutations["missing_limitations"] = json.dumps(changed)
    raw = json.dumps(original)
    mutations["duplicate_status"] = raw[:-1] + ',"status":' + json.dumps(original["status"]) + "}"
    count = 0
    with TemporaryDirectory(prefix="arithmetic-report-rejection-") as folder:
        for optimized in (False, True):
            command = [sys.executable, "-S"] + (["-O"] if optimized else []) + [
                "-B", str(base / "check.py"), "--check"]
            good = subprocess.run(command + [str(base / "results.json")],
                                  capture_output=True, text=True, check=False)
            if good.returncode != 0:
                raise ValueError("pristine report rejected: " + good.stderr)
            for name, text in mutations.items():
                path = Path(folder) / (name + ".json")
                path.write_text(text, encoding="utf-8")
                bad = subprocess.run(command + [str(path)], capture_output=True,
                                     text=True, check=False)
                if bad.returncode == 0:
                    raise ValueError("corrupted report accepted: " + name)
                count += 1
    print(json.dumps({"accepted": True, "pristine_modes": 2,
                      "corrupted_reports_rejected": count}))


if __name__ == "__main__":
    run()
