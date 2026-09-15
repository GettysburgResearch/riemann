# SARG26: S(t) record import and a smaller replay certificate

**Status: imported claims; directed scalar replay passed; primitive Hardy-Z
replay PENDING. Proposed component proof, requiring independent review.**

This packet imports the two argument records supplied by Gideon on 15 September
2026 and adds a smaller, independently derived Turing certificate. It does not
claim a fresh evaluation of zeta, an independently certified world record, or RH.

The announcement is indexed as [Avraham Eisenberg's 14 September X post](https://x.com/avi_eisen/status/2099622967751663749),
with a [certificate reply](https://x.com/avi_eisen/status/2099622971455275255).
Those primary URLs and matching text were located through search; direct retrieval
returned HTTP 403. `news.txt` is the USER-SUPPLIED transcription, not an authenticated
export of the complete thread. The original author's computation is not ours.

## What is imported and what is added

All **844 coarse brackets** and both fine record brackets are preserved in
[news.txt](news.txt). The exact 30-digit heights and 31-digit counts remain integers.
The posted midpoint integrals, bracket-width errors, Turing bounds, integer-count
enclosures and one-sided S ranges are independently reconstructed with 384-bit
outward arithmetic and a complete analytic theta remainder.

| Claim | Reconstructed enclosure, conditional on the indicated Z sign changes |
|---|---|
| Positive record, S(gamma1+0) | [4.184313790968, 4.185379642172] |
| Negative record, S(gamma2-0) | [-4.338683949971, -4.338370564460] |

**New practical deduction:** the records do not require replaying every supplied
bracket. A monotone-defect argument permits these shorter padding windows:

| Record | Left/right padding | Selected brackets | Certified inner core, CONDITIONAL on signs |
|---|---|---:|---|
| 1 | 7 / 7.32 | 153 | [-1.001862683, 1.008402874] |
| 2 | 7.67 / 7.34 | 157 | [-1.010014783, 1.008373582] |

Each fine record bracket REPLACES its coarse parent. Thus **310 brackets / 620
endpoint jobs suffice** to establish the anchor counts, both records and a
complete local census on both [t_i-1,t_i+1]. This implication does not assume RH,
list completeness, simple zeros, or the asserted anchor counts. Genuine signs
are still an unperformed prerequisite. No globally optimal compression is claimed.

Read [the proof and research programme](RESEARCH.md), then
[the source and validation boundary](VALIDATION.md). Complete derived data and
zero-based selected indices are in [results.json](results.json).

## Run

Python 3.10 or later; standard library only. From this directory:

```sh
python -I -S -B check.py --check results.json --jobs jobs.tsv
python -I -S -B test_check.py
python -I -S -B -O check.py --check results.json
python -I -S -B -O test_check.py
```

`jobs.tsv` contains exact integer anchors and exact rational offsets, not lossy
floating point heights. Its 310 rows specify 620 endpoints. Regenerate it rather
than treating it as another primitive evidence source.

```sh
python -I -S -B check.py --require-primitive
```

The last command MUST refuse with exit status 2: this packet has no Hardy-Z
backend. Ordinary successful execution explicitly retains
`primitive_z_replayed: false` and `record_independently_certified: false`.

## Ownership and next acceptance target

Continue this programme on its PR: first obtain a source-pinned, remainder-bounded
high-height Z backend and replay the 620 endpoint jobs; then independently review
the local-census proof. Only after that should record status be promoted. The
subsequent research targets are sharper local gap/cluster data and targeted
prime-phase searches, not another claimed RH completion from a finite window.

This addition is based on `main@f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
No existing research, main, canonical status, formal file or workflow is changed.
Third-party text retains its original rights; this import does not relicense it.
