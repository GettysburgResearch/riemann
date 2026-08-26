# Exact two-place cumulant defects in the quadratic genus-two family

Status: **PROVED** for every odd prime power (q). The packet computes a
complete two-place joint law and its mixed cumulant defects; it proves no
zero theorem, RH implication, or principal-member amplifier.

## Start here

Let

\[
 \mathcal H_5(q)={D\in\mathbf F_q[T]:D\text{ monic squarefree},\deg D=5}.
\]

Choose distinct rational places (a,b\in\mathbf F_q), and put

\[
 X_D=\chi(D(a)),\qquad Y_D=\chi(D(b)),
\]

where (chi(0)=0). These are the local quadratic Euler coefficients at
(T-a) and (T-b). Write

\[
 \epsilon=\chi(-1),\qquad s=\chi(b-a).
\]

The complete family has size

\[
 A=q^4(q-1).
\]

Define

\[
\begin{aligned}
 V&=q^5-2q^4+2q^3-2q^2+2q-1,\\
 W&=q^5-3q^4+5q^3-7q^2+9q-6,\\
 C&=2q-3,
\end{aligned}
\qquad
 v={V\over A},\quad w={W\over A},\quad c={C\over A}.
\tag{1}
\]

Then the six moments determining the joint law are

\[
\boxed{
\begin{aligned}
 \mathbb E X=\mathbb E Y&=0,\\
 \mathbb E X^2=\mathbb E Y^2&=v,\\
 \mathbb E(XY)&=c,\\
 \mathbb E(X^2Y)&=sc,\\
 \mathbb E(XY^2)&=\epsilon sc,\\
 \mathbb E(X^2Y^2)&=w.
\end{aligned}}
\tag{2}
\]

In particular, the two places have identical centered one-place laws but are
not independent:

\[
 \operatorname{Cov}(X,Y)={2q-3\over q^4(q-1)}>0.
\tag{3}
\]

This is the first arithmetic mixed-place residual requested by the detector
renormalization packet. It is an all-field theorem, not a fit to three
characteristics.

## 1. The five tiny Euler products

For a Dirichlet character (psi), squarefree Euler factorization gives

\[
 \sum_{D\ {m monic\ squarefree}}\psi(D)u^{\deg D}
 =\prod_P(1+\psi(P)u^{\deg P})
 ={L(u,\psi)\over L(u^2,\psi^2)}.
\tag{4}
\]

The degree-one character (D\mapsto\chi(D(a))) has (L)-polynomial (1):
for every positive degree, evaluation at (a) is uniform and the nontrivial
character sum vanishes. The product character
(D\mapsto\chi(D(a)D(b))) has (L)-polynomial (1-u). Its degree-one row is

\[
 \sum_{z\in\mathbf F_q}\chi((a-z)(b-z))=-1,
\tag{5}
\]

because (z\mapsto(a-z)/(b-z)) maps
(mathbf F_q\setminus\{b}) bijectively to
(mathbf F_q\setminus\{1}); all higher rows vanish by the uniform joint
evaluation map.

Consequently the five generating functions needed at degree five are

\[
\begin{array}{c|c}
\text{row}&\text{generating function}\\ \hline
\#\mathcal H_5&(1-qu^2)/(1-qu)\\
\mathbf1_{X\ne0}&(1-qu^2)/((1-qu)(1+u))\\
\mathbf1_{X\ne0,Y\ne0}&(1-qu^2)/((1-qu)(1+u)^2)\\
X&(1-qu^2)/(1-u^2)\\
XY&(1-u)(1-qu^2)/(1-u^2)^2.
\end{array}
\tag{6}
\]

The degree-five coefficients are respectively (A,V,W,0,C). To get the
mixed rows, remove the unwanted rational Euler factor from the one-character
product:

\[
 {1-qu^2\over(1-u^2)(1+\sigma u)},
\tag{7}
\]

whose degree-five coefficient is (sigma(2q-3)). Here
(sigma=s) for (X^2Y) and (sigma=epsilon s) for (XY^2). This proves
(2).

## 2. The full (3\times3) joint law

For (x,y\in\{-1,1}), the exact cell counts are

\[
\boxed{
 N_{x,y}={W+ysC+x\epsilon sC+xyC\over4}.}
\tag{8}
\]

The axis and ramified cell counts are

\[
\boxed{
\begin{aligned}
 N_{x,0}&={V-W-x\epsilon sC\over2},\\
 N_{0,y}&={V-W-ysC\over2},\\
 N_{0,0}&=A-2V+W.
\end{aligned}}
\tag{9}
\]

Equations (8)--(9) are integral, nonnegative, and sum to (A). They are also
an exact finite-field explanation for the orientation dependence: the fixed
monic odd-degree model remembers both (chi(b-a)) and (chi(-1)).

## 3. Exact renormalization residual

Let

\[
 \Delta_m=\kappa_m(X+Y)-\kappa_m(X)-\kappa_m(Y).
\tag{10}
\]

This is precisely the mixed-place cumulant defect omitted by an independent
Euler-factor model. Put

\[
 u=s(1+\epsilon)c.
\]

Moment--cumulant inversion applied to (2) gives

\[
\boxed{
\begin{aligned}
 \Delta_2={}&2c,\\
 \Delta_3={}&3u,\\
 \Delta_4={}&8c+6w-6v^2-24vc-12c^2,\\
 \Delta_5={}&15u(1-4(v+c)),\\
 \Delta_6={}&32c+30w-30(v+c)(2v+8c+6w)-90u^2\\
             &\quad+240(v+c)^3+30v^2-60v^3.
\end{aligned}}
\tag{11}
\]

Thus every first residual channel has the same finite-family scale:

\[
\boxed{
\begin{aligned}
 \Delta_2&=4q^{-4}+O(q^{-5}),\\
 \Delta_3&=6s(1+\epsilon)q^{-4}+O(q^{-5}),\\
 \Delta_4&=-32q^{-4}+O(q^{-5}),\\
 \Delta_5&=-90s(1+\epsilon)q^{-4}+O(q^{-5}),\\
 \Delta_6&=544q^{-4}+O(q^{-5}).
\end{aligned}}
\tag{12}
\]

When (q\equiv3\pmod4), the odd aggregate defects vanish exactly. When
(q\equiv1\pmod4), their sign remembers the squareclass of the oriented
separation (b-a). The even defects remain.

## 4. Interpretation

The result makes three methodological points exact.

1. Complete one-place laws do not determine the two-place detector flow.
   Here the one-place means are zero and the marginals agree, yet
   (Delta_2>0).
2. The first arithmetic residual is small but structured: all five displayed
   cumulant defects begin at order (q^{-4}), not at unrelated scales.
3. Conditioning and orientation expose odd channels. Center symmetry at one
   place does not force the aggregate odd cumulants to vanish when
   (q\equiv1\pmod4).

This coupling comes from the fixed-degree squarefree ensemble. It is not
evidence for a mysterious motive, a zero bias, or an RH detector. A next
cohomological experiment would replace the two rational Euler coefficients by
a nuisance-quotiented character observable and track the exact same-prime
extension tower; that stronger recurrence question remains open.

## 5. Provenance and replay

The conceptual source is the mixed-prime residual definition in
`EULER_DETECTOR_RENORMALIZATION_FLOW.md`, frozen at commit
`fe9ba35f67e39c5706cef79d2e7cefd07fce7d67`, blob
`e1740dd014cd0f43222b8ec73a09ee1374b7f3cc`. The present proof is otherwise
self-contained.

The producer performs formal series algebra only through degree five and
exact rational moment--cumulant inversion only through degree six. The
`q=3,5,7` rows are formula evaluations, not family enumerations or proof
inputs.

```text
python research/l-families/atlas/function_field/quadratic_family_two_place_cumulant_defect.py --check
python -O research/l-families/atlas/function_field/quadratic_family_two_place_cumulant_defect.py --check
python -m pytest -q tests/test_quadratic_family_two_place_cumulant_defect.py
python -O -m pytest -q tests/test_quadratic_family_two_place_cumulant_defect.py
```

No external novelty claim is made.
