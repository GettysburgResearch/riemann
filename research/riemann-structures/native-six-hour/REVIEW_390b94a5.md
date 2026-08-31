# Independent review of the frozen event-minor calibration contract

Reviewed freeze `390b94a5b5a1f87d69cca71ef258df5d74d67ffd`:

| File | Git blob |
|---|---|
| `native_event_minor.py` | `b806a192035d559855be2cae0de6334968dabadc` |
| `NATIVE_EVENT_MINOR_PREREGISTRATION.md` | `d64c92e7da9d029c991f4168bc3e7748fb7761ba` |
| `NATIVE_EVENT_MINOR_REPLAY.md` | `4bc9c7c18caba74da69990de77d63fd5f7feadb8` |
| `native_event_minor.calibration.json` | `8267944c696e683eb5e02c2a7d6679a67add81ed` |
| `tests/test_native_six_hour_event_minor.py` | `9f88d93fc70d31f6ae0ecfb5bc2965d105633a90` |

I independently read the complete producer, preregistration, replay note and all 18 tests. The reviewed working files agree with these frozen blobs. No mathematical or implementation blocker remains in this calibration and continuation contract.

The source reconstruction retains the literal current factor 2, every reduced-ratio `1/g` allocation, and all event addresses, including allocations with zero update. The exact base calculation reconstructs the authenticated horizon-900 minor. Both modular states are updated through an entire simultaneous event group before rank is tested; neither an intermediate singular state nor an isolated omitted alias is substituted for the completed physical fibre. Prime certification, denominator eligibility, modular elimination witnesses and the fallback field are checked explicitly. Nonzero determinant in either field proves rational rank 20; failure in both fields remains an unknown interval rather than a rank counterexample.

The continuation imports only the immediately preceding verified frozen endpoint. Its interval ledger correctly carries an accepted rank through event-free integer ranges and retains gaps following unknown events. The collector composes previously verified immutable components, checks their source identities, endpoint links, census and interval coverage, and does not claim to rerun local source reconstruction or modular elimination. A complete later chain or an all-horizon conclusion is not established by this calibration alone.

During review I identified a resource issue in the first collector layout: retaining every raw and decoded panel at once could defeat the declared memory discipline. The author repaired it before this freeze. The reviewed collector first authenticates and discards each raw component, then reauthenticates and parses one component at a time, retaining only compact predecessor state. The mathematical contract and complete event coverage are unchanged.

The coordinator reports Ruff checks, calibration write/check/optimized-check, and all 18 ordinary plus 18 optimized tests passed. The frozen calibration proof-object hash is `1637bcc69d4c714818587af8d29cdb0e16a65c660692a47d6b02afde5122f269`. I performed no scientific execution; these run results are attributed to the coordinator. This report makes no claim that a target panel, the full continuation chain, an ambient 64-dimensional decoder, an energy bound, or a retained-gamma identification has been completed.
