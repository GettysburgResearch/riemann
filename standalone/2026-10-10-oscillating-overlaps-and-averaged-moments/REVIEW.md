# Proof audit and claim boundaries

Status: proposed research with scoped independent AI-agent review. These audits do not constitute human mathematical acceptance or an integrated repository verdict. No full short-row moment or new zero-free half-plane is certified.

## 1. Frozen proof identities

| Published file | Reviewed working name | SHA-256 |
|---|---|---|
| OSCILLATING_OVERLAPS.md | attack2_moment.md | 271f4f71bda533810ee49f6498f4ffbc42c3f0cb37c59151f9f703e715f58397 |
| AVERAGED_MASK_OPERATORS.md | attack2_amplification.md | 1acb3ff591c6b53f1200418bc69b3f0f96d63d987f22cfd66e88c41017abe299 |
| SCALE_AVERAGED_CRITERION.md | attack2_scale_criterion.md | c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0 |
| FACTORWISE_THETA_REFLECTION.md | attack2_theta.md | f4854894c797f9b9f92b6d52a24b61caa941e3aff2b15c4c5a460db8fff469ff |

The proofs were authored in separate working files by three collaborating agents and the root agent. The root proposed the moving-cutoff operator route and the localized all-even-degree extension, then independently reconstructed the proofs described below. The operator and scale notes intentionally retain their overlapping operator argument so that each principal application has a complete proof at its reviewed hash.

## 2. Independent review map

| Report | Independent scope |
|---|---|
| [overlap_review.md](reviews/overlap_review.md) | Cubic/quadratic all-row decomposition, exact incidence eligibility, master bounds, fourth and rectangular cutoffs; overlap note Sections 2–5 |
| [operator_review.md](reviews/operator_review.md) | Mean operator and all-Y weighted coercivity, operator note Sections 1–5; complete scale-averaged criterion |
| [scale_review.md](reviews/scale_review.md) | Complete independent reconstruction of the moving-cutoff theorem and moment-to-zero implication |
| [operator_checker_review.md](reviews/operator_checker_review.md) | Independent source inspection and normal/optimized replay of exact operator checks |
| [theta_execution.md](reviews/theta_execution.md) | Author execution and source normalization record; this report is not itself an independent analytic review |

The root read the exact proof files, checked the classical large-sieve statements at their primary papers, inspected the complete local scalar calculation in the pinned October 5 manuscript, and independently replayed the theta checker. Source automorphy and the full imported quasi-Riemann argument were not reconstructed.

## 3. Root audit: arithmetic overlap statements

The cubic valuation decomposition must allow primes of the cube base to overlap the squarefree remainders. The proof does so, and retains the indicator on the inner column before invoking the squarefree sieve. The three dyadic inequalities are verified algebraically by substituting either A=B*U or B=A*U, with all remaining variables at least one.

For a designated incidence ideal, the original tuple and every candidate divisor are distinguished. A prime common to all residual inside factors is permitted only if it also occurs outside. This is exactly the condition excluding a second prime of the designated incidence type. The ordinary subset-gcd variant uses a different eligibility condition, as it should. All restrictions on the varying column are row independent; none is removed from a signed sum.

The frozen-tuple count is product(D_i)*L^(-m), including nonempty bounded scales. The column coefficient mass is O(L). The resulting squared cost has C powers 1-2m, 2-2m, and 5/3-2m. Their square-root exponents are negative for m>=2, so the dyadic tail is geometric. Substituting m=k=2 gives the precise fourth-moment bound and cutoff in the README.

The newly added localized Corollary 6.1 was checked separately from the overlap agent's Sections 2–5 review. Each outside original pair has ordinary gcd at least a fixed multiple of D, so it has O(D) possibilities. There are O(D^(ell-1)) outside tuples. After freezing them, the same cubic proof on the first pair applies with arbitrary row-independent eligibility masks. Its norm is multiplied by D^(ell-1), and its energy by D^(k-2), producing D^(k+2) times the cubic bracket. The matched previous-core comparison in (6.7) has the stated two exponents. This establishes only the specified overlap configurations.

The designated-core comparator in Section 6 follows from three explicit incidence weights: |J|/2, |J|, and 5|J|/6. Only the first has harmonic pair sums. The other two distinguished tails have powers 1-m and 1-5m/6 before squaring. This validates the comparison without treating a common-gcd formula as automatically applicable to every incidence ideal.

The optional Section 7 is an implication from its displayed uniform, moving-mask Möbius second-moment premise. Its smooth-cutoff requirement is substantive and is retained. The numerical example m=5,k=8 has a nonempty improved range for 1<h<16/15, conditional on that premise. This section is not used to call any of the classical or operator results unconditional.

## 4. Root audit: averaging, finite modes, and the scale criterion

The norm of a causal dilation by Nd is (Nd)^(-sigma), with the sign fixed by direct substitution in x^(-p sigma)dx/x. The exact divisibility density is J(Y/Nrad(d))/J(Y). Its error is bounded both by R^(-1) and by Y^(-1/2)R^(-1/2), including R>Y. The interpolated majorant is summable exactly in the sufficient range delta<sigma used by the proof.

The local inverse coefficients are negative eta(p)^j q^(-1)(1-q^(-1))^(j-1). Both Euler products converge in the weighted coefficient algebra. This supplies an actual inverse; a formal identity or an unproved nonvanishing assertion is not substituted for norm convergence. The uniform lower bound for bounded Y follows directly from v=1.

The root also read the finite-mode and model sections, which are outside the theta agent's operator-review scope. Distinct modes can be separated at distinct prime norms, because equality of two local responses at two different rational primes would force a rational ratio of their logarithms. Finite multilinear interpolation gives a positive-definite finite-prime Gram matrix. Its entrywise product with the complementary positive semidefinite matrix remains strictly positive by the stated Schur argument. The finite leading-mode application requires its explicit power-saving asymptotic remainder. The synthetic example imposes the exact removal identities but does not impose the actual Möbius coefficient expansion.

For the moving cutoff, the root's proof and two independent reconstructions agree. The error is made small on the subspace zero below X_0. Inversion is first carried out on each finite interval (X_0,T), with a bound independent of T, and the low-scale forcing term is controlled by the positive coefficient majorant. Thus the unknown high-scale integrability is a conclusion rather than a premise.

Jensen contributes D^(-h/6), and the scale-integrated exponent is k+5h/6+e_k-2k sigma+epsilon. Its negativity gives exactly the stated boundary. The Mellin step uses the previously reviewed universal test, finite Euler corrections, and Hölder. It needs no conductor-uniform reciprocal-L theorem in this direction. The moment estimate itself remains a hypothesis.

## 5. Root audit: factorwise theta reflection

The root checked the source's full scalar, not just the bounded scalar in the short theorem statement. At a row prime, multiplying the conductor by a multiplies sigma_p by a and epsilon_p by a^(-2); each local case therefore scales by chi_p(a)^(2j+2), including active j=0 and j=4. The outside-a primes produce the exact CRT factor gamma_4(a). The conjugate primitive Gauss identity gives gamma_2(a)gamma_4(a)=1. After even-power reciprocity, the total row exponent is j+4+(2j+2)=3j modulo six.

The source's -i/81, ramified Fourier coefficient, conductor unit, Kubota factor, and inactive densities remain in Z. Finite ray partitioning freezes the listed cusp and additive data. Positive multiples of six in row valuations retain their separate zero masks. Only the explicitly squarefree-row specialization makes both row axes quadratic.

The Ramanujan factor has the exact local values -1 and q-1. Its fixed-frequency Euler series is therefore the reciprocal angular L-function times the displayed finite correction. The character has infinity type -3, so the imported finite-order zero-free assertion does not apply. The Euler identity's initial domain Re w>1 and its stronger sufficient absolute-interchange domain are distinguished from any continuation.

Mellin inversion of the two displayed tests gives w=s+1/2-2t=s+2u-1/2. The exact coefficient energy follows from a=d e with d=gcd(a,rad x), leaving phi(d)^2/(Nd Ne). Its annular harmonic sum is uniformly bounded. The fixed-frequency quadratic sieve is a valid deduction, but does not estimate the coupled frequency sum. The residual divisor-channel product scale remains K^2 A E^2/B.

The root's normal-mode checker replay matches the author's optimized result byte for byte. This independently checks the specified finite normalization identities, including a nontrivial CRT cross phase. It does not verify the imported automorphy theorem or an infinite theta norm.

## 6. Corrections and preservation

Review corrected missing addition signs before several displayed error terms and a measurability omission in the abstract moving-cutoff theorem. The final proof hashes above include those corrections. The bounded-Y operator case was strengthened by retaining the identity base. No older proof packet was rewritten.

The theta author's scratch TeX copy contained one extra trailing newline. A byte comparison showed that all source mathematics was identical to the canonical pinned TeX. The execution report now records the canonical file's size, SHA-256 and Git blob, as well as the exact scratch difference.

The finite overlap checker was changed to use explicit exceptions before its final optimized replay, because Python disables bare assertions under -O. Its final source and results are bound in the validation manifest. No optimized run with disabled predicates is counted as validation.

## 7. Smallest remaining gap

The full short-row fourth-moment estimate still needs cancellation in the actual small-gcd balanced polynomial, including the nearly coprime tuples. The scale-averaged version of that estimate now suffices for the same extraction. Higher-order overlap pieces do not bound their full polynomial complements. The exact angular reflection identifies a coupled-frequency problem without resolving it.

The accepted scope of this proposed packet is the displayed partial arithmetic bounds, convergent operator theorems, conditional moment-to-zero implication, and source-qualified transformation. None supplies the missing full arithmetic moment hierarchy.
