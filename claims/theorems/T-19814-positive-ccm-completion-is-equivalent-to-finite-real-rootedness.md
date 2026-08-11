# T-19814 — Positive CCM completion is equivalent to diagonalizable finite real-rootedness

Claim ID: `T-19814`  
Status: **PROVED EXACT FINITE CHARACTERIZATION**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: the CCM determinant identity; elementary finite-dimensional spectral theory  
Scope: exact boundary of every proposed non-ground positive-completion theorem  
Nonclaim: no source-bound completion is constructed for the Xi-like target

## 1. Setup

Let

\[
 \Lambda=\operatorname{diag}(d_1,\ldots,d_n),
 \qquad d_j\in\mathbb R
 \tag{T-19814.1}
\]

with distinct nodes.  Let `xi in C^n` and let `eta in C^n` satisfy

\[
 \eta^*\xi=1.
 \tag{T-19814.2}
\]

Define the rank-one CCM companion

\[
 T_\xi
 =\Lambda-|\Lambda\xi\rangle\langle\eta|.
 \tag{T-19814.3}
\]

Then `T_xi xi=0`.  The CCM determinant identity identifies the nonzero
spectrum of `T_xi` with the nonuniversal zeros of the finite Fourier transform
associated with `xi`.

## 2. Characterization theorem

The following are equivalent.

### (A) Real diagonalizable finite spectrum

The operator induced by `T_xi` on

\[
 \mathbb C^n/\mathbb C\xi
 \tag{T-19814.4}
\]

is diagonalizable and has only real eigenvalues.

### (B) Positive exact symmetrizer

There exists a Hermitian positive semidefinite matrix `Q` such that

\[
 \ker Q=\mathbb C\xi
 \tag{T-19814.5}
\]

and

\[
 \boxed{QT_\xi=T_\xi^*Q.}
 \tag{T-19814.6}
\]

### (C) Positive CCM divided-difference completion

There exists a Hermitian positive semidefinite matrix `Q`, with kernel
`C xi`, whose off-diagonal entries obey

\[
 \boxed{
 (d_j-d_i)Q_{ij}
 =u_i\overline{\eta_j}
  -\eta_i\overline{u_j},
 \qquad i\ne j,
 }
 \tag{T-19814.7}
\]

for one vector `u`.  When `eta=mathbf1` and all data are real, this is exactly

\[
 Q_{ij}={b_i-b_j\over d_i-d_j}
 \tag{T-19814.8}
\]

with `b=-u`, while the diagonal entries are free.

Consequently, in the generic simple-root case,

\[
 \boxed{
 \text{positive CCM completion of }\xi
 \quad\Longleftrightarrow\quad
 \text{all nonuniversal transform zeros are real}.}
 \tag{T-19814.9}
\]

Thus an exact positive completion for an arbitrary isolated interior line is
not a consequence of isolation; it is an equivalent formulation of the finite
real-zero conclusion.

## 3. Proof that (B) implies (A)

The form induced by `Q` on the quotient (T-19814.4) is positive definite.
Equation (T-19814.6) says that the induced companion is self-adjoint in this
Hilbert metric.  Every finite-dimensional self-adjoint operator is
diagonalizable with real spectrum.  This proves (A).

The CCM determinant identity then puts every nonuniversal finite-transform zero
on the real axis.

## 4. Proof that (A) implies (B)

Let `bar T` denote the induced quotient operator.  By (A), choose an invertible
matrix `V` on the quotient and a real diagonal matrix `R` such that

\[
 \bar T=VRV^{-1}.
 \tag{T-19814.10}
\]

Define the positive quotient metric

\[
 \bar Q=(V^{-1})^*V^{-1}.
 \tag{T-19814.11}
\]

Then

\[
 \bar Q\bar T=\bar T^*\bar Q.
 \tag{T-19814.12}
\]

Lift `bar Q` to `C^n` by declaring `xi` orthogonal to the quotient and null.
The resulting Hermitian matrix `Q` satisfies

\[
 Q\succeq0,
 \qquad\ker Q=\mathbb C\xi,
 \qquad QT_\xi=T_\xi^*Q.
 \tag{T-19814.13}
\]

This proves (B).

The construction is independent of a lowest-eigenvalue ordering.  It uses the
real spectrum itself.

## 5. Equivalence of (B) and (C)

Put

\[
 u=Q\Lambda\xi.
 \tag{T-19814.14}
\]

Since `Qxi=0`, expanding (T-19814.6) gives

\[
 Q\Lambda-\Lambda Q
 =|u\rangle\langle\eta|
  -|\eta\rangle\langle u|.
 \tag{T-19814.15}
\]

Taking the `(i,j)` entry for `i!=j` gives exactly
(T-19814.7).  Thus (B) implies (C).

Conversely, (T-19814.7), together with freely chosen diagonal entries, is
precisely the off-diagonal content of (T-19814.15).  If `Qxi=0`, its diagonal
part follows as well: both sides of

\[
 E=Q\Lambda-\Lambda Q-|u\rangle\langle\eta|
   +|\eta\rangle\langle u|
 \tag{T-19814.16}
\]

are skew-Hermitian, `E` has zero off-diagonal entries, and a skew-Hermitian
diagonal with real CCM data is zero.  Hence (T-19814.15) and (B) hold.

For `eta=mathbf1` and real data, setting `b_i=-u_i` rewrites
(T-19814.7) as (T-19814.8).

## 6. Repeated roots and closure

If the quotient companion has a nontrivial Jordan block at a real eigenvalue,
no positive definite quotient metric can make it self-adjoint.  Thus exact
positive completion corresponds to real **semisimple** spectrum.  For the
cyclic generic CCM companion this is the simple-root case.

Nonsimple real-rooted limits are obtained by closure from simple interlacing
vectors, but an exact singular finite level requires a separate semisimplicity
check.

## 7. Consequences

1. `R-19848` violates (A), so `R-19849` must have an empty positive completion
   cone.
2. `L-19871` constructs `Q` directly under the one-sign hypothesis, and hence
   proves (A) without inspecting roots.
3. `L-19869` is the stable approximate form of the present theorem: a small
   commutator defect confines the spectrum to a thin real strip.
4. `L-19870` shows that optimizing over all positive metrics simply recovers the
   spectral strip width.

Therefore the only conclusion-producing version of obligation 2 is to
construct `Q` from arithmetic/source data independently of the finite roots.
An unrestricted spectral construction of `Q` is logically equivalent to the
answer.

## 8. Proof boundary

- The equivalence is exact finite-dimensional algebra.
- It does not impose or recover a ground-state hypothesis for the original
  localized Weil matrix.
- It proves that a generic non-ground positive-completion theorem cannot be
  cheaper than finite real-rootedness.
- The source-bound anisotropic completion/commutator estimate remains open.
