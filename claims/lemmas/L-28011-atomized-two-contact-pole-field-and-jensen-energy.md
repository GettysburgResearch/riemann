# L-28011 — Atomized two-contact pole field and Jensen energy

Claim ID: `L-28011`  
Title: The dyadic two-contact Dirichlet system gives a pole-preserving atomized field whose physical normal energy is exactly its finite carry Gram and one generalized-Chebyshev Jensen defect  
Status: **PROPOSED COMPLETE EXACT ANALYTIC/FINITE THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28005`, `L-28006`; PR #297 `L-29001/L-29004` methodology  
Scope: exact source/field/energy identification and pole criterion; no energy bound or RH claim

## 1. Atomized carry window

For real `x>=1` and `0<=theta<=1`, put

\[
 C(x,\theta)
 =\lfloor x\rfloor
  -\lfloor\theta x\rfloor
  -\lfloor(1-\theta)x\rfloor
 \in\{0,1\}.
\tag{L-28011.1}
\]

In logarithmic coordinates define

\[
 H_\theta(u)=e^{-u/2}C(e^u,\theta)\mathbf1_{u\ge0}.
\tag{L-28011.2}
\]

For

\[
 s=z+\frac12,
 \qquad
 N_\theta(s)={1-\theta^s-(1-\theta)^s\over s},
\]

one has initially in the absolute half-plane and then by continuation

\[
 \boxed{\widehat H_\theta(z)=\zeta(s)N_\theta(s).}
\tag{L-28011.3}
\]

## 2. The exact pole-preserving source

Retain

\[
 B_2(s)={1-2^{-s}\over\zeta(s)},
 \qquad
 A_2(s)={\zeta(s)\over1-2^{-s}},
\]

and its generalized-prime series

\[
 L_2(s)=-{A_2'\over A_2}(s)
       =\sum_{m\ge1}{\Lambda_2(m)\over m^s},
\]

where

\[
 \Lambda_2(m)=\Lambda(m)+(\log2)\mathbf1_{m=2^r}\ge0.
\tag{L-28011.4}
\]

Let `beta_(b2)` be the normalized atomic measure with coefficients
`b_2(n)/sqrt(n)`, and let `lambda_2` be the normalized generalized-prime
measure with coefficients `Lambda_2(m)/sqrt(m)`.  Define

\[
 \boxed{
 \mathfrak P_{2,\theta}
 =\lambda_2*\beta_{b_2}*H_\theta.
 }
\tag{L-28011.5}
\]

Its transform is

\[
 \boxed{
 \widehat{\mathfrak P_{2,\theta}}(z)
 =(1-2^{-s})N_\theta(s)L_2(s).
 }
\tag{L-28011.6}

Since

\[
 L_2(s)=-{\zeta'\over\zeta}(s)
        +{(\log2)2^{-s}\over1-2^{-s}},
\]

every nontrivial zeta zero remains an uncancelled pole.  The finite factor
`1-2^-s` has zeros only on `Re(s)=0`.

At a zero `rho` of multiplicity `m_rho`, the pole-vector residue is

\[
 \boxed{
 -m_\rho(1-2^{-\rho})N_\theta(\rho).
 }
\tag{L-28011.7}

For every fixed balanced interval `[eta,1-eta]`, `0<eta<1/2`, its squared
`theta` norm is strictly positive: `N_theta(rho)` cannot vanish identically on
an interval unless `rho=1`.

## 3. Exact finite two-contact field

For real `X>=1` and integer source scale `m`, define

\[
 \boxed{
 Y_{X,m}(\theta)
 =\sum_{k\le X/m}b_2(k)
   C\!\left({X\over mk},\theta\right).
 }
\tag{L-28011.8}

The divisor-prefix collapse `1*b_2=epsilon-delta_2` gives

\[
 \boxed{
 \begin{aligned}
 Y_{X,m}(\theta)
 ={}&\mathbf1_{m\le X<2m}\\
 &-\mathbf1_{m\le\theta X<2m}
 -\mathbf1_{m\le(1-\theta)X<2m}.
 \end{aligned}}
\tag{L-28011.9}

Finite convolution in (L-28011.5) therefore yields the exact physical field

\[
 \boxed{
 \mathfrak P_{2,\theta}(\log X)
 ={1\over\sqrt X}
  \sum_{m\le X}\Lambda_2(m)Y_{X,m}(\theta).
 }
\tag{L-28011.10}

No Fourier inversion, asymptotic limit, or unknown source map occurs.

## 4. Generalized-Chebyshev Jensen defect

Put

\[
 \Psi_2(y)=\sum_{m\le y}\Lambda_2(m)
\]

and

\[
 \boxed{
 A_2^{\rm Ch}(y)=\Psi_2(y)-\Psi_2(y/2).
 }
\tag{L-28011.11}

The box formula (L-28011.9) gives

\[
 \boxed{
 \sqrt X\,\mathfrak P_{2,\theta}(\log X)
 =A_2^{\rm Ch}(X)
  -A_2^{\rm Ch}(\theta X)
  -A_2^{\rm Ch}((1-\theta)X).
 }
\tag{L-28011.12}

The linear density cancels identically: replacing `Psi_2(y)` by `y` makes
`A_2^Ch(y)=y/2`, whose Jensen defect is zero.

Thus the field is a centered additive-stability defect of one explicit
summatory generalized-prime function.

## 5. Exact normal Gram

For `0<eta<1/2`, define the block energy

\[
 \mathscr E_{2,\eta}(J)
 =\int_J^{J+1}\int_\eta^{1-\eta}
  |\mathfrak P_{2,\theta}(t)|^2d\theta dt.
\tag{L-28011.13}

At fixed `X=e^t`, equation (L-28011.10) gives

\[
 \boxed{
 \begin{aligned}
 &\int_\eta^{1-\eta}
 |\mathfrak P_{2,\theta}(\log X)|^2d\theta\\
 &\qquad={1\over X}
 \sum_{m,n\le X}\Lambda_2(m)\Lambda_2(n)
 \mathcal K_{2,\eta,X}(m,n),
 \end{aligned}}
\tag{L-28011.14}

where

\[
 \boxed{
 \mathcal K_{2,\eta,X}(m,n)
 =\int_\eta^{1-\eta}
   Y_{X,m}(\theta)Y_{X,n}(\theta)d\theta
 \succeq0.
 }
\tag{L-28011.15}

Every entry is a finite piecewise-rational integral with breakpoints among

\[
 {m/X,\;2m/X,\;1-m/X,\;1-2m/X}.
\]

Hence the independent-frequency physical normal matrix is literally the finite
two-contact carry Gram.  The formerly open physical-to-carry transference is
absent for this atomized source.

## 6. One-dimensional energy identity

Define

\[
 \mathcal J_2(X)
 =\int_0^1
 |A_2^{\rm Ch}(X)
  -A_2^{\rm Ch}(u)
  -A_2^{\rm Ch}(X-u)|^2{du\over X}.
\tag{L-28011.16}

Equivalently, after `u=theta X`, this is the full carry-position square.
Writing

\[
 I_2(X)=\int_0^XA_2^{\rm Ch}(u)du,
 \qquad
 J_2(X)=\int_0^X|A_2^{\rm Ch}(u)|^2du,
\]

and

\[
 (A_2^{\rm Ch}*A_2^{\rm Ch})(X)
 =\int_0^XA_2^{\rm Ch}(u)A_2^{\rm Ch}(X-u)du,
\]

expansion gives

\[
 \boxed{
 \begin{aligned}
 \mathcal J_2(X)
 ={}&|A_2^{\rm Ch}(X)|^2
 -{4A_2^{\rm Ch}(X)\over X}I_2(X)\\
 &+{2\over X}J_2(X)
 +{2\over X}(A_2^{\rm Ch}*A_2^{\rm Ch})(X).
 \end{aligned}}
\tag{L-28011.17}

The four large linear-density terms cancel only in this recombined expression.

## 7. Vector-valued pole criterion

The exact source field satisfies

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathscr E_{2,\eta}(J)=e^{o(J)}
 }
\tag{L-28011.18}

for any fixed `eta in (0,1/2)`.

Under RH, the standard square-root prime-error bound gives the stated local
energy estimate.  Conversely, subexponential block energy makes the
`L^2([eta,1-eta])`-valued Laplace transform holomorphic in `Re(z)>0`.  The pole
vector (L-28011.7) has strictly positive norm at every hypothetical zero with
`Re(rho)>1/2`, a contradiction.  Functional-equation symmetry gives RH.

This is a criterion for the exact field, not an assertion that its energy has
already been bounded.

## 8. Relationship to the reserve theorem

`L-28009/L-28010` close the pole-canceling logarithmic transverse sector of the
same `A_2,b_2,Lambda_2` Dirichlet system by an explicit source-capacity matching
and a strict generalized-prime Selberg reserve.

The field (L-28011.10) retains one additional application of the inverse source
`b_2`; that is the unweighted two-contact boundary.  The remaining recurrence
must act on this explicit carry Gram or, equivalently, on the Jensen defect
(L-28011.12).  It may not invoke an unknown physical transference.

## 9. Proof boundary

Closed exactly or by the standard vector-valued Laplace continuation argument:

- the pole-preserving atomized source field;
- its finite two-contact wavelet formula;
- the generalized-Chebyshev Jensen representation;
- cancellation of the complete linear density;
- equality of the physical normal energy and the finite carry Gram;
- the full-position convolution identity;
- the vector-valued RH criterion.

Open:

- a subexponential estimate for `mathscr E_(2,eta)`;
- a lower-scale recurrence for the two-contact Jensen defect;
- the bottom-charge estimate;
- RH.
