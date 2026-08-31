# T-108006 — Beta-pair symmetry selects one chiral cubic-cusp source carrier

Status: **exact insertion of the finite Chebyshev Perron--Fourier transform
into the assembled reciprocal-zeta/beta source; exact reduction of the two
kernel faces to one directed face by beta-pair evenness; exact reflected
vertical-convolution coordinate; exact one-sided cubic log-ratio carrier; and
exact exceptional-67 translate law with fixed-positive-damping decoupling.
No signed reciprocal-zeta correlation estimate, no direct undamped
nonzero-frequency boundary theorem, no full contour estimate, no new
zero-free region, and no proof of RH.**

Bounded replay:
[`beta_chebyshev_chiral_cusp_source_convolution.py`](beta_chebyshev_chiral_cusp_source_convolution.py).
Canonical output:
[`beta_chebyshev_chiral_cusp_source_convolution.json`](beta_chebyshev_chiral_cusp_source_convolution.json).

This packet continues
[T-108004](BETA_CHEBYSHEV_PERRON_FOURIER_CUSP_CARRIER.md). T-108004 found the
complete symmetric two-parameter cubic cusp seen by the Perron integral. The
new point is that the *assembled beta source is itself even in the Fourier
variable*. That exact algebra selects one of the two cusp faces before any
absolute value is taken.

## 0. Frozen notation

Let

\[
 B_\beta(w)=\frac{1-67^{-w}}{\zeta(w)}
\tag{0.1}
\]

and let \(R_r\) be the autocorrelation of the order-\(r\) Chebyshev step. Put

\[
 J_r(z)=\int_{\mathbb R}R_r(x)e^{-z|x|/2}\,dx,
 \qquad \Re z>0.
\tag{0.2}
\]

For the Perron coordinate

\[
 s=\frac{1+z}{2},
\tag{0.3}
\]

define the assembled beta-pair factor

\[
 P_z(t)=B_\beta(s-it)B_\beta(s+it).
\tag{0.4}
\]

It obeys the exact identity

\[
 \boxed{P_z(-t)=P_z(t)}
\tag{0.5}
\]

by commutativity of the two factors. No conjugation, reality assumption, or
critical-line specialization is involved.

T-108004 proves the exact two-face formula

\[
 \widehat R_{r,z}(t)
 =\frac12\{J_r(z+2it)+J_r(z-2it)\}.
\tag{0.6}
\]

The normalized constants from the earlier packets may be restored after the
identities below; the chiral reduction is an identity for the literal
unnormalized source integrand.

## 1. Exact directed-face theorem

Assume first that the displayed integrals are absolutely convergent. The same
identity then extends to every source-locked regularized/truncated form by
linearity and passage to the corresponding limit.

### Theorem T-108006A — one directed kernel face

One has

\[
 \boxed{
 \frac1{2\pi}\int_{\mathbb R}
 \widehat R_{r,z}(t)P_z(t)\,dt
 =
 \frac1{2\pi}\int_{\mathbb R}
 J_r(z+2it)P_z(t)\,dt.}
\tag{1.1}
\]

**Proof.** Insert (0.6). In the second face, substitute \(t\mapsto-t\):

\[
 \int_{\mathbb R}J_r(z-2it)P_z(t)\,dt
 =
 \int_{\mathbb R}J_r(z+2it)P_z(-t)\,dt.
\]

Equation (0.5) makes this equal to the first face. Their average is therefore
one copy of the first face. \(\square\)

This is not an estimate. It is an exact source-facing simplification. The
cosine symmetrization in the geometric kernel is removed only *after* the two
reciprocal-zeta factors have been assembled.

## 2. Reflected vertical beta convolution

Set

\[
 \omega=z+2it.
\tag{2.1}
\]

Then \(d\omega=2i\,dt\) and \(\Re\omega=\Re z\). Moreover,

\[
 s+it=\frac{1+\omega}{2},
 \qquad
 s-it=\frac{1+2z-\omega}{2}.
\tag{2.2}
\]

Consequently (1.1) is equivalent to

\[
 \boxed{
 \frac1{4\pi i}
 \int_{\Re\omega=\Re z}
 J_r(\omega)
 B_\beta\!\left(\frac{1+\omega}{2}\right)
 B_\beta\!\left(\frac{1+2z-\omega}{2}\right)
 \,d\omega.}
\tag{2.3}
\]

The two beta arguments are reflections across \(s=(1+z)/2\): their sum is
\(1+z=2s\). Thus the finite Chebyshev transform is paired with a genuine
one-variable vertical convolution, rather than an unrelated product of two
frequency samples.

This coordinate is useful because the geometric factor now depends on one
vertical variable \(\omega\), while the reciprocal-zeta source is expressed
as two reflected factors. The missing estimate remains difficult, but its
exact analytic interface is smaller.

## 3. Local first-edge chirality

T-108004 uses

\[
 z_n=4in+\lambda n^{1/3},
 \qquad
 t=\tau n^{1/3},
 \qquad
 \lambda>0,
\tag{3.1}
\]

and proves that the normalized symmetric kernel tends locally uniformly to

\[
 \mathcal C(\lambda,\tau)
 =\frac12\left
 \{\mathcal A(\lambda+2i\tau)
       +\mathcal A(\lambda-2i\tau)\right\}.
\tag{3.2}
\]

Here

\[
 \mathcal A(\zeta)
 =\frac{36\sqrt2}{\pi^3}e^{-i\pi/4}
 \int_0^\infty u^{-1/2}
 \exp\!\left(
 -\frac{\pi\zeta}{4}u+i\frac{\pi^3}{24}u^3
 \right)du,
 \qquad \Re\zeta>0.
\tag{3.3}
\]

Let

\[
 \mathcal P_n(\tau)=
 B_\beta(s_n-i\tau n^{1/3})
 B_\beta(s_n+i\tau n^{1/3}),
\tag{3.4}
\]

where

\[
 s_n=\frac12+2in+\frac\lambda2n^{1/3}.
\tag{3.5}
\]

Again \(\mathcal P_n(-\tau)=\mathcal P_n(\tau)\).

### Theorem T-108006B — local chiral reduction

For every symmetric finite \(\tau\)-window, and for every limiting integral
for which the relevant passage is justified,

\[
 \boxed{
 \int \mathcal C(\lambda,\tau)\mathcal P_n(\tau)\,d\tau
 =
 \int \mathcal D(\lambda,\tau)\mathcal P_n(\tau)\,d\tau,}
\tag{3.6}
\]

where the directed cusp is

\[
 \boxed{
 \mathcal D(\lambda,\tau)
 =\mathcal A(\lambda+2i\tau).}
\tag{3.7}
\]

The proof is the same reflection argument as in Section 1. The significance
is that the symmetric cosine carrier of T-108004 is not the final arithmetic
object. After assembly with the beta pair, one directed exponential survives.

## 4. Exact one-sided log-ratio carrier

Use the Fourier convention

\[
 f(\tau)=\frac1{2\pi}
 \int_{\mathbb R}\widehat f(v)e^{i\tau v}\,dv.
\tag{4.1}
\]

T-108004 gives the even density

\[
 H_\lambda(v)
 =\frac{72}{\pi^{5/2}}e^{-i\pi/4}|v|^{-1/2}
 e^{-\lambda|v|/2+i|v|^3/3}.
\tag{4.2}
\]

The directed profile (3.7) has the exact density

\[
 \boxed{
 H^{\leftarrow}_\lambda(v)
 =2H_\lambda(v)\mathbf 1_{v<0}.}
\tag{4.3}
\]

Equivalently,

\[
 \boxed{
 H^{\leftarrow}_\lambda(v)
 =
 \frac{144}{\pi^{5/2}}e^{-i\pi/4}|v|^{-1/2}
 e^{-\lambda|v|/2+i|v|^3/3}\mathbf 1_{v<0}.}
\tag{4.4}
\]

Indeed, in (3.3) put \(v=-\pi u/2\). Then

\[
 \mathcal D(\lambda,\tau)
 =\frac1{2\pi}
 \int_{-\infty}^{0}
 H^{\leftarrow}_\lambda(v)e^{i\tau v}\,dv.
\tag{4.5}
\]

The exact norm is

\[
 \boxed{
 \|H^{\leftarrow}_\lambda\|_1
 =\frac{144\sqrt2}{\pi^2\sqrt\lambda}.}
\tag{4.6}
\]

In the primitive-pair coordinate of T-108004,

\[
 v=n^{1/3}\log(m/n),
\tag{4.7}
\]

the support condition \(v<0\) is the directed half

\[
 \boxed{m<n.}
\tag{4.8}
\]

Thus beta-pair evenness permits an exact orientation of the local primitive
pair before taking an absolute value. The symmetric carrier is recovered by
averaging this orientation with its reflected copy.

This orientation does not by itself produce cancellation. It exposes which
half of the primitive-pair geometry must be estimated.

## 5. Exceptional prime 67 is an exact translate operator

The exceptional numerator in (0.1) contributes, at the local edge,

\[
 \begin{aligned}
 E_{67,n}(\tau)
 &=
 \left(1-67^{-s_n+i\tau n^{1/3}}\right)
 \left(1-67^{-s_n-i\tau n^{1/3}}\right)\\
 &=1-2q_n\cos(a_n\tau)+q_n^2,
 \end{aligned}
\tag{5.1}
\]

where

\[
 q_n=67^{-s_n},
 \qquad
 a_n=n^{1/3}\log67.
\tag{5.2}
\]

Multiplication by \(e^{\pm ia_n\tau}\) translates a Fourier density. Hence
the exact density after inserting the exceptional numerator is

\[
 \boxed{
 H^{(67)}_{\lambda,n}(v)
 =(1+q_n^2)H^{\leftarrow}_\lambda(v)
 -q_n\left
 \{H^{\leftarrow}_\lambda(v-a_n)
       +H^{\leftarrow}_\lambda(v+a_n)\right\}.}
\tag{5.3}
\]

No local Euler state has been discarded: the four states are assembled into
one original copy, two singly translated copies, and one doubly selected
copy.

For fixed \(\lambda>0\),

\[
 |q_n|=67^{-1/2-(\lambda/2)n^{1/3}},
\tag{5.4}
\]

so

\[
 \boxed{
 \|H^{(67)}_{\lambda,n}-H^{\leftarrow}_\lambda\|_1
 \le(2|q_n|+|q_n|^2)
 \|H^{\leftarrow}_\lambda\|_1.}
\tag{5.5}
\]

The exceptional channel therefore decouples exponentially on every fixed
positive-damping edge chart.

This statement must not be extrapolated to the physical boundary
\(\lambda=0\). There \(|q_n|=67^{-1/2}\), so the translated channels remain
macroscopic. The difficult undamped arithmetic problem is not removed.

## 6. Exact zero-frequency directed boundary constant

At \(z=4in\), T-108002 gives

\[
 n^{-1/3}\Phi_n(4i)\longrightarrow\mathcal A(0).
\tag{6.1}
\]

Since

\[
 \frac{J_r(4in)}{h_r^2}
 =4in\,\kappa_r\Phi_n(4i),
 \qquad
 \kappa_r\sim\frac{\pi^2}{72n^2},
\tag{6.2}
\]

one obtains

\[
 \boxed{
 n^{2/3}\frac{J_r(4in)}{h_r^2}
 \longrightarrow
 \frac{i\pi^2}{18}\mathcal A(0).}
\tag{6.3}
\]

Using the exact Gamma value from T-108002, the limit is

\[
 0.800335348364\ldots
 +1.386221486460\ldots i.
\tag{6.4}
\]

This is a zero-frequency boundary statement. It does not prove direct finite
convergence at \(\lambda=0\) for \(\tau\ne0\), where T-108004 already records
additional stationary points.

## 7. Replay

The bounded producer performs the following checks.

1. It builds a finite reciprocal-zeta/beta Dirichlet polynomial and verifies
   exact evenness of the assembled beta pair.
2. It checks the finite Chebyshev two-face sum against the one-directed-face
   sum on a symmetric frequency grid.
3. It checks the reflected vertical beta coordinates independently.
4. It checks the local symmetric-cusp pairing against the directed cusp on a
   symmetric \(\tau\)-grid.
5. It evaluates the one-sided inverse-Fourier formula at
   \(\lambda=2\), \(\tau=0,1,2\).
6. It replays the descending finite boundary errors for
   \(n=32,64,128,256,512\).
7. It verifies the exceptional numerator identity and the descending
   fixed-positive-\(\lambda\) translate bound.

The retained classification is

```text
PASS_T108006_BETA_CHEBYSHEV_CHIRAL_CUSP_SOURCE_CONVOLUTION
```

## 8. Consequence and next gate

The exact source pipeline is now

```text
symmetric finite Chebyshev Perron transform
  -> assemble B_beta(s-it) B_beta(s+it)
  -> beta-pair evenness
  -> one directed face J_r(z+2it)
  -> reflected vertical beta convolution
  -> one-sided cubic carrier on v<0
  -> exceptional-67 translated copies.
```

The next named gate is

```text
BETACHIRALCORR108008

On the undamped/vanishing-damping edge, prove a signed estimate for the
reflected vertical beta convolution against the one-sided carrier

  |v|^(-1/2) exp(i|v|^3/3) 1_(v<0),

with the two exceptional-67 translates retained. Pay the complete local tau
window and the outer-frequency tails before moving the Perron boundary.
```

What is proved:

| statement | status |
|---|---|
| exact beta-pair evenness | **PROVED** |
| two kernel faces reduce to one directed face in the source integral | **PROVED** |
| reflected vertical beta convolution | **PROVED** |
| local symmetric cusp reduces to one chirality in the source integral | **PROVED** |
| one-sided cubic log-ratio density and exact \(L^1\) norm | **PROVED** |
| exceptional-67 translate formula | **PROVED** |
| fixed-positive-\(\lambda\) exceptional decoupling | **PROVED** |

What is not proved:

| statement | status |
|---|---|
| direct \(\lambda=0,\tau\ne0\) finite boundary theorem | **OPEN** |
| signed reciprocal-zeta/beta correlation estimate | **OPEN** |
| complete local and outer-frequency contour estimate | **OPEN** |
| Perron boundary shift in an RH-bearing range | **OPEN** |
| new zeta zero-free region | **NOT PROVED** |
| RH | **UNPROVED** |
