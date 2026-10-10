# Independent review of the averaged mask operators and scale-averaged extraction

Reviewer: theta-closure agent, independently reconstructing the mathematical arguments for the root agent.

Status: the statements in the reviewed scope follow from the stated elementary inputs and the prior universal Mellin test. The arithmetic moment hypothesis remains unproved. This review is a proof audit, not a numerical experiment or an independent proof of RH.

## Exact reviewed files and scope

| File | SHA256 | Reviewed scope |
|---|---|---|
| attack2_amplification.md | 1acb3ff591c6b53f1200418bc69b3f0f96d63d987f22cfd66e88c41017abe299 | Section 1 definitions and Sections 2–5, including the corrected all-Y finite-range coercivity |
| attack2_scale_criterion.md | c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0 | Sections 1–5, including the moving-cutoff theorem, dyadic-scale extraction, and cofinal conditional consequence |

This review does not claim to have audited Sections 6–8 of attack2_amplification.md. The two reviewed files were read directly, and the identities and operator estimates below were independently reconstructed. No new arithmetic computation was needed for this review.

## 1. Counting, averaging, and the exact mask density

The ideal count follows from the fixed Eisenstein lattice, class number one, and its six units. The stated estimate J(t)=kappa_K t+O(sqrt(t)) is valid for every positive t: for t<1 the count is zero and the main term is itself O(sqrt(t)). This full domain matters when the radical norm R exceeds Y.

The exact density of ideals v with rad(d) dividing v is J(Y/R)/J(Y). Multiplication by rad(d) is an injective bijection onto that set, with no missing coprimality condition. Using J(Y) comparable to Y gives the uniform bounds

\[
w_Y(d)\ll R^{-1},\qquad
|w_Y(d)-R^{-1}|
\ll\min(R^{-1},Y^{-1/2}R^{-1/2}).
\]

The same estimate at R>Y is valid because w_Y(d)=0. Interpolating with exponents 1-2delta and 2delta gives exactly Y^(-delta)R^(-1+delta), for 0<delta<=1/2.

The mean bound for E_sigma(v)^p is also correct for every real p>0. Expanding the nonnegative multiplicative local difference (1-q^(-sigma))^(-p)-1 over squarefree divisors and applying J(Y/Nd)<=C Y/Nd gives the convergent Euler product stated in Section 3. Its nonconstant local term is O(q^(-1-sigma)). This proves a genuine bounded average, without a power loss in Y. Zero values of eta only reduce the subsequent majorants.

## 2. The limiting operator and its exact inverse

The coefficient space with norm sum_d |c_d|(Nd)^(-sigma) is a unital Banach algebra under ideal Dirichlet convolution. The dilation S_d f(x)=f(x/Nd) has norm at most (Nd)^(-sigma) in the stated weighted L^p space on (0,T). This follows by the exact change of variables and uses only values at smaller scales.

The coefficient sequence eta(d)/Nrad(d) belongs to that algebra for every sigma>0. The mean error is bounded by

\[
Y^{-\delta}
\sum_d (Nd)^{-\sigma}(N{\rm rad}(d))^{-1+\delta}.
\]

The product for this sum converges precisely under the sufficient restriction delta<sigma used in the files. The additional delta<1/2 comes from the count interpolation. All constants are uniform over completely multiplicative eta with |eta|<=1.

The local inverse is correct:

\[
\left(\frac{1-(1-q^{-1})z}{1-z}\right)^{-1}
=1-q^{-1}\sum_{j\ge1}(1-q^{-1})^{j-1}z^j.
\]

Its coefficient norm has nonconstant local contribution

\[
\frac{q^{-1-\sigma}}
{1-(1-q^{-1})q^{-\sigma}},
\]

which is O(q^(-1-sigma)) outside finitely many primes. Both the operator product and its inverse therefore converge in the same algebra. Finite-prime multiplication followed by norm convergence proves the inverse identity; a merely formal Euler manipulation is not being used in place of convergence.

For sufficiently large fixed Y, the error multiplied by M^(-1) has norm at most 1/2. The resulting Neumann inverse for M_Y has norm at most twice the uniform limiting-inverse norm. Its independence from the endpoint T is valid.

## 3. Finite-range coercivity, including small Y

The upper L^p estimate follows from the mean E_sigma(v)^p bound. For large Y, apply the bounded inverse to the averaged operator and then use Jensen's inequality:

\[
\|f\| \le C\|M_Yf\|,\qquad
\|M_Yf\|^p\le J(Y)^{-1}\sum_{Nv\le Y}\|T_vf\|^p.
\]

The corrected proof covers every 1<=Y<Y_0 by retaining the unit ideal v=1, for which T_1f=f. Its lower constant is at least J(Y_0)^(-1), so the final constant depends only on the fixed parameters.

All operators are defined on the finite interval itself, by causality. No assumption about integrability past T is needed. The extension to the full half-line follows by monotone convergence for a base function of finite weighted norm.

For the arithmetic row decomposition, unrestricted ideal bases v are the correct objects. The unit belongs to the sixth-power-free core, and replacing a generator of v by a unit does not change v^6. Distinct ideals v give distinct rows r v^6 for fixed nonzero r. Thus the sum over cores and the weight (H/Nr)^(1/6) in the integrated transfer are correct. The height H must remain fixed during the scale integral in that statement; the text explicitly retains this requirement.

## 4. The moving-cutoff inverse is a valid separate argument

I independently checked the operator argument in Theorem 3.1 of attack2_scale_criterion.md rather than inferring it from fixed-Y coercivity.

For functions g zero below X_0, and x>=X_0, the coefficient error has a uniform majorant

\[
C c^{-\delta}X_0^{-\rho\delta}
(N{\rm rad}(d))^{-1+\delta}.
\]

Its dilation norm is summable with weight (Nd)^(-sigma). Consequently P-M has arbitrarily small operator norm on the zero-below-X_0 subspace when X_0 is large. The limiting inverse M^(-1) preserves that subspace because every constituent dilation is causal. The Neumann argument therefore applies in the algebra of bounded operators even though P's coefficients depend on x and are not a fixed Dirichlet-convolution sequence.

The proof correctly starts on each finite interval (X_0,T), where the locally bounded arithmetic function has finite norm. All inverse bounds are independent of T. The low part f_0 has finite global norm by its compact scale support and the positive lower cutoff, and P f_0 is bounded by the convergent positive operator with coefficients C/Nrad(d). This gives a uniform bound for the high part on every finite interval. Passing T to infinity therefore proves its integrability without having assumed it.

No regularity of the moving cutoff besides measurability and its lower growth bound is used. The argument is consequently stronger than a formal substitution of Y(x) in a fixed-cutoff estimate.

## 5. The dyadic moment implication and its exponent

For a fixed row r, the replica cutoff is exactly Y_r(D)=(D^h/Nr)^(1/6). Jensen's inequality over those distinct rows gives

\[
|M_{Y_r(D)}A_r(D)|^{2k}
\ll_r D^{-h/6}M_{2k}(D,D^h).
\]

Combining this with the assumed dyadic-scale upper bound and the weight D^(-2k sigma) gives the exponent

\[
k+\frac{5h}{6}+e_k-2k\sigma+\epsilon.
\]

Its dyadic sum converges exactly for the asserted strict condition

\[
\sigma>\frac12+\frac{5h}{12k}+\frac{e_k}{2k},
\]

after choosing epsilon sufficiently small. The moving-cutoff theorem then transfers that integrability to A_r itself.

The final Mellin step is valid. Weighted L^(2k) integrability at sigma implies absolute Mellin convergence for Re s>sigma by Hölder, because the extra factor D^(-(Re s-sigma)) is integrable to the conjugate power at infinity. The positive lower support handles zero. The same argument with logarithmic factors justifies holomorphy and differentiation locally in that half-plane.

In Re s>1 the Mellin integral is the nonvanishing universal test transform times the appropriate finite Euler correction divided by the primitive inducing Hecke L-function. Each deleted Euler correction is holomorphic and nonzero on Re s>0. The reviewed universal-test result from the preceding packet supplies the same property for the Mellin transform. Meromorphic continuation and the identity theorem therefore exclude a zero of the L-function in the derived strict half-plane. A principal pole gives a zero of the reciprocal and does not invalidate this inference.

Taking cofinal fixed orders with h_k=o(k) and e_k=o(k) makes the extraction boundary approach 1/2. This is a correct conditional implication. Its premise is the still-open scale-averaged arithmetic bound; neither operator nonvanishing nor this review proves that premise.

## Review conclusion and boundary

No mathematical defect was found in the stated reviewed scope at the hashes above. The averaging and causal-inverse arguments are complete as operator statements, and the scale-averaged moment hypothesis does imply the stated zero-free conclusion.

The nonvanishing mean-mask multiplier is an auxiliary Euler product. It is not a nonvanishing result for the original Hecke L-function. The arithmetic cancellation needed on the long balanced cores remains a separate missing estimate. This audit validates the reductions and their quantifiers, not a short-row moment theorem, a new zero-free half-plane, or RH.
