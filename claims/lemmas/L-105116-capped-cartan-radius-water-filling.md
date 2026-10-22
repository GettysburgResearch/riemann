# L-105116 - Capped Cartan radius water filling

Claim ID: L-105116

Status: **PROPOSED EXACT FINITE OPTIMIZATION; XI ABSORPTION OPEN**

Created: 2026-08-23

Depends on: L-105114 for the equal-disk coefficients and L-105115 for the
safe-shell normalization

RH status: **unproved**

## 1. Exact optimization

Fix a finite nonempty index set and positive coefficients \(u_j,v_j\).
For \(0<\varepsilon_j\le1\), define

\[
\Phi(\varepsilon)=
\sum_j u_j\log\frac{2}{\varepsilon_j},
\qquad
S_{\rm nom}(\varepsilon)=\sum_jv_j\varepsilon_j.
\tag{L-105116.1}
\]

The \(u_j\) declare the scalarized reciprocal-modulus loss being optimized;
the \(v_j\) are the nominal radius costs.  Put \(U=\sum_j u_j\) and
\(V=\sum_jv_j\).

If \(R\ge V\), the unique minimizer under the closed constraint
\(S_{\rm nom}\le R\) is \(\varepsilon_j^*=1\), and

\[
\Phi^*=U\log2.
\tag{L-105116.2}
\]

If \(0<R<V\), there is a unique \(\lambda>0\) satisfying

\[
\sum_jv_j\min\left(1,\frac{u_j}{\lambda v_j}\right)=R.
\tag{L-105116.3}
\]

The unique minimizer is

\[
\boxed{
\varepsilon_j^*=\min\left(1,\frac{u_j}{\lambda v_j}\right).
}
\tag{L-105116.4}
\]

In allocated-radius variables \(s_j=v_j\varepsilon_j\), this is

\[
s_j^*=\min(v_j,u_j/\lambda).
\tag{L-105116.5}
\]

## 2. Proof and cap ordering

Up to constants independent of \(s\),

\[
\Phi=-\sum_j u_j\log s_j.
\]

This is strictly convex on the positive orthant and diverges when any
\(s_j\downarrow0\).  When \(R<V\), coordinatewise monotonicity makes the
budget active.  The KKT equations give (L-105116.4).  The function

\[
\Psi(\lambda)=\sum_j\min(v_j,u_j/\lambda)
\]

is continuous and strictly decreasing on the range relevant to \(0<R<V\),
so the multiplier and optimizer are unique.

Equivalently, order \(\rho_j=u_j/v_j\) from largest to smallest.  Indices
with \(\rho_j\ge\lambda\) are capped at one; the others receive
\(s_j=u_j/\lambda\).  Ties cause no ambiguity because both formulas agree.

## 3. Interior formula

The uncapped formula is valid when

\[
R\le\frac{U}{\max_j(u_j/v_j)},
\tag{L-105116.6}
\]

with every cap strictly inactive under strict inequality.  At equality,
one or more epsilons can equal one, but the same formula remains valid.  Then

\[
\boxed{
\varepsilon_j^*=\frac{u_jR}{v_jU},
\qquad
v_j\varepsilon_j^*=\frac{u_j}{U}R,
}
\tag{L-105116.7}
\]

and

\[
\boxed{
\Phi^*=\sum_j u_j
\log\left(\frac{2v_jU}{u_jR}\right).
}
\tag{L-105116.8}
\]

Weighted concavity of \(\log\) gives the same sharp allocation directly.
Thus nominal radius is proportional to the declared logarithmic penalty
weight, not generally equal among functions.

## 4. T-105114 specialization

For a scalarized combination of T-105114 lower-modulus exponents, take

\[
u_j=\frac{\theta_jA_j}{\beta_j},
\qquad
v_j=\frac{r_{2,j}A_j}{\beta_j},
\qquad \theta_j>0.
\tag{L-105116.9}
\]

The epsilon-independent spatial terms are added after the optimization.
In the interior regime,

\[
\varepsilon_j^*=
\frac{\theta_jR}
{r_{2,j}\sum_\ell\theta_\ell A_\ell/\beta_\ell}.
\tag{L-105116.10}
\]

For the unweighted sum \(\theta_j=1\) and common \(r_{2,j}=r_2\), all
optimal epsilons are equal:

\[
\varepsilon^*=\frac{R}{r_2\sum_\ell A_\ell/\beta_\ell}.
\tag{L-105116.11}
\]

This equality follows from the special coefficient relation
\(v_j=r_2u_j\); it is not a general equal-allocation rule.  A different
carrier objective or multiplicity weighting changes \(u_j\) and therefore
changes the optimizer.

## 5. Fixed fractional safe-shell slack

Let

\[
d=\min(\Delta_T,\Delta_\eta),
\qquad 0<\delta<1,
\qquad R_\delta=\frac{1-\delta}{2}d.
\tag{L-105116.12}
\]

Optimize under the closed nominal budget \(S_{\rm nom}\le R_\delta\).
Because the actual disk radius satisfies (S\le S_{\rm nom}\),

\[
2S\le(1-\delta)d<d,
\tag{L-105116.13}
\]

so the strict T-105115 gate holds.  Moreover,

\[
\Delta_T-2S\ge\delta\Delta_T,
\qquad
\Delta_\eta-2S\ge\delta\Delta_\eta,
\]

and hence

\[
\boxed{\kappa\le\delta^{-2}.}
\tag{L-105116.14}
\]

The exact merged projections can improve this bound.  As
\(\delta\downarrow0\), the reciprocal penalty improves but the worst-case
normalization bound diverges; as \(\delta\uparrow1\), the normalization is
benign but the optimal logarithmic penalty diverges like
\(U\log(1/(1-\delta))\).  This is an exact Pareto barrier within the
declared equal-disk, total-radius, scalarized-loss ledger.

It is not a universal obstruction: projection overlap, non-equal disks,
authenticated cancellations, or a stronger minimum-modulus theorem can
improve the ledger.  No Xi growth load, selector absorption, signed moment,
RCMV104530, or RH conclusion is proved.
