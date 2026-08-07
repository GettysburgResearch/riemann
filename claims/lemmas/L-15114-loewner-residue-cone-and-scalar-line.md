# L-15114 — The special-completion cone is a Cauchy-residue orthant, and the arithmetic completion is a line

Claim ID: `L-15114`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15109`; elementary partial fractions and Cauchy determinants  
Scope: simple real target roots and the exact target-pinned scalar family  
Related counterexample candidates: none

## 1. Setup

Let

\[
 \lambda_1,\ldots,\lambda_n
\]

be distinct real nodes, let every `p_i` be nonzero, and normalize

\[
 \sum_i p_i=1.
\]

Put

\[
 \Omega(s)=\prod_{i=1}^n(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_i p_i\phi_i(s).
 \tag{L-15114.1}
\]

Let the arithmetic special source be `beta_i`, so off the diagonal

\[
 Q_{ij}=\frac{\beta_i-\beta_j}{\lambda_i-\lambda_j}.
\]

For the target-pinned scalar family, set

\[
 g_i(c)=\beta_i-c\lambda_i
 \tag{L-15114.2}
\]

and

\[
 R_c(s)=\sum_i p_i g_i(c)\phi_i(s).
 \tag{L-15114.3}
\]

Define the rational function

\[
 \boxed{h_c(s)=\frac{R_c(s)}{P(s)}.}
 \tag{L-15114.4}
\]

At every node,

\[
 h_c(\lambda_i)=g_i(c)=\beta_i-c\lambda_i.
 \tag{L-15114.5}
\]

## 2. Exact Loewner identity

Let `L(h_c)` be the confluent Loewner matrix

\[
 L(h_c)_{ij}
 =\begin{cases}
 \displaystyle\frac{h_c(\lambda_i)-h_c(\lambda_j)}
 {\lambda_i-\lambda_j},&i\ne j,\\[2mm]
 h_c'(\lambda_i),&i=j.
 \end{cases}
 \tag{L-15114.6}
\]

Then

\[
 \boxed{T_p(c)=L(h_c).}
 \tag{L-15114.7}
\]

### Proof

The off-diagonal entries agree by (L-15114.5):

\[
 L(h_c)_{ij}
 =\frac{(\beta_i-c\lambda_i)-(\beta_j-c\lambda_j)}
 {\lambda_i-\lambda_j}
 =Q_{ij}-c.
\]

Assume first that `P` is squarefree and let its roots be `r_k`. Partial fractions give

\[
 h_c(s)=\kappa_c+
 \sum_{k=1}^{n-1}\frac{A_k(c)}{s-r_k},
 \qquad
 A_k(c)=\frac{R_c(r_k)}{P'(r_k)}.
 \tag{L-15114.8}
\]

For

\[
 \ell_k(i)=\frac1{\lambda_i-r_k},
\]

divided differences give

\[
 L(h_c)
 =\sum_{k=1}^{n-1}w_k(c)\ell_k\ell_k^{\mathsf T},
 \qquad
 \boxed{w_k(c)=-\frac{R_c(r_k)}{P'(r_k)}.}
 \tag{L-15114.9}
\]

Moreover,

\[
 \ell_k^{\mathsf T}p
 =\frac{P(r_k)}{\Omega(r_k)}=0.
\]

Thus `L(h_c)p=0`. The target-pinned matrix has the same off-diagonal entries and also annihilates `p`; since every `p_i` is nonzero, the kernel equation uniquely fixes each diagonal entry. Hence the matrices agree, including the diagonal.

The identity also follows directly from the Bézoutian congruence of `L-15109`. QED.

## 3. Complete cone of positive special completions

Assume now that `P` has `n-1` distinct real roots

\[
 r_1<\cdots<r_{n-1}.
\]

The Cauchy vectors `ell_k` are linearly independent. Therefore (L-15114.9) gives the exact inertia

\[
 \boxed{
 \operatorname{Inertia}(T_p(c))
 =\left(
   \#\{k:w_k(c)>0\},
   \#\{k:w_k(c)<0\},
   1+\#\{k:w_k(c)=0\}
  \right).}
 \tag{L-15114.10}
\]

In particular,

\[
 \boxed{
 T_p(c)\succeq0,
 \quad
 \ker T_p(c)=\mathbb Rp
 \iff
 w_k(c)>0\quad(1\le k<n).}
 \tag{L-15114.11}
\]

More generally, every real symmetric special matrix with kernel containing `p` has a rational quotient `h=R/P`; when `P` has simple real roots it admits the representation

\[
 Q=\sum_k w_k\ell_k\ell_k^{\mathsf T}.
 \tag{L-15114.12}
\]

Thus the cone of positive special completions with kernel exactly `Rp` is the open positive orthant

\[
 \boxed{(w_1,\ldots,w_{n-1})\in\mathbb R_{>0}^{n-1}}
 \tag{L-15114.13}
\]

in the fixed Cauchy-ray basis. The canonical completion of `L-15111` is the interior point

\[
 w_1=\cdots=w_{n-1}=1,
\]

because its quotient is `-P'/P`.

This makes the distinction between arbitrary and arithmetic completion geometric:

- arbitrary special completion permits every point of the positive orthant;
- the target-pinned arithmetic family permits only one affine line in that orthant coordinate system.

## 4. The arithmetic scalar line

From `L-15109`,

\[
 R_c(s)=R_0(s)-c\{sP(s)+\Omega(s)\}.
\]

At a root of `P`,

\[
 R_c(r_k)=R_0(r_k)-c\Omega(r_k).
\]

Therefore

\[
 \boxed{
 w_k(c)
 =-\frac{R_0(r_k)}{P'(r_k)}
  +c\frac{\Omega(r_k)}{P'(r_k)}.}
 \tag{L-15114.14}
\]

The scalar family is literally the affine line

\[
 w(c)=w(0)+cv
 \tag{L-15114.15}
\]

inside residue space. It passes exactly when that line intersects the open positive orthant.

Writing

\[
 c_k=\frac{R_0(r_k)}{\Omega(r_k)},
 \qquad
 \sigma_k=P'(r_k)\Omega(r_k),
\]

condition `w_k(c)>0` is

\[
 c>c_k\quad(\sigma_k>0),
 \qquad
 c<c_k\quad(\sigma_k<0).
\]

Hence the positive-orthant intersection is exactly

\[
 \boxed{
 \max_{\sigma_k>0}c_k
 <c<
 \min_{\sigma_k<0}c_k.}
 \tag{L-15114.16}
\]

This recovers the Bézoutian threshold theorem as a residue-positivity statement.

## 5. Rational Herglotz formulation

Under the simple-real-root hypothesis,

\[
 h_c(s)=\kappa_c+\sum_k\frac{w_k(c)}{r_k-s}.
 \tag{L-15114.17}
\]

Therefore the target-pinned scalar completion passes if and only if `h_c` is a rational Herglotz--Nevanlinna function with:

- simple real poles `r_k`;
- strictly positive masses `w_k(c)`;
- an arbitrary real constant term.

The finite matrix theorem is the node-restricted Loewner positivity of this rational Herglotz function.

This formulation may be more tractable arithmetically than direct isotropic-cone positivity: prove that one scalar boundary shift turns the explicit rational quotient `R_c/P` into a positive discrete Cauchy transform.

## 6. Parity in residue coordinates

Assume symmetric nodes and an even target, so the roots are paired under

\[
 r\longleftrightarrow-r.
\]

A positive special completion commutes with inversion parity if and only if the residue weights satisfy

\[
 \boxed{w(-r)=w(r)}
 \tag{L-15114.18}
\]

for every paired root, with the obvious condition on a possible root at zero.

The canonical completion has all weights equal to one and is therefore automatically parity compatible. An arbitrary positive completion need not be parity compatible unless its paired weights agree. For the arithmetic scalar family, exact parity of the original data forces (L-15114.18) for every `c`.

## 7. Proof-producing consequences

### Root-explicit certificate

If algebraic root isolators are available, enclose every affine weight (L-15114.14) and prove one rational `c` makes every lower endpoint positive.

### Root-free matrix certificate

Build the exact/directed Loewner matrix `L(h_c)` at a rational candidate `c` and certify positive definiteness on `p^perp` by exact or interval `LDL^T`. This avoids root isolation entirely.

### Dual obstruction

A failed line/orthant intersection has a separating nonnegative vector `y` with

\[
 y^{\mathsf T}v=0,
 \qquad
 y^{\mathsf T}w(0)\le0.
 \tag{L-15114.19}
\]

This is a finite Farkas obstruction in residue coordinates. Algebraic enclosures of such a dual can complement the rational isotropic and threshold-pair obstructions already supported by `X-15103`.

## 8. Gap audit

1. The residue orthant requires simple real target roots. Before that is known, canonical inertia is only a necessary screen.
2. The roots and weights may be algebraic rather than rational; directed isolators or a root-free LDL proof are required.
3. Canonical positivity alone says only that the orthant is nonempty, not that the arithmetic line enters it.
4. A small distance of the line from the orthant boundary at finite levels does not prove a cofinal intersection.
5. Repeated roots require a confluent residue/jet formulation.