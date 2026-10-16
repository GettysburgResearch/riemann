# Validation, review limits, and publication status

## Executed

1. Live GitHub search confirmed #949 and #948 as the latest two proposals.
   Their relevant proof notes were read in full, not inferred from titles.
   #948's version report was read but its PDF inspection was not independently
   reproduced: direct Hexagon PDF/TeX requests failed in this pass.
2. The author wrote the two mathematical notes and reconstructed their bounds
   algebraically, keeping coefficient norms distinct from Euler-function norms.
3. `python chks/check.py` and `python -O chks/check.py` were both executed.
   Their entire outputs are byte-identical to RESULTS.json.
4. Three separate mutated Python processes under `-O` were executed. A wrong
   inverse, q^3 in place of q^2, and erased physical zero masks were all rejected
   by RuntimeError predicates. REPLAY.json records their actual failure lines.

## Exact finite coverage

- 450 local Gaussian-rational phase configurations, even m in
  {2,4,6,8,12,16}, q in {5,7,25}, coefficients through degree 2m+8.
- Both local convolution identities, the inverse identity, and every retained
  coefficient's universal majorant checked exactly.
- 28 rational critical-mass cases, using square local norms; these are local
  algebra tests, not a claim that every such q is a retained prime in a field.
- 74 ideal exponent vectors under norm 823543 in the semigroup of exactly
  three Eisenstein prime ideals with norms 7,7,25. The two norm-7 ideals are
  conjugate and remain distinct. This is NOT all native ideals below the cap.
- All 54 nonzero Eisenstein rows of norm <=13, three additional exclusion
  choices, and hard windows D=128,4096,823543. There are 972 forward/inverse
  physical equalities. The hard windows test finite convolution, not an
  infinite Gaussian identity numerically.
- Zero masks checked separately against actual prime-ideal divisibility.
- Seven explicit false-substitution controls, separate from the three process
  mutations. One concerns an unexcluded prime over 2, outside the theorem's
  allowed source; it is not a counterexample to the native source.

The total is 49,777 explicit finite predicates, including repeated setup and
coefficient checks. It is NOT that many independent analytic cases.

The unchanged primitive arithmetic helper is #936 Git blob
64d21a7f400f5bf5654fd67735743ff1befab067. Its bytes were extracted from the
user-visible archive and checked against that exact blob. Its old entire
census was not rerun. The new assemblies share this helper and are not
independent arithmetic implementations or independent mathematical referees.

## Not done / not claimed

No independent agent or human mathematical review; no proof-assistant
formalization or Lean build; no transitive audit of the imported automorphic
source; no full-repository CI. The theorems about infinite products and the
Gaussian interchanges rest on the written proofs, not the finite counts.

No proof of OPEN-R or OPEN-G2, no new native full-moment exponent, no new zeta
zero-free region, and no RH resolution. In particular 3/7 describes the new
correction alone. The native A-to-two-channel-C kernel still has a critical
harmonic mass; the finite critical constant applies to C-to-B.

## Publication

NOT PUSHED. This session's GitHub tool discovery returned read-only actions;
create-tree/create-commit/create-PR actions were not exposed. A plugin search
found the already-installed GitHub integration, not an additional available
write action. There was no `gh` binary; `git ls-remote` failed DNS resolution
for github.com. No GitHub mutation was claimed or performed.

The packet provides an add-only apply-ready patch and apply_to_repo.py. The
local patch fixture is not a cloned full repository. Intended base is #949
at cdb0666fc48d5166f5edd81f394b13e2001a6b5d; other sources are pinned citations,
not silently merged into that base. No inherited source or status is modified.

## Final packaging checks

The add-only installer was executed in a temporary local Git fixture, including
its check-only mode, successful first application, and rejected second
application. An inherited sentinel file was unchanged. The accompanying patch
was checked and applied in a second local fixture; the resulting packet hashes
and ordinary/optimized checker outputs were verified. ZIP payload bytes were
compared with the final local files. These fixtures are NOT the remote source
repository and no remote publication occurred.
