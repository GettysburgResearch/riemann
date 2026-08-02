# Integrated packet: derivative-free \(\xi\), Pick, and Loewner criteria

**Packet status:** integrated reviewed finite conditional mathematics  
**Scope:** finite RH-necessary theorems and false-RH existential witness geometry; no production violation and no global positivity theorem  
**Global status:** RH remains unsolved  
**Primary source A:** PR [#48](https://github.com/gfreund123/riemann/pull/48) at `ac4e8e7b36a95dd0bb325bcaf69ab79a10e68b12`  
**Primary source B:** PR [#52](https://github.com/gfreund123/riemann/pull/52) at `b19d2982d5cdc3c13eaa72a9064f7c994e0c6313`  
**Review evidence:** `reports/gpt56-global-01/2026-08-01-pre-public-review-pr44-pr63.md` at `88617ac916d3df6e61ec5b4726e866743b8fc4a3`  
**Review verdict:** #48 `VERIFIED`; #52 `VERIFIED`  
**Production status:** no strict directed Riemann-data violation is integrated; the theorem sources contain exact synthetic controls only.

## Completed-\(\xi\) normalization and imported necessity interface

Use

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
F(s)=\frac{\xi'(s)}{\xi(s)}
\]

away from zeros of \(\xi\).

The RH-necessity interface is source-qualified through:

- J. C. Lagarias, “On a positivity property of the Riemann xi-function,” *Acta Arithmetica* **89** (1999), 217–234, DOI `10.4064/aa-89-3-217-234`;
- J. C. Lagarias, “Correction to: On a positivity property of the Riemann xi-function,” *Acta Arithmetica* **116** (2005), 293–294, DOI `10.4064/aa116-3-5`.

The exact-SHA review independently checked the parent interface against Lagarias’s Theorem 1.1 and equations (1.4)–(1.5) and (1.19). The 2005 note corrects the sign before \(1/(s-1)\) in equation (3.8) of the original direct evaluator and does not retract Theorem 1.1.

In this normalization,

\[
F(s)
=
\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
+\frac{\zeta'(s)}{\zeta(s)}.
\]

A proof-producing evaluator must reject any point whose \(\xi(s)\) or \(\zeta(s)\) enclosure does not justify division.

This packet proves the finite algebra and local pole geometry from the source-qualified resolvent interface. It does not reproduce Lagarias’s full literature proof.

## Horizontal response

For real \(T\), \(x>0\), define

\[
R_T(x)
=
\Re F\!\left(\frac12+x+iT\right),
\]

and for \(u=x^2>0\),

\[
J_T(u)
=
\sqrt u\,
\Re F\!\left(\frac12+\sqrt u+iT\right).
\]

Under RH, in the centered symmetric canonical-product normalization,

\[
R_T(x)
=
\sum_\gamma
\frac{x}{x^2+(T-\gamma)^2},
\]

where ordinates are counted with multiplicity, and hence

\[
J_T(u)
=
\sum_\gamma
\frac{u}{u+a_\gamma},
\qquad
a_\gamma=(T-\gamma)^2\ge0.
\]

The real resolvent series is absolutely convergent at fixed \(x>0\): its terms are \(O(\gamma^{-2})\), and the standard zero-counting growth suffices. The secant, divided-difference, and Loewner series below decay at least as fast. No claim is made that an arbitrary unpaired raw \(\sum_\rho1/(s-\rho)\) is absolutely convergent.

This representation yields the finite criteria below.

---

## 1. Two-point value-only secant

Let \(0<x_1<x_2\), \(u_j=x_j^2\), and define

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

A directed enclosure with strict negative upper endpoint at exact zero-free points contradicts RH.

### Proof

For \(a\ge0\),

\[
\frac{\frac{u_2}{u_2+a}-\frac{u_1}{u_1+a}}
{u_2-u_1}
=
\frac{a}{(u_1+a)(u_2+a)}
\ge0.
\]

Sum over the absolutely convergent resolvent atoms.

### False-RH local converse

If RH is false, symmetry gives a same-ordinate pair

\[
\frac12+\delta+i\gamma,
\qquad
\frac12-\delta+i\gamma,
\qquad
\delta>0,
\]

with multiplicity \(m\). Near \(x=\delta\),

\[
F\!\left(\frac12+x+i\gamma\right)
=
\frac{m}{x-\delta}
+
\frac{m}{x+\delta}
+
h(x),
\]

where \(h\) is analytic. The pair contributes

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

This tends to \(-\infty\) as the nodes approach \(\delta^2\) from the right, while the analytic background has bounded nearby secants. The pointwise real parts tend to \(+\infty\). Therefore every RH failure creates an open set with positive scalar values and a negative derivative-free secant. Rational or dyadic triples exist by density.

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

### Exact source

- `claims/lemmas/L-4701-xi-two-point-secant-witness.md`
- source blob `c5289e2b98bf6c35b6d7163547d6ab15ed44c795`

---

## 2. Alternating divided differences

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

Thus \(J_T\) is increasing, its second divided differences are nonpositive, its third are nonnegative, and the signs continue alternately. A strict opposite directed sign at exact nodes contradicts RH.

### Proof

For

\[
f_a(u)=\frac{u}{u+a}=1-\frac{a}{u+a},
\]

the constant has zero positive-order divided differences, and

\[
[u_0,\ldots,u_n]\frac1{u+a}
=
\frac{(-1)^n}{\prod_{k=0}^n(u_k+a)}.
\]

Therefore,

\[
[u_0,\ldots,u_n]f_a
=
\frac{(-1)^{n-1}a}{\prod_{k=0}^n(u_k+a)}.
\]

Apply this to every \(a_\gamma\). The order-one terms are \(O((T-\gamma)^{-2})\); higher orders decay faster.

### Exact finite reduction

At exact offsets \(x_k\), \(u_k=x_k^2\),

\[
[u_0,\ldots,u_n]J_T
=
\sum_{k=0}^n
\frac{J_T(u_k)}
{\prod_{r\ne k}(u_k-u_r)}.
\]

An independent checker should reconstruct these rational coefficients and outwardly contract the primitive balls. It must reject malformed node order or cross-equalities rather than silently repairing them.

### Exact source

- `claims/lemmas/L-4702-xi-complete-bernstein-divided-differences.md`
- source blob `ec1fb75df6432a3d39ac8f56775bfeeccf733482`

---

## 3. Cross-Loewner total nonnegativity

Let

\[
0<u_1<\cdots<u_m,
\qquad
0<v_1<\cdots<v_n,
\]

with \(u_i\ne v_j\), and define

\[
\mathcal L_T(U,V)_{ij}
=
\frac{J_T(u_i)-J_T(v_j)}
{u_i-v_j}.
\]

### Theorem

Under RH, every square minor of this rectangular matrix is nonnegative. A strict negative directed minor is a finite RH-disproof witness.

### Proof

Under RH,

\[
\mathcal L_T(u,v)
=
\sum_\gamma
\frac{a_\gamma}
{(u+a_\gamma)(v+a_\gamma)}.
\]

Group equal positive \(a_\gamma\) and write their combined positive weight as \(c_a\):

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

The minor matrix is \(PCQ^{\mathsf T}\). Cauchy–Binet expands its determinant into positive weights times two Cauchy determinants. For increasing positive \(z_p,b_j\),

\[
\det\left(\frac1{z_p+b_j}\right)
=
\frac{
\prod_{p<q}(z_q-z_p)
\prod_{p<q}(b_q-b_p)
}{
\prod_{p,j}(z_p+b_j)
}
>0.
\]

Every finite-truncation minor is nonnegative. Absolute entrywise convergence and continuity of the determinant give the complete finite minor.

A higher minor can fail even when every sampled entry is positive; this is why the determinant hierarchy is stronger than independent scalar checks.

### Exact source

- `claims/lemmas/L-4703-xi-cross-loewner-total-nonnegativity.md`
- source blob `b36116971d3101972519d3c26737e5ed1c1cff9e`

---

## 4. Barycentric Pick product localizers

Fix distinct positive \(x_0,\ldots,x_r\), set

\[
s_i=\frac12+x_i+iT,
\]

and define

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
\frac1{\prod_{i=0}^r\bigl(x_i^2+(T-\gamma)^2\bigr)}
\ge0.
\]

For a same-ordinate off-line pair at horizontal displacement \(\delta\), its contribution at the matching ordinate is

\[
\frac{2}{\prod_i(x_i^2-\delta^2)}.
\]

Two offsets bracketing \(\delta\) make this pair contribution negative and unbounded in magnitude near the pole. Thus every RH failure creates an open negative two-point barycentric basin.

### Proof

Under the source-qualified Pick representation,

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

### Exact contraction and conditioning

For real \(c_i\),

\[
c^*Kc
=
\sum_i d_i\,\Re F(s_i),
\qquad
d_i=2c_i\sum_j\frac{c_j}{x_i+x_j}.
\]

The exact amplification \(\sum_i|d_i|\) must be compared with the primitive interval widths.

### Exact source

- `claims/lemmas/L-3901-barycentric-pick-product-localizer.md`
- source blob `7c012ec82a0e057275417c179314b9ccbeba158d`

---

## 5. Two sign-complete value channels

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

Moreover,

\[
B_T(u,v)=H_T(v)-uA_T(u,v)
=H_T(u)-vA_T(u,v).
\]

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

and

\[
\frac{B_{\rm pair}}{A_{\rm pair}}=-d.
\]

Straddling \(d\) makes \(A_{\rm pair}<0\); placing both nodes on one side makes \(B_{\rm pair}<0\). One rigorous negative channel suffices; the paired pattern is only a proposal diagnostic.

### Exact source

- `claims/lemmas/L-3902-two-channel-xi-pole-localizer.md`
- source blob `bb1a0da46d1a002945a7b0bdb57af58591105660`

---

## 6. Exact matched-pole Pick annihilator

Choose distinct positive rational nodes \(x_1,\ldots,x_n\) and rational \(d>0\) avoiding all \(x_i^2\). Let

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

and

\[
c_i=D(d)w_i(S_1-S_0x_i).
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

For a modeled same-ordinate reflected pair of multiplicity \(m\),

\[
K^{(d)}_{ij}
=
2m\frac{x_ix_j-d}
{(x_i^2-d)(x_j^2-d)},
\]

so

\[
c^{\mathsf T}K^{(d)}c=-2md.
\]

The positive rank-one component is annihilated exactly; the negative component remains.

### Mismatch polynomial

For actual squared displacement \(q\), define

\[
D_q=\prod_i(x_i^2-q),
\]

\[
U(q)=\sum_i c_ix_i\prod_{j\ne i}(x_j^2-q),
\qquad
V(q)=\sum_i c_i\prod_{j\ne i}(x_j^2-q).
\]

The isolated pair contribution is

\[
2m\frac{U(q)^2-qV(q)^2}{D_q^2}.
\]

At \(q=d\), its numerator is strictly negative, so exact polynomial enclosure can certify an open modeled-mismatch interval.

### Critical boundary

The value \(-2md\) belongs only to the modeled pair component. It is not the sign of the complete Riemann \(\xi\) function. All other zeros and completion terms remain inside the actual \(F\) evaluations. The vector must be frozen before direct outward contraction.

### Exact source

- `claims/lemmas/L-3904-matched-pole-pick-annihilator.md`
- source blob `c040b45ffc3ff2964f985e5535983c6112ed5878`

---

## Domain and normalization checklist

- Every point lies strictly in \(\Re s>1/2\).
- Every denominator is certified nonzero before evaluating \(F=\xi'/\xi\).
- Zeros are counted with multiplicity.
- The centered symmetric product fixes the zero-resolvent normalization.
- Squared nodes use the positive real square root.
- Divided-difference nodes are distinct.
- Cross-Loewner row and column lists are ordered and cross-disjoint.
- The kernel denominator is \(s+\bar w-1\), not \(s+\bar w\).
- The corrected direct evaluator uses \(+1/(s-1)\).

## Computational and assurance status

The source claims include exact synthetic controls. This packet does not include a directed actual-\(\xi\) negative result. The integration performed no Arb, FLINT, Riemann–Siegel, zero, or interval production replay.

## Common misreadings

- A positive finite matrix does not prove the global Pick kernel positive.
- A fitted rational model, surrogate, or midpoint eigenvector is proposal-only.
- Large barycentric weights can destroy a nominal moat.
- Real same-height constraints are not the complete complex Pick cone.
- A local zero census cannot retire a global predicate without a locality theorem.
- The false complex-center targeted Li family is not licensed by these theorems.
- Existential witness geometry does not say a predetermined finite grid will find the witness.

## Why this packet matters

It gives a coherent derivative-free finite disproof architecture whose algebra and local converse geometry survived independent exact-SHA review. The remaining burden is precise: authenticated primitive production and strict witness discovery.

## Exact next missing step

Construct a small proof-grade producer for exact point pairs or \(2\times2\) Loewner packets using a separately audited normalization and a distinct implementation. Freeze the points and rational contraction before final interval evaluation. Any strict negative survivor requires immediate independent reproduction.
