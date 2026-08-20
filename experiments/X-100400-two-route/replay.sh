#!/usr/bin/env bash
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$HERE/../.." && pwd)
python3 "$HERE/verify.py" --output "$HERE/results/verification.json"
python3 -m unittest discover -s "$HERE/tests" -v
(cd "$ROOT" && sha256sum -c T100400_CONTENT_SHA256SUMS)
