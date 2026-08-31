# Actual Xi high-derivative saddle gate

Status: NEW NATIVE ANALYTIC PROOF; INDEPENDENT EXACT-SHA REVIEW REQUIRED.

Scope: the actual positive theta kernel, all sufficiently large integer
derivative orders, and growing complex rectangles. This closes the repaired
high-derivative endpoint gate only. XICURV107110, descent, and RH remain open.

The PR767 claims at cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57 are immutable
inputs, not edited claims. Their full-disk tail-height issue is repaired here.
No proposed historical complex moving-saddle theorem is imported.

What is machine checked: bounded exact saddle-coordinate algebra, curvature
and perturbation budgets, Gaussian moment identities, and an integer-certified
tail-height countercontrol. No numerical integration, Xi samples, numerical
zero counts, fitted limits, or formal verification of the analytic proof.

## 1. Literal kernel, normalization, and theorem

Use XL1--XL4 and XL11--XL12 of the reviewed real-kernel note frozen at
3b6972320899a82c6caa3a98e2ada5ff703a605a. Write
\[
 \phi_0(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2})
                      e^{-\pi n^2e^{2u}},\qquad u\ge0.
\]
The full-line Fourier kernel is 2 phi_0, so the half-line cosine kernel is
\(\Phi_+(u)=4\phi_0(u)\). In particular
\[
 \Xi(z)=\int_0^\infty\Phi_+(u)\cos(uz)\,du,\qquad
 d\nu_k(u)=\frac{u^k\Phi_+(u)du}{Z_k},\quad
 Z_k=\int_0^\infty u^k\Phi_+(u)du>0.
\tag{HD1}
\]
These scalar conventions do not change nu_k; no frequency rescaling occurs.
For theta=k pi/2 define
\[
 F_k(z)=\int\cos(uz-\theta)d\nu_k(u)
       =(-1)^k\Xi^{(k)}(z)/Z_k.
\tag{HD2}
\]
Thus normalization and parity do not change zeros or Laguerre signs.

Put b=9/2. For k>0 let a=a_k be the unique positive solution of
\[
 k/a+b=2\pi e^{2a},\qquad S=S_k=k/a,\qquad
 \Lambda=\Lambda_k=k/a^2+2k/a+9,\qquad \sigma=\Lambda^{-1/2}.
\tag{HD3}
\]
The center a is the saddle of the explicit comparison density, not a claim
about exact global log-concavity or the exact mode of the full theta kernel.
Existence and uniqueness follow since k/a+b decreases from infinity to b
and the right side increases. As k tends to infinity,
\[
 a=\tfrac12 W(k/\pi)+O(\log k/k)
  =\tfrac12(\log k-\log\log k-\log\pi+o(1)),\quad
 S\sim2k/\log k,\quad \sigma\sim\tfrac12\sqrt{\log k/k}.
\tag{HD4}
\]
The Lambert-W relation follows from 2a e^(2a)=(k+ba)/pi; its derivative
or the mean value theorem bounds the perturbation from ba by O(a/k).

**Theorem.** For every fixed integer j>=0 and fixed B>=0 there is an explicit
finite C_(j,B), given in (HD10), such that for all a>=2 and
S>=max(64,1024 B^2),
\[
 \mathbb E_{\nu_k}|U-a|^j e^{H|U-a|}
 \le C_{j,B}S^{-j/2},\qquad 0\le H\le B\sqrt S.
\tag{HD5}
\]
Consequently, for any nonnegative sequences T_k,H_k satisfying
\[
 T_k+H_k=o(\sqrt{S_k})=o(\sqrt{k/\log k}),
\tag{HD6}
\]
all sufficiently large k have the following properties:

1. Every zero of Xi^(k) in |Re z|<=T_k, |Im z|<=H_k is real and simple.
2. Each comparison-zero disk specified in Section 4 has exactly one real,
   simple zero, and there are no other zeros in that rectangle.
3. F_k'(t)^2-F_k(t)F_k''(t)=a_k^2(1+o(1)) uniformly for |t|<=T_k.

The little-o assertions are uniform along any such sequences, in both
parities. Fixed H=1/2 is allowed; there is no need for H<1/2. No assertion
about zeros outside the specified rectangles or about low derivatives is made.

## 2. A global real saddle bound, including the origin-side tail

Let V(u)=exp(bu-pi exp(2u)), q_k(u)=u^k V(u), and ell=log q_k.
The primitive theta bounds XL11--XL12 give, for every u>=0,
\[
 4\pi^2 V(u)\le\Phi_+(u)\le12\pi^2 V(u),\qquad
 \Phi_+(u)/(8\pi^2V(u))\longrightarrow1\quad(u\to\infty).
\tag{HD7}
\]
They are global real bounds, not an imported translated-ray assertion.
Using the exact saddle equation, for every s>-a,
\[
 \ell(a+s)-\ell(a)
 =k[\log(1+s/a)-s/a]
  -\frac{S+b}{2}[e^{2s}-1-2s].
\tag{HD8}
\]
Both bracketed losses have the required sign. More explicitly:

- If s>=0, e^(2s)-1-2s>=2s^2.
- If -1<=s<=0, the integral Taylor remainder is at least 2e^(-2)s^2.
- If s<=-1, putting r=-s gives e^(-2r)-1+2r>=r.

Since e<3, these prove the deliberately conservative global estimate
q_k(a+s)/q_k(a)<=exp[-S min(s^2,|s|)/16]. This includes every u in (0,a-1),
not just a fixed neighbourhood of the saddle.

For |s|<=S^(-1/2), a>=2 and S>=64, one has
\[
 |\ell''(a+s)|/S
 \le128/225+2(137/128)e^{1/4}<4<8.
\]
Here a/(a-1/8)^2<=128/225, b/S<=9/128, and e^(1/4)<4/3, since e<3.
Taylor's integral formula gives ell(a+s)-ell(a)>=-4 on that interval.
Its length is 2/sqrt(S). Combining this normalization reserve with (HD7)
gives the actual normalized density bound
\[
 \boxed{\frac{d\nu_k(a+s)}{ds}
 \le C_*\sqrt S\exp[-S\min(s^2,|s|)/16],\qquad
 C_* =3e^4/2,quad s>-a.}
\tag{HD9}
\]
All denominators are positive and finite. Superexponential decay justifies
differentiation of (HD1)--(HD2) for complex z on each compact set; near u=0
the theta kernel is bounded and u^k is integrable.

## 3. Uniform weighted moments and an actual weighted-tail bound

For |s|<=1 substitute t=sqrt(S)|s| in (HD9). For |s|>=1, the hypothesis
S>=1024 B^2 implies H<=S/32, leaving exp(-S|s|/32). Extension of the two
integrals to positive infinity yields (HD5) with, for example,
\[
 \boxed{C_{j,B}=3e^4\left[
  \int_0^\infty t^j e^{-t^2/16+Bt}dt+j!32^{j+1}\right].}
\tag{HD10}
\]
Indeed the far integral is at most
3e^4 j!32^(j+1) S^(-j-1/2), no larger than the claimed bound for S>=1.
These are constants depending only on j,B, not on k,T,H or parity.

For a fully rational perturbation budget take B=1. Since
t<=t^2/32+8, e<3 and pi<4,
\[
 \int_0^\infty t e^{-t^2/32}dt=16,\qquad
 \int_0^\infty t^2e^{-t^2/32}dt<96.
\]
Thus (HD5) holds for j=1,2 with the explicit, nonoptimal constants
\[
 M_1=243(16\cdot3^8+32^2)=25758000,\quad
 M_2=243(96\cdot3^8+2\cdot32^3)=168980256.
\tag{HD11}
\]
These large constants are a proof reserve, not a claimed practical k threshold.

For the tail required by PR767, put
\[
 \mathfrak T_H(\delta)=\mathbb E\left[
 (1+U^2/a^2)e^{H|U-a|}\,1_{|U-a|>\delta}\right].
\]
There is an absolute finite C such that, whenever a>=2, S>=64 and
\[
 S^{-1/2}\le\delta\le1,\qquad 0\le H\le S\delta/32,
\]
one has
\[
 \boxed{\mathfrak T_H(\delta)\le C e^{-S\delta^2/64}.}
\tag{HD12}
\]
To see this, use 1+(1+s/a)^2<=3+s^2/2. On delta<=|s|<=1 the exponent is
at most -S s^2/32; on |s|>=1 it is at most -S|s|/32. Scaling the first
integral and using the elementary Gaussian tail bound gives
C exp(-S delta^2/64). The second integral is at most
C S^(-1/2)exp(-S/32), bounded by the same expression since delta<=1.
Thus no exterior weighted tail is left uncontrolled.

## 4. Normalized F,F',F'' comparison and Rouché on enlarged disks

Let theta=k pi/2 and G(z)=cos(az-theta). For y=Im z, the mean value formula
for sine and cosine, along the real frequency segment from a to U, gives
\[
 e^{-a|y|}|F_k(z)-G(z)|\le |z|\,\mathbb E|U-a|e^{|y||U-a|},
\]
\[
 e^{-a|y|}\frac{|F_k'(z)+a\sin(az-\theta)|}{a}
 \le(|z|+a^{-1})\mathbb E|U-a|e^{|y||U-a|},
\]
\[
 e^{-a|y|}\frac{|F_k''(z)+a^2G(z)|}{a^2}
 \le(|z|+2a^{-1})\mathbb E|U-a|e^{|y||U-a|}
       +a^{-2}\mathbb E|U-a|^2e^{|y||U-a|}.
\tag{HD13}
\]
For the second and third lines, split U-a or U^2-a^2 before taking absolute
values. No complex contour deformation or Gaussian replacement is used.

Fix T,H>=0. Put r=1/(4a), H_*=max(H,r), R=T+2r+H_*. For each real zero
z_j of G with |z_j|<=T+r, use the FULL disk D_j={|z-z_j|<r}.
These are exactly the comparison disks whose closures can meet the real
horizontal range of the rectangle. Their union and the rectangle have
|z|<=R and |Im z|<=H_*. In particular the horizontal enlargement T+2r
and the height H_* are both retained.

On every disk boundary and outside their union in the rectangle,
\[
 |G(z)|\ge1/(2\pi)>1/8,\qquad
 e^{a|y|}\le1+2|G(z)|,\qquad
 \boxed{e^{-a|y|}|G(z)|\ge1/10.}
\tag{HD14}
\]
For the first bound, select the nearest real comparison zero, write its
scaled displacement as x+iv with |x|<=pi/2, and use
|sin(x+iv)|^2=sin^2 x+sinh^2 v>=(4/pi^2)(x^2+v^2).
Outside a radius-r disk, x^2+v^2>=1/16. The exponential bound follows from
|G|>=sinh(a|y|). These arguments cover the full complex boundary, not just
separate real and imaginary cases.

If a>=2, S>=1024 and H_*<=sqrt(S), (HD11)--(HD13) imply the finite bounds
\[
 e_0=M_1\rho,\quad e_1=M_1(\rho+\alpha),\quad
 e_2=M_1(\rho+2\alpha)+M_2\alpha^2,
 \quad\rho=R/\sqrt S,\quad\alpha=1/(a\sqrt S).
\tag{HD15}
\]
In particular e_0<1/10 is a sufficient strict Rouché condition. It yields
exactly one zero, counted with multiplicity, in every D_j and no zeros
outside these disks in the rectangle. The disks are disjoint; each is
conjugation invariant. Reality of F_k on the real axis and uniqueness
force each counted zero to be real and simple.

There is NO assertion that the count inside the closed rectangle equals
the number of comparison zeros inside that same rectangle: a disk crossing
Re z=+/-T permits its zero to move across the endpoint. The disk assignment
and order are exact; an endpoint count needs an additional boundary margin.

For real t put A=F_k, B_0=-F_k'/a, C_0=-F_k''/a^2. Their reference values
are cos(at-theta), sin(at-theta), cos(at-theta). If the three errors are
bounded by e_0,e_1,e_2, respectively, then
\[
 \left|\frac{F_k'^2-F_kF_k''}{a^2}-1\right|
 \le e_1(2+e_1)+e_0(1+e_2)+e_2.
\tag{HD16}
\]
For example e_0,e_1,e_2<=1/32 leave reserve >=447/512>1/2.
Under (HD6), rho and alpha tend to zero and H_*<=sqrt(S) eventually,
so (HD14)--(HD16) prove every assertion of the theorem. The same proof
also supplies an absolute small-c, sufficiently-large-k version with
T+H+a^(-1)<=c sqrt(S); no numerical value of the practical cutoff is claimed.

## 5. Gaussian limit and what a fixed-width tail actually does

This section is a separately proved control, not the load-bearing argument
for (HD13)--(HD16). Taylor expansion of (HD8), with s=sigma x, gives
\[
 \ell(a+\sigma x)-\ell(a)\longrightarrow-x^2/2
\]
uniformly on bounded x sets: Lambda=-ell''(a), while ell'''=O(S) locally
and S sigma^3=O(S^(-1/2)). By (HD7) the theta multiplier tends to its
first-orbit constant on the same sets. To justify normalization without
circularity, use the UNNORMALIZED bound from (HD8). For a>=2, S>=64,
64/169<=S sigma^2<=1/2 and S sigma>=64/13. The rescaled unnormalized
integrand, divided by 8pi^2 q_k(a), is dominated by
(3/2)[exp(-4x^2/169)+exp(-4|x|/13)], extended by zero when a+sigma x<=0.
This is an integrable majorant. Dominated convergence proves the
normalization asymptotic and then the probability limit. Hence
\[
 (U-a)/\sigma\ \Longrightarrow\ Z\sim N(0,1),\qquad
 Z_k\sim8\pi^2q_k(a)\sigma\sqrt{2\pi}.
\tag{HD17}
\]
The same split proves uniform integrability of every fixed polynomial
times exp(B|(U-a)/sigma|), for each fixed B. One can alternatively use
(HD5) at twice the exponential weight and a higher polynomial moment.
Since sigma/a tends to zero, for fixed C>0 and any H_k>=0 with
H_k sigma_k tending to h>=0,
\[
 \boxed{\mathfrak T_{H_k}(C\sigma_k)
 \longrightarrow4e^{h^2/2}\,\overline\Phi(C-h)>0,}
\tag{HD18}
\]
where overline(Phi) is the standard normal upper tail. The factor four
comes from the weight 1+U^2/a^2 tending to two and the two Gaussian tails.
This strictly positive limit rules out exponential decay in k at fixed C.

Nevertheless, if H_*sigma tends to zero, the choice delta=4sigma gives
\[
 \lim\mathfrak T_{H_*}(4\sigma)=4\overline\Phi(4)
 \le e^{-8}/\sqrt{2\pi}<1/256.
\tag{HD19}
\]
The displayed tail bound follows by integrating x e^(-x^2/2)/4 on x>=4;
e>2 makes the last strict inequality immediate. Thus a fixed four-standard-
deviation window eventually meets a small fixed perturbative threshold.

If a vanishing tail is desired, choose delta=A_k/sqrt(S), A_k tending to
infinity, A_k<=sqrt(S); then (HD12) gives C exp(-A_k^2/64) provided
H<=A_k sqrt(S)/32. Polynomially small tails follow from
A_k=D sqrt(log S); the corresponding phase window is T+H=o(sqrt(S/log S)),
of order o(sqrt(k)/log k). A slowly growing A_k gives a smaller loss.
These are different contracts from a small FIXED tail. An exponentially
small-in-k tail with delta comparable to sigma is impossible by (HD18).

## 6. Repairing the inherited full-disk tail contract

L-107102 at the pinned PR767 SHA, lines 155--167, weights tails only to H
but inherits full disks of radius r=1/(4u_0), lines 121--130. This is false
when H<r. Here is an exact family counterexample, not Xi data.

Take u_0=1, theta=0, T=2, H=1/8 and R congruent to 3 mod 4. For any c>0
put epsilon=c exp[-H(R-1)]/(1+R^2) and
nu=(1-epsilon) delta_1+epsilon delta_R. Choose the concentration half-width
delta>0 arbitrarily small. Its normalized core is the point mass at one,
and its weighted tail is exactly c. At z_0=pi/2,
\[
 F(z_0+iy)=-i[(1-\epsilon)\sinh y-\epsilon\sinh(Ry)].
\tag{HD20}
\]
For sufficiently large R the bracket has positive derivative at zero,
but is negative at y=1/4, because the exponent (1/4-H)R defeats R^2.
There is therefore an additional conjugate pair INSIDE the promised disk,
as well as its central simple zero. The measure has compact support, so
entire-function regularity cannot resolve this counterexample.

A bounded exact control uses R=511 and c=2^(-20). Since sinh(R/4)>
e^(R/4)/4 and e>2,
epsilon sinh(R/4)>2^44/[4(1+511^2)]>1, whereas sinh(1/4)<1.
Also epsilon(1+R)<c, so the central derivative is nonzero. The checker
verifies these rational/integer inequalities, not sampled hyperbolic values.

A sufficient repaired source-independent contract retains the hypothesis
that F is holomorphic on a neighbourhood of
the closed rectangle and full disks (in particular when F is entire).
A finite exponential moment at only one height does not itself imply
entireness. The actual theta kernel already supplies entireness above.
The quantitative conditions are
\[
 \eta=\delta/u_0\le1/32,\quad
 \delta(T+H+u_0^{-1})e^{\delta H}\le1/256,\quad
 \boxed{\mathfrak T_{H_*}\le1/256,\qquad
 H_* =\max(H,1/(4u_0)).}
\tag{HD21}
\]
For points on the needed rectangle and FULL disks, |z|<=T+H+u_0^(-1).
Comparing the full measure to the point mass directly gives
\[
 e^{-u_0|y|}|F-G|
 \le\delta|z|e^{\delta H_*}+2\mathfrak T_{H_*}\le1/64,
\]
because exp[delta(H_*-H)]<=exp(eta/4)<2. This is below the 1/10 reserve
in (HD14). Real derivative comparisons also retain Laguerre reserve:
the errors in A,B,C are bounded by q+2tau, eta+q+2tau, 3eta+q+tau,
where q=|t|delta and tau=mathfrak(T)_(H_*). For eta,q<=1/32 and
tau<=1/256, the resulting loss is at most 6eta+6q+11tau<2/3.
Hence the advertised u_0^2/3 lower bound is valid under this repair.

These are fixed absolute thresholds. The heading 'exponentially small tails'
and T-107110 line 93 demand more than this proof needs. Applying (HD19),
delta=4sigma, and (HD6) satisfies (HD21) for all sufficiently large k.
For fixed positive H the H_* correction eventually disappears, but it must
be retained for statements uniform in small or zero H.

## 7. Prior art, exact replay, and the remaining earlier-work frontier

Cosine universality under repeated Xi differentiation is classical, not a
novelty claim of this packet. See Haseo Ki, *The Riemann Xi-function under
repeated differentiation*, J. Number Theory 120 (2006), 120--131:
[publisher record](https://www.sciencedirect.com/science/article/pii/S0022314X05002489).
The verified primary abstract states compact convergence after scaling.
Gunns and Hughes, *The effect of repeated differentiation on L-functions*,
J. Number Theory 194 (2019), 30--43, give an extended-Selberg version:
[accepted primary manuscript](https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf),
Theorem 3.1, pp.10--11. Its positive-direction asymptotic and saddle equation
are closely related; its printed compact-domain statement is not silently
substituted for the growing-domain estimates proved here. No claim that
these growing-domain bounds are absent from the wider literature is made.

The useful programme contribution is an explicit actual-source proof and
repair of the precise earlier endpoint gate. It uses only the real theta
bounds and elementary Laplace estimates; old moving-contour claims are not
dependencies. Fixed H=1/2 and k/(T^2 log T) tending to infinity (for T tending
to infinity) fit (HD6), but no universal count is asserted at the endpoints.

The producer uses exact integer/Fraction algebra only. Its saddle-coordinate
panels do not pretend rational a,S are actual transcendental saddle samples.
It checks the exact logratio Taylor coefficients independently against
derivatives, the curvature constants, the explicit moment majorants,
finite F/F'/F'' and Rouché/Laguerre budgets, Gaussian moment recurrences,
and the full-disk countercontrol. Raw types, order, bit-size, coverage, and
source contracts fail closed. No assertion disappears under Python -O.

Every immutable repository input is bound by commit, Git blob, and
LF-normalized SHA-256. The fixture binds the note, producer, test, and
manifest. Complete typed canonical-JSON equality to a fresh rebuild is
required. External citation contracts are authenticated as metadata, not
remote bytes. Finite checks do not certify the unbounded analytic theorem.

Replay commands:
```text
python research/exploratory/xi_high_derivative_saddle_closure.py --check
python -O research/exploratory/xi_high_derivative_saddle_closure.py --check
python -m unittest discover -s tests -p test_xi_high_derivative_saddle_closure.py
python -O -m unittest discover -s tests -p test_xi_high_derivative_saddle_closure.py
```

Author replay: both producer modes and all 33 new tests passed. The adjacent
Hardy-translation (33) and actual-Xi-kernel (15) tests also passed in both
modes, 48 adjacent tests per mode; their producers passed in both modes.
Ruff lint/format and diff checks passed. These finite results do not replace
independent frozen-code and analytic-proof review.

The frozen T-107100 cascade still charges every rung's nonnegative defect
and its endpoint index. R-107100's polynomial counterexamples remain valid.
This packet supplies no bound on sum_(j<k) R_j, no actual-Xi curvature
transport, no source-Pick congruence, and no low-order RH conclusion.
XICURV107110 and all descent/RH claims remain OPEN.
