# Nakamura–Suzuki zeta-screw source lock — 2026-08-11

## Primary sources

1. Takashi Nakamura and Masatoshi Suzuki, **On infinitely divisible distributions related to the Riemann hypothesis**, *Statistics & Probability Letters* 201 (2023), 109889.  
   DOI: `10.1016/j.spl.2023.109889`  
   arXiv: `2306.08317`  
   Version inspected online on 2026-08-11: arXiv page reporting version date 2026-03-22.

2. Masatoshi Suzuki, **Aspects of the screw function corresponding to the Riemann zeta-function**, *Journal of the London Mathematical Society* 108 (2023), 1448–1487.  
   DOI: `10.1112/jlms.12785`  
   arXiv: `2206.03682`.

## Imported statements

The local files import only the following source-level facts:

- the explicit even function `g_zeta`;
- the equivalence
  ```text
  RH <=> exp(g_zeta) is an infinitely divisible characteristic function;
  ```
- under RH, the Lévy measure
  ```text
  sum_gamma m_gamma/gamma^2 delta_gamma;
  ```
- the zero expansion
  ```text
  g_zeta(t)=sum_gamma m_gamma (exp(-i gamma t)-1)/gamma^2;
  ```
- the one-sided Fourier/Laplace identity relating `g_zeta` to `xi'/xi`;
- Suzuki's screw-kernel criterion: RH is equivalent to positivity on all compact smooth mean-zero tests;
- the unconditional growth bound used to place the new rational Hardy tests in a weighted form domain.

## Local additions

The following are local to `gfreund123/riemann` and are **not** claims of the cited authors:

- the exact bosonic Fock realization of the generalized-Jordan kernel;
- the radial prime-power birth process;
- localization by the causal Cauchy spectral factor of `L-91026`;
- the exact admissibility constant `(15/16) log 2`;
- the two-Hardy-channel cross-Gram;
- the one-fixed-safe-scale form-core theorem;
- the fixed-scale RH criterion `T-91006`;
- the Poisson-chaos/Stinespring completion target.

No source or Lean verification status transfers automatically to these local additions.  All are marked for independent review, and RH remains unproved.
