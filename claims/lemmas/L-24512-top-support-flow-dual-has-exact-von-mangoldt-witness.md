# L-24512 — The top-support flow dual has the exact von Mangoldt witness

Claim ID: `L-24512`  
Status: `PROPOSED COMPLETE — exact finite LP duality`  
Scope: circularity firewall for signed adjacent-flow constructions  
Issue: #245  
Depends on: `L-24502`, `L-24508`

Fix any set of flow indices

\[
\mathcal J\subseteq\{2,\ldots,X-1\}
\]

and define

\[
A(q,j)=
\mathbf1_{q\mid j+1}
-2\mathbf1_{q\mid j}
+\mathbf1_{q\mid j-1},
\]

\[
c_j=\log\frac{j^2}{j^2-1}>0.
\]

Let

\[
r_q=v_q(b_X^{(0)})-w_X(q)
\qquad(q=p^a\le X).
\]

Consider the nonnegative-flow linear program

\[
\begin{aligned}
\text{minimize }&\sum_{j\in\mathcal J}c_jF_j,\\
\text{subject to }&r_q+\sum_{j\in\mathcal J}A(q,j)F_j\le0,\\
&F_j\ge0.
\end{aligned}
\tag{L-24512.1}
\]

## 1. Exact dual

Its dual is

\[
\begin{aligned}
\text{maximize }&\sum_qr_qy_q,\\
\text{subject to }&-\sum_qA(q,j)y_q\le c_j
\quad(j\in\mathcal J),\\
&y_q\ge0.
\end{aligned}
\tag{L-24512.2}
\]

## 2. Von Mangoldt saturation

Choose

\[
\boxed{y_q=\Lambda(q).}
\tag{L-24512.3}
\]

Then, using

\[
\sum_{q=p^a\mid n}\Lambda(q)=\log n,
\]

one has for every `j`

\[
\begin{aligned}
-\sum_qA(q,j)\Lambda(q)
&=2\log j-\log(j-1)-\log(j+1)\\
&=\boxed{\log\frac{j^2}{j^2-1}=c_j.}
\end{aligned}
\tag{L-24512.4}
\]

Thus the von Mangoldt vector is dual feasible and saturates **every** flow coordinate, independently of the chosen support `J`.

Its dual objective is

\[
\boxed{
\sum_q\Lambda(q)r_q
=J_X(b_X^{(0)})-S_X.}
\tag{L-24512.5}
\]

Consequently every feasible nonnegative adjacent flow satisfies

\[
\boxed{
\sum_{j\in\mathcal J}c_jF_j
\ge J_X(b_X^{(0)})-S_X.}
\tag{L-24512.6}
\]

If equality holds, the corrected residual has zero von-Mangoldt weighted slack.

## 3. Meaning of tiny top-half LP costs

Floating top-half flow reconnaissance on PR #254 finds very small costs. Equation (L-24512.6) shows that this is not independent evidence for a cheap universal transport mechanism: the optimum is constrained below by the exact RH-bearing prime-ramp discrepancy.

A proof that the top-half optimum is `X^o(1)` would already prove

\[
S_X\ge J_X(b_X^{(0)})-X^{o(1)},
\]

which is the desired prime-ramp theorem.

The high dimensionality of the flow cone, local half-scale descent, or generic LP feasibility cannot by itself bound the cost. The source-specific scalar must enter.

## 4. Signed flows

Allowing unrestricted signs changes the dual equality constraints but does not remove the witness: (L-24512.4) still holds identically. For any signed flow that makes all residuals nonpositive,

\[
\sum_jc_jF_j
\ge J_X(b_X^{(0)})-S_X
\]

follows directly by multiplying the final residual inequalities by `Lambda(q)`.

## Review boundary

This lemma does not refute signed transport. It proves that its sharp cost theorem is genuinely RH-bearing and may not be justified by a source-blind rank, feasibility, or local-descent argument.
