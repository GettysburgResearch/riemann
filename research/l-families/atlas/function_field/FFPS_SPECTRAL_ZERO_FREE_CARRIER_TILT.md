# Exponential tilts remove every accidental real spectral notch with no energy gap

Status: **exact positive spectral-zero-free carrier construction,
exact strict-but-gapless variational theorem, and exact local energy
curvature; uses the classical all-real-zero theorem for
\(J_{m+1/2}\); no new beta estimate, proof of RH, or claim that
spectral zero-freeness improves arithmetic cancellation**

Bounded replay:
[ffps_spectral_zero_free_carrier_tilt.py](ffps_spectral_zero_free_carrier_tilt.py).
Canonical summary:
[ffps_spectral_zero_free_carrier_tilt.json](ffps_spectral_zero_free_carrier_tilt.json).

Frozen source: the higher-derivative carrier hierarchy at commit
**0123d1ecb097294fc132cf251aebeab9a6bda169**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

Fix \(m\ge1\), \(S>0\), and write \(x=2t/S-1\). The sharp positive
carrier from the frozen source is

\[
 Q_{m,S}(t)
 =\frac{(2m+1)!}{m!^2S^{2m+1}}
 t^m(S-t)^m\mathbf1_{[0,S]}(t).
\tag{0.1}
\]

Define the normalized entire moment-generating function

\[
 \Phi_m(z)
 =
 \frac{\displaystyle\int_{-1}^{1}
 e^{zx}(1-x^2)^m\,dx}
 {\displaystyle\int_{-1}^{1}(1-x^2)^m\,dx}.
\tag{0.2}
\]

For every real \(\tau\ne0\), exponentially tilt the carrier:

\[
\boxed{
 Q_{m,S,\tau}(t)
 =\frac{e^{\tau(2t/S-1)}}{\Phi_m(\tau)}Q_{m,S}(t).}
\tag{0.3}
\]

This remains positive, compactly supported, and unit mass. Its first
\(m-1\) endpoint derivatives vanish, so the zero-extended
\(D^mQ_{m,S,\tau}\) lies in \(L^2\).

With Fourier convention
\(\widehat Q(\omega)=\int Q(t)e^{-i\omega t}\,dt\), put
\(a=\omega S/2\). Then

\[
\boxed{
 \widehat Q_{m,S,\tau}(\omega)
 =e^{-ia}\frac{\Phi_m(\tau-ia)}{\Phi_m(\tau)}.}
\tag{0.4}
\]

Every nonzero zero of \(\Phi_m\) lies on the imaginary axis. Therefore
the vertical line \(\tau-i\mathbb R\) misses the zero set whenever
\(\tau\ne0\), and

\[
\boxed{
 \widehat Q_{m,S,\tau}(\omega)\ne0
 \quad\hbox{for every real }\omega.}
\tag{0.5}
\]

Consequently

\[
 \widehat{D^mQ_{m,S,\tau}}(\omega)
 =(i\omega)^m\widehat Q_{m,S,\tau}(\omega)
\tag{0.6}
\]

has exactly the forced order-\(m\) zero at \(\omega=0\) and no other
real zero.

The construction is gapless at the variational optimum. With

\[
 C_m=(m!)^2(2m+1)\binom{2m}{m}^2,
\tag{0.7}
\]

one has, for every \(\tau\ne0\),

\[
\boxed{
 \|D^mQ_{m,S,\tau}\|_2^2
 >\frac{C_m}{S^{2m+1}},}
\tag{0.8}
\]

but

\[
\boxed{
 \lim_{\tau\to0,\ \tau\ne0}
 \|D^mQ_{m,S,\tau}\|_2^2
 =\frac{C_m}{S^{2m+1}}.}
\tag{0.9}
\]

Thus the positive carriers with no real Fourier zeros have the same
sharp energy infimum as all signed carriers, but do not attain it.
Deleting every accidental spectral notch creates no positive energy
gap.

## 1. Bessel zero geometry

The beta integral gives the classical identity, with the singularity
at \(z=0\) removed,

\[
\boxed{
 \Phi_m(z)
 ={}_0F_1\!\left(;m+\frac32;\frac{z^2}{4}\right)
 =\Gamma\!\left(m+\frac32\right)
 \left(\frac2z\right)^{m+1/2}I_{m+1/2}(z).}
\tag{1.1}
\]

The integral or \({}_0F_1\) expression is the branch-safe definition.
The fractional-power Bessel expression is interpreted through that
entire continuation; its factors must not be assigned incompatible
branches separately.

Equivalently,

\[
 \Phi_m(iz)
 =\Gamma\!\left(m+\frac32\right)
 \left(\frac2z\right)^{m+1/2}J_{m+1/2}(z).
\tag{1.2}
\]

The NIST Digital Library of Mathematical Functions records that all
zeros of \(J_\nu\) are real for \(\nu\ge-1\); see
[DLMF §10.21(i)](https://dlmf.nist.gov/10.21#i), especially the
all-real-zero statement immediately following equation 10.21.3.
Here \(\nu=m+1/2\), so (1.2) proves that every nonzero zero of
\(\Phi_m\) is purely imaginary. This is the one external classical
input in the packet.

At \(\tau=0\), the optimal beta carrier therefore has infinitely many
nonzero real Fourier notches:

\[
 \omega=\pm\frac{2j_{m+1/2,k}}{S},
 \qquad k=1,2,\ldots,
\tag{1.3}
\]

where \(j_{\nu,k}\) is a positive zero of \(J_\nu\). Formula (0.3)
moves the Fourier sampling line off the imaginary zero lattice without
moving any source point or adapting to a zeta zero.

## 2. Positivity, normalization, and the exact Fourier shift

The centered beta law underlying (0.1) has density proportional to
\((1-x^2)^m\) on \([-1,1]\). Hence \(\Phi_m(\tau)>0\) for real
\(\tau\), and (0.3) is positive and normalized:

\[
 \int_0^S Q_{m,S,\tau}(t)\,dt=1.
\tag{2.1}
\]

Substituting \(t=S(x+1)/2\) in the Fourier transform gives

\[
\begin{aligned}
 \widehat Q_{m,S,\tau}(\omega)
 &=
 e^{-ia}
 \frac{\int_{-1}^{1}
 e^{(\tau-ia)x}(1-x^2)^m\,dx}
 {\Phi_m(\tau)\int_{-1}^{1}(1-x^2)^m\,dx}\\
 &=e^{-ia}\frac{\Phi_m(\tau-ia)}{\Phi_m(\tau)},
\end{aligned}
\tag{2.2}
\]

which proves (0.4). The denominator is positive and the numerator has
real part \(\tau\ne0\) in its argument, so the Bessel zero theorem
proves (0.5).

The tilt factor is smooth and nonzero at both endpoints. Multiplying
the order-\(m\) endpoint zeros of \(Q_{m,S}\) by it preserves those
zeros. Distributional differentiation after zero extension therefore
introduces no delta masses through order \(m\), and the ordinary
Fourier derivative rule proves (0.6).

## 3. Strict variational inequality, equal infimum

The frozen source proves that among every real unit-mass carrier
supported in \([0,S]\) with zero-extended \(D^mQ\in L^2\),

\[
 \|D^mQ\|_2^2\ge\frac{C_m}{S^{2m+1}},
\tag{3.1}
\]

with equality only for \(Q=Q_{m,S}\) almost everywhere.

For \(\tau\ne0\), the ratio
\(Q_{m,S,\tau}/Q_{m,S}=e^{\tau x}/\Phi_m(\tau)\) is not constant on
\((0,S)\). Hence \(Q_{m,S,\tau}\ne Q_{m,S}\), and uniqueness in (3.1)
gives the strict inequality (0.8).

On a fixed finite interval, the map
\(\tau\mapsto e^{\tau x}/\Phi_m(\tau)\) is analytic in every
\(C^m\) norm near zero. Therefore

\[
 D^mQ_{m,S,\tau}\longrightarrow D^mQ_{m,S}
 \quad\hbox{in }L^2
\tag{3.2}
\]

as \(\tau\to0\), proving (0.9). Every punctured member is
spectral-zero-free by (0.5), so

\[
\boxed{
 \inf_{\substack{Q\ge0,\ \int Q=1,\ \operatorname{supp}Q\subset[0,S]\\
 D^mQ\in L^2\text{ after zero extension}\\
 \widehat Q(\omega)\ne0\ \forall\omega\in\mathbb R}}
 \|D^mQ\|_2^2
 =\frac{C_m}{S^{2m+1}},}
\tag{3.3}
\]

and the infimum is not attained. Indeed an attaining carrier would
have to be the unique beta minimizer, whose nonzero notches are listed
in (1.3).

## 4. Exact local energy curvature

The lack of a gap has a sharp second-order form. In centered
coordinates, omit harmless normalization and scale and put

\[
 f_m(x)=(1-x^2)^m.
\tag{4.1}
\]

Rodrigues' formula and one leading-coefficient comparison give

\[
\begin{aligned}
 D_x^mf_m
 &=(-1)^m2^mm!P_m(x),\\
 D_x^m(xf_m)
 &=(-1)^m2^mm!P_{m+1}(x).
\end{aligned}
\tag{4.2}
\]

At \(\tau=0\), symmetry gives \(\Phi_m'(0)=0\), so the first variation
of the tilted carrier is \(xQ_{m,S}\). It has mass zero. The
second variation is
\[
 \left.\partial_\tau^2Q_{m,S,\tau}\right|_{\tau=0}
 =\left(x^2-\frac1{2m+3}\right)Q_{m,S},
\]
and also has mass zero. The Euler--Lagrange orthogonality of the beta
minimizer therefore kills both cross terms with the base detector.
Legendre orthogonality then gives

\[
 \frac{\|D_x^m(xf_m)\|_2^2}
 {\|D_x^mf_m\|_2^2}
 =\frac{2m+1}{2m+3}.
\tag{4.3}
\]

The energy is even in \(\tau\), because reflection sends \(\tau\) to
\(-\tau\). Therefore

\[
\boxed{
 \frac{\|D^mQ_{m,S,\tau}\|_2^2}
 {C_m/S^{2m+1}}
 =
 1+\frac{2m+1}{2m+3}\tau^2+O_m(\tau^4).}
\tag{4.4}
\]

The cost is globally strict for every fixed \(\tau\ne0\), and locally
quadratic as \(\tau\to0\). It can be made arbitrarily small, so
spectral zero-freeness has no uniform coercive energy penalty.

For the first rung the complete energy is elementary. With the
removable value at \(\tau=0\),

\[
\boxed{
 S^3\|DQ_{1,S,\tau}\|_2^2
 =
 \frac{\tau^3\!\left[
 (4\tau^2+1)\sinh(2\tau)-2\tau\cosh(2\tau)\right]}
 {4(\tau\cosh\tau-\sinh\tau)^2}.}
\tag{4.5}
\]

Its exact local jet is

\[
\begin{aligned}
 S^3\|DQ_{1,S,\tau}\|_2^2
 &=
 12+\frac{36}{5}\tau^2+\frac{72}{175}\tau^4
 -\frac4{315}\tau^6\\
 &\quad+\frac{204}{336875}\tau^8+O(\tau^{10}).
\end{aligned}
\tag{4.6}
\]

The leading ratio \((36/5)/12=3/5\) is (4.4) at \(m=1\). The higher
coefficients show that the exact energy is not merely a quadratic
surrogate.

## 5. Pushforward to the beta detector

For

\[
 H_{m,S,\tau,X}(t)
 =\sum_{n\le X}\frac{\beta(n)}{\sqrt n}
 D^mQ_{m,S,\tau}(t-\log n),
\tag{5.1}
\]

unit mass still gives the carrier-independent matched moment

\[
 \int t^mH_{m,S,\tau,X}(t)\,dt
 =(-1)^mm!B_0(X).
\tag{5.2}
\]

Thus the tilt removes all accidental real spectral zeros without
tuning away the source-faithful beta prefix. The sharp support
projection and every reverse-to-RH inequality from the frozen source
remain valid.

What does not follow is just as important. Zero-freeness of the local
carrier transform supplies no cancellation in the multi-atom beta
convolution, no subpower field-energy estimate, and no improvement of
the support condition number. A fixed small \(\tau\) changes only a
constant local energy factor. The theorem is an inverse-design
firewall, not an RH estimate.

There is also a load-bearing Laplace-orientation distinction. The
carrier exponential generating function is

\[
\boxed{
 \mathscr Q_{m,S,\tau}(z)
 =e^{Sz/2}\frac{\Phi_m(\tau+Sz/2)}{\Phi_m(\tau)}.}
\tag{5.3}
\]

Since the zeros of \(\Phi_m\) are purely imaginary, all zeros of
\(\mathscr Q_{m,S,\tau}\) lie on

\[
 \boxed{\Re z=-\frac{2\tau}{S}.}
\tag{5.4}
\]

Thus \(\tau>0\) is zero-free in the closed right half-plane, whereas
\(\tau<0\) moves an infinite zero lattice into that half-plane. Both
signs are real-Fourier-zero-free, but only the positive orientation is
automatically compatible with a right-half-plane Mellin--Landau
quotient argument. The matched-moment reverse criterion (5.2) remains
valid for either sign because it does not divide by
\(\mathscr Q_{m,S,\tau}\).

## 6. Scope and firewalls

| statement | grade |
|---|---|
| positive normalized exponential tilt (0.3) | **PROVED EXACT** |
| exact Fourier shift (0.4) | **PROVED EXACT** |
| all nonzero zeros of \(\Phi_m\) lie on \(i\mathbb R\) | **CLASSICAL EXTERNAL THEOREM** |
| no real Fourier zeros for every \(\tau\ne0\) | **PROVED FROM CLASSICAL INPUT** |
| only the forced order-\(m\) derivative zero remains | **PROVED** |
| strict energy inequality for every nonzero tilt | **PROVED** |
| same zero-free and unrestricted energy infimum | **PROVED** |
| exact quadratic energy coefficient (4.4) | **PROVED EXACT** |
| Laplace zero line \(\Re z=-2\tau/S\) | **PROVED EXACT** |
| new beta-convolution cancellation | **NOT PROVED** |
| uniform condition-number improvement forced by real zero-freeness | **DISPROVED IN THIS ENERGY CLASS** |
| subpower detector estimate, RH, or GRH | **NOT PROVED** |

The theorem concerns zeros of the real-frequency Fourier transform of
one compact carrier. They are not zeros of \(\zeta(s)\), an
\(L\)-function, or the completed xi function.

The zero-free class in (3.3) retains the boundary condition
\(D^mQ\in L^2\) after zero extension. Dropping that condition changes
the variational problem.

The tilt parameter is real, fixed independently of zeta zeros, and may
be arbitrarily small but nonzero. No uniform lower bound
\(|\widehat Q(\omega)|\ge c>0\) is claimed; the transform tends to zero
at high frequency by the Riemann--Lebesgue lemma.

As \(\tau\to0\), the old real zeros become arbitrarily deep
near-notches. The theorem removes exact zeros, not small values or
ill-conditioning at selected frequencies.

The no-gap result concerns the local carrier norm. It is not uniform
in the horizon \(X\) for the complete translated beta field. It also
does not rule out improved conditioning on a fixed frequency band or
inside a finite arithmetic Gram matrix. The disproof in the ledger is
only for a uniform improvement of the frozen support/moment,
diagonal-normalized energy condition number.

No external novelty or priority is claimed. The Bessel input is
classical and cited explicitly.

## 7. Bounded replay

The producer:

- verifies the frozen higher-derivative quartet by full Git blob ID;
- constructs \((1-x^2)^m\), its matched derivative, and its tilted
  first variation exactly for \(1\le m\le6\);
- checks both Legendre identities in (4.2), exact norms, the curvature
  coefficient \((2m+1)/(2m+3)\), and expands the displayed first-rung
  closed form through \(\tau^8\), while also checking centered beta
  moments and the sharp carrier constant using rational power-series
  and polynomial arithmetic;
- records the DLMF all-real-Bessel-zero input and the logical vertical-
  line consequence, but does not pretend to reprove that external
  theorem computationally;
- performs no beta sum, prime enumeration, zeta evaluation, Bessel
  root search, random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py --check
python -O -B research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py --check
python -B -m unittest tests.test_ffps_spectral_zero_free_carrier_tilt
python -O -B -m unittest tests.test_ffps_spectral_zero_free_carrier_tilt
python -m ruff check research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py tests/test_ffps_spectral_zero_free_carrier_tilt.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_spectral_zero_free_carrier_tilt.py tests/test_ffps_spectral_zero_free_carrier_tilt.py
~~~
