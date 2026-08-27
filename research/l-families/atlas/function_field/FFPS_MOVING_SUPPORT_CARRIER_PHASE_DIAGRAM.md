# Width-renormalized carrier energy is RH-exact at every support scale

Status: **sharp carrier moment inequality, all-support
width-renormalized parabolic RH criterion, raw-energy zero-free wedge,
moving-BV forward theorem, explicit Young dilution bound, and exact
normalization repair; no beta-energy estimate, proof of RH, or GRH
result**

Bounded replay:
[ffps_moving_support_carrier_phase_diagram.py](ffps_moving_support_carrier_phase_diagram.py).
Canonical summary:
[ffps_moving_support_carrier_phase_diagram.json](ffps_moving_support_carrier_phase_diagram.json).

Frozen source: the variational probability-carrier optimum at commit
**19f274c9335ecffb357e296b3fd5fefdeba5f3fd**. The producer pins all
four Git blobs and imports no live predecessor module.

## 0. Outcome

For every horizon \(X\), let \(Q_X\) be a compactly supported,
integrable real function on \([0,S_X]\) with

\[
 \int_{\mathbb R}Q_X(u)\,du=1.
\tag{0.1}
\]

The reverse theorem does not require \(Q_X\ge0\). Extend \(Q_X\) by
zero, take its distributional derivative

\[
 J_X=DQ_X,
\tag{0.2}
\]

and assume that \(J_X\) is represented by an \(L^2\) function. For the
complete beta source

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\tag{0.3}
\]

define

\[
\begin{aligned}
 H_X(t)
 &=
 \sum_{n\le X}{\beta(n)\over\sqrt n}
 J_X(t-\log n),\\
 \mathcal E_Q(X)
 &=\int_{\mathbb R}|H_X(t)|^2\,dt,\\
 B(X)
 &=\sum_{n\le X}{\beta(n)\over\sqrt n}.
\end{aligned}
\tag{0.4}
\]

The central discovery is the sharp support-energy inequality

\[
\boxed{
 \mathcal E_Q(X)\bigl(\log X+S_X\bigr)^3
 \ge 12\,|B(X)|^2.}
\tag{0.5}
\]

It follows only from two exact moment identities:

\[
 \int H_X(t)\,dt=0,
 \qquad
 \int tH_X(t)\,dt=-B(X).
\tag{0.6}
\]

No positivity, Fourier nonvanishing, or fixed carrier shape is used.
The constant \(12\) is optimal from support, total mass, first moment,
and \(L^2\) information alone.

Put

\[
 L_X=\log X+S_X,
 \qquad
 \mathfrak R_Q(X)=L_X^3\mathcal E_Q(X).
\tag{0.R1}
\]

The sharp inequality immediately gives the support-independent reverse
theorem

\[
\boxed{
 \mathfrak R_Q(X)=X^{o(1)}
 \quad\Longrightarrow\quad \mathrm{RH}.}
\tag{0.R2}
\]

The support may grow arbitrarily fast. Under RH, the sufficient
forward gate for this renormalized energy is

\[
 L_X^4
 \left(
 \|J_X\|_\infty+\operatorname {Var}(J_X)
 \right)^2
 =X^{o(1)}.
\tag{0.R3}
\]

For the parabolic carrier below, (0.R3) holds for **every** schedule
\(S_X\ge1\). Consequently,

\[
\boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \bigl(\log X+S_X\bigr)^3\mathcal E_{S_X}(X)
 =X^{o(1)}
 \quad(S_X\ge1).}
\tag{0.R4}
\]

This is the strongest support-uniform theorem in the packet. The raw,
unrenormalized energy retains the following useful phase diagram.

Suppose, for one fixed \(\gamma\ge0\) and uniformly at all sufficiently
large horizons,

\[
 S_X\le X^{\gamma+o(1)},
 \qquad
 \mathcal E_Q(X)=X^{o(1)}.
\tag{0.7}
\]

Then

\[
\boxed{
 \zeta(\rho)=0
 \quad\Longrightarrow\quad
 \Re\rho\le {1\over2}+{3\gamma\over2}.}
\tag{0.8}
\]

The functional equation excludes the reflected symmetric wedge. In
particular,

\[
\boxed{
 S_X=X^{o(1)},\qquad
 \mathcal E_Q(X)=X^{o(1)}
 \quad\Longrightarrow\quad \mathrm{RH}.}
\tag{0.9}
\]

Here \(X^{o(1)}\) has its standard uniform meaning: for every
\(\varepsilon>0\), the quantity is
\(O_\varepsilon(X^\varepsilon)\) for all sufficiently large \(X\).
Unlike the preliminary moving-Laplace proof, (0.5) needs no monotone
upper envelope for a fluctuating support schedule.

Conversely, the exact sufficient forward gate for the raw energy is

\[
 \bigl(\log X+S_X\bigr)
 \left(
 \|J_X\|_\infty+\operatorname {Var}(J_X)
 \right)^2
 =X^{o(1)}.
\tag{0.10}
\]

If (0.10) holds, then

\[
\boxed{
 \mathrm{RH}
 \quad\Longrightarrow\quad
 \mathcal E_Q(X)=X^{o(1)}.}
\tag{0.11}
\]

Separate subpower bounds on \(S_X\) and the BV cost imply (0.10), but
are not necessary. Every uniformly subpower normalized derivative
family satisfying this raw forward gate gives an exact raw-energy RH
criterion. Its multiplicative ratio band may be as wide as
\(\exp(X^{o(1)})\).

For the variational parabolic carrier

\[
 Q_S(x)={6x(S-x)\over S^3}\mathbf1_{[0,S]}(x),
 \qquad J_S=DQ_S,
\tag{0.12}
\]

one also has the unconditional source-size estimate

\[
\boxed{
 \mathcal E_S(X)\le {192X\over S^3}.}
\tag{0.13}
\]

The zero-free boundary supplied by (0.8) and the trivial-energy
boundary supplied by (0.13) meet at the same exponent:

| support scale | consequence of subpower energy |
|---|---|
| \(X^{o(1)}\) | RH |
| \(X^{\gamma+o(1)},\ 0<\gamma<1/3\) | no zero with \(\Re\rho>1/2+3\gamma/2\) |
| \(X^{1/3+o(1)}\) | wedge reaches \(\Re\rho=1\), while (0.13) becomes subpower trivially |

For \(\gamma\ge1/3\), the wedge is vacuous relative to the classical
zero-free half-plane. The cubic meeting does **not** prove RH. It
locates the exact meeting of a sharp moment-recovery law and an
elementary dilution law. The renormalization (0.R1) removes this
escape by charging exactly for the enlarged support.

## 1. Exact carrier moments

Compact support and the zero-extended distributional derivative give

\[
 \int_{\mathbb R}J_X(u)\,du=0.
\tag{1.1}
\]

Distributional integration by parts and (0.1) give

\[
 \int_{\mathbb R}uJ_X(u)\,du
 =-\int_{\mathbb R}Q_X(u)\,du
 =-1.
\tag{1.2}
\]

For each shifted packet,

\[
\begin{aligned}
 \int_{\mathbb R}J_X(t-\log n)\,dt&=0,\\
 \int_{\mathbb R}tJ_X(t-\log n)\,dt
 &=\int_{\mathbb R}(u+\log n)J_X(u)\,du\\
 &=-1.
\end{aligned}
\tag{1.3}
\]

Finite summation proves (0.6). The logarithmic location of each beta
atom disappears because it multiplies the zero mode (1.1). This is
the exact source-recovery mechanism.

The field \(H_X\) is supported inside

\[
 [0,L_X],
 \qquad
 L_X=\log X+S_X.
\tag{1.4}
\]

Since \(\int H_X=0\), its first moment may be centered at any real
number \(c\):

\[
 B(X)=-\int_0^{L_X}(t-c)H_X(t)\,dt.
\tag{1.5}
\]

The \(L^2[0,L_X]\)-optimal center is \(c=L_X/2\), for which

\[
 \int_0^{L_X}\left(t-{L_X\over2}\right)^2dt
 ={L_X^3\over12}.
\tag{1.6}
\]

Cauchy--Schwarz in (1.5) now gives (0.5).

## 2. Sharpness and the dual extremizer

Among all \(H\in L^2[0,L]\) satisfying

\[
 \int_0^L H(t)\,dt=0,
 \qquad
 \int_0^L tH(t)\,dt=-B,
\tag{2.1}
\]

orthogonal projection onto the span of \(1\) and \(t\) gives the exact
minimum

\[
\boxed{
 \|H\|_2^2\ge {12|B|^2\over L^3}.}
\tag{2.2}
\]

Equality holds exactly for

\[
 H_*(t)={6B(L-2t)\over L^3}.
\tag{2.3}
\]

More precisely, orthogonal projection gives the exact Pythagorean
decomposition

\[
\boxed{
 \|H\|_2^2
 ={12|B|^2\over L^3}
 +\|H-H_*\|_2^2.}
\tag{2.3a}
\]

For the beta field this becomes

\[
\boxed{
 \mathfrak R_Q(X)
 =12|B(X)|^2
 +L_X^3\|H_X-H_{X,*}\|_2^2.}
\tag{2.3b}
\]

The first term is the literal Mertens/RH signal. The second is a
nonnegative carrier-shape defect. Any direct proof of the
renormalized criterion must control both; any quotient that removes
the defect returns exactly to the classical beta-prefix problem.

For \(X=1\), one has \(\beta(1)=1\), \(B(1)=1\), and the parabolic
derivative \(J_L\) in (0.12) is precisely (2.3). Thus equality is
realized by an admissible one-atom carrier field. No universal
improvement of the exponent \(L^{3/2}\) or constant \(12\) can follow
from only the data in (2.1).

This is an information firewall, not a claim that every multi-atom
beta field saturates (2.2). Beating the \(3/2\) wedge slope requires
using additional arithmetic structure of the convolution, not a
stronger abstract support-moment inequality.

### Autocorrelation second moment

Define the signed field autocorrelation

\[
 \mathcal C_X(u)
 =\int_{\mathbb R}H_X(v)H_X(v+u)\,dv.
\tag{2.4}
\]

Finite support permits Fubini. Substituting \(w=v+u\) and using
(0.6) gives

\[
\begin{aligned}
 \int_{\mathbb R}u^2\mathcal C_X(u)\,du
 &=
 \iint_{\mathbb R^2}(w-v)^2H_X(v)H_X(w)\,dv\,dw\\
 &=-2\left(\int_{\mathbb R}tH_X(t)\,dt\right)^2\\
 &=-2B(X)^2.
\end{aligned}
\tag{2.5}
\]

Thus the arithmetic beta prefix is not merely bounded by the field:
its square is exactly the negative second moment of the signed
autocorrelation. This identity uses the complete coherent field, not
its positive spectral density or an absolute autocorrelation.

## 3. Zero-free wedge and RH criterion

Equation (0.5) may first be read without assigning a support exponent:

\[
 \mathfrak R_Q(X)\ge12|B(X)|^2.
\tag{3.0}
\]

Thus \(\mathfrak R_Q(X)=X^{o(1)}\) gives
\(B(X)=X^{o(1)}\). The argument below with \(\gamma=0\) then proves
RH. This is (0.R2), and it has no support-growth hypothesis.

For the raw-energy wedge, assume (0.7). Equations (0.5) and (0.7) give

\[
 B(X)
 =O_\varepsilon\!\left(
 X^{3\gamma/2+\varepsilon}
 \right)
\tag{3.1}
\]

for every \(\varepsilon>0\). Ordinary Abel summation shows that

\[
 F(s)=\sum_{n\ge1}{\beta(n)\over n^{1/2+s}}
\tag{3.2}
\]

converges locally uniformly and is holomorphic in

\[
 \Re s>{3\gamma\over2}.
\tag{3.3}
\]

In the original absolute-convergence half-plane,

\[
 F(s)
 ={1-67^{-(s+1/2)}\over\zeta(s+1/2)}.
\tag{3.4}
\]

Equivalently, after clearing the sole zeta pole,

\[
 (s-\tfrac12)\zeta(s+\tfrac12)F(s)
 =(s-\tfrac12)\bigl(1-67^{-(s+1/2)}\bigr).
\tag{3.5}
\]

The identity theorem continues (3.5) through (3.3). If a nontrivial
zero \(\rho\) satisfied

\[
 \Re\rho>{1\over2}+{3\gamma\over2},
 \qquad
 s_0=\rho-{1\over2},
\tag{3.6}
\]

then evaluation at \(s_0\) would force

\[
 0=1-67^{-\rho}.
\tag{3.7}
\]

This is impossible because \(\Re\rho>1/2\) implies
\(|67^{-\rho}|<1\). This proves (0.8). At \(\gamma=0\), reflection by
the zeta functional equation proves (0.9).

## 4. Projected Laplace replay

When \(Q_X\ge0\), positivity and unit mass also give, for
\(\alpha>0\),

\[
 \widehat J_X(\alpha)
 =\alpha\widehat Q_X(\alpha)
 \ge\alpha e^{-\alpha S_X}.
\tag{4.1}
\]

Set \(z=\alpha L_X\) and

\[
 V(z)
 ={1-e^{-2z}\over2z}
 -\left({1-e^{-z}\over z}\right)^2.
\tag{4.2}
\]

This is the variance of \(e^{-zU}\) for
\(U\sim\operatorname {Unif}[0,1]\). Since \(\int H_X=0\), first
project \(e^{-\alpha t}\) off the constants on \([0,L_X]\). Exact
Cauchy--Schwarz gives

\[
\boxed{
 \left|
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 \right|
 \le
 {\sqrt{L_XV(\alpha L_X)}
 \over\alpha\widehat Q_X(\alpha)}
 \mathcal E_Q(X)^{1/2}.}
\tag{4.3}
\]

Using (4.1) and either the centered Lipschitz variance bound or the
unprojected exponential norm gives

\[
 \left|
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 \right|
 \le
 e^{\alpha S_X}
 \min\left\{
 {L_X^{3/2}\over\sqrt{12}},
 {1\over\sqrt2\,\alpha^{3/2}}
 \right\}
 \mathcal E_Q(X)^{1/2}.
\tag{4.4}
\]

The older unprojected bound is the second branch:

\[
 \left|
 \sum_{n\le X}{\beta(n)\over n^{1/2+\alpha}}
 \right|
 \le
 {e^{\alpha S_X}\over\alpha\sqrt{2\alpha}}
 \mathcal E_Q(X)^{1/2}.
\tag{4.5}
\]

The factor in (4.5) is minimized at

\[
 \alpha={3\over2S_X},
\tag{4.6}
\]

with cost

\[
 {e^{3/2}\over\sqrt2}\left({2S_X\over3}\right)^{3/2}.
\tag{4.7}
\]

A dyadic moving-tilt argument recovers the same exponent
\(3\gamma/2\). The centered-moment proof is stronger: it is pointwise
in \(X\), allows signed normalized carriers, and bypasses a running
support envelope. As \(\alpha\downarrow0\), (4.3) converges exactly to
the sharp centered inequality. The projected Laplace calculation is
therefore a finite-abscissa interpolation, not an independent source
of better support exponents.

## 5. Forward theorem under RH

Assume RH. The classical Mertens consequence for the beta source is

\[
 B(y)=\sum_{n\le y}{\beta(n)\over\sqrt n}
 =O_\delta(y^\delta)
\tag{5.1}
\]

for every fixed \(\delta>0\). Abel summation of (0.4) against (5.1)
gives

\[
 \|H_X\|_\infty
 \ll_\delta X^\delta
 \left(
 \|J_X\|_\infty+\operatorname {Var}(J_X)
 \right).
\tag{5.2}
\]

Using the support interval (1.4),

\[
 \mathcal E_Q(X)
 \ll_\delta
 L_XX^{2\delta}
 \left(
 \|J_X\|_\infty+\operatorname {Var}(J_X)
 \right)^2.
\tag{5.3}
\]

Multiplying by \(L_X^3\) also gives

\[
 \mathfrak R_Q(X)
 \ll_\delta
 L_X^4X^{2\delta}
 \left(
 \|J_X\|_\infty+\operatorname {Var}(J_X)
 \right)^2.
\tag{5.4}
\]

Under (0.10), choose \(\delta\) after any prescribed final exponent;
this proves the raw forward theorem (0.11). Under (0.R3), the same
choice in (5.4) proves the renormalized forward theorem. Positivity and
a fixed carrier shape are not required.

## 6. The parabolic RH-equivalence family

For (0.12),

\[
 J_S(x)
 ={6(S-2x)\over S^3}\mathbf1_{(0,S)}(x).
\tag{6.1}
\]

Direct integration gives

\[
\boxed{
 \|J_S\|_2^2={12\over S^3},
 \qquad
 \|J_S\|_\infty={6\over S^2}.}
\tag{6.2}
\]

The zero-extended \(J_S\) has endpoint jumps of total size
\(12/S^2\), and its interior derivative has total mass \(12/S^2\).
Therefore

\[
\boxed{
 \operatorname {Var}(J_S)={24\over S^2}.}
\tag{6.3}
\]

Every schedule \(S_X\ge1\), even a power-sized or larger one, satisfies
the raw forward gate because

\[
 (\log X+S_X){900\over S_X^4}
 \le 900(1+\log X).
\tag{6.4}
\]

More importantly, the renormalized gate also holds for every such
schedule:

\[
 L_X^4{900\over S_X^4}
 =900\left({\log X+S_X\over S_X}\right)^4
 \le900(1+\log X)^4
 =X^{o(1)}.
\tag{6.5}
\]

Equations (0.R2)--(0.R4), (5.4), and (6.5) therefore prove the
all-support equivalence

\[
\boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \bigl(\log X+S_X\bigr)^3\mathcal E_{S_X}(X)
 =X^{o(1)}
 \qquad(1\le S_X<\infty).}
\tag{6.6}
\]

No monotonicity or upper growth bound on the schedule is hidden.

For the raw reverse implication, retain
\(1\le S_X=X^{o(1)}\). Equations (0.9), (0.11), and
(6.2)--(6.4) give

\[
\boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathcal E_{S_X}(X)=X^{o(1)}.}
\tag{6.7}
\]

This includes fixed, logarithmic, polylogarithmic, and genuinely
superlogarithmic subpower supports. The diagonal density
\(12/S_X^3\) may shrink strongly, but source recovery remains
subpower.

## 7. Cubic dilution and the matched boundary

Let

\[
 \nu_X
 =\sum_{n\le X}{\beta(n)\over\sqrt n}\delta_{\log n}.
\tag{7.1}
\]

Then \(H_X=J_S*\nu_X\). The source bound
\(|\beta(n)|\le2\) gives

\[
 \|\nu_X\|_{\rm TV}
 \le2\sum_{n\le X}n^{-1/2}
 \le4\sqrt X.
\tag{7.2}
\]

Young's inequality and (6.2) give

\[
 \|H_X\|_2
 \le\|J_S\|_2\|\nu_X\|_{\rm TV},
 \qquad
\boxed{
 \mathcal E_S(X)\le {192X\over S^3}.}
\tag{7.3}
\]

If \(S_X=X^{\gamma+o(1)}\), this bound has exponent
\(1-3\gamma+o(1)\). At \(\gamma=1/3\) it becomes subpower without any
Möbius cancellation. At the same point, the zero-exclusion line is

\[
 {1\over2}+{3\over2}\cdot{1\over3}=1.
\tag{7.4}
\]

Thus sharp moment recovery loses nontrivial zero information exactly
where elementary dilution can make the raw energy small. The
renormalized Young bound is instead

\[
 \mathfrak R_{S_X}(X)
 \le192X
 \left({\log X+S_X\over S_X}\right)^3
 \le192X(1+\log X)^3.
\tag{7.5}
\]

It remains power-sized even when \(S_X\) is enormous. The factor
\(L_X^3\) exactly charges the sharp source-recovery price and removes
the trivial cubic escape.

### Criticality of the cubic renormalization

For \(p\ge0\), define

\[
 \mathfrak R_S^{(p)}(X)=L_X^p\mathcal E_S(X).
\tag{7.6}
\]

The exponent \(p=3\) is the unique scale-balanced point between the
two proved mechanisms.

If \(0\le p<3\), choose

\[
 S_X=X^{1/(3-p)}.
\tag{7.7}
\]

Then (7.3) gives, unconditionally,

\[
 \mathfrak R_S^{(p)}(X)
 \le192
 \left({L_X\over S_X}\right)^p
 =O(1).
\tag{7.8}
\]

Thus every smaller width power admits a schedule on which its
subpower premise is paid by trivial dilution and records no Möbius
cancellation.

At \(p=3\), the sharp reverse moment law and the RH forward BV law
meet to give the all-support equivalence (6.6).

If \(p>3\), the current RH forward estimate contains

\[
 L_X^{p+1}{900\over S_X^4}
 \asymp S_X^{p-3}
\tag{7.9}
\]

when \(S_X\gg\log X\). It therefore does not pay an arbitrary-support
forward theorem. This is a boundary of the proved estimate, not a
claim that no stronger arithmetic theorem could control \(p>3\).

### Weighted and multiscale firewall

For a positive weight \(w\), the sharp dual cost of recovering the
first moment from

\[
 \mathcal E_w=\int_0^{L_X}w(t)|H_X(t)|^2\,dt
\tag{7.10}
\]

is

\[
 \inf_{c\in\mathbb R}
 \int_0^{L_X}{(t-c)^2\over w(t)}\,dt.
\tag{7.11}
\]

Any dimensionless family of weights uniformly comparable to constants
still has cost \(\asymp L_X^3\). Likewise, if
\(F_X(s)=\int H_X(t)e^{-st}\,dt\), then
\(F_X(0)=0\) and \(F_X'(0)=B(X)\). Multiscale Laplace samples are
finite-difference probes of this derivative; its exact Riesz norm on
the zero-mean subspace is \(L_X^{3/2}/\sqrt{12}\).

Therefore neither uniformly comparable reweighting nor repackaging
the same unweighted energy into several Laplace scales improves the
support exponent. A genuine improvement must add arithmetic
convolution structure, a noncomparable weighted estimate, Sobolev
control, or another independent source norm.

## 8. Scope, firewalls, and next target

| statement | grade |
|---|---|
| carrier moment identities (0.6) | **PROVED EXACT** |
| sharp centered inequality (0.5) | **PROVED EXACT** |
| optimal constant and one-atom extremizer | **PROVED EXACT** |
| Pythagorean Mertens-plus-shape decomposition | **PROVED EXACT** |
| signed autocorrelation second-moment identity | **PROVED EXACT** |
| projected finite-\(\alpha\) carrier inequality | **PROVED EXACT** |
| arbitrary-support renormalized reverse theorem (0.R2) | **PROVED** |
| all-support parabolic RH equivalence (0.R4) | **PROVED** |
| support-exponent zero-free wedge (0.8) | **PROVED** |
| subpower-support reverse RH theorem (0.9) | **PROVED** |
| invariant BV forward gate under RH | **PROVED** |
| parabolic forward theorem for every \(S_X\ge1\) | **PROVED** |
| parabolic norms and variation | **PROVED EXACT** |
| explicit parabolic bound \(192X/S^3\) | **PROVED FROM SOURCE SIZE** |
| matched cubic phase boundary | **PROVED FOR THE DISPLAYED MECHANISMS** |
| width renormalization removes trivial dilution | **PROVED** |
| \(p<3\) trivial-dilution schedule | **PROVED** |
| comparable-weight or multiscale improvement from the same data | **RULED OUT** |
| full RH reverse theorem from raw positive-power energy | **NOT PROVED** |
| \(p>3\) all-support RH forward theorem | **NOT PROVED** |
| beta-energy estimate in an RH-bearing region | **NOT PROVED** |
| improved wedge using arithmetic convolution structure | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The energy premise is assumed for the complete beta source at every
horizon; it is not inferred from a sparse sequence. The derivative
after zero extension and the unit-mass normalization are load-bearing
for (1.1)--(1.2). Positivity is not load-bearing for the centered
reverse theorem.

The next ambitious target is no longer an abstract carrier
optimization. That problem is solved sharply by (2.2). It is:

\[
\boxed{
 \text{Exploit the translated beta-convolution structure to improve
 on the universal support-moment wedge.}}
\tag{8.1}
\]

Any improvement must see arithmetic cancellation that a generic
zero-mean field with prescribed first moment does not possess.

No external novelty or priority is claimed without a dedicated
literature comparison.

## 9. Bounded replay

The producer:

- verifies the frozen variational-carrier quartet by full Git blob ID;
- checks the exact centered test norm and dual extremizer constant;
- evaluates three bounded log horizons and five symbolic support
  exponents;
- checks the independent optimized Laplace parameter;
- records the zero-exclusion wedge and cubic meeting point;
- performs no beta sum, zeta evaluation, prime enumeration, random
  sampling, or quadrature.

~~~text
python -B research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py --check
python -O -B research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py --check
python -B -m unittest tests.test_ffps_moving_support_carrier_phase_diagram
python -O -B -m unittest tests.test_ffps_moving_support_carrier_phase_diagram
python -m ruff check research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py tests/test_ffps_moving_support_carrier_phase_diagram.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_moving_support_carrier_phase_diagram.py tests/test_ffps_moving_support_carrier_phase_diagram.py
~~~
