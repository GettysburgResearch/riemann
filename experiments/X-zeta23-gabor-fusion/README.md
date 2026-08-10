# X-zeta23-gabor-fusion

Finite numerical regression for two exact proof notes:

1. `COHERENT_MULTIWINDOW_COLLAPSE.md`;
2. `OFFLINE_PAIR_SPECTRUM.md`.

Run:

```bash
python3 experiments/X-zeta23-gabor-fusion/verify.py
sha256sum -c experiments/X-zeta23-gabor-fusion/SHA256SUMS
```

The cyclic coherent-window test constructs four fully mixed complex windows, an arbitrary Hermitian physical operator, and verifies:

```text
S_multi=S_scalar U,
U U*=I,
G_multi=U*G_scalar U,
```

including equality of the nonzero spectrum and trace powers one through four.

The off-line test uses the rectangular window, truncates the analytically continued Shannon sums at 30,000 lattice points on each side, and compares them with

```text
sum |hat psi(z-tau_k)|^2=L sinh(yL)/y,
sum hat psi(z-tau_k)^2=L^2,
```

then verifies the normalized hyperbolic eigenvalues

```text
1+sinh(yL)/(yL),
1-sinh(yL)/(yL).
```

The experiment tests algebra and normalization only. It does not establish the analytic finite-height tail theorem, a global no-cancellation theorem, or RH.
