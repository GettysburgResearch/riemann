# L-100103 — DCE100100 is predecessor positivity, and every fixed tail retains the reciprocal-zeta obstruction

Claim ID: `L-100103`  
Status: **PROVED EXACT ALGEBRAIC/ANALYTIC IDENTIFICATION**  
Created: 2026-08-20  
Depends on: `T-100100`; the centered cubic Mellin consumer of PR #676  
RH status: **not assumed**

Let `p` be one typed future-prime label, let `p+` denote the successor state,
and retain the exact recurrence

\[
C_p(Y)=C_{p^+}(Y)-p^{-1/2}C_{p^+}(Y/p).
\tag{L-100103.1}
\]

Then

\[
\begin{aligned}
C_{p^+}(Y/p)\le\sqrt p\,C_{p^+}(Y)
&\iff
C_{p^+}(Y)-p^{-1/2}C_{p^+}(Y/p)\ge0\\
&\iff
\boxed{C_p(Y)\ge0.}
\end{aligned}
\tag{L-100103.2}

Thus `DCE100100` is not a separate Harnack estimate lying before the sign
problem. At every edge it is exactly the sign of the predecessor state written
as a ratio inequality. Requiring it at every low-prime typed state is requiring
every state produced by the backward induction to be nonnegative.

## Fixed-tail Mellin inheritance

Fix one tail state after finitely many prime labels have been removed. Its
Dirichlet source differs from the duplicate-67 source

\[
B(z)=\frac{1-67^{-z}}{\zeta(z)}
\]

by a finite product of factors of the form

\[
(1-q^{-z})^{-1},
\qquad
1-q^{-z},
\]

with the two labelled `67` occurrences recorded separately. Hence

\[
\boxed{B_p(z)=B(z)F_p(z),}
\tag{L-100103.3}

where `F_p` is holomorphic and nonzero throughout `Re z>0`; all zeros and poles
of the finite Euler factors lie on `Re z=0`.

The centered cubic kernel multiplier from PR #676 has constant numerator and
only real carrier poles. Its carrier subtraction removes the positive-real
poles, while it is nonzero at every translated nontrivial zeta zero. Therefore
any zero `rho` with `Re rho>1/2` remains a nonreal pole of the Mellin transform
of every fixed tail state.

It follows from the same one-sign Mellin--Landau theorem that

\[
\boxed{
C_p(Y)\ge0\text{ eventually for any one fixed tail }p
\quad\Longrightarrow\quad RH.
}
\tag{L-100103.4}

Accordingly, the low-prime DCE family is conclusion-bearing at each fixed-tail
interface. Kernel positivity and the terminal corridor do not prove it by
formal composition.

## Exact disposition

```text
future-prime recurrence                  proved exact
DCE edge inequality                      identical to predecessor sign
fixed finite tail preserves zeta poles   proved
fixed-tail eventual sign -> RH           proved by frozen consumer
DCE100100                                open / conclusion-bearing
Riemann Hypothesis                       unproved
```
