# T-27303 — Squarefree composite collector proposal for RH

Claim ID: `T-27303`  
Title: A squarefree collector lift of the parabolic ordinary-prime residual implies the Riemann Hypothesis  
Status: **FULL ELEMENTARY PROPOSAL — `SCL` OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: `R-27301/R-27302`; `L-27301`--`L-27304`; PR #248 `L-24517/L-24520`; PR #265 `L-26202`; inherited square-screw/Landau transfer

## 1. Exact starting point

The parabolic benchmark satisfies

\[
b_X^{(0)}(m)\ge0
\]

and its ordinary-prime objective obeys

\[
\boxed{
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
}
\tag{T-27303.1}
\]

`L-27301` proves that ordinary-prime feasibility alone has zero affine charge.
`R-27302` shows why prime-to-prime blocks are nevertheless insufficient for the
sharp objective: the full ordinary-prime residual has positive density drift
of proposed size

\[
4(1-\gamma)\frac{\sqrt X}{\log^2X}.
\tag{T-27303.2}
\]

Thus the final repair must compress ordinary-prime incidence rather than merely
move it one-for-one.

## 2. Squarefree Collector Lift theorem (`SCL`)

For every sufficiently large \(X\), construct nonnegative masses

\[
t_{A,B}\ge0
\]

on ordered squarefree pairs

\[
1\le A<B\le X
\]

such that, with

\[
h_m
=
\sum_{A<B}t_{A,B}\mathbf1_{A<m\le B},
\tag{T-27303.3}
\]

one has

\[
\boxed{
 r_X(p)
 +
 \sum_{A<B}t_{A,B}
 \left(\mathbf1_{p\mid B}-\mathbf1_{p\mid A}\right)
 \le0
 \qquad(p\le X).
}
\tag{SCL}
\]

No endpoint in the source is allowed to contain a squared prime factor.

## 3. Exact finite consequences

`L-27304` gives automatically

\[
h_m\ge0,
\tag{T-27303.4}
\]

\[
\boxed{
v_{p^a}(h)=0\qquad(a\ge2),}
\tag{T-27303.5}
\]

and

\[
\boxed{
J_{\mathbb P,X}(h)
=J_X(h)
=
\sum_{A<B}t_{A,B}\log(B/A)
\ge0.
}
\tag{T-27303.6}
\]

Therefore

\[
b_X=b_X^{(0)}+h
\]

is coordinatewise nonnegative, every ordinary-prime constraint is feasible,
and its ordinary-prime objective is no smaller than the parabolic benchmark.

The exact prime dual gives

\[
\boxed{
\sum_{p\le X}
\frac{\log p}{\sqrt p}\log\frac Xp
\ge4\sqrt X-O(\log^2X).
}
\tag{T-27303.7}
\]

The proper-prime-power ramp contributes only \(O(\log^2X)\), so the complete
prime-power ramp has the same sharp lower bound.

## 4. RH transfer

At \(X=N^2\), the source-pinned square-screw identity converts
(T-27303.7) into a polylogarithmic upper envelope for the screw function.
The inherited interpolation estimate extends it from square samples, and the
upper-envelope Landau one-sign theorem excludes every zeta zero with real part
greater than \(1/2\). Functional-equation symmetry gives

\[
\boxed{\mathrm{SCL}\Longrightarrow\mathrm{RH}.}
\tag{T-27303.8}
\]

## 5. Exact dual acceptance statement

For \(y_p\ge0\), define

\[
Y_y(n)=\sum_{p\mid n}y_p.
\]

By finite Farkas duality, SCL is equivalent to

\[
\boxed{
\sum_{p\le X}y_pr_X(p)\le0
}
\tag{T-27303.9}
\]

for every nonnegative prime vector satisfying

\[
\boxed{
Y_y(A)\le Y_y(B)
\qquad
\text{for all squarefree }1\le A<B\le X.
}
\tag{T-27303.10}
\]

This is one finite elementary inequality. The logarithmic vector
\(y_p=\log p\) belongs to the dual cone and produces the prime-ramp deficit,
so the theorem retains the complete RH burden.

## 6. Proposed route to the cut inequalities

The repository now supplies three pieces that a proof should combine.

### Continuum order

PR #265 proves that every upper tail of the continuum parabolic defect is
nonpositive. Thus defect is transportable to larger scale before prime
sampling.

### Prime-density correction

`R-27302` identifies the first lost term under prime sampling:

\[
4(1-\gamma)\frac{\sqrt X}{\log^2X}.
\]

This determines the exact incidence compression the collector family must
supply.

### Squarefree hypergraph

A collector with \(\omega(A)>\omega(B)\) reduces total prime incidence by

\[
t_{A,B}(\omega(A)-\omega(B))
\]

while increasing the objective by \(t_{A,B}\log(B/A)\).  The intended proof is
a source-specific Hall/Strassen transport on this squarefree divisibility
hypergraph, with bounded small-prime helper reservoirs and exact matching of
every macroscopic prime row.

The proof must establish all squarefree-monotone dual cuts simultaneously; a
mere count of available collectors is insufficient.

## 7. Reviewer-first rejection conditions

Reject a claimed completion if it:

1. uses an endpoint divisible by a proper prime power while claiming neutrality;
2. changes a prime row not accounted for by endpoint incidence;
3. takes absolute values before the squarefree collector family is recombined;
4. proves only total incidence compression, not every individual prime
   constraint;
5. ignores the positive density drift in `R-27302`;
6. omits the logarithmic dual ray;
7. replaces the continuum tail coupling by a finite-prime statement without a
   proof-grade discretization;
8. imports the rejected prime-only `PTC` bound.

## 8. Status

```text
ordinary-prime feasibility                 PROPOSED COMPLETE
prime-to-prime greedy algebra              RETAINED EXACT
prime-only subpower PTC                    PROPOSED REFUTED
squarefree collector algebra               PROPOSED COMPLETE EXACT
squarefree collector dual                  PROPOSED COMPLETE EXACT
all-scale SCL                              OPEN / RH-BEARING
SCL -> sharp prime ramp -> RH              PROPOSED COMPLETE
Riemann Hypothesis                         UNPROVED
```
