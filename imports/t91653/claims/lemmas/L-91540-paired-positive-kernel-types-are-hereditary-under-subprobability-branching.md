# L-91540 — Positive paired target/score kernel types are hereditary under subprobability rough branching

Claim ID: `L-91540`  
Status: **PROVED EXACT TYPED-KERNEL BRANCHING THEOREM**  
Created: 2026-08-13  
Frozen inputs: PR `#399` at `15edbccaeedd96cfa76783713b41715d8ad7d8e5`; PR `#416` at `23aa9adc48a6c3176b799944dfbac11e665407ef`  
Depends on: positive component rows; `L-91329`; the one-prime branch formulas frozen above  
RH status: **unproved**

## 1. Paired positive kernel types

Fix an endpoint \(x\ge1\).  A **paired positive kernel type** is a tuple

\[
 \tau=(a_T,b_T,a_S,b_S,\kappa)
\]

with nonnegative coefficients such that, on its declared support \(n\le x\),

\[
 \boxed{
 T_{\tau,x}(n)
 =a_T\frac{\sqrt x}{n}-b_T\frac1{\sqrt n}\ge0,
 \qquad
 S_{\tau,x}(n)
 =a_S\frac{\sqrt x}{n}-b_S\frac1{\sqrt n}\ge0.
 }
 \tag{L-91540.1}
\]

Its exact finite-row atom is

\[
 \boxed{
 R_{\tau,x}(n;j)
 =\kappa\,n^{-1/2}Q_{x/n}(j)\ge0
 \qquad(j\ge2),
 }
 \tag{L-91540.2}
\]

with causal zero extension.  The target and score kernels need not come from the
same common coefficient measure and need not satisfy the special identity

\[
 S_{\tau,x}-T_{\tau,x}=\sqrt x/n.
\]

This is the point: the common `W_Psi/W_S` ray of `L-91343` is one member of a
larger hereditary typed cone.

For a positive finite source measure \(\nu\), put

\[
 \mathfrak T_{\tau,x}(\nu)=\sum_n\nu(n)T_{\tau,x}(n),
 \qquad
 \mathfrak S_{\tau,x}(\nu)=\sum_n\nu(n)S_{\tau,x}(n),
 \tag{L-91540.3}
\]

and define the component row by summing (L-91540.2).

## 2. Arbitrary subprobability rough children

At each source node \(n\), let \(b\) range over a finite or countable family of
labels.  Attach a scale \(p_b\ge67\) and a weight

\[
 \theta_b(n)\ge0,
 \qquad
 \theta_b(n)=0\ \text{unless }n\le x/p_b,
 \qquad
 \boxed{\sum_b\theta_b(n)\le1.}
 \tag{L-91540.4}
\]

The child measure at endpoint \(x/p_b\) is

\[
 \nu_b(n)=\theta_b(n)\nu(n)
 \tag{L-91540.5}
\]

and retains the same type label \(\tau\).

No arithmetic tensorization is being asserted.  Equation (L-91540.4) is a
positive source partition supplied upstream, for example by the least-prime
hazard telescope.

## 3. Exact positive target and score residuals

For either \(K=T_\tau\) or \(K=S_\tau\), one active child satisfies

\[
 \boxed{
 K_{\tau,x}(n)-K_{\tau,x/p_b}(n)
 =a_K\left(1-p_b^{-1/2}\right)\frac{\sqrt x}{n}\ge0.
 }
 \tag{L-91540.6}
\]

The constant term cancels.  Therefore

\[
\begin{aligned}
 K_{\tau,x}(n)-\sum_b\theta_b(n)K_{\tau,x/p_b}(n)
 ={}&
 \left(1-\sum_b\theta_b(n)\right)K_{\tau,x}(n)\\
 &+\sum_b\theta_b(n)
   \left[K_{\tau,x}(n)-K_{\tau,x/p_b}(n)\right]\ge0.
\end{aligned}
\tag{L-91540.7}
\]

Define these two residuals as \(D_T(x,n)\) and \(D_S(x,n)\).  Integration gives
the exact positive identities

\[
 \boxed{
 \mathfrak T_{\tau,x}(\nu)
 =\sum_b\mathfrak T_{\tau,x/p_b}(\nu_b)
  +\sum_n\nu(n)D_T(x,n),
 }
 \tag{L-91540.8}
\]

\[
 \boxed{
 \mathfrak S_{\tau,x}(\nu)
 =\sum_b\mathfrak S_{\tau,x/p_b}(\nu_b)
  +\sum_n\nu(n)D_S(x,n).
 }
 \tag{L-91540.9}
\]

The parent target and score are each spent once.

## 4. Every finite row has the same exact decomposition

The positive component row is increasing with the endpoint:

\[
 Y_1\le Y_2
 \Longrightarrow
 Q_{Y_1}(j)\le Q_{Y_2}(j).
 \tag{L-91540.10}
\]

Hence

\[
\begin{aligned}
 D_j(x,n)
 :={}&R_{\tau,x}(n;j)
      -\sum_b\theta_b(n)R_{\tau,x/p_b}(n;j)\\
 ={}&
 \left(1-\sum_b\theta_b(n)\right)R_{\tau,x}(n;j)\\
 &+\sum_b\theta_b(n)
  \left[R_{\tau,x}(n;j)-R_{\tau,x/p_b}(n;j)\right]\ge0.
\end{aligned}
\tag{L-91540.11}
\]

Thus every exact row is a sum of typed child rows plus a nonnegative
current-generation row.  Applying the ordinary carry matrix preserves the
identity coefficientwise.  The radix-four endpoint block is assembled by
pushing all child measures to the parent coordinate and applying `L-91329`
once.

## 5. Target-mass subprobability and bounded local debt

Suppose \(\mathfrak T_{\tau,x}(\nu)>0\).  Define the child target fractions

\[
 \omega_b=
 \frac{\mathfrak T_{\tau,x/p_b}(\nu_b)}
      {\mathfrak T_{\tau,x}(\nu)}.
 \tag{L-91540.12}
\]

Equation (L-91540.8) gives

\[
 \boxed{
 \omega_b\ge0,
 \qquad
 \sum_b\omega_b\le1.
 }
 \tag{L-91540.13}
\]

The residual need not have favorable score orientation.  That stronger property
of `L-91343` is not required.  Its positive score-loss debt is

\[
 E_{\tau,x}(\nu)
 =\sum_n\nu(n)\,[D_T(x,n)-D_S(x,n)]_+.
 \tag{L-91540.14}
\]

Because \(D_S\ge0\),

\[
 \boxed{
 0\le E_{\tau,x}(\nu)
 \le\sum_n\nu(n)D_T(x,n)
 \le\mathfrak T_{\tau,x}(\nu).
 }
 \tag{L-91540.15}
\]

After target normalization, the local typed-kernel debt is therefore at most
one.  At any fixed tree depth, (L-91540.13) implies that the sum of path target
weights is at most one, so the total debt charged at that depth is at most one.

This is the exact replacement for the unnecessary demand that every residual
score dominate its target pointwise.

## 6. The survival and hazard types lie in one uniform physical corridor

For the frozen binary-return output put \(r=p^{-1/2}\), \(0<r<1\), and
\(z=\sqrt{x/n}\ge1\).  The target-per-score ratios are

\[
 q_s(z)
 =\frac{(2r+4)z-(r+3)}
        {(r+1)(5z-3)},
 \tag{L-91540.16}
\]

\[
 q_h(z)
 =\frac{(2r+2)z-(r+2)}
        {(4r+1)z-(2r+1)}.
 \tag{L-91540.17}
\]

The four exact factorisations

\[
 2N_s-D_s=(3-r)(z-1)\ge0,
 \tag{L-91540.18}
\]

\[
 D_s-N_s=(3r+1)z-2r>0,
 \tag{L-91540.19}
\]

\[
 2N_h-D_h=3(z-1)\ge0,
 \tag{L-91540.20}
\]

\[
 2D_h-N_h=3r(2z-1)>0
 \tag{L-91540.21}
\]

give

\[
 \boxed{
 \frac12\le q_s(z)<1,
 \qquad
 \frac12\le q_h(z)<2.
 }
 \tag{L-91540.22}
\]

Equivalently, for both branch types,

\[
 \boxed{
 \frac12\,T\le S\le2T.
 }
 \tag{L-91540.23}
\]

Thus their target and score norms are uniformly equivalent, including the
limit \(p\to\infty\).  The hazard type may lie outside the smaller common-kernel
cone; it nevertheless remains in the full positive physical two-ledger cone.

## 7. Exact entry telescope

The frozen one-prime formulas also give

\[
 \boxed{
 T_s+T_h=4z-3,
 }
 \tag{L-91540.24}
\]

and

\[
 \boxed{
 S_s+S_h
 =5z-3+r(1-r)(z-1)
 \ge5z-3.
 }
 \tag{L-91540.25}
\]

Therefore a target-exact Hall projection of the two branch types enters the
typed cone with no target loss and no positive score debt.  Once it has entered,
Sections 2--5 carry each type unchanged through every later positive rough
branch.  No theorem identifying it again with the single native
`W_Psi/W_S` type is needed.

## 8. Firewalls and scope

This theorem does **not** assert:

```text
the hazard type belongs to the common W_Psi/W_S measure cone;
the residual score always dominates the residual target;
the full parent source may be copied into every rough branch;
a finite child may be evaluated at a fractional physical column;
the imported one-prime Hall/row producer is correct.
```

It proves the hereditary part after a positive paired type has been produced.

```text
paired positive target/score residuals              EXACT
typed child target fractions sum <=1                EXACT
finite-row residual positivity                      EXACT
local target-normalized debt <=1                    EXACT
survival/hazard physical-corridor bounds             EXACT
survival/hazard entry target telescope               EXACT
survival/hazard entry score superordination          EXACT
all-generation paired-type stability                 CLOSED
one-prime signed arithmetic -> typed positive entry  IMPORTED / AUDIT REQUIRED
Riemann Hypothesis                                   UNPROVEN
```
