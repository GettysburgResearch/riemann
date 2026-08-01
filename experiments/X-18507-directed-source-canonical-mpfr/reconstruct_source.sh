#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cat "$here"/source/directed_ladder.c.part00 \
    "$here"/source/directed_ladder.c.part01 \
    "$here"/source/directed_ladder.c.part02 \
    "$here"/source/directed_ladder.c.part03 \
    > "$here"/directed_ladder.c
actual="$(sha256sum "$here"/directed_ladder.c | cut -d' ' -f1)"
expected="c2e0ff82d7fef848e600efedeb26a889c4c8e1ba95d4184b8c34bf3b104c58df"
test "$actual" = "$expected"
printf 'reconstructed directed_ladder.c sha256=%s\n' "$actual"
