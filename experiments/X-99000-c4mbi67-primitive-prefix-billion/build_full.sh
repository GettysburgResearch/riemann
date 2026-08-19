#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
N="${1:-1000000000}"
K="${2:-40}"
BIN="${TMPDIR:-/tmp}/scan_cprefix_exact.$$"
trap 'rm -f "$BIN"' EXIT
g++ -O3 -std=c++17 "$HERE/src/scan_cprefix_exact.cpp" -o "$BIN"
exec "$BIN" "$N" "$K"
