# Independent reconstruction of the two unfiltered-trace refutations

**Reviewer:** the bilinear-conductor subagent, which did not author the three notes reviewed below. This is a same-team mathematical review, not external certification or a proof-assistant check. The reviewer separately authored the conjugate-pair conductor note in this research wave; that note is not an input to either refutation.

**Verdict:** no load-bearing defect found in the exact versions listed below. Both counterexamples use an allowed fixed source specialization and refute the stated pointwise unfiltered contracts. Neither establishes a lower bound for the complete norm-filtered moment, nor a failure of that moment conjecture, nor a new zero-free boundary. The imported prime ideal theorem is sufficient and is independent of the requested generalized moment.

## 1. Exact review target and source binding

The review applies to these byte-identical targets only:

| Target | SHA256 |
|---|---|
| `EULER_TRACE_RESONANCE.md`, read from the extraction author's `pass3_euler_trace_resonance.md` | `c8931a93f3fc47805143ab4074ca4e315656a87e58abd5e0e7ba59c03079fb10` |
| `RESONANT_SHORT_TRACE.md` | `1c043c4650e72d9c78daef4111a3a2485c6f5d285a1ca2afee62283c9286a70f` |
| `SHORT_FACTOR_NONSMALLNESS.md` | `0af49f68a90bc19253e6543abd2e8d8af295a2bb133c5ebb59686e516655a935` |

The following exact source files were reread, rather than relying only on the new notes' account of their contracts:

| Source at PR #911 commit `2f8b6a3898a722d0602a91dea73bac344a3bb7dd` | SHA256 |
|---|---|
| `PRIME_SLOT_CANCELLATION.md`, especially P1, P2, P5 and P8 | `d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13` |
| `COMPLEMENTARY_SHORT_TRACE_CONTRACT.md`, CT1–CT4 | `968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c` |
| `SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md`, SC1–SC4 | `c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac` |
| `WIDE_SUBCRITICAL_TUBE.md`, WT1–WT3 | `53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02` |

The source majorant was checked directly in `CONDUCTOR_SECTORS.md`, Section 2, at PR #914 commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, SHA256 `c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`. It is a fixed nonnegative radial smooth function, at least one on the unit disk. Its specified compact support is stronger than the Schwartz property used in the two new notes.

For the one imported prime-distribution input, I opened the primary source [Alex Burgin, *A New Elementary Proof of Landau's Prime Ideal Theorem, and Associated Results*, arXiv:2406.08565v2](https://arxiv.org/html/2406.08565v2). Theorem 1, Lemma 1, and the explanation following Lemma 1 supply the stated classical conclusion `pi_K(x) ~ x/log x`. I checked that the cited conclusion is present; I did not reprove the classical theorem or certify the paper's complete proof. No effective prime-counting error term is needed by the new arguments.

## 2. The two objects and their actual quantifiers

The distinction between the objects is essential:

| Item | Object inside the complete row trace | Range refuted |
|---|---|---|
| Original P13 | The finite Euler numerator `C` itself | Every fixed `k >= 1`, at `Re s_i = 1/2`; the companion proves the broader range `0 < sigma_0 < 1` |
| Subcritical CT1 | `Q_coll product_i T_i`, with `Q_coll = C / product_i B_i` and the literal short Möbius polynomials `T_i` | Every fixed `k >= 2`, `1/3 < sigma < 1/2`, outside the specified WT1 common conjugate tube |
| Short-factor lemma | A product of bounded-coefficient, norm-truncated ideal Dirichlet polynomials with constant coefficient one | A simultaneous lower value on a predetermined small frequency grid; no prime theorem needed |

P13 has no physical column tests inside `C`. CT1 likewise has no column tests inside its trace, and its `T_i` use the common cutoff `Y`, even when an incidence mask makes a physical column scale smaller. These points are explicit in the old contracts. The new notes preserve those objects exactly. In particular, they do not substitute an arbitrary coefficient sequence for the source Möbius polynomial when applying the short-factor lemma.

The trivial finite-order datum `nu = 1` is allowed by the source. A counterexample for this one fixed datum suffices to refute a proposed theorem having the stated source-wide scope. The notes do not prove the same resonant lower bound for every fixed nontrivial twist.

The original row range is `H = D^h`, `1 < h <= 11/10`, with `Y = bD` and fixed positive `b`. Both arguments work for every fixed positive `h`, so they cover that source range. They require no uniformity in `k`, in the approach to a real-part endpoint, or in their possibly enormous eventual threshold.

## 3. The large mask is fixed and is a legal source allocation

For the real part under consideration, choose a fixed threshold `P_0` for which

\[
2kq^{-\sigma}\le\frac12\qquad(q>P_0).
\]

Here `sigma` may be `sigma_0` in the P13 companion. The ideal `Q` is the product of the finitely many good prime ideals of norm at most `P_0`. It is squarefree and prime to the source bad set. It does not depend on `Y`.

The allocation

\[
q_{\{1,k+1\}}=Q,\qquad q_I=1\quad(I\ne\{1,k+1\})
\]

meets the pairwise-coprime incidence rule. Its only nontrivial column masks are `c_1 = c_{k+1} = Q`. Thus the actual source requirement `Nc_i <= Y` is satisfied for every `Y >= NQ`. The general norm bound `NQ <= Y^k` follows as well. There is no requirement that `NQ` be at most the fixed prime threshold `P_0`.

This resolves the most plausible quantifier objection. The product norm can be exceptionally large, but it remains fixed before the large-scale limit. The contracts are asserted at all sufficiently large scales; a counterexample beginning beyond this fixed norm still contradicts them. Even a constant allowed to depend on this one fixed `Q` would not rescue a polynomial upper bound.

The source exterior row multiplier is exactly

\[
\chi_Q(u)\overline{\chi_Q(u)}=\mathbf1_{(u,Q)=1}.
\]

The two exterior Möbius factors multiply to `mu_K(Q)^2 = 1`. For the selected trivial datum there is no additional exterior twist. This is an actual cross-pair incidence contribution, with its original nonunit mask. No arbitrary row selector or artificial prime deletion has been introduced.

## 4. Positivity is proved for the complete actual row trace

On the paired plane `t_(k+j) = -t_j`, the normalized variables at an eligible prime not dividing `u` form the multiset

\[
v_1,\ldots,v_k,\overline v_1,\ldots,\overline v_k,
\qquad |v_j|=1.
\]

Consequently the local numerator is at least `1 - 2k q^(-sigma) >= 1/2`, while the single-factor denominator is

\[
\prod_{j=1}^k|1-q^{-\sigma}v_j|^2>0.
\]

A prime dividing the row has every slot value zero, so its local numerator and denominator are both exactly one. Hence the finite Euler numerator is positive on every row, and the collision ratio is positive on every row. In the CT1 trace the actual right short polynomial is the conjugate of its paired left polynomial; the full short product is therefore

\[
\prod_{j=1}^k|T_{Y,u}(\sigma+it_j)|^2\ge0.
\]

Multiplication by the exterior coprimality indicator and the nonnegative source majorant preserves nonnegativity. This proof does not replace a signed sum by a sum of absolute values. It proves that the original complete trace happens to be nonnegative term by term at these frequencies.

The row `u = 1` remains in the source sum, has exterior weight one, and has spatial weight at least one for `H >= 1`. A lower bound from that row is therefore legitimate. There is no missing argument controlling cancellation from other rows.

Both revised notes also settle convergence. For fixed `Y`, the finite Euler products and short polynomials have finite bounds uniform in the arithmetic row. Every collision denominator is bounded away from zero by a finite product of positive factors `1 - q^(-sigma)`. The Schwartz lattice sum is absolutely convergent; with the source compact majorant it is actually finite. Thus termwise positivity and the unit-row comparison apply to a well-defined trace.

## 5. Independent reconstruction of the first-order P13 growth

At row one and common left frequency `pi/log Y`, every eligible prime contributes

\[
1-2kq^{-\sigma_0}\cos\!\left(\frac{\pi\log q}{\log Y}\right).
\]

For `Y^(3/4) < q <= Y`, the cosine is at most `-1/2`. The logarithm of this factor is at least `(k/2)q^(-sigma_0)`. At smaller eligible primes it is bounded below by `-4kq^(-sigma_0)`. The mask ensures the elementary logarithm inequalities apply; no endpoint Taylor remainder is being suppressed.

For sufficiently large `Y`, all fixed excluded primes lie below `Y^(3/4)`. The prime ideal theorem gives at least a fixed positive multiple of `Y/log Y` prime ideals in `[Y/2,Y]`. This interval is eventually contained in the positive region. Its contribution is therefore at least a positive multiple of

\[
\frac{Y^{1-\sigma_0}}{\log Y}.
\]

By the fixed-field ideal count and partial summation, the entire possible negative prefix is `O(Y^((3/4)(1-sigma_0)))`. It is lower order whenever `0 < sigma_0 < 1`. Exponentiating gives the stated lower bound for the retained row and hence the complete trace.

At the critical line this is `exp(c sqrt(Y)/log Y)`. Every component of the frequency vector is `O(1/log Y)`, so a fixed polynomial frequency weight is bounded. Since `H D^A` is a fixed power of `Y`, the lower bound contradicts every enlarged P13 bound of the displayed polynomial form.

This resonance is on the exact common conjugate slice. It does not contradict P5: P5 bounds `C / product_i B_i`, whereas P13 bounds `C`. An exponentially large single-factor product can coexist with the ratio suppression already proved in P5. The companion handles `k = 1` correctly; its fixed cross-pair allocation is still permitted.

## 6. Independent reconstruction of the second-order CT1 growth

For `k >= 2`, put `n_+ = ceil(k/2)`, `n_- = floor(k/2)` and `d = n_+ - n_-`. The intended high-prime vector has `2n_+` signs `+1` and `2n_-` signs `-1`. Its complete pair sum is

\[
\frac{(2d)^2-2k}{2}=-(k-2d^2)=-\gamma.
\]

The constant `gamma` is positive: it is `k` for even `k`, and `k-2 >= 1` for odd `k >= 3`. Thus the omission of `k = 1` is material and correctly stated.

Take the two left clusters at `t` and `t + pi/log Y`, with the stated multiplicities. Over the interval `|t| <= 1/(100k^2 log Y)` and prime norms `Y^(1-1/(100k^2)) <= q <= Y`, each normalized variable is within `(1+pi)/(100k^2)` of its designated sign. Each pair product changes by at most twice that amount. The total error is strictly less than `1/5`, since `pi < 4`; it is less than `gamma/2` for every allowed `k`. The pair sum is real because the variables occur with their conjugates. It remains at most `-gamma/2` uniformly throughout the central interval.

The local logarithm calculation is

\[
\log\frac{1-x\sum_i v_i}{\prod_i(1-xv_i)}
=-x^2\sum_{i<j}v_iv_j+O_k(x^3).
\]

The linear terms cancel exactly. The quadratic identity is the ordinary expansion of `(sum_i v_i)^2`; no pair is omitted. Pairing the denominator logarithms first makes this a real logarithm of a positive quantity. The mask supplies the uniform smallness needed for Taylor expansion. The prime sum of the remainder converges because `3 sigma > 1`.

Writing `rho = 1 - 2 sigma > 0`, the positive high-prime contribution is at least `c Y^rho/log Y`. The earlier-prime contribution is bounded in absolute value by `C Y^(a_k rho)`, where the fixed `a_k < 1`. The latter is negligible. This proves exponential collision growth on the whole central interval, with no dependence on selecting the successful short-factor frequency afterward.

The two clusters have separation `pi/log Y`. WT1 permits a common left center of radius only `kappa/log Y`, with `kappa < arcsin(1/sqrt(2k)) < pi/2`. Since both clusters are nonempty, their simultaneous membership would require `pi <= 2kappa`, which is impossible. The countervectors lie in the exact complementary-frequency region asserted by CT1.

## 7. The simultaneous non-smallness lemma closes the actual remaining factor

I reconstructed the short-factor argument rather than assuming that a Möbius polynomial is nonzero near the chosen frequencies.

First, the number of Eisenstein ideals of an integer norm is at most the ordinary divisor function, as is seen separately at split, inert and ramified rational primes. Thus

\[
\zeta_K(4)-1\le\zeta(4)^2-1
\le(53/48)^2-1=505/2304<1/4.
\]

Every permitted polynomial is within `1/4` of one at real part four, uniformly in its imaginary part, its exclusions and its row. Its modulus there is at least `3/4`. This uses the actual constant coefficient one; it does not assume nonvanishing of an asymptotic Euler product.

For a product of `m` such polynomials, expansion over ordered ideal tuples shows that every exponential frequency is between zero and `m log Y`. The derivative bound

\[
|F_Y^{(N)}(s)|\le C_{K,\sigma}^mY^{m(1-\sigma)}(m\log Y)^N,
\qquad \Re s\ge\sigma,
\]

is valid for every derivative order, uniformly in arbitrary imaginary shifts. The shifts only multiply coefficients by phases.

With `N = ceil(100m log Y)` interpolation nodes on the stated short vertical segment, the remainder at the anchor four is bounded by the derivative bound times `5^N/N!`. The complex divided-difference formula used here is valid on the convex hull: repeated straight-segment integration gives the integral of the `N`th derivative over a barycentric simplex of volume `1/N!`. No invalid real mean-value theorem for a complex function is used.

The resulting ratio is at most `e/20 < 3/20`. Its `N`th power dominates the possible factor `Y^(m(1-sigma))`, so the remainder is uniformly `o(1)`. The anchor is bounded below by `(3/4)^m`, and hence the interpolant at four has a fixed positive lower modulus.

The exact Lagrange denominator product at the equally spaced nodes is `Delta^(N-1) j!(N-1-j)!`. Summing its reciprocal gives the binomial factor used in the note. The total interpolation amplification is at most

\[
\left(10e\log Y/\epsilon\right)^{N-1}
=\exp[O_{m,\epsilon}(\log Y\log\log Y)].
\]

At least one predetermined node must consequently satisfy the stated lower bound. Applying this argument to the entire product, with `m = k` and the two prescribed shifts, handles simultaneous zeros correctly. It is not necessary to find a different good point for each factor.

The successful node lies in the central interval on which the collision lower bound was uniform. The complete positive trace is therefore at least

\[
\exp\!\left(c\frac{Y^\rho}{\log Y}
-C\log Y\log\log Y\right).
\]

The negative term is negligible for fixed positive `rho`, yielding the CT1 contradiction. The optional positive-measure corollary of the interpolation note is also consistent: its derivative bound supplies a small one-dimensional interval. That corollary is not needed for the pointwise refutation and does not supply a full-dimensional signed Mellin integral bound.

## 8. Boundaries that must survive any summary or promotion

1. These are asymptotic counterexamples to the exact pointwise contracts P13 and CT1. Finite local tests cannot by themselves prove their prime-product growth.
2. P13 is refuted at the critical line for every fixed `k >= 1`. The displayed second-order CT1 argument applies to `k >= 2` and `1/3 < sigma < 1/2`; it does not itself refute a critical-line short-trace contract.
3. The fixed mask is legal only once `Y >= NQ`. The proofs explicitly allow a sufficiently large threshold depending on fixed parameters; no useful effective threshold is established.
4. Every original row is retained, with its nonunit zeros. Positivity of the full trace at the selected vectors is the step that permits the unit-row lower bound.
5. The current WT1 tube estimate survives because the CT1 resonance is outside its tube. The P13 common-slice ratio estimate survives because it estimates a different factor.
6. Complete column norm filtering is absent from both refuted trace objects. A lower bound on a paired frequency locus cannot be transferred to the signed, complete multivariate Mellin integral. The exact norm-filtered identities and native moment conjecture are not contradicted.
7. The proofs use the classical fixed-field prime ideal theorem, not the repository's proposed generalized moment, theta foundation, RH, or a new subcritical zero-free assertion.

No mandatory correction to the reviewed exact versions was identified. The substantive value of the refutations is diagnostic: the unfiltered pointwise route has asked for a statement that is false even after allowing any fixed polynomial loss. Further work must address the physical norm horizons or the complete signed frequency cancellation, rather than continue attempting to prove those same uniform contracts.
