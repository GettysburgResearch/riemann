# Independent review of the correlation, theta and low-kappa adapters

Review date: 2026-10-10. Status: the displayed arithmetic and elementary analytic implications below pass independent inspection at their stated scope. This review does not rebuild an external quasi-RH proof or establish an estimate for the actual arithmetic source.

## Correlation transfer C1–C11

Reviewed `../correlations/CORRELATION_TRANSFER.md` and checked its C6 interface against `../arithmetic/NEGATIVE_MASS.md`.

* C1 counts every zero-extended window with the correct `H-d` multiplicity. The index range `1<=j<=N+H-1` includes both endpoint fragments. Its Cauchy consequence C2 retains the signed energy; C3 and C4 correctly pay half the smaller shift-range and absolute-correlation saving.
* C5 includes all square divisors, including nonsquarefree integers. The positive internal epsilon makes the square-divisor sum convergent at `theta=1/2`; no exact endpoint bound is asserted.
* C6 retains `M_beta(x)=M(x)-M(x/67)`. The needed cancellation of the `sqrt(x)` main term follows from the zero value of `sum beta(n)/n`, justified by the convergent series and its Abel limit. The cited nonnegative-transform argument has the required real-axis holomorphy and noncancellation of off-line poles.
* C7 holds uniformly over every character and real frequency because `Re(alpha conjugate(chi(p)p^(it)))<=alpha`. The prime lower bound for the positive summatory function excludes every power exponent below one.
* C8 is an exact log-weight identity before its Chebyshev upper bound: complete multiplicativity supplies `g(md)=g(m)g(d)`, and `log n=sum_(d|n) Lambda(d)`. C9 is a positive Euler-product majorant, requiring no asymptotic for the summatory function.
* C10 removes the log weight by splitting at `sqrt(X)`. C11 applies Cauchy to a shifted interval contained in `[1,2X]`; its constant is independent of every integer `0<=h<=X`. Thus the proof needs only the explicitly named Chebyshev and prime-harmonic estimates, not Selberg–Delange.

The firewall is correctly scoped to bounded completely multiplicative functions. Its logarithmic correlation saving comes from decaying mean-square mass, and the source is positive; it does not supply signed cancellation or have the unit modulus of Liouville. These distinctions do not invalidate its intended counterexample to an implication from the listed general bounded-source properties.

The complete classical reconstruction in `../arithmetic/ZERO_FREE_MERTENS.md` was also reviewed. Its elementary polynomial zeta bound is sufficient for Borel–Carathéodory on the fixed zero-free disk. The positive harmonic rectangle barrier has the correct edge bounds and exponentially small center-height correction, giving a strictly sublinear power of `log(t)` for `log zeta` and hence subpower reciprocal growth. The half-integer Perron error is `O(x log(x)/T)`; its contour stays away from zero, and the reciprocal's removable zero at one creates no residue. With `T=x^2`, `sigma_0=theta+epsilon/2` and `eta=epsilon/4`, the stated Mertens exponent follows. The resulting exact fixed-SHARP negative-mass growth exponent `Theta-1/2` handles `Theta=1`, `theta=1/2`, and an unattained supremum at their explicitly stated scope. No correction was found.

## Complete positive theta source and modular binding

Reviewed `../xi/POSITIVE_THETA_QUARTET.md`, `../xi/MODULAR_BINDING_AND_TRANSPORT.md`, the Fourier normalization in `reviews/D-pass3/PROOFS_AND_REPAIRS.md#R16`, and the saddle interface in `reviews/A/supplement/REPORT.md#S06`.

P1–P7 pass: the polynomial adds exactly the indicated quartet with multiplicity; integration by parts has `D^2 -> -z^2` and `D^4 -> z^4`; the derivative recurrence and complete atom positivity imply full-source positivity on both half-lines. The R=10 lower margin is 2000, and the unbounded-height polynomial has positive coefficients.

The Fraction checker was replayed from a byte-identical copy in `/tmp`, avoiding mutation of the owner's receipt. It passed all 49 Bernstein coefficients, 36 synthetic quartet locations and both unbounded tails. The compact Bernstein cover and the positive tail are complete domain certificates; the quartet evaluations are finite consistency checks of the independently displayed factorization.

P8 has the stated scope. For each fixed R,d the leading atom has degree six, changing the bounded linear coefficient from `9/2` to `25/2`; the double-exponential curvature and the S06 local/exterior estimates survive. Constants and the first applicable derivative order may depend on R,d. This does not assert uniformity in R, a low-order companion bound, or a descent theorem.

M1–M11 pass: the two normalizations `Q(0)` and `Q(i/2)` are distinguished; even L commutes with Jacobi reflection; `L(1/2)=L(-1/2)` preserves the endpoint and small-v terms. Repeated Mellin integration by parts gives the correct factor `L(s-1/2)/C`. Its real-axis growth excludes an ordinary absolutely convergent Dirichlet series normalization. The compact-error factorization and derivative bounds are correct. The companion ratio estimate retains and protects both original denominators, so it does not silently deduce descent from a small polynomial correction.

## Compiled low-kappa arithmetic

Reviewed `../xi/formal/LowKappaCapacity.lean`, its README and the complete compilation receipt. The variables match `KAPPA_EXTENSION_CONDITIONAL.md`, Section 2.2: `A=n_1+n_2+z`, capacity `A+(6*kappa-1)z`, and M includes the declared moving twist-radical width.

The comparison, strict-width, support-error, terminal and clipped deleted-column theorems match the written adapter. The real positive examples inhabit the new interval `13/18<=kappa<3/4`; the equality and below-threshold examples have the advertised values. The reported axiom sets of all fifteen compiled statements contain only `propext`, `Classical.choice` and `Quot.sound`.

This is a compiled real-arithmetic adapter with explicit analytic hypotheses. It proves neither the extended analytic moment theorem nor the source identities that would instantiate those hypotheses.

## Separate independent induction audit

A second mathematical reviewer read all of the frozen September-30 Section 18 source, lines 12477–14973, together with its logarithmic-control, smooth-calculus and kernel interfaces. Sections 1–3 of `KAPPA_EXTENSION_CONDITIONAL.md` passed that review, conditional on the cited analytic inputs. The exact source findings were:

| Source lines | Audited use |
| --- | --- |
| 12929–12936 | The terminal exponent uses `kappa*z<=M/6`; the auxiliary `z<=2M/9` can be replaced by `z<=3M/13`. |
| 12947–12980 | The intermediate `z<M/21` is weakened to `z<M/20`, which already supplies the source's operative comparison totals `23M/30` and `14M/15`. |
| 12833–12900 and 1531–1607 | The prime estimate retains `beta_*<=(1+kappa)/2`; the compact enlarged range has `s_kappa>=31/36`, and its derivative-independent prime exponent is unchanged. |
| 14218–14301 | Greedy removal has capacity decrement `6*kappa*d` and squared-prime cost `kappa*d`, hence exact ratio `1/6`; deletion monotonicity needs `6*kappa-1>=0`, and overshoot uses `kappa<=1`. |
| 14810–14971 | Finite induction and weighted all-height propagation need `0<=6*kappa-1<=5` and the preserved margins. Full-product Fourier measures, aggregate support thresholds, backward finite internal orders and the later external tail order are retained. |

The actual-capacity crossing and balanced count in Section 3 were also checked, including the inverse `7/37` supply and the plain `c/3` capacity. The former `Delta/4` penalty came from the baseline-capacity replacement and disappears when the actual capacity is retained. The clipped auxiliary hypotheses already imply `M>=0` from `0<=short<=M/4`; no missing hypothesis was found.

This audit validates the written parameter adapter against its frozen source. The shared analytic inputs remain dependencies, and this result alone does not establish the continuation conclusion or independently rebuild the upstream L-function theorem.

## Convex payment and complete source window

`../operators/CONVEX_WINDOW_EXTENSION.md` and its exact checker pass independent review. The moving-integral norm has support of length `L+s`, total integral `s*mu`, and the stated Cauchy lower bound. The `s=L` primitive identity retains both endpoint fragments and works for complex h. The mean coefficient simplifies exactly to `L^-1 integral_0^L w` after two integrations by parts, with the weighted-curvature hypotheses controlling zero. Thus a negative endpoint is genuinely paid from the full positive curvature mixture.

The literal source bounds have the correct directed signs. The full prime constant uses both sides of the convex trapezoid tail, and the gamma integral drops only positive terms in its lower bound. The helper enclosures imply `C_b>-(.578+.6932+1.1448-1)/3=-.472`; the new lower gamma/log enclosures imply `C_b<(1-.57-.693-1.144)/3=-.469`. The curvature lower bound covers the complete interval, and its weighted endpoint integrability survives at `L=3/20`.

Normal and optimized `-B` checker outputs were independently replayed into `/tmp` and are byte-identical. Their source hash is `72ff5c1c4653558f40b737348860a9937ae21be49201329b44c5178673072c2e`. The resulting `3/500` and `1/300` lower coefficients are correct. This certifies all complex L2 tests on the stated window in a primitive norm; it supplies neither a uniform L2 spectral gap nor interval joining.

## Recompleted negative height features and extended anchors

A separate independent reviewer verified N10–N13 of `../heights/NEGATIVE_FEATURES.md`. Symbolic comparison to the native quartet gave zero. Normalized Leibniz produces W2 and W3 as stated; `zeta_o>0` ensures the odd positive-square coefficient, and the negative coefficients give exactly `16A^2(S^4 W2 S8/zeta_c+S^6 W3 S10/zeta_o)`. The j=10 tail and `log H<63/2` give `2845/(81H^9)`. Compact convergence retains all positive quartet squares via `sum m/b^2`.

At the reviewed freezes, `../certificates/certify_hardy_z.py` certifies 16 intervals with 33 endpoint balls, and `../heights/certify_extended_anchors.py` certifies 48 intervals with 96 endpoint balls. Both were replayed at 128 bits with python-flint 0.9.0 into `/tmp`; the extended producer's normal and optimized receipts were byte-identical. The floating-point finder only places proposals. Exact rational endpoints, strict real signs, zero-containing imaginary enclosures, disjointness and the existing continuous Hardy-Z functional-equation argument justify the IVT existence conclusions. They do not prove uniqueness, simplicity or a zero census.

The reviewed hashes are: negative features `4415102019f19efe63f581d4aa5dd8b734faa6af47e146f37c10b96b790ce4f4`; 16-anchor producer `44c83f855447c7acf348da070b9617ca12d5ce270ef949d5a99eb7bf17dc6a6a`; 48-anchor producer `875baffd29b1dde90683503536814e3eb9f7cb9d75745407fc7c4641e2f3a574`. `HARDY_Z_REVIEW.md` separately records the earlier nine-anchor freeze.

## Weighted squarefree stitch

Two independent mathematical reviews pass `../arithmetic/SQUAREFREE_STITCH.md` and `verify_squarefree_stitch.py` for their stated scope: every real x>=1 and every real m>=1.737. The noninteger continuation remainder in S5 has the correct sign and `z^-b` bound. Completing the two absolutely convergent h-sums gives S4's exact error constant while retaining the negative `zeta(b)/zeta(2b)` term. Rescaling the 67 label gives the three displayed factors without losing its separate multiplicity.

The normalized Bernoulli prefix and tail errors produce exactly E0, L and C in S9. Holding the slab coefficients fixed, the derivative lower bound has the stated factor `x^(b0-2)[B0(m0-1)sqrt(x)/2-L0(1-b0)]`, plus a positive omitted error derivative. Thus S12 covers every real tail endpoint, rather than just the stitched horizon. The labelled-prime finite-horizon argument covers the whole bounded endpoint interval; the seven closed slabs and the inherited higher-power theorem cover the entire claimed power range.

The second reviewer replayed the 192-bit Arb checker in normal and optimized `-B` Python into `/tmp`: all seven slabs pass and the receipts are byte-identical. Each constructed whole-power ball was also confirmed to enclose both exact endpoint balls. Directed coefficient endpoints, complete prime enumeration and explicit guards were checked. Finite density and prefix controls corroborate the normalizations but are not substitutes for S1–S12.

Reviewed SHA-256: manuscript `62253844e57e2ad2c4490cb5dd08dc318a90ef058fdf81062dac9112ab32b221`; checker `746be9f6382323a0131e3a7ece95e4448461c2b44c7e0dd33310d02675513550`; horizon dependency `8486059b8468ceb6cb59d34c4c16c61eeb72a8097583596e5253b934571e5104`. No mathematical correction was identified. This remains a sufficient supercritical-power theorem, with no critical-power-one or RH claim.
