# High-rank Haar boundary-layer tomography for SU(2) characters

Status: **proved uniform tail, crossover, truncation, and endpoint-profile
theorems** for the compact Haar model. No arithmetic-family or zero theorem is
claimed.

## Start here

Let

\[
 X_N(\Theta)
 =\left|{\sin(N\Theta)\over\sin\Theta}\right|,
 \qquad
 d\mu(\theta)={2\over\pi}\sin^2\theta\,d\theta,
 \qquad N=n+1.
\]

The earlier high-rank note proves weak convergence to
\(|\sin U|/\sin\Theta\), the cubic limiting tail, and
\(\mathbb E X_N^p\asymp N^{p-3}\) above the critical exponent \(3\). This
packet resolves the missing transition between those statements.

The main new results are:

1. **Uniform mesoscopic tail.** If \(1\ll x\ll N\), uniformly throughout
   that two-parameter region,

   \[
   \boxed{
   \Pr(X_N>x)
   \sim {16\over9\pi^2}x^{-3}.}
   \tag{1}
   \]

2. **Full ceiling crossover.** For fixed \(0<\lambda<1\),

   \[
   \boxed{
   N^3\Pr(X_N>\lambda N)\longrightarrow
   H(\lambda)
   ={4\over\pi}\int_0^{1/\lambda}
   t^2\mathbf1_{\{|\sin t|>\lambda t\}}\,dt.}
   \tag{2}
   \]

   This interpolates between the cubic tail and the hard cap:

   \[
   \boxed{
   \lambda^3H(\lambda)\longrightarrow{16\over9\pi^2}
   \quad(\lambda\downarrow0),}
   \tag{3}
   \]

   \[
   \boxed{
   H(\lambda)\sim{8\sqrt6\over\pi}
   (1-\lambda)^{3/2}
   \quad(\lambda\uparrow1).}
   \tag{4}
   \]

3. **Truncated moments.** If \(T\to\infty\) and \(T/N\to0\), then

   \[
   \boxed{
   \mathbb E[X_N^3\mathbf1_{X_N\le T}]
   \sim{16\over3\pi^2}\log T,}
   \tag{5}
   \]

   and, for every fixed \(p>3\),

   \[
   \boxed{
   \mathbb E[X_N^p\mathbf1_{X_N\le T}]
   \sim{16\over3\pi^2(p-3)}T^{p-3}.}
   \tag{6}
   \]

4. **Endpoint tomography.** For \(p>3\), the entire leading moment is
   distributed on the scale \(N^{-1}\) with an explicit cumulative profile.
   At \(p=3\), the logarithmic mass is instead spread across all intermediate
   endpoint scales: the window
   \(\min(\Theta,\pi-\Theta)\le N^{-\beta}\) captures asymptotic fraction
   \(1-\beta\), for \(0<\beta<1\).

These are boundary-layer theorems, not numerical fits.

## 1. Frozen source contract

The analytic source is
ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md at commit
8ba581fcc9c0b3ef6b68ac6d121648dd36c1c289, blob
2a0c0b9fefbbe394477dc97cc5c05d22b9ae7bde.

The exact finite-rank source is the
ELLIPTIC_TENSOR_SYMMETRIC_POWER_MOMENT_LADDER packet at commit
010827a518374e34b28d29f6a92741c3174ae803. Its canonical JSON payload is

    0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088

The new arguments use only Haar measure, elementary changes of variables,
periodic averaging, and Taylor expansion. The source packet is provenance,
not a numerical input.

## 2. Exact finite-\(N\) tail coordinate

For \(x\ge1\), the inequality \(X_N>x\) forces
\(\sin\Theta<1/x\). Reflection about \(\pi/2\) gives the exact identity

\[
\boxed{
\Pr(X_N>x)
={4\over\pi}
\int_0^{\arcsin(1/x)}
\mathbf1_{\{|\sin(N\theta)|>x\sin\theta\}}
\sin^2\theta\,d\theta.}
\tag{7}
\]

With \(y=x\sin\theta\), this becomes

\[
\boxed{
\Pr(X_N>x)
={4\over\pi x^3}
\int_0^1
{y^2\,
\mathbf1_{\{|\sin(N\arcsin(y/x))|>y\}}
\over\sqrt{1-y^2/x^2}}\,dy.}
\tag{8}
\]

It follows immediately that

\[
\Pr(X_N>x)=0\quad(x\ge N),
\tag{9}
\]

because \(|\sin(N\theta)|\le N\sin\theta\), and that

\[
\Pr(X_N>x)
\le {2\over\pi}
\left(
\arcsin{x^{-1}}
-x^{-1}\sqrt{1-x^{-2}}
\right)
\quad(x\ge1).
\tag{10}
\]

The upper bound is the complete Haar mass of the two possible endpoint
regions. It is nonasymptotic but deliberately does not pretend that every
phase in those regions exceeds the threshold.

## 3. Uniform mesoscopic cubic tail

Put

\[
\phi_{N,x}(y)=N\arcsin(y/x).
\]

If \(x\to\infty\) and \(N/x\to\infty\), then

\[
\inf_{0\le y\le1}\phi'_{N,x}(y)\to\infty,
\qquad
{1\over\sqrt{1-y^2/x^2}}\to1
\]

uniformly. A standard nonstationary periodic-averaging lemma therefore gives

\[
\int_0^1y^2
\mathbf1_{\{|\sin\phi_{N,x}(y)|>y\}}\,dy
\longrightarrow
\int_0^1y^2q(y)\,dy,
\tag{11}
\]

where the phase proportion is

\[
q(y)
={1\over2\pi}
\operatorname{meas}\{u\in[0,2\pi]:|\sin u|>y\}
={2\over\pi}\arccos y.
\tag{12}
\]

For completeness, the averaging lemma can be proved by approximating the
indicator in \(L^1([0,1]\times\mathbf R/2\pi\mathbf Z)\) by a finite
trigonometric polynomial in the phase variable. Every nonconstant Fourier
mode tends to zero by integration by parts because \(\phi'\) tends uniformly
to infinity and

\[
{\phi''\over(\phi')^2}
=O\!\left({1\over (N/x)x^2}\right).
\]

The discontinuity set \(|\sin u|=y\) has two-dimensional measure zero, so
the approximation loses no mass.

Integration by parts gives

\[
\int_0^1y^2\arccos y\,dy={2\over9}.
\tag{13}
\]

Substituting (11)--(13) into (8) proves the sequential statement

\[
x^3\Pr(X_N>x)\longrightarrow{16\over9\pi^2}
\quad
\text{whenever }x\to\infty,\ N/x\to\infty.
\tag{14}
\]

Equivalently, and genuinely uniformly,

\[
\boxed{
\lim_{A\to\infty}\;
\limsup_{N\to\infty}\;
\sup_{A\le x\le N/A}
\left|
x^3\Pr(X_N>x)-{16\over9\pi^2}
\right|=0.}
\tag{15}
\]

Indeed, failure of (15) would produce a sequence with both \(x\) and \(N/x\)
tending to infinity, contradicting (14).

This closes the precise gap between the fixed-\(x\) weak-limit tail and the
\(N^{p-3}\) divergent moments.

## 4. The full \(x\asymp N\) crossover

Set \(x=\lambda N\) in (8), with fixed \(0<\lambda<1\). Dominated convergence
gives

\[
\begin{aligned}
N^3\Pr(X_N>\lambda N)
&\longrightarrow
{4\over\pi\lambda^3}
\int_0^1y^2
\mathbf1_{\{|\sin(y/\lambda)|>y\}}\,dy\\
&={4\over\pi}
\int_0^{1/\lambda}
t^2\mathbf1_{\{|\sin t|>\lambda t\}}\,dt.
\end{aligned}
\]

This proves (2). The equality set has measure zero: on a bounded interval,
the nonzero analytic function \(\sin^2t-\lambda^2t^2\) has only finitely many
zeros.

After \(s=\lambda t\),

\[
\lambda^3H(\lambda)
={4\over\pi}\int_0^1
s^2\mathbf1_{\{|\sin(s/\lambda)|>s\}}\,ds.
\tag{16}
\]

Periodic averaging and (13) prove (3).

As \(\lambda\uparrow1\), only the first small positive lobe contributes. Let
\(t_\lambda\) be the positive solution of

\[
{\sin t_\lambda\over t_\lambda}=\lambda.
\]

Taylor expansion gives

\[
t_\lambda\sim\sqrt{6(1-\lambda)}.
\tag{17}
\]

Consequently

\[
H(\lambda)
={4\over3\pi}t_\lambda^3
\sim{8\sqrt6\over\pi}(1-\lambda)^{3/2},
\]

which proves (4). The exponent \(3/2\) is the ceiling analogue of the cubic
endpoint law.

## 5. An exact finite-\(N\) ceiling coefficient

The crossover has a finite-rank sharpening. For every fixed integer \(N\ge2\),

\[
{\sin(N\theta)\over N\sin\theta}
=1-{N^2-1\over6}\theta^2+O_N(\theta^4)
\quad(\theta\to0).
\tag{18}
\]

The absolute character reaches its maximum \(N\) only at the two endpoints.
Therefore, as \(\varepsilon\downarrow0\),

\[
\boxed{
\Pr\!\left(X_N>N(1-\varepsilon)\right)
\sim
{8\sqrt6\over\pi(N^2-1)^{3/2}}
\varepsilon^{3/2}.}
\tag{19}
\]

Indeed, the threshold endpoint width is

\[
\theta_\varepsilon
\sim\sqrt{6\varepsilon\over N^2-1},
\]

and the combined Haar mass of two endpoint intervals of width \(a\) is

\[
{4\over\pi}\int_0^a\sin^2\theta\,d\theta
\sim{4\over3\pi}a^3.
\]

Multiplying (19) by \(N^3\) and then letting \(N\to\infty\) recovers the
coefficient in (4).

## 6. Truncated and Winsorized moments

Let \(T=T_N\) satisfy

\[
T\to\infty,\qquad T/N\to0.
\tag{20}
\]

For every nonnegative random variable \(X\),

\[
\mathbb E[X^p\mathbf1_{X\le T}]
=p\int_0^Tt^{p-1}\Pr(X>t)\,dt
-T^p\Pr(X>T),
\tag{21}
\]

whereas

\[
\mathbb E[\min(X,T)^p]
=p\int_0^Tt^{p-1}\Pr(X>t)\,dt.
\tag{22}
\]

The uniform tail (15) may be integrated throughout
\(A\le t\le T\). Low values contribute only \(O_A(1)\). With

\[
c={16\over9\pi^2},
\]

equations (21)--(22) give, at the critical exponent,

\[
\boxed{
\mathbb E[X_N^3\mathbf1_{X_N\le T}]
\sim
\mathbb E[\min(X_N,T)^3]
\sim3c\log T
={16\over3\pi^2}\log T.}
\tag{23}
\]

For every fixed \(p>3\),

\[
\boxed{
\mathbb E[X_N^p\mathbf1_{X_N\le T}]
\sim {3c\over p-3}T^{p-3}
={16\over3\pi^2(p-3)}T^{p-3},}
\tag{24}
\]

\[
\boxed{
\mathbb E[\min(X_N,T)^p]
\sim {pc\over p-3}T^{p-3}
={16p\over9\pi^2(p-3)}T^{p-3}.}
\tag{25}
\]

The difference between (24) and (25) is exactly the capped tail mass
\(T^p\Pr(X_N>T)\sim cT^{p-3}\).

These formulas explain what a robust experiment should compare at growing
rank. A hard truncation and a Winsorization have different leading constants
above the cubic threshold even though both remove the extreme cap.

## 7. Endpoint tomography of the divergent moments

Let

\[
D(\Theta)=\min(\Theta,\pi-\Theta).
\]

For fixed \(a>0\) and fixed \(p\ge0\), direct endpoint scaling gives

\[
\boxed{
N^{3-p}
\mathbb E\!\left[
X_N^p\mathbf1_{\{ND(\Theta)\le a\}}
\right]
\longrightarrow
\Psi_p(a)
={4\over\pi}
\int_0^a|\sin t|^p t^{2-p}\,dt.}
\tag{26}
\]

For \(p>3\), the earlier full-moment constant is

\[
C_p={4\over\pi}\int_0^\infty|\sin t|^p t^{2-p}\,dt.
\]

Therefore

\[
\boxed{
\lim_{N\to\infty}
{\mathbb E[X_N^p\mathbf1_{\{ND\le a\}}]
\over\mathbb E X_N^p}
={\Psi_p(a)\over C_p},
\qquad
{\Psi_p(a)\over C_p}\uparrow1
\quad(a\to\infty).}
\tag{27}
\]

This is a complete cumulative profile: for every \(p>3\), all leading mass
lies within \(O(N^{-1})\) of the two central conjugacy classes, and the
integral in (27) tells exactly how it accumulates.

The critical cubic moment has a different geometry. For fixed
\(0<\beta<1\), substitution \(t=N\theta\) and periodic averaging of
\(|\sin t|^3\), whose period mean is \(4/(3\pi)\), give

\[
\boxed{
\mathbb E\!\left[
X_N^3
\mathbf1_{\{D(\Theta)\le N^{-\beta}\}}
\right]
\sim
{16\over3\pi^2}(1-\beta)\log N.}
\tag{28}
\]

Since the total cubic moment is
\((16/(3\pi^2))\log N+o(\log N)\),

\[
\boxed{
{\mathbb E[
X_N^3\mathbf1_{\{D\le N^{-\beta}\}}]
\over\mathbb E X_N^3}
\longrightarrow1-\beta.}
\tag{29}
\]

No fixed \(a/N\) boundary layer captures a positive fraction of the cubic
moment. Instead, every logarithmic endpoint scale contributes the same
first-order density. This is the precise critical phenomenon hidden by the
single statement \(\mathbb E X_N^3\asymp\log N\).

## 8. Scientific boundary

Proved exactly in this packet:

- the finite-\(N\) tail coordinates (7)--(8);
- the uniform mesoscopic law (15);
- the crossover function and both endpoint limits (2)--(4);
- the finite-\(N\) ceiling law (19);
- the hard-truncated and Winsorized moment laws (23)--(25);
- the \(p>3\) cumulative boundary profile (26)--(27);
- the cubic logarithmic-scale profile (28)--(29).

Not proved:

- any arithmetic-family equidistribution uniform in \(N\);
- any finite-field, elliptic-curve, modular-form, Euler-product, or
  low-lying-zero theorem;
- transfer of the compact tail to a family of global L-functions;
- RH, GRH, or an individualization statement;
- external novelty.

The arithmetic next step is now precise: for a sourced family and a growing
symmetric-power index, prove equidistribution against threshold or smoothed
truncation functions uniformly on the scale \(1\ll x\ll N\), or prove a
boundary-stratum count reproducing \(H(\lambda)\). Fixed-rank
equidistribution alone cannot exchange the arithmetic-family and rank limits.

## 9. Reproduction

The producer checks exact rational Taylor coefficients, beta-integral
certificates, tail/truncation constants, source locks, and resource caps.
It performs no quadrature, root search, sampling, character enumeration,
finite-field enumeration, or L-function computation.

    python research/l-families/atlas/function_field/high_rank_haar_boundary_layer_tomography.py --check
    python -O research/l-families/atlas/function_field/high_rank_haar_boundary_layer_tomography.py --check
    python -m pytest -q tests/test_high_rank_haar_boundary_layer_tomography.py
    python -O -m pytest -q tests/test_high_rank_haar_boundary_layer_tomography.py
    python -m ruff check research/l-families/atlas/function_field/high_rank_haar_boundary_layer_tomography.py tests/test_high_rank_haar_boundary_layer_tomography.py

Regenerate the canonical JSON by omitting --check from the first command.
