# Sources, mathematical imports, and review scope

## Exact repository source

Repository: GettysburgResearch/riemann.
Parent PR: 805.
Parent branch: research/astra/20260906-dilation-observability.
Parent commit: 032c92e540202d1c409974c0c7b43130d684bfed.
Original main base: 051808c1f8367b4320c52f94b40908eb2173d622.

The parent PR metadata and exact proof were freshly read. The source-code
blob identities were independently returned by the authenticated GitHub
contents endpoint at that commit:

```
scripts/intervals.py  54e216c0ef0bb52913cee86387e0e838d062b3c2  6922 bytes
scripts/replay.py     87e66bacc507bae4dee3a4b6b288056aebcd1844 15375 bytes
```

Local Git-blob hashes match those identities. SOURCE_LOCK.json gives the
SHA-256, Git blob, size and path of each consumed parent source. The checker
also binds the parent proof and numerical-remainder note. No publication
claim is inferred solely from a file name or a PR body. The code does not
load an external zero table or a fitted expected Gram.

The parent proves the finite dilation identity, strictly positive original
Gram, exact Schur update and the conditional gain-to-RH implication. Its
unchanged interval implementation computes positive-real digamma values
with explicit Euler–Maclaurin remainders and outward dyadic arithmetic.
Those analytic remainder proofs were read and are inherited explicitly,
not replaced by high-precision agreement. The new proof reconstructs every
additional parity, Jordan and coupling identity.

## Classical literature

1. Luis Baez-Duarte, *A strengthening of the Nyman–Beurling criterion for
   the Riemann Hypothesis*, arXiv:math/0202141v2 (2002), published 2003.
   https://arxiv.org/abs/math/0202141
   The integer approximation criterion is classical. The exact step-space
   formulation used here is also stated in source 2, Proposition 10.

2. Michel Balazard, *An arithmetical function related to Baez-Duarte's
   criterion for the Riemann hypothesis*, arXiv:1812.04309v1 (2018).
   https://arxiv.org/abs/1812.04309
   The parsed paper and relevant page images were read, including the
   projection notation and Vasyunin dual system. The parent uses this
   source for its step-space setup. No solution of the paper's spectral
   synthesis questions is claimed here.

3. Sandro Bettin, J. Brian Conrey and David W. Farmer, *An optimal choice
   of Dirichlet polynomials for the Nyman–Beurling criterion*,
   arXiv:1211.5191v1 (2012).
   https://arxiv.org/abs/1211.5191
   The abstract and hypothesis boundary were checked. Its result assumes
   RH and a bound on inverse squared zeta derivatives at zeros. It is not
   an unconditional premise here; neither its finite polynomial problem
   nor its asymptotic is silently identified with a bound on differences
   of our finite squared distances.

4. Classical gcd/Jordan matrix factorization and divisor-poset Mobius
   inversion are reconstructed in full in PROOF.md, rather than claimed
   as a new theory. Relevant background includes Guillot and Wu,
   *Total nonnegativity of GCD matrices and kernels*, arXiv:1901.01947.
   https://arxiv.org/abs/1901.01947
   The power-two factorization needed here is proved directly, not
   imported from a total-nonnegativity assertion.

The weighted two-point variance identity, orthogonal projections, Schur
complements, Euler products at absolute convergence and Jordan totients
are standard. No external novelty or priority is asserted for this
synthesis. The all-scale detail theorem needs neither PNT nor RH. The
original all-scale source-complete gain remains open.

## Execution and independence boundary

The three fixed exploratory numpy midpoint calculations that motivated
this continuation were non-directed and are not proof evidence. They were
replaced by the deposited outward-interval reconstruction. No broad
parameter, conductor, prime or zero campaign was run. No Lean or other
proof-kernel build, fresh external zero verification, remote CI success,
or non-author mathematical acceptance is claimed.
