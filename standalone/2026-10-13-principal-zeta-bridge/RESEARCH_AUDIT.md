# Where the Riemann program presently stops

**Status:** source-qualified structural audit and proposed change of target. This note does not prove a full fourth moment, a generalized diagonal moment, a new zero-free half-plane, or RH. It distinguishes the actual new identities from the arithmetic estimates still required.

**Scope of review:** the current integrated statements and the native sextic Möbius, covariance, collision, and sampling route. The imported October 5 theta foundation and the external conductor theorems are retained as named inputs; this pass does not independently certify their complete proofs. Exact repository inputs are listed below and copied with commit/path/hash bindings in AUDIT_SOURCE_BINDINGS.json.

## 1. The first missing estimate is an arithmetic signed sum

For the literal source family over \(K=\mathbb Q(\sqrt{-3})\), with its fixed finite-order character, fixed bad primes, compact smooth test, and every nonzero physical row, write
\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\]
The desired estimate is
\[
\boxed{\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll D^\varepsilon H D^k,\qquad H=D^h,\quad h>1,}
\tag{1.1}
\]
at every sufficiently large real scale, for the exact tests and derivative windows used in extraction. Constants may depend on each fixed \(k,h,W,\nu,S,\varepsilon\). Neither the fourth-moment case nor an unbounded hierarchy is proved by the cited continuation notes.

The conditional sixth-power extraction gives the strict half-plane
\[
\Re s>\frac12+\frac{5h}{12k}.
\tag{1.2}
\]
For \(k=2\), \(h\downarrow1\), this approaches \(17/24\). Equation (1.2) is an implication from (1.1), not a zero-free theorem obtained in these passes.

PR #913 already gives an exact all-order incidence reduction: repeated-prime allocations have only logarithmic or convergent recombination costs at fixed \(k\). The remaining squarefree \(k\)-factor mean square must hold at all unbalanced factor scales, with polynomially moving exclusions and the same large row set. A bound only on the balanced face, only for fixed exclusions, or only when the row height follows the smaller column scale does not meet that premise. Repeated-prime bookkeeping is therefore not the earliest remaining obstruction.

The new #916 Hermitian reduction goes further: after deleting a sufficiently large but fixed initial prime set, it absorbs all shared-prime collisions across the entire \(2k\)-tuple in a common-height, scale-integrated norm. The remaining two products \(r,s\) are squarefree and coprime, and the row character is primitive of conductor \(Nr\,Ns\). The resulting signed primitive high-conductor scalar still has no proved diagonal-size estimate. This is the presently cleanest native expression of the missing arithmetic.

## 2. Audit of the second-moment foundation

There are two different inputs that must not be conflated.

**Native M2.** PR #913, FOURTH_MOMENT_ATTACK.md, Proposition 2.1 derives
\[
\sum_{0<Nu\le D^{1+\theta}}
\left|\sum_{(n,qS)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/X)\right|^2
\ll D^\varepsilon D^{1+\theta}X
\tag{2.1}
\]
uniformly for \(1\le X\le D\) and \(Nq\le D^C\), conditional on the imported canonical theorem and Poisson reduction. It is not a reciprocal-\(L\) hypothesis restated under another name.

The scale check is explicit. At a child block of the imported reduction,
\[
Y=X/(BF),\qquad \mathcal H\ll X^2/(HB^2),\qquad
\Sigma=YF=X/B,\qquad
\mathcal H/\Sigma\ll X/(HB)\le D^{-\theta}.
\]
Thus the canonical fixed-gap condition is valid, with the original \(D\) retained as the polynomial reference parameter and, for example, gap \(\theta/2\). Exact geometric Euler inversion removes the moving exclusion at norm cost
\[
\prod_{\mathfrak p\mid q}(1-(N\mathfrak p)^{-1/2})^{-1}
\ll_\eta(Nq)^\eta.
\]
This includes character zeros at primes dividing the row. The source theorem has an explicit polynomial scale range and fixed smooth-test norms, so these are genuine uniform deductions from that theorem.

The limitation is foundational: this audit checks the adapter and its quantifiers, but does not re-prove the upstream cubic-theta reflection and canonical estimate. The original OpenAI paper, its exact version, and its named hypotheses remain visible.

**Uniform pointwise input.** The separate analytic-log argument in #913, Lemma 8.1, assumes a common zero-free half-plane for the relevant finite-order Hecke family. Polynomial conductor bounds plus the common zero-free domain then produce a reciprocal estimate uniform in the moving conductor. A fixed-character estimate with uncontrolled character-dependent constants does not suffice. This is a stronger and different premise from (2.1). The inherited angular input has its own scope as well.

In particular, this packet does not promote the prior source-qualified conditional value \(139999/160000\) into an independently certified unconditional zero-free result.

## 3. Why the recent improvements have not lowered the boundary

### 3.1. The old pointwise bootstrap has a proved saturation barrier

This barrier is already proved in PR #913; it is not new work here. Combining native M2 with a uniform pointwise exponent \(b\) gives
\[
M_{2k}(D,H)\ll H D^{1+2(k-1)b+\varepsilon}.
\]
Putting this into the same extraction yields
\[
b+\frac{1-2b+5h/6}{2k}.
\tag{3.1}
\]
When \(h\downarrow1\), the fixed point is \(11/12\). If \(b<11/12\), every finite \(k\) gives a worse exponent than \(b\), and the cofinal limit merely returns \(b\). An improvement to a positive envelope can be real while remaining useless for this particular bootstrap.

The exact sixth-power copy count is \(H^{1/6+o(1)}\). Changing positive weights on those same exact copies does not produce a larger effective family for this extraction. More importantly, #913 already identifies the cofinal all-row moment hierarchy, with its stated test and uniformity hypotheses, with GRH for the corresponding full sextic row-twist family. Ordinary RH alone is not its converse premise. This explains why an apparently modest all-row estimate can contain substantially more information than the user's ordinary-zeta objective.

### 3.2. Complete inversion can return the original covariance

PR #927, SMALL_W_CORE_AUDIT.md, traces the full auxiliary-divisor reunion back to the original centered native product-column energy. It is an exact identity, not a second independent source of cancellation. Absolute bounds on separated inverse pieces can erase the signs that reunite them.

On the balanced fourth-moment face, with physical height \(H=D^h\), the initial dual height is \(Y=D^{4-h}\). The displayed positive \(YD\) term, with the outer normalization \(H/D^2\), is \(D^3\). For \(h\) near one it cannot give the required normalized \(O(H)\). Removing some diagonals or shortening a different term leaves this large primitive face intact.

### 3.3. A dual identity is not an automatic height descent

The #916 all-color kernel gives, for a common fixed nonnegative row measure and \(\sigma=1/2+\delta\),
\[
(1-q)I_M\le I_C\le(1+q)I_M,\qquad q\le1/3,
\]
after a fixed prime cutoff depending on \(k,\delta\). The signed \(I_C\) is positive after the completed row-and-scale integration; its individual summands need not be positive. The theorem does not permit changing the row measure after each scale dilation, and its absolute kernel argument is unavailable at \(\delta=0\).

The primitive Gaussian Poisson identity exchanges \(H\) and a constant multiple of \(Nr\,Ns/H\). Applying the functional equation twice returns to \(H\). Low-conductor sectors can be paid, but the remaining high-conductor signed sum needs a genuinely new estimate. Calling the involution a descent does not supply one.

### 3.4. The new conductor regions are useful, but not the dominant disjoint sector

At #929's exact head, its conductor-average proof reports the source-dependent positive bound
\[
\mathcal Q_L^\Phi\ll D^{k+\varepsilon}H^{1/2}L^{3/4},
\qquad L\asymp Ng_1.
\]
It pays \(Ng_1\le H^{2/3}\). The rational-prime refinement writes \(Ng_1=v(g_1)w(g_1)^2\) and pays the larger region
\[
v(g_1)^3w(g_1)^2\le H^2.
\tag{3.2}
\]
These are absolute tuple-accounting regions, including all their moving masks. The cubic mean imports the named version of de Faveri's polynomial large-sieve input; other analytic branches retain their separate inputs.

For \(2k\) unrelated coprime columns of length \(D\), the singleton norm can be \(D^{2k}\), with no compensating rational pairings. That region survives (3.2). The comparison does not deny better estimates for certain complete signed blocks in earlier work; arbitrary-subset positive accounting and a coherent signed block are different assertions.

The same #929 packet's joint continuation reaches \(a,b>1/2,\ 6a+8b>11\), for its exact coherent reflected function and stated foundation. It explicitly notes that a candidate energy from the scalar \(73/120\) remains weaker than an existing physical envelope. That number is not a zero-free boundary.

### 3.5. Sampling and contour transport reduce the observations, not their size

The #929 fixed log-Gaussian criterion recovers the full moving-height moment from \(O(\log X/\log\log X)\) prescribed scales, with the actual moving endpoints covered. Its entire logarithmic-scale interpolation is effective. The sampled arithmetic estimate remains unproved.

The #911 short-polynomial transport is a finite coefficient identity after all physical norm tests are applied. The proved common conjugate tube pays one frequency region. Its open CT1 asks for the actual signed short trace on the complementary independent-frequency region, including every allocation, ray phase, and row-zero mask. It is stronger than merely writing the integrated moment in that region.

The present packet proves a new obstruction to an overly positive continuation of that approach: ANTI_CONJUGATE_COLLISION_GROWTH.md constructs an admissible independent-frequency point with total frequency zero and
\[
|Q_{\rm coll}|\ge
\exp\!\left(cY^{1-2\sigma}/\log Y\right),
\qquad 1/3<\sigma<1/2,\quad k\ge2,
\]
uniformly over polynomially bounded rows and masks. Total-frequency balance alone does not recover the conjugate-tube decay. This is a statement about the exact collision factor, not a counterexample to CT1, the completed signed trace, or RH. It argues for retaining the physical norm filtering and coupled cancellation before applying a size estimate.

Its companion SHIFTED_COLLISION_AND_LITERAL_SHORT_FACTORS.md strengthens this obstruction: a common set of shifts of positive measure retains the same stretched-exponential growth after multiplying by every actual short Möbius factor, simultaneously over a polynomial collection of rows and masks. The argument uses a uniform Euler anchor and finite-polynomial zero avoidance. It still concerns individual arithmetic row factors; exterior multipliers may vanish, and the signed row sum may cancel. Thus the stronger conclusion does not promote the obstruction into a refutation of CT1.

## 4. The wider repository has the same source-versus-component boundary

The integrated CURRENT_RESULTS.md at #928 retains genuine finite and conditional results without a global RH conclusion. Its source-defined Mellin negative-part criterion still needs the actual arithmetic negative-part estimate. Its operator reductions still need an actual continuum lower certificate and an unbounded family of complete windows; positive Galerkin sections approach from above. Its low-order xi positivity permits off-line model configurations and does not supply all-order positivity. Fixed-\(P_{61}\) control does not give growing-prime control, and the causal Euler correction retains its stated line-one domain.

These are specific missing assertions in the current integrated account, not a claim that exact algebra, finite certificates, or analytic continuation are worthless. They prevent a component theorem in another program from being inserted as the missing native signed estimate without an exact source adapter.

## 5. A narrower target and the remaining creative strike

The present packet constructs an exact ordinary-zeta bridge. A fixed bounded-prefix periodic filter removes the quadratic companion factor, and finite prime-ideal restoration gives
\[
B_1(D)=\sum_{n\ge1}\mu_{\mathbb Z}(n)W(n/D),\qquad
B_{w^6}(D)=\sum_{\operatorname{rad}r\mid w}B_1(D/Nr).
\tag{5.1}
\]
The filter preserves every exponent \(\alpha>0\), provided the same-height source norm is known at every smaller scale for the specified logarithmic derivative window. This is a proved adapter; it is not an automatic inference from a single-window bound on a curved range.

For a fixed rough prime set and a fixed positive fraction of principal replicas, the companion sparse-capture theorem reduces ordinary zero exclusion to small values at a predetermined polylogarithmic grid. It neither requires estimates for every Hecke twist nor assumes that the good replicas remain the same at different nodes.

PRINCIPAL_REPLICA_AVERAGES_AND_CONVERSE.md proves the exact positive rough-annulus average and its invertible multiplier
\[
m_Q(s)=\prod_{\mathfrak p\notin Q}
\frac{1-(1-(N\mathfrak p)^{-1})(N\mathfrak p)^{-s}}
     {1-(N\mathfrak p)^{-s}},\qquad \Re s>0.
\]
The multiplier and its reciprocal are holomorphic and nonzero there. Thus averaging exact principal copies preserves the target's Mellin singularities; it does not manufacture cancellation. Moving finite-annulus averages are treated by a uniform causal operator approximation, not falsely identified with this scalar multiplier.

For every fixed \(\alpha>1/2\), ordinary RH implies the required bound for all polynomially bounded principal replicas. Conversely the companion cofinal capture assertions imply ordinary RH. This is a narrower exact target than the old full-family GRH hierarchy, but it is still RH-strength in cofinal form. No same-endpoint converse is claimed from zero-freeness only in \(\Re s>\alpha\).

The new attack should therefore seek a bound for the actual restored principal replicas, or the actual norm-filtered primitive signed covariance, with its signs intact. A positive fraction of prescribed-node capture is now enough for the ordinary-zeta objective. Proving that capture, rather than another unfiltered absolute envelope, is the outstanding arithmetic step.

## Exact input ledger

| Input | Frozen commit | Load-bearing files |
|---|---|---|
| Integrated state and previous packet, #928 | ab98878279cd5614fe79bb94aa916e97c9ee50b4 | STATUS.md; research/integrated/CURRENT_RESULTS.md |
| Native M2 adapter and old saturation/converse barriers, #913 | 6498d6cc2eded03159c7332b25fd224ad07f89c1 | standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md; MOMENT_OBSTRUCTIONS.md |
| Exact signed reunion, #927 | f9939c957f5aac6b2099b591e4988991700a152b | standalone/2026-10-10-sextic-signed-reunion/SMALL_W_CORE_AUDIT.md |
| Hermitian coprime core, #916 | dd70e580a5ffdbe5b140784ba6cebd173cb84792 | standalone/2026-10-10-all-order-collision-removal/continuation-hermitian-disjoint/PROOF.md; DUAL_CORE.md |
| Conductor, continuation and sampling state, #929 | 97bf40329489992e9384c34d7595af6d01a40774 | standalone/2026-10-10-conductor-averages/README.md; CUBIC_CONDUCTOR_AVERAGE.md; RATIONAL_PRIME_INCIDENCE.md; JOINT_CONTINUATION.md; GAUSSIAN_SAMPLED_MOMENTS.md |
| Prime-slot route and CT1, #911 | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | research/exploratory/2026-10-10-two-hour-continuation/literature/PRIME_SLOT_ROUTE_STATUS.md; the four sources in ANTI_CONJUGATE_SOURCE_BINDINGS.json |
| Imported theta foundation | OpenAI/math adc7f1241b42e322a6451854ab7e4b4c146bf78a | preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex; retained repository snapshot SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d |

The #929 regional and continuation claims above are reported at their source-qualified scope; this note is not a new independent proof of every external analytic input in that packet. The new results have separate complete manuscripts and independent review receipts. Finite diagnostics, where supplied, check their stated algebra and source bindings only.
