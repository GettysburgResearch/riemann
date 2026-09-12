# HBR28 — exact hyperbolic renormalization and the cutoff law

**Status: proposed component proofs; independent review required. RH is not proved.**

This is a new, add-only research contribution continuing the Brownian modes of PR #856. It does not restore the refuted phase condition of #846. It also records how the newer gamma-defect, branching-height, and Ising work changes the choice of a next proof strategy. The reviewed source versions are frozen in `SOURCES.json`; their author checks were not rerun or silently accepted.

## The constructive results

For the unchanged source `L(t)=sqrt(6t)/sinh(sqrt(6t))`, the linearization is

    T f(t)=2 integral_1^2 L(t/u^2)f(t/u^2)du.

The change `r=sqrt(6t)`, `x=tanh(r/2)`, `f=r*g(x)` gives exactly

    A g(x)=2 integral_(h(x))^x g(y)dy/y,
    h(x)=tanh(atanh(x)/2).

On every specified analytic Wiener space of radius `0<R<1`, its nonzero spectrum consists precisely of the simple eigenvalues `2a_m`, where `a_m=integral_1^2 u^(-2m)du`, `m>=1`. The proof includes the entire infinite complement and an explicit resolvent-tail bound. These are perturbation eigenvalues, **not parameters of xi zeros**. A bounded eigenbasis or metric is not asserted. The same nonzero eigenvalue list is universal for normalized analytic source multipliers; the paper proves this too. It therefore carries no arithmetic zero-exclusion information by itself.

A solvable positive comparison replaces the bounded rescaling law by its Pareto extension. For each `m>=1`,

    Ptilde_m(t)=[2tanh(sqrt(6t)/2)/sqrt(6t)]^(2m-1).

The true and comparison perpetuities have the exact Wasserstein distance

    delta_m=3 epsilon_m(4m^2-1)/[16-(12m+10)epsilon_m],
    epsilon_m=2^(1-2m).

More strongly, the true mode has an **exact survival factor**:

    P_m(t)=Ptilde_m(t) Pr(T_m>t),  t>=0.

The paper gives a positive density for `T_m`, proves its full normalization and the ratio's strict decrease from one to zero, and expresses the actual companion as a positive mixture of explicitly truncated comparison integrals. This is not a finite-level perpetuity approximation.

The entire comparison companion is a finite, explicitly triangular combination of

    R_j(s) xi(s+2j),  0<=j<m,

with all coefficient cancellations supplied. Thus the probabilistic operator and the arithmetic-shift representation are linked exactly, not only numerically.

## Where the attack stops

A positive operator spectrum is not a proof about xi's zeros. The native transformed kernel has a rational negative 3-by-3 minor `-512/25`, so it is not totally positive of all orders. The first closed comparison is `(2/3)(2^(-s)-1)xi(s)`, which shares xi's zeros and has a phase that changes sign. Finally, a positive mixture of truncated Mellin integrals does not automatically preserve real zeros. The full signed complex estimate for the literal cutoff mixture is still missing.

The exact whole-source comparison, the named-space spectral completion, and the arithmetic-shift identity are the proposed progress. None is promoted to RH or external novelty. Read `PROOF.md`, especially (14)–(16), (25)–(26e), and (27)–(35).

## Reproduce

No third-party package is required for the exact checks:

```sh
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

Both executed modes reconstruct **4,243 bounded rational checks**, with digest

    c3253680f4b938259b08b8d2fc54ecb290a09ef36116d21da650f929026232d1

and reject six altered receipts plus duplicate-key JSON through the actual comparator/parser. These tests check finite algebra, not the infinite analytic proofs or RH.

Optional, NONCERTIFYING numerical identities use mpmath:

```sh
python diagnostic.py --dps 70 --out /tmp/hbr28-diagnostic-70.json
python diagnostic.py --dps 90 --out /tmp/hbr28-diagnostic-90.json
```

Both precisions were executed. Each compares 18 complex defining integrals with the shifted-xi formula, six removable coefficients, and six integer normalizations. No directed rounding, proved quadrature remainder, root count, or independent backend is claimed. See `VALIDATION.md` and `EXPLORATION.md` for failed/discontinued scouts and exclusions.

## Publication status

Prepared against main `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
**No new remote branch, commit, review comment, or PR was created in this session.** The available GitHub connector exposed 48 read actions but no write action; provider discovery found only the already-installed connector, and no usable authenticated CLI write path was available. The accompanying add-only patch is the publication handoff, not evidence of a remote push. Main and all existing research files remain untouched.
