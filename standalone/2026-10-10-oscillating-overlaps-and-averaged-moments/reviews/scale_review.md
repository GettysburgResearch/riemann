# Independent review of the scale-averaged generalized moment criterion

Reviewed file: /workspace/scratch/5b23d9b20a3a/attack2_scale_criterion.md

Reviewed SHA-256: c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0

Reviewer: the moment-obstructions research agent, independently of the author.

Verdict: PASS for the stated conditional arithmetic implication and the abstract causal-operator theorem at this corrected hash. The previously noted measurability omission in Theorem 3.1 has been fixed. No further proof correction is required.

## Scope of the review

I read the complete note. I checked the exact replica identity, density weights, coefficient-norm convergence and inverse, moving-cutoff perturbation on finite intervals, lower-scale forcing term, scale-integrated Jensen estimate, Mellin continuation, and the cofinal-order quantifiers.

The universal compactly supported Mellin test from PR #912 is an explicit dependency of the note. Its previously reviewed nonvanishing property is used as stated here. The review does not pretend that the unproved arithmetic moment hypothesis has been established.

## 1. Replica identity and density weights

The identity \(T_vA_r=A_{rv^6}\) has the correct sign and direction. Multiplying the local inverse Euler factor \(1-\eta(p)p^{-s}\) by its geometric inverse removes coefficients divisible by \(p\). This agrees exactly with the zero-extended sixth-power factor. If \(\eta(p)=0\), the identity remains valid without any special convention.

All ideal bases \(v\) may be retained. Their chosen generators give distinct rows \(rv^6\), independently of the unit choice because every unit has sixth power one. The restriction \(Nv\le(D^h/Nr)^{1/6}\) is precisely the required row-norm restriction.

For \(R=N\operatorname{rad}(d)\), the density \(J(Y/R)/J(Y)\) is exact. From \(J(Y)=\kappa Y+O(\sqrt Y)\), its error from \(R^{-1}\) is \(O(Y^{-1/2}R^{-1/2})\) when \(R\le Y\). When \(R>Y\), it is exactly \(R^{-1}\), agreeing with the minimum in (2.2). Interpolation with exponent \(2\delta\) gives \(Y^{-\delta}R^{-1+\delta}\), as claimed.

## 2. Weighted dilation algebra

The norm of \(f(x)\mapsto f(x/a)\) in the weight \(x^{-p\sigma}dx/x\) is at most \(a^{-\sigma}\) on every finite causal interval. The power and its sign in Section 2 are correct.

The Euler factor in (2.4) has nonconstant term
\[
\frac{q^{-1+\delta-\sigma}}{1-q^{-\sigma}}.
\]
Its prime sum converges exactly under \(\delta<\sigma\). This proves the uniform majorant for the moving coefficients as well as the norm approximation to \(M\).

The inverse local factor
\[
1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}\eta(p)^jS_p^j
\]
is algebraically the inverse of (2.6). Both local products have summable nonconstant coefficient norms \(O_\sigma(q^{-1-\sigma})\), uniformly for \(|\eta(p)|\le1\). Thus both inverse identities hold in a convergent Banach algebra of causal dilations. No zero-free estimate for any \(L\)-function enters this construction.

## 3. Moving cutoff and finite-interval inversion

On functions zero below \(X_0\), the row-dependent error coefficients are uniformly bounded by
\[
O(c^{-\delta}X_0^{-\rho\delta})R^{-1+\delta}.
\]
This is sufficient for the operator-norm estimate even though the coefficients depend on \(x\). Commutativity of the moving-cutoff operator is not needed.

The factorization \(P=M(I+M^{-1}E)\) is valid as composition of bounded operators on the finite interval, with \(E=P-M\). The fixed operator \(M^{-1}\) is causal, so it preserves the support subspace. Choosing \(X_0\) large makes the Neumann inverse uniformly bounded in the upper endpoint \(T\).

The compact lower-scale part \(f_0\) is not dropped. Its image under \(P\) is controlled globally by the limiting positive coefficient majorant \(R^{-1}\), which is summable in the same weighted algebra. Consequently the uniform finite-\(T\) inverse may be applied to \(f_1\) without assuming the unknown tail is already integrable. Monotone convergence in \(T\) then proves the conclusion.

The measurability amendment is sufficient. In the arithmetic application, the finite sum defining \(A_r(D;W_*)\) is smooth locally in \(D\) and vanishes for all sufficiently small \(D\), so this hypothesis is automatic.

## 4. Extraction exponent and analytic continuation

Jensen divides the row moment by \(J(Y_r(D))\asymp_r D^{h/6}\). The dyadic integral of the resulting weighted right side has exponent
\[
k+\frac{5h}{6}+e_k-2k\sigma+\epsilon.
\]
Strict negativity is equivalent to
\[
\sigma>\frac12+\frac{5h}{12k}+\frac{e_k}{2k}
\]
after choosing the positive loss sufficiently small. The stated exponent is correct; neither an extra factor of \(k\) nor an additional row-height cost is missing.

The moving-cutoff theorem converts this integrated bound into the weighted \(L^{2k}\) norm of the fixed-row sum. Hölder then gives absolute and locally uniform convergence of its Mellin transform on \(\Re s>\sigma\). Positive lower support handles \(D\downarrow0\); a positive real-part margin controls the upper tail and all logarithmic factors needed for holomorphy.

The direct Euler identity holds at least on the overlap \(\Re s>\max(1,\sigma)\), which is sufficient for continuation. It also holds directly on \(\Re s>1\) by the elementary \(O(D)\) coefficient bound. The finite Euler-restoration factors have no zeros or poles in \(\Re s>0\). Together with the nonvanishing Mellin test, this prevents cancellation of a reciprocal-\(L\) pole. The principal \(L\)-pole creates a reciprocal zero and is harmless.

The conclusion is for a strict half-plane. Letting \(\sigma\) approach the threshold is legitimate point by point and does not require constants uniform in \(\sigma\).

## 5. Quantifiers and what remains open

The fixed row \(r\) may affect constants, including the lower threshold for the causal inverse. Uniformity in its conductor is not needed for this implication. Each \(k\) and \(h_k>0\) is fixed before passing \(D\) to infinity, so cofinal \(k\) with \(h_k=o(k)\) and \(e_k=o(k)\) gives the stated limiting half-plane without any uniform-in-\(k\) constants.

For a fixed \(\nu\), the note concludes zero-freeness to the right of one half for the corresponding row-twist family. The stronger GRH conclusion for the whole finite-order Hecke family is correctly stated under the additional hypothesis for every fixed \(\nu\), which supplies conjugates and includes any prescribed primitive finite-order character by taking \(r=1\). The Dirichlet-family consequence then follows from the usual norm-pullback factorization, with finite local factors harmless in the critical strip.

The arithmetic input is only the dyadic scale integral. The proof does not infer a pointwise moment estimate from it. The note explicitly leaves that averaged arithmetic input, including the nearly coprime balanced part, unproved. There is no hidden use of quasi-Riemann zero-freeness, a uniform reciprocal-\(L\) estimate, or a finite dominant-mode expansion.
