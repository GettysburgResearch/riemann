# Exact pole recurrence and the empty-modulus tail

Status: proposed analytic identity and tail estimate; independent review
required.

Scope: the primitive adjoint remainder paired with the actual normalized
Möbius coefficient. These are identities for Gauss-vector adjoint
pairings. They do not identify this scalar pairing with the full inverse
moment or control its complementary row space.

Provenance: signed_kernel proposed physical empty-modulus removal;
root checked the primitive-density mechanism and the refined mean
accounting. The exact residue recurrence, completion-free geometric
expansion, and paired tail bound below were derived and recorded by
joint_continuation.

## 1. Sources and notation

Let all ideals be good Eisenstein ideals, with the fixed multiplicative
primary representatives. Fix a ray character nu modulo 36, of trivial
infinity type and order dividing six, exactly as in paper 8 v1. Fixed
finite combinations of those sections, including the primary-section
and reciprocity conversions used in the actual adjoint, are allowed.
No extension to an arbitrary order-six character or to every section
of the full 216-component functional-equation vector is asserted.
Write

\[
 D_\nu(r,u)=\sum_c\frac{\nu(c)g_6(r,c)}{(Nc)^u},
 \quad
 H_\nu(r,u)=\sum_{(c,r)=1}\frac{\nu(c)g_6(r,c)}{(Nc)^u},
 \quad\theta=7/6.
\]

Write rho_full and rho_prim for their residues at theta. The raw
exponent convention is essential.

Import paper 10 v2, Section 3, equations (3.2), (3.3), and (3.6)--(3.7),
from the version-pinned source
<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>,
SHA256 `525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`.

Import paper 8 v1, Section 3, equation (3.2): for every numerator r,
including all valuations at an excluded prime,

\[
 \rho_{Q,\nu}(r)
   =\prod_{p\mid Q}(1+(Np)^{-1})^{-1}\rho_{\rm full,\nu}(r).
 \tag{1}
\]

The display source is
<https://rstation.ai/problems/riemann_hypothesis/papers/8>.
Its version pin is
<https://rstation.ai/api/v1/papers/riemann_hypothesis_8/versions/1/download>.
The local snapshot `work/round3_sources/paper8-v1.md` has SHA256
`f1f9aed624908ccb9b6842911d898916230545ff76dc123187d7eadc3558def1`.
Its fixed residual square-sum estimate, Section 4, and
\(t_\nu(n)=(Nn)^{1/12}\rho_{\rm full,\nu}(n)\), give

\[
 \sum_{n\asymp D}|\rho_{\rm full,\nu}(n)|^2
       \ll_{\epsilon,\nu}D^{5/6+\epsilon}.
 \tag{2}
\]

This is a fixed-form estimate, used only for the fixed components nu.

## 2. The complete divisor residue identity

For squarefree n, paper 10 gives

\[
 H_\nu(n,u)=E_n(u)^{-1}
       \sum_{d\mid n}a(n,d)(Nd)^{3/2-2u}D_\nu(nd^2,u),
 \tag{3}
\]

\[
 E_n(u)=\prod_{p\mid n}(1-(Np)^{5-6u}),\qquad
 a(n,d)=\mu(d)\nu(d)^2\gamma_2(d)
                  \overline{\chi_d(n/d)}^{\,2}.
 \tag{4}
\]

The fixed reciprocity phases in (4) are retained; they are not replaced
by absolute values. At numerator valuations 1 and 3, the local inversion
does not change the ray component.

**Residue identity.** For every squarefree n and every d|n,

\[
 \boxed{\quad
 a(n,d)(Nd)^{-5/6}\rho_{\rm full,\nu}(nd^2)
     =\frac{\mu(d)}{Nd}\rho_{\rm full,\nu}(n).
 \quad}
 \tag{5}
\]

To prove it, fix a prime p with q=Np and write the numerator as kp^j,
where (k,p)=1 and j is 1 or 3. The local identity is

\[
 D_j=H_j+a_j H_{4-j},\qquad
 a_j(u)=\nu(p)^{j+1}q^{j+1/2-(j+1)u}
                 \gamma_{j+1}(p)\chi_p(k)^{-(j+1)}.
\]

Apply (1) to both primitive-at-p residues. At u=theta this gives

\[
 \rho(D_j)=\frac q{q+1}
           \bigl(\rho(D_j)+a_j(\theta)\rho(D_{4-j})\bigr),
\]

hence

\[
 a_j(\theta)\rho(D_{4-j})=q^{-1}\rho(D_j).
 \tag{6}
\]

The selected term in primitive inversion has coefficient -a_j. Iterate
(6) over the primes selected in d, in the same fixed order used to
construct (3). The assembled coefficient is exactly (4), by the phase
calculation in paper 10 (3.7). Every selected prime changes valuation 1
to 3 and contributes -q^(-1). This proves (5), without a scalar
multiplicativity assumption for the theta coefficients.

As a check, summing (5) in (3) at theta gives

\[
 E_n(\theta)^{-1}\sum_{d\mid n}\frac{\mu(d)}{Nd}
 =\prod_{p\mid n}\frac{1-q^{-1}}{1-q^{-2}}
 =\prod_{p\mid n}(1+q^{-1})^{-1},
\]

which recovers the primitive density (1).

## 3. The exact integrated expansion

Fix one nonzero smooth annular function w, with support in [a,b] for
0<a<b<infinity, and put c_w=widehat w(2/3). It need not be nonnegative
for this identity. For eta>0 sufficiently small, define

\[
 \mathcal E_L[D_\nu(r)]
  =\frac1{2\pi i}\int_{(1+\eta)}
       D_\nu(r,u)\widehat w(u-1/2)L^{u-1}\,du.
 \tag{7}
\]

Define \(\mathcal E_U[H_\nu(n)]\) by the same integral with H.
Shifting from an absolute line to 1+eta gives

\[
 \mathcal E_L[D_\nu(r)]
  =L^{-1/2}\sum_c\frac{\nu(c)g_6(r,c)}{\sqrt{Nc}}
                     w(Nc/L)
     -c_wL^{1/6}\rho_{\rm full,\nu}(r).
 \tag{8}
\]

All moduli occur in (8), including nonsquarefree ones and moduli sharing
primes with r. No coprime squarefree truncation is being made.

The factor E_n(u)^(-1) in (3) must remain inside Mellin inversion. Its
geometric expansion on the line of (7) is

\[
 E_n(u)^{-1}=\sum_{k\mid n^\infty}(Nk)^{5-6u}.
 \tag{9}
\]

Substitution in (3), followed by the exact power calculation

\[
 (Nd)^{3/2-2u}(Nk)^{5-6u}U^{u-1}
  =(Nd)^{-1/2}(Nk)^{-1}
       \left(\frac{U}{(Nd)^2(Nk)^6}\right)^{u-1},
\]

gives

\[
 \boxed{\quad
 \mathcal E_U[H_\nu(n)]
 =\sum_{d\mid n}a(n,d)(Nd)^{-1/2}
       \sum_{k\mid n^\infty}(Nk)^{-1}
       \mathcal E_{U/((Nd)^2(Nk)^6)}[D_\nu(nd^2)].
 \quad}
 \tag{10}
\]

For each fixed n, the k expansion is absolutely convergent on the
original line, with weights (Nk)^(-1-6eta). Smooth Mellin decay justifies
the interchange. The finite d sum introduces no convergence issue.

## 4. Exact empty-modulus tail

Let D0>=sqrt(bU), and retain in (10) only the terms Nd>D0. For every
such d and every k in (9),

\[
 b\frac{U}{(Nd)^2(Nk)^6}<1.
\]

Every nonzero integral ideal c has Nc>=1. The finite sum in (8) is
therefore empty. This observation includes the unit modulus: it is
absent because its norm is outside the support, not because it is
dropped from the series.

Using (5) inside (10), the tail is exactly

\[
 \boxed{\quad
 \mathcal T_{U,D0}(n)
 =-c_wU^{1/6}E_n(\theta)^{-1}\rho_{\rm full,\nu}(n)
       \sum_{\substack{d\mid n\\Nd>D0}}\frac{\mu(d)}{Nd}.
 \quad}
 \tag{11}
\]

Indeed, after substituting the pole term in (8), the d power is
(Nd)^(-1/2-1/3)=(Nd)^(-5/6), and the k power is
(Nk)^(-1-1)=(Nk)^(-2). The former is exactly the power in (5); the
latter sums to E_n(theta)^(-1).

Since

\[
 1\le E_n(\theta)^{-1}
      =\prod_{p\mid n}(1-q^{-2})^{-1}\le\zeta_E(2),
\]

and

\[
 \left|\sum_{\substack{d\mid n\\Nd>D0}}\frac{\mu(d)}{Nd}\right|
       \le\frac{\tau(n)}{D0}\ll_\epsilon\frac{(Nn)^\epsilon}{D0},
 \tag{12}
\]

the tail is small even without a further cancellation estimate in d.

## 5. Pairing the actual coefficient

Let

\[
 b_n=1_{(n,Q)=1}\frac{\mu(n)\nu_0(n)}{\sqrt{Nn}}W(Nn/D),
\]

with the inherited fixed profile, fixed ray data, and an optional fixed
ray-sector filter. Since \(\|b\|_2\ll1\), equations (2), (11), and (12)
give

\[
 \boxed{\quad
 \left|\sum_n b_n\mathcal T_{U,D0}(n)\right|^2
   \ll_{\epsilon,w,W}(UD)^\epsilon
             U^{1/3}D^{5/6}D0^{-2},
 \qquad D0\ge\sqrt{bU}.
 \quad}
 \tag{13}
\]

The mask (n,Q)=1 can only reduce the coefficient norm. Thus this bound
does not need any additional uniform moving-level residual theorem.
Taking D0 comparable to sqrt(U), with the fixed support constant
included, yields

\[
 \left|\sum_n b_n\mathcal T_{U,D0}(n)\right|^2
       \ll(UD)^\epsilon U^{-2/3}D^{5/6}.
 \tag{14}
\]

The remaining divisors have Nd at most a fixed multiple of sqrt(U).
This note does not estimate them. In particular it does not remove the
medium-divisor interval remaining in an attempted reflected inverse
estimate.

## 6. The whole empty physical region

There is a useful stronger truncation of the double sum in (10). Keep
every pair (d,k) satisfying
\((Nd)^2(Nk)^6>bU\), whether or not Nd exceeds sqrt(bU). Its
contribution is exactly

\[
 -c_wU^{1/6}\rho_{\rm full,\nu}(n)
  \sum_{\substack{d\mid n,\ k\mid n^\infty\\
                  (Nd)^2(Nk)^6>bU}}
           \frac{\mu(d)}{Nd(Nk)^2}.
 \tag{15}
\]

For every fixed 0<sigma<1/3, Rankin's elementary inequality gives

\[
 \sum_{\substack{d\mid n,\ k\mid n^\infty\\
                  (Nd)^2(Nk)^6>bU}}
       \frac1{Nd(Nk)^2}
 \le (bU)^{-\sigma}
       \sum_{d\mid n}(Nd)^{-1+2\sigma}
       \prod_{p\mid n}(1-(Np)^{-2+6\sigma})^{-1}
 \ll_{\sigma,\epsilon}U^{-\sigma}(Nn)^\epsilon.
 \tag{16}
\]

The exponent 2-6sigma is strictly positive. For every fixed a>0 and
every epsilon>0,
\(\prod_{p\mid n}(1-(Np)^{-a})^{-1}\ll_{a,\epsilon}(Nn)^\epsilon\):
separate finitely many small primes, and bound each remaining logarithm
by epsilon times log(Np). The d sum in (16) is at most tau(n), since
-1+2sigma<0. This proves the stated uniform divisor bound without
claiming absolute convergence of the unrestricted Euler product at
exponent 2-6sigma.

By (2) and coefficient Cauchy--Schwarz, the squared pairing of (15)
with the actual b is at most

\[
 \ll_{\sigma,\epsilon,w,W}(UD)^\epsilon
                   U^{1/3-2\sigma}D^{5/6}.
 \tag{17}
\]

Equivalently, choosing sigma sufficiently close to 1/3, this is
\(\ll_\epsilon(UD)^\epsilon U^{-1/3}D^{5/6}\).
Thus the entire double sum can be reduced, with this explicit pole
error, to the finite physical region
\((Nd)^2(Nk)^6\le bU\). This still leaves the medium-divisor head; it
does not estimate that head or the full inverse moment.

## 7. Functional-equation orientation and scope

Bröker--Hoffstein, arXiv:1312.0568v1, Section 3 equation (3.1), maps
\(\Psi(r,s,\eta_i)\) to \(\Psi(r,-s,\eta_j)\) with the same numerator r
and the same embedding epsilon. Their explicit reflected expansion
(3.9) retains \(g_6(r,\varepsilon,c)\); it does not conjugate the
sextic symbol. Consequently, in the coprime squarefree-modulus branch,
writing n=dm, the factors

\[
 \overline{\chi_d(m)}^{\,2}\overline{\chi_c(m)}
\]

combine by squared reciprocity into
\(\overline{\chi_m(cd^2)}\), with the remaining ordinary reciprocity
factor handled in the fixed ray sector. The inverse row is cd^2 in
this orientation. Formula (10), unlike this illustrative coprime
branch, retains every full modulus.

The local and empty-modulus identities above do not use a reflected
contour and make no claim about possible cancellations between a
reflected theta pole and an archimedean zero. Such a cancellation must
be checked with the complete finite-vector functional equation.

Finally, the adjoint identity supplies
\(\langle A_U\alpha,v_1\rangle\), or its finite family of label
analogues. A bound for these pairings is not a bound for
\(\|A_U\alpha\|_2^2\). Transfer to the original signed offdiagonal
return, or an estimate of the full complementary operator, is a
separate required step.
