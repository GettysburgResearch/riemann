# L-28013 — Source-convolved reflected Selberg boundary identity

Claim ID: `L-28013`  
Title: Convolving both legs of the reflected Selberg identity by the exact two-contact inverse source gives the RH-sensitive physical boundary current and its localized Hermitian normal Gram exactly  
Status: **PROPOSED COMPLETE EXACT ALGEBRA/LOCALIZATION THEOREM — INDEPENDENT REVIEW REQUESTED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #302  
Dependencies: `L-28005`; PR #241 `L-9518`  
Scope: exact physical source identity; no upper estimate or RH claim

## 1. One-frequency boundary current

Let `A` be an invertible Dirichlet series with coefficient sequence `a`, inverse
`b`, and generalized von Mangoldt sequence

\[
 \Lambda=b*(a\log).
\]

Put

\[
 C=b*(a\log^2)=\Lambda\log+\Lambda*\Lambda.
\tag{L-28013.1}
\]

The source-convolved logarithmic derivative is

\[
 \boxed{q=b*\Lambda=-b\log.}
\tag{L-28013.2}
\]

The second equality follows by applying the logarithmic derivation to
`b*a=epsilon`.

A second application of the derivation gives the exact one-frequency boundary
Selberg equation

\[
 \boxed{
 b*C=q\log+2q*\Lambda.
 }
\tag{L-28013.3}
\]

Indeed, writing `D f=f log`,

\[
 Dq=D(b*\Lambda)
 =(Db)*\Lambda+b*(D\Lambda)
 =-q*\Lambda+b*(C-\Lambda*\Lambda)
 =b*C-2q*\Lambda.
\]

For the two-contact system

\[
 A=A_2={\zeta\over1-2^{-s}},
 \qquad b=b_2,
\]

one has

\[
 \boxed{
 q_2=b_2*\Lambda_2=-b_2\log.
 }
\tag{L-28013.4}

Its Dirichlet series is `B_2(s)L_2(s)=B_2'(s)`, and every open-strip zeta zero
remains an uncancelled pole.

## 2. Independent reflected twists

For independent real frequencies `t,u`, twist every coefficient by

\[
 f_t(n)=f(n)n^{-it},
 \qquad
 f_{-u}(n)=f(n)n^{iu}.
\]

Let

\[
 C_t=b_t*(a_t\log^2),
 \qquad
 C_{-u}=b_{-u}*(a_{-u}\log^2),
\]

and let `C_(t,-u)` be the Selberg coefficient sequence of the product
`A_t A_(-u)`.  PR #241 `L-9518` proves

\[
 \boxed{
 C_{t,-u}-C_t-C_{-u}
 =2\Lambda_t*\Lambda_{-u}.
 }
\tag{L-28013.5}

Convolve the complete identity by `b_t*b_(-u)`. Associativity gives

\[
 \boxed{
 \begin{aligned}
 &(b_t*b_{-u})*C_{t,-u}
 -(b_t*b_{-u})*C_t
 -(b_t*b_{-u})*C_{-u}\\
 &\qquad=2q_t*q_{-u},
 \end{aligned}}
\tag{L-28013.6}

where

\[
 q_t=b_t*\Lambda_t,
 \qquad
 q_{-u}=b_{-u}*\Lambda_{-u}.
\]

This is the exact reflected Selberg identity for the **physical inverse-source
current**, not for the pole-canceling generalized-prime profile.

On the diagonal `u=t`, the right side is the coefficient system whose Dirichlet
series is

\[
 2|B_2(\sigma+it)L_2(\sigma+it)|^2.
\tag{L-28013.7}

## 3. Localized physical block

Let `H` be a real compact safe window and let

\[
 \mathcal Q_{2,H}(x)
 =\sum_{n\ge1}{q_2(n)\over\sqrt n}H(x-\log n).
\tag{L-28013.8}

For `alpha>1/2`, its Fourier transform is

\[
 \widehat H(\alpha+it)
 B_2\!\left(\frac12+\alpha+it\right)
 L_2\!\left(\frac12+\alpha+it\right).
\]

Apply the independent-frequency block kernel

\[
 \Phi_{J,\alpha}(t-u)
 =\int_J^{J+1}e^{2\alpha x}e^{i(t-u)x}dx.
\]

The double-Fourier calculation of `L-9518`, now using (L-28013.6), gives

\[
 \boxed{
 \begin{aligned}
 2\int_J^{J+1}|\mathcal Q_{2,H}(x)|^2dx
 ={}&{1\over(2\pi)^2}
 \iint\widehat H(\alpha+it)
       \widehat H(\alpha-iu)\\
 &\times\Phi_{J,\alpha}(t-u)
 \mathcal C^{\rm bdry}_{t,u}(\sigma)
 \,dt\,du,
 \end{aligned}}
\tag{L-28013.9)

where

\[
 \boxed{
 \mathcal C^{\rm bdry}_{t,u}
 =(b_t*b_{-u})*
  (C_{t,-u}-C_t-C_{-u}).
 }
\tag{L-28013.10)

Equivalently, expanding the finite arithmetic block gives

\[
 \boxed{
 \int_J^{J+1}|\mathcal Q_{2,H}(x)|^2dx
 =\sum_{m,n}{q_2(m)q_2(n)\over\sqrt{mn}}
 K_J^H(\log m,\log n).
 }
\tag{L-28013.11)

Every source convolution and every independent-frequency cross term is retained.
The parameter `alpha` disappears from the finite arithmetic identity.

## 4. Atomized carry specialization

Choose the atomized carry-position window `H_theta` of `L-28011`.  Then the
finite physical field is

\[
 \mathfrak P_{2,\theta}(\log X)
 ={1\over\sqrt X}
 \sum_{m\le X}\Lambda_2(m)Y_{X,m}(\theta)
 ={1\over\sqrt X}
 \sum_{q\le X}q_2(q)C(X/q,\theta).
\tag{L-28013.12)

Thus (L-28013.9)--(L-28013.11) specialize to the exact finite two-contact carry
Gram `L-28011.14`.  The physical/carry identification and the reflected
Selberg identity now concern the identical coefficient sequence `q_2`.

## 5. Source decomposition of the left side

Each individual term on the left of (L-28013.6) retains a distinct role:

```text
product Selberg source convolved on both legs
    -> complete coupled forcing;

individual source-convolved Selberg terms
    -> transverse logarithmic sectors
    -> source-capacity matching and reserve L-28009/L-28010;

unit/unweighted source excluded by logarithmic moments
    -> exact two-contact boundary L-28005/L-28007.
```

No term may be deleted before the subtraction.  In particular, generalized-prime
positivity alone does not sign the unweighted boundary, while the boundary may
not be counted again inside the transverse reserve.

## 6. Consequence for RTCT/CISR

The formerly open statement

```text
construct the physical source map to the two-contact carry Gram
```

is closed by (L-28013.6)--(L-28013.12).  The complete source map is convolution
by `b_t*b_(-u)` in the reflected coefficient identity, and its finite carry
realization is `Y_(X,m)(theta)`.

Combined with `L-28012`, the balanced interior of the physical block is already
controlled by the explicit transverse reserve.  The only remaining estimate is
the source-convolved product/boundary return: prove that the unweighted
endpoint coordinate in (L-28013.6) routes to strict lower scale with
subpolynomial loss.

## 7. Proof boundary

Closed exactly:

- the one-frequency source-boundary Selberg equation;
- the independent-frequency source-convolved reflected identity;
- the exact Hermitian physical current;
- the double-Fourier unit-block localization;
- recovery of the finite arithmetic normal Gram;
- specialization to the atomized two-contact carry field;
- the complete source-term disposition.

Open:

- a strict lower-scale estimate for the source-convolved product/boundary term;
- a subpower bottom-charge recurrence;
- RH.
