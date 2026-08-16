# T-94050 — Every fixed phase-locked Q4–Hermite level is an RH criterion

Claim ID: `T-94050`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-94050`; PR #379 terminal-pair argument  
Scope: criterion only; no unconditional all-parameter positivity claim

Fix an integer \(m\ge0\). Then

\[
\boxed{
\mathrm{RH}
\iff
\mathcal M_m(q,x)\ge0
\quad\text{for every }q>0,
\ x\in\mathbb R.
}
\tag{T-94050.1}
\]

The same statement remains true with positive integer \(q\) and rational
\(x\), or with any unbounded discrete heat sequence having bounded ratios.

## Proof

Under RH every centered zero is real, so every summand in (L-94050.7) is
nonnegative.

Conversely assume an off-real zero exists. The terminal-pair theorem of PR #379
provides a pair \(t\pm iy\), \(0<y<1/2\), such that after division by
\(e^{qy^2}\), all other zero contributions vanish as \(q\to\infty\).
The multiplier \(P(z-t)^{2m}\) is bounded on the closed zero strip for fixed
\(m\), while

\[
P(iy)^{2m}>0.
\]

Therefore

\[
{\mathcal M_m(q,t)\over2y^2e^{qy^2}P(iy)^{2m}}
\longrightarrow -m_{t,y}<0.
\tag{T-94050.2}
\]

For all sufficiently large \(q\), \(\mathcal M_m(q,t)<0\). Continuity supplies
a nearby rational centre and, if desired, a nearby integer heat parameter.
This contradicts the asserted positivity. \(\square\)

## Variable-order extension

Let \(m(q)\) be integer valued with

\[
m(q)=o(q).
\tag{T-94050.3}
\]

Then the variable family

\[
\mathcal M_{m(q)}(q,x)
\]

is also RH complete. Fix a terminal pair \(t\pm iy\). On the whole closed
zero strip,

\[
|P(z-t)|\le 10,
\qquad P(iy)>0.
\tag{T-94050.4}
\]

After normalising by the target amplitude, every multiplier ratio is at most

\[
\left({10\over P(iy)}\right)^{2m(q)}=e^{o(q)}.
\tag{T-94050.5}
\]

Split the nuisance zeros into a fixed bounded ordinate window and its
complement. Terminality gives a fixed strict exponent gap on the finite bounded
part. On the complement, the Gaussian exponent is at most \(-cR^2q\) after a
fixed sufficiently large cutoff \(R\), and the subquadratic zero count is
summable against that Gaussian. Multiplication by \(e^{o(q)}\) preserves both
limits. Meanwhile the target amplitude is

\[
e^{qy^2}P(iy)^{2m(q)}=e^{qy^2-o(q)}.
\tag{T-94050.6}
\]

Thus the same terminal asymptotic remains strictly negative. This
variable-order clause is used only with explicit sublinear profiles in
`T-94051`.
