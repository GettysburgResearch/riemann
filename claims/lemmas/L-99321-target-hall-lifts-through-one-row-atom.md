# L-99321 — Compact Hall and causal rough splitting lift through one target-aligned row atom

Claim ID: `L-99321`  
Status: **PROPOSED COMPLETE EXACT COMMON-PARENT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99320`; compact target Hall and target-source identities at the
exact frozen scopes of PRs #620, #632, and #636  
RH status: **not assumed**

## 1. Compact finite-Euler fibre

Let \(P_{61}=\prod_{p\le61}p\). For \(1\le x<67\), define

\[
D_{61,x}(j)
=
\sum_{\substack{k\mid P_{61}\\k\le x}}
\frac{\mu(k)}{\sqrt k}Q_{x/k}(j).
\]

Using `L-99320.7` and finite Fubini,

\[
\boxed{
D_{61,x}(j)
=
\int_1^x
\eta_j(t)\,
\Phi_{61}(x/t)\frac{dt}{t},
}
\tag{L-99321.1}
\]

where

\[
\Phi_{61}(y)
=
\sum_{\substack{k\mid P_{61}\\k\le y}}
\frac{\mu(k)}{\sqrt k}T(y/k).
\tag{L-99321.2}
\]

For fixed \(t\), the bracket is exactly the compact target Hall problem at
parameter \(y=x/t<67\). The frozen directed Hall theorem supplies one target
flow with nonnegative residual target. Since \(\eta_j(t)\ge0\) is independent
of the source colour \(k\), the same flow simultaneously gives the row
identity in every \(j\):

\[
\text{signed row at }t
=
\eta_j(t)\times
\bigl(\text{matched nonnegative target current}
+\text{positive residual target}\bigr).
\tag{L-99321.3}
\]

Thus

\[
\boxed{
D_{61,x}(j)\ge0
\qquad(1\le x<67,\ j\ge2).
}
\tag{L-99321.4}
\]

This uses only target Hall. The normalized component-row profile determinants
and their source-dependent monotonicity are unnecessary.

The Hall flow changes only at finitely many activation values of \(x/t\).
Choose the canonical nested-neighbourhood flow on each cell. It is piecewise
measurable, and finite Tonelli gives one literal common-parent source.

## 2. Causal parent-minus-child current

For a prime \(p\ge67\), \(r=p^{-1/2}\), and \(Y\ge p\),

\[
Q_Y(j)-rQ_{Y/p}(j)
=
\int_1^Y
\eta_j(t)
\Bigl[
T(Y/t)
-r\mathbf1_{t\le Y/p}T(Y/(pt))
\Bigr]\frac{dt}{t}.
\tag{L-99321.5}
\]

If \(t>Y/p\), the bracket is \(T(Y/t)>0\). If \(t\le Y/p\), put
\(z=Y/(pt)\ge1\). Then

\[
\begin{aligned}
T(pz)-p^{-1/2}T(z)
&=
4\sqrt z(\sqrt p-p^{-1/2})
-3(1-p^{-1/2})\\
&\ge
\frac{(\sqrt p-1)(4\sqrt p+1)}{\sqrt p}>0.
\end{aligned}
\tag{L-99321.6}
\]

Therefore

\[
\boxed{
Q_Y(j)-p^{-1/2}Q_{Y/p}(j)>0
\quad(p\ge67,\ Y\ge p,\ j\ge2)
}
\tag{L-99321.7}
\]

whenever the row is active.

Equation (L-99321.5) is source-level: the same target difference multiplies
every row atom. Current, target, and every row use one coefficient list.

## 3. One random key for all rows

At a residual target micro-source with endpoint \(Y\), the exact causal
coefficients satisfy

\[
\alpha_i=r_i\lambda_i,\qquad
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

Cross the target source with one key \(u\in[0,1]\), and assign disjoint
intervals of lengths \(\alpha_i\mathbf1_{t\le Y_i}\) to the children. Since
every row observation is \(\eta_j(t)\) times the same target source, the single
partition gives simultaneously

\[
\alpha_i Q_{Y_i}(j)
\]

in every row. Its complement gives the exact positive current in
(L-99321.5). Repeat with a fresh key at every child. Since

\[
Y'\le Y/67+1,
\]

the tree is finite at each root.

## 4. Rank-one common-parent principle

Let \(\mathcal S\) be a finite signed target source for which the frozen
target-only Hall/causal construction gives one nonnegative labelled measure
\(\nu\). Then for every \(j\ge2\),

\[
\boxed{
\mathcal S[Q_Y(j)]
=
\int Q_Y(j)\,d\nu\ge0,
}
\tag{L-99321.8}
\]

with the same source labels and coefficients in all rows.

The component-row common-parent problem is rank one over the scalar target.
No additional row transport gate remains.

## 5. Scope firewall

This theorem does not prove the compact target Hall inequalities, the exact
root target-source identity, or the finite endpoint calibration. It proves
that once those target-only inputs are supplied, the complete row lift is
automatic and exact. Score and ordinary/radix-four capacities are outside this
fixed-row theorem.
