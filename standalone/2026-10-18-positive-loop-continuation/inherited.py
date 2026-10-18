"""Load exact pinned predecessor data; no network or cached theta moments."""
from pathlib import Path
import hashlib, importlib.util, sys
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent/'2026-10-18-theta-degree-eighteen'
EXPECTED={'parameters.json': 'c8810df849f30d71aeef2e5b59ffc3b6434df2d5fab4434306de806143777460', 'interval_source.py': 'aaa8d85c17bee2cbe7fb9bceefbd63f58cd2258fd47c2b989951d97cd8b501ff'}
for name,digest in EXPECTED.items():
    if hashlib.sha256((BASE/name).read_bytes()).hexdigest()!=digest:
        raise ValueError('Inherited source identity mismatch: '+name)
spec=importlib.util.spec_from_file_location('loop_theta_primitives',BASE/'interval_source.py')
source=importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
I=source.I
SCALE=source.SCALE
