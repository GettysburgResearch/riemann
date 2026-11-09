# Native source capture: the information lost by norm-twist averaging

9 November 2026. Standalone research note. No improved zero-free boundary is claimed.

## Result

The short Gauss frame in PR #1019 is a controlled observation of the native
Möbius vector. It does not capture the whole vector. This note gives three
precise results about attempts to obtain that missing capture:

1. **A source-blindness theorem.** For good squarefree Eisenstein ideals,
   Möbius is determined by the integer norm. Consequently infinite norm-twist
   covariance, after any fixed linear row operator, is exactly unchanged if
   Möbius is replaced by the constant coefficient 1. More strongly, the signed
   and unsigned finite norm-twist families have identical orbit closures.
2. **An exact finite-window formula.** Every distinction between the two
   covariances is carried by interference between *different* norms having
   opposite Möbius signs. A quantitative bound shows when long averaging
   necessarily erases that information.
3. **Native finite certificates.** Actual Eisenstein sextic character matrices
   have norm-packet ranks 31, 115 and 413 at the displayed three scales, proved
   by exact nonzero minors modulo 1009. These certify many invisible directions
   in the unrestricted finite smooth-profile family. The accompanying native
   Möbius/Gauss-frame projection calculations retain all common-prime zeros.

This rules out a specific proposed shortcut: an inverse theorem based only on
the fully dephased norm-twist covariance cannot exploit Möbius signs. It does
not rule out cancellation at the actual untwisted source. That cancellation
must survive as cross-norm information or enter through additional arithmetic.

## 1. Exact objects and inherited claims

Work in \(E=\mathbb Q(\sqrt{-3})\), \(\mathcal O=\mathbb Z[\omega]\),
\(\omega^2+\omega+1=0\). Every good ideal, meaning prime to 6, is represented
by its generator congruent to 1 modulo 3. Put
\(\chi_n(z)=(z/n)_6\), with its literal value zero at a shared prime.

The native operator and frame, from paper 10 v2 §7 and PR #1013, are

\[
A_{z,n}=\sqrt{w(Nz/U)}\chi_n(z),\qquad
v_R(z)=U^{-1/2}\sqrt{w(Nz/U)}\gamma_1(z)\overline{\chi_z(R)}.
\tag{1}
\]

Rows are all good squarefree ideals in the support of \(w\). Columns below
are all good squarefree ideals in the support of \(W\); restricting to these
columns changes nothing for a Möbius coefficient. We use

\[
b_n=\frac{\mu_E(n)\nu_0(n)}{\sqrt{Nn}}W(Nn/D)1_{(n,Q)=1},
\qquad y(t)=A\bigl(\overline b_n(Nn)^{it}\bigr)_n.
\tag{2}
\]

The finite experiment has \(Q=1\), \(\nu_0=1\), and real \(W\), so the
conjugate in (2) is immaterial. The general statements below allow fixed ray
data and fixed punctures. All row operators, frames, and projections are fixed
as \(t\) varies. In particular they are not reselected from \(y(t)\).

For squarefree labels \(NR\le K\), let \(V=(v_R)\) and let \(P\) be the
orthogonal projection onto their span. If \(G=V^*V\) is invertible,
\(P=VG^{-1}V^*\). PR #1019 records a source-dependent upper bound for
\(\|Py(0)\|^2\), with \(K\le D^{1/7}\) and a separate Gram half-range.
That upper bound is an imported claim here; it is not used to prove any result
in this note. An upper bound for \(\|Py\|^2\) cannot be subtracted from an
upper bound for \(\|y\|^2\) to estimate \(\|(I-P)y\|^2\).

Commit-pinned links and Git blob identities are in `SOURCES.json`.

## 2. Möbius has one sign per norm

**Lemma 1.** If \(n\) is a good squarefree ideal, \(\mu_E(n)\) depends only
on its integer norm \(m=Nn\).

**Proof.** A rational prime \(p\equiv1\pmod3\) splits into two prime ideals
of norm \(p\). Squarefreeness permits zero, one or both, so its exponent
\(e_p\) in \(m\) is 0, 1 or 2 and its Möbius contribution is
\((-1)^{e_p}\). A rational prime \(p\equiv2\pmod3\) is inert, with one
prime ideal of norm \(p^2\). Its exponent in \(m\) is \(2f_p\), where
\(f_p=0\) or 1, and its contribution is \((-1)^{f_p}\). Primes over 6
are absent. Thus

\[
\sigma(m):=\mu_E(n)
=(-1)^{\sum_{p\equiv1(3)}e_p+\sum_{p\equiv2(3)}f_p}.
\tag{3}
\]

The right side uses only \(m\). In particular, conjugate ideals with the
same norm must not be treated as independent norm frequencies. ∎

Let \(a_m\) be the unsigned coherent norm packet

\[
a_m=\sum_{Nn=m} A_{\cdot,n}
\frac{\overline{\nu_0(n)W(m/D)}}{\sqrt m}1_{(n,Q)=1},
\quad B=(a_m)_m.
\tag{4}
\]

Only finitely many distinct integer norms occur. Then
\(y_\mu(t)=\sum_m\sigma(m)a_m m^{it}\), whereas the source with
Möbius replaced by 1 is \(y_+(t)=\sum_m a_m m^{it}\).

**Theorem 2 (covariance invariance).** For every fixed linear row operator
\(L\), the two limits

\[
\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}
 Ly_\mu(t)y_\mu(t)^*L^*\,dt
=\lim_{T\to\infty}\frac1{2T}\int_{-T}^{T}
 Ly_+(t)y_+(t)^*L^*\,dt
=LBB^*L^*.
\tag{5}
\]

**Proof.** Expand the finite double sum. The average of
\(e^{it\log(m/k)}\) is 1 for \(m=k\) and tends to zero otherwise.
On the surviving diagonal \(\sigma(m)^2=1\). Equal-norm ideals have already
been summed coherently in (4). Finite sums justify taking limits termwise. ∎

Taking \(L=P\), \(I-P\), a stacked channel operator, or any fixed
combination of them does not restore the lost signs.

**Theorem 3 (identical orbit closures).** The closures of
\(\{y_\mu(t):t\in\mathbb R\}\) and
\(\{y_+(t):t\in\mathbb R\}\) in the finite row space are equal.
Their continuous long-time averaged statistics are also equal.

**Proof.** List the finitely many rational primes occurring in the source.
Their logarithms have no nonzero integer relation, by unique factorization.
The continuous one-parameter flow
\((e^{it\log p})_p\) is therefore dense and equidistributed in the full
prime torus (continuous-time Kronecker approximation). Multiplying the torus
coordinate at each split prime by \(-1\), and at each inert prime by \(i\),
multiplies every norm monomial by exactly (3): inert norm exponents are even.
Translation preserves the prime torus and its Haar measure. The vector sum
is a continuous function of that torus, proving the assertions. ∎

The code uses \((Nn/D)^{it}\), which differs from (2) by the common unit
scalar \(D^{-it}\). All computed norms, projections and covariances are
therefore identical. The literal vector-orbit equality is asserted in the
\((Nn)^{it}\) convention; energy-orbit equality holds in either convention.

In particular the supremum over *all* norm twists of projected or complementary
energy is unchanged by removing Möbius. This says nothing about how large a
twist is required. It does not contradict an estimate whose constant grows
with the smooth-profile seminorms or with \(t\).

## 3. The cross-norm information that a successful estimate must retain

For \(T>0\), set \(S_T(m,k)=\operatorname{sinc}(T\log(m/k))\), with
\(\operatorname{sinc}(x)=\sin(x)/x\) and value 1 at zero. Let
\(\Sigma=\operatorname{diag}(\sigma(m))\). Exact integration gives

\[
C_T^\mu=B\Sigma S_T\Sigma B^*,\qquad C_T^+=BS_TB^*,
\tag{6}
\]

and hence

\[
C_T^\mu-C_T^+
=-2\!\sum_{\sigma(m)\ne\sigma(k)}
a_ma_k^*\operatorname{sinc}(T\log(m/k)).
\tag{7}
\]

This is an identity, not a cancellation estimate. It identifies precisely
the terms discarded by infinite averaging: cross-norm correlations with
opposite Möbius signs.

**Proposition 4 (quantitative dephasing).** If all norms are integers in
\((D,2D)\), \(D\ge1\), then

\[
\|C_T^\mu-C_T^+\|\le
\frac{8D\,[1+\log\lceil D\rceil]}{T}\,\|BB^*\|.
\tag{8}
\]

**Proof.** For \(m,k\in(D,2D)\), the mean value theorem gives
\(|\log(m/k)|\ge|m-k|/(2D)\). Each row of \(S_T-I\) has absolute sum
at most \((4D/T)\sum_{j\le\lceil D\rceil}j^{-1}\). The Hermitian
row-sum bound controls its operator norm. Both \(B(S_T-I)B^*\) and
\(B\Sigma(S_T-I)\Sigma B^*\) are bounded by that norm times
\(\|B\|^2=\|BB^*\|\). The triangle inequality and the harmonic-sum
bound prove (8). ∎

Thus averaging on scales much larger than \(D\log D\) is provably
insensitive to these signs in relative operator norm. A shorter averaging
window retains them, but bounding (7) is new arithmetic work. Choosing an
observable from the already computed target vector would be circular as a
proof method; the needed estimate must arise from independently controlled
arithmetic structure.

## 4. Minimal extra observations for the dephased family

Write \(C=BB^*\) and \(C_\perp=(I-P)C(I-P)\), with decreasing eigenvalues
\(\lambda_1\ge\lambda_2\ge\cdots\ge0\).

**Proposition 5.** Among all orthogonal extensions \(P+E\) with
\(E\le I-P\) and \(\operatorname{rank}E=q\), the largest captured mean
energy is exactly

\[
\operatorname{tr}(PC)+\sum_{j=1}^{q}\lambda_j.
\tag{9}
\]

The minimum residual operator norm is \(\lambda_{q+1}\).

**Proof.** The captured mean is (5), hence
\(\operatorname{tr}(PC)+\operatorname{tr}(EC_\perp)\). In an eigenbasis
of \(C_\perp\), the diagonal entries of \(E\) lie in \([0,1]\) and sum
to \(q\), so their weighted sum is at most the sum of the largest \(q\)
eigenvalues. The corresponding spectral projection gives equality. The
operator-norm statement is the same min-max argument applied to the
remaining subspace. ∎

This is standard finite-dimensional spectral theory, applied to the *correct
arithmetic covariance*. It is an exact design criterion, not an analytic
estimate for its eigenvalues. Moreover (5) shows that this particular design
criterion is source-blind to Möbius.

The ratio \(\operatorname{tr}(PC)/\operatorname{tr}C\) below is the ratio
of the two mean energies. It is not the unweighted time average of the
pointwise capture fraction. It is an energy-weighted average of that fraction.

## 5. Native calculation and exact rank certificates

The experiment uses

\[
W(x)=w(x)=
\begin{cases}\exp\{4-[(x-1)(2-x)]^{-1}\},&1<x<2,\\0,&\text{otherwise.}\end{cases}
\tag{10}
\]

Every good squarefree ideal in each displayed annulus is included. The code
enumerates primary generators, factors them in \(\mathbb Z[\omega]\),
evaluates local sextic symbols by the finite-field Euler power, and multiplies
them with their natural zero masks. It computes prime Gauss phases using

\[
e((x+y\omega)/(a+b\omega))
=\exp\{2\pi i(ay-bx)/N(a+b\omega)\}
\]

and assembles squarefree Gauss phases by CRT. Complete direct additive sums
on all 24 squarefree composite good ideals of norm at most 300 check this
assembly, with maximum floating discrepancy below \(10^{-15}\).

For each norm \(m\), form the *unweighted exact* packet
\(T_{z,m}=\sum_{Nn=m}\chi_n(z)\in\mathbb Z[\omega]\). Multiplication
by the nonzero smooth row and norm weights, and by the norm-specific Möbius
sign, preserves its rank. Map \(\omega\) to a nontrivial cube root modulo
1009. A nonzero minor there implies the same minor is nonzero in
\(\mathbb Q(\omega)\). The selected minors attain the number of columns,
so these are exact ranks, not merely lower bounds.

| \(D\) | \(U\) | Rows | Squarefree columns | Distinct norms / exact packet rank | Nonzero minor mod 1009 |
|---:|---:|---:|---:|---:|---:|
| 256 | 128 | 37 | 74 | 31 | 860 |
| 1024 | 512 | 139 | 294 | 115 | 263 |
| 4096 | 2048 | 583 | 1145 | 413 | 512 |

`NATIVE_RESULTS.json` contains the chosen finite-field embedding, every pivot
row and column, and an independent replay of each selected minor. All integer
products used in modular elimination fit safely in signed 64-bit arithmetic.
The frame ranks are likewise certified exactly after removing their common
nonzero row weights and unimodular Gauss phases.

Projection energies, QR factorizations, singular values and covariance
eigenvalues are ordinary double-precision diagnostics, not interval-certified
theorems. For the largest example:

| \(K\) | Frame rank | Actual \(t=0\) energy captured | Ratio of mean energies captured | Best possible mean capture by any frame of this rank |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0.006615% | 0.347177% | 2.465176% |
| 7 | 3 | 0.276228% | 1.023990% | 6.885401% |
| 13 | 5 | 0.862781% | 1.676069% | 10.801832% |
| 25 | 8 | 1.294217% | 2.620075% | 16.391209% |
| 43 | 14 | 2.194073% | 4.595352% | 26.238760% |

The \(K=43\) Gram condition number is approximately 2.061, so the small
observed energy is not explained by numerical Gram ill-conditioning. An
optimal extension of that particular frame requires 31, 107 or 183 further
dimensions to capture respectively 50%, 90% or 99% of the total *mean*
energy, according to (9) and the numerical spectrum.

**Range warning.** The displayed \(K=43\) lies in the numerical half-range
\(K<\sqrt U\), but exceeds PR #1019's separate range \(K\le D^{1/7}\).
No theorem from that PR is being applied to it. At all three tested scales
\(D/U=2\); the natural label space \(NR\le2\) contains only \(R=1\),
because the smallest nonunit good ideal norm is 7. Thus the \(K=1\) row is
also the exact natural-label-space diagnostic. These small experiments do
not reach a growing natural frame, and they do not establish an asymptotic
power or estimate an unknown implied constant.

## 6. A rigorous finite noncapture conclusion, with its exact scope

**Corollary 6.** For the largest finite arithmetic example and any fixed
rank-14 row observation space, at least 399 complex dimensions of the native
unrestricted smooth-profile image are invisible to it. If the source profile
must be real, there are at least 385 real invisible dimensions.

**Proof.** The 413 norm packets are linearly independent by the exact minor
certificate. Evaluation at their finitely many distinct points \(m/D\)
can be prescribed arbitrarily by a smooth compactly supported profile:
choose disjoint small bump functions around those points. Therefore the
native profile image has complex dimension 413. A rank-14 complex observation
has kernel of codimension at most 14 on that image. For real interpolation,
its equations impose at most 28 real conditions on 413 independent real
profile parameters. This proves both bounds. ∎

This corollary concerns **unrestricted interpolation at fixed finite scales**.
The necessary derivative seminorms can grow very rapidly with the scale and
chosen coefficients. It does not contradict PR #1019's fixed smooth-profile
estimates, does not disprove capture for the particular profile (10), and does
not require the invisible profiles to be nonnegative. It refutes only a
uniform positive-capture claim for the whole unrestricted smooth-profile
class based on the short frame alone.

## 7. What remains open, and the changed research target

The actual required claim is a source-specific estimate for
\((I-P)A\overline b\), or an exact signed source-return identity that
controls this vector together with its other channels. The preceding facts
show why neither a small projected norm nor a covariance with all cross-norm
terms removed supplies it.

A useful inverse theorem would have to retain the signed kernel (7), a
bounded-window counterpart with a justified reconstruction step, or additional
local relations that force a quantitative restriction on the actual source.
It cannot obtain a Möbius advantage from the fully dephased covariance, whose
signed and unsigned versions are identical. The needed uniform analytic
estimate is not supplied here. No RH resolution, improved zero-free region,
or claim of literature-wide novelty follows.

## Reproduce

From this directory, with Python 3 and NumPy:

```bash
python native_projection.py
```

This recreates `NATIVE_RESULTS.json`. Defaults are the three cases and all
displayed label caps that satisfy \(K\le\sqrt U\). The output records the
script SHA-256, exact arithmetic data, literal-zero counts, modular minor
certificates, Gauss replay, finite norm-twist samples, and floating spectral
diagnostics. It uses no random data, repository mutation or network access.
