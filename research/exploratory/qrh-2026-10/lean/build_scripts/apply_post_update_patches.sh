#!/bin/bash
# Replicates the lakefile `post_update` hook (which only runs under `lake update`):
# for each listed dependency, verify HEAD == manifest rev, then git apply the shipped
# patches/<label>-lean4341.patch (or confirm it is already applied).
. ${LEANBUILD:?set LEANBUILD to your scratch dir}/scripts/env.sh
set -u
cd $P
fail=0
for label in fixed-point-theorems PrimeNumberTheoremAnd Zeta3Irrational rellich-kondrachov carleson StrongPNT AbsorptionCutoff AINTLIB ClassFieldTheory schoenflies-lean SphereEversion gromov; do
  d=.lake/packages/$label
  want=$(python3 -I -c "import json,sys; m=json.load(open(sys.argv[1])); print([p['rev'] for p in m['packages'] if p['name'].strip('«»')==sys.argv[2]][0])" lake-manifest.json "$label")
  head=$(git -C $d rev-parse HEAD)
  if [ "$head" != "$want" ]; then echo "FAIL $label HEAD $head != $want"; fail=1; continue; fi
  patch=$P/patches/$label-lean4341.patch
  if git -C $d apply --check --reverse $patch 2>/dev/null; then echo "OK $label already applied ($head)"; continue; fi
  if git -C $d apply --check $patch; then
    git -C $d apply $patch && git -C $d apply --check --reverse $patch && echo "OK $label applied $(sha256sum < $patch | cut -c1-16) at $head" || { echo "FAIL $label apply"; fail=1; }
  else echo "FAIL $label patch conflicts"; fail=1; fi
done
exit $fail
