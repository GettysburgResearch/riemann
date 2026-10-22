# L-14304 — Exact CCM-to-centered Hardy basis adapter

Claim ID: L-14304  
Title: Centering the CCM Fourier basis removes every support-coordinate and Hardy-Gram phase ambiguity  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: elementary Fourier algebra; CCM equations (2.6), (3.17), (3.21), and Proposition 5.9  
Scope: normalization adapter for T-14301, L-14302, and L-14303  
Related counterexample candidates: none

## Purpose

The source paper uses the interval `[0,L_CCM]`, where

\[
 L_{\rm CCM}=2\log\lambda,
\]

while the positive route naturally uses the centered logarithmic coordinate

\[
 t=\log u\in[-\ell,\ell],
 \qquad \ell=\log\lambda=L_{\rm CCM}/2.
\]

The two Fourier bases differ by a nontrivial sign phase. Forgetting that phase
changes the displayed sign pattern of both the direct and reciprocal Hardy
Toeplitz matrices. This lemma gives the exact conversion and checks the Mellin
transform convention.

## Statement

Let

\[
 U_n(x)=L_{\rm CCM}^{-1/2}
        \exp\!\left(\frac{2\pi i n x}{L_{\rm CCM}}\right),
 \qquad 0\leq x\leq L_{\rm CCM},
 \tag{L-14304.1}
\]

be the CCM basis and

\[
 V_n(u)=U_n(\log(\lambda u)),
 \qquad \lambda^{-1}\leq u\leq\lambda.
 \tag{L-14304.2}
\]

Let

\[
 \phi_n(t)=(2\ell)^{-1/2}
           \exp\!\left(\frac{i\pi n t}{\ell}\right),
 \qquad -\ell\leq t\leq\ell.
 \tag{L-14304.3}
\]

Then, under `u=e^t`,

\[
 \boxed{V_n(e^t)=(-1)^n\phi_n(t).}
 \tag{L-14304.4}
\]

Thus the coefficient vectors are related by the real orthogonal diagonal matrix

\[
 D=\operatorname{diag}((-1)^n)_{|n|\leq N},
 \qquad a=D\xi,
 \tag{L-14304.5}
\]

where `xi` denotes CCM coefficients and `a` centered coefficients.

### A. Parity

Multiplicative inversion acts by

\[
 V_n(u^{-1})=V_{-n}(u),
 \qquad
 \phi_n(-t)=\phi_{-n}(t).
 \tag{L-14304.6}
\]

Since `D_{-n}=D_n`, the sign adapter commutes with coefficient reversal.
Consequently the CCM and centered notions of even and odd vectors agree exactly.

### B. Mellin transform

For a finite vector

\[
 f(u)=\sum_{|n|\leq N}\xi_nV_n(u)
     =\sum_{|n|\leq N}a_n\phi_n(\log u),
 \tag{L-14304.7}
\]

extended by zero outside `[lambda^-1,lambda]`, the CCM Fourier--Mellin transform

\[
 \widehat f(z)=\int_0^\infty f(u)u^{-iz}\,d^*u
 \tag{L-14304.8}
\]

has the two identical representations

\[
 \boxed{
 \widehat f(z)
 =2(2\ell)^{-1/2}\sin(z\ell)
   \sum_{|n|\leq N}\frac{\xi_n}{z-\pi n/\ell}}
 \tag{L-14304.9}
\]

and

\[
 \boxed{
 \widehat f(z)
 =(2\ell)^{-1/2}
 \sum_{|n|\leq N}a_n
 \frac{2\sin((z-\pi n/\ell)\ell)}{z-\pi n/\ell}.}
 \tag{L-14304.10}
\]

The removable singularities have their limiting values. Formula
(L-14304.9) is exactly CCM Proposition 5.9 after substituting
`L_CCM=2 ell`.

### C. Direct Hardy Gram

For `0<tau<1/2`, put

\[
 W_\tau(t)=e^{2\tau t}+e^{-2\tau t}
          =2\cosh(2\tau t).
 \tag{L-14304.11}
\]

Using the convention antilinear in the first variable, define

\[
 G^{\rm cent}_{mn}
 =\langle\phi_m,W_\tau\phi_n\rangle,
 \qquad
 G^{\rm CCM}_{mn}
 =\langle V_m,W_\tau V_n\rangle.
 \tag{L-14304.12}
\]

Then

\[
 G^{\rm CCM}=DG^{\rm cent}D,
 \tag{L-14304.13}
\]

and, writing `d=n-m`,

\[
 \boxed{
 G^{\rm cent}_{mn}
 =(-1)^d
 \frac{4\tau\ell\sinh(2\tau\ell)}
      {4\tau^2\ell^2+\pi^2d^2},}
 \tag{L-14304.14}
\]

whereas the CCM-coordinate matrix has no alternating sign:

\[
 \boxed{
 G^{\rm CCM}_{mn}
 =\frac{4\tau\ell\sinh(2\tau\ell)}
       {4\tau^2\ell^2+\pi^2d^2}
 =\frac{2\tau L_{\rm CCM}\sinh(\tau L_{\rm CCM})}
       {\tau^2L_{\rm CCM}^2+\pi^2d^2}.}
 \tag{L-14304.15}
\]

Both matrices satisfy the exact Loewner floor

\[
 G^{\rm cent}\succeq2I,
 \qquad
 G^{\rm CCM}\succeq2I.
 \tag{L-14304.16}
\]

### D. Reciprocal Hardy Gram

Let

\[
 H^{\rm cent}_{mn}
 =\langle\phi_m,W_\tau^{-1}\phi_n\rangle,
 \qquad
 H^{\rm CCM}_{mn}
 =\langle V_m,W_\tau^{-1}V_n\rangle.
 \tag{L-14304.17}
\]

Again

\[
 H^{\rm CCM}=DH^{\rm cent}D.
 \tag{L-14304.18}
\]

The centered full-line approximation of L-14303 is

\[
 H^{\rm cent,\infty}_{mn}
 =\frac{\pi}{8\tau\ell}
  \operatorname{sech}\!\left(
    \frac{\pi^2d}{4\tau\ell}
  \right).
 \tag{L-14304.19}
\]

Hence the CCM-coordinate approximation carries the alternating phase

\[
 \boxed{
 H^{\rm CCM,\infty}_{mn}
 =(-1)^d\frac{\pi}{8\tau\ell}
  \operatorname{sech}\!\left(
    \frac{\pi^2d}{4\tau\ell}
  \right)
 =(-1)^d\frac{\pi}{4\tau L_{\rm CCM}}
  \operatorname{sech}\!\left(
    \frac{\pi^2d}{2\tau L_{\rm CCM}}
  \right).}
 \tag{L-14304.20}
\]

The finite-support entry error is unchanged by the phase:

\[
 \boxed{
 |H^{\rm CCM}_{mn}-H^{\rm CCM,\infty}_{mn}|
 \leq
 \frac{e^{-2\tau\ell}}{2\tau\ell}
 =\frac{e^{-\tau L_{\rm CCM}}}{\tau L_{\rm CCM}}.}
 \tag{L-14304.21}
\]

### E. Invariance of every finite certificate

Let `A_cent=D A_CCM D`, and transform every vector and finite basis by `D`.
Then:

1. Rayleigh values and ordinary residual norms are identical;
2. parity sectors and their dimensions are identical;
3. direct and reciprocal Hardy quadratic forms are identical;
4. generalized coercivity constants are identical;
5. Schur-complement dual-residual values are identical;
6. positive semidefiniteness, eigenvalues, and exact LDL pivot signs are
   preserved.

Therefore `T-14301`, `L-14301`, `L-14302`, and `L-14303` may be implemented in
either coordinate system, but matrices, vectors, and Gram kernels must all use
the same side of the adapter.

## Proof

Since `x=log(lambda u)=t+ell` and `L_CCM=2 ell`,

\[
 U_n(t+\ell)
 =(2\ell)^{-1/2}
  e^{i\pi n(t+\ell)/\ell}
 =(-1)^n\phi_n(t),
\]

which proves (L-14304.4)--(L-14304.5). Under inversion,
`x` is sent to `L_CCM-x`, proving (L-14304.6).

For the centered transform,

\[
 \int_{-\ell}^{\ell}
 \phi_n(t)e^{-izt}\,dt
 =(2\ell)^{-1/2}
  \frac{2\sin((z-\pi n/\ell)\ell)}{z-\pi n/\ell}.
\]

Because

\[
 \sin(z\ell-\pi n)=(-1)^n\sin(z\ell)
\]

and `a_n=(-1)^n xi_n`, summing gives (L-14304.9)--(L-14304.10).

The direct centered integral is

\[
 \frac1{2\ell}\int_{-\ell}^{\ell}
 2\cosh(2\tau t)e^{i\pi dt/\ell}\,dt,
\]

which is (L-14304.14). Conjugation by `D` contributes

\[
 (-1)^{m+n}(-1)^{n-m}=1,
\]

proving (L-14304.15). The pointwise inequality `W_tau>=2` proves
(L-14304.16).

The reciprocal relation follows from the same diagonal conjugation. Since
`(-1)^{m+n}=(-1)^{n-m}`, conjugating the positive centered full-line
coefficient produces (L-14304.20); absolute errors are unchanged, giving
(L-14304.21).

Finally, `D=D^*=D^{-1}` and it commutes with parity reversal. Every item in part
E follows by unitary similarity or by simultaneous transformation of the
relevant vectors and bases. QED.

## Inner-product convention audit

CCM uses inner products antilinear in the first variable. L-14303 explicitly
states the opposite convention for its abstract variational proof. The two
conventions transpose/conjugate coordinate matrices but do not alter any
Hermitian quadratic value, Loewner inequality, inverse-compression inequality,
or absolute-square correction. Equations (L-14304.12)--(L-14304.21) use CCM's
antilinear-first convention so that a production adapter can compare entries
directly.

## Gap audit

- `L_CCM` is the full interval length `2 log(lambda)`; `ell=log(lambda)` is the
  centered half-length. Confusing them changes every frequency by a factor two.
- The direct Hardy Gram alternates in the centered basis but not in the CCM
  basis. The reciprocal full-line approximation has the opposite phase pattern.
- Transforming a matrix without transforming its vector and Gram data is
  invalid even though each separate object looks plausible.
- The phase is real only because the shift is exactly half the interval.
- The formulas assume the CCM basis ordering indexed by the same integers
  `-N,...,N`; reordering requires a simultaneous permutation.
- The adapter proves normalization equivalence, not the imported CCM real-zero
  theorem or the asymptotic prolate approximation.

## Adversarial checks

1. At `n=1`, `V_1(e^0)=-phi_1(0)`; omitting the sign is immediately visible.
2. At `d=1`, the centered direct Gram entry is negative while the CCM direct
   Gram entry is positive.
3. At `d=1`, the centered reciprocal full-line coefficient is positive while
   the CCM coefficient is negative.
4. At `tau->0`, both direct matrices converge to `2I`.
5. Substituting `a_n=(-1)^n xi_n` into the centered transform reproduces CCM
   Proposition 5.9 term by term.
6. The inversion map sends both coefficient systems by `n -> -n` with no extra
   sign.

## Remaining uncertainty

The algebra above is exact and complete-looking but remains `PROPOSED` pending
an independent review. The cited paper equations must still be checked against
the exact version used by any production code. No production matrix or RH claim
is made here.
