# A high-dual band from direct sixth-root label aggregation

**Status: source-qualified partial estimate.** This is a partial estimate for the physical signed-dual reduction, not a proof of the inverse moment or a new zero-free region. It assumes paper 5 v3 Theorem 5 (9.3), the original physical Poisson/profile identities, finite-sector reciprocity and the growing-k label aggregation reviewed in [the earlier direct-theta note](../2026-10-29-low-dual-theta-bound.md). In particular the theorem's allowed puncture, row/label weights, and all common-profile separations must match the displayed source conventions. Its recent analytic inputs and that matching are not externally verified here. High_match and Other_families independently checked the fixed-a puncture, common profiles, label multiplicity and normalization under those inputs.

## Candidate bound

Use \(P=Y^{6/5}\), dyads \(Nd\asymp D_0\), \(Nk\asymp K\), \(Ng\asymp G\), \(Nb\asymp B\), and the physical dual cutoff \(H\ll Y^\epsilon P^2K/(YD_0^2)\). Write
\[
 d=kd',\qquad v=b a^6,\qquad Na\ll (H/B)^{1/6}.
\]
Here b is sixth-free, a may share primes with b, and nonempty support has \(B\ll H\). The source characteristic is multiplicative with its zero extensions. Thus
\[
 \chi_n(vk)=\chi_n(bk)\,\mathbf1_{(n,a)=1},
\]
including all overlapping prime masks. The original d-puncture contributes \(d'\), while \(\chi_n(gk)^4\) already carries the k-puncture. For each **fixed** a and d′ use paper 5's column puncture \(Q=\operatorname{rad}(ad')\), label \(f=gk\), row \(h=bk\), label scale \(F\asymp GK\), row scale \(\ll BK\), and residual column scale \(D\asymp P/(D_0G)\). The label f and puncture Q are squarefree; f is squarefree because \((g,k)=1\). No coprimality of a with b, f or d′ is assumed. The stated source theorem imposes no \((Q,f)=1\) condition: overlap merely duplicates zero masks.

As in the growing-k proof, the decomposition \(k\mid\gcd(f,h)\) has divisor-bounded multiplicity. One first fixes a, d′ and finite ray sectors and uses logarithmic Fourier separation of the physical kernel to get common smooth column profiles; after the nonnegative square, discard the common row masks and the constraints \(k\mid h\) and \(k\mid f\). The first alternative of (9.3), with divisor-bounded label weight and puncture \(Q=\operatorname{rad}(ad')\), would then give
\[
 \sum_{f\asymp GK}\sum_{Nh\ll BK}|P_{h,f}(D;\operatorname{rad}(ad'))|^2
 \ll Y^\epsilon GK\bigl(BK+D\,GK\bigr).
\]
The original physical normalization is \(Y/(PKG)\). Summing over \(O(Y^\epsilon D_0/K)\) possible d′ and the possible sixth roots a gives
\[
 \boxed{\quad
 \mathcal D_{D_0,K,G,B}\ll Y^\epsilon (H/B)^{1/6}
       \left(Y+\frac{Y D_0 B}{P}\right).\quad}\tag{1}
\]
The principal-pair restoration, original-sector Cauchy, separately budgeted diagonal, nonnegligible Poisson range and source profile/height constants are exactly the separate qualifications of the earlier growing-k argument. High_match checked that, for fixed a,d′, the column window depends on \(Nd'\,Nf\,Nn/P\) and the physical dual kernel on \(Na^6\,Nh\,Y/(Nf^2Nn_1Nn_2)\), so the source Fourier separation makes the profiles independent of the factorization \(k\mid\gcd(f,h)\).

Writing \(D_0=Y^d\), \(K=Y^\kappa\), \(B=Y^b\), and using \(\log_YH\le7/5+\kappa-2d+\epsilon\), (1) has exponent at most the maximum of
\[
 \frac{37}{30}+\frac\kappa6-\frac d3-\frac b6,
 \qquad \frac1{30}+\frac{2d}{3}+\frac\kappa6+\frac{5b}{6}.\tag{2}
\]
On the target residual core \(d,\kappa\ge0\), \(\kappa\le d\), \(d+6\kappa/5\le7/50\), the first expression is at most \(21/20\) for \(b\ge11/10\), and the second is at most \(21/20\) for \(b\le277/250\). Thus, subject to the full audit above, this supplies a separate **high-dual band**
\[
 \frac{11}{10}\le b\le\frac{277}{250}\tag{3}
\]
with target exponent \(21/20+\epsilon\). This is disjoint from the earlier certified lower interval and does not control the gap or larger b.

For \(E_* =19949123/18750000\) and the θ-residual core \(d+6\kappa/5\le1925877/15625000\), the analogous proposed band is
\[
 \frac{3175877}{3125000}\le b\le\frac{88917107}{78125000}.\tag{4}
\]
At fixed positive distance from both endpoints, its exponent is strictly below \(E_*\) after choosing the source losses sufficiently small. These bands remain conditional on the named source and physical interfaces, and they do not prove an individual Hecke or Dedekind zero-free region.

## The second source alternative closes the low-core gap

The source's second alternative in (9.3) gives, for the same fixed a,d′ and label/row enlargement,
\[
 GK\left[BK+BK\,GK\sqrt{NQ}\right],\qquad
 Q=\operatorname{rad}(ad').
\]
It is essential to retain the moving puncture cost: \(\sqrt{NQ}\le\sqrt{Na\,Nd'}\). Using ideal counting to sum the square roots over a and d′, the same physical normalization gives two terms bounded by
\[
 Y^\epsilon\left[\frac{YD_0B}{P}(H/B)^{1/6}
 +\frac YP\,B G K^{1/2}D_0^{3/2}(H/B)^{1/4}\right].\tag{5}
\]
In logarithmic variables they have exponents
\[
 \frac1{30}+\frac{2d}{3}+\frac\kappa6+\frac{5b}{6},\qquad
 \frac3{20}+d+g+\frac{3\kappa}{4}+\frac{3b}{4}.\tag{6}
\]
The actual residual core includes \(d+g+6\kappa/5\le C\), so both \(2d/3+\kappa/6\) and \(d+g+3\kappa/4\) are at most their respective values at \(d=C,\kappa=g=0\). The second expression is the restrictive one in the following ranges. For \(C=7/50\), (5) is \(\ll Y^{21/20+\epsilon}\) uniformly for
\[
 0\le b\le\frac{76}{75}.\tag{7}
\]
For the θ-residual \(C=1925877/15625000\), it is strictly below \(E_*\) when
\[
 0\le b<\frac{74127853}{70312500}.\tag{8}
\]
Both assertions inherit the source and physical-interface qualifications above, including the possibility of a squarefree puncture sharing primes with f. Their union with the first-alternative bands does not control all large b.

For E21, the two displayed sixth-free-core intervals leave the gap \(76/75<b<11/10\). For θ, the second-alternative interval overlaps the strict interior of (4), so their union covers \(0\le b<88917107/78125000\), with fixed endpoint margins and source losses chosen accordingly. This overlap still leaves larger sixth-free-core b uncontrolled.

## Higher sixth-power extraction and a dual-norm range

The same source permits arbitrary row valuations, so the sixth-root decomposition is not essential to the direct-theta estimate. For any **fixed** positive integer m, decompose each dual ideal uniquely as \(v=b_m a^{6m}\) with \(b_m\) \(6m\)-free, and put the good squarefree puncture \(Q=\operatorname{rad}(ad')\). The zero-preserving identity \(\chi_n(a^{6m})=\mathbf1_{(n,a)=1}\) remains valid. Repeating the same fixed-a,d′ label aggregation and using the first source alternative gives
\[
 \mathcal D_{D_0,K,G,B_m}\ll Y^\epsilon (H/B_m)^{1/(6m)}
       \left(Y+\frac{Y D_0 B_m}{P}\right).\tag{9}
\]
The units and finite bad-prime sectors are treated as in the physical source; n is already good and Q contains only good primes. The fixed source profile and its derivative orders are chosen before Y grows.

For m=5, the first exponent in (9) is at most \(157/150<21/20\) throughout the E21 core, and the second is at most \(21/20\) when \(\log_YB_{5}\le1609/1450\). On the θ core the corresponding strict threshold is \(\log_YB_{5}<516678519/453125000\). Here \(B_5\) measures the 30-free part, not the sixth-free \(B\) used in (7)–(8); the two partitions must not be identified. Rows with larger 30-free part remain open, and the displayed rates give no new individual zero-free region by themselves. High_match independently checked the second-alternative summation, both exact thresholds, the 30-free ideal decomposition and its source masks under the stated inputs.

The immediate dual-norm corollary of the m=5 estimate is **superseded** by the previously reviewed full-row first-alternative bound (11) in [the earlier note](../2026-10-29-low-dual-theta-bound.md). That bound is \(Y^\epsilon[Y+YD_0H/P]\), and therefore already covers all physical dual rows of norm \(\ll Y^{111/100}\) on the E21 core, and norm \(\le Y^{106940353/93750000-\eta}\) on the θ core for fixed \(\eta>0\). The 30-free-core statement is a different restriction and is retained separately.

## The remaining squarefree top scale

The source-level bounds above still leave a simple top-scale obstruction to this particular positive approach. At \(d=g=\kappa=0\), take dual rows with squarefree \(v\) at \(Nv\asymp H=Y^{7/5}\). Then every extraction \(v=b_m a^{6m}\) has \(a=1\) and \(B_m\asymp H\). The unlabelled paper 5 row-scale estimate allows \(\sum_v|P_v(P)|^2\ll Y^\epsilon H\); with physical normalization \(Y/P=Y^{-1/5}\), this is \(Y^{6/5+\epsilon}\), above \(Y^{21/20}\). Both label alternatives contain the same row-size face, and root counting gives no saving on this slice.

An abstract nonnegative model with \(|P_v|=1\) on \(\asymp H\) rows saturates that positive row-size input. It is not a construction of theta coefficients or a lower bound on the physical signed sum; it only shows that the displayed positive row-norm estimate by itself does not yield the target here. A further route must use additional arithmetic information, the physical oscillatory kernel, or cancellation across the signed projector.
