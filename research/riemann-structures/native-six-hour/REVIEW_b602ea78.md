# Independent review of the accepted fixed-minor diagnostic

Reviewed freeze `b602ea788ed6a74800c5dd394c118dbc14dd59d2`:

| File | Git blob |
|---|---|
| `native_fixed_minor_diagnostic.py` | `3b2fd73054f89f0d2d4ea04bf8a14d02c06bb4d7` |
| `NATIVE_FIXED_MINOR_DIAGNOSTIC_REPLAY.md` | `f808c66805ac768958a627811ddeb310f1f0baad` |
| `native_fixed_minor_diagnostic.json` | `a2a38c2f79b2ce7d0ab7243dae0392f51880cfcb` |
| `tests/test_native_six_hour_fixed_minor_diagnostic.py` | `5e10df88a8036f8fffe9658f7f26dc3e4c31a76b` |

The complete producer, replay note and eight tests were read, followed by the repair delta, the frozen source-field assignment and the accepted artifact. The reviewed working files agree with these blobs. No remaining blocker was found.

The first coordinator write attempt caught an error missed in my initial static review: the new reader treated `maximum_alias` as the last smooth alias, whereas the frozen producer stores the integer cutoff `isqrt(H // (a*b))`. The repaired reader checks that exact cutoff and separately bounds the last smooth alias. The tests now retain a real strict gap and reject a changed cutoff. The unsuccessful first write produced no accepted artifact and is not counted as a successful run.

All four predecessor blobs authenticate before decoder compilation or capture parsing. The diagnostic checks the fixed twenty rows and columns, the canonical exact inverse-entry bounds, all forty-four local shift-kind tables with the unchanged 65 terms, the partial/remainder identities, the alias metadata, and every stored comparison row sum. It imports the already verified inverse and source/comparison identities from the frozen extension; it does not claim to recompute them.

The accepted artifact verifies that the inverse-amplified local-cutoff remainder is less than `1/2500000`, while every positive diagonal weighting of the recorded comparison matrix has infinity norm greater than three. It preserves the original `UNKNOWN_TAIL_NOT_CONTRACTIVE` outcome. Its alias metadata separately records maximum cutoff 11863283 and maximum smooth alias 11809800, with 13348 retained alias entries. No all-future rank certificate or new tail method is asserted.

The proof-object digest is `e8c2ea499e991fc292d012aaa13246e5fe9ed5f691ed300bf02440b25afded61`. The coordinator reports the corrected write/check/optimized-check and all eight ordinary plus eight optimized tests passed. I ran no scientific job; execution is attributed to the coordinator. This accepted diagnostic supplies the numerical premises that Section 5 of the frozen singular-minor proof had explicitly left as a separate exact-rational verification target.
