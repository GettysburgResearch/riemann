# Earlier pass-three attachment: preservation and coverage reconciliation

The subsequently supplied `riemann_review_pass3_bundle.zip` contains a different, earlier local pass-three handoff based on `13ac26caae546c8a6481a85b2f61ecc524dbbb27`. Published pass three at `37ea752b07700c7ba76335ba082cb6993caca35f` remains the controlling current review. Its subtree `8f3236ffb99fc0033e3cc40684a872d0ca922530` is unchanged by this import.

The attachment reports 37/45 principal manuscripts covered and 4,966 bounded checks; the published pass reports 45/45 and additional independently reconstructed finite minima. Do not replace the published record with the attachment, add their overlapping counts together, or interpret either count as package-wide acceptance.

## Why retain the earlier attachment?

Twenty of its 23 inspected source-file identities occur in published pass three. Three additional inspection records in its FILES.tsv concern synthesis notes that the published RESUME still leaves for targeted follow-up:

| PR | Exact source commit | Source path | Recorded Git blob |
|---|---|---|---|
| 803 | db175de165a9077e709b1cb482998171ffc0c6e7 | standalone/2026-09-08-arithmetic-norm-transfer/SYNTHESIS.md | c57f733bd97ea2dff808cb9141bd24303296bcb3 |
| 828 | 528b33ac8d57b5a046260ee45d585cd3fe720f4c | standalone/2026-09-08-astra-grounding-capacity/SYNTHESIS_AND_ATTEMPT.md | d5b5775cfed45695b3450226b210231a8deed504 |
| 829 | f782788933dc21a0fe6a844950f5ca532eba7d86 | standalone/2026-09-08-astra-coherent-channel-synthesis/SYNTHESIS.md | 6430664f8f9b047ccedbf9fa08bc00cc727143d3 |

These are the attachment author's inspection records, not new mathematical verdicts by the uploader. The next reviewer should reconcile their actual scope and findings with the published report before changing any hold. Their presence alone does not clear the outstanding synthesis/source-interface work.

## Preserved delivery

All seventeen review payload files are retained byte-for-byte under [pass3-local-handoff](pass3-local-handoff/README.md), together with the original delivery README and receipt under its `delivery/` subdirectory. Relative internal links and the original SHA256SUMS remain usable. Historical paths and statements such as "not pushed" remain unchanged as authoring-time records; this note records their later publication. The redundant add-only patch is not applied or copied into the repository.

The uploader authenticated every payload file against DELIVERY_RECEIPT.json and checked the published pass-three manifest. No prior review is replaced, no research source is edited, and no mathematical acceptance or integration into main is implied. Original author execution claims retain their stated limitations.
