#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
"$ROOT/experiments/X-96500-parity-covariant-gluing/build_and_replay.sh"
"$(dirname "$0")/build.sh"
