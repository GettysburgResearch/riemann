# Joint conductor and theta research packet

**Status:** proposed, separately reviewed research combining the frozen [PR #914](https://github.com/GettysburgResearch/riemann/pull/914) and [PR #915](https://github.com/GettysburgResearch/riemann/pull/915). This packet proves a sharper residual reduction for each fixed higher moment and an exact arithmetic bridge between the two completions. It does not prove the full fourth moment, the boundary \(17/24\), a cofinal moment hierarchy, a shrinking zero band, or RH. The earlier source-conditional boundary \(139999/160000\) is unchanged.

**Scope:** actual inverse coefficients over the Eisenstein field; literal character zeros and moving exclusions; fixed moment order and smooth tests. The incidence estimate uses the inherited native second moment. The optional pointwise exponent \(b<1\) is an additional uniform hypothesis; \(b=1\) requires only elementary counting. The basic mixed-theta estimate uses the preceding all-row sextic sieve. The arithmetic identities themselves do not require new automorphy or continuation statements.

**Exact sources:** PR #914 at `0cc0428fedbbfc340044c7451b3d392c1da9a103`; PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`; their pinned dependencies. The two required #914 notes are copied byte-for-byte under [sources](sources/README.md), because this branch is stacked on #915. Neither source packet is edited or promoted into the integrated record.

## 1. A strictly smaller remaining higher-moment sector

Write the literal inverse polynomial as

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad H=D^{1+\theta}.
\]

For each ordered tuple in \(A_u(D)^k\), its exact shared-prime incidence determines singleton lengths \(X_1,\ldots,X_k\). Put

\[
Q=\frac{\prod_iX_i}{\max_iX_i}.
\]

Split the polynomial into the complete incidence blocks with \(Q\le Q_0\) and the residual polynomial. PR #915 controls the first portion. Apply a norm inequality before smoothing the entire residual square; only then use PR #914's positive accounting bounds on its Hermitian expansion.

The resulting signed remainder \(\mathcal T_{k,Q_0}^{\Phi}\) contains only tuples satisfying all three conditions:

- \(Q>Q_0\) on each side of the Hermitian expansion;
- a prime occurs exactly once among all \(2k\) factors;
- \(Ng_1\sqrt{Ng_2}>H\), where \(g_1\) is the product of those global singleton primes and \(g_2\) is the product of nonprincipal primes occurring exactly twice.

The proved inequality is

\[
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\le C_\epsilon HD^{k+\epsilon}(1+Q_0^{2b-1})
 +2\max(0,\mathcal T_{k,Q_0}^{\Phi}).
\]

For a growing subpower cutoff \(Q_0\), the first term has the desired moment size. At every fixed \(k\ge3\) and \(0<\theta<1\), explicit feasible incidence patterns show that the two exclusions are complementary: the new remaining tuple domain is strictly smaller than either previous reduction alone. This is a reduction in the arithmetic task, not a bound for the remaining signed sum. The equal-length fourth-moment periphery was already controlled, so no new fourth-moment exponent follows.

Read the full proof and its review: [DOUBLE_RESIDUAL_REDUCTION.md](DOUBLE_RESIDUAL_REDUCTION.md) · [DOUBLE_RESIDUAL_REVIEW.md](DOUBLE_RESIDUAL_REVIEW.md).

## 2. An exact bridge from the A2 completion to mixed theta families

The two published completions share the squarefree two-factor face, but have different local support. A divisor weight on the outer axis cannot identify them. For the fixed tensor test \(W_1(x)W_2(y)\), composing PR #914's five-label correction with the source's cube inversion gives an exact finite identity for its full A2 polynomial. Extending the norm estimate to a general smooth test requires the uniform Mellin-seminorm control stated in the proof.

For a correction triple \(t=(c,d,e)\), the required theta child has

\[
A_t=\frac A{Nc(Nd)^2(Ne)^2},\qquad
B_t=\frac B{(Nc)^2Nd(Ne)^2},\qquad
q_t=q_0cde,\quad f_t=ef.
\]

Cube inversion introduces a squarefree \(h\), the further scale \(B_t/(Nh)^3\), and the outer mask \((a,h)=1\). The exact normalized scalar has absolute value at most

\[
\frac1{Nc\,Nd\,(Ne)^{3/2}\,Nh}.
\]

The \(c,d,h\) sums are harmonic and the \(e\) sum converges. Thus a uniform squared norm bound \(M\) for every displayed mixed child gives \(O(M\log^6 Z)\) for the squared row norm of the normalized A2 polynomial \(Q_{q_0}/\sqrt{AB}\). Every phase and the overlap between \(q_t\) and \(f_t\) at \(e\) is retained.

The mixed children also admit the existing all-row sieve envelope

\[
D^\epsilon\left(\mathcal H+\mathcal H^{1/6}AB
 +(\mathcal H AB)^{2/3}\right).
\]

Here \(\mathcal H\) denotes the row range of the transformed problem, distinct from the original \(H\). This basic bound is uniform in the displayed moving masks and auxiliaries. The stronger reflected or centered estimate needed at the longest fourth-moment scale remains open.

Full identity, proof, norm transfer, baseline estimate and review: [INTERFACE_COMPARISON.md](INTERFACE_COMPARISON.md) · [INTERFACE_REVIEW.md](INTERFACE_REVIEW.md).

## 3. Which diagonal has been removed

PR #914's exact signed first-Poisson product-column diagonal is the original algebraic diagonal minus its zero Fourier term. Its discrepancy is \(O(D^\epsilon)\) in the stated normalized form, after the complete auxiliary sums are reunited. The [source-level interaction audit](SIGNED_DIAGONAL_INTERACTION.md) verifies this and distinguishes it from the positive character-row diagonal in the large-value Gram matrix.

The latter still produces the \(D^4\) term in PR #915's fourth-moment large-value estimate. Removing the signed Poisson diagonal does not delete that different positive Gram contribution. A stronger approach must estimate the remaining signed strict off-diagonal with the actual coefficients and coupled kernel.

The exact A2/theta representation now specifies what that route would have to retain: cross terms between independently corrected children, generally different auxiliaries, all zero masks, and equality of reconstructed original product columns. A positive mean-square transfer is not a theorem about the corresponding covariance subtraction.

## 4. Quantitative route to the requested boundary

If the new remainder estimate

\[
\mathcal T_{k,Q_0}^{\Phi}(D,D^{1+\theta})
\ll D^{k+1+\theta+\epsilon}
\]

were proved for a growing subpower \(Q_0\), for every \(\epsilon>0\), uniformly over all \(D\ge2\), with each required fixed smooth test and each fixed finite-order character, and for arbitrarily small fixed \(\theta>0\) in the permitted range, the reduction in Section 1 would give the full native \(2k\)-th moment with those quantifiers. This includes the fixed nonvanishing-Mellin detector used in the recorded extraction theorem; constants may depend on the fixed data, but not on the moving scale or rows. The moment-to-zero-free implication would then give boundaries tending to

\[
\frac12+\frac{5}{12k}
\]

as the permitted \(\theta>0\) tends to zero. At \(k=2\), this is \(17/24\); a cofinal proved hierarchy would approach \(1/2\). These are conditional consequences, not results established in this packet.

For a cutoff \(Q_0=D^q\), the controlled incidence portion instead has explicit excess \((2b-1)q\). Thus an improvement need not arrive as the entire conjectured estimate at once: a smaller proved power loss for the residual could be combined with this quantified cost. No improved residual power is asserted here.

## Validation and remaining boundary

The new claims have complete written proofs and scoped independent AI-agent reviews tied to exact file hashes. Source snapshots, review bindings, arithmetic conventions and limitations are recorded in [VALIDATION.md](VALIDATION.md), [SOURCE_LOCK.json](SOURCE_LOCK.json) and [MANIFEST.json](MANIFEST.json). These reviews are not human mathematical acceptance or Lean formalization. The new finite identities and inequalities were checked by proof, without claiming that finite numerical examples certify their analytic consequences.

The smallest remaining mathematical task is a new cancellation estimate for the stated signed residual, or an adequately uniform centered theta/A2 estimate that implies it. This packet narrows and specifies that task; it does not conceal it inside an unsigned norm or an unproved conductor adapter.
