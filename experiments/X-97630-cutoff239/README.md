# X-97630 cutoff-239 replay

The lightweight replay checks:

- the `x=184` refutation;
- the exact cutoff `239`;
- low-child pre-observation recombination;
- the strict `1/960` contraction arithmetic;
- the PR #566 reserve/complement countermodel;
- zero-safe finite Mellin multipliers;
- ten hostile mutations.

The included C++ is also a lightweight reconstruction: it checks the `x=184`
witness and endpoints `67..238`, but does not execute the reported sweep to
`2,500,000` and does not implement the analytic tail. Neither replay proves the
all-real cutoff theorem or RH.
