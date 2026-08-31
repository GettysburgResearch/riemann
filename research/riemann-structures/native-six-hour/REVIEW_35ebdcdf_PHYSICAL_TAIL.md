# Independent review of the frozen physical-tail acceptance packet

Reviewed freeze:35ebdcdf060489be7a53e81246094043ec4aa9c0.

| Frozen file | Git blob |
| --- | --- |
| native_physical_tail_certificate.py | 99eb1ed9b7ace56412f6fb0cbb1f72e4155f1b28 |
| native_physical_tail_certificate.json | a5834b190157418648148b8098d3b210b88c7507 |
| NATIVE_PHYSICAL_TAIL_REPLAY.md | 1651cbfd8fd6a8bcfadbb088c324eef7178ef7f4 |
| tests/test_native_six_hour_physical_tail_certificate.py | 57344d1cccfada6d00e18fc8f70bb74591c564df |

The final artifact proof is
2e07cd1e848f5ef516aa17e0d2e5c4628df7b5a18575a51b9d2f6ddf6027ef16.
All four working files have no diff from the freeze. This report covers
only the physical-tail packet. It does not independently review the
H450 packet in the same commit, whose producer I authored.

I read the complete final producer, replay note and all14 tests. This
also uses my complete read of the frozen minor-tail proof and its
literal local coefficient, majorant and inverse helpers. All seven
direct source inputs are authenticated before parsing or compilation;
the unchanged scout authenticates its own source chain. Both complete
acquisitions are replayed and compared as typed records before the
separate arithmetic audit.

The independent audit retains every1/g alias weight and all36 signed
coordinates, reconstructs the selected20-column matrix and positive
prefix, and subtracts that same majorant from its infinite upper bound.
It verifies both exact inverse products, every entry of the absolute
inverse-times-tail matrix, every row sum and the exact theta. Display
intervals are outward summaries only. The acceptance logic keeps both
theta>=1 results as UNKNOWN_TAIL_NOT_CONTRACTIVE; neither is a rank
counterexample or a successful all-future contraction certificate.

The source, alias-order, coordinate-selection, signed-prefix, inverse,
status and numeric-type countercontrols match the stated contract.
Complete old records are retained, and the original acquisition18-test
contract is not replaced. No blocker was found in this scope.

At review time the coordinator reported final producer write, check and
optimized check passes and14 ordinary test passes. The14 optimized
test run was still pending after a memory-gate stop. I ran no scientific
job, and this review does not mark that pending run complete. Earlier
acquisition18-test passes remain a separate reported result.

The actual inverses prove rank20 at the two isolated tested horizons900
and2^20, using the source dimension bound. The certificate does not fill
the intervening gap or establish a future threshold. The separate
data-informed2^48 extension, its validation and any outcome are outside
this four-file review.
