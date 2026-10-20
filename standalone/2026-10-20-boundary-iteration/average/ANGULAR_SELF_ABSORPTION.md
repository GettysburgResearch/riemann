# Angular second moments by resumming the complete dual

20 October 2026. **Status: proposed source-dependent analytic theorem.**
The finite local-family closure in Section 2 has an independent exact
cusp calculation and reflection audit in
[AUDIT_CUSP_REFLECTION.md](../mixed/AUDIT_CUSP_REFLECTION.md).
This is not a certification of the complete upstream preprints.

The absorption mechanism follows David--de Faveri--Dunn--Stucky,
[arXiv:2410.03048v2](https://arxiv.org/html/2410.03048v2), Lemma 6.6.
Its stated spherical theorem is not quoted with an angular twist.
Instead we use the explicit angular theta transform of Dunn--Radziwill
(DR), [arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
Sections 5.2--5.5 and Appendix A. The one-pass argument in
[AVERAGED_TYPE_I.md](../type_i/AVERAGED_TYPE_I.md) is a separate, weaker
candidate result which does not need the closure below.

## 1. Statement

Use primary Eisenstein integers, \(E=\mathbb Q(\omega)\),
\(\alpha(c)=c/|c|\), and \(\widetilde g(c)=g(c)/\sqrt{Nc}\).
Fix \(\ell\ne0\). For squarefree \(r\), put
\[
 \mathcal R_r(s)=\sum_c\widetilde g(c)\overline{(c/r)_3}
                       \alpha(c)^\ell(Nc)^{-s},\qquad
 Q_r(s)=Z_r(3s-\tfrac12,3\ell)\mathcal R_r(s).
 \tag{1}
\]
Here \(Z_r\) omits primes dividing \(3r\). Its full cube factor is
retained. All common-prime zeros are natural.

**Proposed theorem.** For \(1/2<\sigma<3/4\),
\[
 \sum_{Nr\le R}^{*}|Q_r(\sigma+it)|^2
 \ll_{\ell,\sigma,\epsilon} R^{1+\epsilon}(1+|t|)^C.       \tag{2}
\]
The asterisk means primary and squarefree. The same estimate holds
for the fixed finite family of realized ramified profiles below.
For \(1/4<p<1/2\), reflection then gives
\[
 \sum_{Nr\le R}^{*}|Q_r(p+it)|^2
 \ll_{\ell,p,\epsilon} R^{2-2p+\epsilon}(1+|t|)^C.         \tag{3}
\]

For arbitrary \(|b_v|\le1\) and fixed smooth compactly supported weights,
\[
 T_\ell(A,B)=\sum_{u,v}b_v\widetilde g(uv)\alpha(uv)^\ell
                         W_A(Nu/A)W_B(Nv/B)
\]
would consequently satisfy
\[
 |T_\ell(A,B)|\ll(AB)^\epsilon A^{1/2}B.                 \tag{4}
\]
If the actual factor \(Z_1(z,3\ell)\) is zero-free for \(\Re z>\beta\),
then, for \(p=(2\beta+1)/6\), it also satisfies
\[
 |T_\ell(A,B)|\ll(AB)^\epsilon A^pB^{3/2-p}.             \tag{5}
\]
Both bounds give \(X^{3/4+\epsilon}\) at \(A=B=X^{1/2}\).
A coherent Mobius mark is permitted in \(b_v\). A moving quadratic
row character is not included.

## 2. Realized finite closure at the prime above 3

Use the conjugate theta representation underlying DR Section 5 and
its actual 27 cusp functions. For a primary element write
\(c=1+\alpha_2(c)\lambda^2+\alpha_3(c)\lambda^3\pmod9\), and put
\(\kappa_{a,b}(c)=\omega^{a\alpha_2(c)+b\alpha_3(c)}\).
For each \(a\in\{\ell,-\ell\}\), let \(\mathbf Q_r^{(a)}\) consist
of the four completed scalar series with angular factor
\(\alpha(c)^a\) and the additional coefficient characters
\[
 \kappa_{0,0},\quad\kappa_{0,-1},\quad
 \kappa_{1,-1},\quad\kappa_{2,-1}.
\]
They are cubic, so their cube factors are those of (1), with
\(\ell\) replaced by \(a\). Apply the construction below to both
angular signs, and use the eight-component direct sum
\(\mathbf Q_r=\mathbf Q_r^{(\ell)}\oplus\mathbf Q_r^{(-\ell)}\)
and its Euclidean norm throughout Sections 3--4. Reflection reverses
the angular sign, so this direct sum is the family controlled by the
same supremum in the absorption argument. The following four-channel
calculation is written for \(a=\ell\); it holds identically for
\(a=-\ell\).

The source projection of Lemma 5.1 extracts the first channel with
nonzero scalar \(3^{5/2+3s}i^\ell\psi_r(\lambda)\), where
\(\psi_r(x)=\overline{(x/r)_3}\). The other three channels are
extracted from the actual cusps 22, 26, 27. Here is the full minor,
so that closure does not rest on an abstract assertion about profiles.
Put \(\rho=e^{2\pi i/9}\), \(\psi_r(\omega)=\omega^{-b}\),
\(m=\ell-b\), and
\(B_t=(\omega^2,\rho\omega,\rho^{-1})_t\), \(t=0,1,2\).
After dividing the three cusp Mellins by
\(9\,3^{4s}(-1)^\ell\), their entries in column
\(\kappa_{a,-1}\) are
\[
 \begin{split}
 M_{26,-t}&=B_t\omega^{tm},\\
 M_{27,2-t}&=B_t\omega^{tm}\rho^{-\operatorname{Tr}(\omega^t)},\\
 M_{22,2-t}&=\omega B_t\omega^{tm}
                       \rho^{-\operatorname{Tr}(\omega^{t+1})}.
 \end{split}                                           \tag{6}
\]
The columns are read modulo three. Directly,
\(MM^*=3I\), so the inverse is \(M^*/3\). This identity holds for
every angular integer and every ramified row class. All extracting
scalars and their inverses are bounded on fixed vertical strips.

Conversely, DR (5.7), (5.13), (5.14), and Appendix A express every cusp
Mellin through these four channels. The only infinite ramified sums
have ratio of modulus \(3^{1/2-3\Re s}\); hence they are uniformly
bounded on the strips \(\Re s>1/6\) in use. Additive phases at
valuation \(-4\) permute the first coordinate of
\(\kappa_{a,-1}\), as in (6). At the other valuations their phases
are constant on each primary residue sector. Thus the two Mellin
families bound each other with fixed constants.

The complete Ramanujan sum is also valid for all 27 cusps. In DR's
factorization of the reflection matrix, write
\(\gamma=\beta\widetilde\gamma\), with
\(\widetilde\gamma\in\Gamma_1(9)\) and
\(\beta=E^3W(r,b_0)^{-1}\). Since \(b_0r\equiv1\pmod9\),
the reduction of \(\beta\) is independent of the residue summed
modulo \(r\). Two valid choices differ by \(\Gamma_1(9)\), whose
multiplier is common to all cusps. DR (5.32), (5.38) show that both
choices fix the nonzero function \(F_1\); their common scalar ratio
is therefore one. Consequently the whole cusp action is independent
of that residue. DR (5.41) computes the remaining multiplier, and
(5.69)--(5.70) give the full signed Ramanujan sum for every cusp.

Nonzero angular differentiation kills every cusp constant term.
The split Mellin integrals of DR (5.49)--(5.60) therefore give entire
continuation of the extracted four channels. The boundary-line
absolute estimates and the common gamma quotient give polynomial
vertical growth of a degree independent of the moving row; its
constant may depend polynomially on that row.

Finally the four scalar characters are multiplicative. The exact
divisor resummation acts on these scalar Mellin series and keeps
the same character, with factors \(\kappa(k)\) on extracted divisors.
No assertion that literal coefficient shifts are compact-group
actions is required. The independent audit cited above checks both
the corrected minor and this full-reflection mechanism.

## 3. Resummed reflection

Put \(s=1/2-\delta+it\), \(w=1-s\), \(0<\delta<1/4\).
The exact local calculation is in
[DUAL_RESUMMATION.md](../type_i/DUAL_RESUMMATION.md).
Here is also an absolute majorant of the same complete operation.
The dual index has the form
\[
 \nu=\lambda^L\zeta h c(h'd')^3,\quad h\mid r,\quad
 h'\mid r^\infty,\quad(cd',r)=1,\quad\mu^2(hc)=1.
\]
The free cube variable \(d'\), including its possible overlap with \(c\),
is summed in the retained cube completion. Only the \(r\)-supported
cube variable \(h'\) is estimated locally below.
The squarefree coefficient factors as
\(\widetilde g(h)\widetilde g(c)\overline{(c/h)_3}\)
times a fixed local profile. Its cube coefficient has size
\((Nh')^{1/2}\); the Ramanujan factor is
\(\mu(r/(h(h')^3,r))\varphi((h(h')^3,r))\).

For a prime \(q=N\mathfrak p\mid h\), its cube-power sum costs
\(O_\delta(q)\). For \(q\mid r/h\), it costs
\[
 1+(q-1)\frac{q^{1/2-3\Re w}}{1-q^{1/2-3\Re w}}
       =1+O_\delta(q^{-3\delta}).
\]
After extracting the factor \(Nh\), the remaining product is
\(O_{\delta,\eta}((Nr)^\eta)\) for every \(\eta>0\).
Restore the remaining excluded squarefree primes by finite
inclusion-exclusion. A divisor \(e\mid r/h\) changes the row to
\(k=he\) and contributes modulus \((Ne)^{-\Re w}\).
The coefficient for fixed \(k\) is bounded by
\[
 (Nk)^{-\Re w}\sum_{h\mid k}Nh
       \ll_\eta(Nk)^{1-\Re w+\eta}.
\]
Deleted cube factors may likewise be restored; their local weights
are \(q^{1/2-3\Re w}=q^{-1-3\delta}\), giving a bounded product.
All shifted scalar factors remain in the four Mellin channels above.

The DR modulus factor is \((Nr)^{1/2-2\Re s}\).
Stirling gives a gamma factor \((1+|t|)^{4\delta}\).
For the Euclidean norm of the finite profile vector, we obtain
\[
 \|\mathbf Q_r(\tfrac12-\delta+it)\|
 \ll (1+|t|)^{4\delta}(Nr)^{-1/2+2\delta+\eta}
       \sum_{k\mid r}(Nk)^{1/2-\delta}
               \|\mathbf Q_k(\tfrac12+\delta-it)\|.       \tag{7}
\]
The dominant divisor \(k=r\) has only the factor \((Nr)^\delta\).

Write \(\mathcal A_\sigma(R,t)=
\sum_{Nr\le R}^{*}\|\mathbf Q_r(\sigma+it)\|^2\).
Square (7), use the divisor bound, and sum over multiples of \(k\).
Ideal counting gives
\(\sum_{r:k\mid r,Nr\le R}(Nr)^{-1+4\delta}
\ll_\delta R^{4\delta}/Nk\).
Consequently
\[
 \mathcal A_{1/2-\delta}(R,t)
 \ll (1+|t|)^{8\delta}R^{4\delta+\eta}
 \sum_{Nk\le R}(Nk)^{-2\delta}
               \|\mathbf Q_k(1/2+\delta-it)\|^2.          \tag{8}
\]
No row larger than \(R\) is introduced.

## 4. Absorption without assuming the desired bound

Set \(\sigma=1/2+\delta\). Start with the free-split integral
\[
 I_r(s;Y)=\frac1{2\pi i}\int_{(c)}
       Q_r(s+z)Y^ze^{z^2}\frac{dz}{z},\qquad c>1-\sigma.
\]
Shift to \(\Re z=-2\delta\); only \(z=0\) is crossed.
For the original integral, the cubic large sieve, cube expansion,
and Minkowski give
\[
 \sum_{Nr\le R}^{*}\|\mathbf I_r(\sigma+it;Y)\|^2
 \ll(RY)^\eta
      \{R+Y^{1-2\delta}+R^{2/3}Y^{2/3-2\delta}\}.        \tag{9}
\]
The first cube sum has exponent \(-1-3\delta\), and the others
have exponents \(-5/2,-2\). Smooth tails and finite local profiles
are harmless. This is the unconditional cubic large sieve,
with common-prime zeros retained.

Fix \(R_{\max}<\infty\) and a large height weight \(C\), and let
\[
 M=\sup_{\substack{2\le T\le R_{\max}\\u\in\mathbb R}}
 \frac{\mathcal A_\sigma(T,u)}
      {T^{1+\epsilon_0}(1+|u|)^C}.                       \tag{10}
\]
It is finite by polynomial growth for finitely many rows. Choose
\(C\) above that growth order and the height powers in (9).
Partial summation in (8), Cauchy--Schwarz on the shifted integral,
and Gaussian decay bound its squared mean by
\[
 \ll M\,Y^{-4\delta}R^{1+\epsilon_0+2\delta+\eta}
                      (1+|t|)^{C+8\delta}.             \tag{11}
\]
Here the convolution in height uses
\((1+|t+v|)^C\le(1+|t|)^C(1+|v|)^C\); its Gaussian integral is
a fixed constant. No global finiteness of (10) is assumed.

Take \(Y=R^{1/2+\delta/4}(1+|t|)^2\). The normalized coefficient
of \(M\) in (11) is \(O(R^{-\delta^2+\eta})\). Choose
\(\eta<\delta^2/2\). Meanwhile the two nontrivial row powers in (9)
are
\[
 (1/2+\delta/4)(1-2\delta)<1,\qquad
 2/3+(1/2+\delta/4)(2/3-2\delta)
       =1-5\delta/6-\delta^2/2<1.
\]
Allocate all auxiliary small losses within \(\epsilon_0\).
Above a fixed \(R_0\), the coefficient of \(M\), including splitting
and Gaussian constants, is at most \(1/2\). Below \(R_0\), a finite
row bound suffices. Thus \(M\le C_0+\tfrac12M\), with constants
independent of \(R_{\max}\). Letting \(R_{\max}\) grow proves (2).

For (3), apply (8) with \(\delta=1/2-p\) and (2). The weighted
sum is \(O(R^{1-2\delta+\epsilon}(1+|t|)^C)\), and hence the
total row exponent is \(4\delta+1-2\delta=2-2p\).

## 5. Return to the marked form and scope

On the line \(1/2+\delta\), the inverse of the Hecke factor in (1)
is bounded by \((Nv)^\epsilon\), using absolute convergence and
the deleted Euler factors. Mellin inversion of (4) in the inner
variable gives \(\widetilde g(v)\mathcal R_v(s)\) by exact twisted
multiplicativity. Cauchy--Schwarz in \(v\) costs \(B^{1/2}\);
(2) costs another \(B^{1/2+\epsilon}\). Rapid Mellin decay handles
height. Taking \(\delta\) sufficiently small proves (4).

Under the stated zero-free premise, move instead to \(p+\delta\).
The fixed-character reciprocal estimate gives polynomial height
growth and \(B^\epsilon\) for deleted Euler factors. Equation (3)
then gives (5). The unconditional bound remains available; (5)
improves it when \(A>B\), while at balance both exponents are \(3/4\).
At \(X=AB\), (4) gives a strict saving below \(X^{5/6}\) for
\(B\le X^{2/3-\eta}\), \(\eta>0\).

The moving quadratic factor in the complete sextic detector changes
the finite Fourier transform and brings in new conductor primes.
The fixed profile argument at 3 cannot absorb it. In particular,
the source terminal with quadratic conductor much larger than the
marked divisor length remains outside this statement.

This document gives no improved numerical \(B_\flat\) and no proof
of RH. Its independent cusp audit closes the specific local-family
issue in Section 2; the moving quadratic conductor remains a separate
analytic obstacle. The one-pass estimate remains useful because it
also has an explicit moving quadratic-conductor extension.
