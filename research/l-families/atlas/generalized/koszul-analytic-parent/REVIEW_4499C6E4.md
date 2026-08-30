# Independent review: mixed-rank Koszul parents and canonical regularization

Reviewed commit: `4499c6e44d425b6e43fbf004f2750123a9b20c31`.
Reviewer: independent `recent_landscape` agent, 2026-08-31.
Scope: the five-file mixed-rank/regularization companion under
`research/l-families/atlas/generalized/koszul-analytic-parent/`.
The later critical-boundary companion is not part of this review.

Conclusion: no blocking mathematical or replay defect was found. The source
construction extends to every nonempty finite positive-rank list; the sharp
Schatten disks, regularized determinant formula, and necessary counterterm zero
are proved with their stated hypotheses. Regularization is not misidentified
with scalar recovery or with a global arithmetic completion.

## Evidence and execution boundary

I read the complete proof, producer and nineteen tests, including the two
independent infinite-tail estimates, and checked that the reviewed working
files had no difference from the frozen Git commit. The proof's bound normalized
hash is `9d8b635fd87fbb61b50c29e20b3af5c5217c6d34b4f56224ff164e4b1e357ae7`.

Root reports successful Ruff, ordinary and optimized producer checks, nineteen
ordinary and nineteen optimized tests, and the final hypothesis/document hash
regeneration. I did not independently execute those jobs; root serialized the
shared-machine workload. I independently verified the proof, code logic,
precursor root theorem, and regularized-determinant references.

## Source growth and operator domains

The iterated Segre algebra, its quadratic dual and odd-generator Lie
superalgebra are specified before the scalar Hilbert series. Iterating the
same Koszul and equivariant PBW imports gives the actual modules M_n and the
signed character product. Rank-one factors have their natural representation
action even though they do not change the dimensions.

I reread the frozen unequal-Segre-root theorem at
`8834fdc7a0dfe15f6bb95eefe0729cb77c93c807`. Its differential recurrence and
interlacing argument provide exactly the simple negative Hilbert roots imported
here. For every nonexceptional profile, the new first-coefficient inequality
`h_1>d` correctly forces the largest reciprocal root R to exceed one; simplicity
makes it unique. The Möbius-inversion proper-divisor bound then proves
`epsilon_n ~ R^n/n`. The two finite exceptions and their actual zero tail follow
from uniqueness of the signed Euler exponents, not a sampled tail.

For unitary inputs the singular values remain the intrinsic block values
`|t|^n`. Consequently the Schatten domain is exactly `|t|<R^(-1/p)`, with
harmonic divergence at every boundary point. Ordinary determinant recovery
holds on the trace-class disk and gives a common zero-free disk. The identity
input has a simple zero at its negative boundary, proving sharpness.

## Regularized determinant and counterterm audit

The definition of det_p uses the same source operator and deletes the first
p-1 powers of each logarithm. The trace-class remainder and local uniform
convergence are justified directly from the block estimates. Both parity
determinants are holomorphic and nonzero on the full strict S_p disk because
the block norms remain below one.

The Adams/Möbius sign was independently derived. Substituting the source
primitive character into the retained block powers gives coefficient
`sum_(k|l,k>=p) mu(l/k) = -a_p(l)` for l>=p. This proves the stated negative
sign in the transformed logarithm. On the enlarged disk every argument t^l
lies inside the ordinary zero-free disk. The bound `|a_p(l)|<=p-1` and a
uniform small-argument logarithm estimate give locally uniform convergence;
analytic continuation therefore does not conceal a divergent regrouping.

The multiplicative counterterm is uniquely fixed by its initial germ and
`F_g/D_(p,g)`. It is holomorphic on the larger disk, but at identity it has
the simple zero at -rho. Therefore it cannot be an everywhere nonvanishing
exponential of a holomorphic additive counterterm. The logarithmic derivative
has the correct integer residue and monodromy at each zero. No divergent
lower trace power is assigned an ordinary operator trace outside its domain.

The result is stronger than merely saying that a scalar function continues:
it identifies a source-compatible regularization and its precise recovery
obstruction. It does not turn the scalar zero into an eigenvalue-one event
for the compact operator, whose norm there is rho<1.

## Exact controls and references

The producer authenticates the frozen executable and proof before importing
the low-degree Lie construction, and the payload also binds the earlier
all-rank root theorem. Two independent Hilbert numerator constructions agree
on the declared profiles. The regularized Adams control uses actual source
Lie grades one through three; those suffice through degree 3p because the
first retained block power is p. It is not a fitted high-grade diagonal model.

Both rational logarithm enclosures have valid infinite-tail guarantees. The
direct estimate bounds the omitted grade tail and power tail separately;
double-counting the corner is harmless. The Adams estimate bounds each scalar
logarithm tail and the omitted Adams indices. All denominators are positive
in the stated strict S_p domain. Their overlap at points outside trace class
is honestly a finite falsification check backed by these estimates, not a
numerical proof of the exact identity.

The tests cover finite exceptions, rank-one invariance, a held-out rational
unitary input, the first regularized sign, the scalar zero, larger-order
domains, bounds/types, source authentication and a forged fixture. Canonical
JSON comparison preserves exact numeric types; no acceptance check relies on
Python `assert`.

The standard determinant convention was checked directly in Britz et al.,
[The product formula for regularized Fredholm determinants](https://arxiv.org/abs/2007.12834),
Section 1, equation (1.3), and Kostenko,
[Trace Ideals with Applications](https://users.fmf.uni-lj.si/kostenko/teach/IdealsNotes.pdf),
Section 3.6, especially Remark 3.6.1. The proof correctly avoids assuming
ordinary multiplicativity for regularized determinants.

No external priority, prime-indexed family, conductor, gamma factor,
functional equation, or arithmetic RH consequence is established. Finite
regularization order does not reach the compactness boundary. These limits
remain explicit in the frozen companion.
