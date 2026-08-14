# R-91316 — PR #464 root Hall does not directly compile to the native NRCT

Claim ID: `R-91316`  
Status: **EXACT NORMALIZATION SEPARATOR**  
Created: 2026-08-14  
Frozen inputs: PR #464 at `2eb70463f3d0ae791a9f140694d2ace7032ae864`; PR #468 at `a41f81466f85d52597c97b41505756a8860698d0`  
RH status: **unproved**

## 1. The finite root Hall algebra survives

The fixed-window score-Hall calculation on PR #464 is not refuted here. On

\[
1\le x<c_0^{-1}<54.2192,
\]

one common transport gives score equality, target subordination and nonnegative
component-row bonuses. The exact stopped-leaf counterexample remains outside
that root window and is retained as a mandatory firewall.

The issue is the packet to which the finite root identity is applied.

## 2. Native and finite-Euler packets are different

Let

\[
c_X(j)=\sum_{k\le X/j}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j)
\]

be the full Möbius row. By `L-91377`,

\[
C_{c_X}=w_X,\qquad
\Xi_{c_X}=\Omega_X,\qquad
\mathcal H(c_X)=J_\Lambda(X).
\]

Let \(P=P_{61}\), and let

\[
D_{P,X}(j)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j)
\]

be the canonical finite-Euler row. `L-91379` proves the exact rough-monoid
decomposition

\[
\boxed{
D_{P,X}
=
c_X+
\sum_{\substack{m\in\mathcal R_{67}\\m>1}}
m^{-1/2}c_{X/m}.
}
\tag{R-91316.1}
\]

Applying the linear physical maps gives

\[
\boxed{
C_{P,X}(q)
=
w_X(q)+
\sum_{\substack{m\in\mathcal R_{67}\\m>1}}
m^{-1/2}w_{X/m}(q),
}
\tag{R-91316.2}
\]

\[
\boxed{
\Theta_{P,X}(q)
=
\Omega_X(q)+
\sum_{\substack{m\in\mathcal R_{67}\\m>1}}
m^{-1/2}\Omega_{X/m}(q),
}
\tag{R-91316.3}
\]

and

\[
\boxed{
\mathcal E_P(X)
=
J_\Lambda(X)+
\sum_{\substack{m\in\mathcal R_{67}\\m>1}}
m^{-1/2}J_\Lambda(X/m).
}
\tag{R-91316.4}
\]

The second terms are the positive rough capacity and benchmark reservoir. The
corresponding native rows \(c_{X/m}\) remain signed until a physical producer is
supplied.

## 3. Exact separating coordinate

Take \(X=136\) and the ordinary column \(q=2\). The only rough integer
\(m>1\) with \(m\le X/q=68\) is \(m=67\). Therefore

\[
\boxed{
C_{P,136}(2)-w_{136}(2)
=
\frac1{\sqrt{134}}\log\frac{68}{67}>0.
}
\tag{R-91316.5}
\]

Elementary bounds give the proof-grade margin

\[
\log\frac{68}{67}>\frac1{68},
\qquad
\frac1{\sqrt{134}}>\frac1{12},
\]

and hence

\[
\boxed{
C_{P,136}(2)-w_{136}(2)>\frac1{816}.
}
\tag{R-91316.6}
\]

Thus evaluation at the ordinary coordinate \(q=2\) is an exact separating
functional between the declared finite-Euler root packet and the native
capacity cone.

## 4. Consequence for PR #464

There are only two possible readings of the global equation in `L-91673`.

### Finite-Euler reading

If the endpoint-frame Hall packet is the canonical finite-Euler packet, then
the current part plus all retained rough children has response \(C_{P,X}\), not
\(w_X\). At `(136,2)` it overdraws native capacity by more than `1/816`.
Therefore it does not satisfy `T-91314.2` unless the rough reservoir is
source-disjointly removed from current ownership and assigned exactly once to
children.

### Full-Möbius reading

If the equation is asserted literally as

\[
c_X=B_X+Z_X
\]

with \(B_X,Z_X\) coefficientwise nonnegative physical rows, then it proves
\(c_X\ge0\). This is the zero-slack native producer fenced by `R-91314`; it is
already conclusion-producing and cannot be obtained merely from the formal
positive-linear theorem `L-91674`.

Accordingly, PR #464's finite Hall algebra is valuable, but it does not by
itself instantiate the Native-Root Capacity Theorem in the normalization of
`L-91377`–`L-91379`.

## 5. Exact repair requirement

A valid compiler must output a typed identity

\[
\mathcal N_X
=
\mathcal P_X^{\rm cur}
+\sum_b\alpha_b U_b\mathcal P_b
+\mathcal S_X
\]

such that:

```text
current row is nonnegative;
children are source-disjoint;
total child target mass is <1/8;
ordinary/detail/port capacities are one-use;
S_X is explicit nonnegative native slack;
sum_q Y_4(q) S_X(q) = o(log^2 X).
```

It must not count the rough reservoir once inside `D_(P61,X)` and again through
the children.

```text
fixed-window root Hall algebra            RETAINED
direct compilation to native NRCT         SEPARATED EXACTLY
separator                                 X=136, q=2, margin >1/816
native rough-reservoir allocation         OPEN
Riemann Hypothesis                        UNPROVED
```
