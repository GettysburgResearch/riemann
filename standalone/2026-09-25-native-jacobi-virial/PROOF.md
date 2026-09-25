# NJV34: native Jacobi, Fourier, and logarithmic-virial comparisons

**Date:** 25 September 2026.  
**Status:** proposed component mathematics, with exact finite replay; independent review required.  
**Parent:** RAB33, PR #907, commit `12433ee0056756da006788a8b82e492aac9e6d1d`.  
**Scope:** finite-source identities for every cutoff, an explicit classical spectral comparison, and a source-specific uniform bound for one completely specified covariance. No new asymptotic bound for the native energy or proof of RH is claimed.

## 0. The actual advance and the attribution boundary

The previous pass proposed a relative arithmetic/Fourier theory but had not constructed a quantitative comparison for the native cumulative-sum metric. This pass supplies an exact finite-source comparison in that metric and a source-specific signed balance law. It is not the full Poisson/Weil trace comparison requested by the broader programme.

The main results are:

1. The literal Mertens energy is a Dirichlet Green energy for a simple tridiagonal Jacobi matrix. It is also exactly the **centered**, not uncentered, variance of reciprocal partial sums. Arithmetic Schur elimination preserves this Jacobi form up to an explicit scale and one terminal boundary correction.
2. That Green energy has explicit continuous dual Hahn and log-Fourier realizations, with the native boundary terms preserved. No prime-complete tail is used.
3. For the actual Mobius source, a complete von Mangoldt-weighted dilation covariance plus its explicit logarithmic drift is a positive resolvent energy, between zero and twice the native energy at **every** cutoff. This is a linear, cutoff-uniform estimate for the drift-corrected target, not an estimate for arbitrary covariance weights.
4. A Liouville gauge and an exact signed-count formula show why the raw multiplicative boundary Gram kernel from the parent packet does not itself supply Mobius cancellation.

The matrix `1/max(m,n)`, its Hardy-kernel/Jacobi theory, and continuous dual Hahn polynomials are **established mathematics**. The relevant literature includes Brevig--Perfekt--Pushnitski, *The spectrum of some Hardy kernel matrices*, and Stampach's Hilbert L-matrix work. The continuous dual Hahn orthogonality and hypergeometric normalization used below are imported from the classical theory, as recorded in NIST DLMF 18.25--18.26. The arithmetic identity behind the virial law is the classical logarithmic derivative of Dirichlet convolution. We claim neither invention of those objects nor external priority for these consequences. The contribution is their explicit, source-faithful assembly and quantitative use in this project.

## 1. The native finite object

Let `N>=1`, `X=N+1`, and let `c=(c_1,...,c_N)` be complex coefficients. Put

\[
S_c(k)=\sum_{n\le k}c_n,\qquad
\mathcal E_N(c)=\sum_{k=1}^N\frac{|S_c(k)|^2}{k(k+1)}.
\tag{1.1}
\]

When `c_n=mu(n)`, write `M(k)=S_c(k)` and `E_N=mathcal E_N(mu)`. The coefficients, cutoff, and summation weights are literal. No minimizing mollifier is substituted for `mu`.

Define the cumulative matrix `C_(k,n)=1_(n<=k)` and `W=diag(1/[k(k+1)])`. Then

\[
K_N=C^*WC,\qquad
(K_N)_{mn}=\frac1{\max(m,n)}-\frac1{N+1},\qquad
\mathcal E_N(c)=c^*K_Nc.
\tag{1.2}
\]

The entry formula follows by telescoping the sum over `k>=max(m,n)`.

### Theorem 1: exact local inverse and Dirichlet comparison

The inverse `A_N=K_N^{-1}` has entries

\[
(A_N)_{nn}=2n^2,\qquad
(A_N)_{n,n+1}=(A_N)_{n+1,n}=-n(n+1),
\tag{1.3}
\]

with all other entries zero. Let `h=K_Nc` and `d_n=nh_n`, with `d_0=d_(N+1)=0`. Then

\[
2d_n-d_{n-1}-d_{n+1}=\frac{c_n}{n},\qquad
\mathcal E_N(c)=\sum_{n=1}^{N+1}|d_n-d_{n-1}|^2.
\tag{1.4}
\]

**Proof.** The inverse of `C` is the lower-bidiagonal difference matrix `D`, with diagonal 1 and subdiagonal -1. Hence `A_N=D W^{-1}D^*`; its diagonal is `n(n+1)+(n-1)n=2n^2`, including the first diagonal entry, and its off-diagonal is `-n(n+1)`. Equivalently `A_N=diag(n) L_N diag(n)`, where `L_N` is the usual Dirichlet second-difference matrix. The equation and energy follow by finite summation by parts. This proof applies to every complex source. QED.

This is a discrete Poisson comparison, not the Weil explicit formula or a claim that zeta zeros are eigenvalues of `A_N`.

### Corollary 1.1: exact centered reciprocal variance

Set `s_0=0` and `s_j=sum_(n<=j)c_n/n`. Then

\[
\bar s_N=\frac1{N+1}\sum_{j=0}^Ns_j
=s_N-\frac{S_c(N)}{N+1},
\]
\[
\boxed{\mathcal E_N(c)=\sum_{j=0}^N|s_j-\bar s_N|^2
=\min_{b\in\mathbb C}\sum_{j=0}^N|s_j-b|^2.}
\tag{1.5}
\]

Indeed, the solution in (1.4) has

\[
d_n-d_{n-1}=\sum_{m=n}^N\frac{c_m}{m}-\frac{S_c(N)}{N+1}
=\bar s_N-s_{n-1}.
\]

In particular, if the uncentered reciprocal energy is `F_N=sum_(j=1)^N |s_j|^2`, then

\[
F_N=\mathcal E_N(c)+(N+1)|\bar s_N|^2.
\tag{1.6}
\]

The additional scalar term is not declared small. This identity does **not** identify the repository's E and F quantities without paying their centering correction, and it says nothing automatically about other historical normalizations.

### Theorem 1.2: exact arithmetic Schur renormalization

Eliminate from A_N every index not divisible by an integer a with `2<=a<=N`. Let `m=floor(N/a)` and `r=N+1-am`, so `1<=r<=a`. On the retained indices `a,2a,...,ma`, the Schur complement is exactly

\[
\boxed{\operatorname{Schur}_{a\mathbb N}(A_N)
=aA_m+\frac{am^2(a-r)}r\,e_me_m^*.}
\tag{1.7}
\]

In particular, whenever `a|(N+1)`, the effective matrix is **exactly `a A_m`**: multiplication changes the scale, but not the Jacobi form. At other cutoffs the entire discrepancy is one explicitly positive terminal entry, not a distributed completion tail.

**Proof.** The inverse Schur complement is the retained principal block of K_N. Its entries are

\[
\frac1a\left(\frac1{\max(i,j)}-\frac1{m+1}\right)
-\delta,\quad \delta=\frac1{N+1}-\frac1{a(m+1)}.
\]

Thus it is `K_m/a-delta 11^*`. Use `A_m 1=m(m+1)e_m` and the elementary rank-one inverse formula. Its denominator is
`1-a delta m(m+1)=r(m+1)/(am+r)>0`, giving precisely (1.7). QED.

Successive eliminations along prime factors give the same operator as retaining multiples of their product directly, by the finite block-elimination identity. This is valid with all terminal corrections kept, not just when cutoffs happen to align. The checker independently performs rational Gaussian elimination and tests both factor orders 2 then 3 and 3 then 2.

There is also an exact closed family if one retains a real boundary endpoint X with `N<X<=N+1`: use `K_N(X)_(ij)=1/max(i,j)-1/X`. Its inverse differs from A_N only by the terminal entry `N^2(N+1-X)/(X-N)`. Arithmetic elimination rescales the endpoint to `X/a` and the inverse matrix by a. This explains the integer-rounding term as ordinary boundary geometry.

The Schur complement construction is classical linear algebra. Its role here is to supply a composable arithmetic scale operation for the same **additive metric** that measures the native source. It does not estimate the covariance between the retained channel and the eliminated channels of a full Euler update.

## 2. The explicit classical spectral bridge

For `t>0` define the real polynomials

\[
p_m(t)={}_3F_2\!\left(\begin{matrix}-m,\;1/2+it,\;1/2-it\\1,\;2\end{matrix};1\right),
\quad m=0,1,\ldots,
\tag{2.1}
\]

and the weight

\[
w(t)=2\pi t(t^2+1/4)\frac{\sinh(\pi t)}{\cosh^2(\pi t)}.
\tag{2.2}
\]

These are the continuous dual Hahn parameters `(a,b,c)=(1/2,1/2,3/2)`, divided by `m!(m+1)!`. The imported classical orthogonality gives

\[
\int_0^\infty p_m(t)p_n(t)w(t)\,dt=\delta_{mn}.
\tag{2.3}
\]

For precision about normalization: DLMF integrates its polynomial variable `x=t^2`, whose weight contains `1/(2t)`. After changing to `dt`, dividing the standard polynomial by `m!(m+1)!`, and dividing the measure by `2pi`, its gamma-product weight becomes (2.2), by the elementary gamma reflection and recurrence formulas. All three parameters are positive, so no discrete mass terms enter this orthogonality formula.

The recurrence is

\[
2n^2p_{n-1}-n(n-1)p_{n-2}-n(n+1)p_n
=(t^2+1/4)p_{n-1},\quad n\ge1,
\tag{2.4}
\]

where the term with `p_(-1)` has zero coefficient. It follows either from the standard recurrence, or coefficientwise from the terminating series (2.1). The first polynomials are

\[
p_0=1,\quad p_1=\frac78-\frac12t^2,\quad
p_2=\frac{51}{64}-\frac{19}{24}t^2+\frac1{12}t^4.
\]

### Theorem 2: exact relative Green transform

For every finite complex source `c` supported through `N`,

\[
\boxed{
\mathcal E_N(c)=
\int_0^\infty\left|\sum_{n=1}^Nc_np_{n-1}(t)\right|^2
\frac{w(t)}{t^2+1/4}\,dt
-\frac{|S_c(N)|^2}{N+1}.}
\tag{2.5}
\]

**Proof without an unproved completeness assumption.** Fix `m>=1` and put

\[
q_n=\int_0^\infty\frac{p_{m-1}(t)p_{n-1}(t)}{t^2+1/4}w(t)\,dt.
\]

Bessel's inequality for the orthonormal family (2.3) implies `(q_n) in l2`, because `p_(m-1)/(t^2+1/4)` is square integrable. Multiplying (2.4) by `p_(m-1)w/(t^2+1/4)` and integrating gives `Aq=e_m` coordinatewise.

The sequence `g_n=1/max(m,n)` is also in `l2` and satisfies the same recurrence with right-hand side `e_m`, by direct substitution. For their difference `r`, write `b_n=nr_n`. The homogeneous recurrence says `2b_n-b_(n-1)-b_(n+1)=0`; the first row gives `r_1=r_2`, equivalently `b_2=2b_1`. Thus `b_n=nb_1` and `r_n=b_1` for every n. Square summability forces `b_1=0`. Therefore

\[
\int_0^\infty p_{m-1}(t)p_{n-1}(t)\frac{w(t)}{t^2+1/4}\,dt
=\frac1{\max(m,n)}.
\tag{2.6}
\]

Expansion of the finite square and (1.2) prove (2.5). Only finite sums are interchanged with integrals. QED.

No spectral completeness theorem or delicate choice of an unbounded Jacobi extension is needed for this finite-source result. Broader spectral theory of the Hardy kernel is available in the cited literature; it is not a discovery of this pass.

### 2.1 Exact moment authentication

Let `rho=w/(t^2+1/4)=-2t(d/dt)sech(pi t)`. If `E_(2k)` denotes the signed Euler number defined by the Taylor series for `sech`, then

\[
\int_0^\infty t^{2k}\rho(t)dt
=\frac{(2k+1)|E_{2k}|}{2^{2k}}.
\tag{2.7}
\]

This follows by integration by parts and the cosine transform
`integral_0^infty sech(pi t)cos(zt)dt=1/[2cosh(z/2)]`; differentiating at zero gives the moments. For a direct derivation of the transform, substitute `y=exp(2pi t)` in its full-line version and use the beta integral `integral_0^infty y^(alpha-1)/(1+y)dy=pi/sin(pi alpha)` with `alpha=1/2+iz/(2pi)`. The rapid exponential tail justifies the differentiations.

The checker uses (2.7), computed from the integer Euler-number recurrence, to check both (2.3) and (2.6) for **all 441 pairs of degrees 0 through 20**. It separately generates (2.1) and (2.4) and checks their coefficientwise agreement. These finite checks test normalization and implementation; they do not replace the classical orthogonality theorem or the proof above.

### 2.2 Why the critical-looking parameter is not an RH result

From (2.3) and `1/(t^2+1/4)<=4`,

\[
0\le\mathcal E_N(c)\le4\sum_{n\le N}|c_n|^2.
\tag{2.8}
\]

For `mu`, this is only `E_N<=4N`. The positive spectral coordinate `t^2+1/4` is a property of this Hardy/Jacobi metric for **every** source. It does not identify zeta ordinates, supply their reality, or yield cancellation for the actual Mobius polynomial. The source-specific spectral mass remains the difficult part.

## 3. A tail-free log-Fourier comparison and arithmetic scaling

Put `L=log X` and

\[
f_{c,N}(u)=e^{-u/2}S_c(\lfloor e^u\rfloor)\mathbf1_{[0,L)}(u).
\tag{3.1}
\]

Its squared `L2(du)` norm is (1.1). With Fourier convention
`hat f(t)=integral f(u)e^(-itu)du`, define the **balanced finite numerator**

\[
B_N(c;s)=\sum_{n\le N}c_nn^{-s}-S_c(N)X^{-s}.
\]

Direct integration of the step functions gives, at `s=1/2+it`,

\[
\widehat f_{c,N}(t)=\frac{B_N(c;s)}s,
\qquad
\boxed{\mathcal E_N(c)=\frac1{2\pi}\int_{\mathbb R}
\frac{|B_N(c;1/2+it)|^2}{1/4+t^2}\,dt.}
\tag{3.2}
\]

At `s=0`, `B_N(c;0)=0`; there is no genuine pole in this finite integral formula. The endpoint subtraction is exactly what kills the continuation beyond `X`, not a discretionary damping term. It cannot be dropped. This is ordinary Mellin/Fourier Plancherel with an explicitly preserved source.

### 3.1 The exact causal Euler realization

Let `(T_delta f)(u)=1_(delta<=u<L)f(u-delta)` on `L2(0,L)` and `h_L(u)=e^(-u/2)`. Then

\[
f_{\mu,N}=\prod_{p\le N}(I-p^{-1/2}T_{\log p})h_L.
\tag{3.3}
\]

Expansion gives `e^(-u/2)` times the signed count of squarefree products at most `e^u`. Products outside the cutoff vanish by causality. Unlike the full prime completion of RAB33, there is no uncontrolled far tail. Restricting from a longer interval to a shorter one commutes with every causal shift, so these source realizations are compatible under restriction.

For a finite prime set P and a new prime p,

\[
\|f_{P\cup\{p\},L}\|^2=\|f_{P,L}\|^2
+\frac1p\|f_{P,L-\log p}\|^2
-\frac2{\sqrt p}\operatorname{Re}\langle f_{P,L},T_{\log p}f_{P,L}\rangle.
\tag{3.4}
\]

The prefix norm is zero if `L<=log p`. This is not monotone contraction: at `N=5`, P={2} gives energy 1/2, while adjoining 3 gives 2/3.

### 3.2 The exact integer-rounding defect

For integer `a>=1`, set `m=floor(N/a)` and let `V_a c` be the dilated coefficient sequence, `(V_a c)_n=c_(n/a)` when `a|n`, zero otherwise. Then

\[
B_N(V_ac;s)=a^{-s}B_m(c;s)
+S_c(m)\big([a(m+1)]^{-s}-X^{-s}\big),
\tag{3.5}
\]
\[
\boxed{\mathcal E_N(V_ac)=\frac1a\mathcal E_m(c)
-|S_c(m)|^2\left(\frac1X-\frac1{a(m+1)}\right).}
\tag{3.6}
\]

The correction is nonnegative before its minus sign, and vanishes when `a|(N+1)`. Proof: the uncut dilated cumulative source extends constantly from `X` to `a(m+1)`; removing exactly that interval removes its displayed energy. The convention `S_c(0)=E_0=0` handles `a>N`. This is an exact scale theorem for a source component, not a bound for the sum over many primes with cross terms omitted.

## 4. A complete source-specific logarithmic covariance bound

All statements in this section hold for every integer `N>=1`. No infinite Euler product or zero-free region is assumed.

The classical coefficient identity is

\[
\mu(n)\log n=-\sum_{d\mid n}\Lambda(d)\mu(n/d),
\tag{4.1}
\]

where `Lambda(p^a)=log p` for every prime power `p^a`, and Lambda is zero otherwise. For example, (4.1) follows from the derivation rule for `Dg(n)=g(n)log n`, the identity `mu*1=delta`, and `log=Lambda*1`. This is exact arithmetic, not analytic continuation of `-zeta'/zeta`.

Summing (4.1), using finite Abel summation, and setting `x=e^u`, gives

\[
u f(u)+\sum_{2\le d\le N}\frac{\Lambda(d)}{\sqrt d}
(T_{\log d}f)(u)=(Rf)(u),\quad 0<u<L,
\tag{4.2}
\]

where `f=f_(mu,N)` and

\[
(Rf)(u)=\int_0^u e^{-(u-v)/2}f(v)dv.
\tag{4.3}
\]

The appearance of `u f` is the logarithmic moment; it is not a removable nuisance.

Define

\[
V_N=\int_0^L u|f(u)|^2du,
\]
\[
\begin{split}
W_N&=\sum_{2\le d\le N}\frac{\Lambda(d)}{\sqrt d}
\operatorname{Re}\langle f,T_{\log d}f\rangle\\
&=\sum_{p^a\le N}\log p\sum_{k=p^a}^N
\frac{M(k)M(\lfloor k/p^a\rfloor)}{k(k+1)}.
\end{split}
\tag{4.4}
\]

Here `W_N` includes **every prime power and every contributing cell**. It is this weighted dilation covariance, not the full Newton composite covariance or the Weil form, that the following theorem controls.

### Theorem 3: native logarithmic-virial comparison

\[
\boxed{W_N+V_N=Q_N,\qquad 0\le Q_N\le2E_N.}
\tag{4.5}
\]

More precisely,

\[
Q_N=\frac12\int_0^L\!\int_0^L
 e^{-|u-v|/2}\overline{f(u)}f(v)\,du\,dv
=\frac1{4\pi}\int_{\mathbb R}
\frac{|B_N(\mu;1/2+it)|^2}{(1/4+t^2)^2}\,dt.
\tag{4.6}
\]

Consequently,

\[
-V_N\le W_N\le2E_N-V_N,\qquad
|W_N|\le\max(\log(N+1),2)E_N.
\tag{4.7}
\]

The finite-length improvement `Q_N<=2(1-X^(-1/4))E_N` also holds.

**Proof.** Take the real inner product of (4.2) with f. The real part of the Volterra kernel is the symmetric kernel `e^(-|u-v|/2)/2`. Its Fourier multiplier on the real line is `(1/2)/(1/4+t^2)`, nonnegative and at most 2. Extending f by zero and applying Plancherel proves (4.5)--(4.6). Since `0<=V_N<=L E_N`, (4.7) follows. For the finite-length improvement, each row integral of the symmetric kernel on `[0,L]` is `2-e^(-u/2)-e^(-(L-u)/2)<=2-2e^(-L/4)`; Schur's test gives the claim. QED.

This is an actual all-cutoff, source-specific quantitative statement: the drift-corrected complete target has a bound **linear in E_N with an absolute constant**. Bounding its individual correlations by Cauchy--Schwarz instead would pay `sum_(d<=N)Lambda(d)/sqrt(d)` times the energy and miss the exact signed compensation. However, the result does not upper-bound E_N itself. The covariance is forced to compensate the log moment; it is not proved to have an independently favorable sign or size in every other weighting.

### 4.1 Coherence on a later logarithmic window

For `0<=T<L`, let `E_before=integral_0^T|f|^2` and `E_window=integral_T^L|f|^2`. Restrict the **full** equation (4.2), not just its sources entirely inside the window. Then

\[
W_{[T,L]}+V_{[T,L]}=Q_{\rm window}+\mathcal B_T,
\tag{4.8}
\]

where the local positive kernel obeys `0<=Q_window<=2E_window` and

\[
\mathcal B_T=\operatorname{Re}\left[
(Rf)(T)\int_T^L e^{-(u-T)/2}\overline{f(u)}du\right],
\quad |\mathcal B_T|\le\sqrt{E_{\rm before}E_{\rm window}}.
\tag{4.9}
\]

Indeed, split the Volterra integral at T, and apply Cauchy--Schwarz to each of the two displayed boundary factors. The sharper factors `sqrt(1-e^(-T))sqrt(1-e^(-(L-T)))` may be retained. This one-dimensional boundary functional is the exact memory of the preceding interval. A window-only argument that omits it is not source faithful.

### 4.2 Exact finite authentication, not merely floating agreement

Let `D=lcm(1,...,N+1)` and `w_k=D/[k(k+1)]`. Define integer prefixes `H_k=sum_(j<=k)M(j)w_j`. The rational coefficient of `log p` in W_N is computed from all `d=p^a` by

\[
D A_d=\sum_{j=1}^{\lfloor N/d\rfloor}M(j)
\big(H_{\min(N,d(j+1)-1)}-H_{dj-1}\big).
\tag{4.10}
\]

The checker compares this hyperbola grouping with direct full-cell summation on the smaller panels.

Independently integrating the cell formulas gives the following representations as a rational constant plus rational coefficients of prime logarithms:

\[
V_N=E_N+\sum_{k=1}^NM(k)^2\left(\frac{\log k}{k}-\frac{\log(k+1)}{k+1}\right),
\tag{4.11}
\]
\[
Q_N=E_N+\sum_{j=1}^N\log\frac{j+1}{j}
\left[M(j)\sum_{k=j+1}^N\frac{M(k)}{k(k+1)}-\frac{M(j)^2}{j+1}\right].
\tag{4.12}
\]

Integer factorization of the logarithm arguments lets the checker verify `Q_N-V_N=W_N` **coefficientwise**, without evaluating any logarithm. Separate outward dyadic logarithm enclosures provide the displayed numeric intervals. No numerical quadrature or zeta oracle enters acceptance.

### 4.3 Literal twists, not family averaging

For any completely multiplicative complex chi, set `c_n=mu(n)chi(n)`, and replace Lambda(d) in (4.1)--(4.4) by `Lambda(d)chi(d)`. The derivation is unchanged. Take real inner products in the covariance definition; the same positive Q and inequalities hold member by member. The finite prime product uses `I-chi(p)p^(-1/2)T_(log p)`.

The checker also executes real character controls modulo 3 and modulo 4, preserving vanishing values and every prime power. It does not infer the principal member from their average, or derive a new bound uniform in conductor.

## 5. Why the raw multiplicative Gram positivity does not close the problem

Let `ell(n)=(-1)^Omega(n)` be Liouville's completely multiplicative sign, and let `Ge_n=ell(n)e_n`. Then

\[
GV_aG=\ell(a)V_a,\qquad GP_NG=P_N,\qquad
G(\mu(n))_{n\le N}=(\mu(n)^2)_{n\le N}.
\tag{5.1}
\]

Thus multiplicative relations, numerical cutoffs, and unitary-invariant positivity alone permit an exact change from signed squarefree coefficients to unsigned ones, provided the representation is conjugated too. This is a specific obstruction to extracting cancellation from only those invariant structures, not a theorem that every multiplicative method is impossible. The additive cumulative metric K_N is not preserved by this sign gauge.

There is a stronger literal diagnostic for the parent's escape maps. Let `E_(a,N)=(I-P_N)V_aP_N`, `g=gcd(a,b)`, `a'=a/g`, `b'=b/g`. Then

\[
\langle E_{a,N}\mu_N,E_{b,N}\mu_N\rangle
=\mu(a')\mu(b')
\sum_{N/\operatorname{lcm}(a,b)<k\le N/\max(a',b')}
\mu(k)^2\mathbf1_{(k,a'b')=1}.
\tag{5.2}
\]

**Proof.** Equal output indices require `an=bm`, hence `n=b'k`, `m=a'k`. Multiplicativity and squarefreeness give `mu(a'k)mu(b'k)=mu(a')mu(b')mu(k)^2 1_(gcd(k,a'b')=1)`, including the zero cases. The support is exactly the parent's gcd/lcm interval. QED.

If a and b are squarefree, multiplying (5.2) by `mu(a)mu(b)` makes it nonnegative: since g, a', b' are then pairwise coprime, the signs cancel to a square. Therefore the corresponding complete Mobius-weighted raw escape Gram sum has no termwise sign cancellation to exploit. The favorable first-exit orthogonality of a single product must not be mistaken for a Mobius cancellation theorem after adding products.

The place where source cancellation survives is the interaction with the additive metric or its exact spectral representations, not a missing sign hidden in the raw Gram count.

## 6. Research consequence and precise remaining gap

The finite comparison requested in RAB33 is now realized for the **native cumulative-sum energy**: coefficient source, additive Dirichlet energy, centered reciprocal variance, log-Fourier transform, and classical dual Hahn Green transform agree with explicit endpoint corrections. The source-specific virial law additionally controls one full weighted dilation target at every scale.

This is still not the full relative Fourier/Poisson mechanism needed for RH. The following distinctions are decisive:

- The explicit positive kernel is universal in c. Its general bound is only (2.8); the native Mobius source is not thereby small.
- W_N in Theorem 3 is not the open Newton composite target. No adapter with its exact centering, weights, phase and endpoint terms has been proved here.
- The available equation fixes W_N+V_N, not V_N or E_N separately. Using (4.5) as an assumed independent bound on the unknown source would be circular.
- The known spectral parameter `t^2+1/4` is not a Hilbert--Polya spectrum for zeta.

The next substantive theorem should control how the arithmetic source's spectral mass is distributed **relative to this fixed additive metric**, or show that a complete repository covariance can be decomposed into the controlled logarithmic direction plus a remainder that is independently smaller. The remaining remainder cannot simply be relabeled positive.

The practical next calculation is not a fit to E_N: express the exact target kernel against these logarithmic dilation directions, retain the residual kernel, and test whether its source-restricted quadratic form has a new coercive or cancellation identity. A successful kernel adapter would let the source-specific estimate above do useful work; its existence is not asserted.

## 7. Scope of validation and external dependencies

`check.py` uses the Python standard library, exact rational polynomials, integer Euler numbers, primitive Mobius authentication by Dirichlet inversion, exact prime-log coefficient vectors, and outward dyadic logarithms. See VALIDATION.md and receipt.json for executed ranges, counts and mutation tests.

Analytic Plancherel, the continuous dual Hahn orthogonality, the sech transform, and the written universal proofs have not been verified by a proof assistant or independently reviewed. The finite checks do not establish their infinite versions. No repository-wide CI or historical branch validation is claimed.

All inherited files in RAB33 are unchanged. This pass is a separate proposed object, not a silent promotion of the parent packet or of integrated claims.
