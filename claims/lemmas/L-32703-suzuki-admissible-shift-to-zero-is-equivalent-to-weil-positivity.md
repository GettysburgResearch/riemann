# L-32703 — In Suzuki's finite real-zero construction, a cofinal admissible shift tending to zero is equivalent to Weil positivity

Claim ID: `L-32703`  
Title: The unconditional finite real-zero theorem does not supply a near-zero cofinal Hilbert-space shift without already proving RH  
Status: **PROPOSED COMPLETE CROSS-ROUTE LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
External source: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026), Theorems 1.3 and 1.5, Corollary 1.6  
Scope: exact monotonicity/equivalence statement for the localized Weil lower eigenvalue; no RH proof

## 1. Suzuki's unconditional finite theorem

For each `a>0`, let `A_a` be the self-adjoint operator representing the Weil quadratic form restricted to `(-a,a)`, and let

\[
\lambda_a
=\inf_{0\ne v\in C_c^\infty(-a,a)}
\frac{Q_W(v)}{\|v\|_2^2}
\tag{L-32703.1}
\]

(the equality with the smooth-core infimum is Suzuki's Corollary 1.2).

For any real shift

\[
\lambda<\lambda_a,
\tag{L-32703.2}
\]

Suzuki forms the positive Hilbert-space norm associated with

\[
T_{a,\lambda}=A_a-\lambda I
\]

and realizes `i d/dx` as a symmetric operator of deficiency indices `(1,1)`. Every self-adjoint extension has a characteristic entire function `W(a,theta;z)` whose zeros are all real (Suzuki, Theorem 1.5). This finite real-zero theorem is unconditional.

Suzuki's conjectural RH limit is formulated in the `lambda=0` situation and the paper explicitly notes that controlling `lambda<lambda_a` is expected to be important in any proof of the limit.

## 2. Support monotonicity of the bottom eigenvalue

If

\[
0<a<b,
\]

then

\[
C_c^\infty(-a,a)\subset C_c^\infty(-b,b).
\]

The global Weil form and the ordinary `L^2` norm are unchanged on the embedded test function. Therefore

\[
\boxed{\lambda_b\le\lambda_a.}
\tag{L-32703.3}
\]

Thus `a -> lambda_a` is nonincreasing. Suzuki separately proves its continuity.

## 3. Cofinal near-zero admissibility implies Weil positivity

Assume there exists a function or sequence

\[
a_j\to\infty,
\qquad
\ell_j<\lambda_{a_j},
\qquad
\ell_j\to0.
\tag{L-32703.4}
\]

We claim

\[
\boxed{\lambda_a\ge0\quad\text{for every }a>0.}
\tag{L-32703.5}
\]

Suppose instead that `lambda_(a_0)<0` for some `a_0`. By monotonicity,

\[
\lambda_a\le\lambda_{a_0}=-\delta<0
\qquad(a\ge a_0)
\tag{L-32703.6}
\]

for some `delta>0`. For all sufficiently large `j`, `a_j>=a_0` and `ell_j>-delta/2`. Then

\[
\ell_j> -\delta\ge\lambda_{a_j},
\]

contradicting the admissibility `ell_j<lambda_(a_j)`.

Therefore (L-32703.5) holds.

By Weil's positivity criterion, (L-32703.5) is equivalent to RH.

## 4. Converse

Assume RH. Then the localized Weil quadratic form is nonnegative for every support radius, so

\[
\lambda_a\ge0
\qquad(a>0).
\]

Choose, for example,

\[
\ell(a)=-1/a.
\]

Then

\[
\ell(a)<\lambda_a,
\qquad
\ell(a)\to0.
\]

Hence

\[
\boxed{
RH
\iff
\exists\ a_j\to\infty,\ \ell_j<\lambda_{a_j},\ \ell_j\to0.
}
\tag{L-32703.7}
\]

## 5. Consequence for the finite-real-zero strategy

Suzuki's Theorem 1.5 is a genuinely unconditional and important finite theorem: every chosen admissible finite characteristic function has only real zeros.

However, a limiting argument cannot obtain the `lambda=0` regime by first proving that an admissible shift tends to zero. Equation (L-32703.7) shows that this step alone already proves RH.

Therefore a noncircular completion must do something subtler, for example:

1. prove the complex-function limit directly for shifts not known to approach zero and show that its zeros are shift-independent;
2. formulate the Fredholm limit in a coordinate in which `lambda` disappears exactly before the limit;
3. prove an arithmetic identity giving the target limit without any near-zero shift assertion.

Merely obtaining a lower bound `lambda_a>-epsilon_a` with `epsilon_a->0` is already a full RH theorem.

## 6. Relation to the repository's affine/prolate obstruction

The repo's `R-19846` proves a complementary fact: if RH is false, an even off-line Xi-cardinal quartet yields a fixed negative localized Weil direction while the Xi target has vanishing Weil value. Thus a cofinal ground-selection gate with vanishing target excess is itself RH-bearing.

`L-32703` identifies the same firewall in Suzuki's newer nonlocal first-order construction at the scalar shift level. The two approaches are not independent escape hatches from the sign obstruction.

## Proof boundary

Established:

- support monotonicity of `lambda_a`;
- equivalence (L-32703.7);
- exact scope correction for a near-zero-shift limit strategy.

Imported from Suzuki/Weil:

- the definition/core characterization of `lambda_a`;
- unconditional finite real-zero characteristic functions for every admissible shift;
- Weil positivity criterion.

Not established:

- Suzuki's conjectural limit formula;
- shift-independence of the finite characteristic functions;
- RH.
