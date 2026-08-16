# Native Factor-67 Compiler — arXiv-ready proposal v1

This bundle contains:

- `native-factor67-proposal-v1.pdf` — compiled manuscript;
- `source/main.tex` — LaTeX source;
- `source/build.sh` — build script (`latexmk -pdf`);
- `THEOREM_LEDGER.md` — dependency and proof-status map;
- `PR_BODY.md` — proposed pull-request description.

## Build

```bash
cd source
./build.sh
```

## Scientific status

This is a conditional proof proposal and adversarial audit. It does **not** claim that the Riemann hypothesis has been proved. The main theorem is conditional on `Cert_67`, whose Target–Lorenz tail and native-normalization clauses are not currently established by the audited repository state.
