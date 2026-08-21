# T-19815 — Pontryagin–Darboux real-zero theorem for a non-ground CCM line

Claim ID: `T-19815`  
Status: **PROVED EXACT FINITE NON-GROUND THEOREM**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: the CCM determinant identity; finite-dimensional Pontryagin spectral theory; Paley--Wiener  
Scope: exact replacement for the false assertion that every isolated even interior CCM line is already real-rooted  
Nonclaim: the total vertical Darboux defect is not proved to vanish on a cofinal Riemann-data sequence

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

implies the corresponding polynomial identity.  If `lambda` and `mu` both lie
in the upper half-plane, then `lambda` is not equal to `conjugate(mu)`.  The
minimal polynomials of the two generalized root spaces are therefore coprime
after conjugation.  A Bezout identity gives

\[
 [x,y]_Q=0.
 \tag{T-19815.9}
\]

Hence `M_+` is a neutral subspace.  In a Pontryagin space with negative index
`kappa`, every neutral subspace has dimension at most `kappa`: projection onto
the negative subspace is injective on a neutral subspace.  Therefore

\[
 \dim M_+\le\kappa,
 \tag{T-19815.10}
\]

which proves (T-19815.7), including algebraic multiplicity.

## 4. Darboux deletion

Let the upper-half-plane nonuniversal zeros be

\[
 \alpha_1,\ldots,\alpha_r,
 \qquad r\le\kappa,
 \tag{T-19815.11}
\]

listed with algebraic multiplicity.  Define

\[
 B_\xi(z)
 =\prod_{j=1}^r(z-\alpha_j)(z-\overline{\alpha_j}).
 \tag{T-19815.12}
\]

Since every factor divides `F_xi`, the quotient

\[
 F_\xi^{\rm del}(z)={F_\xi(z)\over B_\xi(z)}
 \tag{T-19815.13}
\]

is entire and has only real zeros.  This is the deletion version of the finite
non-ground Darboux theorem.

## 5. Darboux vertical flattening

Write

\[
 \alpha_j=a_j+ib_j,
 \qquad b_j>0.
 \tag{T-19815.14}
\]

Instead of deleting the conjugate pair, move it vertically to the real axis:

\[
 \boxed{
 F_\xi^{\flat}(z)
 =F_\xi(z)
  \prod_{j=1}^r
  { (z-a_j)^2
   \over
    (z-\alpha_j)(z-\overline{\alpha_j})}.}
 \tag{T-19815.15}
\]

The denominator divides `F_xi`, so `F_xi^flat` is entire.  Every removed pair is
replaced by a double real zero at `a_j`; all other zeros are already real.
Therefore

\[
 \boxed{F_\xi^{\flat}\text{ has only real zeros}.}
 \tag{T-19815.16}
\]

No ground-state hypothesis has been introduced.

## 6. Support, norm and parity

A finite Fourier transform is an entire function of exponential type `L/2` in
the Paley--Wiener class.  Polynomial division by an actual zero factor preserves
exponential type.  On the real axis,

\[
 \left|
 { (x-a_j)^2
  \over (x-a_j)^2+b_j^2}
 \right|\le1.
 \tag{T-19815.17}
\]

Hence

\[
 \|F_\xi^{\flat}\|_{L^2(\mathbb R)}
 \le\|F_\xi\|_{L^2(\mathbb R)}.
 \tag{T-19815.18}
\]

Paley--Wiener therefore gives an `L2` inverse transform supported on the same
interval.  Equivalently, each division is the compact-support zero-resolvent
operation; the inserted real factor is a local differential operator.

If `xi` is even, group the nonreal roots in reflected quartets.  The complete
flattening factor is then even and `F_xi^flat` remains even.

## 7. Stable off-axis limit criterion

Let `F_j` be real finite transforms converging locally uniformly to `Xi`, and
let `b_(j,l)>0` be the imaginary parts of their upper-half-plane nonreal roots.
Assume

\[
 \boxed{
 V_j:=\sum_l b_{j,l}^2\longrightarrow0.}
 \tag{T-19815.19}
\]

For a compact set `K` at distance `delta>0` from the real axis, eventually every
`b_(j,l)<delta/2`.  The individual flattening factor satisfies uniformly on
`K`

\[
 \left|
 { (z-a)^2
  \over (z-a)^2+b^2}-1
 \right|
 \le {4b^2\over\delta^2}.
 \tag{T-19815.20}
\]

The product estimate and (T-19815.19) give

\[
 \prod_l{(z-a_{j,l})^2
          \over(z-a_{j,l})^2+b_{j,l}^2}
 \longrightarrow1
 \tag{T-19815.21}
\]

uniformly on `K`.  Consequently

\[
 F_j^{\flat}\longrightarrow\Xi
 \tag{T-19815.22}
\]

locally uniformly on every compact subset of `C minus R`.

Every `F_j^flat` has only real zeros.  If `Xi` had one nonreal zero, choose a
small disk around it disjoint from the real axis; Hurwitz applied on that disk
would give a contradiction.  Therefore

\[
 \boxed{V_j\to0\quad\Longrightarrow\quad RH.}
 \tag{T-19815.23}
\]

## 8. Relation to approximate symmetrizers

`L-19869` shows that an operator-norm commutator defect `epsilon_j` places every
nonreal root in `|Im z|<=epsilon_j`.  If `d_j` is the degree of the nonuniversal
polynomial, then

\[
 V_j\le d_j\epsilon_j^2.
 \tag{T-19815.24}
\]

Thus the quantitative condition

\[
 \boxed{d_j\epsilon_j^2\longrightarrow0}
 \tag{T-19815.25}
\]

is sufficient for the exact vertically flattened Darboux transforms to converge
off the real axis to `Xi` and prove RH.

A Hilbert--Schmidt commutator estimate can replace (T-19815.25) directly,
because the sum of squared imaginary parts of the spectrum is bounded by the
squared Hilbert--Schmidt norm of the skew-adjoint part in the symmetrized
metric.

## 9. Necessity of vertical control

If `Xi` has a nonreal zero `rho`, local uniform convergence forces a zero of
`F_j` to remain near `rho`.  Therefore

\[
 \liminf_j V_j\ge |\operatorname{Im}\rho|^2>0.
 \tag{T-19815.26}
\]

So the vertical-defect condition is genuinely conclusion producing; it cannot
follow from finite isolation alone.

## 10. Relation to the other finite results

- `kappa=0` recovers the positive CCM theorem: no Darboux operation is needed.
- `R-19848` has `kappa=1` and one pair `±i`; deletion leaves a constant, while
  vertical flattening replaces `z^2+1` by `z^2`.
- `T-19814` characterizes the special case in which the Darboux polynomial is
  trivial.
- `L-19869` is the approximate metric route to (T-19815.25).

## 11. Proof boundary

- The negative-index count, compact-support Darboux deletion and vertical
  flattening are exact.
- No lowest-eigenvalue or ground-state hypothesis is used.
- The construction uses the finite nonreal roots and therefore is not by itself
  a prime-side proof mechanism.
- The remaining theorem is a source-bound total vertical-defect estimate such as
  `V_j->0`, or the stronger anisotropic commutator estimate of `L-19869` with
  rate (T-19815.25).
