# L-26105 — Exact Hilbert–Farkas dual of the annular carry repair

Claim ID: `L-26105`  
Title: The minimum norm of a feasible annular flow equals one explicit one-sided divisor-gradient restriction constant  
Status: **PROPOSED COMPLETE FINITE CONVEX DUALITY**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `L-26101`, `L-26102`  
Scope: exact finite-dimensional equivalence; exposes the sole arithmetic inequality

## 1. Primal annular repair radius

Let `A_X` be the complete prime-power annular matrix and let

\[
 r_X(q)=v_q(b_X^{(0)})-w_X(q).
\]

Define

\[
\boxed{
 \mathcal R_X
 =\inf\{\|F\|_2:A_XF\ge r_X\}.
}
\tag{L-26105.1}
\]

Use the convention `mathcal R_X=+infinity` if the annular inequalities are infeasible.

By `L-26102`, the bound

\[
 \mathcal R_X=X^{o(1)}
 \tag{L-26105.2}
\]

is sufficient for the sharp prime-ramp estimate.

## 2. Quadratic dual

Consider the strictly convex program

\[
 \min_F\frac12\|F\|_2^2
 \quad\text{subject to}\quad
 A_XF\ge r_X.
 \tag{L-26105.3}
\]

Its Lagrangian with multipliers `lambda_q>=0` is

\[
 \mathcal L(F,\lambda)
 =\frac12\|F\|_2^2
 +\langle\lambda,r_X-A_XF\rangle.
\]

Minimizing over `F` gives

\[
 F=A_X^*\lambda
\]

and the dual objective

\[
 \langle\lambda,r_X\rangle
 -\frac12\|A_X^*\lambda\|_2^2.
 \tag{L-26105.4}
\]

Finite-dimensional strong duality, together with Farkas' alternative in the infeasible case, gives

\[
\boxed{
 \frac12\mathcal R_X^2
 =\sup_{\lambda\ge0}
 \left[
  \langle\lambda,r_X\rangle
  -\frac12\|A_X^*\lambda\|_2^2
 \right].
}
\tag{L-26105.5}
\]

If a nonnegative `lambda` satisfies `A_X^*lambda=0` and
`<lambda,r_X>>0`, both sides are infinite, exactly as required by Farkas.

## 3. Homogeneous restriction constant

For one fixed nonzero direction `lambda`, optimize (L-26105.4) over positive scalar multiples. This yields

\[
\boxed{
 \mathcal R_X
 =\sup_{\substack{\lambda\ge0\\A_X^*\lambda\ne0}}
 \frac{\langle\lambda,r_X\rangle_+}
      {\|A_X^*\lambda\|_2},
}
\tag{L-26105.6}

with the same infinite convention for a positive null direction.

Using the exact adjoint formula from `L-26101`,

\[
\boxed{
 \|A_X^*\lambda\|_2^2
 =\sum_{j\in I_X}
 \left(
  2\sum_{q\mid j}\lambda_q
  -\sum_{q\mid j-1}\lambda_q
  -\sum_{q\mid j+1}\lambda_q
 \right)^2.
}
\tag{L-26105.7}

Thus the complete low-norm flow theorem is equivalent to the finite inequality

\[
\boxed{
 \left(
  \sum_{q=p^a\le X}\lambda_qr_X(q)
 \right)_+
 \le X^{o(1)}
 \left[
  \sum_{j\in I_X}
  \left(
   2\sum_{q\mid j}\lambda_q
   -\sum_{q\mid j-1}\lambda_q
   -\sum_{q\mid j+1}\lambda_q
  \right)^2
 \right]^{1/2}
}
\tag{ADF}

for every nonnegative prime-power vector `lambda`.

Call this the **Annular Dual Frame inequality**.

## 4. Relation to the active projection

At the optimum, the Karush–Kuhn–Tucker equations give

\[
 F_X=A_X^*\lambda_X,
 \tag{L-26105.8}
\]

\[
 \lambda_X\ge0,
 \qquad
 A_XF_X-r_X\ge0,
 \tag{L-26105.9}
\]

and

\[
 \lambda_X(q)\bigl((A_XF_X)_q-r_X(q)\bigr)=0.
 \tag{L-26105.10}
\]

Thus the support of the dual optimizer is an active constraint set, and the minimum-norm projection in `L-26103` is the natural primal active-set solver for (ADF).

`SAF2/SAF3` are a constructive sufficient mechanism for proving (ADF); (ADF) itself is the exact non-iterative acceptance statement.

## 5. The von-Mangoldt near-null firewall

Take

\[
 \lambda_q=\Lambda(q).
\]

Then the exact prime-power identity gives

\[
\boxed{
 (A_X^*\Lambda)_j
 =2\log j-\log(j-1)-\log(j+1)
 =\log\frac{j^2}{j^2-1}.
}
\tag{L-26105.11}

Hence

\[
 \|A_X^*\Lambda\|_2\asymp X^{-3/2}.
 \tag{L-26105.12}
\]

The numerator is

\[
\boxed{
 \langle\Lambda,r_X\rangle
 =J_X(b_X^{(0)})
 -\sum_{q=p^a\le X}
  \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
}
\tag{L-26105.13}

This is exactly the sharp prime-ramp deficit. Therefore a generic lower frame theorem cannot prove (ADF): the von-Mangoldt vector is a genuine arithmetic near-null direction. A successful proof must use the sign of its source pairing and show that every other nonnegative near-null vector is controlled by the same slack mechanism.

This is the dual version of the mandatory Mertens/carry firewall.

## 6. Proposed proof decomposition

A direct proof of (ADF) may proceed by decomposing every nonnegative `lambda` into:

1. a near-null component aligned with the von-Mangoldt prime-power chain;
2. same-base chain fluctuations controlled by the Toeplitz floor of `L-26103`;
3. cross-prime quotient-cell fluctuations controlled by complete-period orthogonality and bounded boundary ledgers.

The first component must be paired with the actual signed residual before any absolute value. The other components may be paid by the annular gradient norm.

The bounded cluster inverses from PR #254 provide the finite correction at consecutive prime-power boundaries.

## 7. Proof boundary

Exact in this file:

- primal/dual equality;
- homogeneous restriction formula;
- KKT relation to the active projection;
- the explicit annular divisor-gradient denominator;
- the von-Mangoldt near-null identity.

Open:

- the all-scale `ADF` inequality with subpower constant;
- equivalently, `SAF2/SAF3` or another proof of `mathcal R_X=X^o(1)`;
- RH.