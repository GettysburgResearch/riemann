# L-3601 — Exact continuous off-lattice sinc-carrier block

Claim ID: L-3601  
Title: Exact Gram, prime, pole, and compact archimedean matrices for arbitrary real sinc carriers  
Status: PROPOSED  
Authoring agent: `gpt56-04-d`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: L-0606; the D-0001/T-2801 Guinand--Weil normalization  
Scope: finite real packets of translated normalized sinc functions  
Related counterexample candidates: none

## Statement

Use

\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx,
 \qquad
 f(z)=\int_{\mathbb R}\widehat f(\xi)e^{2\pi i z\xi}\,d\xi.
\]

Let `Delta>0`, put

\[
 b_\Delta(z)=\sqrt\Delta\,\frac{\sin(\pi\Delta z)}{\pi\Delta z},
 \qquad
 I=[-\Delta/2,\Delta/2],
\]

and choose arbitrary real carriers `T_1,...,T_r`. For a real vector `a`, define

\[
 F_a(z)=\sum_{j=1}^r a_jb_\Delta(z-T_j),
 \qquad
 g_a(z)=\frac12\{F_a(z)^2+F_a(-z)^2\}.
\]

Then `g_a` is even and entire, is nonnegative on the real axis, and has Fourier
support in `[-Delta,Delta]`.

Put

\[
 \delta_{ij}=T_i-T_j,
 \qquad
 \sigma_{ij}=T_i+T_j.
\]

The exact coefficient Gram matrix is

\[
 \boxed{
 G_{ij}=\int_{\mathbb R}b_\Delta(x-T_i)b_\Delta(x-T_j)\,dx
 =\operatorname{sinc}(\pi\Delta\delta_{ij}),}
\]

where `sinc(z)=sin(z)/z`.

For `|xi|<=Delta`, put `ell=Delta-|xi|`. The exact packet Fourier kernel is

\[
 \boxed{
 H_{ij}(\xi)=
 \frac\ell\Delta
 \operatorname{sinc}(\pi\delta_{ij}\ell)
 \cos(\pi\sigma_{ij}\xi),}
\]

and it is zero outside the support. Thus

\[
 \widehat g_a(\xi)=a^{\mathsf T}H(\xi)a.
\]

For `L=log(c)` and `Delta=L/(2*pi)`, the complete finite prime block is

\[
 \boxed{
 (P_c)_{ij}=-\frac1\pi
 \sum_{q=p^m\le c}\frac{\log p}{\sqrt q}
 \left(1-\frac{\log q}{L}\right)
 \operatorname{sinc}\!\left(
  \frac{\delta_{ij}(L-\log q)}2
 \right)
 \cos\!\left(\frac{\sigma_{ij}\log q}{2}\right).}
\]

The exact pole block is

\[
 \boxed{
 R_{ij}=2\operatorname{Re}\left[
 b_\Delta(i/2-T_i)b_\Delta(i/2-T_j)
 \right].}
\]

Let

\[
 k(t)=\frac{e^{-t/4}}{1-e^{-t}}.
\]

The cutoff-free archimedean block is the compact integral

\[
 \boxed{
 A_{ij}=\frac1{2\pi}\left[
 \int_0^{2L}\left(
 \frac{e^{-t}G_{ij}}t-k(t)B_{ij}(t)\right)dt
 +G_{ij}E_1(2L)-G_{ij}\log\pi
 \right],}
\]

where the apparent singularity is interpreted only in the combined removable
expression and

\[
 \boxed{
 B_{ij}(t)=
 \left(1-\frac{t}{2L}\right)
 \operatorname{sinc}\!\left(\frac{\delta_{ij}(2L-t)}4\right)
 \cos\!\left(\frac{\sigma_{ij}t}4\right).}
\]

Subject to the shared normalization, the exact packet matrix is

\[
 Q=A+R+P_c.
\]

A strict negative fixed-vector enclosure for `a^T Q a` would therefore be a
finite RH-disproof witness.

## Proof

The elementary transform pair is

\[
 \widehat b_\Delta(\eta)=\Delta^{-1/2}\mathbf1_I(\eta).
\]

Translation by `T_i` multiplies this box by `e^{-2*pi*i*T_i*eta}`. Parseval
immediately gives the Gram matrix.

For one ordered product, convolution gives

\[
 \widehat{b_\Delta(\cdot-T_i)b_\Delta(\cdot-T_j)}(\xi)
 =\frac1\Delta\int_{I\cap(\xi-I)}
 e^{-2\pi iT_i\eta}e^{-2\pi iT_j(\xi-\eta)}\,d\eta.
\]

The overlap interval has length `ell` and midpoint `xi/2`. Its elementary
exponential integral is

\[
 \frac\ell\Delta
 e^{-\pi i\sigma_{ij}\xi}
 \operatorname{sinc}(\pi\delta_{ij}\ell).
\]

The reflected square contributes its conjugate. Averaging gives `H_ij`.
Substitution at `xi=log(q)/(2*pi)` gives the prime block exactly.

For the pole term, evaluate `2g_a(i/2)`. Since `b_Delta` has real Taylor
coefficients and is even,

\[
 b_\Delta(i/2+T)=\overline{b_\Delta(i/2-T)}
\]

for real `T`, giving the displayed real-part formula.

For the archimedean term use, with the singular terms regularized together,

\[
 \operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi
 =\int_0^\infty\left(
 \frac{e^{-t}}t-k(t)\cos(rt/2)
 \right)dt-\log\pi.
\]

Parseval gives

\[
 \int_{\mathbb R}b_\Delta(r-T_i)b_\Delta(r-T_j)\,dr=G_{ij}
\]

and

\[
 \int_{\mathbb R}b_\Delta(r-T_i)b_\Delta(r-T_j)
 \cos(rt/2)\,dr=B_{ij}(t)
\]

for `0<=t<=2L`, while compact Fourier support makes the latter zero afterward.
The remaining first-term tail is `G_ij E1(2L)`. This proves the compact formula.

## Three mandatory reductions

### Scalar diagonal

When `i=j`,

\[
 G_{ii}=1,
 \qquad
 B_{ii}(t)=\left(1-\frac t{2L}\right)\cos(T_it/2),
\]

and the prime kernel is

\[
 \left(1-\frac{\log q}{L}\right)\cos(T_i\log q).
\]

This is exactly the translated Fejer family of Issue #26.

### Integer lattice

Write

\[
 T_i=\frac{2\pi n_i}{L},\qquad T_j=\frac{2\pi n_j}{L}.
\]

At a normalized prime position `u=log(q)/L`, the correct kernel is

\[
 (1-u)\operatorname{sinc}(\pi(n_i-n_j)(1-u))
 \cos(\pi(n_i+n_j)u).
\]

For integer indices this equals

\[
 \frac{(-1)^{n_i-n_j}}{2\pi(n_i-n_j)}
 \{\sin(2\pi n_j u)-\sin(2\pi n_i u)\},
\]

with the diagonal interpreted by continuity. This is the exact sign congruence
with the D-0001 divided-difference block.

### Fractional adversary

For noninteger `n_i,n_j`, the endpoint phase `pi*(n_i-n_j)` does not collapse to
a sign. Replacing the correct kernel by the same divided difference with real
indices drops these endpoint phases and is generally wrong by order one. Thus
no continuous implementation may substitute real indices into the lattice
closed forms.

## Gram and conditioning audit

The translated sinc functions are not orthogonal off the lattice. Discovery
must solve the generalized eigenproblem against `G`, or freeze a concrete vector
and evaluate its unnormalized exact quadratic form. Near-coincident carriers make
`G` ill-conditioned; an ordinary Euclidean eigenvalue can then manufacture a
negative along a nearly null coefficient direction.

L-3602 supplies an orthonormal confluent basis that removes this failure mode.

## Analytic domain audit

- Every test function is entire of exponential type at most `L`.
- Products decay as `O(|Re z|^-2)` on fixed horizontal strips.
- The zero sum is absolutely convergent in the T-2801 admissible class.
- The prime side is exactly finite because `H_ij` vanishes outside the support.
- All logarithms are real logarithms of positive quantities.
- The combined archimedean integrand, not its two singular pieces, is evaluated at zero.

## Gap audit

1. The Guinand--Weil source signs remain tied to the T-2801 review gate.
2. Ordinary quadrature or eigensolving is not a sign certificate.
3. Near-coincident carriers require a generalized Gram treatment.
4. The full continuous search is nonlinear in the carrier locations.
5. A negative midpoint must be frozen to exact coefficients and reevaluated with balls.

## Suggested next attack

Use the L-3602 confluent hierarchy for stable local carrier geometry, and use
small separated clusters only when the coefficient tail proves that one local
confluent center is insufficient.
