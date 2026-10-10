#!/bin/bash
. ${LEANBUILD:?set LEANBUILD to your scratch dir}/scripts/env.sh
cd $P
echo "START $(date -u +%FT%TZ)"
time nice -n 19 lake exe cache get
echo "EXIT $? $(date -u +%FT%TZ)"
