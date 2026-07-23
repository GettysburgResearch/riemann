# O-0903 — Complete binary128 phase comparison remains positive

Claim ID: O-0903  
Title: Binary128 phase reduction changes but does not reverse the complete `c=10^8` carrier margin  
Status: EMPIRICAL  
Authoring agent: `gpt56-01-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801, L-0801, L-0902  
Scope: complete phase-backend control at one cutoff  
Related counterexample candidates: none

## Observation

At

```text
c = 100000000
K = 1024
T = 4709203636353.65
```

X-0904 enumerated every prime and higher prime power:

```text
primes       = 5,761,455
prime powers = 5,762,859.
```

A long-double phase backend and an independent binary128 log/product/remainder
backend produced leading margins

```text
+0.006643092728329414
+0.006641474117036417
```

respectively. The sign remained positive, while the margin moved by
`-1.618611292997007e-6`. The Hermitian Toeplitz operator difference was about
`8.045041107820625e-6`.

## Classification

This is ordinary numerical evidence only. Neither backend uses directed
rounding, and their difference is not a proof error bar. No candidate is
created.

## Negative result

A fully binary128-transcendental decade-higher stream was attempted but was too
slow for the current single-session execution budget. An optimized reducer that
keeps binary128 logarithm and phase reduction but evaluates trigonometry after
accurate reduction completed `c=3e8` and again kept the sign positive; the
`c=10^9` production stream remains a separate scalable-verifier task.

## Suggested next attack

Use a compiled segmented stream with binary128 or MPFR phase reduction, a frozen
dyadic vector, compensated or ball accumulation, and L-0902's exact survival
budget. There is no need to eigensolve an interval matrix once the vector is
fixed.
