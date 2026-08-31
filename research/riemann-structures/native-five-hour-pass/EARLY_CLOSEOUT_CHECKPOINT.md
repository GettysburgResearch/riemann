# Early closeout: source geometry and Architecture E

Status: reviewed checkpoint, closed early at the user's request on
2026-09-01. RH remains unproved.

This pass kept PRs #782 and #783 as frozen synthesis dependencies. It
advanced two coupled questions on PR #770: what the literal native source
permits in its original metric, and how far the Hermite--Stieltjes safe-axis
programme can be proved without assuming its RH-equivalent endpoint.

## Native source geometry

For the fixed primes \(2,3,5\), the literal twenty occupation coordinates
have a positive infinite-horizon physical Gram matrix:
\[
 \frac1{12\,000\,000}I\preceq G_\infty\preceq68I.
\]
Together with exact finite coverage and a quantified physical tail, this
proves rank 20 for every integer \(H\ge450\), with
\(G_H\succeq I/48\,000\,000\) for \(H\ge2^{48}\).

This does not extend uniformly to varying prime sets. For two primes
\(p,q\) with \(q/p\to r\), the normalized three-coordinate Gram has an exact
limit: positive for \(r>1\), rank one at \(r=1\), and tending to
\(\nu_0I/2\) as \(r\to\infty\). Near collision its two small eigenvalues
are linear in \(h=\log(q/p)\), with slopes
\[
 144+64\sqrt2,\qquad72+32\sqrt2.
\]
The normalized difference directions concentrate in translated detector-edge
packets and converge weakly, but not strongly, to zero. Since consecutive
prime ratios approach one, coordinatewise rescaling cannot supply a uniform
all-prime frame.

The earlier \(w\)-last optimum is strictly beaten by a legal terminal
variation, and each registered linear dual potential \(K=1,2,3\) fails an
exact support inequality. A nonlinear source-owned potential succeeds:
\[
 \Phi=\theta_{10}u^2v+wR-3u^2w(1-v).
\]
At the certified root
\[
(-.0823330570,1.1226168381,-.5082335933,.5775184400,.9383761444),
\]
the resulting ordered two-arc path, including vertical completions, is a
global minimizer over every completed coordinatewise monotone path in the
original infinite \(L^2(\nu)\) norm. Infinite-frame positivity makes its
observed twenty-vector unique.

The first implementation omitted the lower clipped branch and is preserved
as an invalid artifact. The repaired producer splits that branch, corrects
two underdeclared polynomial degrees, uses exact calibrated factors, and
passes continuum inequalities. The result is deliberately labeled
**post-registered**: the preregistration's final sentence demanded Sturm
isolation, while the exact proof used its earlier-permitted Bernstein route.

The optimizer theorem is only for the fixed three primes and declared twenty
coordinates. It does not prove finite-horizon persistence of the same support
type, uniqueness of a parametrized path, a varying-prime result, or survival
through the retained-gamma/native decoder.

## Architecture E: proved regions and exact frontier

Put
\[
Y(x)=\xi(1/2+x),\quad F=Y'/Y,\quad
H(x,y)=\frac{F(x)+F(y)}{x+y},\quad C(x,y)=\frac1{x+y}.
\]
The pass proved these replayed source-exact regions, including confluences:

- at most four nodes \(x_i\ge256\): \(H\succeq C/4\);
- one node in \([1/2,256]\) and up to three at least \(2^{30}\):
  \(H\succeq C/100\);
- two nodes in \([32,256]\) and two at least \(2^{40}\):
  \(H\succeq C/50\);
- three nodes in \([64,256]\) and one at least \(2^{34}\):
  \(H\succeq C/200\).

A separate proof-only packet derives the growing-order statement
\(H\succeq C\) for arbitrary order \(n\) when every node is at least
\(16\cdot3^n\). Its source note retains its own review boundary and is not
used to strengthen any fixed-height all-order claim.

The algebraic exponential-core operator is well defined and dense. Extending
it as a globally closable \(F(A_0)\) is itself an RH-sensitive domain claim;
it cannot be inserted as a harmless functional-calculus premise.

A preregistered 1,911-packet scout found every registered four-node packet
positive at 100/200 digits. Its hardest case is fourfold confluence at
\(x=1/2\), with relative eigenvalue about
\(1.0365420536\,10^{-11}\). This is finite reconnaissance only.

At that endpoint the exact signed four-jet Gram depends only on
\(f_r=F^{(r)}(1/2)\), \(0\le r\le3\), and its determinant factors as
\[
 D_4=A_-A_+.
\]
The explicit odd/even forms are in ENDPOINT_FOUR_JET_FACTORIZATION.md. The
smaller numerical factor is about \(3.8367\,10^{-15}\). The factorization is
exact, but its transcendental signs have high-precision evidence rather than
outward interval proofs. There is no endpoint sign theorem, local
neighborhood theorem, all-moderate four-node theorem, or RH conclusion.

## Ranked continuation

1. Enclose \(\gamma_0,\ldots,\gamma_3\) and prove the endpoint signs; then
   enclose higher derivatives on a declared neighborhood.
2. Prove perturbative stability of the nonlinear optimizer and combine it
   with the physical tail to obtain an explicit finite-horizon optimizer.
3. Reconstruct one complete retained-gamma/native tuple through owner,
   carrier, colour and renewal aggregation before transporting the optimizer.
4. Treat prime collision as a renormalization problem; do not seek a uniform
   all-prime frame by diagonal coordinate scaling.

The untracked compact-two-low bootstrap and the ordered/dual/mixed discovery
scripts remain exploratory working material. They were deliberately excluded
from the reviewed checkpoint. The invalid quadratic output is different: it
is committed on purpose as provenance for the caught lower-clip failure and
is explicitly rejected by the accepted producer.
