# The high-rank Haar boundary law for elliptic symmetric powers

## Status and scope

This note proves an exact compact-group limit theorem.  It requires no finite
field, curve, model, random sample, numerical integration, or runtime symbolic
algebra.  It explains why the exact tensor/symmetric-power moment ladder has
variance one but even moments of order four and above that grow polynomially
with the symmetric-power index.

The result is representation-theoretic.  It is not an arithmetic-family
equidistribution theorem, and it says nothing by itself about Euler products,
zeros, RH, or GRH.

## 1. Oscillatory weak limit

Write a Haar `SU(2)` conjugacy class as

\[
 \operatorname{diag}(e^{i\Theta},e^{-i\Theta}),
 \qquad
 d\mu(\theta)={2\over\pi}\sin^2\theta\,d\theta,
 \quad 0<\theta<\pi.
\]

The character of `Sym^n` is

\[
 \chi_n(\Theta)={\sin((n+1)\Theta)\over\sin\Theta}.
 \tag{1}
\]

Let `U` be uniform on `[0,2pi]`, independently of `Theta`, and put

\[
 W={\sin U\over\sin\Theta}.
 \tag{2}
\]

Then

\[
 \boxed{\chi_n(\Theta)\ \Longrightarrow\ W.}
 \tag{3}
\]

Indeed, for every continuous function `F(theta,u)` that is periodic in its
second variable, Fourier approximation in `u` and the Riemann--Lebesgue lemma
give

\[
 (\Theta,(n+1)\Theta\bmod2\pi)\Longrightarrow(\Theta,U).
 \tag{4}
\]

The quotient in (1) is singular only at the endpoints.  Removing
`(0,delta) union (pi-delta,pi)` loses Haar mass `O(delta^3)`, uniformly in
`n`; on the remaining compact interval the continuous mapping theorem applies.
Letting `delta` tend to zero proves (3).  Every parity subsequence has the same
limit.

## 2. The limit has an exact cubic tail

For `0<=y<=1`, the Haar mass of the two endpoint regions
`sin(Theta)<y` is

\[
 F_\Theta(y)={2\over\pi}
 \left(\arcsin y-y\sqrt{1-y^2}\right)
 ={4\over3\pi}y^3+O(y^5).
 \tag{5}
\]

Since `E|sin U|^3=4/(3pi)`, equations (2) and (5) give

\[
 \boxed{
 \Pr(|W|>x)
 ={16\over9\pi^2}x^{-3}+O(x^{-5}).}
 \tag{6}
\]

Equivalently, for `x>=1`, one may use the exact integral

\[
 \Pr(|W|>x)
 ={8\over\pi^2x^3}\int_0^1
 {t^2\arccos t\over\sqrt{1-t^2/x^2}}\,dt,
 \tag{7}
\]

and `integral_0^1 t^2 arccos(t) dt=2/9`.

For nonnegative real `a`, independence gives

\[
 \mathbb E|W|^a
 =\mathbb E|\sin U|^a\,{2\over\pi}
 \int_0^\pi\sin^{2-a}\theta\,d\theta.
 \tag{8}
\]

Therefore

\[
 \boxed{\mathbb E|W|^a<\infty\quad\Longleftrightarrow\quad0\le a<3.}
 \tag{9}
\]

In particular, `W` is symmetric, has mean zero and variance one, but has
infinite absolute moments of every order at least three.

## 3. The endpoint boundary layer explains the moment polynomial

Put `N=n+1`.  For `k>=2`, the exact even moment is

\[
 B_k(n)={2\over\pi}\int_0^\pi
 \sin^{2k}(N\theta)\sin^{2-2k}\theta\,d\theta.
 \tag{10}
\]

Scaling `theta=x/N` at both endpoints, with a separate dominated-convergence
argument, gives

\[
 \boxed{
 B_k(n)\sim L_kN^{2k-3},\qquad
 L_k={4\over\pi}\int_0^\infty
 {\sin^{2k}x\over x^{2k-2}}\,dx>0.}
 \tag{11}
\]

This is a boundary-layer theorem, not a consequence of weak convergence
alone.  The weak limit has no `2k`-th moment, and the limits `n->infinity`
and `x->infinity` do not commute.

For `n>=k-1`, the coefficient formula in the locked moment-ladder packet is a
polynomial of exact degree `2k-3`.  Its leading coefficient is

\[
 L_k=-{1\over2(2k-3)!}
 \sum_{j=0}^{k-1}(-1)^j{2k\choose j}(k-j)^{2k-3}.
 \tag{12}
\]

The first cases `L_2=1`, `L_3=1/2`, and `L_4=1/3` reproduce the displayed
fourth-, sixth-, and eighth-moment polynomials.  At the cubic threshold,

\[
 \mathbb E|\chi_n|^3
 \sim {16\over3\pi^2}\log N.
 \tag{13}
\]

The second moment is exceptional and remains exactly one.

### 3.1 The complete real-moment phase diagram

The same argument gives a sharp trichotomy for every real `p>=0`, not only
for even integers.  Set

\[
 A_p={1\over\pi}\int_0^\pi\sin^p u\,du
 ={\Gamma((p+1)/2)\over\sqrt\pi\,\Gamma((p+2)/2)}.
 \tag{14}
\]

Then, as `N=n+1` tends to infinity,

\[
 \boxed{
 \mathbb E|\chi_n|^p\longrightarrow
 {2A_p\over\pi}\int_0^\pi\sin^{2-p}\theta\,d\theta,
 \qquad 0\le p<3,}
 \tag{15}
\]

\[
 \boxed{
 \mathbb E|\chi_n|^3\sim {16\over3\pi^2}\log N,}
 \tag{16}
\]

and

\[
 \boxed{
 \mathbb E|\chi_n|^p\sim C_pN^{p-3},\qquad
 C_p={4\over\pi}\int_0^\infty
 {|\sin x|^p\over x^{p-2}}\,dx,\qquad p>3.}
 \tag{17}
\]

All constants displayed here are finite and strictly positive in their stated
ranges.  Formula (15) is exactly the `p`-th absolute moment of the weak limit
`W`: periodic averaging applies because `sin^(2-p)(theta)` is integrable
precisely for `p<3`.  At `p=3`, the average `A_3=4/(3pi)` multiplies the two
logarithmic endpoint integrals and the Haar factor `2/pi`, giving (16).  For
`p>3`, put `theta=x/N` at both endpoints.  The rescaled integrand is dominated
near zero by `x^2` and at infinity by an integrable multiple of `x^(2-p)`;
the portion outside shrinking endpoint neighbourhoods is lower order.  This
proves (17).

For `p=2k>=4`, (17) reduces to (11).  In particular,
`C_4=1`, `C_6=1/2`, and `C_8=1/3`.  The exponent `p-3` is the codimension-three
endpoint law made quantitative: below three, bulk oscillation controls the
statistic; at three, bulk and boundary balance logarithmically; above three,
the near-central boundary layer controls the leading order.

## 4. Product and principal ladder limits are different

For the tensor ladder, let

\[
 X_r=\chi_1(u)\chi_r(v),
 \qquad
 Y_r=\chi_{2r+1}(w),
\]

with all Haar variables independent where appropriate.  Put
`Z=chi_1(u)=2cos(Theta_0)`.  Then (3) gives

\[
 \boxed{Y_r\Longrightarrow W,
 \qquad X_r\Longrightarrow ZW,}
 \tag{18}
\]

where `Z` and `W` are independent.  Both limiting laws are symmetric with
mean zero and variance one.  They are nevertheless different.  Directly,

\[
 \mathbb E|Z|^3={64\over15\pi}.
 \tag{19}
\]

The bounded regular-variation calculation applied to (6) yields

\[
 \boxed{
 \Pr(|ZW|>x)
 \sim {1024\over135\pi^3}x^{-3}.}
 \tag{20}
\]

Thus the product limit has the larger absolute-tail constant by the factor
`64/(15pi)`.  This supplies a high-rank distributional discriminator even
though both laws have the same first two moments and all their finite-rank
even moments of order at least four diverge.

There is a useful non-uniform-integrability warning.  Although the limiting
law `W` is symmetric,

\[
 \mathbb E\chi_n^3=
 \begin{cases}1,&n\text{ even},\\0,&n\text{ odd}.
 \end{cases}
 \tag{21}
\]

Endpoint mass is negligible for weak convergence but can retain a signed
cubic invariant.

## 5. Arithmetic and research boundary

The companion all-r moment packet proves the finite-rank compact moments and
has canonical payload
`0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088`.
This note supplies an analytic large-r interpretation; it does not alter that
source-locked artifact.

An arithmetic use would require a two-limit theorem: first an arithmetic
family must equidistribute to the stated compact image at fixed `r`, and then
that control must be uniform enough to let `r` grow.  Neither step is proved
here.  In particular, finite-field trace histograms, monodromy, automorphy,
analytic continuation, zero statistics, RH, and GRH remain separate.

The concrete experimental prediction is to compare truncated tails or bounded
test functions rather than raw moments when rank grows.  Raw even moments of
order four and higher are increasingly controlled by rare near-central
conjugacy classes.
