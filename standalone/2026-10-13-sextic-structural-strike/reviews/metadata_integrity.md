# Final metadata and integrity-verifier review

Reviewer: extraction lane, `/root/extraction_radical_attack`.

**Verdict: PASS for the metadata wording and verifier scope at the exact
hashes below. No correction is required.** The final manifest and frozen
Git content commit remain to be bound by a separate receipt after this
review is included. This review does not certify an unpublished commit,
authenticate an unpinned manifest, or promote the packet into the
integrated mathematical record.

## 1. Exact reviewed files

All paths in this table are relative to
`standalone/2026-10-13-sextic-structural-strike/` in
`GettysburgResearch/riemann`.

| File | Bytes | SHA256 |
|---|---:|---|
| `VALIDATION.md` | 11612 | `c831d02beb41b09e30080b060fbe8000d3b2b6ed4183a020055d291abdbba62f` |
| `PROVENANCE.json` | 11745 | `5d5f92fbdeccdbb3baec4014adb6dccd140f46739c4acb829626ff6ef8e319d2` |
| `verify_packet.py` | 7216 | `167619c3585292c6e84518a32b6a763bff5b1a2bcbf7689f95c8ab4a061b314e` |
| `README.md` | 18031 | `99bddd1fa16ac04171b42ff0cd40a99d32c8752389a4480b239863e0e777493e` |

I read the full validation document, provenance object, and verifier
implementation. I also inspected the provisional manifest's schema,
exclusions and complete 48-file inventory. That inventory predates this
review's inclusion and is intentionally not assigned a final manifest
hash here. The existing README audit is unchanged and remains bound to
the README hash in this table.

## 2. Authorship and review disclosure

The authorship table is accurate about the work I can directly attest:
I authored the short-factor non-smallness lemma and the first-order
Euler-trace refutation, and participated in the early collision
development underlying the root's CT1 composition. My own reconstruction
of that composition is therefore not a wholly independent development.
The validation document makes that overlap visible and does not count
my contribution as independent review of my own lemma or Euler theorem.

The conductor sieve, its conductor corollaries, and the necklace
representation were authored in other lanes. My existing reviews
reconstruct those written arguments, name imported analytic inputs,
record necessary clarifications, and bind their final bytes. The
necklace review also discloses my work on the motivating resonance
obstruction. The native lane's plateau suggestion and diagnostic
authorship are disclosed in the validation table and its review.

I read `reviews/root_reconstruction.md` at SHA256
`3961c47144060e1979502122b19932121fd0ff841b64b12cbc90efeaa40e5b98`.
It identifies the root's own contributions and separates review of
other lanes from reconstruction of its own composition. Its scope
does not turn team agreement into an external expert endorsement.

The historical review hashes are retained together with explicit
updates. In particular, the initial conductor and CT1 verdicts are not
silently attached to changed final files. The documented corrections
match the final arguments and their update reviews. The document is
also explicit that this is same-team mathematical scrutiny, not a
formalization or certification of the complete external analytic
literature.

## 3. Source identity and mathematical scope

I independently recomputed the byte count, SHA256, and Git blob SHA1 of
each of the eleven copied repository sources. Every value agrees with
`PROVENANCE.json`. The Git blob calculation includes the exact byte
length, Git's `blob` header, its zero separator, and the complete file
bytes, including any terminal newline. I also checked that every
copied source is covered exactly once by the source-transport list.

These are checks against the recorded source identities. This metadata
audit does not claim a new authenticated fetch of all eleven original
commits. Immutable commit/path URLs and recorded original blob IDs make
that separate authentication possible; the local verifier itself
checks their internal consistency without making a network request.

The seven `proof_files` entries match the actual final mathematical
files. The three diagnostic reports bind the correct proof bytes and
the actual producer hashes. The source metadata distinguishes the
three named primary inputs from copied repository sources and from
earlier frontier context. It credits Moree's classical identity while
identifying the new application, and does not claim to reprove the
full de Faveri large sieve or the prime ideal theorem.

The validation boundaries are faithful to the mathematical packet:

- Refuting the larger unfiltered Euler and complementary traces does
  not refute the filtered native moment.
- Exact coefficient preservation under the necklace replacement does
  not transfer a previous tube estimate to the new representation.
- The pair sieve uses a specified conjugate local type, with the
  stated field and primitive-character hypotheses. It does not give
  a conductor mean for every sextic local exponent pattern.
- The signed all-distinct prime result is a selected-sector statement;
  it does not supply a lower bound for the complete prime/composite
  signed core.
- Finite residue, coefficient and exponent checks do not prove an
  asymptotic moment theorem, a new zero-free region, or RH.

The explicit `not_proved` list in provenance and the final paragraph
of validation preserve those distinctions. The parent commit, parent
tree and observed main commit are recorded context. Their eventual
relationship to the published content commit still belongs in the
Git receipt.

## 4. Verifier implementation audit

The verifier implements the advertised local transport contract.

1. It accepts canonical relative packet paths, rejects upward or
   absolute traversal, checks resolved containment, and requires the
   referenced file itself to be a regular non-symlink file.
2. It checks the manifest schema, the declared two-file exclusion set,
   sorted unique entries, and equality between the inventory and the
   actual included regular files. Generated `__pycache__` directories
   are expressly ignored in the manifest. Each included file is
   checked for byte length, SHA256 and Git blob identity.
3. It checks the provenance schema and repository name, verifies all
   eleven copied source identities, requires immutable-format commit
   IDs, and reconstructs each expected commit/path URL. It also
   requires exact coverage of the copied `sources/` paths.
4. It checks seven distinct mathematical source identities. For every
   diagnostic pair, it requires literal report-byte equality, a PASS
   status, the recorded proof size/hash, and the actual producer hash.
5. In replay mode it invokes each producer under ordinary Python and
   `-O`, passes an explicit proof and a report path in a temporary
   directory, checks the process status, and requires the replay's
   bytes to equal the recorded report. Producer calls do not require
   a shell. Inspection of the producers' write operations confirms
   that their requested output is the supplied report path.
6. Acceptance uses explicit `require` failures rather than removable
   `assert` statements. Ordinary mode contains no packet write.

The verifier is deliberately not a trust anchor for its own manifest.
If a different packet, provenance and manifest were all substituted
together, its local hashes would not identify that substitution
without an independently pinned containing Git commit. Its docstring,
output and validation description make that limitation clear.
Likewise, it does not evaluate the truth of the analytic manuscripts
from their hashes or report statuses.

## 5. Execution and focused negative controls

I independently ran ordinary mode against the reviewed packet. It
returned PASS with 48 inventoried files, 11 source transports, 7
mathematical files and 3 identical ordinary/optimized report pairs.
The report quantities, proof hashes and producer hashes agree with
the validation narrative. The root separately reported a successful
six-execution `--replay` run. I inspected that code path but did not
claim those six producer executions as my own independent run.

I also exercised five targeted negative controls in isolated temporary
copies of the packet. The original packet was unchanged. Each control
failed for the expected stated reason:

| Temporary mutation | Expected rejection observed |
|---|---|
| Append one newline to a mathematical file without updating its inventory entry | Mismatched byte count |
| Add an uninventoried regular file | Inventory does not cover the exact packet |
| Alter a copied source URL and refresh the provenance inventory entry | URL does not match its commit and source path |
| Change the producer hash identically in both conjugate-pair reports and refresh both inventory entries | Producer hash mismatch |
| Append a newline only to an optimized report and refresh that inventory entry | Interpreter reports differ |

Refreshing selected inventory entries in the latter three controls
ensures that the deeper consistency checks are exercised, rather than
merely triggering the first manifest checksum check. These are finite
transport tests of the stated verifier behavior, not tests of the
analytic mathematics.

## 6. Required final binding

No mathematical or metadata wording correction is requested. After
this review is copied into the packet, the root should regenerate
the inventory and freeze the content commit as planned. A separate
receipt must then bind the final manifest, all inventoried blobs, the
commit's parent/tree, and the fact that publication-receipt additions
do not alter the reviewed content.

The current validation language anticipates that completed receipt.
Until it exists and is checked, this review's PASS concerns the exact
local files above and the provisional inventory behavior only. It
does not assert that a publication or remote read-back has already
occurred.
