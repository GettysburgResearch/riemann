# Calibrated degree-eight infinite-chain component

The assessment and mathematics were developed outside the Riemann repository
on 12 September 2026. This copy was packaged for publication on 13 September
2026; packaging does not promote the proposed results to accepted mathematics.
The theorem and all qualifications are in [PROOF.md](PROOF.md). It constructs a
small-positive-background-correlation family matching theta's moments through
degree eight and all three real-field growth coefficients. The tenth moment
is different, and no all-order theorem or RH proof is claimed.

The accepting calculation uses Python 3.12.10 standard-library rational and
512-bit outward dyadic arithmetic. It newly reconstructs the complete native
theta moments and infinite calibration tails using the explicitly extracted
primitive routines of #875 at
`be149104721ae7b65b624c100118edfd7b76b69b`. Their source identities and full
analytic remainder proofs are imported. The four original files are unmodified
in `predecessor/`; `predecessor-provenance.json` records their pinned paths and
hashes. Before any predecessor primitive executes, `source_provenance.py`
checks all four files against fixed consumer-side hashes and checks the receipt
against the fixed commit, paths and hashes. The loader compiles the same
verified bytes directly, bypassing cached bytecode and substitute imports.
Changing both a source file and its JSON receipt does not satisfy this gate.
As with any local checker, this does not protect against replacing the consumer
itself together with its expected constants. Local `.gitattributes` preserves
the original source bytes across Git checkout line-ending conversion.
The copied routines are attributed to the Gettysburg Research contributors
at the pinned #875 commit. Its MIT copyright and permission notice is retained
in `predecessor/LICENSE`; no independent authorship of those routines is claimed.

Run from this directory:

```text
python -B certify_dimer.py
python -B certify_dimer.py --mesh 160 --output dimer-certificate-mesh160.json
python -B test_algebra.py
python -B test_provenance.py
python -B test_acceptance.py
```

Both complete-source certificates passed in the original 12 September
assessment, proving the same radius-1e-12 root
box with preconditioned residual below 7.63e-22 and whole-box contraction bound
below 1.252e-7. Each run checks 50 exact inverse equalities. The complete
standardized tenth-moment error is in
`(0.0332114805634689, 0.03321163716180245)` with outward exact rational
endpoints retained in the JSON files. The analytic connected continuation has
no certified explicit positive-q radius.

On 13 September, the full mesh-128 accepting calculation and the four algebra
tests were rerun successfully from this packaged location, after adding the
source-authentication gate. The mesh-160 JSON is the retained 12 September
receipt; it was not newly rerun during packaging. Four new provenance controls
pass: pristine hashes, rejection of altered source despite a resealed receipt
before any primitive executes, rejection of a changed receipt commit, and
execution of verified bytes despite a substituted preloaded module.
Four bounded acceptance tests also pass: exact self-map equality is rejected,
unit contraction is rejected, invalid radii/bound types are rejected, and
nonpositive weights or the limiting edge correlation one are rejected.
These tests do not require an extra native-source integration.

Four independent finite algebra tests passed: exact four-configuration dimer
cumulants, dual-number differentiation of the full five-variable Jacobian,
general unequal-weight edge derivatives, and the reverse inverse identity.
These are meaningful checks of separate algebraic representations, not a
second transcendental backend or formal proof.

`sensitivity.py`, `scout_dimer.py` and `dimer-scout.json` retain the exploratory
selection of the edge and root. They do not support the existence theorem;
the directed fresh-source calculation does. The scout additionally uses
mpmath. The accepting certificate does not.

To reproduce extraction from a repository with the pinned object available,
run `python -B extract_predecessor.py`. Repository discovery uses the Git
checkout enclosing the script or current directory; an archived packet can
instead use `--repo PATH`. The whole incoming set is authenticated before the
four local source copies and receipt are written. No checkout, commit or fetch
is performed. Extraction is unnecessary when using the already copied files.
`scout_dimer.py` uses the same discovery and optional `--repo PATH`, and its
output defaults to this script directory. For both `certify_dimer.py` and
`scout_dimer.py`, a relative `--output NAME` is relative to this script
directory, even when the command is run from the packet root; absolute output
paths are used directly. The accepting certificate itself does not need Git
or a checkout.

The first certificate attempt failed its exact inverse check because the
constant Jacobian row used Python integers and the imported inverse's division
coerced those entries to floating point. The row now uses `Fraction` entries;
the full source reconstruction was rerun successfully before recording results.
This failure was detected, not silently discarded or counted as validation.

A second agent reviewed the full proposed proof, new certificate code, pinned
source routines and their documented analytic remainders. It found no defect
in the stated proof. That is a source-scope analytic review within this session,
not independent mathematical acceptance or formal verification.
