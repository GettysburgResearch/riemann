# L-94201 — Native score optimization splits exactly into an arithmetic gap and a nonnegative packing slack

Claim ID: `L-94201`
Status: **PROVED EXACT SEPARATION THEOREM**
Created: 2026-08-16
Depends on: `L-94200`; the definitions of \(J_\Lambda,P_\Lambda,F_\Lambda\)
RH status: **unproved**

Define

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X).
\]

For every finite row \(d\), `L-94200` gives

\[
P_\Lambda(X)-\mathcal H(d)
=\langle Y_4,\Omega_X-\Xi_d\rangle.
\]

Hence

\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
=
F_\Lambda(X)
+
\langle Y_4,\Omega_X-\Xi_d\rangle.
}
\tag{L-94201.1}
\]

If \(d\) is native-detail feasible,

\[
\Xi_d(q)\le\Omega_X(q)\quad(q\ge2),
\]

then \(Y_4(q)\ge0\) gives the packing slack

\[
\mathfrak W_X(d)
:=
\langle Y_4,\Omega_X-\Xi_d\rangle
\ge0.
\tag{L-94201.2}
\]

Consequently

\[
\boxed{
J_\Lambda(X)-\mathcal H(d)
=F_\Lambda(X)+\mathfrak W_X(d)
\ge F_\Lambda(X).
}
\tag{L-94201.3}
\]

This is the exact optimization firewall: the positive physical cone may reduce
\(\mathfrak W_X(d)\), but it cannot subtract from \(F_\Lambda(X)\).

Let \(\mathcal C_X\) denote any nonempty family of native-feasible rows and put

\[
\mathfrak W_X^{\min}
=\inf_{d\in\mathcal C_X}\mathfrak W_X(d).
\]

Since \(F_\Lambda(X)\) is independent of \(d\),

\[
\boxed{
\inf_{d\in\mathcal C_X}
\bigl[J_\Lambda(X)-\mathcal H(d)\bigr]
=
F_\Lambda(X)+\mathfrak W_X^{\min}.
}
\tag{L-94201.4}
\]

In particular, exact physical saturation \(\mathfrak W_X(d)=0\) leaves

\[
J_\Lambda(X)-\mathcal H(d)=F_\Lambda(X)
\]

rather than proving a smaller arithmetic estimate.

## Consequences

1. A theorem \(\mathfrak W_X(d_X)=o(\log^2X)\) gives only
   \[
   J_\Lambda(X)-\mathcal H(d_X)
   =F_\Lambda(X)+o(\log^2X).
   \]
2. A packing-only argument cannot establish the required upper bound unless it
   separately controls \(F_\Lambda\).
3. The finite physical compiler remains useful as a feasibility theorem, but
   the conclusion-producing producer is arithmetic.

```text
physical cone feasibility                    independent finite problem
minimum physical slack                       nonnegative
complete arithmetic gap F_Lambda             unchanged by packing
packing-only RH closure                      impossible from slack alone
Riemann Hypothesis                           unproved
```
