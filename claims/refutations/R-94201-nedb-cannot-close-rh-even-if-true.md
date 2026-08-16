# R-94201 — NEDB cannot close RH even if its asymptotic support statement is true

Claim ID: `R-94201`
Status: **EXACT COMPOSITION REFUTATION**
Created: 2026-08-16
Depends on: `L-94201`; PR #530 `L-94102`
RH status: **unproved**

PR #530 defines \(B_X\) as the largest positive physical detail-slack column
of its endpoint greedy. Its elementary price theorem proves that

\[
B_X=o(\log^4X)
\]

would imply

\[
\mathfrak W_X(d_X^{\rm ned})=o(\log^2X).
\]

That implication is correct at the physical-slack scope. But `L-94201` gives

\[
J_\Lambda(X)-\mathcal H(d_X^{\rm ned})
=
F_\Lambda(X)+\mathfrak W_X(d_X^{\rm ned}).
\]

Therefore NEDB yields only

\[
\boxed{
J_\Lambda(X)-\mathcal H(d_X^{\rm ned})
=
F_\Lambda(X)+o(\log^2X).
}
\tag{R-94201.1}
\]

The complete gap condition

\[
F_\Lambda(X)=o(\log^2X)
\]

is itself the RH-bearing arithmetic producer in the frozen endpoint chain.
NEDB does not prove, estimate, or cancel it.

Thus:

\[
\boxed{
\mathrm{NEDB}
\not\Longrightarrow
\mathrm{RH}
}
\]

without an independent conclusion-producing upper bound on \(F_\Lambda\).

Finite reconnaissance also shows that the support statistic is not monotone or
obviously local: macroscopic blockers occur at selected endpoints while the
weighted physical slack remains small. Those finite examples do not refute the
asymptotic NEDB statement; the exact refutation above does not need them.

```text
NEDB -> weighted physical slack small          correct
weighted physical slack = full seed loss       false
NEDB alone -> RH                               false composition
independent F_Lambda producer                  still required
Riemann Hypothesis                             unproved
```
