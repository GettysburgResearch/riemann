# Literal-source continuum residual: analytic derivation and directed experiment

Date: 2026-10-10. This file accompanies `enclose_analytic_upper.py`,
`source_convolution.py`, and `enclose_residual.py`. Its analytic argument is
submitted for independent review. The computational receipt is provisional
until that review and a complete directed replay succeed. It proves nothing
about all windows or the xi/Weil terminal adapter.

## Source and target

Use the exact source and Hilbert-space hypotheses O1--O4 in the inherited
`reviews/C/pass4-math-completion/proofs/OPERATOR_AUDIT.md`. Put

\[
b=3/2,\quad c=1/2,\quad d=\log2,\quad q_2=\log2/\sqrt2,\quad
P_2=-\zeta'(2)/\zeta(2),\quad C_b=(1-\gamma-\log(2\pi))/3.
\]

For \(0\le x\le1\), the literal whole source is exactly

\[
W(x)=\tfrac12e^{cx}+C_be^{-bx}+\Gamma(x)-\frac{P_2}{b}\cosh(bx)
+\frac{q_2}{b}\sinh(b(x-d))\mathbf1_{x\ge d},\qquad
\Gamma(x)=\sum_{j\ge1}\frac{e^{-\lambda_jx}}{\lambda_j^2-b^2},\quad
\lambda_j=2j+\tfrac12.
\tag{1}
\]

No prime tail has been discarded. Every prime power \(n\ge3\) is outside this
window and is included in \(P_2\). Let
\(q(h,k)=b\int_0^1\overline{h(t)}\int_0^1W(t-u)k(u)\,du\,dt\).
The independently reviewed `CODIMENSION_14_REFINEMENT.md` gives, on
\(V=E^\perp\),

\[
E=\operatorname{span}\{\sin(j\pi t):1\le j\le11; e^{ct},e^{-ct},\cosh(bt)\},
\qquad q(v,v)\ge\frac65\|\phi_v'\|_2^2,
\tag{2}
\]

where \(\phi_v''-c^2\phi_v=v\) and all clamped boundary conditions follow
from the moment constraints. For any exact trials \(v_i\in V\) and
orthonormal \(e_i\in E\), put \(z_i=e_i-v_i\),

\[
U_{ij}=q(z_i,z_j),\quad
F_z=-K_z'+c^2\int_0^tK_z(s)\,ds,\quad K_z(t)=\int_0^1W(t-u)z(u)\,du,
\quad R_{ij}=\langle\Pi F_{z_i},\Pi F_{z_j}\rangle.
\]

Here \(\Pi\) is the orthogonal projection off
\(1,\cos(j\pi t)\ (1\le j\le11),\sinh(bt)\). The source coupling in the
inherited audit gives

\[
U-\frac{15}{8}R\preceq S\preceq U.\tag{3}
\]

A strictly positive directed lower matrix in (3), together with (2), would
close **the single literal window \(L=1\)**, conditional on O1--O4. Positive
finite Galerkin \(U\) alone does not do so.

## Complete Laplace transforms and exact finite trials

Define \(T(z)=\int_0^1W(x)e^{zx}\,dx\), and
\(f(z)=(e^z-1)/z=e^{z/2}\operatorname{sinc}(iz/2)\), with removable value
\(f(0)=1\). Every nongamma term in (1) has an elementary transform using
\(f\), or the interval transform
\(e^{zd}(1-d)f(z(1-d))\). The entire identity for \(f\) avoids division by
an interval enclosing zero.

For gamma, put \(g(z)=\psi(5/4-z/2)\) and
\(\ell(z)=((z+b)g(b)+(b-z)g(-b))/(2b)\). Absolute convergence and the
partial fraction identity give

\[
A(z)=\sum_{j\ge1}\frac{1}{(\lambda_j-z)(\lambda_j^2-b^2)}
=-\frac{g(z)-\ell(z)}{2(z^2-b^2)}.\tag{4}
\]

At \(z=\pm b\), the producer uses the removable values and derivatives
obtained from \(g',g''\); it never divides by the zero denominator. Therefore

\[
T_\Gamma(z)=A(z)-e^z\sum_{j\ge1}
\frac{e^{-\lambda_j}}{(\lambda_j-z)(\lambda_j^2-b^2)}.\tag{5}
\]

All frequencies used are real \(\pm c,\pm b\), or imaginary \(ij\pi\).
For \(J=50\), \(\lambda_0=2(J+1)+1/2\), the omitted part of (5) is bounded
in complex absolute value by

\[
\delta=\frac{e^{b-\lambda_0}}
 {(\lambda_0-b)^2\lambda_0(1-e^{-2})}.
\tag{6}
\]

Indeed \(|\lambda_j-z|\ge\lambda_j-b\), \(|e^z|\le e^b\), and
\(\lambda_j^2-b^2\ge\lambda_j(\lambda_j-b)\). The derivative tail is at
most \(\delta(1+1/(\lambda_0-b))\). The producer adds a rectangular complex
ball of radius \(\delta\) in each component, which encloses an absolute
error of size at most \(\delta\).

The exact double integral for exponential basis functions is

\[
D(\alpha,\beta)=
\frac{e^{\alpha+\beta}(T(-\alpha)+T(-\beta))-T(\alpha)-T(\beta)}
{\alpha+\beta}.
\tag{7}
\]

When \(\alpha+\beta=0\), its exact value is
\(T(\alpha)+T(-\alpha)-T'(\alpha)-T'(-\alpha)\). Splitting the square into
\(t\ge u\) and \(u\ge t\) proves (7). Semantic frequency keys ensure exact
zero sums are handled by the removable formula.

Let \(B\) be the listed basis of \(E\), and \(H\) be the next 100 sine
modes. Compute the exact ordinary Gram matrix \(G\) and form matrix \(Q\)
using (7), multiplying \(D\) by \(b\). If \(G_{EE}=LL^T\),
\(O=(L^T)^{-1}\) makes \(e=BO\) orthonormal. Put
\(C=O^TG_{EH}\), so the trial columns \(v=H-eC\) lie exactly in \(V\).
Let \(Q_{vv}\) and \(Q_{ve}\) be their exact form blocks and
\(A=Q_{vv}^{-1}Q_{ve}\). The chosen trials are \(vA\), with

\[
z=B\,O(I+CA)-H A,\qquad U=Q_{ee}-Q_{ev}Q_{vv}^{-1}Q_{ve}.
\tag{8}
\]

All transforms, Cholesky operations, solves and coefficients in (8) are
outward Arb/acb balls. These are enclosures of exact quantities, rather than
rounded coefficients defining a different trial space.

## Incomplete gamma transforms and the source primitive

For \(\Re a>0\), write
\(S_r(a)=\sum_{j\ge1}e^{-\lambda_ja}/(\lambda_j-r)\).
Partial fractions give, for \(z\ne\pm b\),

\[
C_a(z)=\sum_{j\ge1}\frac{e^{-\lambda_ja}}
{(\lambda_j-z)(\lambda_j^2-b^2)}
=\frac{S_z(a)-((z+b)S_b(a)+(b-z)S_{-b}(a))/(2b)}{z^2-b^2}.
\tag{9}
\]

Put \(t=e^{-a}\). Then

\[
S_b=e^{-ba}\operatorname{atanh}t,\quad
S_{-b}=-\tfrac12e^{ba}(\log(1-t^2)+t^2),
\]
\[
S_c=-\tfrac12e^{-a/2}\log(1-t^2),\quad
S_{-c}=e^{a/2}(\operatorname{atanh}t-t).
\tag{10}
\]

For an imaginary frequency \(z\), put \(\alpha=5/4-z/2\). The convergent
series identity on \(|t|<1\) gives

\[
S_z=\tfrac12 e^{-5a/2}
\frac{{}_2F_1(1,\alpha;\alpha+1;t^2)}{\alpha}.
\tag{11}
\]

The Arb hypergeometric flags `abc=True, bc=True` encode the exact identities
\(c-a-b=0\) and \(c-b=1\). They are mathematically justified here.
For the two repeated poles, define

\[
D_b=\tfrac12e^{-ba}(\operatorname{Li}_2(t)-\operatorname{Li}_2(-t)),\quad
D_{-b}=\tfrac14e^{ba}(\operatorname{Li}_2(t^2)-t^2),\quad
m=(S_b-S_{-b})/(2b).
\]

Then \(C_a(b)=(D_b-m)/(2b)\), and
\(C_a(-b)=(D_{-b}-m)/(-2b)\). These follow either by differentiating
\(S_z\) or from the squared-denominator series. Consequently

\[
\int_0^a\Gamma(x)e^{zx}\,dx=A(z)-e^{za}C_a(z).\tag{12}
\]

For use in \(W\) and its primitive, direct summation gives

\[
\Gamma(x)=\frac{e^{-x/2}}6+rac{\cosh(bx)}3\log(1+e^{-x})
+\frac{\sinh(bx)}3\log(1-e^{-x}).\tag{13}
\]

Its primitive is \(\int_0^x\Gamma=G_0-G_{\rm tail}(x)\), where
\(G_0=(7-\pi-4\log2)/9\), and, writing \(r=e^{-x/2},t=e^{-x}\),

\[
G_{\rm tail}= -\frac49(\operatorname{atanh}r+\arctan r-2r)
+\frac29\left(e^{-bx}\operatorname{atanh}t-rac12e^{bx}
(\log(1-t^2)+t^2)\right).\tag{14}
\]

The logarithmic expressions are analytic in \(\Re x>0\) on their indicated
branches. Their derivatives and their vanishing limit at infinity prove
(14). Formula (13) has a finite limit at zero, but its derivative has a
logarithmic cusp; no bounded second derivative at zero is assumed.

## Exact convolution residual

For \(z(u)=e^{\beta u}\), and \(T_a(z)=\int_0^aW(x)e^{zx}\,dx\),

\[
K_\beta(t)=e^{\beta t}\{T_t(-\beta)+T_{1-t}(\beta)\},\quad
K_\beta'=\beta K_\beta+W(t)-e^\beta W(1-t).
\]

Using \(H(t)=\int_0^tW\), and \(K_\beta(0)=T(\beta)\), integration gives

\[
F_\beta(t)=(-\beta+c^2/\beta)K_\beta(t)-W(t)+e^\beta W(1-t)
+\frac{c^2}{\beta}\{-T(\beta)-H(t)+e^\beta(H(1)-H(1-t))\}.
\tag{15}
\]

The frequencies never contain \(\beta=0\). At the endpoints this simplifies
to the finite formulas printed in `source_convolution.py`. On the real axis
\(F_{\sin j\pi t}=\Im F_{ij\pi}\). Its analytic extension is
\((F_{ij\pi}-F_{-ij\pi})/(2i)\), so a uniform bound valid for both signs
bounds that extension. The real exponential and cosh basis values follow by
linearity.

The only interior source cusps in (15) occur at \(d\) and \(1-d\). Integrate
separately on \([0,1-d]\), \([1-d,d]\), and \([d,1]\). In each slab the
corresponding branch of (1) is an analytic expression. Its analytic extension
may cross a cusp; the integration nodes stay inside the original slab.

## Cauchy--Gaussian error on the full covered interval

Each normalized slab has its two intervals of length
\(\epsilon=2^{-60}\) omitted. Dyadic panels cover the rest exactly, with
normalized panel width at most \(1/100\). For physical midpoint \(m\) and
half-width \(h\), the producer explicitly checks the disk of radius \(R=2h\)
satisfies \(0<\Re t<1\), \(|\Im t|\le R\le1/100\).

On that disk the analytically continued branch in (1) satisfies \(|W|<8\).
For example, bound the gamma series by its value at zero \(<2/5\), and use
\(|e^{\pm b t}|\le e^b<5\), \(|e^{ct}|<2\),
\(|C_b|<1/2\), \(P_2<3/5\), \(q_2<1/2\), and
\(|\sinh(b(t-d))|\le e^{b|\Re t-d|+b|\Im t|}<3\).
Their sum is below eight. The straight paths used in incomplete integrals
stay in the same half plane and have \(|t|,|1-t|<1.01\).

Let \(\omega_*=(11+100)\pi\). For every primitive basis frequency, (12)
is the analytic path integral of the gamma series. A branch with its prime
correction active has that correction integrated from \(d\) to the length,
rather than from zero. There is at most one active prime correction in any
slab. The base paths have total length below \(1.02\), and the additional
prime path has length below \(0.71\). The prime branch integrand itself is
bounded by one. Thus the sum of the two source partial integrals is bounded
by \(16e^{b+\omega_*R}\). It follows that

\[
|K_\beta|\le16 e^{3+2\omega_*/100},\qquad
|F_\beta|\le(\omega_*+1/2)16e^{3+2\omega_*/100}+100=:M_0.
\tag{16}
\]

For the additive 100, use \(|W|<8\), \(|e^\beta|<5\),
\(|T(\beta)|<20\), \(|H(t)|,|H(1-t)|<8.8\), \(|H(1)|<4\), and
\(c^2/|\beta|\le1/2\) in (15):
\(8+40+\tfrac12(20+8.8+5(4+8.8))<100\). The incomplete primitive
bound includes an optional prime integral of size below \(0.71\), in
addition to its base bound \(8.08\).
If \(C_*\) is the largest exact column sum of absolute trial coefficients
in (8), then \(|F_{z_i}|\le M=M_0C_*\). The implementation takes the
maximum of the directed upper endpoints of every column sum, without float
selection. Projection test functions satisfy \(|p|<3\) on these disks;
for cosine tests this is checked from \(e^{11\pi/100}<3\).

For an analytic integrand bounded by \(B\) on \(|t-m|\le2h\), Cauchy
bounds the Taylor remainder after degree \(2n-1\) by
\(2B\,2^{-2n}\) throughout \([m-h,m+h]\). An \(n\)-point Legendre rule
is exact for that Taylor polynomial and has positive weights summing to
\(2h\). Its error is therefore at most

\[
8hB\,2^{-2n}.\tag{17}
\]

Use \(n=80\), \(B=M^2\) for \(F_iF_j\), and \(B=3M\) for \(pF_i\).
Arb `legendre_p_root(n,k,weight=True)` encloses the actual nodes and weights.
Every node function and arithmetic operation is evaluated with outward balls;
(17) is then added as an extra interval error.

## Omitted pieces: an explicit logarithmic modulus

For real \(|x|\le1\), (1) gives \(|W(x)|<4\). For \(0<\delta\le1/2\),
its even extension obeys

\[
\omega_W(\delta)\le\delta(7+2\log(1/\delta)).\tag{18}
\]

To see the gamma part, use \(\lambda_j\le(5/2)j\),
\((\lambda_j^2-b^2)^{-1}\le1/(4j^2)\), and split at
\(J=\lfloor1/\delta\rfloor\). The low part is at most
\((5\delta/8)(1+\log(1/\delta))\), and the high part is at most
\(\delta/2\). The other terms in (1) have piecewise derivatives of
absolute value below five; their continuous joins preserve that Lipschitz
bound. Their sum with the gamma estimate gives (18).

Integration by parts, valid for the audited \(W^{1,1}\) source, gives

\[
K_z'(t)=W(t)z(0)-W(t-1)z(1)+\int_0^1W(t-u)z'(u)\,du.
\]

Consequently

\[
|F_z(t)-F_z(s)|\le
\omega_W(|t-s|)(|z(0)|+|z(1)|+\|z'\|_1)
+c^2|t-s|\|W\|_\infty\|z\|_1.\tag{19}
\]

For the exact trial coefficients, \(\|z\|_\infty\le5C_*\),
\(\|z'\|_1\le(\omega_*+8)C_*\). The producer evaluates (15) at all
four anchors \(0,1-d,d,1\), using the endpoint formulas at 0 and 1, and
checks every \(|F_z|<1\). It also checks the right side of (19), at distance
\(\epsilon\), is below one. Thus \(|F_z|<2\) on every omitted piece.
Total omitted length is at most \(6\epsilon\); adding radii
\(24\epsilon\) for each FF entry and \(36\epsilon\) for each pF entry
therefore encloses all omitted integrals. Real projection functions satisfy
\(|p|<3\).

## Projection and final acceptance

Let \(P\) list \(1,\cos(j\pi t),\sinh(bt)\). Its exact Gram matrix has
\(G_{00}=1\), \(G_{jj}=1/2\), zero cross cosine/constant entries, and

\[
G_{0s}=(\cosh b-1)/b,\quad
G_{js}=b\{(-1)^j\cosh b-1\}/(b^2+j^2\pi^2),\quad
G_{ss}=\sinh(2b)/(4b)-1/2.
\]

With \(J_{ij}=\int F_iF_j\), \(A_{ki}=\int p_kF_i\), the exact residual
matrix is \(R=J-A^TG^{-1}A\). All covered and omitted integrals are
included in the outward balls. The producer forms the symmetric ball matrix
\(U-(15/8)R\), then verifies LDL pivots for the matrix minus \(10^{-11}I\).
Strictly positive interval pivots certify positive definiteness of that exact
matrix. An inconclusive pivot is only a failed enclosure or failed lower
bound, and supplies no negative-source conclusion.

The complete receipt records panel coverage, bounds, U receipt, matrix balls,
precision, source hashes, timing, and the provisional review status. No
ordinary floating-point eigenvalue is used for acceptance. The replay still
relies on python-flint/FLINT's documented outward transcendental and matrix
operations; a separate rational-only verification is not claimed.
