# Reflected beta kernels have identical energy and opposite carrier chirality

Status: **exact tilted-spline factorization, carrier-zero phase diagram,
Fourier/Gram mirror identity, and all-tilt fixed-order RH-equivalent prefix
energy; no beta-energy estimate, direct one-sided theorem in the carrier-gap
window, RH, or GRH result**

Bounded replay:
[ffps_beta_kernel_carrier_chirality.py](ffps_beta_kernel_carrier_chirality.py).
Canonical summary:
[ffps_beta_kernel_carrier_chirality.json](ffps_beta_kernel_carrier_chirality.json).

Frozen input: the fixed-support zero-free beta-energy ladder at commit
**3658d4c31cc866e15d48ab1fc9d8d119136da424**. Its four blobs are pinned
and checked before the bounded replay runs.

## 0. Outcome

For a real tilt \(a\), define the probability atom on \([0,1]\)

\[
 f_a(x)=
 \begin{cases}
  \displaystyle {a e^{ax}\over e^a-1},&a\ne0,\\[4pt]
  1,&a=0,
 \end{cases}
 \qquad 0\le x\le1.
\tag{0.1}
\]

Let

\[
 P_a=f_a*f_a,
 \qquad
 Q_{a,m}(x)=mP_a^{*m}(mx),
 \qquad
 J_{a,m}=DQ_{a,m}
\tag{0.2}
\]

for a fixed integer \(m\ge1\). Every \(J_{a,m}\) is a nonzero real compact
BV band-pass kernel on the same support \([0,2]\).

The atom has Laplace transform

\[
 \widehat f_a(s)
 ={a(e^{a-s}-1)\over(e^a-1)(a-s)},
\tag{0.3}
\]

with the removable interpretation at \(a=0\) and \(s=a\). Consequently

\[
\boxed{
 \widehat J_{a,m}(s)
 =s\widehat f_a(s/m)^{2m}.}
\tag{0.4}
\]

Besides the forced zero at \(s=0\), its carrier zeros are

\[
\boxed{
 s=m(a+2\pi ik),
 \qquad k\in\mathbf Z\setminus\{0\},}
\tag{0.5}
\]

each of multiplicity \(2m\). Thus the sign of \(a\) decides on which side
of the Mellin plane the zero lattice lies.

But that sign is completely invisible to the Fourier energy. Reflection
gives

\[
\boxed{
 f_{-a}(x)=f_a(1-x),
 \quad
 J_{-a,m}(x)=-J_{a,m}(2-x),}
\tag{0.6}
\]

and hence

\[
\boxed{
 |\widehat J_{-a,m}(it)|^2
 =|\widehat J_{a,m}(it)|^2
 \quad(t\in\mathbf R).}
\tag{0.7}
\]

The two kernels therefore have the same autocorrelation and the same
finite-prefix energy for every coefficient vector, even though their
nontrivial Laplace zeros have real parts \(-m|a|\) and \(+m|a|\).

For the literal beta source

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\tag{0.8}
\]

put

\[
 \mathcal E_{a,m}(X)
 =\int_{\mathbf R}
 \left|
  \sum_{n\le X}{\beta(n)\over\sqrt n}
  J_{a,m}(t-\log n)
 \right|^2dt.
\tag{0.9}
\]

Then for every fixed real \(a\) and fixed \(m\ge1\),

\[
\boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_{a,m}(X)=X^{o(1)}.}
\tag{0.10}
\]

For \(a\le0\), this follows directly from the frozen Mellin--Landau
argument because (0.5) is on or left of \(\Re s=0\). For \(a>0\), use
the exact energy identity

\[
 \mathcal E_{a,m}(X)=\mathcal E_{-a,m}(X)
\tag{0.11}
\]

and apply the safe negative-tilt criterion. In particular, prefix energy
can be RH-equivalent even when the kernel used to display it has carrier
zeros inside the open RH consumer strip.

This is a carrier-design theorem, not an estimate for (0.9).

## 1. Exact tilted-spline construction

Normalization in (0.1) follows from

\[
 \int_0^1e^{ax}\,dx={e^a-1\over a}.
\tag{1.1}
\]

For \(a\ne0\), direct integration gives

\[
 \int_0^1 f_a(x)e^{-sx}\,dx
 ={a\over e^a-1}{e^{a-s}-1\over a-s},
\tag{1.2}
\]

which is (0.3). Its \(a\to0\) limit is

\[
 \widehat f_0(s)={1-e^{-s}\over s}.
\tag{1.3}
\]

Because \(P_a=f_a*f_a\), the density \(P_a^{*m}\) is the law of a sum of
\(2m\) independent \(f_a\)-variables. The scaling in (0.2) is the law of
their sum divided by \(m\), so its support is \([0,2]\) for every \(m\).
It is continuous and vanishes at both endpoints. Differentiation creates
no boundary atom, and scaling the Laplace transform gives

\[
 \widehat Q_{a,m}(s)=\widehat f_a(s/m)^{2m},
 \qquad
 \widehat J_{a,m}(s)=s\widehat Q_{a,m}(s),
\tag{1.4}
\]

proving (0.4). The kernel is compact BV: at \(m=1\), it is the derivative
of the explicit continuous piecewise exponential-linear spline \(P_a\);
at \(m\ge2\), further convolution preserves this regularity. It is
nonzero by (0.4) and has mean zero because it is a compact derivative.

The numerator in (0.3) vanishes when

\[
 a-s=2\pi ik.
\tag{1.5}
\]

The \(k=0\) zero is canceled by the denominator. Substitution of \(s/m\)
in (1.5) proves (0.5), up to replacing \(k\) by \(-k\).

## 2. Fourier weight and the chirality identity

For \(a\ne0\), elementary absolute values in (0.3) give

\[
\boxed{
 |\widehat f_a(it)|^2
 ={a^2\bigl(\sinh^2(a/2)+\sin^2(t/2)\bigr)
   \over
   \sinh^2(a/2)(a^2+t^2)}.}
\tag{2.1}
\]

This depends on \(a\) only through \(|a|\). At \(a=0\), its continuous
limit is

\[
 |\widehat f_0(it)|^2
 =\left({\sin(t/2)\over t/2}\right)^2.
\tag{2.2}
\]

Equations (0.4) and (2.1) yield the exact ladder weight

\[
\boxed{
 w_{a,m}(t)
 :=|\widehat J_{a,m}(it)|^2
 =t^2|\widehat f_a(it/m)|^{4m}.}
\tag{2.3}
\]

For \(a\ne0\), (2.1) is strictly positive, so the only real zero in
(2.3) is the forced double weight-zero at \(t=0\). For \(a=0\), additional
zeros occur at

\[
 t=2\pi mk,
 \qquad k\in\mathbf Z\setminus\{0\}.
\tag{2.4}
\]

The exact reflection is stronger than the even formula. From (0.1),

\[
 f_{-a}(x)
 ={a e^{a(1-x)}\over e^a-1}
 =f_a(1-x).
\tag{2.5}
\]

Reflecting all \(2m\) summands around \(1/2\), then dividing their sum by
\(m\), proves

\[
 Q_{-a,m}(x)=Q_{a,m}(2-x).
\tag{2.6}
\]

Differentiation proves (0.6). On the full Laplace plane,

\[
\boxed{
 \widehat J_{-a,m}(s)
 =-e^{-2s}\widehat J_{a,m}(-s).}
\tag{2.7}
\]

Thus reflection reverses the carrier-zero lattice. On \(s=it\), the
exponential in (2.7) is a phase, proving (0.7).

If

\[
 \mathcal R_{a,m}(u)
 =\int_{\mathbf R}J_{a,m}(v)J_{a,m}(v+u)\,dv,
\tag{2.8}
\]

then Fourier inversion of (0.7), or a direct change of variables in
(2.8), gives

\[
\boxed{
 \mathcal R_{-a,m}(u)=\mathcal R_{a,m}(u).}
\tag{2.9}
\]

## 3. Exact finite-prefix isospectrality

The conclusion is not special to beta coefficients. For arbitrary finite
real coefficients \(c_j\) and shifts \(x_j\), define

\[
 F_{a,m}(t)=\sum_jc_jJ_{a,m}(t-x_j).
\tag{3.1}
\]

Finite Fubini and (2.8) give

\[
 \int_{\mathbf R}|F_{a,m}(t)|^2dt
 =\sum_{j,k}c_jc_k
  \mathcal R_{a,m}(x_j-x_k).
\tag{3.2}
\]

Equation (2.9) makes the right side invariant under \(a\mapsto-a\).
Taking \(c_n=\beta(n)/\sqrt n\) and \(x_n=\log n\) proves (0.11).

This identity is exact at every finite horizon. It does not arise from an
asymptotic comparison, a unitary change of the beta coefficients, or a
zero census.

## 4. Carrier phase diagram

The frozen beta consumer examines possible poles at

\[
 s=\rho-1/2,
 \qquad 0<\Re s<1/2,
\tag{4.1}
\]

coming from a hypothetical zeta zero with \(1/2<\Re\rho<1\). By (0.5),
the direct carrier is nonvanishing throughout this open strip in either
of the ranges

\[
\boxed{
 ma\le0
 \qquad\hbox{or}\qquad
 ma\ge1/2.}
\tag{4.2}
\]

At \(a=0\), the nontrivial carrier zeros lie on the boundary
\(\Re s=0\), although the real Fourier weight has the side notches (2.4).
When

\[
 0<ma<1/2,
\tag{4.3}
\]

the carrier lattice lies inside the consumer strip. The direct
Mellin--Landau proof for the \(J_{a,m}\) field then has a genuine logical
gap: a hypothetical pole at precisely one of these points could be
canceled by the carrier. No such alignment is asserted, and failure of RH
is not inferred.

The mirror repairs the *energy* criterion. For \(a>0\), the kernel with
tilt \(-a\) has every nontrivial carrier zero in the left half-plane and
has exactly the same prefix energy. This proves the reverse direction of
(0.10) for every positive \(a\), including (4.3).

The repair does not transfer an oriented one-sided assertion. Let

\[
 H_{a,m}(t)
 =\sum_{n\ge1}{\beta(n)\over\sqrt n}
  J_{a,m}(t-\log n).
\tag{4.4}
\]

In the direct-safe ranges (4.2), the frozen argument proves

\[
 \int_0^T(H_{a,m}(t))_-dt=e^{o(T)}
 \quad\Longrightarrow\quad\mathrm{RH}.
\tag{4.5}
\]

Inside (4.3), (4.5) is not claimed. Equality of autocorrelations does not
identify the Jordan parts or \(L^1\) norms of the two complete oriented
fields.

## 5. Proof of the all-tilt energy criterion

Under RH, the normalized beta summatory function obeys

\[
 \sum_{n\le x}{\beta(n)\over\sqrt n}=O_\delta(x^\delta)
\tag{5.1}
\]

for every \(\delta>0\). Fixed-kernel bounded-variation summation, exactly
as in the frozen packet, gives

\[
 \mathcal E_{a,m}(X)=X^{o(1)}
\tag{5.2}
\]

for every fixed \(a,m\).

Conversely, suppose (5.2). If \(a\le0\), the direct carrier is safe and
the frozen chain

~~~text
prefix L2 energy -> complete L1 -> one-sided Landau -> RH
~~~

applies to \(J_{a,m}\). If \(a>0\), (0.11) transfers (5.2) exactly to
\(J_{-a,m}\), whose carrier is safe. Applying the same chain there proves
RH. This completes (0.10).

## 6. Near-blind-spot law and design consequences

Nonzero tilt removes exact real side notches, but small tilt does not make
them harmless uniformly. At the former uniform-atom lattice
\(t=2\pi mk\), (2.1)--(2.3) give

\[
\boxed{
 w_{a,m}(2\pi mk)
 =(2\pi mk)^2
 \left({a^2\over a^2+(2\pi k)^2}\right)^{2m}.}
\tag{6.1}
\]

This is positive for \(a\ne0\) but can be extremely small. The theorem
therefore distinguishes three design properties:

1. real-frequency nonalignment;
2. a quantitative spectral floor;
3. complex-carrier safety for the Landau consumer.

They are not equivalent. The sign of \(a\) changes property 3 while
leaving properties 1, 2, the autocorrelation, and every finite energy
unchanged.

For the predecessor kernel, \(a=1\). Its reflected \(a=-1\) partner has
the exact same Gram problem and moves the carrier lattice from
\(\Re s=m\) to \(\Re s=-m\). The positive predecessor is already directly
safe, so reflection does not improve its theorem; it exposes the more
general isospectral mechanism.

## 7. Fixed-parameter firewall

- Both \(a\) and \(m\) are fixed independently of \(X,T\), every zeta
  zero, and every frequency.
- Constants may deteriorate as \(a\to0\), \(|a|\to\infty\), or
  \(m\to\infty\). No uniform two-parameter theorem is inferred.
- The all-tilt result concerns prefix \(L^2\) energy. It does not silently
  transfer a direct \(L^1\), Jordan-mass, or memberwise sign theorem across
  reflection.
- Carrier zeros inside (4.3) identify a gap in one proof coordinate, not
  a zeta zero or a failure of the energy criterion.
- Positive spectral weight and strict finite Gram positivity do not prove
  beta cancellation.

## 8. Claim ledger

| statement | grade |
|---|---|
| tilted atom normalization and transform | **PROVED EXACT** |
| fixed-support compressed spline ladder | **PROVED EXACT** |
| carrier zero lattice and phase diagram | **PROVED EXACT** |
| reflection and Laplace chirality (0.6)--(2.7) | **PROVED EXACT** |
| Fourier weight / autocorrelation mirror identity | **PROVED EXACT** |
| arbitrary finite-prefix energy isospectrality | **PROVED EXACT** |
| all-real-tilt fixed-order RH energy criterion (0.10) | **PROVED FROM FROZEN RH/ENERGY/LANDAU ARGUMENT** |
| direct one-sided Landau criterion in (4.2) | **PROVED FROM FROZEN ARGUMENT** |
| direct one-sided criterion inside (4.3) | **NOT CLAIMED** |
| any beta-energy or off-diagonal estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

Equivalent criteria for RH are common. No external novelty claim is made
without a dedicated literature comparison.

## 9. Bounded replay

The producer checks the four frozen blobs, orders \(1\) through \(6\), six
declared tilts, six bounded nonzero frequencies per row, the exact
tilt-mirror weight identity, the direct-carrier phase classification, and
the uniform-atom side-notch limit. Floating-point values are regression
checks for exact formulas proved above.

It evaluates no zeta zero, numerical zeta value, prime interval, curve,
random sample, or contour integral.

~~~text
python -B research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py --check
python -B -O research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py --check
python -B -m unittest tests.test_ffps_beta_kernel_carrier_chirality
python -B -O -m unittest tests.test_ffps_beta_kernel_carrier_chirality
python -B -m ruff check research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py tests/test_ffps_beta_kernel_carrier_chirality.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_beta_kernel_carrier_chirality.py tests/test_ffps_beta_kernel_carrier_chirality.py
~~~
