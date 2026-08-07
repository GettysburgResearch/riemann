# L-23701 — An exact nonnegative greedy carry minorant

Claim ID: `L-23701`  
Title: Backward minimum-ratio elimination always constructs a nonnegative carry combination below the complete prime ramp  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: Kummer's carry formula and finite triangular elimination  
Scope: finite arithmetic for each integer endpoint; no RH input

## 1. Carry matrix

Fix an integer `X>=2`. For integers

\[
2\le q\le n\le X
\]

define

\[
\boxed{
\beta_{nq}
=
\frac{
 \lfloor n/q\rfloor
 \bigl(q-1-(n\bmod q)\bigr)
}{n+1}.}
\tag{L-23701.1}
\]

Every entry is nonnegative, and

\[
\boxed{
\beta_{nn}=rac{n-1}{n+1}>0.}
\tag{L-23701.2}
\]

Let

\[
\boxed{
 w_X(q)=\frac1{\sqrt q}\log\frac Xq,
 \qquad 2\le q\le X.}
\tag{L-23701.3}
\]

The target vector is nonnegative and vanishes at `q=X`.

## 2. Exact carry interpretation

Let `p` be prime and `q=p^k`. For `0<=j<=n`, the carry across the base-`q`
boundary in the addition

\[
j+(n-j)=n
\]

occurs exactly when

\[
 j\bmod q>n\bmod q.
\]

There are

\[
\lfloor n/q\rfloor\bigl(q-1-(n\bmod q)\bigr)
\]

such values of `j`. Hence `beta_(nq)` is the average carry indicator. Kummer's
theorem and Legendre's formula give

\[
\boxed{
G_n
:=
\frac1{n+1}\sum_{j=0}^n\log {n\choose j}
=
\sum_{q=p^k\le n}\Lambda(q)\beta_{nq}.}
\tag{L-23701.4}
\]

This identity is finite and exact.

## 3. Backward greedy residual

Initialize

\[
\rho_X^{(X)}(q)=w_X(q),
\qquad 2\le q\le X.
\tag{L-23701.5}
\]

For `n=X,X-1,...,2`, assume that

\[
\rho_X^{(n)}(q)\ge0,
\qquad2\le q\le n.
\]

Define

\[
\boxed{
 d_X(n)
 =
 \min_{\substack{2\le q\le n\\\beta_{nq}>0}}
 \frac{\rho_X^{(n)}(q)}{\beta_{nq}}.}
\tag{L-23701.6}
\]

The minimum exists because the diagonal entry is positive. Put

\[
\boxed{
\rho_X^{(n-1)}(q)
=
\rho_X^{(n)}(q)-d_X(n)\beta_{nq},
\qquad2\le q<n.}
\tag{L-23701.7}
\]

All operations are finite. If the inputs are rational, the construction is
rational. For the actual logarithmic target, directed enclosures can be used
without changing the definition.

## 4. Positivity and feasibility

By construction,

\[
d_X(n)\ge0.
\]

For every `q<n` with `beta_(nq)>0`, equation (L-23701.6) gives

\[
 d_X(n)\beta_{nq}\le\rho_X^{(n)}(q).
\]

If `beta_(nq)=0`, the residual is unchanged. Thus

\[
\rho_X^{(n-1)}(q)\ge0.
\]

Induction proves

\[
\boxed{d_X(n)\ge0\quad(2\le n\le X).}
\tag{L-23701.8}
\]

Unwinding the residual recursion gives, for every `q`,

\[
\boxed{
\sum_{n=q}^X d_X(n)\beta_{nq}\le w_X(q).}
\tag{L-23701.9}
\]

Therefore `d_X` is an unconditional nonnegative sub-saturation of the complete
carry system.

This differs from Carry Saturation. The exact triangular inverse `c_X` forces
equality in every row and may a priori have either sign. The greedy vector
`d_X` is always nonnegative and may leave slack.

## 5. Blocking index and exact defect ledger

At stage `n`, choose the least minimizer

\[
q_X(n)
=
\min\operatorname*{argmin}_{\beta_{nq}>0}
\frac{\rho_X^{(n)}(q)}{\beta_{nq}}.
\tag{L-23701.10}
\]

Call `q_X(n)` the **blocking constraint**. Define the diagonal candidate

\[
\widehat d_X(n)
=
\frac{\rho_X^{(n)}(n)}{\beta_{nn}}
\tag{L-23701.11}
\]

and blocker loss

\[
\boxed{
\ell_X(n)=\widehat d_X(n)-d_X(n)\ge0.}
\tag{L-23701.12}
\]

Then

\[
q_X(n)=n
\quad\Longleftrightarrow\quad
\ell_X(n)=0.
\]

If the diagonal blocks at every stage, the greedy construction equals the
unique triangular inverse and proves full Carry Saturation. The aggregate
proposal below does not require that stronger statement.

The complete finite proof object for one endpoint is

```text
X
all beta_(nq)
all directed w_X(q) intervals
all residual rows rho_X^(n)
all blockers q_X(n)
all coefficients d_X(n)
all slacks w_X-Bd_X
```

and can be replayed without a linear-programming solver.

## 6. Prime-ramp consequence

Let

\[
\mathcal P(X)
=
\sum_{q=p^k\le X}
\frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\tag{L-23701.13}
\]

Since every von Mangoldt coefficient is nonnegative, (L-23701.4) and
(L-23701.9) imply

\[
\begin{aligned}
\mathcal P(X)
&\ge
\sum_{q=p^k\le X}
\Lambda(q)
\sum_{n=q}^X d_X(n)\beta_{nq}\\
&=
\boxed{
\sum_{n=2}^X d_X(n)G_n.}
\end{aligned}
\tag{L-23701.14}
\]

Thus the finite greedy object is already a rigorous positive certificate for a
prime-ramp lower bound. No Möbius sign, zero, contour, or operator estimate is
used in this step.

## 7. Why this is a genuine weakening

The exact inverse asks for

\[
B_Xc_X=w_X,
\qquad c_X\ge0.
\]

The greedy theorem asks only for an explicitly generated vector in the larger
feasible cone

\[
B_Xd_X\le w_X,
\qquad d_X\ge0.
\]

For RH it is enough that the greedy vector retain the sharp leading entropy
mass. Pointwise positivity of every exact inverse coefficient is not logically
necessary.

## 8. Proof boundary

Closed exactly:

- the average-carry matrix;
- the Kummer/Legendre prime decomposition;
- the backward minimum-ratio algorithm;
- nonnegativity of every greedy coefficient;
- feasibility against every prime-power constraint;
- the positive prime-ramp lower bound.

Open:

- an asymptotically sharp lower bound for the greedy entropy mass;
- a sufficiently small blocker defect;
- RH.