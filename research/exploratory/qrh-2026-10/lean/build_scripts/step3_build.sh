#!/bin/bash
. ${LEANBUILD:?set LEANBUILD to your scratch dir}/scripts/env.sh
export LEAN_NUM_THREADS=3
cd $P
echo "START $(date -u +%FT%TZ) LEAN_NUM_THREADS=$LEAN_NUM_THREADS GLIBC_TUNABLES=$GLIBC_TUNABLES"
time nice -n 19 lake build OAI.NumberTheory.DirichletL.Nonvanishing
echo "EXIT $? $(date -u +%FT%TZ)"
