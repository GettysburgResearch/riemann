# X-105300 — Low-order Levinson–Hermite–Pick exact replay

This standard-library replay checks:

- quotient-algebra construction of `q=-p/(p'') mod p'`;
- exact Hermite trace-form matrices;
- inertia for all-real, mixed, and zero-real-root fixtures;
- polynomial preconditioning by exact congruence;
- compressed-matrix rank--trace lower bounds against the full root count;
- the exact all-real `16/25` coherence firewall;
- the `0.86864`, `0.67250`, `77057/86864`, and `0.694912` record arithmetic.

It does not evaluate Xi, run a zero scan, prove the asymptotic matrix estimate,
beat the record, or prove RH.
