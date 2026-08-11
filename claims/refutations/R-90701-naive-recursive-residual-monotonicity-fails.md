# R-90701 — Naive recursive monotonicity of critical-hinge residuals fails

Claim ID: `R-90701`  
Status: **EXACT FINITE REFUTATION — DIRECTED RADICAL CERTIFICATE**  
Created: 2026-08-11  
Depends on: staged top-half elimination of `L-32201/L-32204`; `L-90702`  
Scope: refutes only indefinite iteration through the cone of decreasing targets; it does not refute CHS or positivity of the full inverse

## 1. The tempting induction

For

\[
h_0(q)=q^{-1/2}-T^{-1/2},
\qquad 2\le q\le T,
\]

define recursively:

1. \(E_0=T\), \(E_{j+1}=\lfloor E_j/2\rfloor\);
2. solve the exact top-half subsystem on rows \(E_{j+1}<n\le E_j\);
3. let \(h_{j+1}\) be the unused residual on \(2\le q\le E_{j+1}\).

`L-32204` proves \(h_1\ge0\), and `L-32205` proves \(h_1\) is decreasing on the top half where the second solve needs it. A natural proposed continuation is:

> every exported residual is decreasing on its own top half, so `L-32201` can be iterated indefinitely.

That statement is false.

## 2. Exact witness

Take

\[
T=894.
\]

The staged endpoints are

\[
894\longrightarrow447\longrightarrow223
\longrightarrow111\longrightarrow55.
\tag{R-90701.1}
\]

After the fourth elimination, the residual \(h_4\) on \(2\le q\le55\) satisfies

\[
\boxed{
h_4(28)-h_4(29)<0.
}
\tag{R-90701.2}
\]

The retained directed certificate evaluates the exact rational linear functional of the radicals \(q^{-1/2}\) and proves

\[
\boxed{
-4.637751038104931\times10^{-6}
<
h_4(28)-h_4(29)
<
-4.637751038104930\times10^{-6}.
}
\tag{R-90701.3}
\]

Thus \(h_4\) increases at the first pair of its next top-half range.

The certificate is not a floating recursion. The elimination matrices have rational entries. The verifier pulls the functional
\(h_4(28)-h_4(29)\) backwards through all four exact Schur/triangular elimination maps, obtaining a rational linear combination of the original values \(q^{-1/2}-894^{-1/2}\). Each reciprocal square root is enclosed by integer-square-root rational bounds at denominator \(10^{60}\).

## 3. What survives

The next inverse coefficient is nevertheless positive. The same directed pullback proves

\[
\boxed{
0.006346716962584759
<
c_5(28)
<
0.006346716962584761.
}
\tag{R-90701.4}
\]

This is exactly the distinction exposed by `L-90702`: local monotonicity fails, but the weighted upper-tail term in

\[
q(q-1)c(q)
=
q(q+1)[h(q)-h(q+1)]
+
2\sum_{m>q}m[h(m)-h(m+1)]
\]

pays the defect.

## 4. Consequence

The recursive critical-hinge programme may not use

```text
nonnegative residual
-> decreasing residual on its next top half
-> repeat L-32201 forever.
```

The first implication beyond the proved finite stages is false. The legitimate induction target is instead:

\[
\boxed{
q(q+1)\Delta_q+2V_{q+1}\ge0
}
\]

for every active row, together with a source-specific no-lower-overfill theorem after each solved band.

## 5. Exact boundary

```text
first exported residual top-half decrease       retained
indefinite residual monotonicity induction      false
fifth-stage coefficient at the witness          positive
weighted-tail top-inverse cone                  exact
full CHS / average-carry positivity              open
RH                                                unproved
```
