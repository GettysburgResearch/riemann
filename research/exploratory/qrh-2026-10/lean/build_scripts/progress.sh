#!/bin/bash
# prints one progress line; appends to logs/progress.tsv
S=${LEANBUILD:?set LEANBUILD to your scratch dir}
P=$S/src/standalone/2026-10-07-openai-quasi-riemann-import/upstream/lean
oai=$(find $P/.lake/build/lib/lean/OAI -name '*.olean' 2>/dev/null | wc -l)
pnt=$(find $P/.lake/packages/PrimeNumberTheoremAnd/.lake/build -name '*.olean' 2>/dev/null | wc -l)
rk=$(find $P/.lake/packages/rellich-kondrachov/.lake/build -name '*.olean' 2>/dev/null | wc -l)
err=$(grep -cE '^✖|^error' $S/logs/step3_build.log)
line="$(date -u +%T)	oai=$oai/2924	pnt=$pnt	rk=$rk	errors=$err	load=$(cut -d' ' -f1 /proc/loadavg)	avail=$(free -g | awk '/Mem/{print $7}')G	disk_free=$(df -h / | awk 'NR==2{print $4}')"
echo "$line" >> $S/logs/progress.tsv
echo "$line"
