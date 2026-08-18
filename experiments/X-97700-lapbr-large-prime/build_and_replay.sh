#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify.py --output results/verification.json
python3 - <<'PY'
import ast
from pathlib import Path
ast.parse(Path('verify.py').read_text())
PY
sha256sum -c SHA256SUMS
printf '%s\n' PASS_T97700_FULL_REPLAY
