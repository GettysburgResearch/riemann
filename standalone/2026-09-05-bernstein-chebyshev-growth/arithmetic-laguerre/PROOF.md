# Exact pole subtraction and the Laguerre-weighted prime discrepancy

Status: PROPOSED analytic proofs; independent mathematical review required.
The requested subexponential inequality is NOT proved.
Scope: the actual completed Riemann xi function, the original scale v=2,
every integer degree N>=1; separately labelled continuous source controls.
Exact dependency: PR #792 at 81e336a6d62d0963216ae05f809ec4df05447eb8,
`standalone/2026-09-05-bernstein-chebyshev-growth/GROWTH.md`.
What was run: the finite rational checker documented in VALIDATION.md.
Smallest remaining gap: the signed middle-range estimate in Section 6.
Local labels AL-1 through AL-7 are scoped to this directory only.

## 1. Preserve the original observable; linearize its arithmetic source

Keep the parent's normalization

\[
 F(u)=\xi\!\left(\frac12+\sqrt{u+\frac14}\right),\quad
 h=F'/F,\quad
 m_n(v)=\frac{(-1)^n v^{n+1}}{n!}h^{(n)}(v),\quad
 c_N(v)=L_v[T_N(2t-1)],\quad L_v(t^n)=m_n(v).
\]

We choose the ONE fixed scale v=2, which is allowed by the parent's theorem.
Nothing below chooses a scale from an unknown zero. Set

\[
 G(q)=F(q-1/4)=\xi(1/2+\sqrt q),\quad b=9/4,\quad \lambda=8/9,
\]

and define auxiliary moments and traces

\[
 \widetilde m_n=\frac{(-1)^n b^{n+1}}{n!}(G'/G)^{(n)}(b),\quad
 \widetilde L(t^n)=\widetilde m_n,\quad
 d_N=\widetilde L[T_N(2t-1)].                                      \tag{1}
\]

These are source derivatives, not an assumed positive measure. Translation
immediately gives

\[
 m_n(2)=\lambda^{n+1}\widetilde m_n.                               \tag{2}
\]

**AL-1 (polynomial-cost return to the original coordinate).** Expand

\[
 T_N(\lambda x+\lambda-1)=\sum_{j=0}^N\alpha_{N,j}T_j(x).
\]

Then

\[
 c_N(2)=\lambda\sum_{j=0}^N\alpha_{N,j}d_j,\qquad
 |\alpha_{N,0}|\le1,\quad |\alpha_{N,j}|\le2\ (j\ge1),
\]
\[
 |c_N(2)|\le\frac89\sqrt{2N+1}\max_{0\le j\le N}|d_j|.                 \tag{3}
\]

Proof. Equation (2) implies
`L_2[P(t)]=lambda * tildeL[P(lambda*t)]` for every polynomial. Apply it
to `P=T_N(2t-1)`. For x in [-1,1], the argument lambda*x+lambda-1 lies
in [-1,1]. Hence the expanded polynomial has absolute value at most one.
Chebyshev orthogonality, equivalently cosine Fourier coefficients, bounds
the constant coefficient by one and each other coefficient by two. Parseval
also gives `alpha_(N,0)^2+(1/2)sum_{j>=1}alpha_(N,j)^2<=1`. Weighted
Cauchy--Schwarz yields `sum_j |alpha_(N,j)|<=sqrt(2N+1)`, proving (3). This argument is valid for every degree, not just the replay.

In particular subexponential d_N implies the requested subexponential
c_N(2): apply a bound with epsilon/2 and absorb the polynomial in (3).
This change of coordinate is not declared free; (2)--(3) pay for it.

The parent's generating-function algebra, which is a local Taylor identity
and does not require its spectral representation, gives

\[
 D(w):=\sum_{N\ge0}d_Nw^N
  =\frac{d_0}{2}+\frac38\frac{\xi'}{\xi}\!\left(\frac{2-w}{1+w}\right),
 \qquad d_0=\frac34\frac{\xi'(2)}{\xi(2)}.                       \tag{4}
\]

Indeed, let t=(1-w)/(1+w). The parent formula for G at b contains
`b*t/2 * (G'/G)(b*t^2)`. Since
`G'/G(q)=(xi'/xi)(1/2+sqrt(q))/(2sqrt(q))`, this becomes
`sqrt(b)/4 * (xi'/xi)(1/2+sqrt(b)*t)`, proving (4) near zero.
The factor 3/8 is essential.

The map s(w)=(2-w)/(1+w) sends |w|<1 bijectively onto Re(s)>1/2.
Therefore (4), the nonzero residues of the logarithmic derivative at zeros,
and xi(s)=xi(1-s) show, without a zero census,

\[
 d_N=e^{o(N)}\ \text{in the all-epsilon upper-bound sense}
 \quad\Longleftrightarrow\quad\mathrm{RH}.                      \tag{5}
\]

Here and below this notation means `for every epsilon>0 there is C_epsilon
such that |d_N|<=C_epsilon exp(epsilon*N)`; it does not assert a pointwise
asymptotic equivalent or positivity. For the forward implication the Taylor
series is analytic on the disk; a zero of xi in the image would give a
nonremovable pole there. For the reverse implication Cauchy's estimate on
every fixed smaller disk suffices. Boundary zeros cause no difficulty.
This equivalence is a conditional endpoint, not the missing estimate.

## 2. Subtract the zeta pole exactly, before estimating any prime sum

Write Lambda for the von Mangoldt function and define, for N>=1,

\[
 L_N^{(-1)}(x)=\sum_{j=1}^N(-1)^j\binom{N-1}{j-1}\frac{x^j}{j!},
\]
\[
 P_N=\sum_{n\ge2}\frac{\Lambda(n)}{n^2}L_N^{(-1)}(3\log n),
\qquad
 I_N=\int_1^\infty x^{-2}L_N^{(-1)}(3\log x)\,dx,
\]
\[
 E_N=P_N-I_N.                                                   \tag{6}
\]

Each series is absolutely convergent at its fixed finite N, since the
Laguerre polynomial has finite degree and Lambda(n)<=log(n). This is not
a uniform-in-degree summability assertion.

**AL-2 (literal prime-pole identity).**

\[
 I_N=(-1)^N3\,2^{N-1}.                                         \tag{7}
\]

Proof. Substitute y=log(x); then integrate each y^j against exp(-y).
The result is
`sum_{j=1}^N (-3)^j binom(N-1,j-1)=-3(1-3)^(N-1)`.
No prime number theorem is used in this identity.

On |w|<1/2, Re(s(w))>1, so the Euler product gives the actual absolutely
convergent logarithmic-derivative series. The Laguerre generating identity
at parameter -1 gives

\[
 n^{-s(w)}=n^{-2}\exp\!\left(\frac{3\log(n)w}{1+w}\right)
 =n^{-2}\sum_{N\ge0}(-1)^NL_N^{(-1)}(3\log n)w^N.               \tag{8}
\]

Uniform convergence of the prime series on every compact subset of that
disk justifies Taylor coefficient extraction. Equivalently, differentiate
finitely many times and dominate by `log(n)^(N+1)/n^sigma`, sigma>1.
Also

\[
 \frac1{s(w)-1}=\frac{1+w}{1-2w},\qquad
 [w^N]\frac1{s(w)-1}=3\,2^{N-1}\quad(N\ge1).                   \tag{9}
\]

Thus E_N subtracts the entire exponential contribution of the pole at s=1.
Discarding its sign before subtraction would destroy the essential
cancellation. The n variable in (6) includes ALL prime powers, not just
primes. Constants and the degree-zero coefficient are not hidden in (7).

## 3. Complete all archimedean coefficients, with an explicit error bound

The completion formula is

\[
 \frac{\xi'}{\xi}(s)=\frac1{s-1}
  +\left[\frac1s-\frac12\log\pi+\frac12\psi_\Gamma(s/2)\right]
  -\sum_{n\ge2}\frac{\Lambda(n)}{n^s},                          \tag{10}
\]

where psi_Gamma is the digamma function, not the prime-counting function.
Put

\[
 S_N=\sum_{\ell=2}^\infty\frac1{\ell^2}
                  \left(1-\frac3{2\ell}\right)^{N-1}>0.
\]

**AL-3 (exact decomposition and bounded archimedean term).** For all N>=1,

\[
 \boxed{d_N=(-1)^N\left(\frac9{32}S_N-\frac38 E_N\right).}       \tag{11}
\]

In particular the entire archimedean coefficient A_N=(-1)^N(9/32)S_N obeys

\[
 |A_N|\le\frac9{32}\left(\frac{\pi^2}{6}-1\right).
\]

For N>=2 there is the sharper explicit estimate

\[
 \boxed{
 \left|A_N-(-1)^N\frac3{16N}(1-4^{-N})\right|
 \le\frac1{(N+1)^2}.}                                         \tag{12}
\]

Thus A_N=(-1)^N 3/(16N)+O(N^-2), with no hypothesis on zeta zeros.

Proof. The convergent partial-fraction expansion is

\[
 \frac12\psi_\Gamma(s/2)
 =-\frac{\gamma_E}{2}
   +\sum_{m\ge0}\left(\frac1{2m+2}-\frac1{s+2m}\right).
\]

Its m=0 pole cancels the 1/s in (10). For ell=m+1>=2,

\[
 [w^N]\frac1{s(w)+2m}
 =\frac3{4\ell^2}\left(-1+\frac3{2\ell}\right)^{N-1}
 \quad(N\ge1).
\]

The nonconstant coefficients of the convergent digamma expansion may be
summed normally on every compact subdisk of |w|<1; the displayed coefficient
series is absolutely summable. Multiply by 3/8 in (4), and combine (7)--(10).
This proves (11), including its sign and normalization.

For (12), set
`f_N(x)=x^-2*(1-3/(2x))^(N-1)` on x>=2. For N>=2 it is unimodal, with
maximum at x=3(N+1)/4, and `max f_N <=16/[9(N+1)^2]`. Its integral is

\[
 \int_2^\infty f_N(x)dx=\frac2{3N}(1-4^{-N}).
\]

Comparing each integer rectangle with the integral over that rectangle
bounds the sum-integral error by `int_2^infinity |f_N'| <=2 max f_N`.
Multiplication by 9/32 proves (12).

Consequently the subexponential bound for E_N is equivalent to that for d_N,
and is sufficient for the original c_N(2) by (3). The archimedean portion
of this source estimate is fully controlled; the prime discrepancy is not.

## 4. Exact signed integral and normalized prime error

Define

\[
 \Psi(x)=\sum_{n\le x}\Lambda(n),\qquad \Delta(x)=\Psi(x)-x.
\]

**AL-4 (prime-error identity).** For N>=1,

\[
 E_N=\int_{[1,\infty)}x^{-2}L_N^{(-1)}(3\log x)\,d\Delta(x)
\]
\[
 =\int_1^\infty\Delta(x)x^{-3}
       \left[2L_N(3\log x)+L_{N-1}(3\log x)\right]dx.           \tag{13}
\]

Here L_j=L_j^(0). At an integer endpoint the Stieltjes integral includes
its Lambda atom according to the displayed closed/open interval convention.
Lebesgue integrals do not depend on isolated endpoint values.

Proof. Integration by parts is legitimate because
`Psi(x)<=sum_{n<=x} log(n)<=x log(x)` and fixed-degree logarithmic powers
are integrable against x^-2. The boundary at infinity is zero. At x=1,
`L_N^(-1)(0)=0` for N>=1, so the boundary is zero despite Delta(1)=-1.
Finally use
`(L_N^(-1))'=-L_{N-1}` and `L_N^(-1)=L_N-L_{N-1}`. This yields the
coefficient `2L_N+L_{N-1}`, not `2L_N-L_{N-1}`.

With t=3 log(x) and phi_j(t)=exp(-t/2)L_j(t), (13) becomes

\[
 \boxed{E_N=\frac13\int_0^\infty
   \frac{\Delta(e^{t/3})}{e^{t/6}}
       [2\phi_N(t)+\phi_{N-1}(t)]\,dt.}                       \tag{14}
\]

The exact source is the prime error normalized by sqrt(x). Equation (14)
is an ordinary convergent integral for every fixed N under the elementary
bound above. No square-root estimate for Delta has been assumed. Using
such an estimate to bound it would require proving or explicitly importing
that arithmetic premise; equation (14) does not supply it.

## 5. Quantify the failure of a termwise absolute-value proof

For 0<r<1 the parameter-minus-one generating function and Cauchy's estimate
give, for x>=0,

\[
 |L_N^{(-1)}(x)|\le r^{-N}\exp\!\left(\frac{xr}{1+r}\right).     \tag{15}
\]

Indeed the minimum of Re(z/(1-z)) on |z|=r is -r/(1+r).

**AL-5 (exact unsigned exponential rate).** Let

\[
 U_N=\sum_{n\ge2}\frac{\Lambda(n)}{n^2}
                         |L_N^{(-1)}(3\log n)|.
\]

Then unconditionally

\[
 \boxed{\limsup_{N\to\infty}U_N^{1/N}=2.}                       \tag{16}
\]

For the upper bound, take 0<r<1/2 in (15). Then

\[
 U_N\le r^{-N}\sum_{n\ge2}\frac{\Lambda(n)}
          {n^{2-3r/(1+r)}}=C_r r^{-N}<\infty.
\]

Let r increase to 1/2 after taking the root limsup. For the lower bound,
`sum_N (-1)^N P_N w^N = -zeta'/zeta(s(w))` is analytic on |w|<1/2 and has
a nonremovable pole at w=1/2, the image of the simple zeta pole s=1.
Its Taylor radius is exactly 1/2. Cauchy--Hadamard gives
`limsup |P_N|^(1/N)=2`, and `U_N>=|P_N|` finishes the proof.
The N=0 term in the generating series is its ordinary convergent prime sum.

This is a statement about this particular unsigned representation. It does
not rule out estimates using the actual arithmetic signs. It shows exactly
why a direct triangle inequality cannot establish a zero exponential rate.

## 6. Close the small-prime and far-tail ranges uniformly in degree

Let f_N(x)=x^-2 L_N^(-1)(3 log x). For any real cutoff X, keep atoms at X
on the lower side. Define the signed residual on a range J by

\[
 E_N(J)=\sum_{n\in J}\Lambda(n)f_N(n)-\int_J f_N(x)dx.
\]

**AL-6 (two-ended unconditional bounds).** Uniformly in N>=1 and X>=2,

\[
 |E_N([1,X])|\le 2e\sqrt X(\log X+1).                         \tag{17}
\]

Uniformly for X>=3,

\[
 |E_N((X,\infty))|\ll 8^N X^{-2/3}(\log X+1),                 \tag{18}
\]

with an absolute implicit constant independent of N and X.

Proof. In (15), choose r=N/(N+1). Then r^-N<=e and r/(1+r)<1/2, so
`|L_N^(-1)(t)|<=e exp(t/2)`. Use Lambda(n)<=log(n),
`sum_{2<=n<=X}n^-1/2<=2sqrt(X)`, and
`int_1^X x^-1/2 dx<=2sqrt(X)` to obtain (17).
For (18), use r=1/8 in (15):
`|L_N^(-1)(3log x)|<=8^N x^(1/3)`.
The prime and continuous tails are bounded by the elementary sums/integrals
of `log(x) x^-5/3` and `x^-5/3`. Integral comparison, including one endpoint
cell, gives (18). No prime distribution estimate is needed.

In particular, for N>=2, put

\[
 J_N=(e^{\sqrt N},e^{4N}].
\]

Equations (17)--(18) prove

\[
 \boxed{E_N=E_N(J_N)
 +O((\sqrt N+1)e^{\sqrt N/2})
 +O((N+1)e^{-N/2}).}                                          \tag{19}
\]

For the high tail, `8^N exp(-8N/3)<=exp(-N/2)` follows, for example, from
`log(2)<7/10`; the latter follows already from
`1+7/10+(7/10)^2/2+(7/10)^3/6>2`. The omitted finite degrees affect only a fixed constant.
The continuum main term is subtracted INSIDE each of the three ranges;
one must not subtract the whole value (7) from the middle range alone.

Thus this pass proves both complementary estimates. The exact remaining
condition in this coordinate is

\[
 \boxed{\forall\epsilon>0\ \exists C_\epsilon<\infty\ \forall N\ge2:
 |E_N((e^{\sqrt N},e^{4N}])|\le C_\epsilon e^{\epsilon N}.}       \tag{20}
\]

This is a growing prime-power range, not a finite truncation that can be
checked once. Its endpoints were selected from the unconditional kernel
bounds, not fitted to data. Equation (20) remains unproved.

## 7. A positive source satisfying PNT is still insufficient

**AL-7 (continuous-source control, NOT the prime measure).** Put

\[
 \rho=3/4+i,\quad \varepsilon_0=1/2,\qquad
 d\Psi_*(x)=[1+\varepsilon_0 x^{-1/4}\cos(\log x)]dx\quad(x\ge1).
\]

Choose the primitive with Psi_*(1)=1. This is a strictly positive smooth
density, between 1/2 and 3/2, and

\[
 \Psi_*(x)-x=\varepsilon_0\Re\frac{x^\rho-1}{\rho}=O(x^{3/4}).
\]

Nevertheless its discrepancy (6), with dPsi_* replacing the prime atoms,
has

\[
 E_{*,N}=\frac12\Re\left[
       \frac{3(-1)^N}{(2-\rho)^2}
       \left(\frac{1+\rho}{2-\rho}\right)^{N-1}\right],
\]
\[
 \boxed{\limsup |E_{*,N}|^{1/N}=\sqrt{65/41}>1.}               \tag{21}
\]

Proof. Substitute y=log(x) and integrate the finite polynomial against
`exp(-(2-rho)y)`. For q=2-rho,

\[
 \int_0^\infty e^{-qy}L_N^{(-1)}(3y)dy
  =(-1)^N\frac3{q^2}\left(\frac{3-q}{q}\right)^{N-1}.
\]

This follows either by finite integration or the rational generating
function `(1-z)/(q+(3-q)z)`. The modulus squared of (1+rho)/(2-rho) is
65/41. Taking the real part does not erase the exponential limsup: the
conjugate rational generating functions have distinct nonreal poles and
nonzero residues, so the Taylor radius is their common modulus. The
positive and negative frequency poles do not cancel.

This source has a power-saving prime-number-theorem analogue but fails
the target inequality. It has neither actual prime-power support nor the
Euler product of zeta, and is NOT a counterexample to RH. Its role is to
prevent an attempted proof from using only positivity, smoothness, or an
unspecified PNT error while claiming to control (20). The actual discrete
arithmetic must enter a successful next argument.

## 8. Disposition of the attempted proof

What is proved in this draft: exact return to c_N(2) with polynomial loss;
exact subtraction of the polar exponential; every archimedean coefficient
with a uniform bound and O(N^-2) asymptotic error; the normalized-prime-error
integral; the exact rate 2 for unsigned prime estimates; and both tails in
(19). All these proofs are offered for independent review.

What is NOT proved: the signed middle-range estimate (20), the original
all-epsilon bound on c_N, or RH. The source formula is not itself an
estimate. A mean-square or pointwise square-root bound for Delta, analyticity
of xi'/xi on Re(s)>1/2, or an assumption that this Laguerre residual is
bounded would insert the conclusion-bearing premise rather than prove it.

No new zero-free region, zero proportion, all-height census, positivity of
the prime discrepancy, or external mathematical priority is claimed.
The calculations are in the classical Li/Bombieri--Lagarias tradition,
not a new positivity criterion. The contribution is the explicit source
normalization and the independently proved components of its estimation.

## References and trust boundary

- Parent: PR #792, exact commit and path in the header; its original four
  files remain byte-for-byte unchanged by this addendum.
- NIST DLMF 18.12.8 and 18.12.13 (Chebyshev/Laguerre generating functions):
  https://dlmf.nist.gov/18.12
- NIST DLMF 5.7.6 (digamma partial fractions): https://dlmf.nist.gov/5.7
- NIST DLMF 25.2, 25.4, 25.10 (Euler product, completion, zero symmetries):
  https://dlmf.nist.gov/25.2 ; https://dlmf.nist.gov/25.4 ; https://dlmf.nist.gov/25.10
- Jeffrey C. Lagarias, *Li coefficients for automorphic L-functions*,
  Ann. Inst. Fourier 57 (2007), 1689--1740, DOI 10.5802/aif.2311.
  https://aif.centre-mersenne.org/articles/10.5802/aif.2311/

The classical identities used are stated above and specialized directly.
No theorem from the Lagarias article is invoked to discharge the open
prime discrepancy. No zero-verification input or computation is needed
for AL-1 through AL-7. Finite fixtures cannot certify the analytic passages,
all-degree estimates, or arithmetic cancellation in (20).
