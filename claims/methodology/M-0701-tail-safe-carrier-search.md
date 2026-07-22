# M-0701 — Tail-safe carrier search and candidate promotion

Proposal ID: M-0701  
Problem with current process: translated carrier searches can create impressive false negatives when only the largest prime terms are retained  
Proposed change: require complete prime-power reevaluation before a screen is retained, then certify a fixed vector rather than an eigenvalue  
Expected benefit: prevents prime-tail and eigenspace-instability artifacts from entering the candidate registry  
Possible cost or risk: complete sums and certified phase reduction are expensive  
Trial procedure: X-0701  
Success criterion: every retained negative has a complete finite prime sum and a deterministic path to an exact Rayleigh certificate

## Protocol

### 1. Discovery family

Fix exact or reproducibly rounded `L`, carrier `T`, dimension, and basis. Record
the full test-function definition, not only a matrix.

### 2. Partial screening

A weighted prime subset may rank carriers, but its output must be labeled
`TRUNCATED_PRIME_SCREEN`. Never attach a `Z-####` identifier.

### 3. Complete finite reevaluation

Before retaining any sign, enumerate every prime power `q<=c`, prove the list is
complete at the discovery implementation's level, and recompute the leading
matrix with safer phase reduction.

### 4. Full-matrix correction

Evaluate or rigorously bound:

- the negative-frequency sinc branch;
- the exact nonidentity Gram matrix;
- the compact archimedean matrix;
- the pole matrix;
- all rounding and phase errors.

### 5. Fixed-vector extraction

Round the empirical minimizing vector to a low-height dyadic vector. Recompute
the exact quadratic value of that fixed vector. Do not require an interval
eigensolver.

### 6. Exact checking

Export dyadic entry or direct Rayleigh intervals and use a small exact checker.
Acceptance requires an upper endpoint strictly below zero.

### 7. Promotion and review

Only then allocate a `Z-####` candidate. Require an independent analytic
normalization audit and a second implementation before claiming a counterexample.

## Trial result

X-0701 found apparent negative leading eigenvalues using top-prime subsets. Both
representative screens became positive after the complete 665,134-term sum. The
protocol therefore prevented false candidate promotion in its first trial.
