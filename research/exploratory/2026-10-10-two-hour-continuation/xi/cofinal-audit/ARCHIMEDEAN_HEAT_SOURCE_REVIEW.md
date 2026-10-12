# Independent analytic review of the complete prime and heat identities

Status: full mathematical/source read ACCEPT at the two frozen proof hashes
below. No native quadrature, prime-tail computation or derivative certificate
is claimed by this review.
Scope: literal actual completed-zeta identities, complete tails, and a global
equivalence criterion with an explicit general representation-theorem import.
No actual all-order positivity, cofinal census or RH result follows.
Exact sources: [ARCHIMEDEAN_PRIME_SHIFT_IDENTITY.md](../ARCHIMEDEAN_PRIME_SHIFT_IDENTITY.md),
SHA256 `cc70524e065919ae15dee63085c8ec357b2d32e782b8d78ac6db9c9d53811937`;
[COMPLETE_PRIME_HEAT_TRACE.md](../COMPLETE_PRIME_HEAT_TRACE.md), SHA256
`d48987c9143620d6b433163c080a89f3bc4966764d0880a83666a671fda3fb29`;
and corrected [SHIFTED_COMPLETE_MOMENTS_V2.md](../SHIFTED_COMPLETE_MOMENTS_V2.md),
SHA256 `84dff8dd45a579649bf8c515ef273559147d0b3f4a12a158ce1d7fcad1e9505b`.
What was actually run: complete analytic derivation/read and direct proof-hash
authentication. No primitive native heat computation.
Smallest remaining gap: a sign theorem for the complete literal source,
or an authenticated strict negative derivative test with both tails retained.

## Prime coefficient identity and complete finite envelope

AP1–AP4 preserve the actual normalization. The functional equation changes
`xi(1/2-sqrt(t^2-w))` into `xi(1/2+sqrt(t^2-w))`; it does not alter the
logarithmic coefficient. Since the complete moment extraction is `-k[w^k]`,
the decomposition is exactly `C_k=G_k-P_k`. The prime coefficient has the
opposite sign from the Gamma coefficient in this completed identity.

The binomial coefficients of `t-sqrt(t^2-w)` are
`binom(2h,h)/(4^h(2h-1))*t^(1-2h)`, strictly positive. Differentiating the
exponential gives the stated finite Bell recurrence, including its `q/k`
factor. The Euler logarithm coefficient is exactly `Lambda(n)/log n`, equal
to `1/m` at `n=p^m`; it is not the logarithmic derivative weight.

For `|w|<=r<t^2-1/4`, the nonnegative shift series bounds
`Re s(w)>=1/2+sqrt(t^2-r)>1`. Uniform absolute Euler convergence justifies
termwise coefficient extraction. Nonnegative coefficients then bound the
complete discarded kth coefficient by its value at r divided by `r^k`.
Using `0<=Lambda(n)/log n<=1` and the decreasing-power integral gives exactly
`k*r^(-k)*N^(1-sigma_r)/(sigma_r-1)`. No literal prime tail is dropped.

The residual upper bound correctly uses a finite prime LOWER endpoint,
because the prime term is subtracted, and uses every selected root's UPPER
interval endpoint, because its inverse power decreases on the real axis.
It also retains the Gamma coefficient uncertainty. That bound supplies a
potential input to a shifted exclusion guard; it does not establish that
the guard succeeds.

At `w_1=t^2-1/4`, `s(w_1)=1` and `s'(w_1)=-1`. The elementary `s-1` zero
and zeta's residue-one pole give the exact opposite logarithmic singular
parts. Their separately displayed kth contributions to G_k and P_k are
both `w_1^(-k)` and cancel in the complete difference. This is a local
singular-part statement and is explicitly not a coefficient-asymptotic
claim. The completed source also removes the square-root branch at `w=t^2`
by its evenness in `s-1/2`. Separate positive Euler estimates therefore do
not automatically preserve the complete cancellations.

## Heat identity, interchanges and constants

HT1–HT2 use the full multiplicity-preserving spectral trace. On every compact
positive heat-time interval its derivative series converges normally: a
fixed polynomial times the Gaussian is bounded by a constant times the
summable inverse-square weights. For `X>1/4`,
`X+Re(rho^2)>0`, and the sum of absolute Laplace integrals is finite by the
same complete summability. Thus the complete product logarithmic derivative
is the Laplace transform of the complete trace without an RH premise.

An independent differentiation of
`log(s(s-1)/2)-s log(pi)/2+log Gamma(s/2)+log zeta(s)`, with
`s=1/2+sqrt X`, gives

\[
 f(X)=\frac1{X-1/4}
 +\frac{\psi(\sqrt X/2+1/4)-\log\pi}{4\sqrt X}
 -\frac1{2\sqrt X}\sum_{n\ge2}\Lambda(n)n^{-1/2}
                                        e^{-\sqrt X\log n}.
\]

In particular the elementary derivative is exactly `1/(X-1/4)`, the Gamma
coefficient is `1/4`, and the prime coefficient is `-1/2`. Applying the
Gaussian Laplace transform with parameter `q/2` in the digamma integral
produces `exp(-q^2/(16u))`; parameter `log n` in the Euler sum produces
`exp(-log^2(n)/(4u))`. These check every constant in HT6.

Near `q=0`, the combined Gamma numerator is `-3q/4+O(q^2)` for each fixed
positive u, so its division by `1-exp(-q)` is regular. For the joint Laplace
interchange, the stated split reduces the nonuniform Gaussian part to
`integral u^(-1/2)exp(-Xu) min(1,q^2/(16u)) du=O(q)`. Substitution `u=q^2 w`
gives a finite w integral; after division by the q denominator the remaining
q integral is locally integrable. The large-q part has exponential bounds.
The prime interchange is Tonelli on a nonnegative literal series and the
Euler half-plane sum is finite.

The literal prime heat series and each fixed derivative converge at every
positive time by the logarithmic block Gaussian estimate. Its large-time
absolute growth is a polynomial times `exp(u/4)`. The spectral expression
has the same exponential bound. Both functions are continuous for positive
u and absolutely Laplace integrable for `X>1/4`; uniqueness of the Laplace
transform therefore identifies them pointwise. This uses complete series
and the combined Gamma integral throughout, rather than termwise inversion
of a divergent Euler expression.

## Global criterion and its exact limitation

HT3 explicitly imports Bernstein–Widder. Under the asserted complete
monotonicity of K it supplies a positive measure on `[0,infinity)`, possibly
of infinite total mass. Tonelli converts the finite Laplace transform into
the Stieltjes integral `integral dnu(a)/(X+a)`. Finiteness at one positive X
pays the weighted total mass and establishes analyticity off the negative
real axis. Complete source resolvent poles have positive integer residues
and cannot cancel; the positive-half-plane squaring map is injective.
Identity continuation then excludes every nonreal `-rho^2` pole. The actual
theta source excludes imaginary-axis representatives. Conversely, real
zeros plainly give all complete-monotonicity signs. Thus the criterion is
equivalent to RH location and includes multiplicities; it does not prove
simplicity or supply the missing actual sign premise.

Failure of the criterion implies a strict negative derivative at a finite
order and positive time. Continuity permits a rational time witness. A
directed search could certify it only after authenticating the entire Gamma
integral and both complete tails. This manuscript supplies no such actual
negative derivative certificate or quadrature implementation.

For the separate polynomial example, the trace is exactly
`exp(-u)+2 exp(-15u/4) cos(2u)`. Its stated two-interval lower bounds prove
positivity for every u>0. Its Laplace transform is consequently completely
monotone for every X>0 even though the polynomial has off-real zeros. The
normalized integral logarithm is a Bernstein function, but K itself cannot
be completely monotone by the same noncanceling pole argument. All-time
heat positivity and all scalar shifted signs thus remain weaker than the
global criterion. This polynomial is not asserted to be the actual theta
source or a positive Fourier source.

## Complete derivative tail

Direct differentiation gives
`P_(r+1)=(z-r-1/2)P_r-z P'_r`; the recurrence and the powers of u in HT10
are correct. Applying it to the combined Gamma integrand preserves the
near-zero cancellation. For each prime-tail polynomial coefficient, the
absolute remainder is bounded by the decreasing function
`(log x)^(2j+1)*x^(-1/2)*exp(-log^2(x)/(4u_+))`.
The exact condition `log N>=2(2r+1)` makes its logarithmic derivative
negative for every `j<=r`. The second condition `log N>=4u_+` permits the
upper Gaussian exponent `-q^2/(8u_+)` after conversion to q coordinates.
The substitution `z=q^2/(8u_+)` gives precisely
`(8u_+)^(j+1)/2 * Gamma(j+1,Q^2/(8u_+))`, with the outer
`u_-^(-r-1/2)/(2 sqrt(pi))` and `(4u_-)^(-j)` factors stated in HT12.
Its integer incomplete Gamma endpoint is elementary and directed-computable.
The argument proves a sufficient complete bound; it makes no efficiency
claim and supplies no finite prime-weight authentication on its own.

Verdict: ACCEPT for AP1–AP4 and HT1–HT5 at the exact hashes above. These
complete source identities and equivalent criteria preserve the unresolved
actual-source sign and cofinal boundaries.
