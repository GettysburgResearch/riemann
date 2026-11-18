# Conditional inversion of the generator-target error form

17 November 2026. Assume RH and the asserted limiting quadratic form for every finite real combination of the step targets \(R_k\). For a simple zero \(\rho=\tfrac12+i\gamma\), let its mass be \(|\zeta'(\rho)|^2/|\rho|^2\), counting both ordinate signs. Write their measure as \(\nu\). The following calculation uses the form as exact input and does not prove the arithmetic asymptotic producing it. The finite and noisy examples are synthetic measures. [Target and taper setup](generator63_tapered_prime_array_skeptic.md)

## Full real form

Put \(M=\nu(\mathbb R)\), \(F(t)=\int e^{-i\gamma t}\,d\nu(\gamma)\), and \(a_k(\gamma)=\sqrt{k}e^{-i\gamma\log k}-1\) for \(k\ge2\). Conjugation symmetry of the zeros and their weights makes \(\nu\) symmetric and \(F\) real and even. The input says
\[
 Q\left(\sum_k c_kR_k\right)=\int\left|\sum_k c_ka_k(\gamma)\right|^2\,d\nu(\gamma)
 \quad(c_k\in\mathbb R).
\]
If the singleton value \(C_k=Q(R_k)\) is finite for one \(k\), positivity already makes \(\nu\) finite because \(|a_k|\ge\sqrt{k}-1\). On the synthetic class the same prescription defines genuine forms on the real span. A finite linear relation among \(R_k\) would, by their jumps \((\log n)(k1_{k\mid n}-1)\), have coefficient sum zero by evaluating at a prime beyond the last index. Evaluating at the smallest remaining index with nonzero coefficient then contradicts the relation.

The singleton identity and a mass estimate are
\[
 C_k=(k+1)M-2\sqrt{k}F(\log k),\qquad
 M=\lim_{k\to\infty} C_k/k,\qquad
 |C_k/k-M|\le M(k^{-1}+2k^{-1/2}).
\]
For any single \(k\),
\[
 \frac{C_k}{(\sqrt{k}+1)^2}\le M\le
 \frac{C_k}{(\sqrt{k}-1)^2}.
\]
The endpoints are sharp over the symmetric positive class, using a symmetric pair where the phase cosine is respectively \(-1\) or \(1\).

The anchor terms cancel if the form is evaluated on a difference:
\[
 Q(R_k-R_l)=(k+l)M-2\sqrt{kl}F(\log(k/l)).
\]
Thus the full form recovers \(F\) at the logarithms of all positive rationals. Every positive rational can use numerator and denominator at least 2, and their logarithms are dense in \(\mathbb R\). Continuity of the Fourier transform follows from finiteness. Uniqueness of Fourier transforms of finite measures then recovers \(\nu\). The scalar relations and uniqueness also apply to a finite signed symmetric difference, using its total variation in the asymptotic bound. For a general measure the real form sees only its even part, because the Gram functions are even. For example \(\delta_u-\delta_{-u}\), \(u\ne0\), is invisible in the nonsymmetric signed class.

An atom at zero is included in the reconstruction. For every \(x\in\mathbb R\), Fubini and dominated convergence give
\[
 \nu\{x\}=\lim_{T\to\infty}\frac1T\int_0^T F(t)e^{ixt}\,dt .
\]
For \(x=0\) this is the ordinary one-sided time mean. The integrand averaged against an atom at \(x\) is identically one, and for every other ordinate the exponential mean tends to zero. No assumption of a nonzero minimum ordinate is needed. For the actual pure point measure, its support recovers the simple-zero ordinates and its weights recover the derivative magnitudes. Multiple zeros and derivative phases are outside these data.

## Singleton reconstruction for pure point measures

All singleton values alone recover \(F(\log j)\) from the mass. Set \(\Delta_j=\log(j+1)-\log j\) and \(T_K=\log(K+1)\). For fixed \(x\), the function \(F(t)e^{ixt}\) is uniformly continuous. Its left endpoint quadrature on cells \([\log j,\log(j+1))\), \(2\le j\le K\), has error \(o(T_K)\): the maximum variation on cell \(j\) tends to zero and the cell lengths sum to \(T_K-\log2\). The initial interval \([0,\log2]\) has bounded contribution. Consequently
\[
 \nu\{x\}
 =\lim_{K\to\infty}\frac1{T_K}\sum_{j=2}^K
     \Delta_j F(\log j)e^{ix\log j}.
\]
This recovers all atoms of any finite symmetric measure and hence the whole measure in the pure point class. Taking real parts of the sums gives the same limit.

Only the first \(K\) singleton values are needed for the \(K\)-th estimator. Use \(\widehat M_K=C_K/K\) and
\[
 \widehat F_{j,K}=\frac{(j+1)\widehat M_K-C_j}{2\sqrt j}.
\]
The change in the normalized mean is bounded by
\[
 \frac{|\widehat M_K-M|}{T_K}
       \sum_{j=2}^K\Delta_j\frac{j+1}{2\sqrt j}
 =O(M/\log K),
\]
since the sum is \(O(\sqrt K)\). This part of the error is uniform in \(x\). The quadrature and averaging limits do not supply a uniform finite-data recovery rate over all possible measures.

In the class allowing diffuse measures, singleton uniqueness fails. Choose a nonzero real even smooth frequency bump with compact support in \((-\log 2,0)\cup(0,\log 2)\). Its inverse Fourier transform \(g\) is real even and Schwartz, with integral zero and with transform zero at every \(\log k\), \(k\ge2\). The positive and negative densities of \(g\) give distinct symmetric finite measures of equal mass and identical singleton data. This ambiguity leaves every atom unchanged, as the mean calculation requires.

## Exact finite-data ambiguity

For each pair of indices the real Gram integrand is the even entire function
\[
 K_{kl}(z)=\sqrt{kl}\cos(z\log(k/l))
             -\sqrt{k}\cos(z\log k)-\sqrt{l}\cos(z\log l)+1 .
\]
At \(z=i/2\), its four contributions are \((k+l)/2,-(k+1)/2,-(l+1)/2,1\), so it vanishes there. The integrand of the form evaluated on any finite real combination is a finite real linear combination of these kernels and has the same vanishing.

Let \(p_1,\ldots,p_d\) be a basis for the span of any finite list of measured kernels. The constant function 1 is linearly independent of these kernels on any nonempty real open interval, by analytic continuation and evaluation at \(i/2\). Choose \(d+1\) distinct \(\gamma_j>0\) in any desired positive open interval such that the evaluation columns for \(1,p_1,\ldots,p_d\) are independent. Such a choice exists because the evaluation vectors span the whole coordinate space, since a linear functional annihilating all of them would give a dependence on that interval. With \(m_j=(\delta_{\gamma_j}+\delta_{-\gamma_j})/2\), solve the finite linear system for a signed measure \(\eta=\sum_j s_jm_j\) whose \(p_i\) integrals are all zero and whose mass is 1. Its positive and negative parts, with a common positive measure added if needed, give distinct finite positive symmetric profiles with the same measured data and different masses. This makes the mass limit genuinely asymptotic in the unrestricted finite-measure model.

If the mass is given independently, use \(d+2\) distinct positive nodes and find a nonzero kernel vector for the \(d\) measurements and the mass row. Now the signed difference has zero mass, so its positive and negative parts both have positive equal masses and different supports. These constructions require no atom at zero and apply in arbitrary prescribed height intervals. Their weights and ordinates are synthetic.

## Error regimes

For an observed singleton with absolute error \(\epsilon_k\), the preceding mass interval remains rigorous by using \(\max(0,\widetilde C_k-\epsilon_k)\) in the lower bound and \(\widetilde C_k+\epsilon_k\) in the upper bound. The limit \(\widetilde C_k/k\) gives the exact mass if \(\epsilon_k/k\to0\). If \(\epsilon_k=o(\sqrt{k})\), the same condition is sufficient for the atomic estimator. Using \(\widetilde C_K/K\) changes the mass error by \(o(K^{-1/2})\), and the local errors \(\epsilon_j/(2\sqrt j)\to0\) average to zero against the quadrature weights. At error scale \(O(\sqrt{k})\), two distinct equal-mass profiles have singleton differences \(O(\sqrt{k})\) and can be indistinguishable within the error bounds. Thus vanishing error after division by \(k\) alone gives a mass limit.

For full pair data, the scale of error matters. The model has the exact ray identity
\[
 \frac{Q(R_{nk}-R_{nl})}{n}=(k+l)M-2\sqrt{kl}F(\log(k/l)).
\]
With errors \(o(n)\) on every fixed pair ray and \(o(k)\) on the singletons, taking these scaled limits still recovers the exact Fourier transform. Uniform absolute errors are a special case. In contrast, arbitrarily small uniform errors in the normalized Gram entries \(B(R_k,R_l)/[(\sqrt{k}+1)(\sqrt{l}+1)]\) cannot uniformly control the total variation of the measure.

Here is a finite atomic example for that instability. Let \(N=2^r\). Start with polynomials \(P_0=Q_0=1\), and recursively set
\[
 P_{r+1}=P_r+z^{2^r}Q_r,\qquad Q_{r+1}=P_r-z^{2^r}Q_r .
\]
Their coefficients are signs and \(|P_r(z)|^2+|Q_r(z)|^2=2N\) on \(|z|=1\). The \(2N\) coefficients \(s_j\) of \(z(1-z^N)P_r(z)=\sum_{j=1}^{2N}s_jz^j\) have exactly \(N\) positive and \(N\) negative signs. The symmetric signed measure
\[
 \eta_N=\frac1N\sum_{j=1}^{2N}s_j\,\frac{\delta_j+\delta_{-j}}{2}
\]
is the difference of two mutually singular probability measures, and \(\|F_{\eta_N}\|_\infty\le 2\sqrt{2/N}\). Its mass is zero. Substitution in \(K_{kl}\) bounds the difference of all normalized Gram entries by the same \(2\sqrt{2/N}\). The form differences on finite combinations similarly obey the bound after normalization by \((\sum_k(\sqrt{k}+1)|c_k|)^2\). The two profiles retain total variation distance 2 in the norm of signed measures.

For the arithmetic approximation that supplies \(Q\), the limit in its polynomial length must first be justified for each fixed target or fixed combination. Neither the diagonal estimator nor the ray identity supplies a joint growth regime for the target indices and the polynomial cutoff.
