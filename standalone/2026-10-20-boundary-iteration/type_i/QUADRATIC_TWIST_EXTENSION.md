# A conductor-explicit quadratic twist of the averaged cubic block

Date: 2026-10-20. Status: proposed theorem, with proof for review.
This extends the object in [AVERAGED_TYPE_I.md](AVERAGED_TYPE_I.md).
It does not prove a new zero-free boundary. In particular, the conductor
cost below is too large in the currently binding sextic terminal range.

The imported ingredients are Dunn--Radziwill,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
Lemma 5.2, Lemma 5.3, Proposition 5.1, the coefficient formulas
(5.7), (5.13), (5.14), and the unconditional cubic large sieve
(Theorem 9.1). The extension of the cube identity from Lemma 5.4 to
a noncubic character is proved below; it is not imported as a statement
of that lemma.

## 1. Exact object and estimates

Use primary generators in \(E=\mathbb Q(\omega)\), and
\(\alpha(z)=z/|z|\). Fix \(\ell\ne0\). Let \(r\) be squarefree,
\(R=Nr\), and let \(\xi\) be a primitive quadratic character of conductor
\(S\), with \(H=NS\), \((r,S)=1\), and \((3,rS)=1\).
The trivial character of conductor 1 is allowed. Let \(A,B\ge1\),
let the two smooth compactly supported weights be fixed, and let
\(|b_v|\le1\). Set

\[
 T_\xi=\sum_{u,v}b_v\widetilde g(uv)\alpha(uv)^\ell
  \overline{(uv/r)_3}\xi(uv)W_A(Nu/A)W_B(Nv/B).
 \tag{Q1}
\]

Every common-prime zero in this formula is retained. In particular only
squarefree \(u,v\) with \((u,v)=1\), \((uv,rS)=1\) can contribute.

**Unconditional assertion.** Uniformly in \(r,S,\xi\),

\[
 |T_\xi|\ll_{\ell,W_A,W_B,\epsilon}(ABRH)^\epsilon
 \begin{cases}
 A^{1/2}B^{11/10}R^{1/5}H^{2/5},&RH^2\le B^2,\\
 A^{1/2}B R^{1/4}H^{1/2},&RH^2\ge B^2.
 \end{cases}
 \tag{Q2}
\]

The trivial bound \(O(AB)\) and any independently proved pointwise bound
may be intersected with this estimate.

Here is the exact optional input for the conditional improvement. Given
\(1/2\le\beta<1\), set \(p=(2\beta+1)/6\). For each fixed
\(\delta,\epsilon>0\), assume, uniformly over the quadratic family under
consideration,

\[
 |L(3(p+\delta+it)-1/2,\xi\alpha^{3\ell})^{-1}|
  \ll_{\ell,\delta,\epsilon}
  H^\epsilon(1+|t|)^C.
 \tag{Q3}
\]

The \(L\)-function here uses the primary-generator convention, with the
fixed ramified Euler factor deleted. The constant and \(C\) do not depend
on \(S\) or \(\xi\). This is a quantitative assumption, not merely a
separate zero-free assertion for each member with uncontrolled constants.
The common zero-free hypothesis plus a uniform reciprocal theorem can
supply (Q3); that implication is a separate interface.

Under (Q3), (Q2) becomes

\[
 |T_\xi|\ll(ABRH)^\epsilon
 \begin{cases}
 A^pB^{3/2-4p/5}R^{1/2-3p/5}H^{1-6p/5},
          &RH^2\le B^2,\\
 A^pB^{3/2-p}R^{(1-p)/2}H^{1-p},
          &RH^2\ge B^2.
 \end{cases}
 \tag{Q4}
\]

## 2. Cube completion for a general primitive character

For a squarefree \(k\) coprime to \(S\), write \(K=Nk\),
\(m=kS\), \(M=Nm=KH\), and
\(\psi=\overline{(\cdot/k)_3}\xi\), a primitive character modulo \(m\).
Define

\[
 \mathcal R_{k,\xi}(s)=
 \sum_c\widetilde g(c)\overline{(c/k)_3}\xi(c)
                   \alpha(c)^\ell(Nc)^{-s},
 \qquad
 Q_{k,\xi}(s)=Z_{k,\xi}(3s-1/2,3\ell)\mathcal R_{k,\xi}(s),
 \tag{Q5}
\]

where

\[
 Z_{k,\xi}(z,3\ell)
  =\sum_{(d,k)=1}\xi(d)\alpha(d)^{3\ell}(Nd)^{-z}.
 \tag{Q6}
\]

This is \(L(z,\xi\alpha^{3\ell})\) with the Euler factors at \(k\)
deleted. It is the correct factor because
\(\psi(d)^3=\mathbf1_k(d)\xi(d)\), including its zero extensions.

To verify the completion, the coefficient of the theta series on
\(\mu=\lambda^{-3}cd^3\) is a fixed constant times
\(\widetilde g(c)(Nd)^{1/2}\). Twisting it by
\(\psi(\lambda^4\mu)\) gives
\(\psi(\lambda)\psi(c)\psi(d)^3\).
Summing over \(d\) therefore produces exactly (Q6), with no restriction
discarded. With the raw Dirichlet series \(\mathcal D_F\) of DR (5.44),
the exact identity in the absolutely convergent half-plane is

\[
 Q_{k,\xi}(s)=
 (-1)^\ell i^\ell\psi(\lambda)^{-1}
       3^{-5/2-3s}\mathcal D_F(s;\psi,\ell)_S .
 \tag{Q7}
\]

This is the direct coefficient proof behind Lemma 5.4, now with
\(\psi^3\) in its Euler factor. Proposition 5.1 makes (Q7) entire for
\(\ell\ne0\).

## 3. The finite transform and its full conductor cost

Write \(\chi_m=(\cdot/m)_3\), and put
\(\kappa=\xi\chi_S\). This is a primitive character modulo \(S\).
Indeed, at a prime power dividing \(S\), a quadratic character primitive
at that exponent cannot become imprimitive after multiplication by a
character of order dividing three: on the last nontrivial conductor
kernel, cancellation would make a character have order both two and
three. The same observation handles the conductor-1 trivial case.

The primitive Gauss transform satisfies
\(\widehat\psi(d)=\overline{\psi(d)}\tau_m(\psi)\), with
\(|\tau_m(\psi)|=\sqrt M\); it vanishes for nonunit \(d\).
Consequently the hypothesis on \(\widehat\psi\) in DR Lemma 5.2 holds.
Substitution in its finite transform (5.22)--(5.23) gives, for a unit
constant \(\eta\) independent of \(u\),

\[
 \widetilde\psi(u)
   =\eta\,\tau_m(\psi)
       \sum_{a\bmod m}^{*}\psi(a)\chi_m(a)\check e(au/m).
 \tag{Q8}
\]

This follows from \(ad\equiv\lambda^{-8}\pmod m\), so that
\(\overline{\psi(d)}\) is a fixed unit times \(\psi(a)\).
Since \(\psi\chi_m=\mathbf1_k\kappa\), the Chinese remainder theorem
factors the sum in (Q8) into a Ramanujan sum modulo \(k\) and a primitive
Gauss sum modulo \(S\). Unit changes of the additive variables alter
only the fixed phase and the unit value of the character. Thus

\[
 \boxed{|\widetilde\psi(u)|
    =K^{1/2}H\,|c_k(u)|\,\mathbf1_{(u,S)=1}.}
 \tag{Q9}
\]

For squarefree \(k\),
\(|c_k(u)|=\varphi_E((u,k))\). Equation (Q9) is the reason that a
growing quadratic twist costs an extra factor \(H\) on the dual side.

## 4. Absolute mass of the raw theta dual

The raw dual \(\mathcal D_G(w;\widetilde\psi,-\ell)\) from
Proposition 5.1 has coefficients on

\[
 \mu=\lambda^j\zeta c d^3,\qquad j\ge-4,\quad
 \mu_E^2(c)=1,\quad c,d\equiv1\pmod3.
 \tag{Q10}
\]

The explicit theta formulas (5.7), (5.13), (5.14) imply

\[
 |a^*(\mu)|\ll3^{j/6}(Nd)^{1/2}.
 \tag{Q11}
\]

Only a subset of the displayed support occurs, which can be enlarged
for an upper bound. Split \(c=h w\), where \(h\mid k\) and \((w,k)=1\).
By (Q9),

\[
 \frac{|\widetilde\psi(\lambda^4\mu)|}{K^{1/2}H}
 \le Nh\,N\operatorname{rad}((d,k)).
 \tag{Q12}
\]

Fix \(j,\zeta,h,d\) and sum over
\(Nw\le T/(3^jNh(Nd)^3)\). For fixed \(\sigma>0\), the same elementary
lattice count as in (11)--(12) of the cubic-only note gives

\[
 \sum_{N\mu\le T}
  |a^*(\mu)|\,
  \frac{|\widetilde\psi(\lambda^4\mu)|}{K^{1/2}H}
  (N\mu)^{\sigma-1}
 \ll_{\sigma,\epsilon}T^\sigma K^\epsilon .
 \tag{Q13}
\]

For clarity, after the \(w\)-sum the summand is bounded by
\(T^\sigma3^{-5j/6}N\operatorname{rad}((d,k))(Nd)^{-5/2}\).
The \(h\)-sum costs \(\tau_E(k)\). The \(d\)-sum is bounded uniformly:
at a prime of norm \(q\) dividing \(k\), its local factor is
\(1+q^{-3/2}/(1-q^{-5/2})\); elsewhere it is
\((1-q^{-5/2})^{-1}\). Both products converge. The finite units and
ramified geometric sum are harmless. Fractional norms require only
\(T\ge3^{-4}\), with a changed constant.

This proof treats the full raw theta dual. It does not remove a cube
Euler factor and then forget to restore its coefficients.

## 5. Free split and large sieve

Using (Q7), Lemma 5.3 and Proposition 5.1 directly, the functional
equation has a conductor factor

\[
 K^{1/2-2s}H^{1-2s}
 \tag{Q14}
\]

times the gamma quotient from the cubic-only note, a unit phase, a
fixed power of \(3^s\), and a dual series whose coefficient mass is
(Q13). Keeping the raw theta normalization in this step avoids any
ambiguity from rescaling the fractional Fourier index. Fixed factors
of 3 rescale the dual weight only.

The contour argument of (15)--(18) in the cubic-only note therefore gives

\[
 |J_{k,\xi}(\sigma+it;Y)|
  \ll_{\ell,\sigma,\epsilon}
 (1+|t|)^C K^{1/2+\epsilon}H\,Y^{-\sigma},
 \qquad 1\le Y\le (KH)^2 .
 \tag{Q15}
\]

The effective dual length is a fixed constant times
\((KH)^2/Y\), and substitution of (Q13) cancels the factors
\(K^{-2\sigma}H^{-2\sigma}\) in (Q14). The implied constant in (Q15)
is independent of \(S,\xi\).

Average over \(k=rv\), with \(v\asymp B\), squarefree and
\((v,rS)=1\). On the original side the column coefficient gains
\(\xi(c)\), while the cube coefficient gains \(\xi(d)\).
Both have modulus at most one, so exactly the same unconditional cubic
large sieve and Minkowski argument applies. For \(0<\sigma<1/2\),

\[
 \|Q_{rv,\xi}(\sigma+it)\|_2
 \ll (1+|t|)^C(BRHY)^\epsilon
 \left(
 B^{1/2}Y^{1/2-\sigma}+Y^{1-\sigma}
 +B^{1/3}Y^{5/6-\sigma}
 +BR^{1/2}H Y^{-\sigma}
 \right).
 \tag{Q16}
\]

If \(RH^2\le B^2\), choose
\(Y=B^{4/5}R^{3/5}H^{6/5}\). Then
\(B^{1/2}\le Y\le B^2\), the first two terms are at most the third,
and the last two balance. This gives

\[
 \|Q_{rv,\xi}(\sigma+it)\|_2
 \ll (1+|t|)^C(BRH)^\epsilon
 B^{1-4\sigma/5}R^{1/2-3\sigma/5}H^{1-6\sigma/5}.
 \tag{Q17}
\]

If \(RH^2\ge B^2\), choose \(Y=BR^{1/2}H\), so \(Y\ge B^2\).
The second term dominates the first and third and balances the fourth:

\[
 \|Q_{rv,\xi}(\sigma+it)\|_2
 \ll (1+|t|)^C(BRH)^\epsilon
 B^{1-\sigma}R^{(1-\sigma)/2}H^{1-\sigma}.
 \tag{Q18}
\]

Both choices satisfy \(Y\le(RBH)^2\).
For \(\sigma=1/2+\delta\), \(0<\delta<1/8\), replace the first term
of (Q16) by \(B^{1/2}\), as in the proof of (28) in the cubic-only note.
The other displayed terms and their balances remain valid and dominate
\(B^{1/2}\).

## 6. Removing the completion and returning to the sum

Twisted multiplicativity gives the exact identity

\[
 T_\xi=\frac1{\widetilde g(r)}
 \sum_{\substack{v\text{ squarefree}\\(v,rS)=1}}
 b_v\alpha(v)^\ell\xi(v)W_B(Nv/B)
 \sum_u\widetilde g(urv)\alpha(u)^\ell\xi(u)W_A(Nu/A).
 \tag{Q19}
\]

Mellin inversion places \(\widetilde g(rv)/\widetilde g(r)\) beside
\(\mathcal R_{rv,\xi}\); all these row factors have modulus one.
The outer coefficient norm is \(O(B^{1/2})\).

For the unconditional statement shift to
\(\sigma=1/2+\delta\). The reciprocal completion is bounded by its
absolutely convergent Euler product because \(3\sigma-1/2>1\).
For the conditional statement shift to \(p+\delta<1/2\) and use
(Q3), together with the elementary \( (RB)^\epsilon\) bound for deleted
Euler factors on that line. Since \(\ell\ne0\), no theta main pole is
crossed. Cauchy--Schwarz, (Q17) or (Q18), and rapid Mellin decay prove
(Q2) and (Q4), absorbing \(\delta\) into the stated \(\epsilon\).

## 7. What this does and does not settle

The current terminal sextic row, after fixing its quadratic row \(R_0\),
has a cubic block with \(A=U\), \(B=L\), \(r=1\), and
\(\xi=\chi_{R_0}^3\) of norm conductor comparable to \(K=NR_0\).
The prime weights in the \(B\)-variable are allowed by the arbitrary
\(b_v\) quantifier, and the fixed cube-mask can be kept in those weights.

The favorable regime in (Q2) is \(K\le L\). In the binding source range
\(K\gg L\), the unconditional bound, after the terminal normalization
\((UL)^{-1/2}\), is only \(L^{1/2}K^{1/2}\), before outer-row factors.
Thus the new theorem supplies the missing *individual* quadratic
functional-equation interface, but not the needed cancellation in the
average over \(R_0\). Swapping \(A\) and \(B\) would put the prime support
inside the unrestricted smooth Type-I variable, so it is not justified
by (Q1).
