# A reciprocal-Gamma limit for the native regularized period determinant

Status: PROPOSED ANALYTIC THEOREM; independent exact-source review required.
Scope: level-one cusp spaces, weight tending to infinity, bounded complex
endpoint coordinate. The normalization preserves finite-weight determinant
zeros, but does not assert scalar-quotient noncancellation or an RH mechanism.

## 1. Statement and why the normalization is necessary

Use the native operator \(\mathcal T_k\) of (K1) in
[the cusp spectral theorem](CUSP_KRONECKER_SPECTRAL_LAW.md). Let
\(d_k=\dim V_k\). Its ordered eigenvalues satisfy the following consequences
of Theorem K:

\[
 \operatorname{tr}\mathcal T_k\sim\frac{k\log k}{24},
 \qquad
 k^{-p}\operatorname{tr}|\mathcal T_k|^p
 \longrightarrow\frac{\zeta(p)}{24^p}\quad(p>1). \tag{G1}
\]

In particular the natural scaled limit is Hilbert--Schmidt but not trace
class. Ordinary determinants require a diverging linear counterterm.
For a finite matrix define

\[
 \det{}_2(I-B)=\det(I-B)\exp(\operatorname{tr}B).
\]

**Theorem G.** Locally uniformly for \(z\in\mathbb C\),

\[
 \det{}_2(I-z\mathcal T_k/k)
 \longrightarrow \frac{\exp(\gamma z/24)}{\Gamma(1-z/24)}. \tag{G2}
\]

There is also an EXACT-PERIOD version. Let \(\mathcal P_k(s)\) be the
Petersson form operator of \(I_s\), and set

\[
 B_k(c)=I+\frac{2c}{k}\mathcal P_k(1-c/k),\qquad
 \mathfrak D_k(c)=\det{}_2(I-B_k(c)). \tag{G3}
\]

The singularity at \(c=0\) is removable, with \(B_k(0)=0\) and
\(\mathfrak D_k(0)=1\). On every fixed compact subset of the \(c\)-plane,
these functions are holomorphic for all sufficiently large weights, and

\[
 \boxed{\mathfrak D_k(c)\longrightarrow
       \frac{\exp(\gamma c/12)}{\Gamma(1-c/12)}} \tag{G4}
\]

locally uniformly. Thus the whole fixed-endpoint ladder is encoded by one
limiting entire function, rather than separate finite depth fits.

In any fixed disk around \(c=12j\) containing no other positive multiple of
12, (G4) implies exactly one full-period determinant zero for large weights.
It is simple and real by multiplicity counting and conjugation symmetry.
This recovers the full-determinant part of the accepted fixed-depth ladder;
the NEW content here is the regularized entire-function/operator limit.
The stronger growing-coordinate inertia theorem in the separate P packet
is not obtained by extrapolating (G4) to moving compact sets.

## 2. Spectral summability and the trace

The scalar symbol (K2) is bounded below on \(y\ge a_0\):
\(\pi y/6-(\log y)/2\) has a finite global minimum. Together with (K4),
there is an absolute constant \(B\) such that, for all legal indices,

\[
 -B\le\lambda_j(k)\le\frac{k}{24j}+B,
 \qquad
 \frac{|\lambda_j(k)|}{k}\le\frac1{24j}+\frac Bk. \tag{G5}
\]

Extend \(\lambda_j(k)/k\) by zeros beyond \(d_k\). At every fixed index
it tends to \(1/(24j)\), by (K6). For every \(p>1\), (G5) gives

\[
 \sum_{j>M}\left|\frac{\lambda_j(k)}k\right|^p
 \le 2^{p-1}24^{-p}\sum_{j>M}j^{-p}
       +2^{p-1}B^p d_k/k^p.
 \tag{G6}
\]

Since \(d_k=O(k)\), fixed-coordinate convergence and this tail bound prove
convergence in \(\ell^p\) to \((1/(24j))_{j\ge1}\). This proves the
second assertion of (G1), without assuming positivity of every eigenvalue.

The trace upper bound follows by summing (K4). For the lower bound choose
\(J_k=\lfloor k/(\log k)^2\rfloor\). The explicit bounds (K3),(K13),(K14)
are uniform for \(1\le j\le J_k\), so their relative error tends to zero
uniformly there. Alternatively summing (K5) directly subtracts at most
\(O(J_k\log k)\) from the leading harmonic sum. The remaining
\(d_k-J_k\) eigenvalues are at least \(-B\). Therefore

\[
 \operatorname{tr}\mathcal T_k
 \ge(1-o(1))\frac{k}{24}\sum_{j\le J_k}\frac1j-O(k)
 \sim\frac{k\log k}{24}.
\]

This proves the first assertion of (G1).

## 3. The operator determinant limit

The \(\ell^2\) convergence just proved controls canonical products of genus
one. For completeness, on a small disk the logarithm is

\[
 \log\det{}_2(I-z\mathcal T_k/k)
 =-\sum_{p\ge2}\frac{z^p}{p}\sum_j(\lambda_j(k)/k)^p.
 \tag{G7}
\]

The series converges normally there by a uniform operator norm bound and
the uniform squared-eigenvalue sum. Its limit is
\(-\sum_{p\ge2}\zeta(p)(z/24)^p/p\).
For any complex number \(w\),

\[
 |(1-w)e^w|\le\exp(|w|^2/2),
\]

because \(\log|1-w|\le[-2\Re w+|w|^2]/2\). Hence the determinants are
locally uniformly bounded on the entire plane. The elementary normal-family
and uniqueness theorem extends the small-disk convergence everywhere.
The Weierstrass product for Gamma identifies the limit as (G2):

\[
 \prod_{j\ge1}(1-z/(24j))e^{z/(24j)}
 =\frac{e^{\gamma z/24}}{\Gamma(1-z/24)}.
\]

The imported Gamma product is [NIST DLMF 5.8.2](https://dlmf.nist.gov/5.8.E2).
In particular the sign of the Euler-constant exponential is PLUS.

## 4. A uniform fixed-coordinate period remainder

The key estimate is, for every fixed \(R>0\),

\[
 \sup_{|c|\le R}
 \left\|B_k(c)-\frac{2c}{k}\mathcal T_k\right\|_{\mathrm{op}}
       =O_R(\log k/k),
 \tag{G8}
\]

and therefore the corresponding Hilbert--Schmidt norm is
\(O_R(\log k/\sqrt k)\). All norms are in the ORIGINAL Petersson metric.

Here are full-domain estimates proving (G8). In the normalized measure of
any nonzero cusp form, for each fixed integer \(r\ge1\),

\[
 \mathbb E_f[y^r]\le C_r k^r. \tag{G9}
\]

Above height one this follows coefficientwise from

\[
 M_r(a)=\frac{\int_1^\infty y^{\nu-1+r}e^{-ay}dy}
                   {\int_1^\infty y^{\nu-1}e^{-ay}dy},
 \quad
 M_r(a)\le1+\frac{\nu+r-1}{a}M_{r-1}(a),\quad a\ge4\pi.
\]

The compact-domain contribution is at most its norm. Thus (G9) holds for
the WHOLE space, independently of dimension or coefficient size. Also,
for \(y\ge1\), \(\log y\le\log k+y/k\), so

\[
 \mathbb E_f[y^r\log y]=O_r(k^r\log k),\qquad r=1,2. \tag{G10}
\]

For \(\varepsilon=c/k\), \(|c|\le R\), expansion of the two scalar
constant-term coefficients and of \(e^{\pm\varepsilon\log y}\) gives

\[
 \left|E^*(z,1-\varepsilon)+\frac1{2\varepsilon}-E_0(z)\right|
 \le C|\varepsilon|\left[1+y^{1+|\varepsilon|}(1+\log y)
                          +y^{|\varepsilon|}(1+\log^2y)\right]
 \tag{G11}
\]

on \(y\ge1\); below one it is \(O(|\varepsilon|)\). At zero the left side
is interpreted by analytic continuation. In deriving the polar term,
the linear exponential term is subtracted BEFORE dividing by
\(\varepsilon\):
\(|e^{\varepsilon l}-1-\varepsilon l|
 \le |\varepsilon|^2l^2e^{|\varepsilon|l}/2\).

The nonconstant Fourier remainder is uniformly analytic near \(s=1\).
To check this also for \(\Re s>1\), take a fixed small disk there.
The Bessel integral bounds \(|K_{s-1/2}(t)|\le K_1(t)\) and

\[
 K_1(t)\le\sqrt{\pi/(2t)}\,e^{-t}e^{1/(2t)},\qquad t\ge2\pi a_0,
\]

follow by \(\cosh u\ge1+u^2/2\) in its defining integral. The divisor and
power factors are then bounded by a fixed polynomial in \(n\), while
\(e^{-2\pi ny}\) is summable uniformly for \(y\ge a_0\). Cauchy's estimate
therefore bounds its difference from the value at one by \(O(|\varepsilon|)\).
No inequality is analytically continued from the left half of the disk.

Finally concavity gives \(y^{|\varepsilon|}\le1+|\varepsilon|y\) on
\(y\ge1\), for large \(k\). Equations (G9)--(G10), with moments up to
three, and \(\log^2y\le y\), show the expectation of the right side of
(G11) is \(O_R(|\varepsilon|k\log k)\).
Weighted Cauchy--Schwarz gives the same operator norm bound for the
compressed form, even when \(c\) is complex. Multiplication by \(2c/k\)
proves (G8).

## 5. Passage from the exact period to its Gamma limit

Diagonalize the fixed self-adjoint operator \(\mathcal T_k\), independently
of \(c\), and extend its matrix by zeros to \(\ell^2\). Its scaled matrix
converges in Hilbert--Schmidt norm to
\(D=\operatorname{diag}(1/(24j))\). Equation (G8) shows in the same coordinates

\[
 B_k(c)\longrightarrow2cD
\]

in Hilbert--Schmidt norm, uniformly on compact \(c\)-sets. This coordinate
choice is only for the proof; the finite determinant and trace in (G3)
are basis independent.

On a small disk, use the logarithmic determinant series from (G7) with
\(B_k\) in place of \(z\mathcal T_k/k\). For powers \(p\ge2\), the trace
differences tend to zero by a telescoping expansion and
\(|\operatorname{tr}(UV)|\le\|U\|_2\|V\|_2\), with the remaining factors
bounded in operator norm. The series is uniformly summable there.
For larger compact sets, Schur triangularization gives
\(\sum|\lambda_j(B_k)|^2\le\|B_k\|_2^2\), so the scalar inequality in
Section 3 bounds the regularized determinants by
\(\exp(\|B_k\|_2^2/2)\). Normal-family uniqueness again gives locally
uniform convergence and proves (G4).

The only other Eisenstein pole corresponds to \(c=k\), which eventually
lies outside any fixed compact set. Thus no pole is hidden in this argument.
The exponential counterterm never vanishes. Away from \(c=0\), zeros of
\(\mathfrak D_k\) are therefore exactly zeros of the native period determinant,
with their multiplicities unchanged.

## 6. Boundaries and next question

The regularization is an explicitly declared trace counterterm; it does not
claim positivity or a new arithmetic source morphism. It preserves zeros
because its additional factor is nonvanishing. The scalar Gamma limit is
not the finite-weight period function and does not turn that function into
an automorphic L-function. Its appearance is explained by the harmonic
cusp spectrum and the required genus-one product.

For moving \(c\), compact convergence is insufficient. The direct P theorem
already addresses growing inertia. A sharper target is a uniformly accurate
Poincare diagonal model resolving individual roots for growing index, with
all compact-domain and nonconstant Fourier couplings paid separately.
