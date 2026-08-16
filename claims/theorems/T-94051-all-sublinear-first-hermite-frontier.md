# T-94051 — Q4 phase locking removes every sublinear excess above the first-Hermite constant-four frontier

Claim ID: `T-94051`  
Status: **PROPOSED COMPLETE UNCONDITIONAL POSITIVITY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `T-94050`, `L-94051`  
Scope: pointwise positivity for the filtered RH-equivalent hierarchy; the leading supercritical constant remains open

Write

\[
\ell(x)=\log\log(2+|x|).
\tag{T-94051.1}
\]

## 1. Fixed-order boundary improvement

Fix an integer \(m\ge2\) and \(\varepsilon>0\). There is an effective
\(X_{m,\varepsilon}\) such that

\[
\boxed{
\mathcal M_m(q,x)>0
}
\tag{T-94051.2}
\]

whenever \(|x|\ge X_{m,\varepsilon}\), \(q\ge1\), and

\[
\boxed{
q
 \le4\ell(x)
 +(4m-6-\varepsilon)\log(2+\ell(x)).
}
\tag{T-94051.3}
\]

### Proof

For fixed \(m\), the adverse ratio of the prime envelope to the gamma reserve is

\[
\ll_m
 {q^{3/2-m}e^{q/4}\over\log(2+|x|)}.
\tag{T-94051.4}
\]

Under (T-94051.3), its logarithm is at most

\[
-{
\varepsilon\over4}\log\ell(x)+O_m(1),
\]

which tends to \(-\infty\). The pole term is Gaussian small. \(\square\)

Thus every fixed phase-lock order crosses the old boundary by an additional
\((4m-6-o(1))\log\log\log|x|\).

## 2. An explicit growing-order corollary

For sufficiently large \(q\), put

\[
m_*(q)=\left\lfloor {q\over\log\log q}\right\rfloor.
\tag{T-94051.5}
\]

Then \(m_*(q)=o(q)\), so `T-94050` shows that the variable-order family remains
RH complete. For every fixed \(\eta<16\), there is an effective \(X_\eta\) such
that

\[
\boxed{
\mathcal M_{m_*(q)}(q,x)>0
}
\tag{T-94051.6}
\]

whenever \(|x|\ge X_\eta\) and

\[
\boxed{
q\le
4\ell(x)
+\eta\,
{\ell(x)\log\log\log(3+\ell(x))
 \over\log\log(3+\ell(x))}.
}
\tag{T-94051.7}
\]

Indeed,

\[
m_*(q)\log{q\over C_0m_*(q)}
 = (1+o(1))
 {q\log\log\log q\over\log\log q},
\tag{T-94051.8}
\]

while the gamma error \(e^{O(m_*(q))}\) is \(e^{o(\ell(x))}\).

## 3. Every prescribed sublinear excess

More generally, let \(\Delta(t)\ge0\) satisfy

\[
\Delta(t)=o(t).
\tag{T-94051.9}
\]

No monotonicity is assumed. Define its monotone upper envelope

\[
\Delta^*(Q)=\sup_{1\le t\le Q}\Delta(t).
\tag{T-94051.10}
\]

Then \(\Delta^*(Q)=o(Q)\). There is an explicit integer profile
\(m_\Delta(q)=o(q)\) such that the variable-order RH criterion is
unconditionally positive throughout

\[
\boxed{
q\le4\ell(x)+\Delta(\ell(x))
}
\tag{T-94051.11}
\]

for all sufficiently large \(|x|\).

Set \(m_\Delta(q)=0\) below a fixed effective threshold. For large \(q\), choose the least integer \(1\le m\le q/(2C_0)\) satisfying

\[
m\log{q\over C_0m}
 \ge {\Delta^*(q)\over4}+3\log q.
\tag{T-94051.12}
\]

Such a solution exists with \(m=o(q)\): the right side is \(o(q)\), while
\(m\mapsto m\log(q/(C_0m))\) reaches a positive constant multiple of \(q\)
and its least crossing is sublinear. More explicitly, for every fixed
\(0<\varepsilon<1/(2C_0)\),

\[
\varepsilon q\log{1\over C_0\varepsilon}
\gg_\varepsilon q,
\]

so the least crossing is below \(\varepsilon q\) once the right side of
(T-94051.12) is \(o(q)\).

If \(q<\ell(x)\), the first two terms of (L-94051.15) already contribute at
most \(-3\ell(x)/4\), while \(m=o(q)\); positivity follows directly. On the
remaining range \(q\ge\ell(x)\), (T-94051.11) gives

\[
{q\over4}-\ell(x)
 \le {\Delta(\ell(x))\over4}
 \le {\Delta^*(q)\over4}.
\tag{T-94051.13}
\]

Equation (T-94051.12) therefore forces the left side of (L-94051.15) to
\(-\infty\). Since \(m=o(q)\) and in the only delicate range
\(q\asymp\ell(x)\), the growing-order gamma error is also
\(e^{o(\ell(x))}\). Equations (L-94051.15)–(L-94051.16) apply.

The theorem therefore removes **every sublinear correction** to the constant
four. What remains is a genuine leading-constant problem:

\[
q=(4+\delta)\ell(x),
\qquad \delta>0\text{ fixed}.
\tag{T-94051.14}
\]

## 4. Logical boundary

This is an unconditional theorem about an RH-equivalent family, not an RH
proof. A terminal zero of fixed depth \(y\) needs a heat scale with

\[
q y^2>\ell(x)
\]

to dominate the archimedean reserve. For \(y<1/2\) fixed away from the boundary,
this requires a fixed leading constant larger than four. The phase-blind
filtering obstruction in `R-94054` shows why analytic saddle cancellation alone
cannot supply that gap.
