# L-23826 — In-support weighted tail charge and shell summation

Claim ID: `L-23826`  
Title: The weighted shell charge can be paid at the largest existing prime, so corrected fixed-ratio shells compose without oversupport leakage  
Status: **PROPOSED COMPLETE FINITE COROLLARY — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23824`; PR #248 signed prime-incidence blocks  
Scope: finite shell assembly; no asymptotic shell-charge estimate

## 1. In-support boundary atom

Retain ordered primes

\[
p_1<\cdots<p_m,
\qquad x_i=\log p_i,
\]

a signed residual `r`, weighted tails

\[
R_j=\sum_{i=j}^m x_i r_i,
\]

and

\[
\mathcal B(r)=\max_j(R_j)_+.
\]

Instead of adding an oversupport prime, reduce the residual at the largest
existing prime by

\[
\boxed{
 r_m\longmapsto r_m-\frac{\mathcal B(r)}{x_m}.}
\tag{L-23826.1}
\]

Every weighted upper tail is reduced by exactly `mathcal B(r)`:

\[
R_j\longmapsto R_j-\mathcal B(r)\le0.
\tag{L-23826.2}
\]

The single-prime endpoint block from `1` to `p_m` realizes (L-23826.1) and has
objective loss exactly

\[
\frac{\mathcal B(r)}{x_m}x_m=\mathcal B(r).
\tag{L-23826.3}
\]

Applying the zero-cost weighted transport of `L-23824` afterwards makes every
prime residual nonpositive. Thus:

\[
\boxed{
\text{every finite prime residual has an in-support signed feasible repair
with objective loss at most }\mathcal B(r).}
\tag{L-23826.4}
\]

No coordinate beyond the original endpoint is introduced.

## 2. Shell certificates compose

Let

\[
X=X_0>X_1>\cdots>X_M\ge2
\tag{L-23826.5}
\]

be integer endpoints. Extend every seed and target by zero outside its own
support and define shell differences

\[
 b^{[j]}=b_{X_j}^{(0)}-b_{X_{j+1}}^{(0)},
\tag{L-23826.6}
\]

\[
 w^{[j]}(p)
 =w_{X_j}(p)-\mathbf1_{p\le X_{j+1}}w_{X_{j+1}}(p).
\tag{L-23826.7}
\]

Their residual is the shell residual `s_(X_j,X_(j+1))` of `L-23824`.
Apply (L-23826.4) inside the prime support through `X_j`. This produces a signed
shell certificate `c^[j]` satisfying

\[
 v_p(c^{[j]})\le w^{[j]}(p)
\qquad(p\le X_j),
\tag{L-23826.8}
\]

and

\[
 J_{\mathbb P}(c^{[j]})
\ge
J_{\mathbb P}(b^{[j]})
-\mathcal B_{X_j,X_{j+1}}.
\tag{L-23826.9}
\]

Summing the finite certificates gives

\[
 c=\sum_{j=0}^{M-1}c^{[j]}+c^{[M]},
\tag{L-23826.10}
\]

where `c^[M]` is any finite feasible base certificate at endpoint `X_M`.
Linearity and telescoping give

\[
\boxed{
 v_p(c)\le w_X(p)
 \qquad(p\le X),}
\tag{L-23826.11}
\]

and

\[
\boxed{
J_{\mathbb P}(c)
\ge
J_{\mathbb P}(b_X^{(0)})
-\sum_{j=0}^{M-1}\mathcal B_{X_j,X_{j+1}}
-O_{X_M}(1).}
\tag{L-23826.12}
\]

The construction uses signed coordinates, which are sufficient by PR #248
`L-24508`. It does not assert a nonnegative row decomposition.

## 3. Dyadic shell criterion

Take

\[
X_{j+1}=\max(2,\lfloor X_j/2\rfloor).
\tag{L-23826.13}
\]

Suppose that for every `epsilon>0`,

\[
\boxed{
\mathcal B_{Z,\lfloor Z/2\rfloor}
\le C_\varepsilon Z^\varepsilon
\qquad(Z\ge2).}
\tag{L-23826.14}
\]

The number of shells is `O(log X)`, while

\[
\sum_jX_j^\varepsilon\ll_\varepsilon X^\varepsilon.
\]

Therefore (L-23826.12) and the parabolic seed estimate imply

\[
\boxed{
P_X
\ge4\sqrt X-O_\varepsilon(X^\varepsilon).}
\tag{L-23826.15}
\]

Restoring proper prime powers costs only `O(log^2X)`.

Thus the dyadic weighted shell-tail theorem (L-23826.14) is already a complete
finite arithmetic criterion for RH through the reviewed square-screw/Landau
consumer.

## 4. Proof boundary

Closed exactly:

1. in-support payment of the least weighted upper-tail charge;
2. exact signed feasibility of each shell;
3. composition of shell certificates;
4. the dyadic shell-charge criterion for the prime-ramp lower bound.

Open:

1. the subpolynomial shell-charge estimate (L-23826.14);
2. RH.
