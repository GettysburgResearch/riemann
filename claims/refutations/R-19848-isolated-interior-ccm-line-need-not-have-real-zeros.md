# R-19848 — An isolated simple even interior CCM eigenline need not have a real-zero transform

Claim ID: `R-19848`  
Status: **PROVED EXACT FINITE COUNTEREXAMPLE**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Scope: refutes the unconditional non-ground implication proposed in `M-19802`  
Nonclaim: this does not assert that RH is false

## 1. Statement

The implication

\[
\boxed{
\begin{array}{c}
A\text{ is a finite real parity-invariant CCM/Loewner matrix},\\
\xi\text{ is a simple isolated even eigenvector of }A
\end{array}
\Longrightarrow
\widehat\xi\text{ has only real zeros}
}
\tag{R-19848.1}
\]

is false.  It remains false when the target residual is exactly zero and the
two-sided singular moat on its orthogonal complement is equal to one.

Consequently spectral isolation, even perfect spectral isolation, cannot replace
the positive-kernel/ground hypothesis in the finite CCM real-zero theorem.

## 2. Exact CCM matrix

Use the three ordered scaling frequencies

\[
 d_{-1}=-1,\qquad d_0=0,\qquad d_1=1
\]

and put

\[
 A=
 \begin{pmatrix}
 0&1&1\\
 1&2&1\\
 1&1&0
 \end{pmatrix}.
\tag{R-19848.2}
\]

This is a real symmetric matrix commuting with the reflection
`-1 <-> 1`.

It lies in the exact finite CCM/Loewner class.  Indeed, take

\[
 b_{-1}=-1,\qquad b_0=0,\qquad b_1=1,
\]

and diagonal data

\[
 a_{-1}=0,\qquad a_0=2,\qquad a_1=0.
\]

Then, for `i != j`,

\[
 A_{ij}={b_i-b_j\over d_i-d_j},
 \qquad A_{ii}=a_i.
\tag{R-19848.3}
\]

Thus `A` has precisely the divided-difference commutator structure used in the
finite Caratheodory--Fejer/CCM theorem.  By the finite interpolation converse in
Connes--van Suijlekom, it is realized by a real distribution; this is not a
matrix outside the theorem's structural class.

## 3. Exact spectrum and parity

The three vectors

\[
 o=(1,0,-1)^T,
 \qquad
 \xi=(1,-1,1)^T,
 \qquad
 e=(1,2,1)^T
\]

satisfy

\[
 Ao=-o,
 \qquad
 A\xi=0,
 \qquad
 Ae=3e.
\tag{R-19848.4}
\]

Hence

\[
 \operatorname{spec}(A)=\{-1,0,3\}.
\tag{R-19848.5}
\]

The line `C xi` is even, simple, and strictly interior.  Moreover

\[
 \|(A-0I)w\|\ge \|w\|
 \qquad(w\perp\xi),
\tag{R-19848.6}
\]

because the singular values on `xi^perp` are `1` and `3`.  The candidate
residual is exactly

\[
 \|(A-0I)\xi\|=0.
\tag{R-19848.7}
\]

Thus the isolated-line ratio is `b/g=0` with `g=1`.

## 4. Exact nonreal zeros

For distinct real nodes `d_j`, the non-lattice numerator in the finite CCM
Fourier transform is, up to a nonzero real convention factor,

\[
 P_\xi(z)
 =\sum_{j=-1}^1 \xi_j
   \prod_{\substack{k=-1\\k\ne j}}^1(z-d_k).
\tag{R-19848.8}
\]

Substitution of `d=(-1,0,1)` and `xi=(1,-1,1)` gives

\[
\begin{aligned}
P_\xi(z)
&=(-z+z^2)+(1-z^2)+(z+z^2)\\
&=\boxed{z^2+1}.
\end{aligned}
\tag{R-19848.9}
\]

Therefore the transform has the nonreal conjugate zeros

\[
 \boxed{z= i,\qquad z=-i.}
\tag{R-19848.10}
\]

The remaining universal sine/lattice factor in the CCM formula has only real
zeros and cannot remove these two zeros.

This proves (R-19848.1) false.

## 5. Darboux-multiplier firewall

Let `F` be entire and let `Q` be an entire function whose zeros are all real.
Then every nonreal zero of `F` remains a zero of `QF`.  In particular,

\[
 F(\alpha)=0,\quad \alpha\notin\mathbb R
 \quad\Longrightarrow\quad
 (QF)(\alpha)=0.
\tag{R-19848.11}
\]

Hence a proposed groundification satisfying only

\[
 \widehat\xi^{\,D}(z)=Q(z)\widehat\xi(z),
 \qquad Q\text{ real-rooted},
\tag{R-19848.12}
\]

cannot repair a non-ground transform.  A genuine Darboux operation would have
to divide out/cancel zeros or mix several eigenlines.  To remain useful for RH,
it would then also have to prove that no hypothetical nonreal Xi zero is
cancelled.  That noncancellation is a separate conclusion-producing theorem.

## 6. Correct finite replacement

For a specified finite vector `xi`, the valid replacement is an independent
positive CCM completion:

\[
 \exists\ T\succeq0,
 \qquad \ker T=\mathbb C\xi,
 \qquad [D,T]\text{ has the CCM rank-two form}.
\tag{R-19848.13}
\]

The finite Caratheodory--Fejer theorem then gives real zeros.  But (R-19848.13)
is not a consequence of isolation in another Hermitian matrix `A`; the present
counterexample separates those statements exactly.  In the finite converse,
existence of such a positive completion is itself equivalent to the relevant
real-zero property.

## 7. Consequence for the three-obligation programme

The first and third obligations may establish that a finite line is isolated
and converges to Xi.  They do not imply the second obligation.  A complete
proposal must add one genuinely new positive CCM/Loewner completion for that
same line, or a rank-changing transform with a proved noncancellation theorem.
No ground-state wording may be removed while retaining its positivity content
silently.
