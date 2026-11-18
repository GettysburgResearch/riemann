# Finite negative mass from squared blocks of critical-line residues

Status — Proposed conditional result for the original 5:3 arithmetic detector.

Assume RH and that all nontrivial zeros are simple. A logarithmically weighted square sum over unit frequency blocks of the actual detector's residues suffices for
\[
 \int_1^\infty (5c_X(2)+3c_X(3))_-\,\frac{dX}{X}<\infty .
 \tag{1}
\]
The arithmetic applications below allow \(J_{-1}(T)\ll T^4/(\log T)^{3+\eta}\) for any fixed \(\eta>0\). Absolute convergence of the residue series is unnecessary. None of these zero or reciprocal-derivative hypotheses is established here.

## Source and statement

Use \(w(u)=5c_{e^u}(2)+3c_{e^u}(3)\), \(P(z)=-3(2^{-z}-1)(2^{-z}-2)\) and \(H(s)=6+P(1/2+s)/\zeta(1/2+s)\). The original Laplace transform is \(H(s)/s^2\), absolutely for \(\Re s>1/2\). Write \(A=H(0)>6\), \(B=H'(0)\). The [companion note](detector-nov18.md) gives the primitive arithmetic sum and proves unconditional oscillation of the centered source. The frozen arithmetic source is [L-99261](https://github.com/GettysburgResearch/riemann/blob/433fd3662f7b2e4ba384ce64f196380e88624090/claims/lemmas/L-99261-five-three-row-zero-free-mellin-witness.md).

Include both signs of every ordinate and put
\[
 c_\gamma=\frac{P(1/2+i\gamma)}{(i\gamma)^2\zeta'(1/2+i\gamma)},\qquad
 b_k=\sum_{k\le\gamma<k+1}|c_\gamma|\quad(k\in\mathbb Z).
\]
Under RH and simplicity, \(\sum_k b_k^2<\infty\) implies
\[
 \int_0^T w(u)_-\,du=o(\log(2+T)).
 \tag{2}
\]
The stronger condition \(\sum_k\log(2+|k|)b_k^2<\infty\) implies (1).

## 1. The unit-interval square estimate

For any finite coefficient family \(d_\gamma\), let \(D_k=\sum_{k\le\gamma<k+1}|d_\gamma|\). Then for an absolute \(C\),
\[
 \sup_{v\in\mathbb R}\int_v^{v+1}
       \left|\sum_\gamma d_\gamma e^{i\gamma u}\right|^2du
       \le C\sum_kD_k^2 .
 \tag{3}
\]
Take a smooth nonnegative compactly supported majorant \(\chi\) of the unit interval indicator and integrate against \(\chi(u-v)\). The term for a pair in blocks \(k,\ell\) has modulus bounded by a constant times \(|d_\gamma d_\lambda|(1+|k-\ell|)^{-2}\) by two integrations by parts away from zero frequency. The discrete convolution kernel is summable. Cauchy–Schwarz for each shift proves (3). Frequency collisions within blocks are fully charged to \(D_k\).

If \(\sum b_k^2<\infty\), the finite partial residue sums therefore converge to a function \(S\) in the norm \(\|f\|_{S^2}=\sup_v(\int_v^{v+1}|f|^2)^{1/2}\). Convergence follows first in each local \(L^2\), and (3) makes the convergence uniform in the interval. Truncation and the inequality also give convergence in this norm of the Gaussian sums \(\sum_\gamma e^{-\epsilon\gamma^2}c_\gamma e^{i\gamma u}\) to \(S\) as \(\epsilon\downarrow0\).

## 2. Identification with the actual source

For \(u>0\), invert \(e^{\epsilon s^2}H(s)/s^2\) on \(\Re s=1\), using the factor \(e^{su}\). Shift the contour to \(\Re s=-1\). The crossed pole at zero contributes \(Au+B\) for every \(\epsilon>0\). Under the two zero hypotheses, all other crossed poles are the simple poles at \(i\gamma\), with residues \(e^{-\epsilon\gamma^2}c_\gamma e^{i\gamma u}\). The pole of zeta corresponds to a regular point of the reciprocal. All trivial zeros lie to the left of this strip.

Here are the contour bounds. On the right, \(H(1+it)=O(1)\) by absolute convergence. On the left, the functional equation and the bounded reciprocal on \(\Re z=3/2\) give \(1/\zeta(-1/2+it)=O((1+|t|)^{-1})\), using Stirling for \(|t|\ge2\) and compactness for the remaining segment. Thus \(H(-1+it)=O(1)\).

For completeness, there are cofinal positive heights \(T_j\), and their negatives, on which \(1/|\zeta(\sigma+iT_j)|\le\exp(C\log^2T_j)\) uniformly for \(-1/2\le\sigma\le2\). The Riemann–von Mangoldt formula counts \(O(\log j)\) ordinates in \([j-1,j+2]\), so one can choose \(T_j\in[j,j+1]\) with separation \(\gg1/\log j\) from all ordinates. Subtract the logarithmic derivatives of the Hadamard product of the completed xi function at \(s=\sigma+iT_j\) and \(s'=2+iT_j\). The resulting zero sum has terms \(1/(s-\rho)-1/(s'-\rho)\). Within unit distance in ordinate their total is \(O(\log^2 T_j)\). Outside that range the difference is \(O(|T_j-\Im\rho|^{-2})\), whose sum is \(O(\log T_j)\) by the same local count in successive unit intervals. The gamma and elementary factors contribute \(O(\log T_j)\) by Stirling, and \(\zeta'/\zeta(s')=O(1)\). Integration horizontally from \(s'\) gives the asserted bound. The Gaussian factor then makes the horizontal integrals vanish for each fixed \(\epsilon>0\).

On letting \(\epsilon\downarrow0\), dominated convergence applies to both vertical lines. The right integral tends to \(w(u)\) by ordinary Fourier inversion of the continuous exponentially damped arithmetic sum, whose transform is integrable on that line. The left integral tends to
\[
 R(u)=\frac{e^{-u}}{2\pi}\int_{\mathbb R} e^{itu}\frac{H(-1+it)}{(-1+it)^2}\,dt,
 \qquad |R(u)|\ll e^{-u}.
\]
On compact intervals of \(u\) both convergences are uniform by the same integrable vertical majorants. Step 1 identifies the intervening residue sums in local \(L^2\). Consequently
\[
 w(u)=Au+B+S(u)+R(u) \quad\text{for almost every }u>0 .
 \tag{4}
\]
This derivation compares the physical source and the frequency series before estimating negative parts.

## 3. Spending the positive linear term

Write \(M=(\sum b_k^2)^{1/2}\) and, for integer \(n\ge1\), choose \(K_n=\lfloor cn^2\rfloor\) with fixed \(c>0\) sufficiently small. The part \(S_{\rm lo}\) in blocks \(|k|\le K_n\) is bounded pointwise by \((2K_n+1)^{1/2}M\le An/4\) for all sufficiently large \(n\). On \([n,n+1]\), \(Au+B+R(u)\ge 3An/4\) eventually. The real sum \(S\) can be split using real parts of both finite and residual pieces if the half-open bins are asymmetric. Equation (4) gives
\[
 \int_n^{n+1} w_-\,du
 \le \int_n^{n+1}(|S-S_{\rm lo}|-An/2)_+\,du
 \le \frac{C'}{n}\sum_{|k|>K_n} b_k^2
 \tag{5}
\]
by \((t-h)_+\le t^2/(4h)\) and (3). The tail tends to zero. Its harmonic sum up to \(T\) is \(o(\log(2+T))\), proving (2). Summing (5) over all \(n\), Tonelli gives an upper bound by a constant times
\[
 \sum_k b_k^2\sum_{\substack{n\ge1\\cn^2<|k|}}\frac1n
 \ll \sum_k \log(2+|k|)b_k^2 .
\]
The initial finite intervals have finite negative mass by continuity. This proves (1).

## 4. A reciprocal-derivative moment that suffices

Set \(J_{-1}(T)=\sum_{0<\gamma\le T}|\zeta'(1/2+i\gamma)|^{-2}\). As \(|P|\) is bounded on the critical line, the local zero count and Cauchy–Schwarz give, for \(X\ge4\),
\[
 \sum_{X\le|k|<2X} b_k^2
 \ll X^{-4}\log X\,J_{-1}(2X+2).
\]
Consequently \(J_{-1}(T)\ll T^4/(\log T)^{3+\eta}\) for some \(\eta>0\) implies the weighted sum for (1), by taking \(X=2^j\) and summing \(O(j^{-1-\eta})\). The exponent \(2+\eta\) on the logarithm already gives the unweighted sum for (2). Any fixed power saving \(J_{-1}(T)\ll T^{4-\delta}\), \(\delta>0\), gives (1). By comparison, the direct dyadic Cauchy–Schwarz bound for the absolute residue sum is \(O(X^{-2}(X\log X)^{1/2}J_{-1}(2X+2)^{1/2})\) per dyadic block and certifies absolute convergence for a power exponent strictly below three. These are sufficient conditions for distinct conclusions. This proof does not claim eventual nonnegativity or the necessity of a reciprocal-derivative bound.

No numerical input enters this conditional result. The imported facts are the zeta functional equation, its Euler product in the absolute-convergence half-plane, the xi Hadamard product, Stirling's estimate, and the classical Riemann–von Mangoldt local counting bound. The unresolved hypotheses are the stated zero location, simplicity and residue control.
