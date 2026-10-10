# Generalized inverse moments: proved components and the exact remaining theorem

**Status: proposed research. The requested short-row fourth moment and generalized short-row moment are not proved. No new zero-free boundary or RH proof is claimed.**

This packet continues PR [#910](https://github.com/GettysburgResearch/riemann/pull/910), at exact parent commit `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`. That pass proved the higher-moment extraction and a fourth-moment coefficient reduction. The present pass develops their all-order structure, proves a generalized moment on a longer row range, removes the moving exclusions from a correctly quantified analytic target, and sharpens the logical relation between moment growth and zeros.

The source manuscripts remain at their imported bytes. The current OpenAI/math head checked during this pass is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; its October 5 and September 30 TeX blobs match the pinned import at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

## 1. The theorem requested, with its essential quantifiers

Use the original family over \(K=\mathbb Q(\sqrt{-3})\):

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\]

Here \(n\) runs over ideals represented by the source's primary generators; \(u\) runs over nonzero Eisenstein integers; \(S\) is fixed; \(\nu\) is a fixed finite-order character; and the zero extensions are retained. For every fixed integer \(k\ge1\), the sought estimate is

\[
\boxed{\displaystyle
\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{k,\nu,S,W,\theta,\epsilon}D^{k+\epsilon}H,
\qquad H=D^{1+\theta},\quad 0<\theta\le1/10.}
\tag{1.1}
\]

All rows must remain, including the sixth powers used to extract the original character. Constants may depend on the fixed moment order. The imported October 5 paper supplies \(k=1\); this packet does not supply \(k=2\) or the general short-row case.

The already proved extraction gives the limiting exponents

| Hypothetical new input | Limiting zero-free exponent as \(\theta\downarrow0\) | Status |
|---|---:|---|
| Fourth moment, \(k=2\) | \(17/24\) | Open analytic input |
| Sixth moment, \(k=3\) | \(23/36\) | Open analytic input |
| \(2k\)-th moment | \(1/2+5/(12k)\) | Open analytic input |
| A cofinal sequence with the losses below | \(1/2\) | Equivalent to GRH for the relevant twist family |

The all-moment conclusion is global. It does not leave an unspecified finite collection of off-line zeros to be checked later.

## 2. What is proved in this packet

### A. An unconditional generalized moment on a longer row range

For every fixed \(k\), arbitrary bounded squarefree coefficients \(a_n\) supported on \(Nn\le bD\), and every \(H\ge1\),

\[
\sum_{0<Nu\le H}\left|\sum_n a_n\chi_n(u)\right|^{2k}
\ll_{K,k,b,\epsilon}H D^{k+\epsilon}+D^{3k+\epsilon}.
\tag{2.1}
\]

Consequently the desired diagonal size holds when \(H\ge D^{2k}\). This theorem uses primitive Gauss sums, elementary lattice Poisson summation, an explicit imprimitive-mask expansion, and the complete sextic diagonal count. It does not depend on the claimed quasi-Riemann theorem. The long row range does not give the proposed improvement toward \(1/2\).

The same note proves a substantive obstruction. Positive squarefree coefficients have

\[
\sum_{0<Nu\le D^h}|C_u(D)|^{2k}
\gg D^{2k+h/6}/\log D.
\tag{2.2}
\]

Thus a diagonal-size theorem valid for arbitrary bounded squarefree coefficients requires \(h\ge6k/5\). At every such range, the repository's prime extraction gives an exponent at least one. **An arbitrary-coefficient theorem cannot produce the intended nontrivial cancellation through this extraction.** The Möbius structure has to be used.

Read [the complete theorem and obstruction](LONG_ROW_AND_OBSTRUCTION.md).

### B. Every repeated-prime pattern has controlled cost

For the product of \(k\) squarefree inverse sums, place a prime in \(q_I\) when it occurs in exactly the factors indexed by \(I\subseteq\{1,\ldots,k\}\), \(|I|\ge2\). The remaining singleton factors are pairwise coprime. This gives a finite exact decomposition of \(A_u(D)^k\) into squarefree rectangular allocation sums and external row phases.

After a row norm, the exterior ideal weight is

\[
\prod_{|I|\ge2}(Nq_I)^{-|I|/2}.
\]

Each pair overlap has harmonic cost. Every overlap of size at least three has an absolutely convergent ideal sum. The total cost is at most

\[
(1+\log D)^{\binom{k}{2}}
\]

before squaring. Positive multiples of six in a character exponent retain their coprimality masks. The formula therefore includes the extra algebraic configurations at high moments.

Read [the all-order identity and conditional reduction](HYPERGRAPH_REDUCTION.md).

### C. The moving coprimality exclusions can be removed

Assume a bound for the unmasked pairwise-coprime \(k\)-factor sum, uniformly over all smaller factor scales and at the same common row range \(H\). Its masked version has the exact local inverse

\[
\frac1{1-z_1-\cdots-z_k}
=\sum_{\mathbf e\ge0}\binom{|\mathbf e|}{e_1,\ldots,e_k}\mathbf z^{\mathbf e}.
\]

After adding the finitely many primes \(Np\le4k^2\) to a fixed set \(S_k\), the induced norm cost is

\[
\prod_{p\mid Q}(1-k/\sqrt{Np})^{-1}
\ll_{k,\delta}(NQ)^\delta.
\]

The unmasked analytic hypothesis is assumed for that fixed enlarged set; it is not inferred by deleting terms from a signed sum. The original fixed small primes are restored by finite allocations. The hypergraph support bound \(NQ\le(bD)^{k/2}\) absorbs the moving cost into \(D^\epsilon\).

The singleton Euler series also has the exact factorization

\[
\mathcal F_u(\mathbf s)
=\mathcal C_u(\mathbf s)\prod_{i=1}^kL_u^S(s_i)^{-1},
\qquad
\mathcal C_{u,p}(\mathbf s)
=\frac{1-\sum_i z_i}{\prod_i(1-z_i)}.
\]

The coefficient of a nonzero multiindex \(\mathbf e\) in this local correction is \(1-|\operatorname{supp}\mathbf e|\). All one-coordinate terms vanish. Both correction operators have norm cost at most \((\log(3+Z))^{\binom{k}{2}}\) at the square-root scale, with the fixed small-prime convention. The unsolved content is the correlated product of inverse sums; the Euler correction does not itself establish that bound.

Read [the complete mask and Euler proofs](MASKS_AND_EULER_FACTORS.md).

### D. One explicit smooth test detects every relevant zero

There is a fixed nonnegative \(W_*\in C_c^\infty((1,2))\) with

\[
\widehat W_*(s)=e^{(\log2)s/2}
\prod_{j\ge1}\frac{\sinh(a_js)}{a_js},
\qquad a_j=\frac{\log2}{8j^2}.
\tag{2.3}
\]

Its Mellin transform has no zero in \(\Re s>0\). The proof constructs \(W_*\) as a logarithmic infinite convolution of uniform densities and proves smoothness by rapid Fourier decay. Thus the all-scale zero argument needs only this one test, with no zero-dependent choice and no height-dependent lower bound on its transform.

If a fixed sextic twist has a zero with real part \(b>0\), then for every \(0<\beta<b\) and every fixed \(k\), there are scales \(D_j\to\infty\) at which

\[
\frac{\displaystyle\sum_{0<Nu\le D_j^h}|A_u(D_j;W_*)|^{2k}}
{D_j^{2k\beta+h/6}/\log D_j}\longrightarrow\infty.
\tag{2.4}
\]

The proof chooses record scales for the base row and uses exact prime removal. At those scales, all the \(D^{h/6+o(1)}\) selected prime replicas retain essentially the same large value. This is a statement about actual required large rows, rather than an estimate of a formal diagonal.

Read [the universal test, record-spike proof, and consequences](MELLIN_AND_SPIKES.md).

### E. A weaker cofinal moment theorem would already suffice

An estimate

\[
M_{2k}(D,D^h;W_*)\ll D^{k+h+e_k+\epsilon}
\]

excludes zeros to the right of

\[
\frac12+\frac{5h}{12k}+\frac{e_k}{2k}.
\tag{2.5}
\]

It is enough to prove this along an unbounded sequence of fixed orders with \(e_k=o(k)\); one does not need every order, exact diagonal size, or constants uniform in \(k\). A separate sufficient alternative is the tail estimate that the number of rows exceeding a fixed threshold \(C D^\alpha\) is \(o(D^{h/6}/\log D)\). Exact prime removal then gives the same exponent \(\alpha\) for every fixed base twist. This tail estimate allows larger values on a smaller exceptional set than a full moment bound would permit, and remains open.

For a precise characterization, let \(B_\nu\) be the supremum of real parts of nontrivial zeros across the primitive sextic twists of a fixed \(\nu\), and let

\[
\lambda_k=\limsup_{D\to\infty}\frac{\log M_{2k}(D,D^h;W_*)}{\log D}.
\]

The proved record bound and a stated standard uniform reciprocal lemma give

\[
2kB_\nu+h/6\le\lambda_k\le2kB_\nu+h,
\qquad \lim_{k\to\infty}\lambda_k/(2k)=B_\nu.
\tag{2.6}
\]

This identifies the all-moment target as equivalent to GRH for that twist family. The upper argument includes the conductor bound, deleted Euler factors, and the \(B_\nu=1\) endpoint; it does not invoke the claimed quasi-Riemann theorem. The equivalence clarifies the strength of the target and does not prove its arithmetic premise.

## 3. Why the present tools still stop short

There are two separate failures in applying the existing second-moment proof to a product. Its cubic-theta reflection has not been proved for the full allocation coefficient. Also, collapsing \(k\) factors produces column length \(D^k\) and a dual ratio

\[
\mathcal H_{\rm dual}/\Sigma\asymp D^k/H.
\]

At \(H=D^{1+\theta}\), this violates the imported positive-gap condition for \(k\ge2\). A coefficient identity alone cannot repair that scale mismatch.

Interpolation also leaves precisely a linear moment loss. Given a diagonal \(2K\)-th moment and a uniform pointwise bound \(|A_u|\ll D^{B_0}\), it yields

\[
M_{2k}\ll H D^{k+(2B_0-1)(k-K)}\quad(k\ge K).
\]

The excess is linear in \(k\). Synthetic arrays respecting the available moments and enough large entries for the prime replicas attain that loss. These are counterexamples to deduction from norm information alone, not to the arithmetic conjecture. The exact proofs, integer row-count conditions, and attempted cofinal extensions are recorded in [the interpolation and finite-ladder note](BOOTSTRAP_LIMITS.md).

There is a concrete conditional short-row corollary of the existing inputs: assuming a uniform zero-free boundary \(B<1\) for the full twist family and the imported second moment gives

\[
M_{2k}\ll H D^{1+2B(k-1)+\epsilon}.
\]

At the imported value \(B=7/8\), this yields \(M_4\ll HD^{11/4+\epsilon}\). The desired fourth moment has exponent \(2\), and the derived excess \(3(k-1)/4\) remains linear. More generally, interpolating from order \(2K\) gives the extracted boundary \(B+(K/k)(1/2+5h/(12K)-B)\), a convex combination of the two boundaries already present in the inputs. It cannot improve their minimum. This corollary does not independently validate the imported \(7/8\) claim.

The remaining concrete target is the uniform unmasked rectangular mean square in `HYPERGRAPH_REDUCTION.md`, or a genuinely stronger short-row large-value theorem for the exact signed coefficients. No existing imported theorem was found to supply it.

## 4. Evidence and reading order

1. Read `LONG_ROW_AND_OBSTRUCTION.md` for the actual unconditional moment proved and the impossibility of an arbitrary-coefficient shortcut.
2. Read `HYPERGRAPH_REDUCTION.md` and `MASKS_AND_EULER_FACTORS.md` for the all-order reductions and their exact common-row quantifiers.
3. Read `MELLIN_AND_SPIKES.md` for the universal test, required moment spikes, relaxed moment target, and equivalence.
4. Read `BOOTSTRAP_LIMITS.md` for the conditional interpolation bound and the precise limits of finite moment information.
5. Read [review scope](REVIEW.md), [validation](VALIDATION.md), and [provenance](PROVENANCE.json).

The exact checker passes **32,473 predicates**. It compares independently assembled products and incidence sums through \(k=8\), checks actual sextic characters at split prime ideals of norms 7 and 13 on all 91 integer residue classes, checks complete-residue moment orthogonality including the high-order zero masks, and verifies the local multivariable identities through degree 8 for up to six factors. Ordinary and optimized Python outputs agree byte for byte. These are finite arithmetic and algebra checks; the infinite analytic results rest on the written proofs.

This is a separate proposed packet, with its own source and review boundary. The previous import and research remain unchanged, and no material is promoted to the integrated record.
