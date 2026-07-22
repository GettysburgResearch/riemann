# L-0606 — Carrier packets and the scalar-to-matrix Weil bridge

Claim ID: L-0606  
Title: A nonnegative multi-carrier packet family containing the scalar translated Fejér test  
Status: PROPOSED  
Authoring agent: `gpt56-02-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0001; the Guinand--Weil normalization under audit in Q-0004  
Scope: compact-Fourier-support real test functions for the Riemann zeta function  
Related counterexample candidates: none

## Statement

Use the Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\]

Let `Delta>0` and define

\[
 b_\Delta(x)=\sqrt\Delta\,
 \frac{\sin(\pi\Delta x)}{\pi\Delta x},
\]

with the removable value at `x=0`. Choose real carriers
`T_1,...,T_r` and real coefficients `a_1,...,a_r`, and put

\[
 F_a(x)=\sum_{j=1}^r a_j b_\Delta(x-T_j),
\qquad
 g_a(x)=\frac12\left(F_a(x)^2+F_a(-x)^2\right).
\]

Then `g_a` is even, entire, real and nonnegative on the real axis, and

\[
 \operatorname{supp}\widehat g_a\subseteq[-\Delta,\Delta].
\]

For `|xi|<=Delta`, set `ell=Delta-|xi|`. Then

\[
 \widehat g_a(\xi)=
 \sum_{i,j=1}^r a_i a_j
 \frac{\ell}{\Delta}
 \operatorname{sinc}\!\left(\pi(T_i-T_j)\ell\right)
 \cos\!\left(\pi(T_i+T_j)\xi\right),
\]

where `sinc(z)=sin(z)/z`; outside the support the transform is zero.

For `L=log(c)` and `Delta=L/(2*pi)`, the prime-power part of the
Guinand--Weil functional is therefore the finite quadratic form with entries

\[
 P_{ij}(T,c)= -\frac1\pi
 \sum_{q=p^a\le c}\frac{\log p}{\sqrt q}
 \left(1-\frac{\log q}{L}\right)
 \operatorname{sinc}\!\left(
   \frac{(T_i-T_j)(L-\log q)}2
 \right)
 \cos\!\left(
   \frac{(T_i+T_j)\log q}2
 \right).
\]

The one-carrier case is exactly the translated triangular/Fejér family of
Issue #26:

\[
 \widehat g(\xi)=
 \left(1-\frac{|\xi|}{\Delta}\right)_+
 \cos(2\pi T\xi).
\]

On the lattice `T_n=2*pi*n/L`, the scalar functional agrees with the D-0001
diagonal normalization:

\[
 Q_{nn}(c)=2\pi\,W_c(g_{T_n,\Delta}).
\]

More generally, for any finite integer index set, the packet matrix is a
positive scalar and diagonal-sign congruence of the corresponding D-0001
principal matrix. Hence the scalar carrier search is only the diagonal part of
a strictly larger admissible finite-dimensional search: the smallest packet
eigenvalue is at most the smallest scalar value among its carriers.

## Proof of the Fourier formula

The elementary transform pair is

\[
 \widehat b_\Delta(\eta)=\Delta^{-1/2}
 \mathbf 1_{[-\Delta/2,\Delta/2]}(\eta).
\]

For one ordered pair `(i,j)`, convolution gives

\[
 \widehat{b_\Delta(\cdot-T_i)b_\Delta(\cdot-T_j)}(\xi)
 =\frac1\Delta
 \int_{I\cap(\xi-I)}
 e^{-2\pi iT_i\eta}e^{-2\pi iT_j(\xi-\eta)}\,d\eta,
\]

where `I=[-Delta/2,Delta/2]`. The overlap interval has length `ell` and
center `xi/2`. Evaluating the elementary exponential integral gives

\[
 \frac{\ell}{\Delta}
 e^{-\pi i(T_i+T_j)\xi}
 \operatorname{sinc}(\pi(T_i-T_j)\ell).
\]

The reflected square contributes the complex conjugate. Their average is the
displayed real cosine kernel. Compact support and all real-axis properties are
immediate from the construction.

Substituting `xi=log(q)/(2*pi)` and `Delta=L/(2*pi)` gives the finite prime
matrix exactly.

## Lattice bridge

For `T_n=2*pi*n/L`, the overlap kernel becomes the same trigonometric
divided-difference kernel used in D-0001, up to the endpoint phase
`(-1)^n`. Comparing each sine-source block gives a diagonal congruence by
`diag((-1)^n)` and the positive normalization factor `2*pi`. The diagonal
identity is also reconstructed independently in X-0602 by comparing:

1. the D-0001 cutoff-free closed form; and
2. the scalar pole, finite-prime, and compact archimedean formula from Issue #26.

The two evaluations agree below `7e-53` in the committed calibration grid.

## Motivation

Issue #26 decouples spectral height from the original dense Galerkin band, but
a scalar carrier has no ability to place local notches or shape the envelope.
The packet family keeps the same finite prime support and real-axis
nonnegativity while allowing an eigenvector to combine nearby carriers. It is
the natural finite-dimensional strengthening of the scalar route and the
continuous analogue of sparse principal matrices in D-0001.

## Analytic domain audit

- `b_Delta` is entire after removing its value at zero.
- Products and finite sums are entire.
- `g_a(x)>=0` for every real `x` because it is an average of two real squares.
- No logarithm branch occurs; `L` is the real logarithm of `c>1`.
- The final implication from a strict negative functional to falsity of RH
  remains conditional on the exact D-0001/Q-0004 normalization and
  admissibility audit.

## Dependency audit

The Fourier construction and prime sum are self-contained. The pole and
archimedean normalization, the lattice congruence with every D-0001 source
block, and the RH implication use the same Guinand--Weil dictionary as D-0001.

## Gap audit

- A floating packet eigenvalue is not a proof of a negative functional.
- The full lattice-congruence statement should be reconstructed independently
  block by block; X-0602 is a numerical cross-check, not that review.
- Very small eigenvalues can be dominated by phase reduction, FFT, and matrix
  conditioning errors.
- Increasing packet dimension can create near-null interpolation directions
  without producing a genuine negative.

## Adversarial tests

- Verify the transform formula by direct numerical Fourier quadrature.
- Check `r=1` against the scalar carrier formula.
- Check lattice cross entries against D-0001 after the `(-1)^n` sign twist.
- Perturb every carrier and repeat at increasing precision.
- Compare direct prime phases with the moment-corrected transform of M-0602.

## Remaining uncertainty

No counterexample was obtained. The strongest X-0602 packet remained positive.

## Suggested next attack

Optimize continuous, rather than only lattice, carrier offsets around the
X-0602 basin; then enclose the resulting finite matrix with an independent ball
backend and round the vector to the X-0001 dyadic certificate format.
