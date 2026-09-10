# Reciprocal gamma research: test the flow, then remove its deterministic bias

**Status: PROPOSED component proofs and two complete finite-source root
certificates. Independent mathematical/code review required. RH and asymptotic
zero confinement remain OPEN.** This is an add-only continuation of PR #849,
not a modification of main, its integration candidate, or an accepted theorem.

## What this pass actually obtains

The original positive gamma flow is not critical-strip zero-preserving. The exact
u=7/10 point of its second-to-third step has one simple zero in the radius-10^-6
disk about **26.8135855368140614+0.4209949404628030i**. The earlier N4 nonreal root
is now certified too. These are finite approximants, NOT xi zeros. The numerical
proof uses every quadrature cell, an analytic complex-disk remainder and the
entire real-line tail; it is not agreement of two high-precision scouts.

A constructive repair retains the mean of the omitted tail. Let

    X_N=sum_(n<=N)G_n/n^2,  G_n~Gamma(2,1),
    tau_N=2 sum_(n>N)n^-2,  Xhat_N=X_N+tau_N.

Take its density g_N and the reciprocal projection
sqrt(g_N(pi exp(2t))g_N(pi exp(-2t))). Its normalized Fourier transform Fhat_N has
nonnegative even source, compact support |t|<log(pi/tau_N)/2, and the proposed
complete-source bound

    sup_(|Im z|<=R) |Fhat_N(z)-Xi(z)/Xi(0)| = O_R(N^-3).

Every real frequency and both omitted reciprocal tails are covered. The proof
uses a convergent differential deconvolution and the actual Jacobi reciprocal
identity. No fitted parameter, signed extrapolation or numerical zero enters
the construction. Constants are explicit but deliberately large.

The same argument validates the original cascade's translation model with
O_R(N^-3) residual error and identifies its O(N^-1) leading drift by exact xi
values shifted into the safe Euler half-plane. This is not a theorem that the
shift operator preserves real zeros.

**The remaining estimate is spectral, not a convergence gap:** exclude persistent
nonreal zeros in an expanding window of this prescribed centered family. The
complete conditional implication to RH is in PROOF.md §8. A separate scout
suggests a centered N5 nonreal zero as well, so global real-rootedness of every
finite centered stage is not assumed. That centered scout is not certified.

## Read and reproduce

Read [PROOF.md](PROOF.md), especially §§3, 4--7 and 8. The classical BPY source
and exact predecessor are in [SOURCES.json](SOURCES.json). The original parent
files are byte-preserved. Source uniformity, zero-confinement and finite tests
are not conflated.

From this directory:

```sh
python -I -S -B check.py --expect results.json
python -I -S -B -O check.py --expect results.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Every pristine accepting command freshly reconstructs both complete certificates.
Use `--emit /outside/packet/result.json` only as producer mode. The accepting
implementation uses standard-library integers/Fractions with outward 512-bit
intervals, not a numerical special-function oracle. The optional mpmath scout
is separate: `python -B scout.py --output /outside/packet/scout.json`.

[VALIDATION.md](VALIDATION.md) records what ran, the tests' actual scope and the
unperformed full-checkout/Lean/CI/parameter-continuation work. A self-contained
implementation is not an independent referee or an all-order theorem proof.
