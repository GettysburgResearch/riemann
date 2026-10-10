# Separated moment sectors and an all-row Gauss-sum gain

**Status: proposed, source-conditional research with scoped independent AI-agent reviews.** This packet proves new component estimates and smaller sufficient signed remainders. It does not prove the full fourth moment, a new numerical zero-free boundary, the generalized diagonal moment hierarchy, or RH. The previously derived source-conditional boundary remains \(139999/160000\).

The packet is stacked on PR #919 at commit 9b04a887e171b3104a66cf57296ce5b0b2920d78. It combines that signed arithmetic frontier with the new complete-group reflection and angular estimates in PR #920, and with the existing classical and native moment machinery. Earlier published proof packets are unchanged.

## 1. The strongest new analytic result includes every row

Let \(P(D,D;k)\) be the literal balanced two-factor Gauss polynomial defined in [the raw-family note](SHORT_CUBE_RAW_GAIN.md), with its squarefree product, fixed smooth factor tests, fixed ray character and original nonunit zeros. The normalizing factor is \(D\). Here \(H\) bounds the **norm of an arithmetic row**; it is not itself the imaginary part of a zeta zero.

[The all-row theorem](ALL_ROW_COMPLETION_AND_RAW_GAIN.md) proves
\[
\boxed{
\sum_{k\asymp H}|P(D,D;k)/D|^2
\ll_\epsilon
\begin{cases}
D^{6/5+\epsilon}H^{13/15},
&1\le H\le D^{38/87},\\
D^{1+\epsilon}H^{151/114},
&D^{38/87}\le H\le D^{19/22}.
\end{cases}}
\]
The sum includes **all nonzero Eisenstein element rows**, including sixth-power copies and factors at the fixed bad primes.

For example,
\[
\boxed{
H=D^{1/2}
\quad\Longrightarrow\quad
\sum_{k\asymp D^{1/2}}|P(D,D;k)/D|^2
\ll_\epsilon D^{379/228+\epsilon}.}
\]
The earlier classical all-row envelope gives \(D^{25/12+\epsilon}\) at this height. The displayed exponent improves from \(25/12\approx2.083333\) to \(379/228\approx1.662281\), a saving of \(8/19\) in the exponent of this mean-square upper bound. The new raw estimate is \(O(D^{2+\epsilon})\) through \(H\le D^{114/151}\).

The estimate is obtained from a stronger theorem for the literal theta completion:
\[
\boxed{
\sum_{k\asymp H}|\mathcal C_{A,B}(k)|^2
\ll_\epsilon D^\epsilon
\left[
HA+\frac{H^2A}{B}\min(A,\sqrt B)^{5/6}
+\left(\frac{H^2A^2}{B}\right)^{2/3}
\right].}
\]
It is uniform for an additional original outer mask \((a,h)=1\) of polynomially bounded norm. At \(A=B=D\), the bracket is
\[
HD+H^2D^{5/12}+H^{4/3}D^{2/3}.
\]
Thus the completed energy is \(O(D^{2+\epsilon})\) through \(H\le D^{19/24}\). **The number \(19/24\) here is a row-height exponent. The desired zero-free boundary \(17/24\) remains unproved.**

### How the estimate is obtained

1. **Use exact support cancellation first.** PR #920 makes each complete projected group with negative allocation \(Ng>C_S\sqrt B\) vanish. The proof inserts this cutoff before splitting its positive allocations, cube indices, ramified valuations, or frequency dyads.
2. **Retain the Gauss coefficient at all three cusps.** The explicit primary coefficient formulas keep the cubic Gauss structure needed for the quadratic–cubic sieve, with all reflected bad-prime factors and ramified towers included.
3. **Sum the Möbius negative allocation before taking its norm.** Its infinity type is \(-3\). The conductor-uniform reciprocal estimate on every fixed line right of \(11/12\), together with a convergent operator for the moving \(e\)-exclusion, replaces the allocation cost \(G\) by \(G^\sigma\). Squaring and choosing a positive margin in terms of epsilon gives the exponent \(5/6\).
4. **Extend the calculation to repeated-prime rows.** Write \(k=sv^2\), separate \(t=(s,\operatorname{rad}v)\), and retain the remaining squarefree variable for the sieve. The potentially large local Ramanujan factor can first occur at \(p^2\mid v\). Its squared amplitude therefore has convergent weights \(J(v)/(Nv)^2\) and \(J(v)/(Nv)^{4/3}\), where \(J(v)=\prod_{p^2\mid v}Np\). The row strata are disjoint, so their squared norms are summed directly.
5. **Optimize the exact cube inverse.** Bound the short inverse analytically and regroup the long inverse with
   \[
   c_R(d)=\sum_{\substack{h\mid d\\Nh>R}}\mu_K(h).
   \]
   The long tail keeps the outer mask \((a,d)=1\), allows the inner squarefree index to overlap \(d\), and uses the classical all-row sieve. Balancing the two bounds gives the displayed raw regimes.

The local audit also resolves a tempting but incorrect obstruction: an inactive exponent-zero prime disappears from both the first-reflection denominator and the second projection period. Its only contribution is a scalar. Keeping this exact local fact permits the all-row support and norm extension.

The analytic assumptions remain explicit. The new proof uses the imported October 5 theta framework and classical sieves, and the source-conditional angular extension in PR #920. It is not an independent reconstruction or formal verification of those inputs. The weaker completed bound, with exponent \(1\) instead of \(5/6\) on \(\min(A,\sqrt B)\), needs no angular reciprocal input and permits arbitrary row-independent subpower outer coefficients.

## 2. A further part of the actual fourth-moment remainder is controlled

The [cross-side sector theorem](CROSS_SIDE_SEPARATION_SECTOR.md) concerns the actual Möbius/sextic inverse family over all nonzero rows. It preserves both original within-side restrictions
\[
N(n_1,n_2)<C,\qquad N(m_1,m_2)<C.
\]
Assume the pinned native second moment at every smaller column scale in the same row range. If a row-uniform pointwise exponent \(1/2<b\le1\) is also supplied, the complete signed covariance with one cross gcd at least \(D/R\) satisfies
\[
\boxed{|\mathcal G_{11}(C,D/R)|
\ll_\epsilon HD^{2+\epsilon}R^{2b-1}.}
\]
At \(b=1\) the pointwise premise is elementary counting. At \(b<1\) it is an additional uniform analytic input, with its stated conductor quantifiers.

The proof does not remove the side restrictions before applying cancellation. It derives an exact gcd decomposition of a two-factor polynomial \(F_{q,C}\), proves
\[
\|F_{q,C}\|_{\Phi,H}^2
\ll_\epsilon D^\epsilon HD(D/Nq)^{2b},
\]
and uses the literal identity
\[
\mathcal G_{11}
=\sum_{Nc\ge D/R}\sum_{(e,cS)=1}\mu_K(e)
\sum_u\Phi(u/\sqrt H)\mathbf1_{(u,ce)=1}|F_{ce,C}(u)|^2.
\]
Here \(c,e\) are squarefree and outside \(S\), with \((c,e)=1\); thus \(ce\) is in the stated domain of \(F_{ce,C}\).
The zero mask and Möbius sign are retained. The remaining ideal tails converge because \(2b>1\).

For the previous cutoff \(C=D^{(6-h)/7}\), \(1<h\le11/10\), take \(R=D^r\) with \(0\le r<(1+h)/14\). The four cross-gcd events are disjoint inside the hard-conductor domain, by exact prime-exponent and common-divisor inequalities. Their **union** therefore has the same cost \(R^{2b-1}\). A supplied \(b=7/8\) gives \(R^{3/4}\), improving the earlier \(R\) bound.

Consequently a sufficient remaining signed fourth-moment domain can impose all of
\[
\begin{gathered}
N(n_1,n_2),N(m_1,m_2)<D^{(6-h)/7},\\
g_1\ne1,\qquad Ng_1\sqrt{Ng_2}>D^h,\\
N(n_i,m_j)<D/R\quad\text{for all }i,j.
\end{gathered}
\]
Here \(g_1,g_2\) are exactly the pinned conductor-accounting variables. If the one-sided signed dyadic average on this remaining domain has excess \(e\ge0\), the total fourth-moment excess is
\[
\lambda=\max\{e,(2b-1)r\}.
\]
For a fixed growing subpower \(R\), the new controlled sector has zero exponent cost. The residual average is still open. Deleting terms from a signed sum has not been treated as a monotonic improvement of its absolute value.

## 3. A sharper estimate for higher-moment incidence patterns

[The subset-product theorem](SUBSET_PRODUCT_INCIDENCE.md) treats several singleton factors together. Put \(P=\prod_iX_i\) and \(P_J=\prod_{j\in J}X_j\). For every nonempty subset \(J\),
\[
\boxed{
\|B_C(\mathbf X)\|_{2,H}^2
\ll_\epsilon D^\epsilon HP
\left(\frac{P}{P_J}\right)^{2b-1}
\left[
1+\frac{P_J}{H^{5/6}}
+\left(\frac{P_J^2}{H}\right)^{1/3}
\right].}
\]
This uses the classical all-row sieve and the stated row-uniform pointwise bound on omitted factors. It preserves every collision in the intermediate physical product. The exact forward Euler correction is bounded on the realized finite horizon even when several weights equal \(1/2\), and it keeps the moving exclusion \(C\). The native second moment is needed only when the older one-axis bound is also included in the minimum.

For an actual sixth-moment triangle of pair overlaps, take
\[
H=D^{21/20},\qquad Nc_{12},Nc_{13},Nc_{23}\asymp D^{5/24},
\qquad X_1,X_2,X_3\asymp D^{7/12}.
\]
At supplied \(b=7/8\), estimating two singleton factors together improves the incidence portion's bound from
\[
HD^{3+7/8+\epsilon}
\quad\text{to}\quad
\boxed{HD^{3+623/720+\epsilon}.}
\]
The saving is \(7/720\), against both the previous native one-axis and full classical estimates for this portion. The full common gcd is one, so this is an additional configuration.

The note proves an aggregate selector using the minimum over all subsets and the older bound. Its remaining signed average has the same exact conditional extraction interface as PR #919:
\[
\Re s>\frac12+\frac{5h}{12k}
+\frac{\max\{\lambda,e\}}{2k}.
\]
The new selector expands the controlled portion at a prescribed positive loss. It does not improve the worst balanced top-scale core or prove a new zero-excess region. In particular, no cofinal cancellation estimate has been inferred merely from the finite subset optimization.

## 4. Exact remaining goals

The full fourth-moment target is still
\[
M_4(D,D^h)\ll_\epsilon D^{h+2+\epsilon},
\qquad h>1\text{ arbitrarily close to }1,
\]
or its sufficient one-sided signed dyadic average. The reviewed extraction would then give the strict boundary \(17/24\) in the limiting sense described in PR #919.

This packet advances three distinct interfaces. They have not been composed by silently identifying their coefficient classes:

| New result | What still needs to be proved |
|---|---|
| Cross-side gcd sector with both side thresholds | The signed average over the separated hard-conductor remainder |
| Proper-subset higher-moment estimates | Cancellation in the remaining top-scale nearly coprime core, with losses sublinear in \(k\) for a cofinal hierarchy |
| All-row completed and raw two-axis gain | The moving inner exclusions \(q\), auxiliary \(f\), and their exact A2 overlaps, followed by the actual Möbius Poisson comparison at every required scale |

The adverse initial dual height is near \(D^{3-\theta}\). The raw short-height regimes proved here do not control that range. The extra A2 labels are also different from the repeated-row factors that have now been handled. A new quantitative band in zero height would additionally require uniform control of constants as the moment order grows; fixed-order estimates alone do not supply it.

## 5. Proofs, review, and reproduction

The [all-row addendum](ALL_ROW_COMPLETION_AND_RAW_GAIN.md) and [independent local derivation](ALL_ROW_LOCAL_AUDIT.md) supersede the squarefree-only limitations of their prerequisite notes **for the literal family they specify**. The earlier squarefree notes remain byte-for-byte as reviewed and provide the intermediate proofs and sharper squarefree-row example.

| File | Role |
|---|---|
| [Cross-side separation](CROSS_SIDE_SEPARATION_SECTOR.md) | Actual signed-sector theorem |
| [Subset-product incidence](SUBSET_PRODUCT_INCIDENCE.md) | Whole-product estimate, correction kernel, and higher-moment selector |
| [Pruned coupled mean square](PRUNED_COUPLED_MEAN_SQUARE.md) | All-cusp and angular estimates, initially on squarefree rows |
| [Short-cube raw gain](SHORT_CUBE_RAW_GAIN.md) | Exact inverse regrouping and squarefree-row optimization |
| [All-row local audit](ALL_ROW_LOCAL_AUDIT.md) | Independent scalar, period, and summability derivation |
| [All-row completion and raw gain](ALL_ROW_COMPLETION_AND_RAW_GAIN.md) | Full row extension and quantitative raw bound |
| [Integration review](INTEGRATION_REVIEW.md) | Root's independent mathematical and composition review |
| [Validation](VALIDATION.md) | Scope of finite diagnostics and byte verification |

Each mathematical note has a separately named review report binding its exact SHA-256. These are scoped AI-agent reviews, not external peer review or proof-assistant certificates.

[SOURCE_LOCK.json](SOURCE_LOCK.json) pins seventeen source files. Five adjacent-source files are preserved under [sources](sources/README.md); the remaining dependencies have exact copies in the inherited branch. [MANIFEST.json](MANIFEST.json) binds the deliverable bytes. The deterministic finite diagnostic checks the new gcd identities with sixth-root phases and zeros, local conductor inequalities, and the rational exponent ranges. It does not test or certify an infinite analytic estimate.

No integrated status, accepted-results file, or formal proof has been changed by this packet.
