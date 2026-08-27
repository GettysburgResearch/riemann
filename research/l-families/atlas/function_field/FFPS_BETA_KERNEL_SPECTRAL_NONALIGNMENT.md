# The beta boundary notches admit exact zero-independent repairs

Status: **exact frozen-kernel transform and zero-divisor theorem, exact
finite-window scalar repair, exact all-height two-channel repair, and exact
all-height scalar compact-BV construction; no Perron estimate, zeta-zero
computation, simplicity theorem, RH, or GRH result**

Bounded replay:
[ffps_beta_kernel_spectral_nonalignment.py](ffps_beta_kernel_spectral_nonalignment.py).
Canonical summary:
[ffps_beta_kernel_spectral_nonalignment.json](ffps_beta_kernel_spectral_nonalignment.json).

Frozen sources are the beta-boundary quartet at
**b870366141fe8d5f43d5b81f6e50a67d2a888070**, the band-pass energy
quartet at **05aaabe69060c24c8db4ca33c350e109231960f1**, and the zero-tube
residue quartet at **3a1d92b57b6234c046c2abf42d9ab15d03173838**.
The replay pins all twelve imported blobs. It uses no zeta ordinate,
numerical zeta-value evaluation or data, prime, curve, or numerical root
finder. Section 4 does use an elementary analytic proof of the exact sign
\(\zeta(1/2)<0\).

## 0. Outcome

Put \(L=\log2\), and write

\[
 \mathcal K(s)
 =\int_{\mathbf R}K_{\rm bd}(x)e^{-sx}\,dx.
\tag{0.1}
\]

The literal frozen boundary kernel has the exact transform

\[
\boxed{
 \mathcal K(s)=
 { (1-2^{-s})^2(1-2^{1/2-s})^2
   (s-1)(10s+3)
  \over
   2s^2(s-1/2)}.}
\tag{0.2}
\]

All apparent singularities are removable. Its real Fourier zeros are
exactly

\[
\boxed{
 t={2\pi k\over L},
 \qquad k\in\mathbf Z\setminus\{0\}.}
\tag{0.3}
\]

Each zero has amplitude multiplicity two and autocorrelation-weight
multiplicity four. Thus the positive-weight assumption in the zero-tube
packet is genuinely nontrivial for the literal source kernel.

There are three zero-independent repairs.

### A scalar channel on a prescribed window

For \(T>0\), put

\[
 a_T={1\over1+T},
 \qquad
 C_T=\Delta_{a_TL}
 \bigl[K_{\rm bd}(\,\cdot/a_T)\bigr].
\tag{0.4}
\]

Then

\[
\boxed{
 |\widehat C_T(t)|^2>0
 \qquad(0<|t|\le T),}
\tag{0.5}
\]

and its Laplace carrier is nonzero throughout
\(0<\Re s<1/2\). The scale depends only on the declared height \(T\),
never on a zero.

### Two source-locked channels at every height

If \(C_a\) denotes the construction in (0.4) at a general scale \(a\),
then

\[
\boxed{
 w_\oplus(t)
 =|\widehat C_1(t)|^2
  +|\widehat C_{1/\sqrt2}(t)|^2
 >0
 \qquad(t\ne0).}
\tag{0.6}
\]

This is a vector/direct-sum energy, equivalently the sum of two scalar
Perron inners. It is not represented here as one scalar autocorrelation.

### One universal scalar channel at every height

Define

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+,
 \qquad
 K_*(x)=\Phi'(x)\quad\text{a.e.}
\tag{0.7}
\]

Then \(K_*\) is real, compact, BV, and mean zero, and

\[
\boxed{
 |\widehat K_*(t)|^2
 ={16t^2
   \bigl(\sinh^2(1/2)+\sin^2(t/2)\bigr)^2
  \over(1+t^2)^2}
 >0
 \qquad(t\ne0).}
\tag{0.8}
\]

Its Laplace carrier is nonzero throughout the open RH strip. An elementary
alternating-eta argument gives \(\zeta(1/2)<0\), so no critical-line zero
has ordinate zero. Hence (0.8) is positive at every critical-line zero,
at every height, with no zero-dependent choice.

These results discharge a spectral-nonalignment interface in the local
zero-tube theorem. They do not prove the required \(O_T(1/c)\) Perron
bound, move a contour, control \(T\to\infty\), prove simplicity, or prove
RH.

## 1. The frozen transform and its complete zero divisor

The source-locked boundary packet gives

\[
 K_{\rm bd}
 =(1-\tau_L)^2(1-\sqrt2\,\tau_L)^2w,
 \qquad
 w(t)=\mathbf1_{t\ge0}(13+3t-8e^{t/2}).
\tag{1.1}
\]

Initially where the tail integrals converge,

\[
\begin{aligned}
 \widehat w(s)
 &= {13\over s}+{3\over s^2}-{8\over s-1/2}\\
 &= {(s-1)(10s+3)\over s^2(2s-1)}.
\end{aligned}
\tag{1.2}
\]

Translation multiplies the Laplace transform by
\(e^{-Ls}=2^{-s}\). Equations (1.1)--(1.2) prove (0.2) on an initial
half-plane and then everywhere by continuation. This also agrees with the
frozen identity \(\mathcal K=M_{\rm ext}/s\).

The five shift coefficients in (1.1) are

\[
 1,\quad -2-2\sqrt2,\quad 3+4\sqrt2,\quad
 -4-2\sqrt2,\quad2.
\tag{1.3}
\]

They are replayed in exact \(\mathbf Q(\sqrt2)\) arithmetic.

Because \(K_{\rm bd}\) is compact, (0.2) is entire after removable values
are filled. Its complete zero divisor is

\[
\begin{array}{c|c}
\text{zero}&\text{multiplicity}\\ \hline
2\pi ik/L,\ k\ne0&2\\
1/2+2\pi ik/L,\ k\ne0&2\\
1/2&1\\
1&1\\
-3/10&1.
\end{array}
\tag{1.4}
\]

At \(s=0\), the double zero of \(1-2^{-s}\) cancels \(s^2\), and

\[
 \mathcal K(0)=3(1-\sqrt2)^2L^2\ne0.
\tag{1.5}
\]

At \(s=1/2\), the double zero of \(1-2^{1/2-s}\) cancels the simple
denominator and leaves a simple zero. No rows in (1.4) collide.

On the Fourier axis,
\(\widehat K_{\rm bd}(t)=\mathcal K(it)\). For \(t\ne0\),

\[
\boxed{
 |\widehat K_{\rm bd}(t)|^2
 ={4\sin^4(Lt/2)
   (3-2\sqrt2\cos Lt)^2
   (t^2+1)(100t^2+9)
  \over
   t^4(t^2+1/4)}.}
\tag{1.6}
\]

Every factor except \(\sin^4(Lt/2)\) is strictly positive, because

\[
 3-2\sqrt2\cos Lt
 \ge3-2\sqrt2
 =(\sqrt2-1)^2>0.
\tag{1.7}
\]

This proves (0.3) and its multiplicities. The removable value at zero is

\[
 |\widehat K_{\rm bd}(0)|^2
 =9(1-\sqrt2)^4L^4>0.
\tag{1.8}
\]

### A multiplier no-go

For a time translate,

\[
 \widehat{\tau_hK_{\rm bd}}(t)
 =e^{-iht}\widehat K_{\rm bd}(t).
\tag{1.9}
\]

Thus translation changes no weight. More generally, a finite translate
polynomial, finite difference, or compact convolution multiplies
\(\widehat K_{\rm bd}\) by an entire Fourier multiplier. It can preserve
or increase an inherited zero's multiplicity, but cannot divide that zero
away. Dilation, a direct sum, and replacement by a separately designed
kernel are not covered by this no-go; those are exactly the repairs below.

## 2. A source-locked scalar repair on a finite window

For \(0<a\le1\), define

\[
 F_a(x)=K_{\rm bd}(x/a),
 \qquad
 C_a=\Delta_{aL}F_a
 ={F_a-\tau_{aL}F_a\over aL}.
\tag{2.1}
\]

Scaling and translation give

\[
\boxed{
 \widehat C_a(t)
 ={1-e^{-iaLt}\over L}
 \widehat K_{\rm bd}(at).}
\tag{2.2}
\]

The difference lattice and the dilated frozen-kernel lattice coincide
exactly:

\[
 Z(C_a)={2\pi\over aL}\mathbf Z.
\tag{2.3}
\]

The amplitude zero has order one at zero. At each nonzero lattice point,
the simple difference zero and double frozen zero combine to exact order
three.

For \(a=a_T=(1+T)^{-1}\),

\[
 a_TT={T\over1+T}<1,
\tag{2.4}
\]

and the first nonzero lattice point satisfies

\[
 {2\pi\over a_TL}>T.
\tag{2.5}
\]

This proves (0.5) without querying a zeta zero.

The Laplace carrier is

\[
 \widehat C_a(s)
 ={1-e^{-aLs}\over L}\mathcal K(as).
\tag{2.6}
\]

The first factor has zeros only on \(\Re s=0\). The other zeros have real
parts

\[
 0,\qquad {1\over2a},\qquad {1\over a},
 \qquad -{3\over10a}.
\tag{2.7}
\]

For \(0<a\le1\), none lies in \(0<\Re s<1/2\). Thus the replacement
preserves the off-line-pole carrier used by the Mellin--Landau consumer.
This is a carrier theorem, not a bound for the resulting beta field.

## 3. Two fixed source-locked channels cover all heights

Take

\[
 a_1=1,
 \qquad
 a_2={1\over\sqrt2}.
\tag{3.1}
\]

A nonzero common zero of their lattices would give nonzero integers
\(k,m\) with

\[
 {2\pi k\over L}
 ={2\pi m\sqrt2\over L},
 \qquad\text{hence}\qquad k=m\sqrt2.
\tag{3.2}
\]

Squaring gives \(k^2=2m^2\). Infinite descent forces \(k=m=0\), a
contradiction. Therefore the lattices meet only at zero, proving (0.6).
Both scales satisfy the strip statement (2.7).

The distinction is load-bearing:

~~~text
one scalar compact kernel             not claimed in this section
two scalar kernels / vector kernel    proved
sum of two autocorrelation energies   proved
strict positive weight for t != 0     proved
~~~

No scalar compact spectral factorization of \(w_\oplus\) is asserted.

## 4. One universal compact scalar kernel covers all heights

The universal construction is independent of the frozen kernel but fits
the zero-tube packet's hypothesis of one fixed real compact band-pass
kernel. Let

\[
 \Phi(x)=e^{x-1}(1-|x-1|)_+.
\tag{4.1}
\]

It is continuous, supported on \([0,2]\), and vanishes at both endpoints.
Its almost-everywhere derivative is

\[
 K_*(x)=
 \begin{cases}
 e^{x-1}(x+1),&0<x<1,\\
 e^{x-1}(1-x),&1<x<2,\\
 0,&\text{otherwise}.
 \end{cases}
\tag{4.2}
\]

Hence \(K_*\) is real, compact, BV, and belongs to \(L^1\cap L^2\).
Since it is the derivative of a compact continuous function,

\[
 \int_{\mathbf R}K_*(x)\,dx=0.
\tag{4.3}
\]

The two exact piece masses are

\[
 \int_{-1}^0e^y(y+2)\,dy=1,
 \qquad
 \int_0^1-e^yy\,dy=-1.
\tag{4.4}
\]

The centered tent factors as

\[
 (1-|y|)_+
 =\mathbf1_{[-1/2,1/2]}*
  \mathbf1_{[-1/2,1/2]}(y).
\tag{4.5}
\]

Exponential tilting, translation, and (4.5) give

\[
 \widehat\Phi(s)
 =4e^{-s}{\sinh^2((s-1)/2)\over(s-1)^2}.
\tag{4.6}
\]

Integration by parts has no endpoint term, so

\[
\boxed{
 \widehat K_*(s)
 =4s e^{-s}
 {\sinh^2((s-1)/2)\over(s-1)^2}.}
\tag{4.7}
\]

The apparent value at \(s=1\) is removable and nonzero. The complete zero
set is

\[
 s=0\quad\text{(simple)},
 \qquad
 s=1+2\pi ik,\quad k\ne0
 \quad\text{(double)}.
\tag{4.8}
\]

Thus the carrier is zero-free in \(0<\Re s<1/2\). On the Fourier axis,

\[
 |\sinh(-1/2+it/2)|^2
 =\sinh^2(1/2)+\sin^2(t/2),
\tag{4.9}
\]

and (4.7) gives (0.8). The forced band-pass zero at \(t=0\) is simple in
amplitude and double in weight; no other real zero exists.

For \(0<\sigma<1\), the alternating eta series converges and

\[
 \eta(\sigma)
 =\sum_{n\ge1}{(-1)^{n-1}\over n^\sigma}>0.
\tag{4.10}
\]

Pairing each odd term with the following smaller even term proves
positivity. By continuation,

\[
 \eta(\sigma)
 =(1-2^{1-\sigma})\zeta(\sigma).
\tag{4.11}
\]

At \(\sigma=1/2\), the first factor is negative, so

\[
 \zeta(1/2)<0.
\tag{4.12}
\]

Therefore no critical-line zero has ordinate zero, and
\(w_*(\gamma)>0\) at every critical-line zero.

### A zero-free smoothing ladder

For a fixed integer \(m\ge1\), set

\[
 K_m=D(\Phi^{*m}).
\tag{4.13}
\]

Then \(K_m\) is real, compact, BV, and mean zero, with

\[
 \widehat K_m(s)=s\widehat\Phi(s)^m.
\tag{4.14}
\]

Its real Fourier zero set remains exactly \(\{0\}\), its carrier remains
zero-free in the open RH strip, and

\[
 |\widehat K_m(t)|^2
 =O(|t|^{2-4m}).
\tag{4.15}
\]

Thus arbitrary fixed polynomial high-frequency decay is available without
creating a nonzero real spectral notch.

## 5. Consequence for the zero-tube theorem

The frozen local theorem says that a critical zero
\(\rho=1/2+i\gamma\) of multiplicity \(m\), at a positive-weight
ordinate, contributes

\[
 \binom{2m-2}{m-1}
 Q_\rho w(\gamma)c^{1-2m}
\tag{5.1}
\]

to the real-\(c\), height-truncated Perron inner. The three repairs make
the positivity premise explicit:

\[
\begin{array}{c|c|c}
\text{construction}&\text{range}&\text{dependence}\\ \hline
C_T&0<|t|\le T&T\text{ only}\\
C_1\oplus C_{1/\sqrt2}&t\ne0&\text{none}\\
K_*&t\ne0&\text{none}.
\end{array}
\tag{5.2}
\]

Accordingly, on a guarded finite window, the conditional estimate

\[
 \mathfrak P_T(c)=O_T(1/c)
\tag{5.3}
\]

with \(C_T\) or \(K_*\) would force simplicity of every critical-line zero
in that window by the frozen residue law. The two-channel version uses the
sum of the corresponding Perron inners.

Equation (5.3) is not proved here. Neither is the contour displacement,
the \(T\to\infty\) tail, the absence of off-line zeros, or an
individual-zeta estimate. The exact achievement is narrower: spectral
weight can no longer miss a critical-line zero.

## 6. Claim ledger

| statement | grade |
|---|---|
| exact frozen transform (0.2) | **PROVED FROM THE FROZEN CAUSAL FORMULA** |
| complete Laplace zero divisor (1.4) | **PROVED EXACT** |
| real Fourier lattice and multiplicities | **PROVED EXACT** |
| translate/multiplier no-go | **PROVED EXACT** |
| scalar finite-window repair \(C_T\) | **PROVED EXACT, ZERO-INDEPENDENT** |
| two-channel all-height positivity | **PROVED BY IRRATIONAL-LATTICE DESCENT** |
| universal scalar kernel \(K_*\) | **PROVED EXACT** |
| zero-free smoothing ladder \(K_m\) | **PROVED EXACT** |
| positivity at every critical-line zero | **PROVED USING \(\zeta(1/2)<0\)** |
| \(O_T(1/c)\) Perron estimate | **NOT PROVED** |
| simplicity of any actual zeta zero | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

## 7. Bounded replay

The replay checks all twelve frozen blobs, the five
\(\mathbf Q(\sqrt2)\) shift coefficients, the exact rational tail
factorization, exact finite-window scale certificates, bounded integer
checks of the irrational-lattice conclusion, the two piece masses in
(4.4), bounded nonzero samples of (0.8), and all scope/resource fences.

The infinite zero-divisor classifications, irrationality descent, and
positivity proofs are analytic proofs in this document. Bounded numerical
samples are regression checks, not their logical basis. No primitive zeta
data is replayed.

~~~text
python -B research/l-families/atlas/function_field/ffps_beta_kernel_spectral_nonalignment.py --check
python -B -O research/l-families/atlas/function_field/ffps_beta_kernel_spectral_nonalignment.py --check
python -B -m unittest tests.test_ffps_beta_kernel_spectral_nonalignment
python -B -O -m unittest tests.test_ffps_beta_kernel_spectral_nonalignment
python -B -m ruff check research/l-families/atlas/function_field/ffps_beta_kernel_spectral_nonalignment.py tests/test_ffps_beta_kernel_spectral_nonalignment.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_beta_kernel_spectral_nonalignment.py tests/test_ffps_beta_kernel_spectral_nonalignment.py
~~~
