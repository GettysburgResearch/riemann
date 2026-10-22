# L-90902 — Quantitative detection of a negative trace-class eigenvalue

Claim ID: `L-90902`  
Status: **PROPOSED COMPLETE ABSTRACT THEOREM**  
Created: 2026-08-11  
Scope: explicit shifted-Hankel degree, heat time, and finite-section stability bounds

Let \(A\) be a self-adjoint trace-class operator.  Suppose \(-\eta<0\) is an eigenvalue.  Put

\[
 R_+=\|A_+\|,
 \qquad
 M_+=\operatorname{tr}A_+.
\]

## 1. Chebyshev selector and a failing Hankel matrix

Assume \(R_+>0\).  Define

\[
 p_d(x)=
 \frac{T_d(2x/R_+-1)}
 {T_d(-1-2\eta/R_+)},
\tag{L-90902.1}
\]

where \(T_d\) is the Chebyshev polynomial.  Then

\[
 p_d(-\eta)=1,
 \qquad
 \sup_{0\le x\le R_+}|p_d(x)|
 \le\frac1{T_d(1+2\eta/R_+)}.
\tag{L-90902.2}
\]

All other negative eigenvalues only decrease the shifted moment quadratic, while the positive spectrum contributes at most \(M_+/T_d^2\).  Hence

\[
 \boxed{
 \operatorname{tr}\big[A|p_d(A)|^2\big]
 \le-\eta+
 \frac{M_+}{T_d(1+2\eta/R_+)^2}.
 }
\tag{L-90902.3}
\]

Consequently the shifted-Hankel matrix

\[
 H_d=(\operatorname{tr}A^{i+j+1})_{0\le i,j\le d}
\]

fails to be positive semidefinite as soon as

\[
 \boxed{
 d>
 \frac{\operatorname{arcosh}\sqrt{M_+/\eta}}
 {\operatorname{arcosh}(1+2\eta/R_+)}.
 }
\tag{L-90902.4}
\]

If \(M_+\le\eta\), degree zero already works.  In the shallow regime \(\eta\ll R_+\), the sufficient degree is

\[
 d=O\!\left(
 \sqrt{\frac{R_+}{\eta}}
 \log\left(2+\frac{M_+}{\eta}\right)
 \right).
\tag{L-90902.5}
\]

## 2. Explicit heat time

For

\[
 \Theta_A(\beta)=\operatorname{tr}(e^{-\beta A}-I),
\]

one has

\[
 \boxed{
 \Theta_A(\beta)
 \ge e^{\beta\eta}-1-\beta M_+.
 }
\tag{L-90902.6}
\]

Indeed, the selected negative eigenvalue gives \(e^{\beta\eta}-1\), every other negative eigenvalue is favorable, and \(e^{-x}-1\ge-x\) on \(x\ge0\).

Writing \(r=M_+/\eta\), take

\[
 \boxed{
 \beta_*=\frac2\eta\log(1+r).
 }
\tag{L-90902.7}
\]

Then

\[
 \Theta_A(\beta_*)
 \ge r\,[r+2-2\log(1+r)]>0.
\tag{L-90902.8}
\]

## 3. Xi-cardinal insertion

If a vector \(v\) satisfies

\[
 \langle Av,v\rangle=-2m,
 \qquad
 \|v\|^2=C,
\]

then the min--max principle gives a negative eigenvalue of magnitude

\[
 \eta\ge\eta_0:=\frac{2m}{C}.
\tag{L-90902.9}
\]

Thus (L-90902.4) and (L-90902.7) become completely explicit once an upper bound for \(\|A\|_1\) and the Xi-cardinal coefficient cost \(C\) are available.

## 4. Stability under finite prime and Galerkin truncation

For self-adjoint \(A,B\), Duhamel's formula gives

\[
 \boxed{
 |\Theta_A(\beta)-\Theta_B(\beta)|
 \le
 \beta e^{\beta\max(\|A\|,\|B\|)}
 \|A-B\|_1.
 }
\tag{L-90902.10}
\]

For a fixed polynomial \(p\), the map

\[
 A\mapsto\operatorname{tr}[A|p(A)|^2]
\]

is continuous in trace norm on operator-norm bounded sets.  Therefore every strict negative Hankel quadratic or strict positive heat witness persists after a sufficiently accurate finite prime cutoff and finite Galerkin projection.

These bounds turn the qualitative finite-witness theorem of PR #373 into an explicit adaptive complexity estimate.  They do not establish that any Riemann-data witness is negative.
