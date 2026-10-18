# Exact moment preservation does not make a theta zero strip stable

Status: a proved obstruction for a class of Fourier kernels, with an application
to perturbations of the actual Riemann theta kernel. This is **not** a new
zero-free region for zeta. The perturbed kernels are not claimed to retain the
Jacobi modular identity or an Euler product.

The point of the theorem is specific. A global zero-strip argument cannot be
closed from positivity, strong log-concavity, smooth proximity to the exact
theta kernel, and any prescribed finite set of its moments. All these
properties survive the perturbations below, while a zero can be placed at
any fixed distance from the real axis and arbitrarily high real part.

## 1. Kernel assumptions and notation

Let \(\phi:\mathbb R\to(0,\infty)\) be even and smooth. Assume that for every
real \(b\), every nonnegative integer \(j\), and every nonnegative integer
\(N\),

\[
 \sup_{t\in\mathbb R}(1+|t|)^N
       \left|\frac{d^j}{dt^j}\{e^{bt}\phi(t)\}\right|<\infty.       \tag{1}
\]

Thus every exponential tilt is a Schwartz function. Write

\[
 F(z)=\int_{\mathbb R}\phi(t)e^{izt}\,dt,
 \qquad
 m_{2j}=\frac{\int_{\mathbb R}t^{2j}\phi(t)\,dt}{F(0)}.
\]

Dominated differentiation on compact subsets makes \(F\) entire. Integration
by parts gives, for every fixed compact interval \(I\subset\mathbb R\),

\[
 \sup_{b\in I}|F^{(j)}(T+ib)|=O_{I,j,N}((1+|T|)^{-N}).            \tag{2}
\]

The uniform version follows from domination by finitely many exponential
tilts at the endpoints of a slightly larger interval; derivatives of those
tilts include only polynomial factors in \(b\). No unproved estimate for
\(1/F\) is used.

## 2. The theorem

**Theorem.** Fix \(K\ge0\) and \(B>0\). There are even smooth positive
kernels \(\phi_T\), defined for every sufficiently large real \(T\), such
that:

1. The normalized even moments through degree \(2K\) of \(\phi_T\) equal
   those of \(\phi\) exactly.
2. Their normalized Fourier transforms have a zero at \(T+iB\), and hence
   also at \(\pm T\pm iB\).
3. For every fixed \(b,j,N,A\),
   \[
   \sup_t(1+|t|)^N
   \left|\frac{d^j}{dt^j}
       \{e^{bt}(\phi_T(t)-\phi(t))\}\right|=O(T^{-A}).             \tag{3}
   \]
   In particular the transforms converge locally uniformly to the original
   transform faster than every power of \(T\).
4. If \((\log\phi)''\le-c<0\) on the whole real line, the construction can
   be chosen so that \((\log\phi_T)''\le-c/2\) there.

The unnormalized kernels in this statement need not have exactly the original
mass. Normalizing each kernel to the original mass preserves assertions 1,
2, and 4 and preserves convergence (3).

### 2.1 Fixed moment corrections with an invertible matrix

Assume first \(K\ge1\). Set

\[
 L_j(k)=\int_{\mathbb R}(t^{2j}-m_{2j})\phi(t)\cos(kt)\,dt,
 \quad 1\le j\le K.
\]

There exist fixed distinct positive \(k_1,\ldots,k_K\) for which the matrix
\(L=(L_j(k_\ell))_{j,\ell=1}^K\) is invertible.

To prove this, expand at \(k=0\). The constant coefficient vanishes and

\[
 L_j(k)=\sum_{r\ge1}\frac{(-1)^r k^{2r}}{(2r)!}\,C_{jr},
 \quad
 C_{jr}=\int(t^{2j}-m_{2j})(t^{2r}-m_{2r})\phi(t)\,dt.             \tag{4}
\]

The \(K\times K\) covariance matrix \((C_{jr})_{j,r=1}^K\) is positive
definite: a nonzero polynomial \(\sum_{j=1}^K a_jt^{2j}\) cannot equal a
constant on the support of a strictly positive density on \(\mathbb R\).
Choose distinct positive \(u_1,\ldots,u_K\) and put \(k_\ell=\delta u_\ell\).
The first nonzero term in the determinant expansion is

\[
 \delta^{K(K+1)}\det(C_{jr})_{j,r=1}^K
 \left(\prod_{r=1}^K\frac{(-1)^r}{(2r)!}\right)
 \det(u_\ell^{2r})_{r,\ell=1}^K.                                 \tag{5}
\]

The last determinant is a nonzero Vandermonde determinant times
\(\prod_\ell u_\ell^2\). Hence sufficiently small fixed \(\delta>0\)
works. Analyticity used in (4) follows from (1).

### 2.2 Two independent directions for a prescribed complex zero

Let \(M(b)=F(ib)=\int\phi(t)\cosh(bt)\,dt\). Positivity and evenness give
\(M(B)>0\) and

\[
 M'(B)=\int t\sinh(Bt)\phi(t)\,dt>0.
\]

Since \(F'(iB)=-iM'(B)\), there exists a fixed sufficiently small \(h>0\)
such that \(\Im F(h+iB)\ne0\). Thus the two complex numbers
\(F(iB)/2\) and \(F(h+iB)/2\) are linearly independent over \(\mathbb R\).

Use the finite trigonometric modulation

\[
 g_T(t)=\alpha_T\cos(Tt)+\beta_T\cos((T-h)t)
              +\sum_{\ell=1}^K c_{\ell,T}\cos(k_\ell t).          \tag{6}
\]

At \(\rho_T=T+iB\), the first two transform columns are

\[
 A_T=\tfrac12\{F(2T+iB)+F(iB)\},
 \qquad
 B_T=\tfrac12\{F(2T-h+iB)+F(h+iB)\}.                             \tag{7}
\]

The fixed-frequency columns are

\[
 C_{\ell,T}=\tfrac12\{F(T+k_\ell+iB)+F(T-k_\ell+iB)\}.           \tag{8}
\]

Impose the two real equations

\[
 F(\rho_T)+\alpha_T A_T+\beta_T B_T
                +\sum_\ell c_{\ell,T}C_{\ell,T}=0                \tag{9}
\]

and the \(K\) real equations

\[
 \int(t^{2j}-m_{2j})\phi(t)g_T(t)\,dt=0,
 \qquad 1\le j\le K.                                           \tag{10}
\]

By (2), the coefficient matrix of (9)--(10) converges to a block diagonal
matrix. Its first block consists of the real and imaginary parts of
\(F(iB)/2,F(h+iB)/2\), and its second block is \(L\). Both are invertible.
The matrix is therefore invertible for all sufficiently large \(T\), with
a uniformly bounded inverse. Its only nonzero right-hand entries are the
real and imaginary parts of \(-F(\rho_T)\). Consequently, for every \(A\),

\[
 |\alpha_T|+|\beta_T|+\sum_\ell|c_{\ell,T}|=O(T^{-A}).            \tag{11}
\]

For \(K=0\), simply omit the second block and all the fixed frequencies.

### 2.3 Positivity, moments, convergence, and curvature

Set \(\phi_T=\phi(1+g_T)\). The coefficient bound gives
\(\|g_T\|_\infty\to0\), so this is a strictly positive even kernel for
large \(T\). Equations (10) say exactly that

\[
 \int t^{2j}\phi_T(t)\,dt
       =m_{2j}\int\phi_T(t)\,dt,
\]

which proves normalized moment preservation. Equation (9) gives the exact
zero, not an approximate root of a truncated expression.

Every fixed derivative of \(g_T\) is a finite sum with coefficients bounded
by (11), multiplied by a fixed power of \(T\). The Leibniz rule and (1)
therefore prove (3).

Finally,

\[
 (\log\phi_T)''=(\log\phi)''+
       \frac{g_T''}{1+g_T}-\frac{(g_T')^2}{(1+g_T)^2}
 \le-c+\frac{\|g_T''\|_\infty}{1-\|g_T\|_\infty}.
\]

The last fraction tends to zero, proving the curvature assertion. This
completes the proof.

## 3. The actual theta source satisfies the hypotheses

In the physical \(\Xi(z)=\xi(1/2+iz)\) variable, take

\[
 \Phi(t)=\sum_{n\ge1}
 (4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})e^{-\pi n^2e^{2t}}
 \quad(t\ge0),                                                  \tag{12}
\]

with the even extension. Its normalized Fourier transform is
\(\Xi(z)/\Xi(0)\). The complete source and normalization were proved in
`standalone/2026-10-18-theta26-and-critical-family/theta/SOURCE26.md`
at repository commit `669b6a01f4d4858ae1ef806b07547be95c08c935`; alternatively
the classical theta integral gives the identity directly. This source is a
mathematical reference, not an imported executable dependency.

Positivity is termwise on \([0,\infty)\). Smooth evenness and decay of all
derivatives follow from the Jacobi transformation and the theta series;
see Csordas, Theorem 4.1. The decay is faster than
\(\exp[-c e^{2|t|}]\), for any fixed \(c<\pi\), up to derivative-dependent
factors. This implies (1).

For completeness, the strict concavity input also gives a **uniform**
curvature bound; pointwise negativity alone would not justify that claim.
Csordas, Theorem 4.2(b), cites the established theorem that
\(q(u)=\log\Phi(\sqrt u)\) has \(q''(u)<0\) for \(u>0\). Therefore

\[
 (\log\Phi(t))''=2q'(t^2)+4t^2q''(t^2)
     \le2q'(0)=\frac{\Phi''(0)}{\Phi(0)}.                         \tag{13}
\]

Here \(\Phi'(0)=0\) by evenness. The following elementary estimates give
\(\Phi''(0)<-3/2\) and \(\Phi(0)<5/2\), so the right side of (13) is
strictly less than \(-3/5\); in particular \(c=1/2\) is valid.

Put

\[
 p(x)=16x^4-112x^3+165x^2-\tfrac{75}{2}x.
\]

Differentiating (12) twice gives
\(\Phi''(0)=\sum_{n\ge1}p(\pi n^2)e^{-\pi n^2}\). Using
\(157/50<\pi<22/7\) gives

\[
 p(\pi)\le U:=16(22/7)^4-112(157/50)^3
                         +165(22/7)^2-(75/2)(157/50)<-394.
\]

As \(e<3\) and \(\pi<4\), the first summand is at most \(U/81\).
For \(x\ge\pi\), \(p(x)\le16x^4\). For \(n\ge2\), the consecutive
ratio of the majorants \(n^8e^{-\pi n^2}\) is at most

\[
 (3/2)^8 e^{-15}<(3/2)^8(3/8)^{15}<1/1000,
\]

where \(e>8/3\) follows from its first five series terms. Hence

\[
 \Phi''(0)
 \le U/81+
 \frac{16(22/7)^4\,2^8(3/8)^{12}}{1-1/1000}<-3/2.               \tag{14}
\]

Dropping negative terms in (12), and using the same geometric ratio bound
(which is also valid for the fourth powers), gives

\[
 \Phi(0)
 \le4(22/7)^2(3/8)^3+
 \frac{4(22/7)^2\,2^4(3/8)^{12}}{1-1/1000}<5/2.                 \tag{15}
\]

All strict inequalities at the right of (14)--(15) are rational
inequalities. They are deliberately loose; no floating-point value of a
theta derivative is needed.

## 4. Consequence and precise limitation

For any fixed \(K\) and any desired physical band \(B>0\), there are
arbitrarily close positive, strongly log-concave perturbations of the exact
theta kernel with exactly the same first \(K\) normalized even moments and
with zeros at height \(B\) above the Fourier real axis. The perturbations
preserve the elementary even functional symmetry and all prescribed finite
moment constraints. They do not preserve the full Jacobi modular identity,
the precise theta series, or a zeta Euler product.

This does **not** contradict local uniform closure of a fixed zero-free
domain: the imposed zeros escape to infinite real part. It instead shows
why estimates on compact complex domains and finitely many matched moments
cannot on their own control a strip over all heights. An argument for the
actual zeta function must use additional exact structure or establish the
cofinal all-order positivity premise directly.

## Sources

- G. Csordas, *Fourier transforms of positive definite kernels and the
  Riemann \(\xi\)-function*, arXiv:1309.0055v2, Theorems 4.1 and 4.2(b), and
  Remark 4.3(a): <https://arxiv.org/pdf/1309.0055>.
- G. Csordas and R. S. Varga, *Moment inequalities and the Riemann
  hypothesis*, Constructive Approximation 4 (1988), 175--198, the underlying
  concavity result identified as reference [21] in the preceding source.
- P. Biane, J. Pitman, and M. Yor, *Probability laws related to the Jacobi
  theta and Riemann zeta functions, and Brownian excursions*, Section 2:
  <https://arxiv.org/pdf/math/9912170>.

The interpolation construction and the explicit application bounds above
are derived here. No claim of priority over the complete literature is made.
