# L-91025 — The positive Jordan anchor's cubic logarithmic jet has exactly three orthogonal detail ports

Claim ID: `L-91025`  
Status: **PROPOSED COMPLETE EXACT HILBERT/ANOVA THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`, `L-91019`, `L-91022`  
RH status: **unproved**

## 1. Positive anchor and orthogonal polynomials

Let `eta_a` and the positive anchor law `P_a` be as in `L-91019`.  Write

\[
 T=\log n
\]

for the self-adjoint multiplication operator on the anchor space.  Let

\[
 p_{0,a},p_{1,a},p_{2,a},p_{3,a}
\]

be the orthonormal polynomials obtained from `1,T,T^2,T^3` by Gram--Schmidt in
`L^2(P_a)`, with positive leading coefficients.  Put

\[
 e_{j,a}=p_{j,a}(T)\eta_a.
 \tag{L-91025.1}
\]

The vectors `e_(0,a),...,e_(3,a)` are orthonormal.  If a moment Gram degenerates,
the corresponding zero-norm port is simply deleted; for the infinite anchor
support here the full Gram is strictly positive.

## 2. Exact cubic coproduct

Let `H` carry a self-adjoint logarithmic generator `L` and put

\[
 L_{\rm tot}=L\otimes I+I\otimes T.
\]

For `j=0,1,2,3`, define the scalar polynomial

\[
 \boxed{
 A_{j,a}(\lambda)
 =\mathbb E_a[(\lambda+T)^3p_{j,a}(T)].
 }
 \tag{L-91025.2}
\]

Its degree is at most `3-j`.  Orthogonal expansion in the anchor variable gives

\[
 \boxed{
 L_{\rm tot}^3(f\otimes e_{0,a})
 =\sum_{j=0}^3A_{j,a}(L)f\otimes e_{j,a}.
 }
 \tag{L-91025.3}
\]

There is no remainder because `(lambda+T)^3` has degree three in `T`.

## 3. Coefficient-one returned state

The returned coefficient is

\[
 \boxed{
 A_{0,a}(\lambda)
 =\mathbb E_a[(\lambda+T)^3]
 =\lambda^3+3m_{1,a}\lambda^2
  +3m_{2,a}\lambda+m_{3,a},
 }
 \tag{L-91025.4}
\]

where `m_(r,a)=E_a[T^r]`.  This is the delayed coarse cubic jet with the exact
affine/moment corrections forced by the positive anchor.

The remaining polynomials `A_(1,a),A_(2,a),A_(3,a)` are the three emitted source
details.

## 4. Exact positive four-state identity

Taking norms in (L-91025.3),

\[
 \boxed{
 \|L_{\rm tot}^3(f\otimes e_0)\|^2
 =\|A_{0,a}(L)f\|^2
  +\sum_{j=1}^3\|A_{j,a}(L)f\|^2.
 }
 \tag{L-91025.5
}
\]

The polarized identity is positive semidefinite for arbitrary independent
carrier vectors before aggregation.

Hence the cubic positive-source state has exactly the architecture

```text
one coefficient-one returned coarse state
+ three orthogonal emitted detail states.
```

## 5. Moment-matrix formula

Let

\[
 G_a=(m_{r+s,a})_{0\le r,s\le3}
 \tag{L-91025.6}
\]

be the positive moment Gram and let `G_a=L_aL_a^*` be its Cholesky
factorisation.  In the monomial basis, the vector of coefficients of
`(lambda+T)^3` is

\[
 c(\lambda)=(\lambda^3,3\lambda^2,3\lambda,1)^T.
\]

Then the orthogonal port vector is

\[
 \boxed{
 (A_{0,a}(\lambda),...,A_{3,a}(\lambda))^T
 =L_a^*c(\lambda),
 }
 \tag{L-91025.7
}
\]

up to the fixed triangular convention for the orthonormal polynomials.  Thus all
source-port coefficients are explicit algebraic functions of the first six
anchor moments, hence of derivatives of `log Q_a` at `1+2a`.

## 6. Match to the sixteenfold residual

`L-91022` proves that the coefficient-one normalized Cauchy recurrence emits
exactly three rational square ports

\[
 \widetilde r_{1,a},\widetilde r_{2,a},\widetilde r_{3,a}.
\]

Equation (L-91025.5) proves independently that the positive source cocycle emits
exactly three orthogonal cubic-jet ports after its returned state is removed.
Therefore there is no dimension or signature obstruction to a lossless
source/physical intertwiner: both detail spaces are positive three-dimensional
Hilbert spaces.

The remaining theorem is an equality of their carrier-dependent Gram metrics,
possibly after one explicit `SO(3)` change of detail basis.  No fourth state,
signed source direction, or asymptotic truncation is permitted or required.

## 7. All-generation stability

Because the divisor isometries are coassociative, the cubic decomposition may be
iterated through every dyadic scale.  At each generation the same rule applies:
one coarse cubic state returns and exactly three fresh orthogonal details are
emitted.  The state dimension remains four; only output ports accumulate.

## 8. Boundary

Closed:

```text
strict positive cubic moment Gram;
exact one-plus-three cubic coproduct;
source-side independent-frequency PSD;
explicit moment/Cholesky construction;
state-count match with the sixteenfold Cauchy residual;
all-generation no-proliferation.
```

Open:

```text
explicit unitary/orthogonal intertwiner between source and physical three-port metrics;
completed gamma/pole matching in that intertwiner;
prime-side residual positivity;
RH.
```
