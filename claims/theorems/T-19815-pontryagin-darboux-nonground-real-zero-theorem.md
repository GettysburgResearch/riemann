# T-19815 — Pontryagin–Darboux real-zero theorem for a non-ground CCM line

Claim ID: `T-19815`  
Status: **PROVED EXACT FINITE NON-GROUND THEOREM**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: the CCM determinant identity; finite-dimensional Pontryagin spectral theory; Paley--Wiener  
Scope: exact replacement for the false assertion that every isolated even interior CCM line is already real-rooted  
Nonclaim: the Darboux factors are not proved to escape on a cofinal Riemann-data sequence

## 1. Setup

Let `Q` be a real symmetric CCM divided-difference matrix on a finite Fourier
space `E_N`, and assume

\[
 \ker Q=\mathbb R\xi.
 \tag{T-19815.1}
\]

Normalize the evaluation vector `eta` by

\[
 \eta^{\mathsf T}\xi=1,
 \tag{T-19815.2}
\]

and define the CCM companion

\[
 T_\xi=\Lambda-|\Lambda\xi\rangle\langle\eta|.
 \tag{T-19815.3}
\]

The exact CCM commutator identity is

\[
 QT_\xi=T_\xi^{\mathsf T}Q.
 \tag{T-19815.4}
\]

Let

\[
 \kappa=n_-(Q)
 \tag{T-19815.5}
\]

be the number of negative squares after removing the one-dimensional kernel.
Let `F_xi(z)` be the finite Fourier transform of `xi`, including its universal
real lattice factor in the audited CCM convention.

## 2. Nonreal-zero count

The nonuniversal zeros of `F_xi` are the nonzero eigenvalues of the induced
companion on

\[
 \mathcal P=E_N/\mathbb R\xi.
 \tag{T-19815.6}
\]

The form induced by `Q` on `P` is nondegenerate and has negative index `kappa`.
Equation (T-19815.4) makes the induced companion self-adjoint in this
Pontryagin space.

Then

\[
 \boxed{
 \#\{z:F_\xi(z)=0,\ \operatorname{Im}z>0\}
 \le\kappa,}
 \tag{T-19815.7}
\]

counting algebraic multiplicity.  By reality, the same number occurs in the
lower half-plane.  Thus `F_xi` has at most `kappa` conjugate pairs of nonreal
nonuniversal zeros.

## 3. Proof of the index bound

Complexify `P` and let `M_+` be the direct sum of all generalized root spaces of
the companion whose eigenvalues lie in the open upper half-plane.

For generalized root vectors `x` at `lambda` and `y` at `mu`, the identity

\[
 [Tx,y]_Q=[x,Ty]_Q
 \tag{T-19815.8}
\]

implies

\[
 [p(T)x,y]_Q=[x,p(T)y]_Q
 \tag{T-19815.9}
\]

for every real polynomial `p`.  If `lambda` and `mu` both lie in the upper half
plane, then `lambda` is not equal to `conjugate(mu)`.  The minimal polynomials
of the two generalized root spaces are therefore coprime after conjugation.
A Bezout identity inserted into (T-19815.9) gives

\[
 [x,y]_Q=0.
 \tag{T-19815.10}
\]

Hence `M_+` is a neutral subspace.  In a Pontryagin space with negative index
`kappa`, every neutral subspace has dimension at most `kappa`: projection onto
the negative subspace is injective on a neutral subspace.  Therefore

\[
 \dim M_+\le\kappa,
 \tag{T-19815.11}
\]

which proves (T-19815.7), including algebraic multiplicity.

## 4. Exact Darboux division

Let the upper-half-plane nonuniversal zeros be

\[
 \alpha_1,\ldots,\alpha_r,
 \qquad r\le\kappa,
 \tag{T-19815.12}
\]

listed with algebraic multiplicity.  Define the real polynomial

\[
 B_\xi(z)
 =\prod_{j=1}^r(z-\alpha_j)(z-\overline{\alpha_j}).
 \tag{T-19815.13}
\]

Since every factor divides `F_xi`, the quotient

\[
 \boxed{
 F_\xi^{D}(z)={F_\xi(z)\over B_\xi(z)}
 }
 \tag{T-19815.14}
\]

is entire.  Every nonuniversal zero of `F_xi^D` is real; the universal lattice
zeros are real as well.  Thus

\[
 \boxed{F_\xi^D\text{ has only real zeros}.}
 \tag{T-19815.15}
\]

This is the finite non-ground Darboux theorem.  It does not replace the
interior line by a ground line and it does not assume `Q>=0`.

## 5. Support and parity

A finite Fourier transform is an entire function of exponential type `L/2` and
belongs to the Paley--Wiener class.  Division by a polynomial which divides the
function preserves exponential type and square integrability on the real axis.
Therefore `F_xi^D` is the Fourier transform of an `L2` source supported on the
same interval.

Equivalently, each division by `(z-alpha)` is the compact-support
zero-resolvent operation: because the numerator vanishes at `alpha`, the lower
and upper primitive formulas coincide and do not create an exterior tail.

If `xi` is even, the nonreal zeros occur in the appropriate reflected quartets.
The product `B_xi` may then be grouped into even real factors, and
`F_xi^D` remains even.

## 6. Exact limit criterion

Normalize

\[
 \widetilde B_j(z)={B_{\xi_j}(z)\over B_{\xi_j}(0)}
 \tag{T-19815.16}
\]

when zero is not one of the removed roots.  Suppose

\[
 F_{\xi_j}\longrightarrow \Xi
 \tag{T-19815.17}
\]

locally uniformly.  The Darboux transforms converge to the same limit if and
only if

\[
 \boxed{
 \widetilde B_j(z)\longrightarrow1
 }
 \tag{T-19815.18}
\]

locally uniformly.  A sufficient condition is

\[
 \sum_{\operatorname{Im}\alpha>0}
 {m_\alpha\over1+|\alpha|}
 \longrightarrow0,
 \tag{T-19815.19}
\]

because the logarithm of each normalized conjugate-pair factor is
`O_K((1+|alpha|)^-1)` on a fixed compact `K`.

Under (T-19815.18), every `F_xi_j^D` is real-rooted and converges locally
uniformly to `Xi`; Hurwitz then gives RH.

## 7. Necessity of factor escape

If `Xi` has a nonreal zero `rho`, local uniform convergence in (T-19815.17)
forces zeros of `F_xi_j` to remain near `rho`.  Those zeros must occur among the
Darboux factors.  Consequently (T-19815.18) cannot hold.

Thus, relative to a locally uniform Xi approximation,

\[
 \boxed{
 \text{Darboux-factor escape}
 \quad\Longleftrightarrow\quad
 \text{no persistent nonreal limit zero}.}
 \tag{T-19815.20}
\]

The finite theorem is unconditional; its cofinal factor-escape condition is the
remaining RH-bearing statement.

## 8. Relation to the other finite results

- `kappa=0` recovers the positive CCM theorem: no Darboux factor is needed.
- `R-19848` has `kappa=1` and exactly one conjugate pair `±i`; division by
  `z^2+1` leaves a constant real-rooted transform.
- `T-19814` characterizes the special case in which the Darboux polynomial is
  trivial.
- `L-19869` replaces exact division by an approximate positive symmetrizer and
  confines the factors to a shrinking strip.

## 9. Proof boundary

- The negative-index count and Darboux real-zero conclusion are exact.
- No lowest-eigenvalue or ground-state hypothesis is used.
- The construction uses the finite nonreal roots, so it is not by itself a
  prime-side proof mechanism.
- To complete the Riemann proposal one must prove factor escape, or construct
  the equivalent source-bound approximate symmetrizer of `L-19869`.
