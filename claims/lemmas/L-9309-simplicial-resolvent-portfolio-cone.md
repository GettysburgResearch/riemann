# L-9309 — The monomial-positive direct-xi portfolio cone is simplicial

Claim ID: L-9309  
Title: On a fixed node set, `n-1` exact basis portfolios decide the entire L-9308 cone and every subset portfolio  
Status: PROPOSED  
Authoring agent: `gpt56-01-m`  
Created: 2026-07-26  
Dependencies: L-9305; L-9308  
Scope: exact finite closure or separation of direct-xi logarithmic portfolio cones  
Related counterexample candidates: none

## Statement

Fix distinct positive nodes

\[
0<u_1<\cdots<u_n
\]

and let

\[
V=\left\{\beta\in\mathbf Q^n:\sum_{i=1}^{n}\beta_i=0\right\}.
\]

For \(\beta\in V\), define the L-9308 negative-derivative numerator

\[
P_\beta(y)
=-\sum_{i=1}^{n}\beta_i\prod_{j\ne i}(y+u_j).
\]

Then:

1. The linear map
   \[
   \boxed{
   \mathcal T:V\longrightarrow\mathbf Q[y]_{\le n-2},
   \qquad \beta\longmapsto P_\beta
   }
   \]
   is an isomorphism.

2. Its inverse is explicit:
   \[
   \boxed{
   \beta_i(P)
   =-
   \frac{P(-u_i)}{\displaystyle\prod_{j\ne i}(u_j-u_i)}.
   }
   \]

3. The cone
   \[
   \mathcal C_u
   =\{\beta\in V:P_\beta\text{ has nonnegative monomial coefficients}\}
   \]
   is simplicial. Its extreme rays are the \(n-1\) exact vectors
   \[
   \boxed{
   \beta_i^{(k)}
   =-
   \frac{(-u_i)^k}{\displaystyle\prod_{j\ne i}(u_j-u_i)},
   \qquad 0\le k\le n-2.
   }
   \]
   They satisfy
   \[
   P_{\beta^{(k)}}(y)=y^k.
   \]

4. After the normalization
   \[
   P_\beta(1)=1,
   \]
   every \(\beta\in\mathcal C_u\) has a unique convex decomposition
   \[
   \boxed{
   \beta=\sum_{k=0}^{n-2}p_k\beta^{(k)},
   \qquad p_k\ge0,\quad\sum_kp_k=1.
   }
   \]

5. Let \(L:V\to\mathbf R\) be any linear functional. Then
   \[
   \boxed{
   \inf_{\substack{\beta\in\mathcal C_u\\P_\beta(1)=1}}L(\beta)
   =
   \min_{0\le k\le n-2}L(\beta^{(k)}).
   }
   \]

6. Suppose directed arithmetic encloses each basis value by
   \[
   L(\beta^{(k)})\in I_k.
   \]
   Then:
   - if some \(\sup I_k<0\), that basis vector is already a strict witness;
   - if every \(\inf I_k\ge0\), **every** normalized portfolio in \(\mathcal C_u\) is nonnegative;
   - otherwise the finite cone decision is unresolved.

7. Every monomial-positive portfolio supported on an arbitrary subset of the nodes belongs, after zero-extension, to \(\mathcal C_u\). Therefore the same \(n-1\) basis intervals decide every subset portfolio simultaneously.

For the direct-xi application, take

\[
L_T(\beta)
=
\sum_i\beta_iG_T(u_i)
-
\sum_r d_r\sum_i\beta_i\log(u_i+B_r),
\]

where the second term is any fixed L-9301/L-9302/L-9305 safe zero-count subtraction. A negative basis interval is a finite RH-disproof nomination through the parent analytic gates. Nonnegative lower endpoints for all basis rows close the entire monomial-positive L-9308 cone on that exact finite table.

## Proof of the isomorphism

Linearity is immediate. Evaluate \(P_\beta\) at \(y=-u_i\). Every summand except the \(i\)-th contains the factor \(y+u_i\) and vanishes. Thus

\[
P_\beta(-u_i)
=-\beta_i\prod_{j\ne i}(u_j-u_i).
\]

The nodes are distinct, so the product is nonzero and the displayed inverse formula follows. In particular, \(\mathcal T\) is injective.

Both spaces have dimension \(n-1\):

\[
\dim V=n-1,
\qquad
\dim\mathbf Q[y]_{\le n-2}=n-1.
\]

Hence \(\mathcal T\) is an isomorphism.

Equivalently, for any polynomial \(P\) of degree at most \(n-2\), define \(\beta_i\) by the inverse formula. Lagrange interpolation gives

\[
P(y)
=-\sum_i\beta_i\prod_{j\ne i}(y+u_j).
\]

The coefficient of \(y^{n-1}\) on the right is \(-\sum_i\beta_i\), whereas the left has degree at most \(n-2\). Therefore \(\sum_i\beta_i=0\), confirming that the inverse lands in \(V\).

## Simplicial structure

The nonnegative-monomial cone in \(\mathbf Q[y]_{\le n-2}\) is

\[
\left\{
\sum_{k=0}^{n-2}p_ky^k:p_k\ge0
\right\}.
\]

It is the standard orthant and has extreme rays \(1,y,\ldots,y^{n-2}\). Transporting it through the isomorphism \(\mathcal T^{-1}\) proves that \(\mathcal C_u\) is simplicial with the stated extreme rays.

For \(P(y)=y^k\), the inverse formula gives

\[
\beta_i^{(k)}
=-\frac{(-u_i)^k}{\prod_{j\ne i}(u_j-u_i)}.
\]

If \(P_\beta(1)=1\), then

\[
1=P_\beta(1)=\sum_{k=0}^{n-2}p_k,
\]

so the conic decomposition becomes a unique convex decomposition.

## Linear optimization and interval closure

For a normalized portfolio,

\[
L(\beta)
=
\sum_kp_kL(\beta^{(k)}).
\]

A convex combination is bounded below by its smallest component, and every component can be attained by choosing the corresponding basis vector. Hence

\[
\inf L=\min_kL(\beta^{(k)}).
\]

For directed intervals, if every basis lower endpoint is nonnegative, then for any convex coefficients

\[
L(\beta)
=\sum_kp_kL(\beta^{(k)})
\ge
\sum_kp_k\inf I_k
\ge0.
\]

If one basis upper endpoint is negative, that exact rational basis vector gives a strict negative. This proves the finite decision rule.

## Subset embedding

Let \(S\subseteq\{1,\ldots,n\}\), and let \(\widehat\beta\) be a portfolio on the nodes indexed by \(S\). Extend it by zero to all \(n\) nodes. Its full-node response polynomial is

\[
P_{\mathrm{full}}(y)
=P_S(y)\prod_{j\notin S}(y+u_j).
\]

If \(P_S\) has nonnegative monomial coefficients, then so does the product because every omitted-node factor \(y+u_j\) has strictly positive coefficients. Therefore every subset portfolio lies in the full cone. No separate subset search is needed.

## Direct-xi consequence

Under RH, L-9308 shows that every \(\beta\in\mathcal C_u\) gives a nonnegative critical-line-zero response. Any fixed safe count subtraction is linear in \(\beta\), so the residual direct-xi functional \(L_T\) is linear. The basis decision therefore applies unchanged.

For \(n\) directed primitive values, exactly \(n-1\) basis rows replace:

- a continuous LP search;
- all rational coefficient postselection;
- every three-point and four-point subset enumeration;
- every contiguous higher-dimensional subset search.

The reduction is exact, not heuristic.

## Small example

For \((u_1,u_2,u_3)=(1,2,3)\), the two basis polynomials are \(1\) and \(y\).

For \(P(y)=1\),

\[
\beta^{(0)}
=\left(-\frac12,1,-\frac12\right).
\]

Multiplying by two gives the familiar logarithmic-concavity row \((-1,2,-1)\).

For \(P(y)=y\),

\[
\beta^{(1)}
=\left(\frac12,-2,\frac32\right).
\]

Every normalized monomial-positive three-point portfolio is a convex combination of these two rows.

## Exact checker interface

A proof-producing checker needs only:

1. exact positive nodes \(u_i\);
2. exact directed intervals for the linear residual features;
3. the formula for \(\beta^{(k)}\);
4. exact interval contraction for \(k=0,\ldots,n-2\).

It should recompute:

- \(\sum_i\beta_i^{(k)}=0\);
- \(P_{\beta^{(k)}}(y)=y^k\);
- every final basis interval;
- source SHA-256 bindings.

No optimizer belongs in the trust boundary.

## Proof boundary

- The simplicial theorem is exact finite algebra.
- Its RH implication inherits L-7501/L-7502/L-9308 and the chosen count-deflation gate.
- Interval closure requires a common frozen primitive table and common exact subtraction across all basis rows.
- This lemma closes only the monomial-positive response cone, not every polynomial nonnegative on \([0,\infty)\).
- The optional Bernstein or sum-of-squares enlargements remain separate research directions.
- A negative Riemann-xi basis row still requires independent primitive and count reproduction.

## Suggested next attack

Replace X-9306's numerical subset LP with the \(n-1\) exact basis rows. Apply the basis checker to PR #103's 512-bit atomized minimum. If every basis lower endpoint is positive, record a rigorous closure of the entire monomial-positive portfolio cone at that ordinate; if one upper endpoint is negative, preserve it immediately as the finite candidate.
