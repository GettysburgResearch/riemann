# L-90702 — Exact top-inverse cone: monotonicity is sufficient but not necessary

Claim ID: `L-90702`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-32201` and the exact average-carry matrix  
Scope: top-half inversion algebra; no positivity theorem for every recursive residual and no RH conclusion

## 1. Setup

Let \(E\ge4\), \(N=\lfloor E/2\rfloor\), and let \(h(2),\ldots,h(E)\) be an arbitrary real target. Put \(h(E+1)=0\) and

\[
\Delta_q=h(q)-h(q+1).
\tag{L-90702.1}
\]

Let \(c(q)\), \(N<q\le E\), be the unique top-half coefficients solving

\[
h(q)=\sum_{n=q}^{E}c(n)\beta_{nq},
\qquad
\beta_{nq}
=\frac{a(q-1-r)}{n+1},
\quad n=aq+r,\ 0\le r<q.
\tag{L-90702.2}
\]

Define

\[
V_q=\sum_{m=q}^{E}m\Delta_m,
\qquad
S_q=\frac{V_q}{q(q-1)}.
\tag{L-90702.3}
\]

The exact inversion formula of `L-32201` is

\[
c(q)=(q+1)[S_q-S_{q+1}].
\tag{L-90702.4}
\]

## 2. Exact cone criterion

Since \(V_q=q\Delta_q+V_{q+1}\), equation (L-90702.4) becomes

\[
\boxed{
q(q-1)c(q)
=
q(q+1)\Delta_q+2V_{q+1}.
}
\tag{L-90702.5}
\]

Consequently

\[
\boxed{
c(q)\ge0
\iff
q(q+1)[h(q)-h(q+1)]
+
2\sum_{m=q+1}^{E}m[h(m)-h(m+1)]
\ge0.
}
\tag{L-90702.6}
\]

This is the exact top-inverse cone. Ordinary monotonicity, \(\Delta_m\ge0\), is a sufficient condition, but it is not necessary: one negative local difference may be paid by positive weighted variation above it.

An equivalent value form is

\[
\boxed{
q(q-1)c(q)
=
q(q+1)h(q)
-(q+1)(q-2)h(q+1)
+2\sum_{m=q+2}^{E}h(m).
}
\tag{L-90702.7}
\]

The right invariant for recursive critical-hinge work is therefore the weighted-tail expression (L-90702.6), not pointwise decrease of every exported residual.

## 3. Stable defect estimate

Write

\[
\Delta_q^-=[-\Delta_q]_+.
\]

Equation (L-90702.5) gives the quantitative sufficient condition

\[
\boxed{
V_{q+1}\ge\frac{q(q+1)}2\Delta_q^-
\quad\Longrightarrow\quad c(q)\ge0.
}
\tag{L-90702.8}
\]

This is precisely the mechanism active in the first exact recursive-monotonicity counterexample of `R-90701`: the residual increases locally, but its next inverse coefficient stays strictly positive.

## 4. Proof boundary

Closed here:

```text
exact top-inverse cone                       proved
monotonicity only sufficient                 proved
weighted-tail payment of local increases     proved
recursive preservation of this cone          open
Critical Hinge Saturation                    open / RH-bearing
RH                                            unproved
```
