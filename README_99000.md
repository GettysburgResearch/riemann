# T-99000 — C4MBI67 primitive-prefix reconstruction and billion-endpoint theorem

This packet is a fail-closed continuation of T-97701. It reconstructs every
arithmetic and analytic arrow from the primitive coefficient prefix to RH,
proves the specialized analytic imports inside the manuscript, identifies an
exact weighted-threshold-complex/Bellman formulation, and supplies an outward-
rounded certificate through `10^9`.

It does **not** prove the all-scale primitive-prefix inequality, global
C4MBI67, or RH.

## Fast replay

```bash
cd experiments/X-99000-c4mbi67-primitive-prefix-billion
./replay.sh
```

## Full certificate replay

```bash
cd experiments/X-99000-c4mbi67-primitive-prefix-billion
FULL=1 ./replay.sh
```

The original full replay used about 3.3 GB peak resident memory and completed
in about 25 seconds in the publication container.

## Canonical manuscript

```text
standalone/2026-08-19-t99000-c4mbi67-primitive-prefix-billion/t99000-c4mbi67-primitive-prefix-billion.pdf
standalone/2026-08-19-t99000-c4mbi67-primitive-prefix-billion/main.tex
standalone/2026-08-19-t99000-c4mbi67-primitive-prefix-billion/PROOF.md
standalone/2026-08-19-t99000-c4mbi67-primitive-prefix-billion/THEOREM_LEDGER.md
```

## Repository PDF note

The committed PDF is a deterministic seven-page core-font portability rendering
of the full manuscript. The complete TeX source is committed as a small `main.tex` wrapper plus six
contiguous files under `tex/`; concatenating the six parts reproduces the
retained monolithic source byte-for-byte. Reproducible LaTeX auxiliary files are intentionally omitted from the repository core. The richer LaTeX-typeset PDF is retained in the deterministic
fallback archive under `extras/`.
