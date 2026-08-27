#!/usr/bin/env bash
set -euo pipefail

# Prepared for the frozen pass-three rehearsal tree. This script is intentionally
# serialized and refuses to run against another commit or a nonempty log folder.
WORKTREE="${WORKTREE:-/c/riemann-pass3/combined}"
FORMAL="$WORKTREE/formal"
RAW="${RAW:-/c/Users/gideo/OneDrive/Documents/riemann/audit-local-20260827-pass3/raw/COMBINED}"
AUDIT_PYTHON="${AUDIT_PYTHON:-/c/Users/gideo/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe}"

EXPECTED_HEAD="ae50ef2786b904a9aecdcfb1112d7b323f36ea41"
EXPECTED_TREE="bd621c02db310fc318ee287eefeb6e2c76c8b48a"
BOOTSTRAP="573eb6aa42c3d9469462c91c6b3ddfb8ab36d77f"
A_HEAD="ae0887b8125601c98dc809cffe01c7f1c78bb998"
B_HEAD="6d42bbc31c81e7d6a03909e205b56f30f6f7b49a"
C_HEAD="381a5a98ade7c6bad7122e5182c2fc07332dc747"
LOCK_REL="formal/registry/deltas/C_EXTERNAL_SOURCE_STATEMENTS/EXT.XI.PLATT_TRUDGIAN.2021.txt"
LOCK_ABS="$WORKTREE/$LOCK_REL"
GREEN_C_FORMAL="${GREEN_C_FORMAL:-/c/riemann-pass3/c/formal}"

export PATH="/c/Users/gideo/.elan/bin:$PATH"
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8
export PYTHON="$AUDIT_PYTHON"
export LAKE_JOBS=1

# Retained scripts invoke python3. Export a function so every nested Git Bash
# process uses the pinned bundled Python rather than the WindowsApps shim.
python3() {
  "$AUDIT_PYTHON" "$@"
}
export -f python3
export AUDIT_PYTHON

mkdir -p "$RAW"
if find "$RAW" -mindepth 1 -maxdepth 1 -print -quit | grep -q .; then
  echo "refusing to overwrite nonempty raw-log directory: $RAW" >&2
  exit 2
fi

STATUS="$RAW/COMMAND_EXIT_CODES.tsv"
printf 'sequence\tcommand\texit_code\tstarted_utc\tfinished_utc\tlog\n' > "$STATUS"

finalize() {
  local rc=$?
  {
    printf 'exit_code=%s\n' "$rc"
    printf 'head=%s\n' "$(git -C "$WORKTREE" rev-parse HEAD)"
    printf 'tree=%s\n' "$(git -C "$WORKTREE" rev-parse 'HEAD^{tree}')"
    printf 'status_begin\n'
    git -C "$WORKTREE" status --short
    printf 'status_end\n'
  } > "$RAW/RUN_FINAL_STATE.txt"
  (
    cd "$RAW"
    find . -maxdepth 1 -type f ! -name SHA256SUMS -print0 \
      | sort -z \
      | xargs -0 sha256sum > SHA256SUMS
  )
  return "$rc"
}
trap finalize EXIT

run_step() {
  local sequence="$1"
  shift
  local log="$RAW/${sequence}.log"
  local started finished rc rendered
  started="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf -v rendered '%q ' "$@"
  set +e
  {
    printf 'COMMAND %s\n' "$rendered"
    "$@"
  } 2>&1 | tee "$log"
  rc=${PIPESTATUS[0]}
  set -e
  finished="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$sequence" "$rendered" "$rc" "$started" "$finished" "$(basename "$log")" \
    >> "$STATUS"
  return "$rc"
}

preflight() {
  test "$(git -C "$WORKTREE" rev-parse HEAD)" = "$EXPECTED_HEAD"
  test "$(git -C "$WORKTREE" rev-parse 'HEAD^{tree}')" = "$EXPECTED_TREE"
  test -z "$(git -C "$WORKTREE" status --porcelain=v1)"
  for source in "$BOOTSTRAP" "$A_HEAD" "$B_HEAD" "$C_HEAD"; do
    git -C "$WORKTREE" cat-file -e "${source}^{commit}"
    git -C "$WORKTREE" merge-base --is-ancestor "$source" "$EXPECTED_HEAD"
  done
  git -C "$WORKTREE" show -s \
    --format='commit=%H%nparents=%P%ntree=%T%nsubject=%s' HEAD
  printf 'worktree_lean_toolchain_sha256='
  sha256sum "$FORMAL/lean-toolchain" | awk '{print $1}'
  printf 'worktree_lake_manifest_sha256='
  sha256sum "$FORMAL/lake-manifest.json" | awk '{print $1}'
  printf 'committed_lean_toolchain_blob_sha256='
  git -C "$WORKTREE" show HEAD:formal/lean-toolchain | sha256sum | awk '{print $1}'
  printf 'committed_lake_manifest_blob_sha256='
  git -C "$WORKTREE" show HEAD:formal/lake-manifest.json | sha256sum | awk '{print $1}'
  printf 'PYTHONUTF8=%s\nLAKE_JOBS=%s\nPYTHON=%s\n' \
    "$PYTHONUTF8" "$LAKE_JOBS" "$PYTHON"
  (
    cd "$FORMAL"
    lake --version
    lean --version
  )
}

rematerialize_locked_source_lf() {
  test -f "$LOCK_ABS"
  git -C "$WORKTREE" diff --quiet -- "$LOCK_REL"
  git -C "$WORKTREE" checkout-index --force -- "$LOCK_REL"
  "$AUDIT_PYTHON" - "$LOCK_ABS" <<'PY'
import sys
from pathlib import Path

path = Path(sys.argv[1])
payload = path.read_bytes()
if b"\r" in payload:
    raise SystemExit(f"locked source is not LF-only: {path}")
print(f"LOCKED_SOURCE_LF_ONLY bytes={len(payload)} path={path}")
PY
  git -C "$WORKTREE" diff --quiet -- "$LOCK_REL"
  test "$(git -C "$WORKTREE" hash-object "$LOCK_ABS")" = \
    "$(git -C "$WORKTREE" rev-parse "HEAD:$LOCK_REL")"
}

verify_dependency_sidecars() {
  local rel combined_file green_file
  local -a sidecars=(
    ".lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Analysis/Calculus/ContDiff/FTaylorSeries.olean.private"
    ".lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Analysis/Asymptotics/Lemmas.olean.private"
  )
  for rel in "${sidecars[@]}"; do
    combined_file="$FORMAL/$rel"
    green_file="$GREEN_C_FORMAL/$rel"
    test -s "$combined_file"
    test -s "$green_file"
    cmp -s "$combined_file" "$green_file"
    printf 'SIDECAR_EQUAL bytes=%s sha256=%s path=%s\n' \
      "$(wc -c < "$combined_file")" \
      "$(sha256sum "$combined_file" | awk '{print $1}')" \
      "$rel"
  done
  local brec="/c/Users/gideo/.elan/toolchains/leanprover--lean4---v4.33.0-rc2/lib/lean/Lean/Meta/Constructions/BRecOn.olean.private"
  test -s "$brec"
  printf 'BRecOn_PRESENT bytes=%s sha256=%s path=%s\n' \
    "$(wc -c < "$brec")" \
    "$(sha256sum "$brec" | awk '{print $1}')" \
    "$brec"
}

cd "$WORKTREE"
run_step 00_preflight preflight
run_step 01_rematerialize_c_lock_lf rematerialize_locked_source_lf
run_step 02_axiom_parser_regression "$AUDIT_PYTHON" \
  "$FORMAL/scripts/test_audit_axiom_output.py" -v
run_step 03_dependency_sidecar_equality verify_dependency_sidecars

cd "$FORMAL"
run_step 04_cache_get lake -Kjobs=1 exe cache get
run_step 05_recover_zeta_hypotheses lake -Kjobs=1 build \
  @Zeta23/+Zeta23.Hypotheses
run_step 06_recover_zeta_gamma_facts lake -Kjobs=1 build \
  @Zeta23/+Zeta23.GammaFacts
run_step 07_recover_zeta_defs_counting lake -Kjobs=1 build \
  @Zeta23/+Zeta23.Defs.Counting
run_step 08_recover_zeta_strong_pnt_prefix lake -Kjobs=1 build \
  @Zeta23/+Zeta23.FromPNTPlus.StrongPNTPrefix
run_step 09_lake_build lake -Kjobs=1 build
run_step 10_generate_registry "$AUDIT_PYTHON" scripts/generate_registry.py
run_step 11_validate_registry "$AUDIT_PYTHON" scripts/validate_registry.py
run_step 12_verify_source_locks "$AUDIT_PYTHON" scripts/verify_source_locks.py
run_step 13_validate_blueprint "$AUDIT_PYTHON" scripts/validate_blueprint.py
run_step 14_check_no_sorry bash scripts/check_no_sorry.sh
run_step 15_check_axioms bash scripts/check_axioms.sh
run_step 16_build_comparator_aggregates bash scripts/build_local_comparators.sh
run_step 17_build_a_comparator_smoke lake -Kjobs=1 build \
  RiemannFormal.Analysis.ComparatorSmoke

topics=(
  ArithmeticRows23
  FixedDetectorFiveThree
  MellinAPI
  OperatorPositiveSchurRescue
  RH
  XiPickOrderThreeConditional
  XiPickThreeNode
)
sequence=20
for topic in "${topics[@]}"; do
  run_step "${sequence}_challenge_deps_${topic}" lake -Kjobs=1 build \
    "RiemannComparatorChallengeDeps.${topic}"
  sequence=$((sequence + 1))
  run_step "${sequence}_challenge_${topic}" lake -Kjobs=1 build \
    "RiemannComparatorChallenge.${topic}"
  sequence=$((sequence + 1))
  run_step "${sequence}_solution_${topic}" lake -Kjobs=1 build \
    "RiemannComparatorSolution.${topic}"
  sequence=$((sequence + 1))
done

run_step 50_a_retained_replay bash \
  RiemannFormal/Analysis/replay/run_validation.sh "$WORKTREE"
run_step 51_b_trusted_modules lake -Kjobs=1 build \
  RiemannFormal.Arithmetic.FixedRows \
  RiemannFormal.Arithmetic.SourceIdentities \
  RiemannFormal.Arithmetic.HalfDivisor \
  RiemannFormal.Arithmetic.Wavelet \
  RiemannFormal.MellinLandau.FixedDetectorAssembly

run_step 60_c_verify_declaration_map "$AUDIT_PYTHON" scripts/verify_declaration_map.py
run_step 61_c_check_statement_sources "$AUDIT_PYTHON" scripts/check_statement_sources.py
run_step 62_c_verify_static "$AUDIT_PYTHON" scripts/verify_c_repair_static.py
run_step 63_c_check_external_usage "$AUDIT_PYTHON" scripts/check_external_input_usage.py
run_step 64_c_verify_comparator_fidelity "$AUDIT_PYTHON" \
  scripts/verify_comparator_fidelity.py

sequence=70
while IFS= read -r module; do
  test -n "$module" || continue
  case "$module" in \#*) continue ;; esac
  label="$(basename "$module" .lean)"
  run_step "${sequence}_print_axioms_${label}" lake env lean "$module"
  sequence=$((sequence + 1))
done < scripts/axiom_print_modules.txt

run_step 90_final_registry_validation "$AUDIT_PYTHON" scripts/validate_registry.py
run_step 91_final_source_lock_validation "$AUDIT_PYTHON" scripts/verify_source_locks.py
run_step 92_final_blueprint_validation "$AUDIT_PYTHON" scripts/validate_blueprint.py

echo "PASS_COMBINED_EXACT_HEAD_SUITE head=$EXPECTED_HEAD tree=$EXPECTED_TREE"
