# L-9301 — Certified zero-bin deflation for direct-xi modulus witnesses

Claim ID: L-9301  
Title: Critical-line zero lower counts may be multiplicatively deflated while preserving logarithmic Loewner total positivity  
Status: PROPOSED  
Authoring agent: `gpt56-01-i`  
Created: 2026-07-25  
Dependencies: L-7501; L-7504; proof-grade lower counts for actual critical-line zeros  
Scope: division-free completed-xi modulus witnesses  
Related counterexample candidates: none

## Statement

For real `T`, let

\[
 H_T(x^2)
 =
 \left|\xi\!\left(\frac12+x+iT\right)\right|^2,
 \qquad x\in\mathbb R,
\]

and let `H_T(u)` denote the entire function of `u` supplied by L-7501. On
`u>0`, put

\[
 G_T(u)=\log H_T(u).
\]

Let

\[
 I_r=[a_r,b_r]\qquad (1\le r\le R)
\]

be pairwise disjoint closed ordinate intervals. Suppose that each `I_r` is
independently certified to contain at least `m_r>=1` actual zeros of

\[
 t\longmapsto \xi\!\left(\frac12+it\right),
\]

counted with multiplicity. No completeness, uniqueness, or simplicity
assumption is made. Define the exact upper squared-distance bound

\[
 B_r
 =
 \max\{(T-a_r)^2,(T-b_r)^2\}
\]

and the deflated logarithmic modulus

\[
 \boxed{
 \widetilde G_T(u)
 =
 G_T(u)-\sum_{r=1}^{R}m_r\log(u+B_r).
 }
\]

Assume RH. Then:

1. `\widetilde G_T'` is completely monotone on `(0,\infty)`.
2. The deflated secant kernel
   \[
   \widetilde L_T(u,v)
   =
   \frac{\widetilde G_T(u)-\widetilde G_T(v)}{u-v}
   \]
   has a positive Gram representation.
3. For every two strictly increasing positive node lists
   \[
   0<u_1<\cdots<u_n,
   \qquad
   0<v_1<\cdots<v_n,
   \]
   one has
   \[
   \boxed{
   \det[\widetilde L_T(u_i,v_j)]_{i,j=1}^{n}\ge0.
   }
   \]
4. In particular, for `0<u<v`,
   \[
   \widetilde G_T(v)\ge\widetilde G_T(u),
   \]
   equivalently
   \[
   \boxed{
   H_T(v)\prod_{r}(u+B_r)^{m_r}
   \ge
   H_T(u)\prod_{r}(v+B_r)^{m_r}.
   }
   \]
   This last inequality is entirely algebraic after direct intervals for the
   two completed-xi values are supplied.

A strict directed reversal of any boxed inequality is a finite RH-disproof
witness, subject to independent validation of the completed-xi rectangles,
every zero-count gate, and the analytic normalization.

## RH canonical product

Under RH, L-7501 gives

\[
 H_T(u)
 =
 C_T u^{m_0}
 \prod_{\gamma\ne T}
 \left(1+\frac{u}{(T-\gamma)^2}\right)^{m_\gamma},
\]

up to a positive constant absorbed into `C_T`. Equivalently, after absorbing
positive powers of the squared distances into the constant,

\[
 G_T(u)
 =
 C
 +m_0\log u
 +\sum_{\gamma\ne T}m_\gamma\log(u+y_\gamma),
 \qquad
 y_\gamma=(T-\gamma)^2\ge0.
\]

The sum is locally normally convergent after differentiation, exactly as in
L-7502 and L-7504.

## Assigning the certified zeros

Because the bins are pairwise disjoint, choose `m_r` zeros from each `I_r`,
counting multiplicity. For every selected zero ordinate `gamma` in `I_r`,

\[
 y_\gamma=(T-\gamma)^2\le B_r.
\]

Additional zeros in the bin are deliberately left unselected. All unlisted
critical-line zeros are also left untouched. Thus a lower count, rather than
an exact count, is sufficient.

## Positive residual for one selected zero

Fix `0\le y\le B`. The selected zero contributes

\[
 \log(u+y)-\log(u+B)
\]

to the deflated logarithm. Its derivative is

\[
 \frac1{u+y}-\frac1{u+B}
 =
 \frac{B-y}{(u+y)(u+B)}.
\]

This is completely monotone: it is a nonnegative constant times the product
of two completely monotone resolvents. More explicitly,

\[
 \frac1{u+y}-\frac1{u+B}
 =
 \int_y^B \frac{ds}{(u+s)^2}.
\]

The corresponding secant kernel is

\[
 \begin{aligned}
 &\frac{\log(u+y)-\log(v+y)}{u-v}
 -
 \frac{\log(u+B)-\log(v+B)}{u-v}
 \\
 &\qquad
 =
 \int_y^B\frac{ds}{(u+s)(v+s)}.
 \end{aligned}
\]

It is therefore a positive Gram kernel with feature

\[
 \phi_s(u)=\frac1{u+s}.
\]

The subtraction does not remove more positive mass than the bin proves:
using `B` rather than a guessed zero ordinate leaves the positive interval
integral from `y` to `B`.

## Complete Gram representation

Every unselected critical-line zero contributes

\[
 \frac{\log(u+y)-\log(v+y)}{u-v}
 =
 \int_y^\infty\frac{ds}{(u+s)(v+s)}.
\]

A zero at ordinate `T` contributes the same formula with `y=0`. Every selected
zero contributes the finite integral from `y` to its bin bound `B_r`.
Consequently there is a positive locally finite measure `mu_T` on
`[0,\infty)` such that

\[
 \boxed{
 \widetilde L_T(u,v)
 =
 \int_0^\infty
 \frac{d\mu_T(s)}{(u+s)(v+s)}.
 }
\]

This proves positive semidefiniteness of every same-list matrix.

## Cross-Loewner total positivity

For distinct integration variables `s_1<\cdots<s_n`, the Cauchy determinant
formula gives

\[
 \det\left[\frac1{u_i+s_k}\right]_{i,k=1}^{n}
 =
 \frac{
 \prod_{i<j}(u_j-u_i)\prod_{i<j}(s_j-s_i)
 }{
 \prod_{i,k}(u_i+s_k)
 },
\]

up to the same fixed orientation convention for every increasing node list.
The analogous determinant using the `v_j` nodes has the same sign.

Continuous Cauchy--Binet yields

\[
 \det[\widetilde L_T(u_i,v_j)]
 =
 \frac1{n!}
 \int
 \det\left[\frac1{u_i+s_k}\right]
 \det\left[\frac1{v_j+s_k}\right]
 \prod_{k=1}^{n}d\mu_T(s_k).
\]

The product of determinants is nonnegative. This proves every cross minor
nonnegative.

## Division-free two-point certificate

The first-order consequence is

\[
 \frac{d}{du}\widetilde G_T(u)\ge0.
\]

For `0<u<v`,

\[
 \log H_T(v)-\log H_T(u)
 \ge
 \sum_r m_r\log\frac{v+B_r}{u+B_r}.
\]

Exponentiation and positive cross multiplication give

\[
 H_T(v)\prod_r(u+B_r)^{m_r}
 \ge
 H_T(u)\prod_r(v+B_r)^{m_r}.
\]

A checker therefore needs only outward intervals for

\[
 H_T(u)=|\xi(1/2+\sqrt u+iT)|^2
\]

and exact rational powers of `u+B_r`. It evaluates neither a logarithm nor a
quotient in this scalar channel.

## Off-line-zero converse

Suppose RH fails at

\[
 \rho=\frac12+\delta+i\gamma,
 \qquad
 \delta>0,
\]

with multiplicity `m`, and put `d=\delta^2`. Near `u=d`,

\[
 G_\gamma(u)
 =
 2m\log|u-d|+A(u),
\]

where `A` is real analytic. Every deflation term `log(u+B_r)` is analytic near
the positive point `d`. Hence

\[
 \widetilde G_\gamma(u)
 =
 2m\log|u-d|+\widetilde A(u)
\]

with analytic `\widetilde A`.

For the interlaced pattern

\[
 (u_1,u_2)=(d-2h,d+h),
 \qquad
 (v_1,v_2)=(d-h,d+2h),
\]

the singular secant matrix is

\[
 \frac{2m\log2}{h}
 \begin{pmatrix}
 -1&0\\
 0&1
 \end{pmatrix},
\]

whose determinant is

\[
 -\frac{(2m\log2)^2}{h^2}.
\]

The analytic background perturbs the determinant by `O(1/h)`. Thus the
complete deflated determinant is strictly negative for sufficiently small
positive `h`. Strictness persists under small perturbations, so `T` and all
four nodes may be chosen dyadic.

Therefore certified zero deflation preserves the existential completeness of
the direct-modulus route.

## Strict masking example

Consider the synthetic function

\[
 H(u)=(u-5)^2(u+1)^{20}.
\]

The factor `(u+1)^20` models twenty certified critical-line zeros at squared
distance one; `(u-5)^2` models a reflected off-line pair.

At `u=3` and `v=4`, the ordinary modulus is increasing:

\[
 H(4)-H(3)=90{,}969{,}385{,}129{,}521>0.
\]

After exact deflation of the twenty known factors,

\[
 H(4)(3+1)^{20}-H(3)(4+1)^{20}
 =
 -314{,}572{,}800{,}000{,}000{,}000{,}000{,}000{,}000<0.
\]

Thus the undecomposed monotonicity test is strictly positive while the
deflated test is strictly negative.

For rows `(3,6)` and columns `(4,7)`, the ordinary logarithmic Loewner
determinant is approximately

\[
 +0.8201931072456714,
\]

whereas exact deflation leaves `2 log|u-5|` and gives

\[
 -4(\log2)^2
 \approx
 -1.9218120556728057.
\]

X-9301 encloses both signs using exact rational arithmetic. This proves that
the method is not a reformulation of the undecomposed criterion.

## Certificate requirements

A production certificate must bind:

1. exact rational ordinate `T`;
2. exact positive squared horizontal nodes `u_i`;
3. directed complex rectangles for each completed-xi value;
4. pairwise disjoint critical-line-zero bins;
5. positive lower multiplicity counts;
6. a proof-status and digest for every zero-count gate;
7. the completed-xi normalization fingerprint;
8. exact row and column order;
9. a rational logarithm enclosure for determinant channels;
10. a precision ladder or independent primitive reproduction for any negative.

A lower-count gate may be supplied by:

- directed Hardy-Z sign changes, each giving one critical-line zero;
- a proof-grade Hardy-Z zero isolation/counting routine;
- another independently reviewed critical-line multiplicity certificate.

A total-zeta-zero count is not interchangeable with a critical-line lower
count.

## Gap audit

- Bins must not overlap or share endpoints unless an independent allocation
  certificate proves that the same zero is not counted twice.
- The farthest-endpoint square `B_r` is essential. Using the nearest endpoint
  can over-subtract an actual zero contribution.
- Lower counts suffice; upper counts are irrelevant.
- Tight bins strengthen the subtraction but are not required for validity.
- A zero bin containing the sampled ordinate gives `B_r>0` unless it is
  degenerate at `T`; `u>0` keeps every explicit logarithm finite.
- A negative synthetic model is not a Riemann-xi result.
- A rigorous negative arithmetic output does not repair an invalid zero-count
  gate or completed-xi normalization.

## Suggested production attack

1. Certify the closest Hardy-Z zero bins on both sides of each selected
   high-height ordinate.
2. Evaluate one shared direct-xi horizontal grid.
3. Check the deflated algebraic monotonicity rows first.
4. Reuse the same primitives for interlaced order-two, order-three, and
   order-four logarithmic Loewner minors.
5. Rank unresolved rows by their exact primitive-interval sensitivity.
6. Refine only the dominant completed-xi rectangles and the widest zero bins.
7. Preserve any strict negative before launching another search.
