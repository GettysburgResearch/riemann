# Reviewer C validation: current versus historical execution

Read [pass3/RETRY_REPORT.md](pass3/RETRY_REPORT.md) for interpretation and [pass3/COVERAGE.tsv](pass3/COVERAGE.tsv) for exclusions. New code is review-only and uses exact rational arithmetic or synthetic Git fixtures; none executes a privileged workflow.

From repository root on Linux with Python 3 and Git:

```sh
python -I -S reviews/C/pass3/scripts/validate_retry.py
python -I -S -O reviews/C/pass3/scripts/validate_retry.py
python -I -S reviews/C/pass3/scripts/replay_record_arithmetic.py --output /tmp/c3-record.json
python -I -S reviews/C/pass3/scripts/replay_manifest_contract.py --output /tmp/c3-manifest.json
python -I -S reviews/C/pass3/scripts/replay_majorant.py --output /tmp/c3-majorant.json
```

Each replay authenticates its original producer bytes. Each itself runs the target in ordinary and optimized subprocesses. The three drivers were also executed under both outer interpreter modes, yielding identical retained reports. Counts per driver execution are two original record-function runs, 22 manifest CLI runs plus ten report roundtrips, and 1539 majorant currents per mode. These counts are not added together as theorem counts.

`validate_retry.py` verifies a fixed file denominator, byte hashes, explicit scope fields, retained report counts, and deliberate corruptions. It also rebuilds the historical four-report view in a temporary copy and reruns the old census and pass2 consistency validator in both modes. The four current front-door reports intentionally differ from the old pass2 manifest: running the old manifest check directly against the new front door is not its frozen replay. No historical manifest is rewritten.

The 566-row census, 340 actual historical-source comparison records, and 17 pass2 rejection fixtures were freshly replayed for consistency. Their prior network observations are retained; the 340 heads were not re-fetched. Full sixteen-file X-105560 payload, external Arb certificate, actual scientific manifest graph, complete native majorant fibre and historical source-check function were not replayed.

No fresh Lean/Lake, Comparator, Nanoda, large zero/interval campaign, all-history security scan or complete rights audit was performed. The pass2 Lean regression remains NOT COMPILED. The source reading boundary is in `pass3/FORMAL_REPAIR_CONTRACT.md`.

File-manifest consistency is not a signature of GitHub origin or a proof of the mathematical claims. Publication requires separate remote tree/blob readback; see the PR receipt. Earlier detailed validation text is preserved at `pass3/evidence/PRE_RETRY_VALIDATION.md`.
