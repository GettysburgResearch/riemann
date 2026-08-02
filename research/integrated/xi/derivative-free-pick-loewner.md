# Integrated packet: derivative-free \(\xi\), Pick, and Loewner criteria

**Packet status:** integrated, reviewed finite conditional mathematics  
**Global status:** RH remains unsolved  
**Primary source A:** PR [#48](https://github.com/gfreund123/riemann/pull/48) at `ac4e8e7b36a95dd0bb325bcaf69ab79a10e68b12`  
**Primary source B:** PR [#52](https://github.com/gfreund123/riemann/pull/52) at `b19d2982d5cdc3c13eaa72a9064f7c994e0c6313`  
**Review evidence:** `reports/gpt56-global-01/2026-08-01-pre-public-review-pr44-pr63.md` at review-source commit `88617ac916d3df6e61ec5b4726e866743b8fc4a3`  
**Review verdicts:** #48 `VERIFIED`; #52 `VERIFIED`  
**Parent interface:** the review independently reconstructed the Lagarias positive-real/Pick normalization used by the packet. Exact production still requires authenticated completed-\(\xi\) or \(\xi'/\xi\) primitives.

## Packet summary

Let

\[
F(s)=\frac{\xi'(s)}{\xi(s)}
\]

in the standard completed-\(\xi\) normalization, and for real \(T\), \(u>0\), define

\[
J_T(u)
=
\sqrt u\,
\Re F\!\left(\frac12+\sqrt u+iT\right).
\]

Under RH, \(J_T\) has a positive zero-resolvent representation. This produces a hierarchy of exact finite necessary conditions:

- nonnegative two-point secants;
- alternating divided differences;
- totally nonnegative cross-Loewner matrices;
- barycentric product localizers;
- two sign-complete channels;
- exact modeled-pole annihilators.

Any strict directed violation at exact zero-free points would be a finite RH-disproof witness. No such Riemann-data violation is currently integrated.

---

## 1. Horizontal zero-resolvent representation

Under RH, every nontrivial zero has the form

\[
\rho=\frac12+i\gamma
\]

with multiplicity included. For \(x>0\),

\[
R_T(x)
=
\Re F\!\left(\frac12+x+iT\right)
=
\sum_\gamma
\frac{x}{x^2+(T-\gamma)^2}.
\]

Multiplying by \(x\) and setting \(u=x^2\) gives

\[
J_T(u)
=
\sum_\gamma
\frac{u}{u+a_\gamma},
\qquad
a_\gamma=(T-\gamma)^2\ge0.
\]

The finite criteria below are elementary consequences of this representation.

### Source qualification

The exact zero-resolvent formula depends on the completed-\(\xi\) canonical product and logarithmic-derivative normalization. The exact-SHA review checked that interface against Lagarias’s positive-real criterion and correction. A production certificate must still bind the actual normalization and prove each evaluation point zero-free.

---

## 2. Two-point value-only secant

Let \(0<x_1<x_2\), \(u_j=x_j^2\). Define

\[
\mathcal S_T(x_1,x_2)
=
\frac{x_2R_T(x_2)-x_1R_T(x_1)}
{x_2^2-x_1^2}
=
\frac{J_T(u_2)-J_T(u_1)}
{u_2-u_1}.
\]

### Theorem

Under RH,

\[
\mathcal S_T(x_1,x_2)
=
\sum_\gamma
\frac{(T-\gamma)^2}
{\bigl(x_1^2+(T-\gamma)^2\bigr)
 \bigl(x_2^2+(T-\gamma)^2\bigr)}
\ge0.
\]

A directed enclosure with strict negative upper endpoint at exact zero-free points disproves RH.

### Proof

For one \(a\ge0\),

\[
\frac{\frac{u_2}{u_2+a}-\frac{u_1}{u_1+a}}
{u_2-u_1}
=
\frac{a}{(u_1+a)(u_2+a)}\ge0.
\]

Summation over the absolutely convergent zero-resolvent series gives the formula.

### Converse geometry

If RH is false, symmetry gives an off-line pair

\[
\frac12+\delta+i\gamma,
\qquad
\frac12-\delta+i\gamma,
\qquad \delta>0.
\]

Near \(x=\delta\),

\[
F\!\left(\frac12+x+i\gamma\right)
=
\frac{m}{x-\delta}
+\frac{m}{x+\delta}
+h(x),
\]

with \(h\) analytic. The pair contributes

\[
J_{\rm pair}(u)
=
\frac{2mu}{u-\delta^2}.
\]

For \(\delta^2<u_1<u_2\),

\[
\frac{J_{\rm pair}(u_2)-J_{\rm pair}(u_1)}
{u_2-u_1}
=
-\frac{2m\delta^2}
{(u_1-\delta^2)(u_2-\delta^2)}.
\]

This tends to \(-\infty\) as the nodes approach \(\delta^2\) from the right, while the analytic background has bounded nearby secants. At the same time the pointwise real parts tend to \(+\infty\). Thus every RH failure creates an open set with positive scalar values but a negative derivative-free secant. Exact rational or dyadic triples exist by density.

### Differential limit

As \(x_2\to x_1=x\),

\[
\mathcal S_T(x_1,x_2)
\longrightarrow
\frac12\left(
\Re F'\!\left(\frac12+x+iT\right)
+
\frac1x\Re F\!\left(\frac12+x+iT\right)
\right).
\]

The value-only test is therefore the derivative-free form of the reviewed right-side differential localizer.

### Source

- `claims/lemmas/L-4701-xi-two-point-secant-witness.md`
- source blob `c5289e2b98bf6c35b6d7163547d6ab15ed44c795`

---

## 3. Alternating divided differences

For pairwise distinct positive nodes \(u_0,\ldots,u_n\), let
\([u_0,\ldots,u_n]J_T\) be the ordinary divided difference.

### Theorem

Under RH, for every \(n\ge1\),

\[
(-1)^{n-1}[u_0,\ldots,u_n]J_T
=
\sum_\gamma
\frac{(T-\gamma)^2}
{\prod_{k=0}^n\bigl(u_k+(T-\gamma)^2\bigr)}
\ge0.
\]

Thus:

- \(J_T\) is increasing;
- its second divided differences are nonpositive;
- its third divided differences are nonnegative;
- the signs continue alternately.

A strict opposite sign from exact directed values disproves RH.

### Proof

For

\[
f_a(u)=\frac{u}{u+a}
=
1-\frac{a}{u+a},
\]

the constant has zero divided differences of positive order, while

\[
[u_0,\ldots,u_n]\frac1{u+a}
=
\frac{(-1)^n}
{\prod_{k=0}^n(u_k+a)}.
\]

Therefore

\[
[u_0,\ldots,u_n]f_a
=
\frac{(-1)^{n-1}a}
{\prod_{k=0}^n(u_k+a)}.
\]

Apply this to every \(a_\gamma\). The order-one series decays as
\(O((T-\gamma)^{-2})\); higher orders decay faster, so termwise summation is justified.

### Exact finite reduction

At exact offsets \(x_k\), with \(u_k=x_k^2\), every divided difference is the fixed rational linear combination

\[
[u_0,\ldots,u_n]J_T
=
\sum_{k=0}^n
\frac{J_T(u_k)}
{\prod_{r\ne k}(u_k-u_r)}.
\]

The checker should reconstruct these coefficients and outwardly contract the input balls. It must not silently sort malformed nodes or replace distinct nodes by a hidden derivative.

### Source

- `claims/lemmas/L-4702-xi-complete-bernstein-divided-differences.md`
- source blob `ec1fb75df6432a3d39ac8f56775bfeeccf733482`

---

## 4. Cross-Loewner total nonnegativity

Let

\[
0<u_1<\cdots<u_m,
\qquad
0<v_1<\cdots<v_n,
\]

with \(u_i\ne v_j\). Define

\[
\mathcal L_T(U,V)_{ij}
=
\frac{J_T(u_i)-J_T(v_j)}
{u_i-v_j}.
\]

### Theorem

Under RH, every square minor of this rectangular matrix is nonnegative.

A strict negative directed minor is a finite RH-disproof witness.

### Proof

Under RH,

\[
\mathcal L_T(u,v)
=
\sum_\gamma
\frac{a_\gamma}
{(u+a_\gamma)(v+a_\gamma)}.
\]

Group equal positive \(a_\gamma\) and write the positive combined weight as \(c_a\):

\[
\mathcal L_T(u,v)
=
\sum_{a>0}
\frac{c_a}{(u+a)(v+a)}.
\]

For a finite atom set and a chosen \(k\times k\) minor, write

\[
P_{p\ell}=\frac1{r_p+a_\ell},
\qquad
Q_{q\ell}=\frac1{s_q+a_\ell},
\qquad
C=\operatorname{diag}(c_{a_\ell}).
\]

The minor matrix is \(PCQ^{\mathsf T}\). Cauchy–Binet expands its determinant into sums of products of positive weights and two Cauchy determinants. For increasing \(z_p\) and \(b_j\),

\[
\det\left(\frac1{z_p+b_j}\right)
=
\frac{
\prod_{p<q}(z_q-z_p)
\prod_{p<q}(b_q-b_p)
}{
\prod_{p,j}(z_p+b_j)
}>0.
\]

Every finite-truncation minor is nonnegative. Entrywise absolute convergence and continuity of determinant give the complete result.

### Why higher minors matter

A \(2\times2\) Loewner matrix can have all four entries positive but negative determinant. Thus higher minors test whether all positive-looking secants come from one positive resolvent measure.

### Source

- `claims/lemmas/L-4703-xi-cross-loewner-total-nonnegativity.md`
- source blob `b36116971d3101972519d3c26737e5ed1c1cff9e`

---

## 5. Barycentric Pick product localizers

Fix distinct positive \(x_0,\ldots,x_r\), set

\[
s_i=\frac12+x_i+iT,
\]

and define the Pick matrix

\[
K_{ij}
=
\frac{F(s_i)+\overline{F(s_j)}}{x_i+x_j}.
\]

Let

\[
c_i
=
\frac1{\prod_{j\ne i}(x_i-x_j)}.
\]

### Theorem

Under RH,

\[
c^*Kc
=
\sum_\gamma
\frac1{\prod_{i=0}^r
\bigl(x_i^2+(T-\gamma)^2\bigr)}
\ge0.
\]

For a same-ordinate off-line pair at horizontal displacement \(\delta\), its contribution at the matching ordinate is

\[
\frac{2}
{\prod_i(x_i^2-\delta^2)}.
\]

For two offsets bracketing \(\delta\), this contribution is negative and diverges in magnitude as a bracket endpoint approaches the pole. Every RH failure therefore creates an open negative two-point barycentric basin.

### Proof

Under RH,

\[
K_{ij}
=
\sum_\gamma
\frac1{x_i+i(T-\gamma)}
\frac1{x_j-i(T-\gamma)}.
\]

For \(P(z)=\prod_i(z+x_i)\), partial fractions give

\[
\sum_i\frac{c_i}{z+x_i}
=
\frac{(-1)^r}{P(z)}.
\]

Hence

\[
c^*Kc
=
\sum_\gamma
\left|
\sum_i\frac{c_i}{x_i+i(T-\gamma)}
\right|^2
=
\sum_\gamma
\frac1{\prod_i(x_i^2+(T-\gamma)^2)}.
\]

### Exact contraction

For real \(c_i\),

\[
c^*Kc
=
\sum_i d_i\,\Re F(s_i),
\qquad
d_i=2c_i\sum_j\frac{c_j}{x_i+x_j}.
\]

The quantity \(\sum_i|d_i|\) is the explicit pointwise-error amplification and must be reported.

### Source

- `claims/lemmas/L-3901-barycentric-pick-product-localizer.md`
- source blob `7c012ec82a0e057275417c179314b9ccbeba158d`

---

## 6. Two sign-complete value channels

Define

\[
H_T(u)
=
\frac{R_T(\sqrt u)}{\sqrt u},
\qquad
J_T(u)=uH_T(u).
\]

For \(0<u<v\), put

\[
A_T(u,v)
=
\frac{H_T(u)-H_T(v)}{v-u},
\]

and

\[
B_T(u,v)
=
\frac{J_T(v)-J_T(u)}{v-u}.
\]

### Theorem

Under RH,

\[
A_T(u,v)
=
\sum_\gamma
\frac1{
\bigl(u+(T-\gamma)^2\bigr)
\bigl(v+(T-\gamma)^2\bigr)
}
\ge0,
\]

and

\[
B_T(u,v)
=
\sum_\gamma
\frac{(T-\gamma)^2}{
\bigl(u+(T-\gamma)^2\bigr)
\bigl(v+(T-\gamma)^2\bigr)
}
\ge0.
\]

The exact identities

\[
B_T(u,v)=H_T(v)-uA_T(u,v)
=H_T(u)-vA_T(u,v)
\]

link the channels.

For a same-ordinate off-line pair with \(d=\delta^2\),

\[
A_{\rm pair}(u,v)
=
\frac{2m}{(u-d)(v-d)},
\]

\[
B_{\rm pair}(u,v)
=
-\frac{2md}{(u-d)(v-d)},
\]

and therefore

\[
\frac{B_{\rm pair}}{A_{\rm pair}}=-d.
\]

Thus:

- straddling \(d\) makes \(A_{\rm pair}<0\);
- placing both nodes on the same side makes \(B_{\rm pair}<0\).

One rigorous negative channel suffices. The paired pattern and ratio are proposal diagnostics.

### Source

- `claims/lemmas/L-3902-two-channel-xi-pole-localizer.md`
- source blob `bb1a0da46d1a002945a7b0bdb57af58591105660`

---

## 7. Exact matched-pole Pick annihilator

Choose distinct positive rational nodes \(x_1,\ldots,x_n\) and a rational model \(d>0\) avoiding every \(x_i^2\). Let

\[
P(z)=\prod_i(z-x_i),
\qquad
w_i=\frac1{P'(x_i)},
\]

\[
\alpha_i(d)=\frac{x_i}{x_i^2-d},
\qquad
S_0=\sum_iw_i\alpha_i(d),
\qquad
S_1=\sum_iw_ix_i\alpha_i(d),
\]

\[
D(d)=\prod_i(x_i^2-d),
\]

and define

\[
c_i
=
D(d)w_i(S_1-S_0x_i).
\]

### Exact identities

The vector satisfies

\[
\sum_i c_ix_i^k=0
\qquad(0\le k\le n-3),
\]

and

\[
\sum_i c_i\frac{x_i}{x_i^2-d}=0,
\qquad
\sum_i c_i\frac1{x_i^2-d}=-1.
\]

For a modeled same-ordinate reflected pair of multiplicity \(m\), its Pick matrix is

\[
K^{(d)}_{ij}
=
2m\frac{x_ix_j-d}
{(x_i^2-d)(x_j^2-d)}.
\]

Consequently,

\[
c^{\mathsf T}K^{(d)}c=-2md.
\]

The positive rank-one component is annihilated exactly; the negative component remains.

### Proof extract

The barycentric identities

\[
\sum_iw_ix_i^k=0
\qquad(0\le k\le n-2)
\]

give the moment cancellations.

The first modeled overlap vanishes by construction. To compute the second, use the partial-fraction identity in a temporary quadratic extension \(r^2=d\). One obtains

\[
\sum_i\frac{w_i}{x_i^2-d}
=
\frac1{2r}\left(\frac1{P(-r)}-\frac1{P(r)}\right),
\]

\[
\sum_i\frac{w_ix_i}{x_i^2-d}
=
-\frac12\left(\frac1{P(r)}+\frac1{P(-r)}\right).
\]

Since

\[
P(r)P(-r)=D(d),
\]

the required overlap is exactly \(-1\). The final identity is rational; the temporary square root is only a proof device.

### Exact mismatch polynomial

For an actual squared displacement \(q\), define

\[
D_q=\prod_i(x_i^2-q),
\]

\[
U(q)=
\sum_i c_ix_i\prod_{j\ne i}(x_j^2-q),
\]

\[
V(q)=
\sum_i c_i\prod_{j\ne i}(x_j^2-q).
\]

The isolated pair contribution is

\[
2m\frac{U(q)^2-qV(q)^2}{D_q^2}.
\]

At \(q=d\), the numerator is strictly negative. Exact polynomial interval evaluation can therefore certify an open modeled-mismatch region.

### Critical proof boundary

The value \(-2md\) belongs only to the modeled pair component. It is not the sign of the complete Riemann \(\xi\) function. All other zeros and completion terms remain inside the actual \(F\) evaluations. The final proof object must freeze \(c\) and directly contract directed primitive balls.

### Source

- `claims/lemmas/L-3904-matched-pole-pick-annihilator.md`
- source blob `c040b45ffc3ff2964f985e5535983c6112ed5878`

---

## Dependencies and normalizations

- \(F=\xi'/\xi\) uses the exact completed-\(\xi\) normalization reviewed through the parent positive-real/Pick interface.
- Every evaluation point must lie strictly in \(\Re s>1/2\) and be certified away from zeros before division.
- Zero sums count multiplicity.
- Squared nodes \(u=x^2\) use the positive real square root.
- Cross-Loewner row and column nodes must remain ordered and cross-disjoint.

## Computational status

The theorem files include exact synthetic controls. This packet does not copy or claim a directed actual-\(\xi\) negative result. The separate finite positive controls are in [`finite-pick-controls.md`](finite-pick-controls.md).

The integration pass did not rerun Arb, FLINT, Riemann–Siegel, zero, or interval computations.

## Known exclusions and failed strengthenings

- Positive finite matrices do not prove the global Pick kernel positive.
- A fitted rational model or floating eigenvector is proposal-only.
- High-order barycentric weights may amplify primitive uncertainty catastrophically.
- Real same-height constraints do not equal the complete complex Pick cone.
- A local zero census cannot retire a global predicate without a locality/complement theorem.
- The complex-center targeted Li coefficient family corrected in the companion packet is not licensed by these theorems.
- A finite grid need not locate the open witness basin guaranteed under false RH.

## Why this packet matters

It gives a coherent, derivative-free finite disproof architecture whose elementary formulas and local converse geometry were independently reviewed. The route’s bottleneck is now concrete: exact primitive production and witness discovery, not vague uncertainty about what finite sign would matter.

## Exact next missing step

Construct a small proof-grade producer that evaluates exact point pairs or \(2\times2\) Loewner packets with a distinct backend and strict normalization binding. Freeze the points and rational contraction before final interval evaluation. A strict negative survivor would need immediate independent reproduction.
