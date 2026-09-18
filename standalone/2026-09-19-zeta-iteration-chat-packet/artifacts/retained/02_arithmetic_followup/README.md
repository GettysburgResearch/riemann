# RH arithmetic follow-up package

Start with `RESEARCH_NOTE.md`. It contains the definitions, proofs, source
attribution, certificate method, and the precise unproved RH step.
No RH proof, new zero-free region, or literature-priority claim is made.

## Reproduce

Python dependencies: numpy, scipy, numba, threadpoolctl, mpmath.
The exact versions used are recorded in `results/environment.json`.

From this directory:

```sh
python rh_gram_followup.py --max-n 2048 --cert-n 0 --out-dir new_results
python verify_saved_certificate.py results/certificate_N1024.json
python check_identities.py
```

The first command is floating-point exploration with independent formula and
Schur checks. The second verifies the saved exact rational witness and encloses
the exact optimum without doing a floating-point solve. It uses the analytic
conditioning lemma in the research note. The third performs small numerical
consistency checks; these are not a substitute for the proofs.

`refine_certificates.py` recomputes candidates and interval certificates at
N=256,512,1024. It writes into this package's results directory. For preservation
of original files, run it in a copied directory.

The largest completed certificate proves D<0.00327777. The full floating table
reaches N=2048; that final row is explicitly not interval-certified. Certificate
files store all rational coefficient numerators, outward intervals, precision,
and the optimum-error correction.

These are interval-arithmetic computational certificates, not Lean/Coq/Isabelle
formalizations. No GitHub repository has been modified by this work.
