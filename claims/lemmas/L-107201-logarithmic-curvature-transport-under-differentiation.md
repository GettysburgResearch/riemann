# L-107201 — Logarithmic curvature has an exact derivative-flux transport

Claim ID: `L-107201`  
Status: **PROVED EXACT MEROMORPHIC IDENTITY AND CASCADE FORMULA**  
Created: 2026-08-30  
Depends on: `L-107100`, `L-107200`  
RH status: **not assumed**

Let \(f\) be a nonzero real entire function and, wherever the quotients are
defined, put

\[
r_k=\frac{f^{(k+1)}}{f^{(k)}},
\qquad
Q_k=-r_k'.
\tag{L-107201.1}
\]

## 1. One-step Riccati transport

Since

\[
f^{(k+2)}
=
(r_k'+r_k^2)f^{(k)},
\]

one has the exact meromorphic identities

\[
\boxed{
r_{k+1}
=
r_k+\frac{r_k'}{r_k}
=
r_k-\frac{Q_k}{r_k},
}
\tag{L-107201.2}
\]

and

\[
\boxed{
Q_{k+1}
=
Q_k+
\left(\frac{Q_k}{r_k}\right)'.
}
\tag{L-107201.3}
\]

Thus differentiation transports logarithmic curvature by one explicit
boundary flux.  The identity retains every zero, pole and multiplicity; it
is not an \(L^1\) estimate.

For a smooth compactly supported test function \(\chi\) whose support avoids
the declared boundary poles,

\[
\boxed{
\int\chi Q_{k+1}
=
\int\chi Q_k
-
\int\chi'\frac{Q_k}{r_k},
}
\tag{L-107201.4}
\]

with principal parts retained when the support crosses a zero of \(r_k\).

## 2. Cauchy-screened cascade

Let \(I\) be regular for \(f,f',\ldots,f^{(m)}\).  For every rung define

\[
\mathscr C_{\varepsilon,I}^{(k)}
=
\frac1\pi
\int_I
\frac{\varepsilon(Q_k)_-}{r_k^2+\varepsilon^2}\,dx.
\tag{L-107201.5}
\]

Let \(\mathcal M_k(I)\) be the sum of
\(\operatorname{ord}_c(f^{(k+1)})-1\) over the nonshared derivative zeros
appearing at rung \(k\).  Combining `L-107100` and `L-107200` gives

\[
\boxed{
\begin{aligned}
N_I(f)
={}&N_I(f^{(m)})
-\sum_{k=0}^{m-1}\mathcal M_k(I)\\
&-2\sum_{k=0}^{m-1}
  \lim_{\varepsilon\downarrow0}
  \mathscr C_{\varepsilon,I}^{(k)}
+\sum_{k=0}^{m-1}\varepsilon_I(f^{(k)}).
\end{aligned}
}
\tag{L-107201.6}
\]

Every term is explicit.  In a simple, common-zero-free exhaustion,
\(\mathcal M_k=0\), and the only interior losses are the five or \(m\)
Cauchy-screened negative-curvature layers.

## 3. Exact \(90\%\) arithmetic

For \(f=\Xi\), \(m=5\), and \(I_T=(T,2T)\), write

\[
\mathscr E_5(T)
=
\sum_{k=0}^{4}
\lim_{\varepsilon\downarrow0}
\mathscr C_{\varepsilon,I_T}^{(k)}
\tag{L-107201.7}
\]

and collect multiplicity, common-zero and regularization losses in
\(\mathscr M_5(T)\).  Then

\[
\boxed{
R_0(T,2T)
=
R_5(T,2T)
-
2\mathscr E_5(T)
-
\mathscr M_5(T)
+
O(1).
}
\tag{L-107201.8}
\]

Consequently, from any unconditional input

\[
R_5(T,2T)\ge(p_5-o(1))N(T,2T),
\]

the condition

\[
\boxed{
\limsup_{T\to\infty}
\frac{2\mathscr E_5(T)+\mathscr M_5(T)}
     {N(T,2T)}
<
p_5-\frac9{10}
}
\tag{L-107201.9}
\]

implies more than \(90\%\) of the zeros on the critical line.

At \(p_5=997/1000\), the exact allowance is \(97/1000\).  Equivalently,
in the simple regular case,

\[
\boxed{
\limsup\frac{\mathscr E_5(T)}{N(T,2T)}
<
\frac{97}{2000}.
}
\tag{L-107201.10}
\]

The alternative simple-real input \(p_5=9863/10000\) gives the exact
Cauchy-layer allowance \(863/20000\).

## Scope

Equations (L-107201.2)--(L-107201.10) are exact reductions.  They do not
prove the Xi screened-curvature bound.
