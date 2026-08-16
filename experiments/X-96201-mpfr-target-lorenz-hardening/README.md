# X-96201 true-MPFR Target–Lorenz tail hardening

The frozen PR #508 event reducer is extracted by commit SHA. Every interval
`sqrt` and `log` call is rewritten to MPFR 256-bit outward rounding.

Local smoke:

```bash
g++ -O2 -std=c++17 smoke.cpp -lmpfr -lgmp -o smoke
./smoke
```

Full producer:

```bash
sudo apt-get install -y libmpfr-dev libgmp-dev
python3 rewrite_and_run.py --workers 4
```

The full 65-row artifact is mandatory before accepting the imported numerical
tail. The smoke test only proves that irrational values receive non-singleton
outward enclosures.
