# Lossless local-pressure transfer

Proposed research contribution, 14 September 2026. **Not an RH proof; independent review pending.**

For a prescribed Fourier kernel, separate close pairs from a separated remainder. A complete sinc-square majorant puts the remainder's Gram spectrum below the clipping threshold; every removed pair pays its own two-point pressure budget. This proves a dimension-uniform local-pressure-to-clipped-defect theorem, rather than another RH-equivalent completion criterion.

Using the already published case-J six-gap inequality of Gebendorfer's 7 September research draft, the proposed cumulative simple-critical-zero bound is

```
104405554524189 / 155021134296875
= 0.6734923918453979711624...
```

It exceeds that draft's displayed 0.6734760237990874891990... by 0.00001636804631048196... in the fraction. This is a comparison with a specific internally checked draft, **not a claim of an independently reviewed world record**. The original repository's older seven-point input separately improves from its extracted 0.673009652279... to 0.6730583253156109674105... without modifying its local certificate.

## Read and reproduce

- `PROOF.md`: general theorem, explicit majorant, close-pair bound, smoothing, retained-defect algebra, unconditional arithmetic transfer, numerical corollaries, and precise reading boundaries.
- `inputs.json`: attributed window and case-J coefficients transcribed from the source's complete Appendix A.
- `verify.py`: standard-library exact-rational checks of the **new finite arithmetic** and source capacities.
- `results.json`: retained output.
- `test_verify.py`: seven tests, including rejecting invalid majorants and altered records.
- `VALIDATION.md`: executed checks and exclusions.

```bash
python -I verify.py --check results.json
python -I test_verify.py
python -I -O verify.py --check results.json
python -I -O test_verify.py
```

## Dependency and acceptance boundary

The local six-dimensional pressure searches are imported mathematical inputs. **They were not rerun here.** The checker deliberately emits `six_dimensional_pressure_search_replayed: false`. A finite arithmetic PASS does not validate those searches, the Fourier/Gram proofs, or the external pair-correlation theorem. Do not promote this packet to independently reviewed status without inspecting those dependencies and the new proof.

The principal arithmetic input is Lamzouri's unconditional fixed-function pair-correlation formula (arXiv:2609.02882, Lemma 3.1 and its unweighting). The principal numerical input is Gebendorfer, DOI 10.5281/zenodo.22643957, Proposition 2.1 case J, explicitly labelled an internally checked research draft. Source optimization, pinching, clipped stability, and pair-selection precedents are credited in `PROOF.md`.

The proposed new contribution is the lossless separation-or-pair transfer and its smoothing-compatible use, not authorship of the imported window or the existing arithmetic theorem. The percentage result is not an argument that this method can reach RH: a positive-proportion statement does not exclude sparse exceptional zeros.
