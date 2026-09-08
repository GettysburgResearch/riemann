# Harmonic endpoint transfer and an exact-horizon scalar test

Status: proposed component proofs, requiring independent mathematical review.
**RH, the original uniform block gain, and every new subpower bound below
remain unproved.** This is a research continuation, not an acceptance report.
Parent: PR #805, `acb0a25a373b427c9694aff78cba396f26963e8b`.

There are two distinct results. Sections 1–2 act on the parent's UNCHANGED
balanced source: they replace its full norm by a finite harmonic-step norm,
up to explicit logarithmic errors. Sections 3–7 introduce a DIFFERENT,
terminal-balanced source. For this source, a single rational scalar on a
predetermined fourth-power grid is RH-equivalent. Neither construction
establishes the required cancellation. The second source is an odd/parity
version of classical natural Nyman–Beurling approximants, not a claimed new
approximation principle; see SOURCES.md.

## 0. Fixed conventions and imported parent identities

Let H be the real step-function Hilbert space, zero below 1, with

\[
 \|f\|_H^2=\sum_{n\ge1}\frac{f(n)^2}{n(n+1)},\qquad
 h_k(n)=\{n/k\},\quad h_1=0,\quad\chi(n)=1.
\]

For a finite real source lambda on odd k<=M, satisfying sum lambda_k/k=0,
put F[lambda]=sum lambda_k(h_{2k}-h_k), E[lambda]=||F[lambda]||_H^2,
and B[lambda]=sum |lambda_k|/k. The parent proves, for 0<x<1/2,

\[
 C_\lambda(\tan\pi x)=\sum_{k\text{ odd}}\frac{\lambda_k}{k}
 \sum_{\substack{1\le r<k/2\\r\ge kx}}(-1)^{r+1}\cot(\pi r/k),
 \qquad E[\lambda]=\frac\pi2\int_0^\infty C_\lambda(t)^2dt.       \tag{0.1}
\]

The current is finite and constant between the predetermined breakpoints
 tan(pi r/q), where q<=M is odd and r/q is reduced in (0,1/2). All source
cross terms are retained. The parent also proves, for every tau>0,

\[
 \frac\pi2\int_\tau^\infty C_\lambda(t)^2dt
 \le\frac{\pi B[\lambda]^2}{2\tau}.                         \tag{0.2}
\]

The elementary derivation of (0.2) is worth recalling: for each k the inner
sum in (0.1) is a consecutive alternating sum of decreasing positive terms,
so its magnitude is at most cot(pi x). These are the only analytic Green
identities imported from the parent. Its proof and numerical remainder note
are source-locked. No conclusion-facing parent open gate is assumed.

## 1. TE26.1 — uniform harmonic replacement, with the endpoint retained

For u>=0 define

\[
 h(u)=\log2-\sum_{1\le r<u}\frac{(-1)^{r+1}}r.
\]

Equivalently h(u) is the alternating harmonic tail starting at max(1,ceil u),
with the displayed convention at integers. Its values on countably many
endpoints will not affect any norm. For every odd positive k and 0<x<1/2,

\[
 \left|\frac\pi k\sum_{\substack{1\le r<k/2\\r\ge kx}}
 (-1)^{r+1}\cot(\pi r/k)-h(kx)\right|\le\frac4k.             \tag{1.1}
\]

Proof. Write K=(k-1)/2, R=max(1,ceil(kx)). If 1<=R<=K, subtract the
alternating sums term by term. The function

\[
 b(r)=\frac1{\pi r}-\frac1k\cot(\pi r/k)
\]

is positive and increasing for 0<r<k/2, because sin v<v implies
csc(v)^2-v^{-2}>0. Its maximum is less than 2/(pi k). A consecutive
alternating sum of increasing positive terms has magnitude at most its last
term. The omitted harmonic tail beyond K has magnitude at most 1/(K+1),
which after division by pi is at most 2/(pi k). Add the two bounds.
If R=K+1 the cotangent sum is empty and the harmonic-tail bound suffices.
For k=1 the assertion follows from log2<1<4. End of proof.

Define the finite harmonic source and its energy by

\[
 W_\lambda(x)=\sum_k\lambda_k h(kx),\qquad
 \mathcal H[\lambda]=\int_0^{1/4}W_\lambda(x)^2dx.
\]

Then (1.1) gives the uniform, all-source estimate

\[
 |\pi C_\lambda(\tan\pi x)-W_\lambda(x)|\le4B[\lambda].     \tag{1.2}
\]

In particular the dangerous endpoint x=0 has NOT been removed. No estimate
of a signed Mobius sum occurs in this argument.

## 2. TE26.2 — full-norm transfer and finite rational computation

For every finite balanced odd source,

\[
 \boxed{\sqrt{E[\lambda]}\le\sqrt{\mathcal H[\lambda]}+4B[\lambda],
 \quad\sqrt{\mathcal H[\lambda]}\le\sqrt{2E[\lambda]}+2B[\lambda].} \tag{2.1}
\]

Proof. Put G(x)=pi C_lambda(tan pi x) on (0,1/4). Equation (1.2) implies
||G-W||_2<=2B. The energy below t=1 is

\[
 E_{<1}=\frac12\int_0^{1/4}G(x)^2\sec^2(\pi x)dx,
 \qquad\tfrac12\|G\|_2^2\le E_{<1}\le\|G\|_2^2.
\]

Use (0.2) at tau=1, the triangle inequality and 2+sqrt(pi/2)<4 to obtain
both bounds. End of proof.

Thus E<=2 H+32 B^2 and H<=4 E+8 B^2. In any specified family for which
B=M^{o(1)}, subpower growth of the full original norm squared is equivalent
to subpower growth of H. This applies to the unchanged rational optimum of
the parent, for which it proves B<38+log M. Neither subpower estimate follows
from (2.1).

There is a simpler exact evaluator. Let T=sum lambda_k and form the finite
mesh consisting of 0, 1/4, and all r/k strictly between them. On each open
mesh interval I, put

\[
 v_I=\sum_k\lambda_k\sum_{1\le r<kx}\frac{(-1)^{r+1}}r\quad(x\in I).
\]

Then

\[
 \boxed{\mathcal H[\lambda]=a(\log2)^2+b\log2+c,\quad
 a=T^2/4,\ b=-2T\sum_I |I|v_I,\ c=\sum_I |I|v_I^2.}        \tag{2.2}
\]

All three coefficients are rational when lambda is rational. This is the
complete harmonic energy, not a quadrature or truncated infinite sum. The
full Green energy is generally not equal to H: (2.1) is a norm comparison.
For M>=5, its first interval has energy exactly (log2)^2 T^2/M.

## 3. TE26.3 — a unique terminal-balanced source with an exact horizon

For real x>=1 let

\[
 M_o(x)=\sum_{n\le x,\ n\text{ odd}}\mu(n),\quad
 m_o(x)=\sum_{n\le x,\ n\text{ odd}}\frac{\mu(n)}n,\quad
 Q(x)=M_o(x)-x m_o(x).
\]

For every ODD integer M>=3, define the new coefficients

\[
 \boxed{\lambda^{\rm term}_{k,M}=\mu(k)-M m_o(M)\mathbf1_{k=M}
 \quad(1\le k\le M,\ k\text{ odd}).}                        \tag{3.1}
\]

These are rational, lambda_1=1, and sum lambda_k/k=0 exactly. Their sum
is Q(M). The terminal coefficient is retained even when M is nonsquarefree.
Let F_M=F[lambda^term], E_M=||F_M||_H^2. Then

\[
 \boxed{F_M(n)=1\quad(1\le n<M).}                          \tag{3.2}
\]

Proof. Balance turns F into sum lambda_k(floor(n/k)-floor(n/(2k))). Its
jumps at odd integers m are sum_{k|m}lambda_k and its even jumps vanish.
Below M, finite Mobius inversion makes the odd jumps 1 at m=1 and zero
thereafter. The correction at k=M has not yet entered. End of proof.

In fact (3.1) is the UNIQUE balanced source on these odd indices with
(3.2): odd jumps successively force lambda_k=mu(k) for k<M, and balance
then fixes lambda_M. This is uniqueness within the indicated source class,
not an optimality assertion about the full Gram minimization.

For all real t>=1, with the step-function convention on F_M, the exact
continuation is

\[
 F_M(t)=1+\bigl(\lfloor t/M\rfloor-\lfloor t/(2M)\rfloor\bigr)Q(M)
       -\sum_{\substack{j\le t/M\\j\text{ odd}}}M_o(t/j).  \tag{3.3}
\]

To prove this, extend the Mobius source through t, obtaining 1 by odd divisor
inversion, then subtract all omitted k>M and the terminal correction. Swap
the two finite sums. In particular, on M<=t<3M, F_M(t)=1+Q(M)-M_o(t).
No assertion that this tail is small is made.

The elementary divisor identity sum_{n<=N}mu(n)floor(N/n)=1 gives
|sum_{n<=N}mu(n)/n|<=1. Its exact 2-adic inversion gives |m_o(x)|<=2.
Consequently

\[
 B[\lambda^{\rm term}]\le3+\log M,\qquad
 \sum_k|\lambda^{\rm term}_k|/k^2\le\pi^2/8+2/M<2.          \tag{3.4}
\]

An unconditional bound, not a power saving, is E_M<128M. Indeed in
L^2((0,infinity),dt/t^2), put e(t)={t}; ||e||<=sqrt2 and ||D_k||=k^{-1/2}.
Balance gives F_M=(D_2-I)[sum_{k<=M,odd}mu(k)D_ke-M m_o(M)D_Me]. Apply
the triangle inequality, sum_{k<=M}k^{-1/2}<=2sqrt M, and |m_o|<=2.
Also E_M>=1-1/M by (3.2).

## 4. TE26.4 — the first Green interval is a single rational scalar

Let J_M be the contribution from 0<t<tan(pi/M) to the exact parent Green
energy for the NEW terminal source. No reduced frequency occurs before
1/M, so its current is constant there, even if a zero charge is retained.
Set R_M=Q(M)^2/M, a nonnegative rational number.

The parent proves the following elementary cotangent remainder, with k odd:

\[
 \sum_{1\le r<k/2}(-1)^{r+1}\cot(\pi r/k)
 =\frac{k\log2}{\pi}-\epsilon_k,\qquad
 0<\epsilon_k<\frac\pi{12k}.
\]

It follows from the positive integral
 epsilon_k=pi^{-1} integral_0^infinity tanh(v/(2k))/(exp(v)-1)dv.
Together with (3.4), this gives

\[
 C_M(0)=\frac{\log2}{\pi}Q(M)+r_M,\qquad |r_M|<1.
\]

Since pi/M<=tan(pi/M)<=2pi/M for odd M>=3, we obtain

\[
 \boxed{\frac{R_M}{16}-\frac8M\le J_M\le2R_M+\frac{32}M.} \tag{4.1}
\]

For the lower bound use (a+b)^2>=a^2/2-b^2, log2>1/2 and pi^2<16.
For the upper bound use (a+b)^2<=2a^2+2b^2, log2<1, and pi^2<16.
A negative lower bound is harmless. The exact first harmonic energy, if
integrated to 1/M, is (log2)^2 R_M. For M>=5 this entire first interval
lies inside the harmonic norm of section 2.

Thus subpower J_M is equivalent to subpower R_M, with no uncomputed mesh or
analytic remainder in R_M. This comparison alone does not estimate R_M.

## 5. TE26.5 — no zero can cancel from the scalar transform

We have the exact continuous identity

\[
 Q(x)=-\int_1^x m_o(u)du
     =-\sum_{k\le x,\ k\text{ odd}}\frac{\mu(k)}k(x-k).    \tag{5.1}
\]

The summands vanish at their entry point, so Q is continuous and piecewise
linear. Partial summation also gives Q(x)=-x integral_1^x M_o(t)/t^2 dt.
This is the odd-index version of the classical integrated Mertens statistic
called x*gamma(x) in Baez-Duarte [BD00], equations (1.6)–(1.8), with a minus
sign. The smoothing and pole criterion are not new general principles.
For Re s>1, absolute convergence justifies

\[
 \boxed{\int_1^\infty Q(x)x^{-s-1}dx
 =-\frac1{s(s-1)(1-2^{-s})\zeta(s)}.}                     \tag{5.2}
\]

Indeed each summand contributes -mu(k)k^{-s}/[s(s-1)], and the odd reciprocal
Euler product is 1/[(1-2^{-s})zeta(s)]. The singularity at s=1 is removable,
because 1/zeta has a simple zero there. At EVERY nontrivial zero rho of
zeta, the right side has a nonremovable pole of the same multiplicity:
rho, rho-1, and 1-2^{-rho} are nonzero, and the numerator is -1.

Therefore, if Q(x)=O(x^sigma), with 1/2<=sigma<1, zeta has no zero with
real part greater than sigma. The left integral converges locally uniformly
there and defines a holomorphic function. Apply the identity theorem to
s(s-1)(1-2^{-s})zeta(s) times that function; it cannot equal -1 at a zero.
This is an implication from an UNPROVED arithmetic bound.

We separately import the classical Littlewood implication RH =>
M(x)=O_epsilon(x^{1/2+epsilon}), for every epsilon>0. Odd 2-adic inversion
and partial summation then give, for 0<epsilon<1/2,

\[
 M_o(x)=O_\epsilon(x^{1/2+\epsilon}),\quad
 m_o(x)=O_\epsilon(x^{-1/2+\epsilon}),\quad
 Q(x)=O_\epsilon(x^{1/2+\epsilon}).                         \tag{5.3}
\]

For the second assertion, convergence of sum mu_o(n)/n follows from the
first; its value is zero by Abel's theorem and the reciprocal Euler product
as s decreases to 1. Integrating the tail proves the stated rate. Thus
RH is equivalent to R_M=M^{o(1)} on all odd M, and by (4.1) to the same
statement for this first Green interval. The reverse implication is the
classical conditional input just stated, not an unconditional Mertens bound.

## 6. TE26.6 — an explicit sparse fourth-power grid suffices

This replaces 'all odd M' by a PREDETERMINED grid, not a cherry-picked
subsequence. Let M_j=2j^4+1, j>=1. Then

\[
 \boxed{\mathrm{RH}\ \Longleftrightarrow\
 \forall\epsilon>0\ \exists C_\epsilon:\quad
 R_{M_j}\le C_\epsilon M_j^\epsilon\quad\text{for all }j.}   \tag{6.1}
\]

The same statement holds with J_{M_j}. Here finitely many initial terms
can equivalently be excluded; a finite successful test is not sufficient.

Proof of the sampling step. On any interval [a,b] with odd integer endpoints,
let ell be linear interpolation of Q(a),Q(b). The exact Dirichlet Green
identity is

\[
 Q(x)-\ell(x)=\sum_{\substack{a<k<b\\k\text{ odd}}}\frac{\mu(k)}k
 \frac{(\min(x,k)-a)(b-\max(x,k))}{b-a}.                  \tag{6.2}
\]

Both sides vanish at the endpoints and have the same distributional second
derivative. This can alternatively be checked one hinge function at a time
in (5.1). Each Green factor is at most (b-a)/4; there are at most (b-a)/2
odd interior points and k>=a. Hence

\[
 |Q(x)-\ell(x)|\le\frac{(b-a)^2}{8a}.                    \tag{6.3}
\]

For a=M_j and b=M_{j+1}, b/a<=16 and b-a<=30j^3, while a>=2j^4. Thus

\[
 |Q(x)|\le\max(|Q(M_j)|,|Q(M_{j+1})|)+60\sqrt x.           \tag{6.4}
\]

If R on the grid is O(M^eta), for some 0<=eta<1, (6.4) proves
Q(x)=O(x^{(1+eta)/2}) on the entire half-line. Equation (5.2) then excludes
zeros in Re s>(1+eta)/2. Taking all eta>0 proves the forward implication
in (6.1); (5.3) proves the converse. The grid contains O(X^{1/4}) nodes up
to X. No density-one, random-sampling, or arbitrary-subsequence theorem is
being substituted for this explicit interpolation bound. End of proof.

In particular a hypothetical zero beta>1/2 forces

\[
 \limsup_{j\to\infty}\frac{\log(1+R_{M_j})}{\log M_j}
 \ge2\beta-1,
\]

and the same lower limsup holds for J on the grid. This is a LIMSUP claim;
small values on an arbitrary subsequence would not contradict it.

## 7. TE26.7 — full energy detects every bad zero with the stronger horizon rate

For the finite polynomial P_M(s)=sum lambda^term_k k^{-s}, balance yields
P_M(1)=0. Finite Mellin transformation gives

\[
 \int_1^\infty F_M(t)t^{-s-1}dt
 =\frac{(1-2^{-s})\zeta(s)P_M(s)}s\quad(\Re s>0).          \tag{7.1}
\]

Initially prove this to the right of 1 from the floor formula. Both sides
are holomorphic in Re s>0, with the pole at 1 removed; F_M is bounded and
periodic. This proves the stated continuation.

If zeta(rho)=0, beta=Re rho>1/2, the exact horizon gives
 integral_1^M F_M(t)t^{-rho-1}dt=(1-M^{-rho})/rho. The full integral is
zero, so its tail has magnitude at least 1/(2|rho|) for large M. Applying
Cauchy–Schwarz with the ORIGINAL t^{-2} norm gives

\[
 \boxed{E_M\ge1-1/M+\frac{2\beta-1}{4|\rho|^2}M^{2\beta-1}
 \quad\text{for all sufficiently large odd }M.}           \tag{7.2}
\]

Thus the full-energy lower LIMINF exponent is at least 2beta-1. This is
stronger than the earlier approximate-horizon rate for the different
constrained optimizer. It is not a claim that terminal balancing gives a
smaller finite energy. No simplicity or zero-height information is assumed.

## 8. Attempted closure: what is actually left

The harmonic replacement closes the trigonometric/Green transfer with
explicit norm errors, and the terminal source closes all source balance and
horizon conditions exactly. The scalar transform (5.2) has no cancellation
loophole, and the fourth-power sampling theorem closes the gap between a
specified sparse grid and the full range.

The remaining estimate can now be written with rational arithmetic alone:

\[
 \boxed{\forall\epsilon>0\ \exists C_\epsilon\ \forall j\ge1:\quad
 \frac1{2j^4+1}\left[
 \sum_{\substack{k\le2j^4+1\\k\text{ odd}}}
 \mu(k)\left(1-\frac{2j^4+1}{k}\right)\right]^2
 \le C_\epsilon(2j^4+1)^\epsilon.}                         \tag{TE26.OPEN}
\]

TE26.OPEN has NOT been proved. It is a smoothed Mobius estimate of RH
strength, not an evaluated constant, a finite-coverage problem, or a new
unconditional zero-free strip. The literal relation

\[
 \sum_{d\le x,\ d\text{ odd}}Q(x/d)=1-x
\]

follows by finite divisor inversion. Trying to estimate this renewal
identity after absolute values loses the signed cancellation: the sum of
weights d^{-sigma} diverges for sigma<1. It supplies no contractive bound at
sigma=1/2. The elementary |m_o|<=2 gives only Q(x)=O(x), consistent with
E_M<128M; this falls far short of TE26.OPEN. Classical prime-number estimates
can give subexponential savings relative to x, but not the required fixed
power saving. No such savings are counted as a proof here.

Nor can one bound a generic full energy by its first harmonic interval.
The exact balanced source (lambda_1,lambda_3,lambda_5)=(1,-6,5) has T=0,
so that interval vanishes, but F(1)=F(2)=1 and E>=2/3. The scalar criterion
works only for the specified terminal Mobius family and its all-scale
transform, not for every balanced source or for the parent's different
optimizer. Its nonsquarefree terminal coefficient cannot be dropped.

The natural-approximant literature already warns that exact local agreement
does not prove L2 convergence. We make no strong-convergence assertion for
F_M, and no claim that it solves the original optimal block-gain inequality.
The new packet supplies component proofs and bounded checks, not an RH proof.
