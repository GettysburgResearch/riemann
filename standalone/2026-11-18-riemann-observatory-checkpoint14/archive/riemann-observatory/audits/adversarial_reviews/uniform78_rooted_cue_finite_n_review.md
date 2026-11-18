# Independent finite-N check of the rooted CUE cumulant experiment

18 November 2026. Read the [experiment note](prime78_rooted_cue_band_moment_experiment.md), its [Python implementation](../../scripts/prime78_rooted_cue_band_moments.py), and its [recorded output](../../experiments/results/prime78_rooted_cue_band_moments.json). The exact trace formulas, root normalization, and cutoff are correct for the selected band \((1/20,1/10]\). A separate implementation using widened full Fourier matrices agrees in exact arithmetic at \(N=20,41\), and in double precision at sampled sizes through \(N=2000\). This checks finite calculations and convergence numerics. The [separate proof](uniform77_rooted_cue_full_law.md) supplies the random-matrix weak limit.

## Decomposition and trace algebra

Starting with total \(N\) eigenangles, the rotated sea contains \(N-1\) eigenangles. The \((1-z)^2\) divisibility description gives an ambient degree set \(0,\dots,N\) of length \(N+1\), and two linear conditions remove the value and first derivative at 1. The constant coefficient vector and its orthogonalized degree vector span the removed two-dimensional subspace. The free-angle projection is \(P=I-Q,\ Q=UU^*\); the root count is separate. The first cumulant obtains \(f(0)=-\sum_k1/k\), and the second and third do not change under this deterministic shift.

Let \(A=E M_fE,\ B=E M_{f^2}E,\ C=E M_{f^3}E\), expressed in the degree set, with \(E\) denoting the ambient compression. Compact finite-dimensional determinant differentiation gives
\[
 \kappa_1^{\rm free}=\operatorname{Tr}(PA),\quad
 \kappa_2^{\rm free}=\operatorname{Tr}(PB)-\operatorname{Tr}(PAPA),\quad
 \kappa_3^{\rm free}=\operatorname{Tr}(PC)-3\operatorname{Tr}(PAPB)+2\operatorname{Tr}(PAPAPA).
\]
In particular \(B,C\) allow intermediate Fourier paths outside the degree set, unlike \(A^2,A^3\). For the quadratic correction, \(\operatorname{Tr}(PAPA)=\operatorname{Tr} A^2-2\operatorname{Tr}(QA^2)+\operatorname{Tr}((U^*AU)^2)\). For the cubic correction, the \(\operatorname{Tr}(PAPB)\) terms remove \(\operatorname{Tr}(QAB)\) and \(\operatorname{Tr}(QBA)\) and restore \(\operatorname{Tr}(QAQB)\). In \(\operatorname{Tr}(PAPAPA)\), by cyclicity the three one-removal terms equal \(-3\operatorname{Tr}(QA^3)\), the three two-removal terms equal \(3\operatorname{Tr}(QAQA^2)\), and the last term is \(-\operatorname{Tr}(QAQAQA)\). Hence with \(M_j=U^*F_jU,\ F_j=A,B,C\) respectively, and \(R=U^*A^2U\), the code's third correction is exactly
\[
 -\operatorname{Tr} M_3+3\operatorname{Tr}(U^*(AB+BA)U)-3\operatorname{Tr}(M_1M_2)
 -6\operatorname{Tr}(U^*A^3U)+6\operatorname{Tr}(M_1R)-2\operatorname{Tr}(M_1^3).
\]
The code obtains \(U^*A^3U\) by applying \(A\) to \(AU\) and left-multiplying by \((AU)^*\); it computes \(B,C\) from uncompromised scalar Fourier convolutions before compression. Toeplitz slicing starts at the zero-coefficient index of the relevant convolution.

At \(P=I\) the mean is zero and the variance is \(\sum_{k>0}\min(k,N+1)/(2k^2)\). In this band the minimum is always \(k\). For a signed cubic resonance \(r+s+t=0\), \(A B\) restricts the starting and first postmultiplier points, with trace count \(N+1-|r|\) when all frequencies fit. The three-multiplier trace constraint restricts offsets \(0,r,r+s\), whose span is \(\max(|r|,|s|,|t|)\). In the present range all these counts are nonnegative. Symmetrizing in the ordered signed triple cancels precisely because \(|r|+|s|+|t|=2\max(|r|,|s|,|t|)\). In fact no resonance exists in this particular band: the sum of any two positive frequencies is strictly greater than the upper endpoint. The cardinality of \(k\) is computed by \(\lfloor bN\rfloor-\lfloor aN\rfloor\) with exact fractions. For example, \(N=20\) keeps \(k=2\) and excludes \(k=1\) exactly, while \(N=41\) keeps \(k=3,4\).

## Independent replay through full Fourier matrices

Besides replaying the committed script byte for byte, I formed the whole multiplication matrix \(W_{ij}=c_{i-j}\) on indices \(-3K,\dots,N+3K\), \(K=\lfloor N/10\rfloor\), with \(c_{\pm k}=-1/(2k)\) only for the admitted band. Let \(V\) be the rectangular submatrix of \(W\) formed by columns \(0,\dots,N\), and let \(W_0\) be its square central slice. Then independently
\[
 A=W_0,\qquad B=V^*V,\qquad C=V^*WV .
\]
The widened coordinates capture every possible three-step path that starts and ends in the compressed degree set. Formed \(P\) directly with \(P_{ij}=1_{\{i=j\}}-1/(N+1)-x_i x_j/\sum_\ell x_\ell^2\) for \(x_i=2i-N\), and evaluated the three original trace formulas without the low-rank expansion. In exact arithmetic using Python Fractions, the results were

| \(N\) | Mean | Variance | Third cumulant |
|---:|---:|---:|---:|
| 20 | \(1433/4620\) | \(5147111/21344400\) | \(-39418363/49305564000\) |
| 41 | \(58271/148092\) | \(3100871237/10965620232\) | \(-217631494/268505395403\) |

The first reproduces the archived result. The second is an off-grid case recovered exactly by the experiment's rational route as well. Against the floating low-rank implementation, the widened route agreed within \(1.25\cdot10^{-14}\) in every coordinate across \(N=40,80,160,320,321,640,641,1000,2000\) using NumPy 2.3.5 and two OpenBLAS threads. At \(N=2000\) it gave mean \(0.4913395634393213\), variance \(0.3355121348742422\), and cubic \(-0.0009461049540767\). The continuum formulas give \(0.4937305138932786,\ 0.3367482500021949,\ -0.0009478058530092593\). The cubic is less monotone when using the adjacent \(N=321,641\), illustrating endpoint discretization. The experiment makes no convergence-rate claim.

Inspected script SHA-256 236d2581982fd5f510bed1f2add2feeecdb9c58233b439b197fd819056e1c306. Recorded JSON SHA-256 6e62cb52f84596fa289c07e505e7f288cc7d42e8901d46e793f3e29e3fff78d3. The mathematical review found no issue requiring a change in either.

## Dependency records

Staged four targeted primary-source candidates with exact versions, access scope, pinned PDF hashes and bibliographic metadata. The record comparison exposed one title misattribution in the earlier audit. The primary general microscopic limit is BNR's *Ewens measures on compact groups and hypergeometric kernels*, Theorem 5, and the title in that audit has been corrected. The 2009 BNR IMRN article supplies the separate finite circular-Jacobi density. No canonical records changed. [Round 13 candidate notes](../../quality/pending_round13/uniform78_rmt_dependency_notes.md)
