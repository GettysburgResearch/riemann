# An even-sector, finite-matrix consumer with an explicit cofinal cutoff

Status: proposed analytic component theorems with proofs. The all-scale matrix lower bound and the all-scale positive-selector hypotheses remain OPEN.
Scope: exact finite compressions of the complete semilocal Weil form. This is not a finite numerical certificate of RH or of a new zero-free strip.
Dependencies: the source convention of PR #1017 (`450dd8abecf58dfe60b3bc39bda0f792ea82ce95`); the theta tail estimates and legal-resolvent framework of PR #1021 (`742e952be4ef7843de86ea12678c0bdd3d3579c3`); the companion `SPECTRAL_GROWTH_AND_TIGHT_POSITIVE_SELECTION.md`.
Smallest remaining gap: prove one of the exact cofinal matrix hypotheses below, uniformly in the interval half-width.

Two qualifications that obstruct a naive finite argument can be removed here. First, a bound on the **even** block is enough, by a one-sided Laplace argument. Second, at the specified cofinal Fourier cutoff, a finite-matrix selector theorem can be consumed without separately proving that each selected shift is legal for the infinite-dimensional operator.

## 1. Even-sector lower bounds suffice

Let `lambda_even(a)` denote the lowest value of the full Weil form restricted to even functions on `[-a,a]`. Suppose, for every `epsilon>0`,

\[
\lambda_{\rm even}(a)
\ge-C_\epsilon e^{(2\eta+\epsilon)a}
\tag{1}
\]

for all sufficiently large `a`, where `eta>=0` is fixed.

**Theorem 1.** Equation (1) excludes every zeta zero with `Re rho>1/2+eta`. No lower bound for the odd block is needed.

### Proof

Use a real even compact smooth bump `g` supported in `[-R,R]`, and put `C_g(t)=(K_W*(g*g))(t)`. This is real. The explicit formula and its meromorphic Laplace transform are exactly equations (8)--(10) of the companion note, with coefficient `G(z_rho)^2`.

For `t>2R`, the function

\[
g(x-t/2)+g(x+t/2)
\tag{2}
\]

is even and supported in `[-a,a]`, `a=t/2+R`. Its squared norm is `2||g||_2^2` and its form value is `2q[g]+2C_g(t)`. Hence (1) gives the one-sided estimate

\[
C_g(t)\ge-C_{g,\epsilon}e^{(\eta+\epsilon/2)t}.
\tag{3}
\]

Increasing the constant handles bounded `t`. Put `delta=eta+epsilon/2` and choose `C>0` so that

\[
D(t)=C_g(t)+Ce^{\delta t}\ge0\qquad(t\ge0).
\tag{4}
\]

Originally `C_g(t)=O_g(e^{t/2})`, by the unconditional zero strip and rapid decrease of its zero coefficients. Thus `D` has a finite Laplace convergence abscissa unless its transform is entire. Its meromorphic continuation is

\[
L_D(w)=\sum_\rho\frac{G(z_\rho)^2}{w-i z_\rho}
                  +\frac C{w-\delta}.
\tag{5}
\]

There is no real pole of (5) above `delta`: zeta has no real nontrivial zero. For completeness, on `0<s<1` its alternating series is positive by pairing adjacent terms, while `zeta(s)=eta(s)/(1-2^(1-s))<0`.

The elementary Landau lemma for nonnegative Laplace integrands says that a finite convergence abscissa is a singularity on the real axis. Its short proof is included below. Applying it to (4), the convergence abscissa cannot exceed `delta`. Therefore (5) is holomorphic on `Re w>delta`. If a zero has `beta-1/2>delta`, take `g` sufficiently concentrated near zero that `G(z_rho)!=0`. The corresponding nonzero residue in (5) is a contradiction. Choose epsilon small for any hypothetical zero with `beta-1/2>eta`. QED.

**Landau lemma used above.** If `D>=0` and its Laplace transform has finite convergence abscissa `sigma_c`, it cannot be holomorphic across the real point `sigma_c`. Otherwise choose a real `w_1>sigma_c` sufficiently close to that point that a Taylor disk reaches a real `w_2<sigma_c`. At `w_1`,

\[
(-1)^nL_D^{(n)}(w_1)=\int_0^\infty t^nD(t)e^{-w_1t}\,dt\ge0.
\]

The convergent Taylor series evaluated at `w_2` has nonnegative terms. Tonelli's theorem identifies its sum with `integral D(t)e^(-w_2t)dt`, contradicting the definition of `sigma_c`. Derivative differentiation is justified by the strict gap `w_1>sigma_c`. This proof uses the actual nonnegative integrand (4), not positivity of arbitrary moment data.

## 2. Exact finite matrices

For each integer `a=k>=1`, let

\[
N_k=\lceil k^3\rceil,
\qquad
E_k=\operatorname{span}\{1,\cos(\pi x/k),\ldots,
                              \cos(N_k\pi x/k)\}
\tag{6}
\]

on `[-k,k]`, with zero extension. Let `Q_k` be the exact compression of the full Weil form to this even subspace, with its `L2` inner product. Every prime power up to `exp(2k)` is included, and the archimedean integral and pole terms are exact. Finite quadrature approximations are not `Q_k` without an error bound.

Write `lambda_k=min spec(Q_k)`.

**Theorem 2 (finite spectral-growth consumer).** If, for every `epsilon>0`,

\[
\boxed{\lambda_k\ge-C_\epsilon e^{(2\eta+\epsilon)k}
       \quad(k\text{ sufficiently large}),}
\tag{7}
\]

then zeta has no zero with `Re rho>1/2+eta`.

Only an exact sequence of finite even matrices is required in (7). It is not claimed that their minima bound the infinite-dimensional minima from below.

### Projection estimates needed for the proof

There exist even nonnegative compact smooth bumps of integral one whose Fourier transforms satisfy

\[
|G(t)|\le C\exp(-c|t|^{2/3}).
\tag{8}
\]

Here is a self-contained construction. Convolve the centered uniform probability measures on intervals of half-widths `b_j=c_0 j^(-3/2)`. Their widths have finite sum, so the infinite convolution is a compactly supported probability measure. Its Fourier transform is `product_j sinc(b_j t)`. For a block of `j` comparable to `|t|^(2/3)`, arrange the fixed comparison constants so that `|b_j t|>=2`; each corresponding sinc factor has absolute value at most `1/2`. There are at least `c|t|^(2/3)` such factors, proving (8). The rapid decrease implies by Fourier inversion that this compact measure has a smooth density. Rescaling gives arbitrarily small support and hence nonvanishing `G(z_rho)` at any one prescribed hypothetical zero, as required in Section 1.

Let `P_k` be the orthogonal Fourier projection onto modes `|n|<=N_k` on `[-k,k]`. For any translate of this bump lying inside that interval, its Fourier coefficients are sampled values of `G`, multiplied by phases. The tail bound (8), including one differentiated Fourier series, gives

\[
\|P_kg-g\|_{L^\infty([-k,k])}
+\|(P_kg-g)'\|_{L^\infty([-k,k])}
\le C(1+k)^C\exp(-c k^{4/3}).
\tag{9}
\]

The same constants work for the translated bumps in (2); translation changes only the sampled phases. The effective frequency cutoff is `N_k*pi/k`, of order `k^2`. A sum of its rapidly decreasing Fourier tail is bounded by the corresponding integral, giving (9). Even sums of the translates project into (6).

Let `r` be the projection error on `[-k,k]`, extended by zero, and let the right side of (9) be `d_k`. Direct integration by parts gives

\[
|\widehat r(t)|\le2k d_k,
\qquad
|\widehat r(t)|\le(2d_k+2k d_k)/|t|\quad(t\ne0).
\tag{10}
\]

Thus

\[
\int\log(2+|t|)|\widehat r(t)|^2dt\ll k^2d_k^2.
\tag{11}
\]

This explicitly controls the logarithmic form domain despite the possible small jump of the zero-extended projection at the endpoints. No false `H1` assertion for that extension is used.

The remaining pole and finite-prime operators have combined `L2` norm at most `Ck e^k`, by the same elementary estimates as PR #1017. Their error in the polarized form is bounded by this norm times the `L2` projection error and the bounded norm of the fixed bump or two-bump test. Equations (9)--(11) therefore imply

\[
q[P_kg]=q[g]+o(1),\qquad
q[P_k(g_-+g_+)]=q[g_-+g_+]+o(1),
\tag{12}
\]

uniformly when the two centers are at `+-t/2` and `k=ceil(t/2+R)`. In the latter statement the derivatives of the bumps and their weighted Fourier norms are unchanged by translation; the small boundary clearance may be zero, but smooth compact support and the Fourier tail bound remain valid.

### Proof of Theorem 2

Apply the exact finite lower bound (7) to the projection of (2), with `k=ceil(t/2+R)`. Equations (9)--(12) preserve its norm and form value, with errors tending to zero faster than `exp(-c k^(4/3)+Ck)`. This gives

\[
C_g(t)\ge-C_{g,\epsilon}e^{(\eta+\epsilon/2)t}.
\]

The Landau/Laplace argument of Section 1 now excludes the target zero. The bump (8) can be chosen to avoid that zero's vanishing coefficient. This proves (7)'s implication without an infinite-dimensional spectral comparison. QED.

## 3. Finite positive tight selectors suffice as well

For each `k` choose an exact finite legal shift `kappa_k<lambda_k`, and define the mass-normalized finite resolvent

\[
u_k=(Q_k-\kappa_k)^{-1}1,
\qquad f_k=u_k/\int u_k.
\tag{13}
\]

It is an even trigonometric polynomial on `[-k,k]`, extended by zero. Its finite variational equation and mass-constrained minimum are exact.

**Theorem 3 (finite positive-selector consumer).** If the physical functions `f_k` are nonnegative on their complete intervals and their probability measures are uniformly tight, then `kappa_k->0` and RH holds. Uniformly bounded second moments suffice for tightness.

In particular, exact nonnegative variance-matched solutions for the finite matrices (6), for all sufficiently large `k`, would suffice. A grid sign check is not the nonnegativity premise in this theorem.

### Finite theta test vectors with sup-norm residual control

We give the needed approximants explicitly. For a smooth even rapidly decreasing function `v`, periodize it with period `2k` and truncate its Fourier series at `N_k`. Denote the resulting polynomial by `S_kv`. Its Fourier coefficients are `v_hat(n*pi/k)/(2k)`.

The theta transform `X(t)` has the unconditional bound

\[
|X(t)|\le C(1+|t|)^C e^{-\pi|t|/4},
\tag{14}
\]

from the defining gamma factor, Stirling's formula, and an elementary polynomial bound for zeta on the critical line. Hence both `S_k phi` and its first derivative differ from the periodized theta density by at most `C k^C exp(-c k^2)`.

Subtract the constant endpoint value `(S_k phi)(k)` and normalize the resulting polynomial to have integral one. Call it `v_k`. It vanishes at both endpoints; its derivative does too because it is an even trigonometric polynomial. Its zero extension is therefore `C1` and belongs to the actual operator domain. The endpoint subtraction and normalization cost only

\[
O(k^C e^{-c k^2})+O(\exp(Ck-c e^{2k})).
\tag{15}
\]

On every fixed central interval, `v_k` tends uniformly to `phi`; globally inside `[-k,k]` its negative part in sup norm tends to zero.

For a broad comparator, choose a fixed nonnegative even smooth probability density `eta` supported in `(-1,1)`, put `w=phi*eta_(k/2)`, and perform the same Fourier truncation, endpoint subtraction, and mass normalization. Call the result `w_k`. Since `|eta_hat((k/2)t)|<=1` on the real axis, (14) gives the same Fourier-tail bound. The omitted periodization tails now have size `exp(Ck-c e^k)`. Thus

\[
\|w_k\|_2^2\le C/k+o(1/k).
\tag{16}
\]

For completeness, the full-source residual is controlled in sup norm, not merely in a form norm. Let `r_k` be the difference between one of these zero-extended polynomials and its uncut theta/convolved-theta source. It is `C1`, and

\[
|r_k(x)|+|r_k'(x)|\le B_k e^{-2|x|},
\quad
B_k\le C k^C e^{2k-c k^2}+C\exp(Ck-c e^k).
\tag{17}
\]

The complete operator formula bounds its pole term on `[-k,k]` by `C B_k e^{k/2}`, its archimedean term by `C B_k`, and its prime-power term by `C B_k e^{2k}`. The last bound uses `Lambda(n)<=log n` and the convergent sum `sum_(n>=2) (log n)n^(-5/2)`, including every power beyond the interval's finite translation range when applied to the noncompact residual. Consequently

\[
\|A_kv_k\|_\infty+\|A_kw_k\|_\infty\le\epsilon_k\longrightarrow0.
\tag{18}
\]

Equations (17)--(18) give the stronger rate `k epsilon_k->0`, which
also controls the nonnegative-shift Rayleigh quotient below.

The mass normalizations tend to one and have been included in these bounds. Also `||w_k||_1` is bounded, so `|q[w_k]|<=||w_k||_1||A_kw_k||_infinity=o(1)`.

### Proof of Theorem 3

Pair the exact finite equation for (13) with `v_k`, which belongs to the same finite subspace. Nonnegativity, mass one, and (18) bound the residual by `epsilon_k` without any `L2` norm of `f_k`. Tightness and (15) give `liminf <f_k,v_k>>0`.

Use `w_k`, also in that finite subspace, as the mass-one variational comparator. Equations (16)--(18) reproduce (15)--(19) of the companion note, with the infinite-dimensional spectral minimum replaced throughout by the finite `lambda_k`. Therefore negative shifts tend to zero; nonnegative legal shifts do too, by the finite Rayleigh upper bound from `w_k`.

Now `lambda_k>kappa_k->0`, so the finite spectral-growth premise (7) holds with `eta=0` (indeed a uniform finite lower bound eventually suffices). Theorem 2 proves RH. No inference that a finite spectral minimum is a continuum lower bound has been made. QED.

## 4. Exact remaining tasks and numerical scope

The full finite matrix entries are already specified by the pinned source, including their analytic archimedean tail. The new cofinal choice `N_k=ceil(k^3)` is an explicit sufficient schedule for the projection argument; no optimality is claimed.

The research targets are now either:

- the complete even-matrix growth estimate (7), with `eta=1/4` giving `Re s>3/4`; or
- exact finite-legal, globally nonnegative, uniformly tight selectors (13) along this cofinal sequence, which would give RH.

A finite number of positive matrices, variance roots, or sign samples proves neither premise. The diagnostic script in this directory explores actual source matrices and reports its quadrature, precision, parity, and sign-sampling limits. It does not establish (7), all-scale selector existence, or interval-certified positivity.
