# Finite spectral-factor surgery for compact kernels

Status: **exact finite rational all-pass classification, exact abelian
reflection-orbit divisor-flow calculus, exact real/mean/support/BV gates,
and an explicit Jordan--\(L^1\) noninvariance theorem; no arbitrary infinite
product, global minimum-phase construction, beta-energy estimate, RH, or GRH
result**

Bounded replay:
[ffps_compact_kernel_finite_spectral_factor_surgery.py](ffps_compact_kernel_finite_spectral_factor_surgery.py).
Canonical summary:
[ffps_compact_kernel_finite_spectral_factor_surgery.json](ffps_compact_kernel_finite_spectral_factor_surgery.json).

Frozen provenance:

| source | commit | git blob | role |
|---|---|---|---|
| <code>FFPS_COMPACT_KERNEL_CARRIER_ZERO_FLIP.md</code> | <code>011ad6d3f</code> | <code>4d08a600643e2189a3ba4c9600d9b88d4de1105c</code> | one-zero ODE, all-pass multiplier, and corrected zero-mean scope |
| <code>ffps_compact_kernel_carrier_zero_flip.py</code> | <code>011ad6d3f</code> | <code>f3b3759ff49ca1c1343b7eb9539031b650c8f7ac</code> | bounded predecessor producer |
| <code>ffps_compact_kernel_carrier_zero_flip.json</code> | <code>011ad6d3f</code> | <code>5ddeb3284e02d41d87583772fb92147e02781578</code> | corrected predecessor fixture |
| <code>test_ffps_compact_kernel_carrier_zero_flip.py</code> | <code>011ad6d3f</code> | <code>3e3c6859b9219946ece4a44575c5bdd7fa6b5281</code> | predecessor tests |
| <code>FFPS_BETA_KERNEL_CARRIER_CHIRALITY.md</code> | <code>011ad6d3f</code> | <code>ab15fb0a719545e66417985d32609f9f182e81c9</code> | global reflection symmetry and energy/chirality separation |
| <code>ffps_beta_kernel_carrier_chirality.py</code> | <code>011ad6d3f</code> | <code>da6c4702268d9211c382ee9a0454c81fa2ad60f9</code> | chirality producer |
| <code>ffps_beta_kernel_carrier_chirality.json</code> | <code>011ad6d3f</code> | <code>66fe36ecde1acf70a83d0d67e784153c64bd6ce9</code> | chirality fixture |
| <code>test_ffps_beta_kernel_carrier_chirality.py</code> | <code>011ad6d3f</code> | <code>365f8c2f109433ce13e419c03a82669194e7d48a</code> | chirality tests |

The corrected one-zero predecessor already restricts its mean claim to
zero-mean inputs. This packet rederives the law and strengthens it to the
exact nonzero-mean phase formula in Section 4.

## 0. Outcome

Let \(K\not\equiv0\) be a complex compact BV function supported in the
declared interval \([0,L]\), and put

\[
 F(s)=\int_0^L K(x)e^{-sx}\,dx.
\tag{0.1}
\]

For an off-axis zero \(z\), define the reflection

\[
 Rz=-\overline z
\tag{0.2}
\]

and the elementary normalized all-pass factor

\[
 B_z(s)={s+\overline z\over s-z}.
\tag{0.3}
\]

If \(F(z)=0\), the pole in \(F B_z\) is removable and there is a compact BV
kernel \(T_zK\), supported in the same declared interval, whose transform is

\[
 \widehat {T_zK}(s)=F(s)B_z(s).
\tag{0.4}
\]

One copy of the zero at \(z\) moves to \(Rz\). On the Fourier axis,

\[
 |B_z(it)|=1.
\tag{0.5}
\]

The finite calculus is completely abelian:

\[
 R^2=1,
 \qquad
 B_{Rz}=B_z^{-1},
 \qquad
 B_zB_w=B_wB_z.
\tag{0.6}
\]

Choose one representative \(z_O\) from every two-point reflection orbit
\(O=\{z,Rz\}\) off the imaginary axis. Every normalized finite all-pass
multiplier has a unique reduced form

\[
 A(s)=\prod_O B_{z_O}(s)^{n_O},
 \qquad n_O\in\mathbf Z,
\tag{0.7}
\]

with only finitely many nonzero \(n_O\). If \(m_z\) and \(m_{Rz}\) are the
zero multiplicities of \(F\), the exact entireness capacity is

\[
 \boxed{-m_{Rz}\le n_O\le m_z.}
\tag{0.8}
\]

The output multiplicities are

\[
 m'_z=m_z-n_O,
 \qquad
 m'_{Rz}=m_{Rz}+n_O.
\tag{0.9}
\]

Composition adds the integer flows \(n_O\); inverse surgery negates them;
flows on different orbits commute. This classifies exactly which **finite**
zero multisets can be reoriented while preserving the Fourier magnitude.

For real output, real zeros may move singly, while every nonreal flow must
be duplicated on the conjugate orbit. Zero mean is always preserved. A
nonzero mean is not. Including the optional constant phase from the
rational converse, the exact law is

\[
\boxed{
F_{\rm new}(0)
=\eta F(0)
\prod_O
\left(-{\overline {z_O}\over z_O}\right)^{n_O}.}
\tag{0.10}
\]

Here \(\eta=1\) for the normalized ODE surgery. Conjugate-pair flows
contribute \(1\) to this product, but every odd real-orbit flow contributes
\(-1\).

The surgery preserves Fourier magnitude, autocorrelation, and every finite
translate Gram energy. It does **not** preserve kernel shape, a nonzero mean,
oriented Jordan masses, or the \(L^1\) norm. Section 6 gives an explicit
two-interval counterexample.

## 1. The one-zero primitive

Assume \(F(z)=0\) and \(\Re z\ne0\). Define

\[
 h_z(x)=e^{zx}\int_0^xe^{-zu}K(u)\,du,
 \qquad 0\le x\le L.
\tag{1.1}
\]

Then

\[
 h_z'-zh_z=K.
\tag{1.2}
\]

Both endpoint values vanish:

\[
 h_z(0)=0,
 \qquad
 h_z(L)=e^{zL}F(z)=0.
\tag{1.3}
\]

Thus extension by zero creates no boundary delta. If \(H_z\) is the Laplace
transform of \(h_z\), integration by parts gives

\[
 (s-z)H_z(s)=F(s).
\tag{1.4}
\]

Set

\[
 T_zK=K+(z+\overline z)h_z.
\tag{1.5}
\]

Equations (1.4)--(1.5) give

\[
 \widehat {T_zK}(s)
 =F(s)\left(1+{z+\overline z\over s-z}\right)
 =F(s)B_z(s).
\tag{1.6}
\]

The input zero cancels the displayed pole. If its multiplicity is \(m\), the
output multiplicities at \(z,Rz\) are \(m-1\) and \(m_{Rz}+1\).

The construction is regularity-preserving. Since \(K\) is compact BV, it is
bounded and integrable. The function \(h_z\) is compact absolutely
continuous, and \(h_z'=zh_z+K\) is BV. Hence \(T_zK\) is compact BV and is
supported in the same declared interval. This means support **containment**;
no claim that every point of the essential support remains nonzero is needed.

## 2. Exact composition, commutation, and divisor flow

The reflection in (0.2) is an involution. Direct substitution gives

\[
 B_{Rz}(s)
 ={s-z\over s+\overline z}
 =B_z(s)^{-1}.
\tag{2.1}
\]

All factors are scalar rational functions, so they commute. Therefore,
whenever both ordered compositions are admissible,

\[
 T_zT_wK=T_wT_zK,
\tag{2.2}
\]

and

\[
 T_{Rz}T_zK=K.
\tag{2.3}
\]

Repeated use of \(T_z\) moves repeated zero copies up to their multiplicity.
If both \(z\) and \(Rz\) are listed, their factors cancel in pairs. The
reduced datum is therefore not an unordered list with redundant opposite
entries; it is the integer flow \(n_O\) on each reflection orbit.

For one chosen orientation \(z\to Rz\), multiplication by \(B_z^{n}\)
changes the two orders by

\[
 (m_z,m_{Rz})\longmapsto(m_z-n,m_{Rz}+n).
\tag{2.4}
\]

Both entries are nonnegative exactly under (0.8). This proves necessity and
sufficiency of the capacity interval. A negative \(n\) is the inverse flow.

If \(n_1,n_2\) are sequential admissible flows on the same orbit, their
composition is \(n_1+n_2\). On disjoint orbits, the updates affect disjoint
multiplicity pairs and commute exactly. Thus normalized finite all-pass
factors form the direct sum

\[
 \bigoplus_O\mathbf Z
\tag{2.5}
\]

before the capacity constraints of one fixed input divisor are imposed.
The admissible factors of a fixed \(F\) form a finite box of integer flows
when only finitely many orbits are under consideration.

This algebra also explains why order does not hide a support problem. In a
reduced multiplier, no pole \(z\) occurs together with its reflection \(Rz\):
such a pair would cancel. Every remaining pole is supplied by an input zero,
and flipping other reduced poles neither removes it nor creates a pole there.
Hence the elementary compact-BV surgeries may be performed in any order.

## 3. Rational all-pass converse

The preceding factors are not merely examples. They classify every finite
rational phase change with the declared normalization.

### Theorem 3.1

Let \(A\) be rational, with no pole on \(i\mathbf R\), and assume

\[
 |A(it)|=1
 \quad(t\in\mathbf R),
 \qquad
 A(\infty)=1.
\tag{3.1}
\]

Then \(A\) has a unique reduced factorization of the form (0.7). Without the
normalization at infinity, one additional constant \(\eta\),
\(|\eta|=1\), is present.

**Proof.** Define the para-conjugate rational function

\[
 A^\sharp(s)=\overline{A(-\overline s)}.
\tag{3.2}
\]

On \(i\mathbf R\), equation (3.1) gives \(AA^\sharp=1\). Since two rational
functions agreeing away from finitely many points on a line agree
identically,

\[
 A(s)A^\sharp(s)=1.
\tag{3.3}
\]

A pole at \(z\) of order \(r\) therefore forces a zero at \(Rz\) of the same
order. Factoring \(B_z^r\) removes that pole-zero pair. Repeating over the
finite pole divisor leaves a constant of unit modulus, and (3.1) makes that
constant \(1\). Canceling opposite factors gives uniqueness of the reduced
integer flows. \(\square\)

Now let \(G=FA\). For \(G\) to be entire, every pole multiplicity in the
reduced \(A\) must be supplied by the zero divisor of \(F\). This is exactly
(0.8). Consequently:

\[
 \boxed{
 \begin{gathered}
 \text{rational spectral factors of the same Fourier magnitude}\\
 \text{are exactly finite reflection-orbit reallocations, up to phase.}
 \end{gathered}}
\tag{3.4}
\]

For real kernels, the constant phase is restricted to \(\eta=\pm1\). The
normalized ODE surgery corresponds to \(\eta=1\).

## 4. Real structure and the exact mean law

If \(K\) is real, then

\[
 F(\overline s)=\overline{F(s)}.
\tag{4.1}
\]

Its zero divisor is conjugation-stable. The two involutions

\[
 C(z)=\overline z,
 \qquad
 R(z)=-\overline z
\tag{4.2}
\]

commute. A real finite surgery must have the same flow on the conjugate
reflection orbits. Thus:

- a real zero may be flipped singly;
- a nonreal zero \(z\) must be accompanied by \(\overline z\);
- their targets are \(Rz=-\overline z\) and \(R\overline z=-z\).

For \(z=a+ib\), the conjugate-pair multiplier is

\[
 B_z(s)B_{\overline z}(s)
 ={s^2+2as+|z|^2\over s^2-2as+|z|^2},
\tag{4.3}
\]

which has real coefficients and unit modulus on the imaginary axis.

At \(s=0\), an elementary factor is

\[
 B_z(0)=-{\overline z\over z}.
\tag{4.4}
\]

This proves (0.10). It has three exact consequences.

1. Since every factor is finite at zero, \(F(0)=0\) implies
   \(F_{\rm new}(0)=0\).
2. The magnitude \(|F(0)|\) is always preserved.
3. For a real-preserving surgery, a nonreal conjugate pair contributes

   \[
   \left(-{\overline z\over z}\right)
   \left(-{z\over\overline z}\right)=1,
   \tag{4.5}
   \]

   while every real-zero factor contributes \(-1\).

Hence, for normalized real surgery, a nonzero real mean is multiplied by

\[
 (-1)^{\sum_{O\ {\rm real}}n_O}.
\tag{4.6}
\]

It is preserved when the total real-orbit flow is even and negated when it
is odd. This is the finite-flow refinement of the corrected predecessor
law.

## 5. Fourier, autocorrelation, and Gram invariance

For \(z=a+ib\),

\[
 |it+\overline z|^2
 =a^2+(t-b)^2
 =|it-z|^2.
\tag{5.1}
\]

Thus every finite multiplier in (0.7) has unit modulus on \(i\mathbf R\),
including inverse flows. Therefore

\[
 |F_{\rm new}(it)|=|F(it)|.
\tag{5.2}
\]

For compact BV kernels define

\[
 R_K(u)=\int_{\mathbf R}K(v)\overline{K(v+u)}\,dv.
\tag{5.3}
\]

With the \(e^{+itu}\) convention for transforming \(R_K(u)\), its Fourier
transform is \(|F(it)|^2\), so Fourier uniqueness gives

\[
 R_{K_{\rm new}}=R_K.
\tag{5.4}
\]

For arbitrary finite complex coefficients \(c_j\) and real shifts \(x_j\),

\[
 \int_{\mathbf R}
 \left|\sum_jc_jK(t-x_j)\right|^2dt
 =\sum_{j,k}c_j\overline{c_k}R_K(x_j-x_k).
\tag{5.5}
\]

Thus the entire finite translate Gram form is invariant. The beta prefix
energy is one special real coefficient vector; no arithmetic estimate is
created by replacing one spectral factor with another.

The imaginary-axis zero divisor is also invariant. If \(F(it_0)=0\), then
every energy-identical factor has zero Fourier magnitude at \(t_0\). The
elementary reflection fixes an imaginary-axis point and becomes trivial:

\[
 R(it_0)=it_0,
 \qquad
 B_{it_0}(s)=1.
\tag{5.6}
\]

Therefore Fourier-axis notches cannot be removed by magnitude-preserving
spectral-factor surgery.

## 6. Exact Jordan and \(L^1\) obstruction

Energy invariance does not transfer an oriented one-sided theorem. Consider
the real compact BV kernel

\[
 K(x)=
 \begin{cases}
  1,&0\le x<1,\\
  -4/3,&1\le x\le2,\\
  0,&\text{otherwise}.
 \end{cases}
\tag{6.1}
\]

Its transform is

\[
 F(s)={1-e^{-s}\over s}
 \left(1-{4\over3}e^{-s}\right).
\tag{6.2}
\]

Put

\[
 a=\log(4/3).
\tag{6.3}
\]

Then \(e^{-a}=3/4\), so \(F(a)=0\). The original mean and Jordan masses are

\[
 \int K=-{1\over3},
 \qquad
 \int K_+=1,
 \qquad
 \int K_-={4\over3}.
\tag{6.4}
\]

The real-zero flip can be evaluated explicitly from (1.1)--(1.5):

\[
 T_aK(x)=
 \begin{cases}
  2e^{ax}-1,&0\le x<1,\\
  {4\over3}-{3\over2}e^{ax},&1\le x\le2,\\
  0,&\text{otherwise}.
 \end{cases}
\tag{6.5}
\]

The first piece is positive and the second is negative. Direct integration
gives

\[
 \int (T_aK)_+
 ={2\over3a}-1,
 \qquad
 \int (T_aK)_-
 ={2\over3a}-{4\over3}.
\tag{6.6}
\]

Their difference is \(+1/3\), agreeing with the mean sign law (4.4).

The alternating series for \(\log(1+1/3)\) gives

\[
 {31\over108}
 ={1\over3}-{1\over18}+{1\over81}-{1\over324}
 <a<{1\over3},
\tag{6.7}
\]

and \(31/108>2/7\). Hence

\[
 1<{2\over3a}-1<{4\over3},
 \qquad
 {2\over3}<{2\over3a}-{4\over3}<1.
\tag{6.8}
\]

Both Jordan masses change, and

\[
 \|T_aK\|_1
 ={4\over3a}-{7\over3}
 <{7\over3}
 =\|K\|_1.
\tag{6.9}
\]

Nevertheless, (5.2)--(5.5) apply exactly. This proves

\[
 \boxed{
 \text{Fourier magnitude, autocorrelation, and Gram energy do not determine
 mean sign, Jordan masses, or }L^1.}
\tag{6.10}
\]

No reflection or all-pass argument may silently transfer a direct
one-sided Landau hypothesis.

## 7. Finite minimum-phase design and its exact limit

For this Laplace convention, call a declared finite divisor
**left-oriented** if all its off-axis members have negative real part. This
avoids importing a stronger engineering definition of minimum phase.

Given any finite conjugation-stable multiset of right-half-plane zeros of a
real compact BV transform, apply the positive flow from each \(z\) to
\(Rz\), through its multiplicity. Sections 1--5 produce a real compact BV
kernel with:

- the same support containment;
- the same Fourier magnitude, autocorrelation, and finite Gram form;
- the chosen finite zeros moved to the left half-plane;
- zero mean preserved if present;
- a controlled sign law for a nonzero mean.

More generally, (0.8) allows any finite reallocation between the two sides,
not only right-to-left design.

If the entire wrong-half-plane divisor is finite, this gives a global
left-oriented carrier. If it is infinite, finite surgery supplies only a
height- or list-bounded repair. It does not produce one all-height kernel.
Likewise, imaginary-axis zeros remain fixed.

Even when every zero is left-oriented, this packet does not assert a causal
stable inverse, an outer-function theorem, or any other convention-dependent
minimum-phase property. Its exact theorem concerns the carrier divisor and
finite rational spectral factors only.

## 8. Infinite-product and compactness firewall

An infinite reorientation would formally use

\[
 \prod_jB_{z_j}(s).
\tag{8.1}
\]

The finite theorem proves none of the following load-bearing facts for
(8.1):

1. convergence to a meromorphic or entire-compatible function;
2. a canonical-product or half-plane Blaschke condition;
3. unit boundary modulus after taking limits;
4. preservation of exponential type and the Paley--Wiener support indicator;
5. existence of an inverse transform in BV rather than only as a
   distribution;
6. convergence of the sequential kernels in \(L^1\), \(L^2\), or BV norm;
7. preservation of a source-specific endpoint or shape contract.

The global reflection in the chirality predecessor is a special exact
symmetry which safely moves one explicit infinite lattice. It is not evidence
that an arbitrary product (8.1) converges.

There is also a structural compact-support warning. A rational all-pass
factor changes neither Fourier magnitude nor exponential type, and the ODE
gives a direct compact kernel. A general inner function need not be rational;
boundary unitarity alone does not imply compact support or BV regularity.

## 9. Programme boundary

The result supplies a design language, not an estimate:

~~~text
finite rational spectral factor
    -> exact reflection-orbit divisor flow
    -> exact energy-identical compact BV kernel;

beta prefix energy bound
    -> unchanged and still open;

oriented complete field / L1 / Jordan negative mass
    -> changed in general;

arbitrary infinite carrier repair
    -> requires new convergence and compactness theorems.
~~~

In particular:

- no zeta-zero list is used;
- no beta-energy or off-diagonal estimate is proved;
- no one-sided Landau hypothesis is transported through energy equality;
- no RH or GRH conclusion is obtained;
- no external novelty claim is made without a dedicated literature review of
  spectral factorization and phase retrieval.

## 10. Proof ledger

| statement | grade |
|---|---|
| one-zero ODE construction | **IMPORTED AND REDERIVED EXACT** |
| reflection, inverse, composition, and commutation laws | **PROVED EXACT** |
| reflection-orbit capacity (0.8)--(0.9) | **PROVED EXACT** |
| finite rational all-pass converse | **PROVED EXACT** |
| finite zero-multiset reorientation | **PROVED EXACT** |
| real-output conjugation gate | **PROVED EXACT** |
| exact mean phase/parity law | **PROVED EXACT / CORRECTS PREDECESSOR WORDING** |
| compact support containment and BV preservation | **PROVED EXACT FOR FINITE SURGERY** |
| Fourier/autocorrelation/finite Gram invariance | **PROVED EXACT** |
| imaginary-axis zero immobility | **PROVED EXACT** |
| Jordan and \(L^1\) invariance | **REFUTED BY (6.1)--(6.9)** |
| global left orientation for a finite wrong-side divisor | **PROVED EXACT** |
| global minimum phase for an infinite divisor | **NOT PROVED** |
| arbitrary infinite all-pass product | **NOT PROVED** |
| beta-energy estimate | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

## 11. Bounded replay

The producer pins both predecessor quartets. It checks three exact
reflection orbits, sequential/direct composition, disjoint-orbit
commutation, inverse flow, conjugate-pair real coefficients, mean parity,
the exact two-interval carrier root, the rational logarithm bounds, and six
bounded Fourier-axis controls. Floating-point rows are regression checks for
the exact formulas above.

It uses no root finder, quadrature, zeta zero, numerical zeta value, prime,
curve, random sample, or contour integral.

~~~text
python -B research/l-families/atlas/function_field/ffps_compact_kernel_finite_spectral_factor_surgery.py --check
python -B -O research/l-families/atlas/function_field/ffps_compact_kernel_finite_spectral_factor_surgery.py --check
python -B -m unittest tests.test_ffps_compact_kernel_finite_spectral_factor_surgery
python -B -O -m unittest tests.test_ffps_compact_kernel_finite_spectral_factor_surgery
python -B -m ruff check research/l-families/atlas/function_field/ffps_compact_kernel_finite_spectral_factor_surgery.py tests/test_ffps_compact_kernel_finite_spectral_factor_surgery.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_compact_kernel_finite_spectral_factor_surgery.py tests/test_ffps_compact_kernel_finite_spectral_factor_surgery.py
~~~
