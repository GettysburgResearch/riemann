# Direct interval comparisons for the higher-degree field census

These compressed JSON Lines records contain the LMFDB field label, the strict pass result for the unconditional analytic weight \(2\xi_K'(1)/\xi_K(1)<2\), and the Arb interval for the corresponding completed-function difference. A null is followed by a separate refinement for the same label at the end of the stream. All final comparisons are strict. The starting catalogue is the [LMFDB production snapshot](https://doi.org/10.5281/zenodo.24323763), with field metadata from the LMFDB Collaboration under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The spectral inventory for quintics was independently obtained from the Bordeaux tables and matched field by field.

| Degree | Fields within analytic cap | Tested after small-prime exclusions | Refined | Pass |
|---|---:|---:|---:|---:|
|5|21,440|9,599|2|616|
|6|13,499|5,787|7|487|
|7|2,248|794|0|68|
|8|116|47|0|2|

Use python-flint 0.9.0 and PARI/GP 2.17.2. First run the [snapshot extractor](../../scripts/extract_zhao_lmfdb_fields_nov18.py) against the archived source. Set PARI_GP to the path to gp if it is outside PATH. From the repository root, run, for example,

```bash
python scripts/replay_zhao_high_degree_unconditional_nov18.py /path/to/extracted 8
```

The [mathematical error estimates](../../research/explorations/zhao-field-unconditional-replay-nov18.md) explain the order of the two contour lines, the Fourier interpolation, the fixed-point integer arithmetic and omitted ideal counts. The archive is computational evidence for a proposed classification, subject to review.
