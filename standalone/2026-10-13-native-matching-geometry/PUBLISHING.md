# Publishing handoff -- NOT PUSHED

Exact intended base: `377f548cab8759399aca80ed3188c495667d562a` (PR #942).
Base branch: `research/native-principal-census-20261013`.
Suggested NEW branch: `research/native-matching-geometry-20261013`.
No such branch or PR was created in this session. Do not invent a PR number.

The supplied `riemann_matching_geometry.patch` adds only this standalone
packet. It does not modify any prior proof, main, workflows, or accepted status.

In a publishing-capable checkout, inspect the patch first, then use:

```sh
git fetch origin research/native-principal-census-20261013
git switch -c research/native-matching-geometry-20261013 \
  377f548cab8759399aca80ed3188c495667d562a
git apply --check /path/to/riemann_matching_geometry.patch
git apply /path/to/riemann_matching_geometry.patch
cd standalone/2026-10-13-native-matching-geometry
python -I -S -B verify.py > replay.json
cmp replay.json results.json
python -I -S -B -O verify.py > replay.optimized.json
cmp replay.optimized.json results.json
python -I -S -B calibrate.py > replay.calibration.json
cmp replay.calibration.json calibration.json
rm replay.json replay.optimized.json replay.calibration.json
cd ../..
git add standalone/2026-10-13-native-matching-geometry
git commit -m "research: matching geometry and uniform principal calibration"
git push -u origin research/native-matching-geometry-20261013
```

Open a draft PR against the base branch, using PR_BODY.md. Record the actual
commit and read back the diff before describing the work as published. Keep
the proposed/unreviewed status and the open singleton covariance explicit.
