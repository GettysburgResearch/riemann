# Hostile reconstruction of PRs #565 and #566

See `IDENTIFIER_MIGRATION.md` for the transparent collision-avoidance mapping
from the author packet's `97500` namespace to this repository's `97610`
namespace and for PDF/replay provenance.

This standalone manuscript reconstructs both full factor-67 proposals, including imported source, Target-Lorenz, parity, Mellin, and Landau components.

Verdict:

```text
PR #565 complete proof: no
PR #566 complete proof: no
repaired finite-P61 bias: 1/42
finite scalar Lorenz primal/dual: exact
uniform CPSL67: open / RH-bearing
Riemann Hypothesis: unproved
```

Build:

```bash
./build.sh
```

The PDF is reproducibly built with a frozen `SOURCE_DATE_EPOCH`; the Markdown proof is a readable companion to `main.tex`.
