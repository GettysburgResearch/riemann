# DPG26 — stable inversion of the actual divisor graph

**Proposed component proofs, independent review pending. RH is not proved.**
This is an add-only research contribution, not an integration or review verdict.

The complete prime-power Laplacian in PR #790 already has a sum-of-squares
identity. This packet supplies its missing quantitative inverse estimate:

\[
 L_S\succeq\frac1{24r_S}(I-\Pi_S),\qquad
 \|L_S^\dagger\|\le24r_S,
 \quad r_S=\max_{n\in S}\omega(n),
\]

for **every finite divisor-closed support S**, with every native prime-power
edge retained and only the known harmonic null vector removed. Values may be
in any complex Hilbert space. Here omega counts distinct primes.

For S={1,...,N}, the inverse cost is at most 24 log(N)/log(2), and more sharply
O(log N/log log N). For arbitrary divisor-closed supports on {2,3,5}, the gap
is at least 1/6 regardless of exponent depth or number of vertices. These are
unconditional paper theorems, not extrapolations of the bounded tests.

## Mechanism and usable consequences

Remove each vertex's LEAST prime factor to its full power. Path length is
omega(n), not the total number of prime factors. An edge ending at a receives
harmonic mass at most a^-1 times the finite Euler product on smaller primes.
An elementary Markov/factorial argument bounds that product by 24 log p,
which is paid by the ORIGINAL log p conductance.

The proof gives an explicit tree-gradient decoder, a full-source Poisson
iteration with a proved convergence bound, exact one-prime and finite-box
spectra, and a priced one-mode Schur reduction for perturbations satisfying
an explicit complement bound. The graph cusp estimate in #790 receives an
additional non-harmonic coercive term at its original mean-zero window scope.

This does NOT show that an arbitrary physical observation retains the required
tree edges, bound a signed perturbation of the graph, control unrestricted
window means, or identify the graph with the full Weil or xi operator.
Divisor closure is essential. Rectangular tensor spectra are not silently
applied to n<=N. No uniform all-N spectral gap is asserted.

Read [PROOF.md](PROOF.md), then [REVIEW_AND_SOURCES.md](REVIEW_AND_SOURCES.md)
and [VALIDATION.md](VALIDATION.md). The source lock records exact repository
inputs, not an executed parent suite.

## Replay

```sh
python -I -S -B check.py
python -I -S -B -O check.py
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

The standard-library checker uses exact fractions and directed rational
logarithm bounds. It compares two factorizations and two graph reconstructions,
checks selected matrix inequalities by exact LDL, and verifies the stated
finite spectra. Its finite coverage is not a proof of infinite quantifiers.
