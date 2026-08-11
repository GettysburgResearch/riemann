# L-19871 — A one-sign coefficient vector has an explicit positive CCM completion and interlacing real zeros

Claim ID: `L-19871`  
Status: **PROVED EXACT FINITE NON-GROUND THEOREM**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: elementary weighted Cauchy--Schwarz and partial fractions  
Scope: an explicit finite CCM real-zero theorem which does not assume the vector is the ground line of a pre-existing indefinite matrix  
Nonclaim: the Xi-like residual vector is not proved to satisfy the one-sign hypothesis

## 1. Statement

Let

\[
 d_1<d_2<\cdots<d_n
 \tag{L-19871.1}
\]

be distinct real nodes, and let

\[
 \xi_j>0,
 \qquad
 \sum_{j=1}^n\xi_j=1.
 \tag{L-19871.2}
\]

Define

\[
 \boxed{
 Q_\xi=\operatorname{diag}(\xi_1^{-1},\ldots,\xi_n^{-1})
       -\mathbf1\mathbf1^{\mathsf T}.}
 \tag{L-19871.3}
\]

Then:

1. `Q_xi` is real symmetric positive semidefinite;
2. `ker Q_xi=R xi`;
3. `Q_xi` belongs to the exact CCM divided-difference class on the nodes
   `d_j`: for `i!=j`,
   \[
   (Q_\xi)_{ij}
   ={b_i-b_j\over d_i-d_j},
   \qquad b_j=-d_j,
   \tag{L-19871.4}
   \]
   while the diagonal entries are the allowed values `xi_j^{-1}-1`;
4. the polynomial
   \[
   P_\xi(s)
   =\sum_{j=1}^n\xi_j
     \prod_{k\ne j}(d_k-s)
   \tag{L-19871.5}
   \]
   has exactly one simple zero in each open interval `(d_j,d_(j+1))` and no
   other zero.

Consequently the finite Fourier transform associated with `xi` in the CCM
construction has only real zeros.  This conclusion does not require `xi` to be
the lowest eigenline of any pre-existing localized Weil matrix.

If the node set is symmetric and `xi_(-j)=xi_j`, then `Q_xi` is parity
invariant and `xi` is even.

## 2. Positivity and kernel

For every real or complex vector `x`, weighted Cauchy--Schwarz gives

\[
 \left|\sum_jx_j\right|^2
 =\left|\sum_j\sqrt{\xi_j}\,{x_j\over\sqrt{\xi_j}}\right|^2
 \le\left(\sum_j\xi_j\right)
     \left(\sum_j{|x_j|^2\over\xi_j}\right)
 =\sum_j{|x_j|^2\over\xi_j}.
 \tag{L-19871.6}
\]

Therefore

\[
 x^*Q_\xi x
 =\sum_j{|x_j|^2\over\xi_j}
  -\left|\sum_jx_j\right|^2
 \ge0.
 \tag{L-19871.7}
\]

Equality in (L-19871.6) holds exactly when

\[
 {x_j\over\sqrt{\xi_j}}=c\sqrt{\xi_j},
 \]

that is, when `x=c xi`.  Hence

\[
 \boxed{Q_\xi\succeq0,\qquad\ker Q_\xi=\mathbb C\xi.}
 \tag{L-19871.8}
\]

Directly,

\[
 Q_\xi\xi=\mathbf1-\mathbf1(\mathbf1^T\xi)=0.
 \tag{L-19871.9}
\]

## 3. Exact CCM structure

For `i!=j`, equation (L-19871.3) gives

\[
 (Q_\xi)_{ij}=-1.
 \tag{L-19871.10}
\]

Taking `b_j=-d_j`,

\[
 {b_i-b_j\over d_i-d_j}
 ={ -d_i+d_j\over d_i-d_j}
 =-1.
 \tag{L-19871.11}
\]

The CCM diagonal is independent data, so

\[
 a_j=(Q_\xi)_{jj}=\xi_j^{-1}-1
 \tag{L-19871.12}
\]

completes the exact matrix.  If `d_(-j)=-d_j` and `xi_(-j)=xi_j`, then
`b_(-j)=-b_j` and `a_(-j)=a_j`, which is precisely the parity condition.

## 4. Direct interlacing proof

Away from the nodes, divide (L-19871.5) by

\[
 \Pi(s)=\prod_{k=1}^n(d_k-s).
\]

One obtains

\[
 {P_\xi(s)\over\Pi(s)}
 =\sum_{j=1}^n{\xi_j\over d_j-s}
 =:R_\xi(s).
 \tag{L-19871.13}
\]

On every component of `R minus {d_1,...,d_n}`,

\[
 R_\xi'(s)
 =\sum_{j=1}^n{\xi_j\over(d_j-s)^2}>0.
 \tag{L-19871.14}
\]

For `d_j<s<d_(j+1)`,

\[
 \lim_{s\downarrow d_j}R_\xi(s)=-\infty,
 \qquad
 \lim_{s\uparrow d_{j+1}}R_\xi(s)=+\infty.
 \tag{L-19871.15}
\]

Strict monotonicity therefore gives exactly one simple zero in every open gap.
On `(-infinity,d_1)`, all denominators are positive, so `R_xi>0`; on
`(d_n,infinity)`, all denominators are negative, so `R_xi<0`.  There are no
exterior zeros.  Since `P_xi` has degree `n-1`, the `n-1` interlacing zeros are
all of its zeros.

## 5. Centered Fourier convention

For the centered interval `[-L/2,L/2]` with lattice nodes

\[
 d_k={2\pi k\over L},
 \tag{L-19871.16}
\]

a coefficient vector `a_k` becomes the CCM vector

\[
 \xi_k=(-1)^ka_k
 \tag{L-19871.17}
\]

after translation to `[0,L]`.  Therefore the finite centered transform has only
real zeros whenever the rephased coefficients

\[
 (-1)^ka_k
 \tag{L-19871.18}
\]

have one strict sign.  The half-interval translation contributes only the
zero-free factor `exp(-iLz/2)`.

## 6. Darboux sign correction

Let `F` be real on the real axis and let `M` be a real-rooted polynomial such
that

\[
 M(d_k)F(d_k)>0
 \tag{L-19871.19}
\]

on the selected finite lattice.  Translate the inverse transform of `MF` by
`L/2` and truncate to the selected Fourier modes.  Its CCM coefficient vector
is positive, so the resulting finite transform has only real zeros by the
present theorem.

This is a valid finite rank-changing/Darboux operation.  To use it in a limit,
one must still prove the relative approximation

\[
 {F_{L,N}(z)\over M(z)}\longrightarrow F(z)
 \tag{L-19871.20}
\]

locally uniformly on every compact set disjoint from the real roots of `M`.
Multiplication alone cannot remove a pre-existing nonreal zero; the content must
come from the relative finite approximation.

## 7. Proof boundary

- The positive completion, CCM structure, parity and interlacing are exact.
- This is a genuine non-ground finite theorem because no original indefinite
  matrix or lowest-eigenvalue hypothesis appears.
- It does not prove that the Xi residual line has one-sign rephased Fourier
  coefficients.
- A sign-correcting multiplier can force the finite hypothesis, but its growing
  relative approximation is a separate conclusion-producing theorem.
