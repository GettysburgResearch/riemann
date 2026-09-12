# HSC26 validation and evidence boundaries

Date: 2026-09-12. Proposed component proofs; independent review required.
No RH proof, arbitrary-order realization, numerical retuned parameter, or
independently accepted mathematical result is claimed.

## 1. Inherited full-source replay

The ten-file ICR26 packet from PR #863 was extracted from the supplied ZIP
into a separate inherited directory. Its file names, Git blob identities and
lengths were compared with the live remote subtree
`cd1fc7d91393d788a1cfa07c7df60c0bbaea4918`, at head
`0640c9c59be0bf20c18258460a7517fb09728e82`.
Its proof, cluster-limit note and exact parameter definition were read.
SOURCES.json pins the consumed proof, parameter, producer and result bytes.

Both complete accepting commands were rerun separately:

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json

They reconstruct the full defining theta source, all 84 degree-120 integration
cells, four individual infinite time tails and the complete omitted-index tail.
They reconstruct moments through sixteen, the seven-variable contraction and
its 49 inverse identities. The output in both modes is byte-identical to the
parent result, with SHA256

    531b80259640396ce9f54144b69dbfb8daf90ecf944ca9cecc1e0809d0500160

This is a REPLAY of the unchanged existing interval backend, not a second
independent implementation, new moment calculation or new referee acceptance.
The old rejection suite and other parent/grandparent campaigns were not rerun.
An attempted streaming container launch failed before execution; the subsequent
ordinary executions above completed. No interrupted launch counts as a replay.

## 2. New exact finite controls

The new standard-library check.py uses integers and Fraction arithmetic only.
It reconstructs:

- Eight finite stars with one through eight leaves, comparing conditional
  edge-sign moments through degree sixteen with a separate enumeration of all
  1,020 physical spin configurations in those panels.
- The exact original-metric second moment, retaining all shared-root mean cross
  terms; one dimer specialization and finite fourth-moment controls.
- All 49 identities for an independently inverted seven-by-seven rational seed
  Jacobian; its maximum row-sum inverse norm is below 75,000,000.
- 192 finite harmonic-weight/telescoping identities, five complete finite ballast
  variance identities, and exact symbolic cancellation of the three large-field
  coefficients and the probability-tail constant.
- Three invalid nonferromagnetic/negative-weight inputs, which must reject.

The finite panels are arithmetic tests, NOT proofs of infinite products,
Euler--Maclaurin remainders, the analytic implicit-function argument, or the
large-deviation theorem. The latter are written proofs in PROOF.md.
The copied seed_parameters.json is checked against the parent's literal Git
blob, not merely against a mutable local checksum.

Commands:

    python -I -S -B check.py --check result.json
    python -I -S -B -O check.py --check result.json
    python -I -S -B test_rejections.py
    python -I -S -B -O test_rejections.py

The two mathematical modes reconstruct identical result bytes. In each mode,
the rejection script runs one pristine full acceptance and eight real altered
CLI cases: false RH status, integer/Boolean alias, duplicate JSON key, a resealed
harmonic weight changed from 1/(2n) to 1/(3n), resealed acceptance of negative
leaf correlations, changed pinned seed data, an unsealed proof change, and an
extra unlisted file. These distinguish semantic reconstruction, model-domain
checks, source authentication and inventory checks. No assert is used as an
acceptance rule. No new symlink test or native Windows execution is claimed.

## 3. Delivery contract

There are nine regular payload files; SHA256SUMS names the other eight exactly.
Result JSON uses rational numerator/denominator arrays, strings, integers and
Booleans; floating tokens, duplicate keys and type aliases are not accepted.
The producer-only --emit operation is distinct from the accepting --check.

Before publication a minimal temporary Git roundtrip checks the add-only patch,
preserves a predecessor manuscript and an unrelated sentinel, compares every
new payload byte, and reruns both mathematical modes. Clean archive extraction
is checked separately. These are scoped fixtures, not full Riemann checkouts.
The exact new subtree is computed from local Git objects and compared with the
remote subtree before attaching it to a branch. Final receipts accompany the
external handoff archive; they do not rewrite this immutable proof packet.

## 4. Explicitly unperformed work

No explicit numerical starting index N0, new retuned finite or infinite parameter
vector, finite Ising graph with that new index, actual Xi zero, large-field
spectrum, or infinite star integral was numerically certified. The existence
claim is for all sufficiently large N by strict C1 perturbation of the inherited
root. Its constant C_N is not claimed equal to the theta constant. The models
are proved different at moment sixteen and do not converge to theta as N grows.

A non-directed mpmath calculation checked the harmonic-product asymptotic and
the constant A for orientation; it is not retained as proof evidence. No
scouting value enters accepting code. The weighted Lee--Yang theorem and DLMF
special values/asymptotic formulas are classical imported inputs. The primary
Lee--Yang PDF text was read; its page-image request failed with a cache miss.
No unviewed diagram or image supplies any premise.

No full-repository validator, formal kernel/Lean build, remote CI success,
external zero census, all-order induction, or independent referee review is
claimed. The publication is a global completion theorem for fixed finite
moment seeds, with a complete statement of the remaining RH-strength task.
