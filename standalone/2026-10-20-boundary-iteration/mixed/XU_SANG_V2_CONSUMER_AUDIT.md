# Xu--Sang v2: consumer and centering audit

20 October 2026. This is an interface calculation, not a new
zero-free estimate. Source:
[Xu--Sang, arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
14 October 2026, Sections 3, 5, 6 and 7. The corresponding inherited
consumer is Liu, Sections 13--14, as pinned in the parent packet.

## 1. The new prime theorem uses the existing unmarked count

Xu--Sang Proposition 6.3 explicitly identifies its first count branch
with \(R_\kappa(\delta,0)\), where \(\delta=2a-1\):

\[
 \mathcal R(a)=\frac{31-32a}{21-12a}
   =\frac{15-16\delta}{15-6\delta},\qquad a\le11/12.
 \tag{X1}
\]

Their Theorem 1.2 prime moment is the optimization

\[
 \max_a\{\mathcal R(a)+2a\}
 =\frac{37-10\sqrt6}{6},\qquad
 a_* =\frac{21-5\sqrt6}{12}.                            \tag{X2}
\]

The branch above \(11/12\) gives exponent two. Thus (X2) is a
useful structured-coefficient consequence of the imported moments;
it does not strengthen the selected count
\(R_\kappa(\delta,x)\) already used in the current boundary.

Proposition 7.2 permits independently specified smooth rough-prime
convolutions with product of prime lengths \(Y\), over
sixth-power-free indices of norm \(\asymp Y\). Its upper bound is
\(Y^{\kappa_6+\varepsilon}+Y^{13/6-c+\varepsilon}\), where every
supported prime has norm at least \(Y^c\). It does not permit
arbitrary row-dependent coefficients. The actual terminal character
in `TERMINAL_INTERFACE.md` is

\[
 \chi_R(n)^3\chi_P(n)^{-2}
    =\chi_n(R^3P^4)\quad\text{up to its retained fixed ray phase}.
 \tag{X3}
\]

For disjoint squarefree \(R,P\), its index norm is \(K^3L^4\),
whereas the binding column length is \(U\asymp KL\).
Moreover, its actual \(n\)-coefficient includes the angular cubic
Gauss coefficient, whereas Proposition 7.2 requires a rough-prime
convolution. Even if a separate reduction supplied that coefficient
class, it could not be inserted with \(Y=U\).
Changing a coefficient norm or enlarging an indexed family does not
remove this mismatch. A new estimate ordered by the two conductor
parameters would be needed.

## 2. The improved Gram error is not the binding old term

Proposition 3.1 has Gram main term

\[
 C_{S,w}\left|\mathcal I(U)\right|^2q^{5/6}L^{-2/3}
       \Omega(\mathfrak d,\mathbf e),\qquad
 \mathcal I(U)=\int_0^\infty U(t)t^{-5/6}\,dt,           \tag{X4}
\]

and error
\((2qLD)^\varepsilon\{(q/L)(1+(L^2/q)^{1/12})+D\}\).
The improvement over v1 replaces its final error \(D L^2/q\)
by \(D\). At \(q=XY,L=Y,D=O(1)\), the main term is still
\(X^{5/6}Y^{1/6}\). Its square root gives precisely the
\(b/12\) contribution already in Liu's low exponent for \(Y>X\).
Improving a smaller error alone does not remove this main term.

## 3. The centered profile must match the actual additive factor

Xu--Sang Lemma 5.1 compares two column profiles with equal
\(\mathcal I\), so their rank-one main terms cancel. It is tempting
to choose a signed profile with \(\mathcal I=0\) in the detecting
probe. The original additive factor has a coupled profile, however:

\[
 \widetilde A_{[k]}=Y^{-1/2}\sum_s q_s^{-1}g_s(-k)
 W_1(q_s/Y)\Omega(q_k/(q_sX)),\qquad
 \Omega(v)=\int_G W_0(t\ell_v)\,dt .                   \tag{X5}
\]

This is Liu Section 13.2, paragraph beginning “For (13.7), orbit
unfolding gives.” Set \(Q=XY\), \(v=q_k/Q\), \(t=q_s/Y\),
and \(G(s,-k)=q_s^{-1/2}g_s(-k)\). Then the sum is

\[
 Y^{-1}\sum_s G(s,-k)t^{-1/2}U_v(t),\qquad
 U_v(t)=W_1(t)\Omega(v/t).                              \tag{X6}
\]

Consequently the candidate profile-main cancellation is a family
of conditions, not one condition on an arbitrary isolated test:

\[
 A(v):=\mathcal I(U_v)
   =\int_0^\infty W_1(t)t^{-5/6}\Omega(v/t)\,dt=0.
 \tag{X7}
\]

There is an exact Mellin obstruction to imposing (X7) identically.
With \(\widehat f(z)=\int_0^\infty f(v)v^z\,dv/v\),
compact support and Fubini give

\[
 \widehat A(z)=\widehat W_1(z+1/6)\widehat\Omega(z),
 \qquad
 \widehat A(5/6)=\widehat W_1(1)\widehat\Omega(5/6).
 \tag{X8}
\]

The local Tate functional equation used by Liu Section 13.2
identifies \(\mathcal M(1/6)\) with a fixed nonzero gamma
factor times \(\widehat\Omega(5/6)\). The principal high-side
normalizer in Liu Section 13.3 is

\[
 c_S=\widehat W_1(1)\mathcal M(1/6)
           (\operatorname{Res}_1\zeta_F^S)^2/6.         \tag{X9}
\]

Thus \(A\equiv0\) forces \(c_S=0\), removing the detector's
principal signal. This argument permits signed \(W_1,W_0\);
positivity of \(W_1\) is not the obstruction. A profile depending
on the row cannot be substituted freely into a theorem for a fixed
column array either.

This is only the exact test of the proposed use of the rank-one
profile functional. We do not assert an asymptotic Gram formula for
every coupled profile in (X5), nor rule out a different centered
comparison retaining additional correlations. In particular it does
not settle the signed canonical centering problem in
`CENTERED_INVERSE_INTERFACE.md`, which concerns the inverse
Poisson identity and its full common-divisor sum.

The v2 source therefore adds useful structured prime consequences
and a sharper generic lower bound, but no numerical improvement to
the current boundary has been established by these direct imports.
