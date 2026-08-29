# Notation

- `RH`: the Riemann hypothesis.
- `c > 1`: prime/support cutoff; exploratory code currently requires `c >= 2`.
- `L = log(c)`.
- `Delta = L/(2*pi)` and `rho = 2*pi/L`.
- `N`: Galerkin half-band.  Full indices are `{-N,...,N}` and dimension is
  `2N+1`.
- `v=(v_0,...,v_N)`: real even-sector coordinates.
- `u_0=v_0`, `u_k=u_{-k}=v_k/sqrt(2)`: full symmetric coefficients.
- `Q_N(c)` or `Q_infty`: cutoff-free finite Weil matrix in normalization
  `D-0001`.
- `g_v`: induced even, entire, band-limited Guinand--Weil test function.
- `Z_zeta^* = {z in C : 1/2 + i z is a nontrivial zero of zeta}`.
- `EMPIRICAL`: ordinary numerical evidence without a rigorous enclosure.
- `certified negative`: an exact or interval proof whose Rayleigh upper endpoint
  is strictly less than zero.
