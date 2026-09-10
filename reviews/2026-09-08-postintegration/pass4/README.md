# Final post-integration review: scoped extraction handoff

**Review only. This packet completes the selected final-review queue; it does not integrate main, approve every historical executable, or prove RH.**

Read [REPORT.md](REPORT.md) for the findings, [EXTRACTION.tsv](EXTRACTION.tsv) for all 45 inventoried packets, [DECISIONS.tsv](DECISIONS.tsv) for the final dispositions, and [REPAIRS.md](REPAIRS.md) for six extraction qualifications. Four qualifications are inherited; the infinite-operator trial-domain requirement and the MW receipt-parser finding are new.

The four outstanding numerical campaigns have been replayed at their exact source bytes. The full MW campaign additionally has a separate all-cell integration with an independent sieve and no author-module import. [VALIDATION.md](VALIDATION.md), [EXECUTION.json](EXECUTION.json), [FILES.tsv](FILES.tsv) and [IMPORTS.md](IMPORTS.md) state exactly what was checked and what was not. All original producers copied under `sources/` retain their exact bytes; the stricter accepting wrapper is new review code.

The principal review at `37ea752b07700c7ba76335ba082cb6993caca35f`, its earlier predecessors, the earlier local handoff, and the closing confirmation remain historical evidence. This packet starts from review head `f3ba1a2bd3d925ab5caf3a0a3719392b7c5497d8`. It does not retrospectively change any earlier execution or coverage claim.

The handoff supports preparing a separate integration branch from **then-current main**, applying the exact repairs, keeping classical and RH-conditional inputs beside the affected statements, and using only the selected numerical evidence as trusted certificates. Other original programs may be preserved as exploratory artifacts, not silently accepted. The existing cumulative account—including older Robin, SHARP, fixed-prime, wavelet, xi, heat, and L-family results—must remain intact. A review of the resulting integration tree and separately authorized merge are still distinct operations.

## Reproduce

Run these commands from this directory. Python 3.13.5 on Linux was used here; no third-party Python package is needed.

```sh
python3 -I -S -B verify_packet.py
python3 -I -S -B replay.py --packet FR --expect evidence/fr-normal.json
python3 -I -S -B replay.py --packet CD --expect evidence/cd-normal.json
python3 -I -S -B replay.py --packet MW --expect evidence/mw-normal.json
python3 -I -S -B replay.py --packet SSQ --expect evidence/ssq-normal.json
python3 -I -S -B independent_mw.py > /tmp/riemann-mw-independent.json
cmp evidence/mw-independent-normal.json /tmp/riemann-mw-independent.json
python3 -I -S -B test_replay.py > /tmp/riemann-replay-tests.json
cmp evidence/replay-tests-normal.json /tmp/riemann-replay-tests.json
```

Repeat the mathematical commands with `-O`; the recorded complete outputs are identical. `verify_packet.py` authenticates the packet inventory only. A pristine `replay.py --expect` command also performs the entire selected mathematical reconstruction. `--emit` is explicitly a reconstruction mode, not an arbitrary-certificate acceptance shortcut.
