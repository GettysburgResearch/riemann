# Publication instructions — NOT PUSHED

No remote branch, commit or PR was created by this pass. The connected GitHub
reader verified #966 at

    8d94494698ee447711a53dec922986586418e398

It remains a draft. No earlier frozen source or integrated status is changed.
The new sources are intended to be added under

    standalone/2026-10-18-ramified-shifted-detector/

Suggested branch:

    research/ramified-shifted-detector-20261018

From an authenticated clone, create a branch at that exact base, apply the
provided patch using `git apply --check` and then `git apply --index`, run the
manifest/checker/mutation commands in README.md, and inspect `git diff --cached
--stat` before committing. The diff must contain additions only in the new
directory. Push that branch and open a DRAFT PR against
`research/selected-fourth-density-20261017`, not directly against main.
No force push is necessary or recommended.

Suggested title:

    Research: exact ramified continuation and shifted exceptional-character density

Suggested summary:

Proposed complete component proofs, not independently reviewed. The original
Poisson correction admits explicit formulas for all five ramified classes.
They remove the artificial 3x>2 and 3x+y>5/2 restrictions, preserve all masks,
and yield a critical uniform bound and weighted subcritical averages. A
separate off-central fourth moment and shifted zero detector improve the
exceptional-character exponent at sigma=3/4 from 43/60 to 395/552, a gain of
1/920. All full column sums, conductor dyads and prefix/height maxima remain.
Neither component assumes RH, GRH, an unknown native moment or the previous
proposed global zero-free conclusion. No new all-field zero-free fraction is
claimed. The critical signed fixed-twist bound remains open.

The finite exact checker has 1,507 predicates including setup, with direct
complete local residue cases at norms 13,37,25. Normal/optimized reports
match and eight actual corrupted optimized processes fail. These are finite
algebra tests, not analytic certification. Source/code authorship is shared;
no external review or Lean build is claimed. Review the ramified rational
identities, normal Euler convergence, actual-conductor AFE treatment and
shifted zero detector before considering integration.
