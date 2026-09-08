# Harmonic endpoint transfer and an exact-horizon scalar test

Status: proposed component proofs; independent review required.
**RH and the required scalar/full-source bounds remain unproved.**
This is an author continuation of PR #805 at
`acb0a25a373b427c9694aff78cba396f26963e8b`.

Read [PROOF.md](PROOF.md) sections 1–2 for the transfer on the unchanged
source, and sections 3–7 for the different terminal-balanced family.
Section 8 states the attempted completion and what was not proved.

The full Green energy of any finite balanced odd source is comparable to
an exactly computable harmonic-step norm:

    sqrt(E) <= sqrt(H) + 4 B;
    sqrt(H) <= sqrt(2 E) + 2 B;
    B = sum |lambda_k|/k.

For rational coefficients, H is exactly a quadratic polynomial in log 2
with rational coefficients. No trigonometric mesh or infinite Gram tail is
needed to evaluate H. In the parent's prescribed family B is logarithmic,
so the transfer preserves subpower growth. It does not prove that growth.

A new terminal-balanced family has lambda_k=mu(k) except at the last odd
index M, where subtracting M*sum_(odd k<=M)mu(k)/k enforces exact balance.
It matches the target on every cell below M. Its coefficient sum is

    Q(M) = sum_(odd k<=M) mu(k)(1-M/k).

The first Green interval is comparable to the rational scalar Q(M)^2/M,
with explicit constants and O(1/M) errors. The Mellin transform of Q is
-1/[s(s-1)(1-2^-s)zeta(s)], so no nontrivial zero can cancel. A proved
interpolation estimate reduces the sufficient all-scale bound to the
predetermined cutoffs M_j=2j^4+1. Subpower Q(M_j)^2/M_j is RH-equivalent.
That arithmetic bound remains OPEN. This does not declare the first
interval of the parent's different optimum sufficient.

The natural-approximation and integrated-Mertens ingredients are classical.
No novelty or priority is asserted. The contribution is the quantitative
harmonic/Green transfer and its source-faithful endpoint and sampling use.
The local-horizon result gives stronger zero-forced full-energy growth for
this new family, but it does not prove a smaller finite approximation error.

## Replay

From this directory, with the unchanged sibling green-energy packet present:

```bash
python -B scripts/replay.py --check
python -O -B scripts/replay.py --check
python -B scripts/test_replay.py
python -O -B scripts/test_replay.py
```

The standard-library checker binds three exact parent files before compiling
its consumed mathcore directly from the authenticated bytes. It reconstructs
1,704 bounded exact/directed controls and records seven small full-energy
panels. Seven unit methods include twelve actual CLI corruption refusals.
The first four scalar grid nodes are computed exactly; no broad campaign is
run, and those finite nodes do not prove the all-scale bound.

All new paths are under this directory. Parent sources, canonical/formal
files, workflows, permissions and main are unchanged. See [VALIDATION.md](VALIDATION.md)
and [SOURCES.md](SOURCES.md) for the analytic and execution boundaries.
