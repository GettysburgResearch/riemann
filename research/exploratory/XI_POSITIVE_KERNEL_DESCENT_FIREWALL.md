# Positive smooth theta-tail kernel does not discharge descent

Status: NATIVE QUANTITATIVE COUNTEREXAMPLE; INDEPENDENT EXACT-SHA REVIEW REQUIRED.

Scope: one fixed even real entire cosine transform. Its frequency kernel is
strictly positive and C-infinity, agrees EXACTLY with the actual Xi kernel
outside a compact set, and retains two different high-order/high-frequency
analytic endpoints. Nevertheless it has a simple nonreal zero inside
|Im z|<1/2 and the literal first-rung reverse-Rolle defect is 2.

This is a structural firewall, not a new programme, an RH counterexample,
or an arithmetic object. Established non-descent and cosine-universality
prior art comes first: [Farmer, Section 4.2, pp. 8--9](https://arxiv.org/pdf/2008.07206)
discusses cosine zeros moved off the line and loss of that information under
differentiation. [Gunns--Hughes, Theorem 3.1, pp. 10--11](https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf)
proves compact-domain scaled cosine limits for L-functions. The present
native argument imposes the additional positive smooth exact-theta-tail
conditions and computes a literal defect. No novelty or priority claim is
made for non-descent, cosine universality, or this particular construction.

Exact inputs: the eight commit/blob/LF-hash bindings in the companion
manifest, including the actual-kernel and high-derivative proofs and their
reviews, and L/T/R-107100 at cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57.
These historical files are not changed. Computation checks only bounded
rational identities, strict reserves, coverage, and source contracts;
it does not numerically evaluate Xi, a bump integral, a zero, or a limit.

## 1. One fixed kernel and its exact normalization

Use XL1--XL4 and XL11 of the actual-kernel source. With its theta series
phi0, the full-line Fourier kernel is Phi=2 phi0 and the half-line cosine
kernel is Phi_+=4 phi0. Thus
\[
 \Xi(z)=\int_0^\infty\Phi_+(u)\cos(uz)\,du,\qquad
 4\pi^2V(u)\le\Phi_+(u)\le12\pi^2V(u),\quad
 V(u)=e^{9u/2-\pi e^{2u}}\quad(u\ge0).                 \tag{PF1}
\]
The even extension is smooth and strictly positive. The standard completed
xi normalization gives Xi(i/2)=xi_R(0)=xi_R(1)=1/2, by the residue one of
zeta at 1 and the gamma factors, without RH. Positivity therefore gives
\[
 |\Xi(x+iy)|\le\tfrac12\quad(|y|\le\tfrac12),\qquad
 |\Xi(t)|\le\tfrac12,\quad|\Xi'(t)|\le1,\quad|\Xi''(t)|\le4. \tag{PF2}
\]
Indeed |cos(u(x+iy))|<=cosh(u y), u<=2cosh(u/2), and
u^2<=8cosh(u/2). All differentiations are justified by the real
superexponential tail, uniformly on compact complex sets.

Fix h=1/8. Let beta_h(s) be the even unit-mass bump proportional to
exp[-1/(1-(s/h)^2)] for |s|<h and zero elsewhere. Fix, once and for all,
\[
 B(z)=\int_{-h}^h\beta_h(s)\cos(sz)\,ds,\quad
 P(z)=\cos(4z)+\tfrac13\cos(8z),\quad
 F(z)=B(z)P(z)+\Xi(z)/64,\quad \mathcal F=64F.          \tag{PF3}
\]
Evenness of the bump and the cosine addition formula give
\[
 \widetilde\Phi_+(u)=\Phi_+(u)+64\beta_h(u-4)
                     +\tfrac{64}3\beta_h(u-8),\quad u\ge0,\qquad
 \mathcal F(z)=\int_0^\infty\widetilde\Phi_+(u)\cos(uz)\,du. \tag{PF4}
\]
This is ONE fixed even real entire function. Its kernel is C-infinity and
strictly positive, and equals Phi_+ for u>R=65/8. There is a finite fixed
C>=1 such that Phi_+<=tilde(Phi_+)<=C Phi_+ everywhere: take the maximum
of the continuous ratio on [0,R], then use equality outside. In particular
it is globally comparable to V. No uniform constant over arbitrary bumps
is claimed; this C can be extremely large.

The kernel is NOT frequency-real-analytic. Exact tail equality for two
real-analytic functions on a connected real line would force equality
everywhere. Smoothness here must not be silently upgraded to analyticity.

## 2. A rigorously isolated nonreal zero inside the critical strip

Put C0=(3+sqrt(17))/4, eta=arcosh(C0), z_*=(pi+i eta)/4,
rho=1/256, and D={|z-z_*|<rho}. The equation P(z)=0 is
2x^2+3x-1=0 with x=cos(4z), and cos(4z_*)=-C0.
Since 7/4<C0<2, cosh(1/2)<sqrt(3)<7/4, and
cosh(3/2)>=17/8>2, we have 1/2<eta<3/2.
Consequently the closed disk lies strictly in 0<Im z<1/2 and |z|<3/2.

At its center,
\[
 |P'(z_*)|=\tfrac{4\sqrt{17}}3\sinh\eta>22/3>7,
 \qquad \sinh^2\eta=(5+3\sqrt{17})/8>17/8>(11/8)^2.
\]
Throughout D, using e<3 and |Im z|<1/2,
|P''(z)|<16*9+(64/3)*81=1872. Taylor's integral remainder gives
\[
 |P(z)|>7\rho-936\rho^2=107/8192\quad(z\in\partial D). \tag{PF5}
\]
The same comparison with its linear term proves that P has exactly one
zero in D, counted with multiplicity.

For |z|<3/2 and |s|<=1/8, the elementary entire-series estimate
|cos(sz)-1|<|sz|^2 exp(|sz|)/2 and exp(3/16)<2 give
|B(z)-1|<9/256. Hence B has no zero in D and
\[
 |BP|>\frac{247}{256}\frac{107}{8192}
       =\frac{26429}{2097152}>\frac1{128}\ge|\Xi/64|.  \tag{PF6}
\]
The last strict reserve is 10045/2097152. Rouché proves that F and
therefore cal(F) have exactly one zero in D, counted with multiplicity.
It is simple and nonreal. Evenness and reality give its symmetry partners.
We do NOT claim that every counterfeit zero lies in a fixed strip.

## 3. The actual first-rung defect, not just an off-real zero

Take c=pi/4, r=1/64, I=(c-r,c+r), and J=closure(I). For |s|<=r,
\[
 P(c)=-2/3,\quad P'(c)=0,\quad
 P''(c+s)=16\cos(4s)-(64/3)\cos(8s).
\]
Using 1-x^2/2<=cos x<=1 gives -6<=P''<=-5 on J.
It follows that P<=-2/3, |P|<=4/3, |P'|<=6r,
P'(c-r)>=5r, and P'(c+r)<=-5r.
Since |t|<2 on J, the bump gives
\[
 B(t)\ge31/32,\qquad |B'(t)|\le1/32,\qquad |B''(t)|\le1/64.
\]
Together with (PF2), these are the explicit strict reserves
\[
 F(t)\le-31/48+1/128=-245/384<0,
\]
\[
 F'(c-r)\ge113/6144>0,\qquad F'(c+r)\le-113/6144<0,
\]
\[
 F''(t)\le-155/32+3/512+1/48+1/16=-7303/1536<0.       \tag{PF7}
\]
The endpoint reserve is 155/2048-1/24-1/64=113/6144.
Thus F has no zero on J, and F' has exactly one simple zero t0 in I.
It is a negative strict maximum. The ratio g=F'/F crosses from negative
to positive at t0, and at the endpoints has those same respective signs.

In the L-107100.1--.3 definitions, equivalently the k=0 rung of
T-107100.1--.3, this proves
\[
 r_{0,t0}=1,\quad\iota_{0,t0}=1,\quad
 N_I(F)=0,\quad N_I(F')=1,\quad
 \mathfrak R_I(F)=2,\quad\varepsilon_I(F)=1,\qquad
                    0=1-2+1.                       \tag{PF8}
\]
All four required endpoint values are nonzero. At t0 the Laguerre
quantity F'^2-FF'' is strictly negative. Positive scaling to cal(F)
preserves every sign and every count. We apply the literal real-variable
definition, not the claim that this counterfeit IS Xi. We have not imposed
nonvanishing of every higher derivative at these same endpoints.

## 4. First distinct limit: k tends to infinity

Write b0=tilde(Phi_+)-Phi_+>=0, L=9>R, M=int b0=256/3, and
m=int_[2L,2L+1] Phi_+>0. These are fixed constants. For every integer k>=0,
\[
 Z_k=\int u^k\Phi_+(u)du\ge m(2L)^k,\qquad
 \Delta Z_k=\int u^kb_0(u)du\le ML^k,\qquad
 \delta_k=\Delta Z_k/Z_k\le(M/m)2^{-k}.               \tag{PF9}
\]
Use the EXACT SAME a_k,S_k,sigma_k as HD3--HD4 of the reviewed
high-derivative theorem, not a newly estimated mode:
k/a+9/2=2pi exp(2a), S=k/a~2k/log k, a~(log k)/2.

For each fixed integer j>=0 and B0>=0, uniformly for 0<=H<=B0 sqrt(S),
\[
 \frac{\int u^k b_0(u)|u-a|^j e^{H|u-a|}du}{Z_k}
 \le (M/m)2^{-k}(a+L)^j e^{H(a+L)}
                    =e^{-k\log2+o(k)}.              \tag{PF10}
\]
The last assertion follows from a=O(log k) and
sqrt(S)(a+L)=O(sqrt(k log k))=o(k). It is uniform in that height range.
For the new probability measure, the numerator of each nonnegative
weighted moment is the old numerator plus this compact contribution, and
the denominator is Z_k(1+delta_k). Thus
\[
 \widetilde{\mathbb E}|U-a|^j e^{H|U-a|}
       \le C_{j,B0}S^{-j/2}+e^{-k\log2+o(k)}.         \tag{PF11}
\]
The old constants remain valid for the OLD term; no factor-three bound
for the complete new kernel is asserted.

Let tilde(F_k)=(-1)^k cal(F)^(k)/tilde(Z_k) and G_k=cos(a_k z-k pi/2).
The elementary HD13 comparison applies to the new measure. With m_j(H)
denoting its moment in (PF11), the three errors after dividing by
exp(a|Im z|), and respectively 1,a,a^2, are at most
\[
 |z|m_1,\qquad (|z|+1/a)m_1,\qquad
 (|z|+2/a)m_1+m_2/a^2.                              \tag{PF12}
\]
Hence all tend to zero uniformly when T_k+H_k=o(sqrt(k/log k)).
Use FULL comparison disks of radius r_k=1/(4a_k), centers
|z_j|<=T_k+r_k, horizontal enlargement T_k+2r_k, height
H_*=max(H_k,r_k), and |z|<=T_k+2r_k+H_*.
The HD14 reference lower bound 1/10 and conjugation then give one simple
real zero in each selected disk and no other zero in the rectangle, for
all sufficiently large k. In particular every counterfeit derivative
zero in the rectangle is real and simple. Fixed H=1/2 is allowed.
There is NO exact count at the rectangle's vertical endpoints: disks may
meet those endpoints. On its real interval,
\[
 \widetilde F_k'^2-\widetilde F_k\widetilde F_k''
                       =a_k^2(1+o(1))>0.            \tag{PF13}
\]
For errors at most 1/32 the explicit relative reserve is 447/512.
This is an endpoint statement about large k, compatible with (PF8) at k=0.

The old Gaussian limit also persists: (PF9) gives vanishing total
variation, and (PF10), including any fixed higher polynomial/exponential
weight in (U-a)/sigma, gives weighted uniform integrability.
Consequently the HD18 fixed-Csigma weighted tail has the SAME strictly
positive limit 4 exp(h0^2/2) normal_upper_tail(C-h0) if H sigma->h0>=0.
It is not exponentially small in k. Its four-sigma, h0=0 limit is less
than 1/256. Neither fixed-window decay nor a practical k cutoff is invented.

## 5. Second distinct limit: source frequency xi tends to infinity

Now K is a FIXED positive odd integer, not k and not growing with xi.
Use full-line kernels Phi(u)=Phi_+(|u|)/2 and
tilde(Phi)(u)=tilde(Phi_+)(|u|)/2. Their tails agree for |u|>R.
Define exactly the generic convolution objects
\[
 u=(\xi-d)/2,\quad v=(\xi+d)/2,\quad H_\xi(d)=\Phi(u)\Phi(v),
 \quad W=d(v^K-u^K),\quad Z=\int WH_\xi,\quad d\mu=WH_\xi\,dd/Z. \tag{PF14}
\]
Tildes mean replacement of both Phi factors, with no change in W.
For odd K and xi>0, W is nonnegative by the XL5 positive polynomial.

Here is the endpoint-side extension of the actual global kernel bound.
For |d|<=xi, (PF1) gives
H/H(0)<=9 exp[-2pi e^xi(cosh d-1)].
For d>=xi let a=d-xi. Evenness changes |u|+|v| from xi to d, and
\[
 e^d\cosh\xi-e^\xi\cosh d=\sinh(d-\xi).
\]
The additional factor is exp[9a/2-2pi sinh a]<=1, because
sinh a>=a and 2pi>9/2. Reflection handles d<=-xi. Thus for ALL real d,
\[
 0<H_\xi(d)/H_\xi(0)\le9e^{-2\pi e^\xi(\cosh d-1)}
                              \le9e^{-\pi e^\xi d^2}. \tag{PF15}
\]
No region with a negative u or v has been discarded.

For xi>2R the central values agree: tilde(H)(0)=H(0).
The difference D=tilde(H)-H is nonnegative, bounded by (C^2-1)H,
and supported in
\[
 \xi-2R\le |d|\le\xi+2R.                             \tag{PF16}
\]
Indeed a changed factor requires |u|<=R or |v|<=R. Both cannot occur
when u+v=xi>2R. The two enclosing intervals have total length 8R;
(PF16) is a SUPPORT ENCLOSURE, not an assertion of nonzero difference
at every point, and it includes |d|>xi.

For fixed integer q>=0 and fixed h0>=0, define
D_q=int |d|^(2q) exp(h0|d|) W(d) D(d) dd. Since on that support
W<=2(xi+2R)(xi+R)^K, (PF15) proves the explicit bound
\[
 D_q\le144R(C^2-1)H_\xi(0)(\xi+2R)^{2q+1}(\xi+R)^K
       e^{h0(\xi+2R)}e^{-\pi e^\xi(\xi-2R)^2}.       \tag{PF17}
\]
The actual XL14 normalization is
\[
 Z\ge c_K\xi^{K-1}H_\xi(0)e^{-3\xi/2},\qquad
 c_K=(2e^{-2\pi}/27)K2^{1-K}>0.                      \tag{PF18}
\]
For xi>=4R, (xi-2R)^2>=xi^2/4. Every other logarithmic factor in
(PF17)/(PF18) is O_(K,q,h0,C,R)(xi+log xi). Therefore, for all
sufficiently large xi, D_q/Z=O(exp[-(pi/8)e^xi xi^2]).
Constants and the threshold depend on the fixed displayed data.

Normalization must still be paid. For any integrable observable A,
put J=int AWH, Delta J=int AWD, delta=Delta Z/Z. Then EXACTLY
\[
 \widetilde{\mathbb E}A-\mathbb EA
  =\frac{\Delta J/Z-(\mathbb EA)\delta}{1+\delta},
 \quad
 |\widetilde{\mathbb E}A-\mathbb EA|
 \le|\Delta J|/Z+|\mathbb EA|\delta.                 \tag{PF19}
\]
This includes signed A; coefficient cancellation is not assumed.
For A=|d|^(2q)exp(h0|d|), XL8 bounds the old expectation, so the
normalized moment difference is superexponentially small too.

For completeness the unweighted numerator estimate is
int |d|^j exp(h0|d|)D dd <=
72R(C^2-1)H(0)(xi+2R)^j exp[h0(xi+2R)-pi e^xi(xi-2R)^2].
Apply it termwise to the finite XL6 polynomials P_K,Q_K and use (PF19)
and (PF18). Their fixed powers of xi and exp(xi) are absorbed by lowering
pi/8 to, for example, pi/16. Thus the counterfeit's IDENTICALLY DEFINED
generic L_K,a_(K,0),g_K,p_K and current ratios retain the actual XL8--XL21
leading constants, and any finite-order correction already proved there:
\[
 \tilde m_2\sim(3/(2\pi))e^{-\xi},\qquad
 \tilde g_K\sim(\pi/K)\xi^2e^\xi,\qquad
 \tilde p_K=\frac1{2K}+\frac{K^2-1}{4\pi K}
                \frac{e^{-\xi}}{\xi^2}+o(e^{-\xi}/\xi^2). \tag{PF20}
\]
At K=1, p=1/2 exactly by its algebra. L=Z/4 has relative error delta,
and the positive unweighted numerator has the same relative conclusion
by XL16. Hence absolute leading densities also agree, because the tail
coefficient in (PF4) is ONE. Using F instead of cal(F) would multiply
quadratic absolute densities by 1/64^2, but not normalized ratios.
For the current, apply (PF19) to A=sinh(hd)/(hd)-1, not just to
sinh(hd)/(hd): for 0<h<=h0 it is bounded by a constant times
h^2 d^2 exp(h0|d|). Thus the normalization error also retains its h^2
factor. The remainder after h^2 d^2/6 is bounded by a constant times
h^4 d^4 exp(h0|d|). These estimates retain the XL21 uniformity for
0<h<=h0 after division by h^2 exp(-xi), with continuity at h=0.
This is NOT an assertion that any authentic Xi source jets or arithmetic
Pick identity belong to the counterfeit.

## 6. Exact gate implication and replay boundary

The fixed function (PF3)--(PF4) simultaneously has a positive smooth
kernel, exact theta tail, the high-derivative endpoint (PF12)--(PF13),
and the generic high-frequency current constants (PF20). Nevertheless
(PF6) gives a nonreal strip zero and (PF8) gives a paid defect of two.
Those analytic properties ALONE therefore cannot discharge the
T-107100 accumulated defect or Xi-specific XICURV107110.

Nothing here refutes an authentic-Xi argument using additional
arithmetic or native source information. There is no Euler product,
authentic source-jet congruence, global strip confinement, RH/GRH,
percentage-of-zeros, or novelty claim. The limits k->infinity and
xi->infinity at fixed K are separate and have not been interchanged.

The companion exact-rational producer rebuilds the fixed algebraic root,
Taylor/bump/curvature reserves, the r=1,iota=1 boundary ledger, odd-K
balanced and endpoint-side weight identities, exterior exponential
identity in formal positive variables, ratio-normalization identities,
and finite compact-mass and exponent budgets. It authenticates every
frozen repository source and binds note/producer/test/manifest LF hashes.
Semantic mutations, bool/float contamination, missing sources and caps
fail closed, also under Python -O. The native analytic proofs above,
not these finite controls or status labels, establish existence and limits.

Replay:
python -m unittest discover -s tests -p test_xi_positive_kernel_descent_firewall.py
python -O -m unittest discover -s tests -p test_xi_positive_kernel_descent_firewall.py
python research/exploratory/xi_positive_kernel_descent_firewall.py --check
python -O research/exploratory/xi_positive_kernel_descent_firewall.py --check

Smallest load-bearing interfaces: the strict reserves (PF5)--(PF7), the
full-disk weighted-moment inheritance (PF10)--(PF12), and the global
endpoint-side/normalization bounds (PF15)--(PF19). Review all three;
no bounded numerical panel substitutes for any of them.
