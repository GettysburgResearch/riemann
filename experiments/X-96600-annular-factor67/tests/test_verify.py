from pathlib import Path
import json,subprocess,sys,tempfile
r=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as td:
 out=Path(td)/"v.json";subprocess.run([sys.executable,str(r/"verify.py"),str(out)],check=True);d=json.loads(out.read_text())
assert d["verdict"]=="PASS_SOURCE_COMPLETE_ANNULAR_FACTOR67_CANDIDATE"
assert d["rh_established"] is False
