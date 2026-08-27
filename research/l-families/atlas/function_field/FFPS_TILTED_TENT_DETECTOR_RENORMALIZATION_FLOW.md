# The tilted-tent detector has a derivative-Gaussian renormalization flow

Status: **exact probability factorization, cumulant, support, carrier,
diffusive Fourier, spectral-weight, norm, Jordan, and cusp-refill theorem;
no growing-order beta estimate, Perron bound, RH, or GRH result**

Bounded replay:
[ffps_tilted_tent_detector_renormalization_flow.py](ffps_tilted_tent_detector_renormalization_flow.py).
Canonical summary:
[ffps_tilted_tent_detector_renormalization_flow.json](ffps_tilted_tent_detector_renormalization_flow.json).

Frozen sources: the complete zero-free beta-energy-ladder quartet at commit
**3658d4c31**, and the max-cusp identity quartet at commit
**3dbf13f6d1c49e573a5b9cd8355d9c124273062b**. The producer pins all eight
Git blobs and checks the live ladder producer before replay.

## 0. Outcome

The predecessor introduced

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+,\qquad
 Z=\int_{\mathbb R}\Phi(x)\,dx=4\sinh^2(1/2),\qquad
 P=\Phi/Z.
\tag{0.1}
\]

This packet studies the ordinary convolution powers of the probability
density \(P\), not the predecessor's fixed-support compressed averages.
Put

\[
 K_m=D(P^{*m}),\qquad m\geq1.
\tag{0.2}
\]

If \(X\sim P\), then

\[
 \mu=\mathbf E X=\frac{2}{e-1},\qquad
 \sigma^2=\operatorname {Var}X
 =\frac{2(e^2-3e+1)}{(e-1)^2}>0.
\tag{0.3}
\]

Define the centered density and detector

\[
\begin{aligned}
 f_m(y)&=\sigma\sqrt m\,
 P^{*m}(m\mu+\sigma\sqrt m\,y),\\
 J_m(y)&=m\sigma^2K_m(m\mu+\sigma\sqrt m\,y).
\end{aligned}
\tag{0.4}
\]

The normalization is exact:

\[
\boxed{J_m=f_m'.}
\tag{0.5}
\]

Let

\[
 \varphi(y)=\frac{e^{-y^2/2}}{\sqrt{2\pi}},\qquad
 H_4(y)=y^4-6y^2+3,
\tag{0.6}
\]

and write \(\lambda_r=\kappa_r/\sigma^r\) for the standardized
cumulants of \(P\). Section 3 gives a self-contained Fourier-splitting
proof of the global expansion

\[
\boxed{
 J_m(y)=-y\varphi(y)
 -\frac{\lambda_3}{6\sqrt m}H_4(y)\varphi(y)
 +O(m^{-1})}
\tag{0.7}
\]

uniformly for \(y\in\mathbb R\). Thus the first Hermite mode, the
derivative Gaussian, is the diffusive renormalization limit.

If \(\psi(t)=\mathbf E\exp(-it(X-\mu)/\sigma)\), then

\[
 \widehat J_m(t)=it\,\psi(t/\sqrt m)^m,\qquad
 W_m(t)=|\widehat J_m(t)|^2
 =t^2|\psi(t/\sqrt m)|^{2m}.
\tag{0.8}
\]

The spectral flow is

\[
\boxed{W_m(t)\longrightarrow t^2e^{-t^2}}
\tag{0.9}
\]

locally uniformly and in \(L^1(\mathbb R)\). More precisely,

\[
 W_m(t)=t^2e^{-t^2}
 \left(1+\frac{\lambda_4t^4}{12m}+O_A(m^{-2})\right)
 \quad (|t|\leq A),
\tag{0.10}
\]

and

\[
 \int_{\mathbb R}|W_m(t)-t^2e^{-t^2}|\,dt=O(m^{-1}).
\tag{0.11}
\]

Odd cumulants change Fourier phase but not spectral weight. The fourth
cumulant is the first weight deformation.

Every causal \(K_m\) retains a zero-free carrier in the open RH strip. The
centered \(J_m\) has a different scaled carrier and is safe only when
\(\sigma\sqrt m\ge1/2\); in particular, \(J_1\) is not carrier-safe. The
Gaussian limit appears only after centering and square-root dilation,
which makes \(J_m\) noncausal and its support grow. This is a kernel
renormalization theorem, not a uniform growing-order beta criterion.

## 1. Frozen source and scope

The exact source contract is:

| frozen path at 3658d4c31 | Git blob |
|---|---|
| research/l-families/atlas/function_field/FFPS_ZERO_FREE_BETA_ENERGY_LADDER.md | bd4cbb842e78c1dad5d380c8d20ff14c39bba15e |
| research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.py | df80000192292cc5fc1cd08013f152fb257054f9 |
| research/l-families/atlas/function_field/ffps_zero_free_beta_energy_ladder.json | 7e8889aa0dd1b01674e20158a52502cff0d8dffa |
| tests/test_ffps_zero_free_beta_energy_ladder.py | 983a1320f89087028f6724fe36aaca5ca1309b15 |

The max-cusp source contract is:

| frozen path at 3dbf13f6d | Git blob |
|---|---|
| research/l-families/atlas/function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md | e7959b8788b8a374920aa53bcafd1fb28cda3b72 |
| research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.py | 52023bb4527a32a2c9983fdd25707da3361242e8 |
| research/l-families/atlas/function_field/ffps_bandpass_assembled_perron_leakage.json | 0031e9ae114d7bf6c60d69789d5d52fe4cf04f6e |
| tests/test_ffps_bandpass_assembled_perron_leakage.py | efc9cde7eef3e833aaa5ac40b5d37b1e34f76770 |

The predecessor studies

\[
 Q_m(x)=mP^{*m}(mx),\qquad DQ_m,
\tag{1.1}
\]

whose support remains \([0,2]\). The present packet studies
\(P^{*m}\), centers at \(m\mu\), and dilates by \(\sqrt m\). These
are different flows and no conclusion is transferred between them without
the displayed change of variables.

No zeta zero, numerical zeta value, prime, curve, random sample, long
source range, or contour is evaluated.

## 2. Exact factorization, cumulants, and carrier

The mass in (0.1) is

\[
 Z=4\sinh^2(1/2)=\frac{(e-1)^2}{e}.
\tag{2.1}
\]

Consequently

\[
 P(x)=\frac{e^x}{(e-1)^2}
 \begin{cases}
 x,&0<x<1,\\
 2-x,&1<x<2,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{2.2}
\]

Let

\[
 p_V(v)=\frac{e^v}{e-1}\mathbf1_{[0,1]}(v).
\tag{2.3}
\]

The length of \([0,1]\cap[x-1,x]\) is \(x\) for \(0<x<1\) and
\(2-x\) for \(1<x<2\). Hence

\[
\boxed{P=p_V*p_V.}
\tag{2.4}
\]

Thus \(X=V_1+V_2\) for two independent truncated exponentials, and

\[
\boxed{
 M_X(t)=
 \left(\frac{e^{1+t}-1}{(e-1)(1+t)}\right)^2.}
\tag{2.5}
\]

The value at \(t=-1\) is filled by removal. Differentiating
\(\log M_X(t)\) gives

\[
\begin{aligned}
 \kappa_1&=\frac{2}{e-1},\\
 \kappa_2&=\frac{2(e^2-3e+1)}{(e-1)^2},\\
 \kappa_3&=-\frac{2(2e^3-7e^2+5e-2)}{(e-1)^3},\\
 \kappa_4&=
 \frac{2(6e^4-25e^3+32e^2-25e+6)}{(e-1)^4}.
\end{aligned}
\tag{2.6}
\]

For every \(r\geq2\),

\[
\boxed{
 \kappa_r=2\left[
 (-1)^{r-1}\operatorname {Li}_{1-r}(e^{-1})
 +(-1)^r(r-1)!
 \right].}
\tag{2.7}
\]

Negative-index polylogarithms are rational functions, so this is exact in
\(e\). For

\[
 Y_m=\frac{X_1+\cdots+X_m-m\mu}{\sigma\sqrt m},
\tag{2.8}
\]

the cumulant flow is exactly

\[
 \kappa_1(Y_m)=0,\qquad \kappa_2(Y_m)=1,\qquad
 \kappa_r(Y_m)=\lambda_rm^{1-r/2}\quad(r\geq3).
\tag{2.9}
\]

With the bilateral Laplace convention
\(\mathcal P(s)=\int P(x)e^{-sx}\,dx\),

\[
\boxed{
 \mathcal P(s)=
 \left(\frac{e^{1-s}-1}{(e-1)(1-s)}\right)^2.}
\tag{2.10}
\]

The value at \(s=1\) is removable and nonzero. Its nonremovable zeros are

\[
 s=1+2\pi ik,\qquad k\in\mathbb Z\setminus\{0\},
\tag{2.11}
\]

each of order two. Since

\[
 \mathcal L K_m(s)=s\mathcal P(s)^m,
\tag{2.12}
\]

the carrier divisor is exactly

\[
\boxed{
 s=0\ \text{simple},\qquad
 s=1+2\pi ik\ \text{of order }2m\quad(k\neq0).}
\tag{2.13}
\]

It is zero-free in \(0<\Re s<1\), hence in the open RH strip. On the real
Fourier axis, \(e^{1-it}-1\) cannot vanish because its two terms have
different moduli. Therefore \(K_m\) has exactly one real Fourier zero,
at \(t=0\).

The supports are

\[
 \operatorname {supp}K_m=[0,2m],
\tag{2.14}
\]

and

\[
\boxed{
 \operatorname {supp}J_m=
 \left[-\frac{\mu}{\sigma}\sqrt m,
 \frac{2-\mu}{\sigma}\sqrt m\right].}
\tag{2.15}
\]

Moreover

\[
 \mathcal L J_m(s)=
 s\exp\left(\frac{s\mu\sqrt m}{\sigma}\right)
 \mathcal P\left(\frac{s}{\sigma\sqrt m}\right)^m.
\tag{2.16}
\]

Its nonzero zeros are

\[
 s=\sigma\sqrt m(1+2\pi ik),\qquad k\neq0,
\tag{2.17}
\]

of order \(2m\). Their real parts recede like \(\sigma\sqrt m\).
Thus the centered carrier is nonvanishing in the open consumer strip
exactly when \(\sigma\sqrt m\ge1/2\). Since
\(\sigma\approx0.398312\), this fails at \(m=1\) and holds for every
integer \(m\ge2\). This does not affect the causal \(K_m\) statement in
(2.13).

Translating \(J_m\) right by \((\mu/\sigma)\sqrt m\) restores causality
and leaves Fourier weight unchanged. In Laplace coordinates it inserts
\(\exp(-s\mu\sqrt m/\sigma)\). This shrinking multiplier matters in any
attempt to let \(m\) grow inside a Mellin argument.

## 3. Quantitative Fourier splitting

Use

\[
 \widehat h(t)=\int_{\mathbb R}h(y)e^{-ity}\,dy.
\tag{3.1}
\]

The explicit transform (2.10) gives three elementary estimates.

First, for a fixed \(\delta>0\),

\[
 \log\psi(u)=
 -\frac{u^2}{2}
 +\frac{i\lambda_3u^3}{6}
 +\frac{\lambda_4u^4}{24}
 +O(|u|^5)
 \quad(|u|\leq\delta).
\tag{3.2}
\]

Second, after decreasing \(\delta\),

\[
 |\psi(u)|\leq e^{-c_0u^2}\quad(|u|\leq\delta)
\tag{3.3}
\]

for some \(c_0>0\). Third, absolute continuity and nondegeneracy imply
\(|\psi(u)|<1\) for \(u\neq0\), while (2.10) gives

\[
 |\psi(u)|\ll(1+|u|)^{-2}.
\tag{3.4}
\]

Split the Fourier line into

\[
\begin{array}{ll}
\mathrm I:&|t|\leq m^{1/10},\\
\mathrm {II}:&m^{1/10}<|t|\leq\delta\sqrt m,\\
\mathrm {III}:&\delta\sqrt m<|t|\leq A\sqrt m,\\
\mathrm {IV}:&|t|>A\sqrt m,
\end{array}
\tag{3.5}
\]

where \(A\) is fixed sufficiently large.

In region I, exponentiating (3.2), retaining the cubic term, and using
(3.3) bounds the remainder by

\[
 \frac{C}{m}(1+|t|^6)e^{-c_1t^2}.
\tag{3.6}
\]

Region II is superpolynomially small by (3.3). On region III,
compact-annulus Cramér damping gives \(O(\rho^m)\) for some
\(\rho<1\). On region IV, put \(t=\sqrt m\,u\) and use (3.4):
for \(A\) large, the integrals of
\((1+|t|)(C/|u|^2)^m\) are geometrically small. The Gaussian comparison
has an even smaller tail. Therefore

\[
\begin{aligned}
 \int_{\mathbb R}(1+|t|)
 \left|
 \psi(t/\sqrt m)^m-e^{-t^2/2}
 \left(1+\frac{i\lambda_3t^3}{6\sqrt m}\right)
 \right|dt
 =O(m^{-1}).
\end{aligned}
\tag{3.7}
\]

This is the quantitative input for (0.7), not an imported Edgeworth
theorem. Indeed,

\[
 \widehat f_m(t)=\psi(t/\sqrt m)^m,\qquad
 \widehat J_m(t)=it\,\widehat f_m(t).
\tag{3.8}
\]

Because \(it^3=-(it)^3\), Fourier inversion of (3.7) gives

\[
 f_m(y)=\varphi(y)
 +\frac{\lambda_3}{6\sqrt m}H_3(y)\varphi(y)
 +O(m^{-1})
\tag{3.9}
\]

uniformly. The identity

\[
 (H_3\varphi)'=-H_4\varphi
\tag{3.10}
\]

then proves (0.7).

For the weight statements, expand the real part two orders farther:

\[
 2m\Re\log\psi(t/\sqrt m)
 =-t^2+\frac{\lambda_4t^4}{12m}
 +O_A(m^{-2}).
\tag{3.11}
\]

The same four-region split proves

\[
 \int_{\mathbb R}
 \left|
 |\psi(t/\sqrt m)|^{2m}-e^{-t^2}
 \right|dt=O(m^{-1}),
\tag{3.12}
\]

and, after retaining the displayed fourth-cumulant correction, for
\(j=0,2\),

\[
 \int_{\mathbb R}|t|^j
 \left|
 |\psi(t/\sqrt m)|^{2m}
 -e^{-t^2}\left(1+\frac{\lambda_4t^4}{12m}\right)
 \right|dt=O(m^{-2}).
\tag{3.13}
\]

To see the last rate directly, use the cumulant expansion through order
six in region I. The unretained exponent is
\(O((t^6+t^8)/m^2)\) under Gaussian damping. Regions II--IV are
geometrically or superpolynomially small exactly as above. Thus the
global \(L^1\), norm, and first-correction claims do not rely on a
silently imported local limit theorem.

## 4. Weight, autocorrelation, norms, and cusp refill

Equations (3.11)--(3.13) prove (0.9)--(0.11). Fourier inversion also gives
uniform convergence of the detector autocorrelations

\[
 R_m(x)=\int_{\mathbb R}J_m(y)J_m(y+x)\,dy
\tag{4.1}
\]

to

\[
\boxed{
 R_\infty(x)=
 \frac{1}{4\sqrt\pi}
 \left(1-\frac{x^2}{2}\right)e^{-x^2/4}.}
\tag{4.2}
\]

Parseval and (3.13) give

\[
\boxed{
 \|J_m\|_2^2=
 \frac{1}{4\sqrt\pi}
 +\frac{5\lambda_4}{64\sqrt\pi\,m}
 +O(m^{-2}).}
\tag{4.3}
\]

Here

\[
 \int_{\mathbb R}t^6e^{-t^2}\,dt=\frac{15\sqrt\pi}{8}.
\tag{4.4}
\]

Undoing (0.4) yields

\[
\boxed{
 \|K_m\|_2^2=
 \frac{1}{4\sqrt\pi\,\sigma^3m^{3/2}}
 \left(1+O(m^{-1})\right).}
\tag{4.5}
\]

The pinned max-cusp theorem identifies the zero-tilt linear refill
coefficient \(\ell_m(0)\) with the squared norm of the detector cumulative.
The cumulative of \(J_m=f_m'\) is \(f_m\), so (3.13) with \(j=0\) gives

\[
\boxed{
 \ell_m(0)=\|f_m\|_2^2=
 \frac{1}{2\sqrt\pi}
 +\frac{\lambda_4}{32\sqrt\pi\,m}
 +O(m^{-2}).}
\tag{4.6}
\]

Thus this renormalized physical cusp coefficient converges to a positive
Gaussian constant. It is a kernel statement, not a beta-source estimate.

Two signed moments are exact for every \(m\):

\[
 \int J_m(y)\,dy=0,\qquad
 \int yJ_m(y)\,dy=-1.
\tag{4.7}
\]

The second follows by integration by parts against the probability density
\(f_m\).

## 5. Jordan asymptotics and the one imported closure lemma

The density \(p_V\) is log-concave in the extended sense: its logarithm
is affine on \([0,1]\) and \(-\infty\) outside. We use one classical
analytic fact:

> **Log-concavity closure.** The convolution of integrable log-concave
> functions on the real line is log-concave.

This is the one-dimensional convolution corollary of the
Prékopa--Leindler theorem. It is explicitly imported; it is not certified
by the bounded replay.

By (2.4), every \(P^{*m}\), hence every \(f_m\), is log-concave and
unimodal. It vanishes at both support endpoints, so

\[
 \int(J_m)_+\,dy=\int(J_m)_-\,dy=\max_y f_m(y),\qquad
 \|J_m\|_1=2\max_yf_m(y).
\tag{5.1}
\]

The uniform density limit (3.9) implies

\[
 \max_yf_m(y)\longrightarrow\varphi(0)=\frac{1}{\sqrt{2\pi}}.
\tag{5.2}
\]

Therefore

\[
\boxed{
 \int(J_m)_+\,dy,\ \int(J_m)_-\,dy
 \longrightarrow\frac{1}{\sqrt{2\pi}},\qquad
 \|J_m\|_1\longrightarrow\sqrt{\frac2\pi}.}
\tag{5.3}
\]

Scaling back gives

\[
\boxed{
 \int(K_m)_+\,dx,\ \int(K_m)_-\,dx
 =\frac{1+o(1)}{\sigma\sqrt{2\pi m}}.}
\tag{5.4}
\]

This is the Jordan mass of the kernel itself, not the mass of the
beta-source field made from its translates.

## 6. Fixed-versus-growing firewall

For every fixed finite \(m\), \(K_m\) is compact, causal, and of bounded
variation, and (2.12) is nonzero in \(0<\Re s<1/2\). It therefore cannot
cancel the Mellin pole produced by a hypothetical off-line zeta zero.
This is the same carrier mechanism used by the predecessor.

At every fixed nonzero real frequency,

\[
 |\widehat K_m(t)|^2=t^2|\widehat P(t)|^{2m}\longrightarrow0
\tag{6.1}
\]

exponentially, because \(P\) is a nondegenerate continuous probability
density. Its spectral mass concentrates on \(t=O(m^{-1/2})\). The
nontrivial Gaussian profile appears only in the moving centered coordinate
of (0.4).

The logical firewall is:

    fixed finite m
      -> compact causal carrier and no nonzero real notch;

    m growing with X, T, or the inverse Perron shift
      -> changing support and constants;
      -> centered Gaussian coordinate is noncausal;
      -> causal restoration inserts a shrinking Laplace multiplier;
      -> fixed-kernel RH equivalences are not uniform automatically.

This packet does not interchange

\[
 m\to\infty,\qquad c\downarrow0,\qquad T\to\infty.
\tag{6.2}
\]

Nor does the Gaussian kernel law supply cancellation in beta coefficients.
It is a universal detector baseline only.

## 7. Claim ledger

| statement | grade |
|---|---|
| exact density factorization and MGF | **PROVED EXACT** |
| all cumulants and normalized cumulant flow | **PROVED EXACT** |
| support and carrier zero divisors | **PROVED EXACT** |
| derivative-Gaussian Fourier limit | **PROVED** |
| global first Edgeworth correction | **PROVED BY SECTION 3 FOURIER SPLITTING** |
| weight expansion and global \(L^1\) error | **PROVED BY THE SAME SPLITTING** |
| autocorrelation and \(L^2\) asymptotics | **PROVED** |
| cusp-refill asymptotic | **PROVED FROM THE PINNED MAX-CUSP IDENTITY** |
| Jordan asymptotics | **PROVED USING THE STATED LOG-CONCAVITY LEMMA** |
| uniform growing-\(m\) beta theorem | **NOT PROVED** |
| beta energy, Perron, or negative-mass estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

No external novelty claim is made without a dedicated literature comparison.

## 8. Bounded replay

The producer:

- pins all eight predecessor blobs and the live ladder producer;
- differentiates the exact MGF symbolically through cumulant order four;
- checks the four closed cumulant formulas over a formal symbol \(E\);
- evaluates the exact weight at five fixed frequencies for
  \(m=1,2,4,8,32,128\);
- records exact support, carrier, Gaussian-integral, norm, Jordan, and
  refill formulas;
- performs no zeta-zero, zeta-value, prime, curve, random, contour, or
  large-source computation.

The finite rows are regression controls. The asymptotic statements are
proved in Sections 3--5, not inferred from those rows.

    python -B research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py --check
    python -B -O research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py --check
    python -B -m unittest tests.test_ffps_tilted_tent_detector_renormalization_flow
    python -B -O -m unittest tests.test_ffps_tilted_tent_detector_renormalization_flow
    python -B -m ruff check research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py tests/test_ffps_tilted_tent_detector_renormalization_flow.py
    python -B -m ruff format --check research/l-families/atlas/function_field/ffps_tilted_tent_detector_renormalization_flow.py tests/test_ffps_tilted_tent_detector_renormalization_flow.py
