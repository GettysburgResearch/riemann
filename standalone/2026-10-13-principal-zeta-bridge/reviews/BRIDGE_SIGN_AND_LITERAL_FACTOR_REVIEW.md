# Frozen-source review: ordinary-zeta capture and literal collision factors

**Disposition:** PASS at the precise scopes stated below. No correction to the reviewed source bytes is requested.

**Reviewer:** descent_synthesis, a collaborating AI research agent. This is a mathematical scope and proof review, with a replay of the specified exact finite checker. It is not external peer review, a Lean formalization, an independent proof of RH, or an independent reimplementation of the checker.

**Frozen source commit:** ea94f3e40b2755de0ffb9ac7727faa820e0c4cd0.

**Verified Git tree:** 6622be6afbf5e293a07c71b2a9b556640557cc3f.

All paths below are relative to standalone/2026-10-13-principal-zeta-bridge/ in that commit. The source bytes were obtained with git show; working-directory similarity was not used as a substitute.

| Reviewed manuscript | Exact SHA-256 |
|---|---|
| EXACT_ZETA_BRIDGE_AND_SPARSE_CAPTURE.md | a32df720f2d8b4229ac4bdfd18cbe9af18178aed7dfca25c6787632ab98ab9f9 |
| SIGN_QUANTILE_CAPTURE_FOLLOWUP.md | 653ddafdb9ba9a0ab03b92dd1e998de4674d30297d4ca008c39db44eb6cea5bd |
| SHIFTED_COLLISION_AND_LITERAL_SHORT_FACTORS.md | 395bbba988ab81f89ab2cc922d6f1ac070ed05dcbd7efbbd0e7a89d9e4153d46 |

## 1. Exact ordinary-zeta bridge and sparse absolute capture

The finite coefficient argument is correct. The principal ideal Möbius series with the original deleted prime ideals is \(1/(\zeta_K P_S)\). The fixed \(\chi_{-3}\) dilation filter and the complete finite restoration multiply it by \(L(s,\chi_{-3})P_S\), giving \(1/\zeta(s)\). The split, inert, and ramified factors agree. Distinct split prime ideals with equal norms retain their repeated factors.

The principal sixth-power identity is valid with its stated condition \((w,S)=1\). The inverse indices contain every prime power supported on \(w\); they are not restricted to squarefree ideals. The finite causal sums commute with restoration. General nonprincipal filtered rows are not substituted for the ordinary-zeta detector.

The rough-annulus density and limiting mean of \(K_\alpha\) follow from the pinned exact replica source, with a fixed \(Q\) chosen before the scale varies. The majorant is summable for each \(\alpha>0\), and the eventual mean bound gives at least \(1-\gamma/4\) contractive bases. No growing-\(Q\) estimate is silently assumed.

The derivative count after filtering includes \(O(X\log X)\) ideal/integer pairs, preserves literal row zeros, and holds uniformly in the row. The inherited fixed-test derivative bound is explicit in the derivative order; this justifies using orders that grow with \(X\).

I checked the common-block interpolation and row-node incidence contradiction. Its block is selected from the evaluation point and is shared across all rows. Selection of \(m\) separated good nodes gives the stated Lagrange coefficient bound, and the complex divided-difference remainder needs no real mean-value point. The choice \(m=\lceil8\log X/r_X\rceil\) is \(o(\log X)\), including exceptionally fine grids, while \(m r_X\ge8\log X\) still pays the absolute remainder. The height is the same \(X^h\) throughout each dyadic block, so no row-entry endpoint is crossed.

The conclusion is \(B_1(D)\ll_\varepsilon D^{\alpha+\varepsilon}\) and strict-half-plane ordinary-zeta zero exclusion, conditional on the stated every-node positive-fraction arithmetic hypothesis. The hypothesis itself is not proved.

## 2. Two signed quantiles and the exact endpoint

The Taylor–Markov argument is valid for the real restored source and uses only a preceding interval at an absolute past record. The recurrence bounds each contractive replica throughout that past interval by \(3A/2\), and its value at the record has the record's sign and modulus at least \(A/2\). No future envelope is needed.

With \(m=\lceil\log X\rceil\), \(\delta=c/\mathscr L(m)\), and sufficiently small fixed \(c\), the Taylor remainder is \(O(X^{-2})\). Markov's polynomial inequality on the entire interval costs \(m^2/\delta\), including its endpoints. The grid condition \(\Delta_X(\log X)^2\mathscr L(\lceil\log X\rceil)\to0\) makes the displacement to the preceding grid point a relative \(o(A)\). The interval may cross the dyadic boundary because the source derivative estimate is uniform over all rows and can be applied at \(X/2\) or \(X\).

The argument works at \(\beta=\alpha>0\). If \(|B_1(D)|D^{-\alpha}\) were unbounded, take \(\alpha\)-records \(A_j=F_jD_j^\alpha\), \(F_j\to\infty\). At one common preceding grid node at least \(1-\gamma/4\) of the bases retain the record's sign and modulus at least \(A_j/4\). Depending on that sign, one of the two required \(\gamma\)-quantiles is contradicted. This proves the exact endpoint \(B_1(D)=O(D^\alpha)\).

The two quantile sets can be disjoint and may vary with the node. For \(W_*\), the additional logarithmic cost is correctly \(N_X=\lceil(\log X)^3\omega(X)\rceil\), \(\omega(X)\to\infty\). The conclusion supplies no same-endpoint converse from zero-freeness merely in \(\Re s>\alpha\). The cofinal ordinary-RH equivalence retains its separate converse theorem and endpoint margins.

**Contribution disclosure:** during pre-publication review I identified that the author's relative Taylor–Markov argument permits \(\beta=\alpha\), sharpening the initially stated \(\alpha+\varepsilon\) conclusion. The author independently confirmed and incorporated this change before the source freeze. This receipt therefore does not represent a wholly independent discovery or review of that enhancement. The main Taylor–Markov mechanism is the author's. The root reviewer and another agent were asked to review the exact endpoint separately.

## 3. The growing ridge with every literal short polynomial retained

The arithmetic object is exactly the collision factor times the SC2 plus/minus short polynomials. The common moving mask is the source's full incidence mask \(Q\); no new arbitrary coefficient class is introduced. The exterior incidence multiplier and spatial weight are separate and may vanish.

For a real central shift \(b\), the source phase becomes \(a_b=a e^{ib\log q}\). The complete pair bound of the base collision theorem is uniform on the unit circle, so no high-prime shift error accumulates. The finitely many small-prime numerator lower bounds lose only \(O((\log Y)^{-3})\), smaller than their paid worst-case \((\log Y)^{-2}\) size. Thus the base collision growth survives uniformly on the specified shift interval.

The minimum-modulus lemma is correctly anchored at \(\Re s=2\): the complete inverse Euler product has modulus at least \(\zeta_K(2)^{-1}\), and literal truncation has uniform error \(O(Y^{-1})\). On the radius-four disk centered at two, elementary counting gives \(O(Y^3)\). Jensen then counts \(O(\log Y)\) zeros in the radius-three disk. Removing them by the radius-four Blaschke product leaves a bounded holomorphic quotient, zero-free in the radius-three disk. Harnack's factor five on the radius-two disk and the lower bound \(2\delta/11\) for each Blaschke factor give the stated \(\exp[-C_A(\log Y)^2]\) lower bound off radius-\(Y^{-A}\) zero disks.

For a collection of at most \(C_0Y^B\) pairs, choosing \(A>B+2\) makes the union of bad shift intervals smaller than half the interval of length \(2(\log Y)^{-3}\). The same positive-measure set works for every row and mask in the collection. The collision growth \(\exp(cY^{1-2\sigma}/\log Y)\) dominates the product of all fixed \(2k\) short-factor losses.

The theorem is a lower bound for individual arithmetic row factors on this common shift set. It is not a lower bound for the signed row trace, does not include an unrestricted Schwartz tail, does not remove the exterior zero masks, and does not refute CT1 or a norm-filtered moment estimate.

**Dependency authorship disclosure:** I authored the base ANTI_CONJUGATE_COLLISION_GROWTH.md, whose exact dependency hash is 384667530dc3987f9ea77da0bac67a723d6a57d4635748286a500dc6042c87fa. This receipt checks its use and the separately authored shifted/short-factor extension; it is not an independent review of my base theorem. That theorem has separate reviewers. Pre-review also checked the phase substitution and exterior-zero scope before the extension was frozen.

## 4. Source replay and finite computation actually performed

Six load-bearing source bindings were checked against their original commit:path bytes and against the copies in the frozen packet:

| Source | Original commit | SHA-256 |
|---|---|---|
| LOG_FREE_REPLICATED_SPIKES.md | ab98878279cd5614fe79bb94aa916e97c9ee50b4 | b59978c1c5d3b5cb904c7f22d675a67bb71b2af512db9f0577e568a04565a86b |
| SAMPLED_MOMENT_CRITERION.md | ab98878279cd5614fe79bb94aa916e97c9ee50b4 | 18bf2fdad438eb21ae3318eba7d42e9c03803b2dd1abc4d8f6448fb3b04499de |
| PRIME_SLOT_CANCELLATION.md | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | d37ad696b46c7dda15a7faf314c46cda2d7d67e25ac8d3288c7f138aac373c13 |
| WIDE_SUBCRITICAL_TUBE.md | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | 53568631060432784811d8474e8d774257664826e8fb9fa59c0ba47959745f02 |
| SHORT_POLYNOMIAL_COLLISION_TRANSPORT.md | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | c538719277b1e7de70a7e3f872fb2720668bd43ca57c9cffff6ff29b6766d5ac |
| COMPLEMENTARY_SHORT_TRACE_CONTRACT.md | 2f8b6a3898a722d0602a91dea73bac344a3bb7dd | 968a2bee6d47f0a92fded0ab32c23963d31332f649dc0046604b7b568d48640c |

REVIEW_SOURCE_PIN_REPLAY.json records their complete paths and comparisons. The relevant replica, universal-test, SC1–SC6, tube, and CT1 interfaces were read at these pinned identities. The fixed-field prime-ideal supply in the collision dependency is retained as its declared classical input.

I replayed the frozen checks/check_zeta_bridge_capture.py, SHA-256 201ac23e4646b41ae6b05e12e32622024169ee49b0ebf22cb3a25cddbe1f717b, with an explicit repository argument and the frozen bridge manuscript. The exact report is ZETA_BRIDGE_INDEPENDENT_REPLAY.json, SHA-256 5ca98462d89e75b080ab7edbd914e666f34a3da9022fb1ff94353fbcc6bd7bd6. It passed and replayed both original source hashes.

The reported finite coverage is 729 ideal-status assignments through coefficient 160, 116,640 coefficient equalities, eight local deletion series through degree 12, six rejected negative controls, 11,089 good-node patterns, 55,445 rational evaluations, 103,985 polynomial reproduction identities, 9,708 spacing checks, 10,880 constant checks, and 136 incidence-fraction checks. All good-node subsets are covered only for the declared blocks \(q\le12\); larger blocks use the stated edge/spread patterns. No broader exhaustive coverage is claimed.

The replay is finite integer/rational algebra. It does not certify the growing-order derivative theorem, Markov's inequality, the minimum-modulus theorem, an actual capture inequality, any infinite arithmetic bound, any zero-free half-plane, or RH. Those distinctions remain explicit in the reviewed manuscripts.
