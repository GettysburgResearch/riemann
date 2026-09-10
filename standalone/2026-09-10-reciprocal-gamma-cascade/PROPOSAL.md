# Reciprocal gamma cascades: a constructive Bessel-to-xi research programme

Date: 2026-09-10. Status: **proposed component arguments and an open spectral programme; independent review required.** RH is not proved. This is a separate research direction, not an integration or a change to accepted status.

The proposed change of strategy is to start with a genuinely self-adjoint, real-zero model and approach the **entire original xi function through a prescribed positive convolution cascade**. A reciprocal projection enforces the exact functional-equation symmetry at every finite stage. We establish the source limit and a quantitative full-strip error independently of any zero assertion. The missing step is a source-specific zero-confinement theorem for this family, not convergence of the approximants.

The classical gamma-sum/xi representation is due to the probability literature, including Biane–Pitman–Yor [E1]. Their paper also studies finite exponential-sum Mellin approximations. The Bessel/Sturm mechanism is classical [E2–E4]. No priority claim is made for those ingredients or for the proposed combination. The finite reciprocal projection and the explicit estimates below are supplied with proofs rather than attributed as already accepted repository results.

## 1. Prescribed positive arithmetic cascade

Let G_n, n >= 1, be independent gamma variables of shape 2 and rate 1, so each has density x exp(-x) on x > 0. Define

\[
 X_N=\sum_{n=1}^N\frac{G_n}{n^2},\qquad X=\sum_{n=1}^\infty\frac{G_n}{n^2}.
\tag{1}
\]

These are ordinary sums of positive independent variables, not random models for primes or zero ordinates. Every rate n^2 is specified in advance. The expectation of X is finite, so the sum converges almost surely. Write f_N and f for their densities.

For q >= 0 the exact finite Laplace transform is

\[
 L_N(q)=\prod_{n=1}^N(1+q/n^2)^{-2}.
\tag{2}
\]

Adding one coordinate is convolution with a positive gamma density:

\[
 f_{N+1}=k_a*f_N,\qquad k_a(x)=a^2x e^{-ax}\mathbf1_{x>0},
 \qquad a=(N+1)^2.
\tag{3}
\]

Consequently

\[
 (\partial_x+a)^2f_{N+1}=a^2f_N \quad(x>0),
\tag{4}
\]

with the boundary conditions supplied by convolution. No signed coefficients are discarded in using an alternative partial-fraction expression.

### Exact finite formula

For 1 <= n <= N set

\[
 B_{n,N}=\left[\frac{2(N!)^2}{(N-n)!(N+n)!}\right]^2,
\quad
 c_{n,N}=1-2n^2\sum_{\substack{k\le N\\k\ne n}}\frac1{k^2-n^2}.
\tag{5}
\]

Then

\[
 f_N(x)=\sum_{n=1}^N B_{n,N}n^2
       (n^2x+c_{n,N}-1)e^{-n^2x}.
\tag{6}
\]

**Proof.** At the double pole q = -n^2, the coefficient of (q+n^2)^(-2) in (2) is n^4 B_{n,N}. Its simple-pole coefficient is -2 n^4 B_{n,N} times the sum in (5). Inverting these two elementary Laplace fractions gives (6). The closed factorial coefficient follows by multiplying k^2/(k^2-n^2); squaring removes its alternating sign. There is no polynomial part. Positivity comes from (3), not from positivity of the individual terms of (6).

The finite Mellin formula, initially justified by absolute integration for Re s > 0, is

\[
 \mathbb E X_N^s=\Gamma(s+1)\sum_{n=1}^N
                     B_{n,N}(s+c_{n,N})n^{-2s}.
\tag{7}
\]

The actual Mellin integral extends only to Re s > -2N; individual gamma factors in (7) have removable cancellations there. **The finite raw Mellin transform is not being called entire.** The entire approximants below are different objects.

## 2. Exact identification of the infinite source

The known representation in our scaling is

\[
 \mathbb E X^s=2\pi^s\xi(2s),\qquad
 \mathbb E\left(\sqrt{X/\pi}\right)^z=2\xi(z).
\tag{8}
\]

These are the Biane–Pitman–Yor identities [E1, Proposition 1], with their gamma-sum normalization converted explicitly. The following derivation also checks our density and Fourier conventions.

For fixed n, B_{n,N} tends to 4 and c_{n,N} tends to -1/2. Indeed

\[
 \sum_{\substack{k\le N\\k\ne n}}\frac1{k^2-n^2}
 =\frac3{4n^2}+\frac{H_{N-n}-H_{N+n}}{2n},
\quad
 c_{n,N}=-\tfrac12+n(H_{N+n}-H_{N-n}).
\tag{9}
\]

Also B_{n,N} <= 4 and |c_{n,N}| <= 1/2+2n^2, uniformly for n <= N. Formula (6) therefore converges locally uniformly on x > 0 to

\[
 f(x)=\sum_{n\ge1}(4n^4x-6n^2)e^{-n^2x}.
\tag{10}
\]

To identify this limit with the density of X, the elementary global majorant f_N(x) <= 4x exp(-x), proved in Section 4, permits dominated convergence. The density limit has integral one and agrees with the almost-sure distributional limit of (1).

Let theta(x) = sum over all integers n of exp(-n^2 x). Equation (10) is 2x theta''(x)+3 theta'(x). Differentiating the classical Jacobi transformation theta(x)=sqrt(pi/x) theta(pi^2/x) gives

\[
 f(\pi^2/x)=(x/\pi)^{5/2} f(x).
\tag{11}
\]

Large-x exponential decay and (11) give decay faster than every power at zero. Hence all complex moments exist. Termwise integration of (10), first for Re s > 1/2, gives

\[
 \mathbb E X^s=2(2s-1)\Gamma(s+1)\zeta(2s)=2\pi^s\xi(2s).
\]

Analytic continuation of the entire moment integral proves (8). This derivation uses the classical Jacobi identity and the usual entire normalization xi(0)=xi(1)=1/2; no assertion about nontrivial zero locations is used.

With Xi(z)=xi(1/2+iz), the correctly normalized full-line Fourier density is

\[
 \phi(t)=\pi e^{5t/2} f(\pi e^{2t}),\qquad
 \Xi(z)=\int_{\mathbb R}\phi(t)e^{izt}\,dt.
\tag{12}
\]

For example substitution x=pi exp(2t) makes the right side equal to one half of pi^(-s) E X^s at s=1/4+iz/2. Formula (8) gives exactly Xi(z), with no missing factor two. Equation (11) makes phi even.

## 3. Reciprocal projection: symmetry at every finite stage

Define, for real t,

\[
 h_N(t)=\sqrt{f_N(\pi e^{2t})f_N(\pi e^{-2t})},\quad
 Z_N=\int_{\mathbb R}h_N(t)\,dt,
\]
\[
 F_N(z)=\frac1{Z_N}\int_{\mathbb R}h_N(t)e^{izt}\,dt.
\tag{13}
\]

The square root is the positive real square root. We make no claim that h_N has a globally holomorphic continuation as a function of complex t. Instead its real-line decay makes F_N entire in the spectral variable z. Every F_N is even, real on the real axis, and satisfies F_N(0)=1.

At the infinite stage, (11) gives

\[
 h_\infty(t)=e^{5t/2}f(\pi e^{2t})=\phi(t)/\pi.
\tag{14}
\]

Thus the intended limiting function is exactly Xi(z)/Xi(0). This is not a fitted moment limit or an altered target selected to have real zeros.

### Why this projection, rather than an arbitrary symmetrization?

Let p_N(t) be the probability density proportional to e^(5t/2) f_N(pi exp(2t)). This is the one-half size-biased log-law of sqrt(X_N/pi). Among all even probability densities q with finite relative entropy, h_N/Z_N uniquely minimizes D(q || p_N).

**Proof.** Evenness permits replacing log p_N(t) inside its q-integral by [log p_N(t)+log p_N(-t)]/2. The geometric mean of p_N and its reflection is a positive constant times h_N. Consequently

\[
 D(q\Vert p_N)=D(q\Vert h_N/Z_N)-\log A_N,
 \qquad A_N=\int\sqrt{p_N(t)p_N(-t)}\,dt.
\tag{15}
\]

The second term is independent of q and the first is minimized uniquely at h_N/Z_N. That density has finite entropy relative to p_N, by the explicit finite density tails. This is the classical information-projection calculation, not a zero-preservation theorem.

This construction enforces the exact *reciprocal symmetry*. It does not preserve the complete Jacobi modular identity at finite N, or replace f_N by f. At the limit it becomes the identity on the original source. Mere evenness remains insufficient for real zeros.

## 4. Whole-strip convergence with an explicit error budget

**Proposed component theorem.** For each R >= 0 there is an explicit finite C_R, independent of N, such that

\[
 \sup_{|\operatorname{Im}z|\le R}
 \left|F_N(z)-\frac{\Xi(z)}{\Xi(0)}\right|
 \le C_R N^{-1/2}.
\tag{16}
\]

The supremum includes arbitrarily large real frequency. This is an *absolute* error, not a relative error near an exponentially small function or its zeros. Every density coordinate and the entire t tail are included.

### 4.1 Uniform density estimates

Write X_N=G_1+S_N. The full exponential tilt of the remainder is

\[
 \mathbb E e^{S_N}=\prod_{n=2}^N(1-n^{-2})^{-2}
                  =\left(\frac{2N}{N+1}\right)^2\le4.
\tag{17}
\]

The product is 1 when N=1. Conditioning on S_N in the convolution formula gives

\[
 0<f_N(x)\le4xe^{-x},\qquad
 |f_N'(x)|\le4(1+x)e^{-x},\qquad x>0.
\tag{18}
\]

For the derivative, differentiate (x-S) exp(-(x-S)) 1_(S<x). Its value at the moving endpoint is zero, so no omitted boundary atom occurs. Extend f_N by zero on x <= 0; this extension is absolutely continuous. The same density bound holds for f by passage to the limit.

Let R_N=X-X_N, independently of X_N. A second telescoping product and its logarithmic derivative give the **entire** tail budget

\[
 a_N:=\mathbb E[R_Ne^{R_N}]
 =\left(\frac{N+1}{N}\right)^2\left(\frac1N+\frac1{N+1}\right)
 =\frac{(N+1)(2N+1)}{N^3}\le\frac6N.
\tag{19}
\]

The derivative is legitimate because the moment generating function is finite in a neighborhood of 1. Using (18) on the interval between x-r and x gives, also when r>x,

\[
 |f_N(x-r)-f_N(x)|\le4r(1+x)e^{-x+r}.
\]

Condition on R_N and use f=f_N*law(R_N). Then

\[
 |f(x)-f_N(x)|\le4a_N(1+x)e^{-x}.
\tag{20}
\]

### 4.2 Reciprocal projection and both tails

Put x=pi exp(2t), y=pi exp(-2t), so xy=pi^2 and x+y=2pi cosh(2t). Equations (18) and (20), together with |sqrt(A)-sqrt(B)| <= sqrt(|A-B|) for nonnegative A,B, imply

\[
 h_N(t)\le4\pi e^{-\pi\cosh(2t)},
\tag{21}
\]
\[
 |h_N(t)-h_\infty(t)|
 \le4\sqrt{2\pi a_N(\cosh(2t)+\pi)}\,e^{-\pi\cosh(2t)}.
\tag{22}
\]

For clarity, the product difference is bounded by
16 a_N(x+y+2xy) exp(-(x+y)); taking its square root gives (22). There is no lower-density division or omitted small-x region in this estimate.

Define

\[
 A_R=4\sqrt{2\pi}\int_{\mathbb R}e^{R|t|}
           \sqrt{\cosh(2t)+\pi}\,e^{-\pi\cosh(2t)}dt,
\]
\[
 M_R=4\pi\int_{\mathbb R}e^{R|t|}e^{-\pi\cosh(2t)}dt.
\tag{23}
\]

Both are finite explicit one-dimensional integrals. Every polynomially weighted analogue is finite too. Equation (22) gives weighted L1 error at most A_R sqrt(a_N).

### 4.3 A uniform positive normalization, with no unknown small denominator

On |t| <= 1/10, elementary bounds 3<pi<22/7 and exp(1/5)<5/4 put both x and y in [12/5,4]. Further,

\[
 \mathbb E S_N=2\sum_{n=2}^N n^{-2}
 \le2\left(\tfrac14+\int_2^\infty u^{-2}du\right)=\tfrac32.
\]

Markov's inequality gives P(S_N <= 2) >= 1/4. On that event the first gamma density at x-S_N is at least (x-2) exp(-x), so f_N(x) >= exp(-4)/10. This also holds for the infinite remainder. Therefore

\[
 Z_N,Z_\infty\ge e^{-4}/50>1/4050=:b.
\tag{24}
\]

The last bound uses e<3. Both exponential inequalities used here follow directly from the positive series: exp(1/5)<sum_(k>=0)(1/5)^k=5/4, and e<1+1+sum_(k>=2)2^(-(k-1))=3. Dividing the Fourier transforms and retaining the normalizer error now gives (16) with, for example,

\[
 C_R=\sqrt6\,[A_R/b+M_R A_0/b^2].
\tag{25}
\]

Indeed |exp(izt)| <= exp(R|t|) throughout the full strip. This proves (16), not just convergence at finitely many moments or real points. The same reasoning with |t|^k proves uniform convergence of every fixed spectral derivative on each such strip.

The constants can also be made integral and completely explicit. Put m_R=ceil(R/2). On t>=0 substitute v=exp(2t), use cosh(2t)<=v, cosh(2t)>=v/2, and pi/2>1. Doubling the half-line integrals gives

\[
 A_R<28\,m_R!,\qquad M_R<16\,m_R!.
\]

For instance the remaining power in the first integral is v^((R-1)/2), bounded by v^(m_R), and the full integral against exp(-v) is m_R!. With sqrt(6)<3 and b=1/4050, (25) therefore permits

\[
 C_R\le22\,045\,300\,200\;\lceil R/2\rceil!.
\tag{25a}
\]

This constant is intentionally crude, not a practical numerical complexity claim. It proves absolute uniform convergence even on the growing full strips |Im z|<=alpha log N/log log N for any fixed 0<alpha<1: use m!<=m^m and compare its logarithm with (log N)/2. No lower bound for the target's modulus follows.

**Interpretation.** The approximation and complete-tail problem is solved for this proposed family. Spectral reality is not. Uniform *absolute* approximation cannot control zeros where the target itself is smaller than the error floor.

## 5. A genuinely real-zero starting point

For N=1, f_1(x)=x exp(-x), and

\[
 h_1(t)=\pi e^{-\pi\cosh(2t)},\qquad
 F_1(z)=\frac{K_{iz/2}(\pi)}{K_0(\pi)}.
\tag{26}
\]

The modified Bessel integral [E2, 10.32.9], after substituting 2t, gives the equality.

**Proposed component statement (classical mechanism). Every zero of F_1 is real.** Suppose K_(iz/2)(pi)=0 and let u(r)=K_(iz/2)(pi exp(r)), r >= 0. The modified Bessel equation [E3] gives

\[
 [-\partial_r^2+\pi^2e^{2r}]u=\frac{z^2}{4}u,
 \qquad u(0)=0.
\tag{27}
\]

The fixed-order large-argument expansion [E4] makes u and u' decay sufficiently fast at infinity for the Dirichlet energy identity. It is a nonzero function, since its leading asymptotic is nonzero. Thus

\[
 \frac{z^2}{4}\int_0^\infty |u|^2dr
 =\int_0^\infty (|u'|^2+\pi^2e^{2r}|u|^2)dr>0.
\tag{28}
\]

Consequently z^2 is positive real, which forces z real. No hypothetical xi zero was used to define this operator. This is a self-adjoint realization of the **first approximant**, not of xi and not a claim that the same differential operator realizes every later F_N.

## 6. Exact continuous update and the collision question

For a=(N+1)^2 and 0 <= u <= 1, use

\[
 X_{N,u}=X_N+uG/a.
\tag{29}
\]

It connects stages N and N+1 through positive laws. On 0<u<=1 its density satisfies

\[
 (a+u\partial_x)\partial_u f_{N,u}=-2\partial_x f_{N,u}.
\tag{30}
\]

This follows from L_(N,u)(q)=L_N(q)(1+uq/a)^(-2). Equivalently, with E_(a/u) the normalized rate-a/u exponential density,

\[
 \partial_u f_{N,u}=-\frac2u(f_{N,u}-E_{a/u}*f_{N,u}).
\tag{31}
\]

The boundary value f_(N,u)(0)=0 makes the Laplace/spatial conversion legitimate. Use (13) to define h_(N,u) and F_(N,u). At u=0 use the continuous limiting density, not the singular literal expression in (31).

For u>0 define the even score

\[
 S_{N,u}(t)=\tfrac12\left[
 \frac{\partial_u f_{N,u}(\pi e^{2t})}{f_{N,u}(\pi e^{2t})}
 +\frac{\partial_u f_{N,u}(\pi e^{-2t})}{f_{N,u}(\pi e^{-2t})}
 \right].
\tag{32}
\]

On compact subintervals of 0<u<=1 the finite exponential-polynomial density, its positive convolution interpretation, and its endpoint asymptotics justify differentiation of the Fourier integral. If q_(N,u)=h_(N,u)/Z_(N,u), then

\[
 \partial_u F_{N,u}(z)=\int e^{izt}
            [S_{N,u}(t)-\mathbb E_{q_{N,u}}S_{N,u}]q_{N,u}(t)dt.
\tag{33}
\]

A simple zero follows

\[
 z'(u)=-\frac{\partial_u F_{N,u}(z(u))}{\partial_zF_{N,u}(z(u))}.
\tag{34}
\]

At a real simple zero the numerator and denominator are real: its velocity stays real. Leaving the axis requires a multiple-zero collision, unless roots enter the region from its boundary. This is kinematics, **not a proof that collisions do not occur**. Any continuation argument must also count boundary entry; excluding interior double zeros alone is insufficient.

The arithmetic structure to exploit is the exact ordered rate sequence, the positive resolvent in (31), and the reciprocal pairing in (32). It is not a general assertion that positive convolution or geometric averaging preserves real zeros.

### 6.1 A concrete arithmetic tangent: spectral shifts into the safe half-plane

There is a useful exact calculation at the limiting reciprocal density. It is not yet a theorem controlling the full finite cascade. For epsilon >= 0 replace f(x) by f(x+epsilon), apply (13), and call the normalized transform Phi_epsilon. Multiplying f(x+epsilon) by the conditional-law normalizer has no effect on Phi_epsilon. Thus this can equally be defined from X-epsilon conditioned on X>epsilon. Put Phi=Phi_0=Xi/Xi(0).

Define the imaginary-step difference operator

\[
 (\mathcal A P)(z)=\frac{(2iz-1)P(z-2i)-(2iz+1)P(z+2i)}{8\pi}.
\tag{35a}
\]

Then the **right derivative at zero** is exactly

\[
 \left.\partial_\epsilon\Phi_\epsilon(z)\right|_{0+}
 =\mathcal A\Phi(z)-\Phi(z)\mathcal A\Phi(0)
 =\mathcal A\Phi(z)+\frac{\Phi(2i)}{4\pi}\Phi(z).
\tag{35b}
\]

**Proof.** Write h=h_infinity and r(x)=f'(x)/f(x). Differentiating the geometric mean at epsilon=0 gives h[r(x)+r(y)]/2. From h(t)=exp(5t/2)f(x), x=pi exp(2t), and evenness of h,

\[
 \frac h2[r(x)+r(y)]
 =-\frac{h'(t)\sinh(2t)}{2\pi}
  -\frac{5h(t)\cosh(2t)}{4\pi}.
\]

Integration by parts turns its Fourier transform into

\[
 -\frac1{4\pi}\int h(t)\cosh(2t)e^{izt}dt
 +\frac{iz}{2\pi}\int h(t)\sinh(2t)e^{izt}dt,
\]

which is (35a) applied to the unnormalized transform. Dividing by the normalizer gives (35b). All endpoint terms vanish. For the differentiability justification, (10),(11) give |r(x)| <= C(1+x^(-2)); the shifted geometric means, for 0<=epsilon<=1, are bounded by 4 sqrt((x+1)(y+1)) exp(-(x+y)/2). Their score derivatives therefore have an integrable double-exponential envelope on every spectral strip. Dominated differentiation is legitimate. QED.

For real z, the shifted value Phi(z-2i) is xi(5/2+iz)/xi(1/2), in an absolutely convergent Euler half-plane. The other shifted value is its conjugate by the functional equation. Thus the leading *translation model* of tail removal has a closed, explicitly arithmetic spectral expression, rather than an unspecified metric correction. The omitted gamma tail has mean 2 sum_(n>N)n^(-2), but replacing that random tail by its mean is not an exact operation. An error-controlled expansion transferring (35b) to the actual nonlinear cascade remains to be derived. No zero-preservation property of the difference operator is assumed.

## 7. Stress-test and the necessary change of target

The first working conjecture was that every F_N might have only real zeros. It is not a safe foundation.

Two different high-precision quadrature grids give an apparent zero of the actual N=4 approximant near

\[
 28.0555855384091825810+2.6219979332686197955\,i.
\tag{35}
\]

One uses a single 160-node Gauss–Legendre rule on [0,3]; the other uses 12 subintervals with 32 nodes each. Their located roots agree to over 45 decimal places in the recorded run. The source is (6),(13), not a zeta or gamma-function oracle. The same mpmath arithmetic backend is used in both. **No outward quadrature/error enclosure or Rouche certificate is supplied, so this is exploratory evidence, not a certified nonreal zero.** It is evidence about F_4, not zeta.

The finite partial-fraction sum suffers cancellation near x=0; the scout explicitly stops if it loses numerical positivity. The common omitted tail beyond t=3 has the analytic envelope (21), but the scout has not assembled all primitive, quadrature and root-count errors into an accepting interval computation.

This stress-test motivates a weaker and more useful target: finite approximants may have spurious zeros, but no fixed nonreal zero may survive the cascade. We do not extrapolate that assertion from the following real-root scout:

| N | one tracked first real root |
|---|---|
| 1 | 11.871335044628 |
| 2 | 12.735695079348 |
| 4 | 13.368029185045 |
| 8 | 13.719730963351 |
| 16 | 13.913437349342 |

These are non-certified root tracks, not complete zero censuses. An apparent negative higher Hankel determinant in early scouting is likewise not promoted to a theorem and is not used by this packet.

## 8. The end-to-end completion theorem and the open task

**Conditional completion theorem.** Suppose there are integers N_j -> infinity, real T_j -> infinity and epsilon_j -> 0 such that every zero of F_(N_j) in

\[
 |\operatorname{Re}z|\le T_j,\qquad |\operatorname{Im}z|\le1
\tag{36}
\]

lies in |Im z| <= epsilon_j. Then RH follows.

**Proof.** A nonreal zero z_0 of Xi has 0<|Im z_0|<1/2 by the classical zeta strip and coordinate change. Choose a small closed disk around z_0 lying strictly off the real axis and within |Im z|<1, with zero-free boundary. It contains at least one zero, with its full multiplicity. By (16), F_(N_j) converges uniformly on that disk boundary. Rouche gives the same positive number of zeros in the disk for large j. But the disk eventually lies inside (36) and outside |Im z| <= epsilon_j, a contradiction. No simplicity assumption is made. QED.

A theorem with a prescribed scale such as T_N = c log N (some fixed c>0) and an explicit shrinking epsilon_N would suffice. **No such rate or zero-confinement theorem has been proved here.** The logarithmic scale is a starting research target suggested by an algebraic absolute approximation error competing with an exponentially small real-frequency transform; it is not an established frontier or a complexity guarantee.

The target is deliberately weaker than global real-rootedness of every approximant. The apparent root (35) does not refute it. It also avoids asserting simplicity of every xi zero, a bounded positive metric for the old nonnormal operator, or an all-rank ferromagnetic moment realization.

### First substantive attack, rather than another fit

Use the differential/resolvent law (30)–(33) to study the birth and motion of conjugate zero pairs. A useful initial deliverable is a *certified* parameter-continuation calculation on the first two cascade steps, including all zeros in its stated rectangle, double-zero tests, and boundary winding counts. In parallel, seek an analytic inequality for the reciprocal score that prevents pair creation in a scale-dependent rectangle, or forces every nonreal pair outside it. The certificate's purpose is to falsify or sharpen a candidate score inequality, not to extrapolate RH from a finite picture.

The source-specific theorem must involve the actual square-rate cascade. A theorem for arbitrary positive even densities or arbitrary gamma rates would need separate justification and would probably be too broad. The complete Jacobi reciprocity is recovered only at infinity; finite evenness alone does not pay for zero confinement.

## 9. Relationship to the current project

This proposal differs from the bounded-metric route of #834/#839/#841: it does not try to change the norm of the existing xi operator. It differs from #842's new finite ferromagnetic realization: it approximates the *whole exact source*, at a proved full-strip rate, instead of solving finitely many inverse moment equations and leaving their compatible all-order realization to be constructed.

It complements those programmes without importing their proposed conclusions. The latest six PR descriptions received orientation reading, not a new principal-proof audit. A closing read found #842 had advanced to a connected/collective-limit continuation; it remains metadata-only context here. Although the auxiliary gamma variables in (1) are independent, the reciprocal projection of their log-sum is not a convolution decomposition of the final theta Fourier law into independent spin blocks. The previous local trace/Hankel packet motivates avoiding another generic positivity promotion, but none of its new positivity assertions is a theorem dependency here.

The positive start, exact convolution recurrence, reciprocal variational projection, original source limit and whole-strip error form the proposed reusable foundation. **The missing spectral-confinement inequality is genuine research, not an omitted technical check.** No integration, canonical acceptance or full RH proof is asserted.

## References and attribution

[E1] P. Biane, J. Pitman and M. Yor, *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions*, Berkeley technical report 569, arXiv:math/9912170. Proposition 1 and Section 5 were inspected, including PDF page images for printed pages 7 and 28. The gamma-sum representation, Mellin/xi identity, size-bias reciprocity and existing finite Mellin-approximation literature are credited here. This was not an exhaustive re-review of the paper.
https://statistics.berkeley.edu/sites/default/files/tech-reports/569.pdf
https://arxiv.org/abs/math/9912170

[E2] NIST DLMF 10.32.9, integral representation of K_nu.
https://dlmf.nist.gov/10.32

[E3] NIST DLMF 10.25.1, modified Bessel equation.
https://dlmf.nist.gov/10.25

[E4] NIST DLMF 10.40.2 and 10.40.4, fixed-order large-argument K and derivative asymptotics. Used only for the endpoint/domain justification in the seed energy identity.
https://dlmf.nist.gov/10.40

Classical gamma convolution, Jacobi transformation, relative entropy, dominated convergence and Rouche theory are imported standard tools. Their applications above are explicitly derived. A default-branch repository search for “Biane” returned no matches; that does not establish absence from other branches or originality in the literature.
