# Where a numerical improvement still needs a new estimate

Date: 2026-10-20. Research note, not a new zero-free theorem.

The source throughout is Baiying Liu, *Zero-free half-planes for Hecke
L-functions over number fields*, arXiv:2610.26835v1, especially printed
pp. 46–48, 60–61, 64–85 and 88–94. The source PDF SHA256 is
`5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
The already prepared angular/unitary adapters are additional
source-dependent inputs. They do not change the numerical value
\(B_\flat=0.874886647039964\ldots\).

## 1. The direct theta estimate has a squarefree, cube-free extremal block

Use Liu's notation in the proof of Lemma 13.2. Near the current tangent,
\(\ell<1/5\). There is an admissible endpoint with

\[
d=O=A_0=N_0=B_0=S_0=\ell_b=0,\quad
H=v=1-\ell,\quad z_a=\ell,\quad N_*=1+\ell.
\]

Consequently \(T_d=H\), and
\[
u=\min(v,z_a,(v+z_a)/3)=\ell,
\qquad E=H.
\]

This gives the full \(Z^{1-\ell}\) theta mean in (13.6). Both the row and
the remaining squarefree numerator have norm length \(Z^{1-\ell}\); the
cube ideal is the unit ideal. An improvement which only sums a nontrivial
cube variable more efficiently cannot improve this block.

At this endpoint the remaining arithmetic matrix is
\[
\chi_R(n)^3\chi_P(n)^{-2}\mathbf1_{(R,P)=1},
\]
with squarefree \(R,n\) of the same length and the complete active selected
prime tuple \(P\) of length \(Z^\ell\). All finite unit phases and natural
zeros are retained. The prime tuple cannot be replaced by a positive
average of independent labels.

The exact coefficient in Lemma 10.2, with its frozen denominator absent,
is, up to a fixed finite unit character,
\[
\beta(n,1)=\Lambda(n)\gamma_2(n)\xi(n)
            =a_0(n)\Lambda(n)^2\xi(n).
\]
Indeed the product of the prime Gauss factors and their CRT multipliers is
\(\gamma_2(n)\), and reflection inverts the angular character
\(\bar\Lambda\). This is a prescribed angular Gauss coefficient, not an
arbitrary bounded sequence. However, regarding the displayed matrix as
one sextic twist creates the row \(R^3P^4\): its norm length is
\(3H+4\ell\), not \(H+\ell\). Applying the existing inverse estimate to
that enlarged row is outside the required range.

On squarefree ideals, the Gauss–Jacobi and CRT identities also give
\[
\beta(n,1)^3=\mu_F(n)\Lambda(n)^4\xi(n)^3.
\]
Cancellation for this cubic power does not give cancellation for
\(\beta(n,1)\). Even an arbitrary unit-modulus sequence with a prescribed
cubic power can choose every cube root in the arc with real part at least
one half. One needs the actual Gauss-sum structure to bridge that gap.

## 2. The additive factor's sixth-power modes are retained by the detector

Liu's (13.7) is
\[
\sum_k |\widetilde A[k]|^2
 \ll \frac{Q'}{Y'}\left(1+P_a^{1/6}+P_a^2/Y'\right)Z^\epsilon,
\quad P_a=Y'^2/Q'.
\]
The term \(P_a^{1/6}\) comes from genuine principal inducing characters in
the finite-correlation Poisson formula: the exterior valuations of the
dual frequency are all divisible by six. In the coprime column block
\(D=E=C=1\), the finite coefficient for such a principal frequency is one
on its allowed unit support. This is not an angular character sum to which
the new angular zero-free estimate can be applied.

The source's auxiliary ideal coefficient is exactly one. Inserting a
nontrivial angular coefficient there changes the reflected numerator
\(L(w,\chi_u)\) to an angular Hecke function and removes the \(w=1\) pole
which creates the principal target quotient. A projection or a changed
test must therefore prove that it retains the principal term; simply
deleting the coherent modes is not a numerical improvement.

The source bounds the theta mean and this additive mean separately. A
possible improvement is a bound on their *joint correlation*, exploiting
the prescribed \(\Lambda\gamma_2\) coefficient on the squarefree block
above. No such power saving is proved in this note.

## 3. What the new structured Gauss mean supplies

The primary rStation preprint *Structured cubic and sextic means for
angular Gauss coefficients*, v3, 17 October 2026, proves a prescribed
coefficient estimate over the Eisenstein integers. Its Theorem 5 gives
\[
\frac1F\sum_{f\asymp F}w(f)\sum_{0<Nz\le K}
 \left|\sum_{n\ {\rm sf}}\frac{\alpha(n)^j\gamma_2(n)\nu(n)}{\sqrt{Nn}}
   \chi_n(z)\chi_n(f)^4W(Nn/D)\right|^2
 \ll (KDFNQ)^\epsilon\min\{K+DF,K+KF\sqrt{NQ}\},
\]
for fixed nonzero angular order and its stated fixed puncture. Its
Theorem 6 gives an unmarked quadratic-theta mean of size \(K\), at every
column length. Both the positive label normalization and the absence of
an arbitrary residual column multiplier are essential.

Its §13 identifies the physical mark after a second reflection as
\(\mathbf1_{p\mid\mu}-1/Np\). An additive prime-divisor weight on an inverse
polynomial has the exact expansion
\[
\sum_n\frac{\mu(n)\psi(n)A(n)}{\sqrt{Nn}}W(Nn/Y)
=-\sum_{r\ge1}\sum_p
 \frac{\eta(p)\psi(p)^r}{(Np)^{r/2}}M_\psi(Y/(Np)^r).
\]
The \(r=1\) term is a genuine inverse-times-prime polynomial. Our angular
selected inverse adapter is proved for its stated families over
\(F\supseteq\mu_{12}\). It cannot automatically be applied over the
Eisenstein field \(E=\mathbb Q(\omega)\), which does not contain
\(\mu_{12}\). The unmarked angular estimate in rStation paper 5 does
not itself prove a selected-M1 theorem over \(E\). The precise abstract
marked transfer and this unproved field bridge are separated in
[MARKED_INVERSE_TRANSFER.md](MARKED_INVERSE_TRANSFER.md).

As an exponent substitution in a setting where both the structured
Gauss estimate and selected inverse input are available, at the direct
extremal block the second reflected length is
\(D_*=KL^2\). Its sextic Poisson image has row length \(T=KL^4\), ordinary
inverse length \(KL\), and prime length \(L\). The existing selected
inequalities hold at those lengths; the resulting conditional short
Gauss estimate
has a \(D_*\) term, which is larger than \(K\). The unmarked theorem itself
only recovers the already available \(K\) theta mean. These substitutions
do not yet lower the direct exponent.

Source: https://rstation.ai/problems/riemann_hypothesis/papers/5

## 4. An exact higher centering identity for three ordinary factors

There is a useful new algebraic comparison which is worth retaining even
though §5 below blocks a direct sixth-moment conclusion.

On the equal-total-length plane, let
\[
v_1=(1,-1,0),\quad v_2=(0,1,-1),\quad v_3=(-1,0,1),
\qquad
\mathcal D=\prod_{i=1}^3(1-T_{hv_i})^2.
\]
Here \(T_v\) translates the logarithmic triple of scale lengths by \(v\).
The finite operator has 19 nonzero support points, all with coordinate
sum zero. Its central coefficient is \(-6\), and its projection onto
each single coordinate is the zero signed measure. It therefore
annihilates constants and every function of one of the three scale
coordinates.

For a fixed common inducing character, common coprimality indicator and
common norm twist, write each *uncentralized* ordinary mean as
\[
F_i(T)=c_iT^{1+it}+E_i(T),\qquad E_i(T)=O(Z^\epsilon).
\]
On a plane where \(T_1T_2T_3\) is fixed, the triple product's all-main term
is constant. Each term with precisely one error, divided by its common
total main volume, is a function of that error's single scale coordinate.
Thus \(\mathcal D\) annihilates the all-main and all one-error terms. Every
remaining term contains at least two errors.

If \(s_2\) is the sum of the two smallest original plain length exponents,
and genuine extractions remove a total of at most \(v\) on the chosen
side, the two-error saving is at least \((s_2-v)_+\), up to the fixed
stencil displacement. The exact scalar identity is
\[
\inf_{v\ge0}\left\{\frac{2v}{3}+(s_2-v)_+\right\}=\frac{2s_2}{3}.
\]
The exceptional-row calculation in Liu §12.8.3 would consequently have
excess
\[
A-\frac{5M}{6}-\frac{2s_2}{3}
=\frac A3+\frac23\max_i n_i-\frac{5M}{6}\le0
\]
for any balanced triple \(n_i\le M/2\), \(A=n_1+n_2+n_3\le3M/2\).
This is the precise reason three-factor centering is promising.

Dividing each coordinate by a fixed extracted ideal, identical at every
stencil vertex, preserves the zero one-coordinate projections after
translation. The complete whole-column character and common norm twist
must be retained. Distinct explicit twists varying with the vertices
would destroy this cancellation. Fixed incoming norm modes can first be
absorbed into the normalized profiles with their original scalar factors
kept outside, as specified in the separate eight-point comparison.

This is an algebraic/fixed-character lemma, not a sixth-moment theorem.
No finite add-back closure for this nineteen-point stencil is proved
here. The separate [TRIPLE_COMPARISON.md](TRIPLE_COMPARISON.md) proves an
eight-point comparison and a finite buffered rank under its explicit
ordinary reflection interface. That result retains the same
fixed-character cancellation, but does not remove the separate positive
diagonal described next.

## 5. The second diagonal is a separate and concrete sixth-moment barrier

Liu §12.7.3, printed p.77, states that the second finite-correlation
Poisson sum at \(j=0\) is zero unless its whole columns satisfy \(u=v\).
For \(u=v\), the finite coefficient is \(\varphi(u)\). Its nominal excess
over the permitted normalization is
\[
A-M-d-(K_0-K)-w_o-B_c+g-\ell
\le A-M+5\sigma/3+\delta_1.
\]
This precedes the exceptional-character calculation of §12.8.3. For
three central half-length factors, \(A=3M/2\), its allowance has a genuine
\(M/2\) excess.

Higher centering does not automatically power-save the squared
convolution coefficient on \(u=v\). For example, take three nonnegative
smooth norm profiles with positive interior annuli, and consider columns
formed from three primes in those annuli at length \(Z^{M/2}\). Use a
fixed nonzero logarithmic stencil displacement. The profiles themselves
are ordinary norm profiles, without a prime indicator.
Whole columns formed from three such primes have every available
nontrivial divisor length near an integer multiple of \(M/2\). The
noncentral comparison rectangles have a factor at a polynomially
different length. On such columns those rectangles vanish, whereas the
original triple coefficient is positive. There are
\(Z^{3M/2-o(1)}\) such columns, after bounded permutation multiplicity.
Hence a general bound replacing their squared coefficient mass by a
power-smaller mass cannot follow from the centering identity alone.

The artificial origin of this diagonal suggests a different research
question. Before the first Cauchy step, (12.2) retains \((a,b)=1\), so
\(a=b\) implies \(a=b=1\). The full Möbius expansion of that coprimality
condition cancels a nonunit diagonal exactly. The source bounds its
sectors separately by positive norms, and that cancellation is lost.
To use it, one must retain the signed cross-correlation, its complete
common Gauss factor, and both transformed character presentations through
an effective amplification and the next Poisson step. Merely applying
Poisson twice returns the previous expression and supplies no width
decrease. A valid signed amplification/descent estimate is currently
missing.

Accordingly this audit does not claim a sixth moment of size
\(U^{1+\epsilon}\), a changed numerator Hölder exponent, or a zero-free
boundary below \(B_\flat\).
