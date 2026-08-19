#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/verify.py"
if [[ "${FULL:-0}" != "1" ]]; then exit 0; fi
BUILD="${BUILD_DIR:-/tmp/t99100-replay}"
rm -rf "$BUILD"; mkdir -p "$BUILD/segments"
c++ -O3 -std=c++20 -march=native "$HERE/src/scan_h67_segment.cpp" -o "$BUILD/scan"
for k in $(seq 1 20); do
  L=$(( (k-1)*100000000 + 1 )); R=$(( k*100000000 ))
  "$BUILD/scan" "$L" "$R" > "$BUILD/segments/seg${k}.txt"
done
python3 "$HERE/combine.py" --segments-dir "$BUILD/segments" --count 20 --nmax 2000000000 --output-json "$BUILD/result.json" --output-text "$BUILD/result.txt"
cmp "$BUILD/result.json" "$HERE/results/harnack67_exact_2e9.json"
cmp "$BUILD/result.txt" "$HERE/results/harnack67_exact_2e9.txt"
{
  for k in $(seq 1 20); do
    printf '===== segment %02d =====\n' "$k"
    cat "$BUILD/segments/seg${k}.txt"
    if [[ "$k" -lt 20 ]]; then printf '\n'; fi
  done
} > "$BUILD/segments.txt"
cmp "$BUILD/segments.txt" "$HERE/results/harnack67_segments_2e9.txt"
echo PASS_T99100_HARNACK67_FULL_REPLAY
