# L-32302 — Any nonnegative exact fragmentation certificate forces a Möbius–Riesz one-sign criterion

Claim ID: `L-32302`  
Title: The elementary affine potential `phi(n)=n-1` projects every nonnegative exact balanced fragmentation onto one fixed reciprocal-zeta Riesz mean  
Status: **PROPOSED COMPLETE EXACT LEMMA / RH FIREWALL**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: exact floor/divergence formulation of PRs #247/#272; one-sided Landau consumer already used throughout the repository  
Scope: exact finite dual projection and its analytic consequence; it does not prove the required one-sign inequality

## 1. Exact target divergence

Let

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X,
\]

and put `w_X(1)=0`.  Let `R_X(1),...,R_X(X)` be its exact node divergence, so

\[
\boxed{
 w_X(q)=\sum_{m=1}^{X}R_X(m)\left\lfloor\frac mq\right\rfloor
 \qquad(1\le q\le X).
}
\tag{L-32302.1}
\]

An exact binary fragmentation flow `d_(n,j)` has divergence

\[
 \partial[n,j]=e_n-e_j-e_{n-j}.
\]

If `d_(n,j)>=0` and `partial d=R_X`, it is a nonnegative exact carry saturation, regardless of which fixed balanced window contains the retained splits.

## 2. The affine dual potential has constant split defect

Define

\[
\boxed{
 \phi(m)=m-1.
}
\tag{L-32302.2}
\]

For every nontrivial binary split `n=j+(n-j)`, exactly

\[
\boxed{
 \phi(n)-\phi(j)-\phi(n-j)=1.
}
\tag{L-32302.3}
\]

Hence every nonnegative exact flow satisfies

\[
\boxed{
 \sum_{m=1}^{X}R_X(m)\phi(m)
 =\sum_{n,j}d_{n,j}\ge0.
}
\tag{L-32302.4}
\]

This uses no entropy estimate, no carry norm, and no asymptotic theorem.

## 3. Möbius projection of the affine potential

The elementary Möbius divisor identity

\[
 \sum_{q\le m}\mu(q)\left\lfloor\frac mq\right\rfloor=1
\]

gives

\[
\boxed{
 m-1
 =-\sum_{q=2}^{m}
 \mu(q)\left\lfloor\frac mq\right\rfloor.
}
\tag{L-32302.5}
\]

Substitute (L-32302.5) into (L-32302.4), interchange the finite sums, and use (L-32302.1).  One obtains the exact identity

\[
\boxed{
 \sum_{m=1}^{X}R_X(m)(m-1)
 =-\sum_{q=2}^{X}
 \frac{\mu(q)}{\sqrt q}\log\frac Xq.
}
\tag{L-32302.6}
\]

Therefore every nonnegative exact fragmentation certificate forces

\[
\boxed{
 \sum_{q=2}^{X}
 \frac{\mu(q)}{\sqrt q}\log\frac Xq\le0.
}
\tag{L-32302.7}

The inequality is not an incidental consequence of a particular producer.  It is a mandatory dual projection of **every** positive exact binary fragmentation of the critical carry target.

## 4. The projected scalar retains every off-line zeta pole

Put

\[
 \mathcal R_*(X)
 =\sum_{q=2}^{X}
 \frac{\mu(q)}{\sqrt q}\log\frac Xq.
\tag{L-32302.8}
\]

For `X=e^t`, initially in the absolute-convergence half-plane,

\[
\begin{aligned}
 \int_0^\infty \mathcal R_*(e^t)e^{-zt}\,dt
 &=\frac1{z^2}
 \sum_{q=2}^\infty\frac{\mu(q)}{q^{z+1/2}}\\
 &=\boxed{
 \frac{1}{z^2}
 \left[
  \frac1{\zeta(z+1/2)}-1
 \right].}
\end{aligned}
\tag{L-32302.9}
\]

Thus every zeta zero `rho` with `Re(rho)>1/2` gives an uncancelled pole at

\[
 z=\rho-\frac12
\]

of this transform.

The standard one-sided Landau theorem already used by the repository therefore gives the following source-pinned implication:

\[
\boxed{
 \mathcal R_*(X)\le0
 \text{ for every sufficiently large }X
 \quad\Longrightarrow\quad
 \mathrm{RH}.
}
\tag{L-32302.10}
\]

Indeed an eventually one-signed Laplace source cannot have its first singularity at a nonreal point, while the right side of (L-32302.9) has no positive-real singularity corresponding to an off-line zero. Functional-equation symmetry supplies the other half of the critical strip.

## 5. Consequence: positive fragmentation is already a full RH theorem

Combining Sections 2--4 gives

\[
\boxed{
\begin{aligned}
&\text{cofinal nonnegative exact balanced fragmentation}\
&\qquad\Longrightarrow
 \mathcal R_*(X)\le0\text{ cofinally}\
&\qquad\Longrightarrow \mathrm{RH}.
\end{aligned}}
\tag{L-32302.11}
\]

This sharpens the status of several live routes.  A theorem such as `MFT`, pointwise producer positivity, `FEP`, or a positive residue automaton is **not** a finite combinatorial lemma followed by the arithmetic part.  Its positivity statement already proves a reciprocal-zeta one-sign theorem before the entropy/prime-ramp consumer is invoked.

This explains why long positive finite ranges and apparently finite residue grammars can fail at remote quotient knots: the scalar (L-32302.7) carries the full strip-sensitive source.

## 6. Relation to the previous instant-pass idea

A previous exploratory sketch proposed that a Möbius projection might simplify the carry problem into an easier contraction.  Equation (L-32302.9) shows the correct scope: the projection does simplify the **interface**, but it does not weaken the arithmetic.  It exposes `1/zeta` directly.

Accordingly, a generic proof of a smooth or finite-state contraction after this projection would itself be an RH proof, not a preliminary adapter.

## 7. Proof boundary

Proved exactly here:

1. constant affine split defect;
2. finite Möbius floor representation of `m-1`;
3. exact projection (L-32302.6);
4. positive fragmentation forces the Riesz one-sign inequality;
5. the reciprocal-zeta Laplace transform.

The last Landau implication uses the repository's existing one-sign pole-exclusion theorem.

Not proved here:

1. the Riesz one-sign inequality itself;
2. existence of a cofinal nonnegative exact fragmentation;
3. RH.
