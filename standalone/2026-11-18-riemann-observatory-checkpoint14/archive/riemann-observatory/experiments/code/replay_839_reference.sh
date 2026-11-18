#!/usr/bin/env bash
# Offline replay of the author's unmodified first-window C++ verifier (~7min here).
# This is not a Lean-kernel replay. See the independent table checker and audit.
set -euo pipefail
observatory_root=$(cd -- "$(dirname -- "$0")/../.." && pwd)
reference_dir="$observatory_root/experiments/code/vendor/839_reference"
input_dir="$observatory_root/experiments/inputs/839_first_window"
run_dir=$(mktemp -d)
trap 'rm -rf -- "$run_dir"' EXIT
g++ -std=c++23 -O3 -DNDEBUG -D_GLIBCXX_ASSERTIONS -DVERIFY_POINT_COUNT=7 \
  "$reference_dir/verify.cpp" -o "$run_dir/verify7"
python "$reference_dir/make_parameters.py" "$input_dir/inputs.json" "$run_dir/parameters.txt"
"$run_dir/verify7" "$run_dir/parameters.txt" "$input_dir/kernel_lower.bin"
