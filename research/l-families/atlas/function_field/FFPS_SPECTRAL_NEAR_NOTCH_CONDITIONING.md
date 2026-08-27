# Removing every spectral zero leaves a sharp quadratic conditioning scar

Status: **exact pointwise and compact-band near-notch theorem, exact local
minimum shift and quartic floor, and classical fixed-order high-frequency
asymptotic; no beta-convolution estimate, proof of RH, or uniform inverse
bound**

Bounded replay:
[ffps_spectral_near_notch_conditioning.py](ffps_spectral_near_notch_conditioning.py).
Canonical summary:
[ffps_spectral_near_notch_conditioning.json](ffps_spectral_near_notch_conditioning.json).

Frozen source: the spectral-zero-free carrier tilt at commit
**805ab873cb051c739f19978ebb772b2625adcffb**. The producer pins the
four source blobs and imports no live predecessor module.

## 0. Outcome

The frozen source showed that an arbitrarily small nonzero exponential tilt
removes every accidental real Fourier zero of the sharp beta carrier while
paying arbitrarily little derivative energy. This packet determines exactly
what that cheap zero removal buys.

Fix \(m\ge1\), support width \(S>0\), and let

\[
 F_m(a)=\Phi_m(-ia)
 =(2m+1)!!\frac{j_m(a)}{a^m}.
\tag{0.1}
\]

The old positive notches are

\[
 a_k=j_{m+1/2,k},
 \qquad \omega_k=\frac{2a_k}{S},
\tag{0.2}
\]

and they are simple. Put

\[
 D_{m,k}=|F_m'(a_k)|
 =\frac{(2m+1)!!}{a_k^m}|j_m'(a_k)|,
 \qquad
 r_m=\frac{2m+1}{2m+3}.
\tag{0.3}
\]

For the positive tilted carrier \(Q_{m,S,\tau}\), define the relative energy
excess

\[
 \Delta_m(\tau)
 =\frac{\|D^mQ_{m,S,\tau}\|_2^2}
 {\|D^mQ_{m,S,0}\|_2^2}-1.
\tag{0.4}
\]

Then, at every fixed old notch,

\[
 \boxed{
 |\widehat Q_{m,S,\tau}(\omega_k)|^2
 =D_{m,k}^2\tau^2+O_{m,k}(\tau^4),}
\tag{0.5}
\]

while

\[
 \Delta_m(\tau)=r_m\tau^2+O_m(\tau^4).
\tag{0.6}
\]

Consequently the exact price-to-floor conversion is

\[
 \boxed{
 \lim_{\tau\to0}
 \frac{|\widehat Q_{m,S,\tau}(\omega_k)|^2}
 {\Delta_m(\tau)}
 =\frac{D_{m,k}^2}{r_m}.}
\tag{0.7}
\]

Zero removal and energy loss occur at the same quadratic scale. The operation
does not produce a hidden coercive gap: making the energy arbitrarily sharp
forces every old notch to remain arbitrarily deep.

The result is stronger than a value at one frequency. On the natural
near-notch scale \(a=a_k+|\tau|y\),

\[
 \boxed{
 \frac{|\widehat Q_{m,S,\tau}(2a/S)|^2}{\tau^2}
 \longrightarrow D_{m,k}^2(1+y^2)}
\tag{0.8}
\]

locally uniformly for bounded \(y\). Thus the lifted notch has both amplitude
and width proportional to \(|\tau|\), with a universal quadratic profile.

## 1. Why the error is quartic

With

\[
 W_\tau(a)
 =\frac{|\Phi_m(\tau-ia)|^2}{\Phi_m(\tau)^2},
\tag{1.1}
\]

the exact Fourier formula from the frozen source gives

\[
 W_\tau(a)=|\widehat Q_{m,S,\tau}(2a/S)|^2.
\tag{1.2}
\]

Because \(\Phi_m\) is even and has real Taylor coefficients,

\[
 \Phi_m(-\tau-ia)
 =\Phi_m(\tau+ia)
 =\overline{\Phi_m(\tau-ia)}.
\tag{1.3}
\]

Hence \(W_{-\tau}(a)=W_\tau(a)\) exactly. It is analytic and even in
\(\tau\), so no cubic remainder is possible. Reflection similarly sends the
tilted carrier at \(\tau\) to the carrier at \(-\tau\), proving that its energy
is even.

Write \(f_j=F_m^{(j)}(a_k)\). At a simple old zero,

\[
 \Phi_m(\tau-ia_k)
 =i\tau f_1-\frac{\tau^2}{2}f_2
 -\frac{i\tau^3}{6}f_3+O(\tau^4).
\tag{1.4}
\]

The real and imaginary terms alternate. Therefore

\[
 |\Phi_m(\tau-ia_k)|^2
 =f_1^2\tau^2
 +\left(\frac{f_2^2}{4}-\frac{f_1f_3}{3}\right)\tau^4
 +O(\tau^6).
\tag{1.5}
\]

Since the centered beta second moment is

\[
 \mu_2=\frac1{2m+3},
 \qquad
 \Phi_m(\tau)^2=1+\mu_2\tau^2+O(\tau^4),
\tag{1.6}
\]

division gives the exact symbolic jet

\[
 W_\tau(a_k)
 =f_1^2\tau^2
 +\left(
 \frac{f_2^2}{4}-\frac{f_1f_3}{3}-\mu_2f_1^2
 \right)\tau^4+O(\tau^6).
\tag{1.7}
\]

This proves (0.5) and records the next term without numerical root fitting.

## 2. Minimum shift and the sharper floor

The normalized transform satisfies

\[
 F_m''(a)+\frac{2m+2}{a}F_m'(a)+F_m(a)=0.
\tag{2.1}
\]

At \(a_k\), this gives

\[
 \frac{f_2}{f_1}=-\frac{2m+2}{a_k},
 \qquad
 \frac{f_3}{f_1}
 =\frac{(2m+2)(2m+3)}{a_k^2}-1.
\tag{2.2}
\]

The implicit-function theorem applied to the local critical point of
\(W_\tau\) gives a unique minimum near every interior old zero. It is even in
\(\tau\) and shifts away from the origin:

\[
 \boxed{
 a_k(\tau)
 =a_k+\frac{m+1}{a_k}\tau^2+O_{m,k}(\tau^4).}
\tag{2.3}
\]

At that moving minimum,

\[
 W_\tau(a_k(\tau))
 =D_{m,k}^2\tau^2
 \left(1+\eta^{\min}_{m,k}\tau^2+O(\tau^4)\right),
\tag{2.4}
\]

where

\[
 \boxed{
 \eta^{\min}_{m,k}
 =\frac13-\frac1{2m+3}
 -\frac{(2m+2)(2m+3)}{3a_k^2}.}
\tag{2.5}
\]

At the unshifted old frequency the corresponding coefficient is

\[
 \boxed{
 \eta^{\mathrm{old}}_{m,k}
 =\frac13-\frac1{2m+3}
 -\frac{(2m+2)(2m+6)}{12a_k^2}.}
\tag{2.6}
\]

The distinction matters at a hard band endpoint: if an old zero lies exactly
at the endpoint and its shift points out of the permitted band, the constrained
minimum cannot follow (2.3), so the old-frequency coefficient rather than the
interior-minimum coefficient controls the quartic correction.

Two low-rung specializations are particularly simple. For \(m=1\), the roots
satisfy \(\sin a-a\cos a=0\), and

\[
 D_{1,k}^2=\frac9{a_k^2(1+a_k^2)},
 \quad
 \eta^{\min}_{1,k}=\frac2{15}-\frac{20}{3a_k^2},
 \quad
 \eta^{\mathrm{old}}_{1,k}=\frac2{15}-\frac8{3a_k^2}.
\tag{2.7}
\]

For \(m=2\), the roots satisfy
\((3-a^2)\sin a-3a\cos a=0\), and

\[
 D_{2,k}^2=\frac{225}{a_k^2(a_k^4+3a_k^2+9)},
 \quad
 \eta^{\min}_{2,k}=\frac4{21}-\frac{14}{a_k^2},
 \quad
 \eta^{\mathrm{old}}_{2,k}=\frac4{21}-\frac5{a_k^2}.
\tag{2.8}
\]

## 3. Compact-band condition number

Fix \(A>0\), with endpoints not equal to an old notch, and set

\[
 \lambda_{m,A}(\tau)=\min_{|a|\le A}W_\tau(a).
\tag{3.1}
\]

If the band contains no old zero, compactness and uniform convergence give

\[
 \lambda_{m,A}(\tau)
 \longrightarrow \min_{|a|\le A}F_m(a)^2>0.
\tag{3.2}
\]

If it contains at least one old zero, define

\[
 d_{m,A}=\min_{a_k<A}D_{m,k}.
\tag{3.3}
\]

There are only finitely many root neighborhoods in the fixed band. Away from
them \(F_m^2\) has a positive lower bound, while (2.4) controls each local
minimum. It follows that

\[
 \boxed{
 \lambda_{m,A}(\tau)
 =d_{m,A}^2\tau^2+O_{m,A}(\tau^4).}
\tag{3.4}
\]

Because \(Q_{m,S,\tau}\) is a probability carrier,

\[
 |\widehat Q_{m,S,\tau}(\omega)|\le1,
 \qquad \widehat Q_{m,S,\tau}(0)=1.
\tag{3.5}
\]

Thus the squared inversion condition number for the carrier multiplier on the
band is exactly \(\operatorname{Cond}_{m,A}=1/\lambda_{m,A}\), and

\[
 \boxed{
 \Delta_m(\tau)\operatorname{Cond}_{m,A}(\tau)
 \longrightarrow\frac{r_m}{d_{m,A}^2}.}
\tag{3.6}
\]

The limit makes the tradeoff unavoidable within this one-parameter positive
tilt: decreasing the energy excess by a factor forces the band condition
number to grow by the reciprocal factor.

If several old roots tie for \(d_{m,A}\), the smallest admissible quartic
coefficient selects the next-order minimum. The leading law (3.4) is unchanged.

## 4. High-frequency worsening

The fixed-order spherical-Bessel limiting form is

\[
 j_m(a)=a^{-1}\sin(a-m\pi/2)+O_m(a^{-2}).
\tag{4.1}
\]

Together with the zero spacing and derivative recurrence, this yields

\[
 \boxed{
 D_{m,k}\sim(2m+1)!!\,a_k^{-m-1}.}
\tag{4.2}
\]

Therefore the individual old-notch squared conditioning scale grows as

\[
 \boxed{D_{m,k}^{-2}\asymp_m a_k^{2m+2}.}
\tag{4.3}
\]

The exact-zero theorem is consequently not uniform as a frequency band grows.
At higher rungs it becomes progressively more ill-conditioned: the powers are
\(4,6,8,10,\ldots\) for \(m=1,2,3,4,\ldots\).

The external classical inputs are precisely separated. Reality and simplicity
of the Bessel zeros use
[DLMF §10.21(i)](https://dlmf.nist.gov/10.21#i). The fixed-order
large-argument formula uses
[DLMF §10.52(ii)](https://dlmf.nist.gov/10.52#ii). No novelty or priority is
claimed for those classical facts.

## 5. Relation to the beta field

For the translated beta detector, the \(m\)-th matched moment remains

\[
 \int t^mH_{m,S,\tau,X}(t)\,dt=(-1)^mm!B_0(X).
\tag{5.1}
\]

The tilt therefore does not erase the source-faithful beta prefix. But (0.7)
shows exactly why dividing by the local Fourier transform is dangerous: the
inverse multiplier near the former notches costs \(1/|\tau|\), and a growing
band incurs the additional polynomial loss (4.3). The frozen support/moment
reverse criterion avoids this division and remains valid for either tilt sign.

For the derivative detector itself, the floor at \(\omega_k\) acquires the
known multiplier \((2a_k/S)^{2m}\). That does not remove the carrier inversion
problem; it only changes which norm is being conditioned. Moreover,
\(\widehat{D^mQ}(0)=0\) to order \(m\), so the derivative detector has infinite
inversion condition number on every symmetric band containing the origin. The
finite condition theorem (3.6) is only for the carrier multiplier.

Nothing here proves cancellation between distinct beta translates. The theorem
quantifies a local analytic regularization and proves a no-free-lunch law for
its conditioning. It does not supply the arithmetic estimate needed by the RH
criterion.

## 6. Scope and firewalls

| statement | grade |
|---|---|
| exact even notch jet through quartic order | **PROVED EXACT** |
| pointwise floor-to-energy limit (0.7) | **PROVED EXACT** |
| universal rescaled profile (0.8) | **PROVED** |
| local minimum shift and quartic floor | **PROVED EXACT** |
| fixed compact-band condition law | **PROVED** |
| high-notch conditioning power | **PROVED FROM CLASSICAL ASYMPTOTICS** |
| zero-free transform implies uniform coercivity | **DISPROVED** |
| new beta-convolution cancellation | **NOT PROVED** |
| subpower detector estimate, RH, or GRH | **NOT PROVED** |

All \(\tau\to0\) limits fix \(m\), a notch index, or a compact band first. No
joint growing-\(m\), growing-\(A\), and shrinking-\(\tau\) assertion is made.

The Fourier tradeoff is the same for the two tilt signs. Their Laplace geometry
is not: only positive tilt moves the zero lattice into the left half-plane.

The notches in this packet are zeros of a compact carrier Fourier transform,
not zeros of \(\zeta\), an \(L\)-function, or xi.

## 7. Bounded replay

The producer:

- verifies the frozen spectral-tilt quartet by full Git blob ID;
- checks the even pointwise jet, energy/floor ratios, compact-band minimum
  algebra, quartic coefficients, and high-notch powers with exact rational
  arithmetic for \(1\le m\le4\);
- performs six tiny numerical root certificates, two each for \(m=1,2,3\),
  using the elementary spherical-Bessel recurrence, a fixed scan step, and 72
  bisections per root;
- uses those roots only as replay sanity checks, not as evidence for the
  analytic theorem;
- performs no beta sum, prime enumeration, zeta evaluation, random sampling,
  quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_spectral_near_notch_conditioning.py --check
python -O -B research/l-families/atlas/function_field/ffps_spectral_near_notch_conditioning.py --check
python -B -m unittest tests.test_ffps_spectral_near_notch_conditioning
python -O -B -m unittest tests.test_ffps_spectral_near_notch_conditioning
python -m ruff check research/l-families/atlas/function_field/ffps_spectral_near_notch_conditioning.py tests/test_ffps_spectral_near_notch_conditioning.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_spectral_near_notch_conditioning.py tests/test_ffps_spectral_near_notch_conditioning.py
~~~
