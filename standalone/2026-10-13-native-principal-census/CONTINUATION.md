# Publication continuation and exact nonprincipal pruning

Status: PROPOSED component proofs plus an exact finite census. Neither the full
native moment hierarchy nor RH has been proved. No independent mathematical
review has been performed.

## Read first

[BANDLIMITED_PRUNING.md](BANDLIMITED_PRUNING.md) is the additional attack on the
nonprincipal sum. A fixed positive Schwartz row majorant, with Fourier support
in a radius-1/8 disk, gives EXACT orthogonality for each nonprincipal tuple whose
TOTAL prime-ideal radical has norm at most H. The actual nonunit masks and every
row in the Schwartz tail remain. The hard-ball native moment is bounded above
by this weighted moment. Its surviving nonprincipal term has radical norm >H.

This is an exact specialization of classical band-limited Poisson quadrature,
not a claim to have invented orthogonality or proved the surviving term small.
The same note proves why shrinking the support to cover a growing radical
range T incurs physical row mass at least c T-1. Thus one cannot eliminate all
long conductors for free while continuing to normalize the row count by H.

[PROOF.md](PROOF.md) estimates the COMPLETE principal part at every fixed order:
P_Phi(H)=c_Phi H B+O(X^(k+epsilon)), uniformly for H>=1, with a separate
O(sqrt(H)X^(k+epsilon)) error for sharp norm balls. It includes nonsquarefree
Liouville columns and all sixth-power aliases. The complete independent-density
principal reference is unchanged by primewise sixth-root phase rotations.
Consequently it cannot distinguish Mobius cancellation from the unsigned source.

[README.md](README.md) and [results.json](results.json) give all 15 complete
native hard-window census cases, including both signs of the remaining term.
The fixed positive band-limited weight was NOT used in that census. The finite
percentages in README must not be described as observations of the new exact
annihilation theorem or as an asymptotic saving.

## Interruption, byte correction and fresh replays

The first upload created unreferenced commit
`0cd017aa6397eed987d654005941acf829094c03`, with parent #939 at
`751eff5d759f82ae8316f141613f2214c97b7553`. Before a branch or PR was announced,
read-back caught a mismatch: census.py had ONE additional blank line immediately
before principal_fourth. Its remote blob is
`2a074ccede483324392a729056ccbf43a1f26eac`, 11417 bytes. The initial local source
had blob `0724ea2c5a52a0f0ee2c27814921707c7c2aad10`, 11416 bytes.

The source was reconciled to the uploaded whitespace, the Python ASTs were
compared with source locations excluded and were exactly equal, and the
manifest was regenerated. No result, executable expression or mathematical
statement changed. This is a corrected manifest, not a silent claim that the
initial hashes matched.

After the interruption, the exact verifier was freshly run in both normal and
optimized modes and again reproduced the 3663-predicate report byte for byte.
The largest census case D=8192,H=12855 was also freshly recomputed under
optimized Python: ALL fields agreed with its recorded case. Observed runtime
was 20.37 seconds, maximum RSS 342472 KiB in this one environment; it is not a
cross-platform performance claim. The preceding session's 15-case second-mode
replays remain archived in the working environment and described in VALIDATION;
they were not all repeated yet again after the whitespace-only reconciliation.

The new verify_bandlimited.py passes 14865 explicit finite predicates, including
setup/polynomial-division checks. Normal and optimized reports agree exactly.
Its five moduli include both distinct ideals over 7 and inert norm 25. It checks
all 115 specified exponent patterns, literal zero masks, exact dual norm scaling,
and 78 finite cyclic band-limited coset sums via cyclotomic reduction. Wider
Fourier support and neutral-zero erasure are rejected. It does not numerically
evaluate an infinite Schwartz sum. The analytic theorem rests on its proof.

Both proof and code have the same author. Alternate finite implementations and
normal/optimized Python are not independent mathematical peer review. No full
repository validator, remote CI, external theorem reconstruction, or proof
assistant was run. MANIFEST.json binds all final payloads except itself.

## Exact next theorem, still open

For the fixed positive weight just constructed, prove the ONE-SIDED upper bound

    sum_(nonprincipal t: N rad(product columns)>H)
       a(t) sum_(u!=0) Phi(u/sqrt(H)) h_t(u)
        <= C_(k,epsilon) H X^(k+epsilon)

for the actual native Mobius coefficients, required twists, and shorter scales
at the same physical height. The Liouville equivalent requires its own stated
same-height transfer. Neither a bound on an arbitrary positive replacement nor
a coefficient-insensitive independent-residue model supplies this estimate.
