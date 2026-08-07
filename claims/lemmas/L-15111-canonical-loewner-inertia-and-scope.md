# L-15111 — Canonical Loewner completion: exact inertia, parity, and scope

Claim ID: `L-15111`  
Status: **PROVED FINITE-DIMENSIONAL LEMMA**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: elementary partial fractions, the Cauchy determinant, and the finite special-matrix definitions  
Scope: squarefree finite target polynomials with no node root  
Related counterexample candidates: none

## 1. Setup

Let

\[
 \lambda_1,\ldots,\lambda_n\in\mathbb R
\]

be distinct, let `p_i != 0`, and normalize

\[
 \sum_i p_i=1.
\]

Put

\[
 \Omega(s)=\prod_{i=1}^n(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_{i=1}^n p_i\phi_i(s).
\]

Then `deg P=n-1`, and

\[
 P(\lambda_i)=p_i\phi_i(\lambda_i)\ne0.
\]

Assume that `P` is squarefree. Notice that `p_i != 0` makes the node values nonzero, but it does **not** imply squarefreeness.

Define

\[
 g(s)=-\frac{P'(s)}{P(s)}
\]

and the real symmetric Loewner matrix

\[
 Q^{\rm can}_{ij}=
 \begin{cases}
 \displaystyle\frac{g(\lambda_i)-g(\lambda_j)}{\lambda_i-\lambda_j},&i\ne j,\\[2mm]
 g'(\lambda_i),&i=j.
 \end{cases}
 \tag{L-15111.1}
\]

## 2. Exact inertia theorem

Suppose `P` has `r` distinct real roots and `c` nonreal conjugate pairs. Thus

\[
 r+2c=n-1.
\]

Then

\[
 \boxed{
 \operatorname{Inertia}(Q^{\rm can})=(r+c,\ c,\ 1).}
 \tag{L-15111.2}
\]

Moreover,

\[
 \boxed{Q^{\rm can}p=0,\qquad \ker Q^{\rm can}=\mathbb Rp.}
 \tag{L-15111.3}
\]

Consequently

\[
 \boxed{
 Q^{\rm can}\succeq0\text{ with corank one}
 \iff
 P\text{ has }n-1\text{ simple real roots}.}
 \tag{L-15111.4}
\]

The number of negative eigenvalues is exactly the number of nonreal conjugate root pairs.

### Proof

Write the simple roots as `mu_1,...,mu_(n-1)`. Partial fractions give

\[
 g(s)=\sum_m\frac1{\mu_m-s}.
\]

For

\[
 \ell(\mu)_i=\frac1{\lambda_i-\mu},
\]

direct divided-difference algebra yields

\[
 Q^{\rm can}=\sum_m\ell(\mu_m)\ell(\mu_m)^{\mathsf T}.
 \tag{L-15111.5}
\]

For a real root, the summand is a real positive rank-one matrix. For a nonreal pair `mu,bar(mu)`, write

\[
 \ell(\mu)=u+iv.
\]

The paired contribution is

\[
 \ell(\mu)\ell(\mu)^{\mathsf T}
 +\ell(\bar\mu)\ell(\bar\mu)^{\mathsf T}
 =2uu^{\mathsf T}-2vv^{\mathsf T}.
\]

Form a real `n by (n-1)` matrix `U` whose columns are:

- `ell(mu)` for each real root;
- `sqrt(2)u,sqrt(2)v` for each conjugate pair.

Let `J` be diagonal with one `+1` for each real root, and a `(+1,-1)` block for every nonreal pair. Then

\[
 Q^{\rm can}=UJU^{\mathsf T}.
 \tag{L-15111.6}
\]

The complex Cauchy matrix with columns `ell(mu_m)` has full column rank. Its Cauchy minors are nonzero because the nodes are distinct, the roots are distinct, and no root is a node. Therefore the displayed real columns of `U` are also independent. A QR decomposition of `U`, followed by completion to an orthogonal basis of `R^n`, makes (L-15111.6) congruent to

\[
 \operatorname{diag}(RJR^{\mathsf T},0)
\]

with `R` invertible. Sylvester inertia therefore gives (L-15111.2).

Finally,

\[
 \ell(\mu)^{\mathsf T}p
 =\sum_i\frac{p_i}{\lambda_i-\mu}
 =\frac{P(\mu)}{\Omega(\mu)}=0.
\]

Hence `U^T p=0`, so `Q^can p=0`. The rank is `n-1`, proving (L-15111.3). QED.

### Important repair to the informal proof

It is not enough to say that one conjugate-pair summand has signature `(1,1)`: adding the other summands could in principle change its negative direction. The full Cauchy factorization (L-15111.6) and full-column-rank argument are what make the exact inertia count valid.

## 3. Automatic parity for the canonical completion

Assume the nodes are symmetric under `lambda -> -lambda`, indexed by an involution `i -> -i`, and the target is exactly even:

\[
 p_{-i}=p_i.
\]

Then the interpolation polynomial is even, its root multiset is invariant under `mu -> -mu`, and

\[
 g(-s)=-g(s).
\]

Therefore the special source

\[
 b_i=g(\lambda_i)
\]

is odd, while the diagonal

\[
 a_i=g'(\lambda_i)
\]

is even. Thus

\[
 Q^{\rm can}_{-i,-j}=Q^{\rm can}_{ij},
\]

and the canonical completion commutes with inversion parity.

This proves that, in the simple-real-root regime, a parity-compatible positive special completion exists canonically. It does not say that every arbitrary completion is parity invariant.

## 4. Exact scope relative to the target-pinned scalar pencil

Let an arithmetic special matrix have source values `beta_i`, so its one-scalar target-pinned family has off-diagonal source

\[
 \beta_i-c\lambda_i.
\]

The canonical matrix `Q^can` belongs to that scalar family if and only if there are real numbers `c,d` such that

\[
 \boxed{
 g(\lambda_i)=\beta_i-c\lambda_i+d
 \qquad(1\le i\le n).}
 \tag{L-15111.7}
\]

Indeed, special source vectors are defined modulo addition of a constant. Equality in (L-15111.7) makes all off-diagonal entries agree. Since both matrices annihilate `p` and every `p_i` is nonzero, the diagonal is then uniquely forced and the matrices agree completely.

Consequently:

- real-rootedness of `P` is equivalent to existence of **some** positive special completion;
- it is only a necessary condition for the arithmetic one-scalar completion of `L-15107`;
- the one-scalar gate still requires the Finsler/Bézoutian threshold separation of `L-15107/L-15109`.

A real-root census alone therefore does not decide the target-pinned scalar gate.

## 5. Repeated roots

If a root has multiplicity `m`, then `-P'/P` has residue `m` there and the canonical matrix contains `m ell ell^T`, not `m` independent columns. Its rank is the number of distinct roots rather than `n-1`, so the canonical matrix has a larger kernel.

This does not prove that every special completion fails for a repeated polynomial: a quotient operator with a repeated but semisimple real eigenvalue can admit another positive metric. The theorem above is deliberately restricted to the squarefree case.

## 6. Proof-producing use

No root finder is needed to construct `Q^can`. At the nodes,

\[
 b_i=-\frac{P'(\lambda_i)}{P(\lambda_i)},
 \qquad
 a_i=\frac{P'(\lambda_i)^2-P(\lambda_i)P''(\lambda_i)}{P(\lambda_i)^2}.
\]

For rational nodes and target coefficients these are rational. Exact symmetric congruence then returns the real/nonreal-pair count through (L-15111.2).

## Gap audit

1. Squarefreeness is not implied by nonzero target coordinates.
2. The parity conclusion requires exact symmetry, not numerical near-symmetry.
3. The canonical completion tests arbitrary special completion, not the restricted arithmetic scalar line.
4. For directed target intervals, rational midpoint inertia is not a certificate without an operator-radius or exact algebraic enclosure.