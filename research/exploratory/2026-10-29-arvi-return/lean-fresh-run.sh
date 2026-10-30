#!/usr/bin/env bash
set -euo pipefail
project=/workspace/scratch/qproject
packet=/workspace/riemann/research/exploratory/2026-10-29-arvi-return
leanbin=/workspace/scratch/lean-4.34.1-linux/bin
export PATH="$leanbin:$PATH"
export LEAN_PATH="$project/.lake/build/lib/lean"
for dir in "$project"/.lake/packages/*/.lake/build/lib/lean; do
  if [[ -d "$dir" ]]; then LEAN_PATH="$LEAN_PATH:$dir"; fi
done
export LEAN_PATH
cd "$project/src"
printf 'LEAN_PATH=%s\n' "$LEAN_PATH" > "$packet/lean-fresh-environment.log"
sha256sum "$leanbin/lean" "$leanbin/leanchecker" "$project/.lake/build/lib/lean/Candidate/Main.olean" "$project/src/Candidate/Main.lean" "$project/lean-toolchain" "$project/lake-manifest.json" "$packet/ZetaCorollary.lean" >> "$packet/lean-fresh-environment.log"
printf '%s\n' 'lean --stdin < ZetaCorollary.lean' > "$packet/lean-zeta-corollary.log"
set +e
lean --stdin < "$packet/ZetaCorollary.lean" >> "$packet/lean-zeta-corollary.log" 2>&1
zeta_status=$?
printf 'exit=%d\n' "$zeta_status" >> "$packet/lean-zeta-corollary.log"
if (( zeta_status != 0 )); then exit "$zeta_status"; fi
printf '%s\n' 'python resource wrapper: timeout 3600 leanchecker --fresh --verbose Candidate.Main' > "$packet/leanchecker-fresh.log"
cat /sys/fs/cgroup/memory.events >> "$packet/leanchecker-fresh.log"
PYTHONDONTWRITEBYTECODE=1 python /workspace/scratch/qproject/run_fresh_checker.py >> "$packet/leanchecker-fresh.log" 2>&1
checker_status=$?
printf 'exit=%d\n' "$checker_status" >> "$packet/leanchecker-fresh.log"
cat /sys/fs/cgroup/memory.events >> "$packet/leanchecker-fresh.log"
exit "$checker_status"
