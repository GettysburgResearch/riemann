# Native Xi companion zeros and sampling on the positive imaginary axis

Status: PROPOSED ACTUAL-SOURCE ANALYTIC RESULT; independent exact-SHA review required.
The axis statements below are unconditional. Inner-factor and physical-operator
interpretations explicitly assume the existing two-component inner premise
(in particular RH suffices). No RH conclusion is claimed.
Parents are preserved; the authoring base is frozen CP at
7aed2ec0b99b9d7f2fb94a774922a83d5b84a870. Six literal source bindings accompany
the finite checker. This is not a numerical zero-location certificate.

## 1. Actual source and statement

Use the standard, unrescaled normalization of XL1--XL4 and GH1:
\[
 f(z)=\Xi(z)=\int_{\mathbb R}\Phi(u)e^{izu}\,du,\qquad
 h(y)=f(iy)=\int_{\mathbb R}\Phi(u)e^{yu}\,du .
 \tag{AX1}
\]
The actual kernel is positive, even and superexponentially decreasing; it is
twice the historical kernel called phi_0. All its moments and exponentially
tilted moments are finite. Put \(\mu_r=h^{(r)}(0)\); odd moments vanish and
every even moment is strictly positive. For y>0 all h derivatives are positive.
For a constant lambda>0 define
\[
 C_k=f^{(k)}+i\lambda f^{(k+1)},\quad
 R_k=f^{(k)}-i\lambda f^{(k+1)},\quad
 \Theta_k=R_k/C_k,\quad
 D_0=h'/h,\quad D_5=h^{(6)}/h^{(5)}.
 \tag{AX2}
\]
The exact phases are \(f^{(r)}(iy)=(-i)^r h^{(r)}(y)\), so
\[
 \Theta_k(iy)=\frac{1-\lambda D_k(y)}{1+\lambda D_k(y)}
 \quad(k=0,5).                                           \tag{AX3}
\]
The denominators here never vanish for y>0, independently of RH.

There is exactly one positive number y_0(lambda) with D_0(y_0)=1/lambda,
and iy_0 is a simple zero of Theta_0. There is a unique y_*>0 minimizing D_5.
Set \(m=D_5(y_*)>0\) and \(\lambda_*=1/m\). The positive-axis zeros of Theta_5
have exactly this classification:

| lambda | Zeros on i(0,infinity), with complex-analytic multiplicity |
| --- | --- |
| 0<lambda<lambda_* | two simple zeros iy_5^-(lambda), iy_5^+(lambda) |
| lambda=lambda_* | one double zero iy_* |
| lambda>lambda_* | none |

Every such zero iy satisfies
\[
 \lambda<y<y_0(\lambda),\qquad \Theta_0(iy)>0.              \tag{AX4}
\]
In particular there is NO common positive-imaginary-axis zero.
No numerical value or explicit rational enclosure for lambda_* is asserted.

Under the existing inner premise, GH makes both components pure Blaschke
products. Write \(\Theta_0=G U,\ \Theta_5=G B\), where G is their maximal
common inner divisor. The native ratio is U/B=Theta_0/Theta_5, exactly the
frozen L-106620.4--.6 source, not a substituted rational example.
G has no positive-axis zero; every zero counted above survives in B with
the same multiplicity, and
\[
 |U(iy)|=|\Theta_0(iy)|/|G(iy)|\ge\Theta_0(iy)>0.           \tag{AX5}
\]
Dividing by G can INCREASE the sampled numerator modulus.

## 2. Positive covariance and the no-common-zero conclusion

The probability density \(\Phi(u)e^{yu}/h(y)\) has full real support.
Differentiating its mean gives D_0'=Var_y(u)>0. Also D_0(0)=0 and
D_0(y) tends to infinity by the source-bound GH10 asymptotic
\[
 D_0(y)=\tfrac12\log(y/(2\pi))+O(y^{-1}),\quad
 D_0'(y)=1/(2y)+O(y^{-2}).                               \tag{AX6}
\]
This proves the claimed unique simple y_0.

Let \(K(y)=h h^{(6)}-h'h^{(5)}\). Symmetrization and evenness give
\[
 K(y)=\frac12\iint_{\mathbb R^2}
 (u-v)(u^5-v^5)\Phi(u)\Phi(v)\cosh(y(u+v))\,du\,dv
 \ge \mu_0\mu_6>0.                                      \tag{AX7}
\]
The polynomial factor is nonnegative, and positive off the diagonal,
because the fifth power is strictly increasing. Superexponential decay
justifies differentiation, changes of variables and Fubini here and below
on every compact y interval. Thus D_5-D_0=K/(h h^(5))>0 for y>0.
Also y h^(6)>h^(5), by \(yu\cosh(yu)>\sinh(yu)\) for u>0.
These facts prove AX4. At a Theta_5 zero,
\[
 \Theta_0(iy)=
 \frac{h h^{(6)}-h'h^{(5)}}{h h^{(6)}+h'h^{(5)}}
 >\frac{\mu_0\mu_6}{2h(y_0)h^{(6)}(y_0)}>0.              \tag{AX8}
\]
The last bound uses y<y_0, positivity and strict increase of the h derivatives.
It is a fixed-lambda lower bound for the finite axis sector, not a bound
uniform in lambda or on an infinite off-axis sequence.

## 3. Exactly one minimum of D_5

Write \(g=h^{(5)}=\int_0^\infty a(u)\sinh(yu)\,du\),
where \(a(u)=2u^5\Phi(u)>0\), and \(H=gg''-(g')^2\). Then
\[
 D_5'=H/g^2,\qquad H(0)=-\mu_6^2<0.                     \tag{AX9}
\]
The exact symmetrized integrand for H on the FULL positive quadrant is
\[
 H(y)=\iint a(u)a(v)Q_{u,v}(y)\,du\,dv,\quad
 Q_{u,v}(y)=\tfrac14\{(u-v)^2\cosh((u+v)y)
                    -(u+v)^2\cosh((u-v)y)\}.             \tag{AX10}
\]
The factor is 1/4 for this full-quadrant formula, or 1/2 if one integrates
only u>v. This distinction includes the negative constant term correctly.
For u,v>0 distinct, put A=u+v and c=|u-v|, so 0<c<A. Then
\[
 Q'_{u,v}(y)=\tfrac14 A c
       \{c\sinh(Ay)-A\sinh(cy)\}>0\quad(y>0),             \tag{AX11}
\]
because sinh(ty)/t is strictly increasing for t>0. For u=v this derivative
is zero. Consequently H'(y)>0 for y>0. There is no subtraction of
uncontrolled infinite integrals: H and H' are absolutely integrable on
compact y intervals, and \(Q_{u,v}(y)-Q_{u,v}(0)\ge0\).
On the compact separated rectangle u in [1,2], v in [3,4],
Q(y)-Q(0) tends to infinity uniformly. Indeed A-c=2min(u,v)>=2, and the
positive cosh(Ay) term exponentially dominates the negative cosh(cy) term
uniformly there. Its a(u)a(v) integral is strictly positive.
Thus H(y)=H(0)+integral a(u)a(v)(Q(y)-Q(0)) tends to infinity.

There is exactly one y_*>0 with H(y_*)=0, and H'(y_*)>0.
Near zero, D_5=1/y+O(y), and at infinity D_5 tends to infinity by GH13.
Hence y_* is the unique, nondegenerate global minimum. The level 1/lambda
therefore has the stated two/simple, one/double or zero solutions.
At the minimum \(D_5''=H'/g^2>0\), so AX3 has a zero of exact order two.
Restriction to the analytic curve z=iy preserves zero multiplicity,
proving the complex-analytic classification, not only a sign-change count.

## 4. The two lambda-to-zero branches have opposite raw sampling behavior

All limits in this section concern ONE fixed actual Xi function while its
constant parameter lambda tends to zero. No simultaneous physical T limit,
window retention or frequency identification is used.
Taylor expansion at zero gives
\[
 D_5(y)=y^{-1}+\frac{\mu_8}{3\mu_6}y+O(y^3),\qquad
 D_0(y)=\frac{\mu_2}{\mu_0}y+O(y^3).
 \tag{AX12}
\]
The reciprocal 1/D_5=g/g' is analytic odd near zero with derivative one.
The analytic inverse-function theorem therefore supplies the smaller branch:
\[
 y_5^-(\lambda)=\lambda+\frac{\mu_8}{3\mu_6}\lambda^3+O(\lambda^5),
 \quad
 \Theta_0(iy_5^-)=1-2\frac{\mu_2}{\mu_0}\lambda^2+O(\lambda^4).
 \tag{AX13}
\]
Existence of the two branches for sufficiently small lambda also follows
from Section 3. Neither moment ratio is numerically substituted.

For the larger branch let y=y_5^+(lambda). GH10--GH13 supply
\[
 D_5-D_0\sim\frac5{y\log y},\qquad
 D_5(y)=\tfrac12\log(y/(2\pi))+O(y^{-1}).
 \tag{AX14}
\]
The latter error follows by adding the former to AX6. Both y and y_0 tend
to infinity. Inverting the displayed estimate at level 1/lambda first gives
y/(2pi exp(2/lambda)) tending to one, then
\[
 y_5^+=2\pi e^{2/\lambda}+O(1),\qquad
 y_0=2\pi e^{2/\lambda}+O(1).                             \tag{AX15}
\]
For clarity, the logarithmic equation has error O(1/y); after the first
ratio limit, exponentiating shows the additive O(1) bound. No differentiation
of an unspecified asymptotic remainder occurs.
The mean value theorem applied to D_0 between y and y_0 now gives
\[
 y_0-y_5^+\sim\frac{10}{\log y_5^+}\sim5\lambda.           \tag{AX16}
\]
Indeed both endpoints differ by O(1) and are asymptotic to the same
exponential scale, so AX6's derivative estimate applies uniformly throughout
that interval. At the larger root, AX3 and D_5=1/lambda give
\[
 \Theta_0(iy_5^+)
 =\frac{\lambda(D_5-D_0)}{2-\lambda(D_5-D_0)}
 \sim\frac{5\lambda}{2y_5^+\log y_5^+}
 \sim\frac5{y_5^+(\log y_5^+)^2}\longrightarrow0.          \tag{AX17}
\]
These are RAW Theta_0 samples. AX5 prevents turning AX17 into an upper
bound tending to zero for the reduced U. Off-axis common factors can change
|G(iy)| even though G has no axis zeros.

## 5. A genuine global physical lower bound, and its geographic limitation

Assume the two-component inner premise for each lambda considered; RH is
a sufficient single premise for this family. Use the corrected IW/CP
physical source \(P_U=P_{UH^2}=M_U M_U^*\), not multiplication M_U alone
and not projection onto K_U. The normalized Hardy kernel at any zero b of
B lies in K_B and satisfies
\[
 P_Ue_b=\overline{U(b)}\,Ue_b,\qquad \|P_Ue_b\|^2=|U(b)|^2.
 \tag{AX18}
\]
Applying this to the surviving small-axis zero b=i y_5^- yields
\[
 1\ge\|P_UP_{K_B}\|_{\rm op}\ge|U(b)|\ge\Theta_0(b)
       =1-2(\mu_2/\mu_0)\lambda^2+O(\lambda^4).
 \tag{AX19}
\]
Thus the global operator norm tends to one as lambda tends to zero.
The global corrected squared Hilbert--Schmidt norm, interpreted in
[0,infinity], is at least the squared value of this ONE unit vector:
\[
 \|P_UP_{K_B}\|_{\mathcal S_2}^2
 \ge 1-4(\mu_2/\mu_0)\lambda^2+O(\lambda^4).               \tag{AX20}
\]
An inequality with O here means that some constant bounds the error in
absolute value for all sufficiently small positive lambda.
In particular CP's synthetic global bound <1/9 cannot hold uniformly for
this actual global family as lambda tends to zero.

This is not a divergent-charge theorem: one direction does not supply a
summable family or an infinite trace. It does not lower-bound every Fourier
band. The small-axis direction has real part zero and is NOT a retained
high-T mesoscopic geographic direction in T-106620's [T,2T] windows.
No native high-T local capture, physical-T uniformity, normalized total
charge, common-factor classification off the axis, Riesz/interpolation
bound, confluent-jet ledger or cofinal/free-energy conclusion follows.

For an exact source bridge let \(W=f f^{(6)}-f'f^{(5)}\). Frozen lambda gives
\[
 R_5=R_0^{(5)},\quad
 \Theta_0-\Theta_5=\frac{2i\lambda W}{C_0C_5},\quad
 U-B=\frac{2i\lambda W}{G C_0C_5}.                        \tag{AX21}
\]
The last quotient is interpreted after removable cancellations.
At a reduced denominator zero of multiplicity q, its Taylor coefficients
through order q-1 are exactly those of U. The corrected physical coefficient
matrix is the ADJOINT of these value jets, with IW's retained outer metric.
They are not freely selectable scalar samples. The positive kernel proof
only controls W on the imaginary axis; at other points its Fourier
integral is oscillatory. That is the first remaining native sampling gate.

## 6. Bounded verification and source boundaries

The producer certifies finite rational Taylor identities for the full
quadrant kernel AX10, positive even finite-measure covariance, the Laurent
normalization y D_5, series inversion for AX13, and the raw small-branch
sample and its square. Finite atomic measures are explicitly NONNATIVE
algebra controls, never substitutes for Phi or a proof of any analytic limit.
Large-branch constants are checked as exact leading-coefficient arithmetic,
not by logarithm, exponential, Xi or zero samples. The axis theorem and the
all-y sign arguments are proved above for the actual kernel, not inferred
from the bounded panel. Arithmetic is MIXED: EXACT_RATIONAL plus
CERTIFIED_INTEGER_COVERAGE.

Public scalar/atom rationals have 16-bit numerator/denominator caps;
working polynomial coefficients and internal rationals have 4096-bit caps.
There are at most four positive distinct atoms, series degree at most
20, Taylor cutoff at most eight, charged work at most 200000, and UTF-8 input
at most 2000000 bytes. Strict types, duplicate/nonfinite JSON rejection,
complete typed reconstruction, six frozen primitive identities, four artifact
seals and the payload seal are mandatory, including under Python -O.
All arithmetic uses integers and Fraction, with no rounding and no
transcendental or actual-Xi numerical evaluation.
The note/test bytes are scanned for prohibited control characters.

The six pinned notes are GH (phases and differentiated asymptotics),
XL (actual positive kernel), IW (adjoint source), L-106620 (constant scale),
T-106620 (native ratio and geographic limitation), and CP (synthetic
countercontrol and corrected global operator). All were personally read.
No historical raw-value source convention or finite-height premise is
silently imported. The classical normalization/reflection and differentiated
gamma contracts were checked against [DLMF 25.4.3--4](https://dlmf.nist.gov/25.4),
[5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.15.9](https://dlmf.nist.gov/5.15.E9); remote bytes are not authenticated
by the offline checker. No exhaustive novelty search or new general
Hardy-space principle is claimed.

The 32 tests use independent direct hyperbolic convolution, the full signed
double-moment covariance, Lagrange coefficient reversion, and a one-atom
closed-form coefficient control. They also attack source/artifact bindings,
quarter-factor and branch constants, bool/int substitutions, caps, and
resealed scope changes. These are author-team finite replays, not an
independent exact-SHA acceptance of the analytic theorem.

Replay entrypoints:

    python -B -m unittest discover -s tests -p test_xi_companion_imaginary_axis_sampling.py
    python -B -O -m unittest discover -s tests -p test_xi_companion_imaginary_axis_sampling.py
    python -B research/exploratory/xi_companion_imaginary_axis_sampling.py --check
    python -B -O research/exploratory/xi_companion_imaginary_axis_sampling.py --check

Smallest result-invalidating burden: the factor and sign in AX10--AX11,
strict covariance AX7, or the source asymptotic inversion AX15--AX17.
Smallest remaining native burden: reduced off-axis numerator/jet control
in the retained physical geometry. RH remains open.
