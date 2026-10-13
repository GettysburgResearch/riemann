#!/bin/bash
# wait for the low-floor run to finish, then refine raised floors with manuscript counts (sequential, single-threaded)
while pgrep -f "full_model_floor.py zero paper 1/500" >/dev/null; do sleep 5; done
cd "$(dirname "$0")"
cp ../results/full_zero_paper.json ../results/full_zero_paper_lowfloor.json 2>/dev/null
timeout 840 python3 full_model_floor.py zero paper 1/5 1/5 1/4 1/4 1/3 1/3 > ../results/full_zero_paper_raised2.log 2>&1
cp ../results/full_zero_paper.json ../results/full_zero_paper_raised2.json 2>/dev/null
