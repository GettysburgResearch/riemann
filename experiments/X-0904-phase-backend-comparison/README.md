# X-0904 — Complete phase-backend comparison

Status: ordinary numerical discovery; no directed rounding.  
Agent: `gpt56-01-c`  
Issue: #42  
Dependencies: D-0801, L-0801, L-0902.

## Question

Is the long-double phase backend accurate enough to support the smallest
complete-prime carrier margins, and what phase radius must a proof producer
achieve after a vector is frozen?

## Exact survival rule

L-0902 proves

```text
||S_approx-S_exact|| <= sum_q Lambda(q)/(pi sqrt(q)) eta_q
```

and the corresponding frozen-vector weighted bound. For the X-0901
`c=10^10` vector, the recorded absolute phase weight is `493.7546104558693`.
After subtracting L-0901's correction budget, a common phase radius below

```text
1.2306921641349523e-6
```

would preserve the recorded positive margin.

## Complete `c=10^8` comparison

The C++ program enumerates every prime power through `10^8` and builds the same
1,024-cell Toeplitz coefficients twice:

1. long-double logarithm, product, and remainder;
2. binary128 logarithm, product, and remainder, with trigonometry evaluated only
   after the accurately reduced phase is converted to long double.

Both paths use Kahan long-double accumulation. The results are:

```text
prime powers                         5,762,859
long-double leading margin           +0.006643092728329414
binary128-phase leading margin       +0.006641474117036417
margin shift                         -1.618611292997007e-6
Toeplitz operator difference          8.045041107820625e-6
```

Both signs remain positive. The backend difference is not an enclosure.

## Reproduce

```bash
g++ -O3 -std=c++17 phase_compare.cpp -lquadmath -o phase_compare
./phase_compare 100000000 1024 4709203636353.65 phase-coefficients.json
python analyze.py phase-coefficients.json --output analysis.json
python phase_budget.py --output results/phase-summary.json
PYTHONPATH=. python -m unittest discover -s tests -v
```

The raw coefficient file is intentionally not committed; regenerate it from the
complete integer stream. The compact analysis and provenance hashes are kept in
`results/`.

## Performance negative result

A straightforward fully binary128-transcendental `c=10^9` stream exceeded the
single-session execution budget. Accurate phase reduction followed by ordinary
trigonometry removes most of that cost, but a production decade-scale verifier
should be segmented, checkpointed, and vector-specific rather than repeatedly
building the full Toeplitz matrix.

## Proof boundary

- binary128 library functions are not treated as directed balls;
- accumulation and eigensolving are ordinary numerical operations;
- the frozen X-0901 vector is not yet an exact dyadic object;
- no candidate is created.
