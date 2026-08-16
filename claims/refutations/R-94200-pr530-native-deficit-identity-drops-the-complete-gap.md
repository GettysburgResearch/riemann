# R-94200 — PR #530's native-deficit identity drops the complete arithmetic gap

Claim ID: `R-94200`
Status: **EXACT REFUTATION WITH AN ELEMENTARY ENDPOINT COUNTEREXAMPLE**
Created: 2026-08-16
Frozen target: PR #530 head `6c818a35094b978863a08bde4227d1f4ad9b65d4`
RH status: **unproved**

## 1. Refuted display

`L-94101.21` identifies

\[
J_\Lambda(X)-\mathcal H(d_X^{\rm ned})
\]

with

\[
\sum_qY_4(q)\bigl(\Omega_X(q)-\Xi_{d_X^{\rm ned}}(q)\bigr).
\]

By `L-94200`, the latter is instead

\[
P_\Lambda(X)-\mathcal H(d_X^{\rm ned}).
\]

The missing term is

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]

The correct identity is therefore

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X^{\rm ned})
=
F_\Lambda(X)
+
\sum_qY_4(q)
\bigl(\Omega_X(q)-\Xi_{d_X^{\rm ned}}(q)\bigr).
}
\tag{R-94200.1}
\]

## 2. Elementary counterexample at \(X=3\)

Take the zero row \(d=0\), which is native feasible. The false identity would
assert \(J_\Lambda(3)=P_\Lambda(3)\).

The parabolic seed is

\[
b_3(2)
=
2\sqrt2\left[
\log(3/2)-2\left(1-\sqrt{2/3}\right)
\right],
\qquad b_3(3)=0.
\]

Hence

\[
J_\Lambda(3)=b_3(2)\log2,
\]

whereas

\[
P_\Lambda(3)
=\frac{\log2}{\sqrt2}\log(3/2).
\]

Their difference is

\[
\boxed{
F_\Lambda(3)
=
\log2\left[
\frac3{\sqrt2}\log(3/2)-4\sqrt2+\frac8{\sqrt3}
\right].
}
\tag{R-94200.2}
\]

It is strictly negative by elementary rational bounds. Indeed,

\[
\log(3/2)<\frac{41}{100},\quad
\frac1{\sqrt2}<\frac{71}{100},\quad
\frac1{\sqrt3}<\frac{29}{50},\quad
\sqrt2>\frac75.
\]

Therefore the bracket in (R-94200.2) is less than

\[
3\frac{71}{100}\frac{41}{100}
-4\frac75
+8\frac{29}{50}
=
-\frac{867}{10000}.
\]

The classical inequality

\[
\log(1+x)>\frac{2x}{2+x}\qquad(x>0)
\]

gives \(\log2>2/3\), and thus

\[
\boxed{
F_\Lambda(3)<-\frac{289}{5000}<0.
}
\tag{R-94200.3}
\]

So the omitted term is not a harmless normalization constant; the claimed
identity already fails at the first nontrivial endpoint.

## 3. Scope

The refutation does **not** invalidate:

- positivity of the endpoint atoms;
- positivity of their radix-four details;
- the finite backward greedy;
- ordinary or detail feasibility.

It invalidates the conclusion-producing identification of physical slack with
the full native seed-score loss.

```text
PR #530 finite endpoint compiler             survives
PR #530 weighted physical slack              survives
PR #530 full native-deficit identity         false
NEDB as a physical-slack statement           meaningful
NEDB as an RH closure by itself              invalid
Riemann Hypothesis                           unproved
```
