# T-15104 — Cofinal Finsler–Bézoutian completion criterion for the Riemann Hypothesis

Claim ID: `T-15104`  
Status: `PROPOSED`  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `L-15107`, `L-15109`, the finite Connes–van Suijlekom real-zero theorem in its exact Fourier coordinates, and Hurwitz's theorem  
Scope: positive repaired-Hermite finite approximation route  
Related counterexample candidates: none

## 1. Precise statement

Use

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right)
\]

and let

\[
 \mathcal S_{1/2}:=\{z\in\mathbb C:|\operatorname{Im}z|<1/2\}.
\]

For every `j`, let `\widetilde p_j` be a nonzero real even vector in one finite
Connes–van Suijlekom Fourier space, and let

\[
 f_j(z):=\widehat{\widetilde p_j}(z)
\]

be the Fourier transform of the corresponding compactly supported finite
Fourier sum. Assume

\[
 \boxed{f_j\longrightarrow\Xi}
 \tag{T-15104.1}
\]

locally uniformly on `\mathcal S_(1/2)`. In particular, locally uniform
convergence on all of `\mathbb C`, as in the stronger formulation, is more than
sufficient.

Let `eta_j` be the boundary vector in the same finite normalization and assume

\[
 \delta_j:=\eta_j^{\mathsf T}\widetilde p_j\ne0.
 \tag{T-15104.2}
\]

Set

\[
 p_j=\delta_j^{-1}\widetilde p_j,
 \qquad
 \eta_j^{\mathsf T}p_j=1.
 \tag{T-15104.3}
\]

Boundary normalization is used only in the finite completion. Since

\[
 \widehat{\widetilde p_j}=\delta_j\widehat p_j,
\]

it does not change the zero set and need not preserve the normalization in
which (T-15104.1) is stated.

Let `Q_j` be a real symmetric finite special matrix in the same nodes, parity,
and Fourier normalization. Assume every coordinate of `p_j` used below is
nonzero. Define

\[
 \boxed{
 T_j(c)=Q_j+
 \operatorname{diag}\!\left(
   \frac{c(\eta_j)_i-(Q_jp_j)_i}{(p_j)_i}
 \right)
 -c\eta_j\eta_j^{\mathsf T}
 =A_j+cB_j,}
 \tag{T-15104.4}
\]

where

\[
 A_j=Q_j-
 \operatorname{diag}\!\left(
   \frac{(Q_jp_j)_i}{(p_j)_i}
 \right),
 \qquad
 B_j=
 \operatorname{diag}\!\left(
   \frac{(\eta_j)_i}{(p_j)_i}
 \right)-\eta_j\eta_j^{\mathsf T}.
 \tag{T-15104.5}
\]

Then

\[
 A_jp_j=B_jp_j=T_j(c)p_j=0
 \quad\text{for every real }c.
 \tag{T-15104.6}
\]

Assume that for every sufficiently large `j` there is a rational number `c_j`
such that

\[
 \boxed{
 T_j(c_j)\succeq0,
 \qquad
 \ker T_j(c_j)=\mathbb Rp_j.}
 \tag{T-15104.7}
\]

Then the Riemann Hypothesis is true.

The word `rational` is a proof-producing convenience rather than an analytic
necessity. Once the strict finite feasible interval is nonempty, it contains a
rational point.

## 2. Finite real-rootedness

In the exact Connes–van Suijlekom coordinates, the boundary vector is the
all-ones vector and the off-diagonal entries of a special matrix have the form

\[
 (Q_j)_{rs}=
 \frac{\beta_r-\beta_s}{\lambda_r-\lambda_s}
 \qquad(r\ne s),
 \tag{T-15104.8}
\]

with distinct real spectral nodes `lambda_r`. The scalar completion preserves
this structure because

\[
 (T_j(c))_{rs}
 =(Q_j)_{rs}-c
 =
 \frac{(\beta_r-c\lambda_r)-(\beta_s-c\lambda_s)}
      {\lambda_r-\lambda_s}.
 \tag{T-15104.9}
\]

The diagonal is unrestricted by the special divided-difference condition and is
exactly the target-pinning diagonal in (T-15104.4). If `Q_j,p_j,eta_j` respect
the inversion parity, then so does `T_j(c)`.

Thus (T-15104.7) makes `T_j(c_j)` a real symmetric positive-semidefinite special
matrix with one-dimensional even kernel. The finite Connes–van Suijlekom theorem
therefore proves that every zero of

\[
 \widehat p_j
\]

is real. Multiplication by the nonzero scalar `delta_j` does not change zeros,
so every zero of the convergent transform `f_j=\widehat{\widetilde p_j}` is real
as well.

Only the eventual tail of the sequence matters; finitely many exceptional
indices may be discarded.

## 3. Hurwitz passage to `Xi`

Put

\[
 \mathcal S^+_{1/2}
 =\{z:0<\operatorname{Im}z<1/2\},
 \qquad
 \mathcal S^-_{1/2}
 =\{z:-1/2<\operatorname{Im}z<0\}.
\]

Each is connected. Since every zero of `f_j` is real, every `f_j` is zero-free
on both half-strips. By (T-15104.1), the sequence converges locally uniformly to
`Xi` there. Hurwitz's zero-free form says that on each connected half-strip the
limit is either zero-free or identically zero.

The second alternative is impossible because `Xi` is not the zero function; for
example

\[
 \Xi(-3i/2)=\xi(2)=\pi/6\ne0.
\]

Therefore

\[
 \Xi(z)\ne0
 \qquad
 (z\in\mathcal S^+_{1/2}\cup\mathcal S^-_{1/2}).
 \tag{T-15104.10}
\]

Every nontrivial zeta zero `rho=beta+i gamma`, with `0<beta<1`, corresponds to

\[
 z_\rho=\frac{\rho-1/2}{i}
 =\gamma-i(\beta-1/2)
 \in\mathcal S_{1/2},
 \tag{T-15104.11}
\]

and

\[
 \Xi(z_\rho)=\xi(\rho)=0.
\]

By (T-15104.10), `z_rho` must be real. Hence `beta=1/2`. Every nontrivial zero
of `zeta` lies on the critical line, which is RH. This proves the first boxed
implication.

## 4. Exact finite Finsler equivalence

Fix one level and omit the index `j`. Put

\[
 H=p^\perp,
 \qquad
 a(x)=x^{\mathsf T}A_px,
 \qquad
 b(x)=x^{\mathsf T}B_px.
 \tag{T-15104.12}
\]

Because `A_pp=B_pp=0`, every vector has a unique decomposition

\[
 y=\alpha p+x,
 \qquad x\in H,
\]

and

\[
 y^{\mathsf T}T_p(c)y=x^{\mathsf T}(A_p+cB_p)x.
 \tag{T-15104.13}
\]

Consequently

\[
 \boxed{
 T_p(c)\succeq0,
 \quad
 \ker T_p(c)=\mathbb Rp
 \iff
 a(x)+cb(x)>0
 \quad(0\ne x\in H).}
 \tag{T-15104.14}
\]

The slope is nondegenerate on `H`. Indeed, with

\[
 D=\operatorname{diag}(\eta_i/p_i),
\]

one has

\[
 B_p=D-\eta\eta^{\mathsf T},
 \qquad
 D^{-1}\eta=p,
 \qquad
 \eta^{\mathsf T}D^{-1}\eta=1.
\]

Thus `ker B_p=Rp`. If

\[
 n_+=\#\{i:\eta_ip_i>0\},
 \qquad
 n_-=\#\{i:\eta_ip_i<0\},
\]

then

\[
 \operatorname{Inertia}(B_p|_H)=(n_+-1,n_-).
 \tag{T-15104.15}
\]

In the definite cases the nonzero isotropic cone is empty, and a sufficiently
large scalar of the appropriate sign makes (T-15104.14) positive. In the
indefinite case, the strict Finsler theorem gives

\[
 \boxed{
 \exists c\in\mathbb R:
 a+cb>0\text{ on }H\setminus\{0\}
 \iff
 a(x)>0
 \text{ whenever }
 0\ne x\in H,\ b(x)=0.}
 \tag{T-15104.16}
\]

The same statement therefore remains valid in all cases, interpreting the
condition as vacuous when `B_p|_H` is definite.

For completeness, define

\[
 c_-=
 \sup_{\substack{x\in H\\b(x)>0}}
 \frac{-a(x)}{b(x)},
 \qquad
 c_+=
 \inf_{\substack{x\in H\\b(x)<0}}
 \frac{-a(x)}{b(x)}.
 \tag{T-15104.17}
\]

Strict Finsler separation is equivalent to

\[
 c_-<c_+,
 \tag{T-15104.18}
\]

and the complete feasible set is the open interval `(c_-,c_+)`, with an infinite
endpoint in a definite-slope case. Indeed, for `b(x)>0`, positivity requires
`c>-a(x)/b(x)`; for `b(x)<0`, it requires `c<-a(x)/b(x)`; and on `b=0` it is
exactly the condition in (T-15104.16).

The nontrivial implication in (T-15104.18) can be seen directly from Dines
convexity of the homogeneous joint range

\[
 \{(b(x),a(x)):x\in H\}.
\]

If the lower and upper thresholds met or crossed, convexity would produce a
nonzero represented point with first coordinate zero and second coordinate
nonpositive, contradicting (T-15104.16). Compactness of the unit isotropic
section supplies strict separation.

Combining (T-15104.14)--(T-15104.18) proves the promised cofinal equivalence:

\[
 \boxed{
 x^{\mathsf T}A_{p_j}x>0
 \quad
 \text{whenever }
 x\perp p_j,
 \ x\ne0,
 \ x^{\mathsf T}B_{p_j}x=0}
 \tag{T-15104.19}
\]

for every sufficiently large `j` if and only if a strict scalar completion
exists at every sufficiently large `j`. Since the feasible interval is open,
`c_j` may be chosen rationally.

## 5. Simple-root Bézoutian equivalence

Assume now that the finite special nodes

\[
 \lambda_1,\ldots,\lambda_n
\]

are distinct and real, `eta=(1,...,1)^T`, and the finite target polynomial is

\[
 \Omega(s)=\prod_{i=1}^n(\lambda_i-s),
 \qquad
 \phi_i(s)=\frac{\Omega(s)}{\lambda_i-s},
 \qquad
 P(s)=\sum_{i=1}^np_i\phi_i(s).
 \tag{T-15104.20}
\]

Write the special off-diagonal source as in (T-15104.8), put

\[
 R_c(s)=
 \sum_{i=1}^np_i(\beta_i-c\lambda_i)\phi_i(s),
 \tag{T-15104.21}
\]

and define the Bézoutian kernel

\[
 \mathcal B_c(s,t)=
 \frac{P(s)R_c(t)-P(t)R_c(s)}{s-t}.
 \tag{T-15104.22}
\]

At the nodes, with `P_i=P(lambda_i)`, one has the exact congruence

\[
 \boxed{
 (\mathcal B_c(\lambda_i,\lambda_j))_{ij}
 =-\operatorname{diag}(P_i)
   T_p(c)
   \operatorname{diag}(P_i).}
 \tag{T-15104.23}
\]

For `i!=j`, this follows immediately from the divided-difference formula. On the
diagonal, the removable limit

\[
 P'(\lambda_i)R_c(\lambda_i)
 -P(\lambda_i)R_c'(\lambda_i)
\]

agrees with the forced diagonal precisely because `T_p(c)p=0`.

Suppose `P` has `n-1` simple real roots

\[
 r_1<\cdots<r_{n-1}.
\]

The kernel `\mathcal B_c` has degree at most `n-2` in each variable. Evaluation
at the `r_k` is therefore an isomorphism on the polynomial space of degree at
most `n-2`, and

\[
 \mathcal B_c(r_k,r_l)=0
 \quad(k\ne l),
 \qquad
 \mathcal B_c(r_k,r_k)=P'(r_k)R_c(r_k).
 \tag{T-15104.24}
\]

Thus (T-15104.23) and congruence invariance of inertia give

\[
 \boxed{
 T_p(c)\succeq0,
 \quad
 \ker T_p(c)=Rp
 \iff
 P'(r_k)R_c(r_k)<0
 \quad(1\le k<n).}
 \tag{T-15104.25}
\]

Now

\[
 R_c(s)=R_0(s)-c\{sP(s)+\Omega(s)\},
\]

so at a target root

\[
 R_c(r_k)=R_0(r_k)-c\Omega(r_k).
 \tag{T-15104.26}
\]

Define

\[
 c_k=\frac{R_0(r_k)}{\Omega(r_k)},
 \qquad
 \sigma_k=P'(r_k)\Omega(r_k).
 \tag{T-15104.27}
\]

Then (T-15104.25) is equivalent to

\[
 c>c_k\quad(\sigma_k>0),
 \qquad
 c<c_k\quad(\sigma_k<0).
\]

Therefore the exact simple-root feasible condition is

\[
 \boxed{
 \max_{\sigma_k>0}c_k
 <
 \min_{\sigma_k<0}c_k.}
 \tag{T-15104.28}
\]

Empty sides are interpreted as infinite. This is the root-coordinate form of
the Finsler interval. Hence, when all sufficiently large finite target
polynomials have simple real roots, the cofinal scalar-completion hypothesis is
equivalent to the cofinal strict threshold separation (T-15104.28).

Repeated roots require a confluent Bézoutian/Hermite criterion and are not
silently included.

## 6. Final logical chain

The proved conditional chain is

\[
 \boxed{
 \begin{gathered}
 f_j=\widehat{\widetilde p_j}\to\Xi
 \text{ locally uniformly on }\mathcal S_{1/2},\\
 \text{and cofinally either (T-15104.19) or, in the simple-root case,
 (T-15104.28)}
 \end{gathered}}
\]

\[
 \Longrightarrow
 \boxed{
 \text{cofinally there are rational }c_j
 \text{ with }
 T_j(c_j)\succeq0,
 \ \ker T_j(c_j)=Rp_j}
\]

\[
 \Longrightarrow
 \boxed{
 \text{every finite }f_j\text{ has only real zeros}}
\]

\[
 \Longrightarrow
 \boxed{
 \Xi\text{ has no nonreal zero in }\mathcal S_{1/2}}
\]

\[
 \Longrightarrow
 \boxed{\mathrm{RH}}.
\]

## 7. Proof boundary

This theorem proves the implication under its stated hypotheses. It does **not**
prove:

1. local-uniform convergence of a production repaired-target sequence in the
   final CvS/CCM normalization;
2. the cofinal Finsler isotropic-cone inequality;
3. cofinal simple real-rootedness or root-threshold separation;
4. the imported finite real-zero theorem or its normalization inside this
   repository.

A finite ladder, however long, does not replace the cofinal hypotheses.