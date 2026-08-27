# Compact carrier zeros can be flipped without changing beta energy

Status: **exact constructive finite-zero surgery for compact BV kernels,
support/mean/autocorrelation/Gram invariance, and finite carrier-defect
repair; no arbitrary infinite zero flip, beta-energy estimate, RH, or GRH
result**

Bounded replay:
[ffps_compact_kernel_carrier_zero_flip.py](ffps_compact_kernel_carrier_zero_flip.py).
Canonical summary:
[ffps_compact_kernel_carrier_zero_flip.json](ffps_compact_kernel_carrier_zero_flip.json).

Frozen input: the explicit tilted-spline chirality theorem at commit
**b0892f2ac6af5bc97010bc281118601547243148**. Its complete quartet is
pinned by Git blob ID.

## 0. Outcome

Let (K) be a real compact BV function supported on ([0,L]), and set

\[
 F(s)=\int_0^L K(x)e^{-sx}\,dx.
\tag{0.1}
\]

Suppose (z) is a carrier zero with (Re z\ne0):

\[
 F(z)=0.
\tag{0.2}
\]

Define the compact primitive

\[
 h_z(x)
 =e^{zx}\int_0^xe^{-zu}K(u)\,du,
 \qquad 0\le x\le L,
\tag{0.3}
\]

and extend it by zero outside ([0,L]). Because of (0.2), both endpoint
values vanish. The one-zero flip is

\[
\boxed{
 K^{[z]}(x)=K(x)+2\Re(z)h_z(x).}
\tag{0.4}
\]

Its transform is

\[
\boxed{
 F^{[z]}(s)
 =F(s){s+\overline z\over s-z}.}
\tag{0.5}
\]

The apparent pole is removable by (0.2). Equation (0.5) removes one copy
of the zero at (z) and inserts one at

\[
 -\overline z.
\tag{0.6}
\]

On the Fourier axis,

\[
\boxed{
 \left|{it+\overline z\over it-z}\right|=1,}
\tag{0.7}
\]

so the surgery preserves

\[
\boxed{
 |F^{[z]}(it)|=|F(it)|
 \qquad(t\in\mathbf R).}
\tag{0.8}
\]

For a real zero, (0.4) is already real. For a nonreal zero of a real
kernel, perform the two flips (z,overline z). The final kernel is real,
compact BV, supported on the same interval, and has transform

\[
\boxed{
 F^{[z,\bar z]}(s)
 =F(s)
 { (s+\overline z)(s+z)
  \over
   (s-z)(s-\overline z)}.}
\tag{0.9}
\]

Thus any finite conjugation-stable multiset of right-half-plane carrier
zeros can be moved to the left half-plane without changing the Fourier
magnitude, autocorrelation, or any finite translate Gram energy.

This is a finite spectral-factor surgery theorem. It does not assert that
an arbitrary infinite carrier-zero set can be flipped by a convergent
product.

## 1. The ODE proof

Differentiating (0.3) gives

\[
 h_z'(x)-zh_z(x)=K(x).
\tag{1.1}
\]

At the right endpoint,

\[
 h_z(L)=e^{zL}F(z)=0,
\tag{1.2}
\]

while (h_z(0)=0) directly. Therefore its extension by zero has no
boundary delta in the distributional derivative. If

\[
 H_z(s)=\int_0^Lh_z(x)e^{-sx}\,dx,
\tag{1.3}
\]

then transforming (1.1) gives

\[
 (s-z)H_z(s)=F(s).
\tag{1.4}
\]

Now transform (0.4):

\[
\begin{aligned}
 F^{[z]}(s)
 &=F(s)+(z+\overline z)H_z(s)\\
 &=F(s)\left(1+{z+\overline z\over s-z}\right)\\
 &=F(s){s+\overline z\over s-z},
\end{aligned}
\tag{1.5}
\]

which proves (0.5).

The regularity assertion is also constructive. A compact BV function is
bounded and integrable. Equation (0.3) makes (h_z) compact absolutely
continuous; (1.1) shows that its derivative is BV. Hence (0.4) is compact
BV on the same support. No Paley--Wiener existence theorem is needed.

## 2. Fourier and Gram invariance

Write (z=a+ib). On (s=it),

\[
 |it+\overline z|^2
 =a^2+(t-b)^2
 =|it-z|^2,
\tag{2.1}
\]

proving (0.7)--(0.8). If

\[
 R_K(u)=\int_{\mathbf R}K(v)\overline{K(v+u)}\,dv,
\tag{2.2}
\]

then its Fourier transform is (|F(it)|^2). Therefore

\[
\boxed{
 R_{K^{[z]}}=R_K.}
\tag{2.3}
\]

For arbitrary finite complex coefficients (c_j) and real shifts (x_j),
finite Fubini gives

\[
 \int_{\mathbf R}
 \left|\sum_jc_jK(t-x_j)\right|^2dt
 =\sum_{j,k}c_j\overline{c_k}R_K(x_j-x_k).
\tag{2.4}
\]

Replacing (K) by its flip leaves the right side unchanged. In
particular, for the beta coefficients and logarithmic shifts,

\[
\boxed{
 \int\left|
  \sum_{n\le X}{\beta(n)\over\sqrt n}K(t-\log n)
 \right|^2dt
 =
 \int\left|
  \sum_{n\le X}{\beta(n)\over\sqrt n}K^{[z]}(t-\log n)
 \right|^2dt.}
\tag{2.5}
\]

This identity is exact at every finite (X).

If (K) has mean zero, then (F(0)=0). Since (z\ne0), the multiplier
in (0.5) is finite at zero, and

\[
 F^{[z]}(0)=0.
\tag{2.6}
\]

Thus the band-pass condition is preserved as well.

## 3. Keeping the output real

For real (K), carrier zeros occur in conjugate pairs. A flip at one
nonreal zero may produce a complex intermediate kernel. Flipping its
conjugate next multiplies the transform by

\[
 B_{z,\bar z}(s)
 ={s^2+2\Re(z)s+|z|^2
   \over
   s^2-2\Re(z)s+|z|^2}.
\tag{3.1}
\]

The rational function has real coefficients and unit modulus on the
imaginary axis. The final transform again satisfies

\[
 F^{[z,\bar z]}(\overline s)
 =\overline{F^{[z,\bar z]}(s)},
\tag{3.2}
\]

so the final compact kernel is real. Repeated zeros are handled by
repeating the same elementary surgery up to their multiplicity.

Flipping a finite conjugation-stable multiset is therefore a finite
composition of support-preserving BV operations. Every intermediate
denominator is canceled by the zero being flipped.

## 4. A literal carrier-gap example

Let (K_0) be piecewise constant on ([0,3]), with weights

\[
 (c_0,c_1,c_2)
 =\left({3\over4},-{7\over4},1\right)
\tag{4.1}
\]

on the successive unit intervals. Its transform is

\[
 F_0(s)
 ={1-e^{-s}\over s}
 \left({3\over4}-{7\over4}e^{-s}+e^{-2s}\right).
\tag{4.2}
\]

The coefficient polynomial factors exactly:

\[
 {3\over4}-{7\over4}y+y^2
 =(y-1)(y-3/4).
\tag{4.3}
\]

The root (y=1) gives the mean-zero condition

\[
 c_0+c_1+c_2=0.
\tag{4.4}
\]

The second root gives the real carrier zero

\[
 z_0=\log(4/3),
 \qquad
 0<z_0<1/2.
\tag{4.5}
\]

Thus (K_0) has a literal zero inside the open Mellin--Landau consumer
strip. Applying (0.4) with (z=z_0) moves this zero to
(-\log(4/3)), keeps support ([0,3]), and leaves the entire Fourier
weight unchanged.

The replay verifies (4.3)--(4.5) in the exact variable
(y=e^{-z_0}=3/4) and checks the unit-modulus identity at six bounded
frequencies. The proof is (0.3)--(1.5), not numerical quadrature.

## 5. Finite carrier-defect repair

Because (F) is entire and not identically zero, it has only finitely many
zeros in a compact rectangle. Fix a declared height (T) and margin
(0<\delta<1/4), and consider

\[
 \mathcal Z_{T,\delta}
 =\{z:F(z)=0,
      \ \delta\le\Re z\le1/2-\delta,
      \ |\Im z|\le T\}.
\tag{5.1}
\]

Flip this finite multiset, including multiplicities and conjugates. The
resulting real compact BV kernel:

- has the same support and mean;
- has exactly the same autocorrelation and beta prefix energy;
- has no carrier zero left in the rectangle (5.1);
- introduces only the reflected zeros in the left half-plane.

This is a zero-independent repair in the relevant sense: the required
input is the fixed kernel's own carrier divisor, never a zeta-zero list.

If a fixed kernel has only finitely many zeros in the whole open strip

\[
 0<\Re s<1/2,
\tag{5.2}
\]

then flipping all of them produces a globally carrier-safe compact BV
kernel with exactly the same Gram problem. For an infinite strip divisor,
the finite theorem applies at every declared height, but a single
all-height kernel requires additional convergence.

## 6. What the surgery does and does not transfer

The theorem cleanly separates two detector layers:

~~~text
Fourier magnitude / autocorrelation / prefix L2 energy
    -> unchanged exactly;

complex Laplace carrier divisor
    -> changed by explicit zero reflection;

oriented complete field / L1 / Jordan negative mass
    -> generally changed and not identified.
~~~

Hence a carrier blind spot is not an invariant of the arithmetic quadratic
form. It can be an artifact of the chosen spectral factor. Conversely,
proving a beta-energy estimate remains exactly as hard after the surgery,
because (2.5) is equality, not domination.

The construction can help another agent in three ways:

1. remove finitely many known kernel-carrier cancellations before applying
   a finite-height zero-tube or Mellin argument;
2. replace a globally finite carrier defect by an energy-identical safe
   kernel;
3. distinguish a genuine arithmetic obstruction from a removable choice
   of compact spectral factor.

It does not preserve a canonical integrated-detector interpretation
automatically. If the exact kernel shape is part of an external source
contract, the flipped kernel must be recorded as a new consumer, not
silently substituted.

## 7. Infinite-divisor frontier

Formally flipping infinitely many zeros suggests a product

\[
 \prod_z{s+\overline z\over s-z}.
\tag{7.1}
\]

The finite proof does not establish convergence, exponential type,
bounded variation of the inverse transform, or preservation of one-sided
support for (7.1). These are load-bearing. Reflection of the whole kernel,
as in the predecessor chirality theorem, is one special global symmetry
which flips an entire explicit divisor safely. A general infinite-product
spectral factorization is left open.

## 8. Claim ledger

| statement | grade |
|---|---|
| one-zero ODE construction (0.3)--(0.5) | **PROVED EXACT** |
| support, BV regularity, and mean preservation | **PROVED EXACT** |
| carrier motion (z\mapsto-\bar z) | **PROVED EXACT** |
| Fourier magnitude and autocorrelation invariance | **PROVED EXACT** |
| arbitrary finite translate/beta Gram invariance | **PROVED EXACT** |
| real conjugate-pair and finite-multiset surgery | **PROVED EXACT** |
| finite compact-rectangle carrier repair | **PROVED EXACT** |
| full-strip repair for a finite strip divisor | **PROVED EXACT** |
| arbitrary infinite carrier-zero flip | **NOT PROVED** |
| (L^1) or Jordan-mass invariance | **FALSE IN GENERAL / NOT CLAIMED** |
| any beta-energy estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

This is closely related in spirit to spectral-factor and phase-retrieval
zero flipping. No external novelty claim is made without a dedicated
literature comparison.

## 9. Bounded replay

The replay pins the predecessor quartet; checks the toy mean and
right-half-plane root exactly over (mathbf Q); checks one-zero and
conjugate-pair unit-modulus multipliers at six frequencies and three
declared complex zeros; and verifies the toy weight equality. It uses no
root finder, quadrature, zeta zero, numerical zeta value, prime, curve, or
random sample.

~~~text
python -B research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.py --check
python -B -O research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.py --check
python -B -m unittest tests.test_ffps_compact_kernel_carrier_zero_flip
python -B -O -m unittest tests.test_ffps_compact_kernel_carrier_zero_flip
python -B -m ruff check research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.py tests/test_ffps_compact_kernel_carrier_zero_flip.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_compact_kernel_carrier_zero_flip.py tests/test_ffps_compact_kernel_carrier_zero_flip.py
~~~
