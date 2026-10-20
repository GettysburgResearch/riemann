# Independent audit of cusp extraction and angular reflection

20 October 2026. Status: native finite extraction lemma and reflection
audit. This is an independent review of the proposed angular mean in
`../average/ANGULAR_SELF_ABSORPTION.md`, not a numerical zero-free result.

The source is Dunn--Radziwill (DR),
[2109.07463v3](https://arxiv.org/html/2109.07463v3), particularly (5.7),
(5.13), (5.16), (5.30)--(5.41), Lemmas 5.1 and 5.3, and Appendix A.
The initially proposed assertion that literal unit shifts preserve the
coefficient span of the 27 cusps is unnecessary and should not be used.
The correct argument extracts four scalar Mellin series explicitly.

## 1. The scalar profiles and the actual moving-row phase

Write a primary element as
\(c=1+\alpha_2(c)\lambda^2+\alpha_3(c)\lambda^3\pmod9\), and let
\(\kappa_{a,b}(c)=\omega^{a\alpha_2(c)+b\alpha_3(c)}\).
The four scalar channels are \(\kappa_{0,0}\) and
\(\kappa_{a,-1}\), \(a\in\mathbb F_3\). The complete series are

\[
 Q_{r,\kappa}(s;\ell)=
 \sum_{c,d}\widetilde g(c)\kappa(c)
 \overline{(cd^3/r)_3}\alpha(cd^3)^\ell
 (Nd)^{1/2}(Nc(Nd)^3)^{-s}.
\]

In particular, the cube sum retains the natural zeros at primes of
\(r\). As every displayed \(\kappa\) is cubic, its cube value is one.

The source cusp series has the twist
\(\psi_r(\lambda^4\mu)\), with
\(\psi_r(x)=\overline{(x/r)_3}\). It is important to retain this
factor when extracting profiles. Set
\(\psi_r(\omega)=\omega^{-b}\) and \(m=\ell-b\).
The integer \(b\) lies in a fixed three-element set. The other ramified
row phase \(\psi_r(\lambda)\) is a nonzero cube root of unity.

The projection of DR Lemma 5.1 gives exactly

\[
 \mathcal D_{S,r}(s;\ell)
 =3^{5/2+3s}i^\ell\psi_r(\lambda)Q_{r,\kappa_{0,0}}(s;\ell).
 \tag{A1}
\]

This scalar has no zeros and both it and its inverse are bounded on
each fixed vertical strip.

## 2. An explicit, uniformly invertible three-cusp minor

Take the actual cusps **22, 26, 27**. Appendix A gives

\[
 d_{22}(x)=\omega^2\tau_1(x)\check e(\omega x),\qquad
 d_{26}(x)=\tau_1(x),\qquad
 d_{27}(x)=\tau_1(x)\check e(x).
\]

Put \(\rho=e^{2\pi i/9}\), so \(\omega=\rho^3\), and
\(B_t=(\omega^2,\rho\omega,\rho^{-1})_t\) for \(t=0,1,2\).
These are the conjugates of the three coefficients of \(\tau_1\)
in DR (5.13), divided by 9.

For each cusp write \(\mu=-\omega^t\lambda^{-4}cd^3\).
The common scalar is \(9\,3^{4s}(-1)^\ell\). In the three columns
\(\kappa_{a,-1}\), the remaining row entries are

\[
 \begin{array}{ll}
 M_{26,-t}=B_t\omega^{tm},\\
 M_{27,-t+2}=B_t\omega^{tm}\rho^{-\operatorname{Tr}(\omega^t)},\\
 M_{22,-t+2}=\omega B_t\omega^{tm}
                       \rho^{-\operatorname{Tr}(\omega^{t+1})}.
 \end{array}                                                    \tag{A2}
\]

All column subscripts are modulo 3. The column shift by 2 is essential:
the nonconstant part of \(\check e(-\omega^t cd^3/9)\) equals
\(\kappa_{2,0}(c)\), because \(d^3\equiv1\pmod9\) and
\(\operatorname{Tr}(\omega^t)\equiv2\pmod3\).

For every integer \(m\), the matrix with rows in order \((22,26,27)\)
satisfies the exact identity

\[
 MM^*=3I_3,\qquad M^{-1}=\tfrac13M^*,\qquad |\det M|^2=27. \tag{A3}
\]

One checks this using \(\rho^3=\omega\) and
\(1+\omega+\omega^2=0\). Changing \(m\) only multiplies rows and
columns by unit scalars. Thus (A1)--(A3) extract all four scalar channels
uniformly in height, angular parity, and the finite ramified row classes.
There is no determinant zero on an exceptional angular congruence class.

The companion [exact checker](audit_cusp_minor.py) reconstructs (A2)
from the three source cusp formulas in
\(\mathbb Z[\rho]/(\rho^6+\rho^3+1)\). It also detects a discarded
incorrect choice: cusps \((20,22,26)\) are singular. Indeed
\(d_{20}(x)=\omega^2\tau_1(\omega x)\), so its Mellin is proportional
to cusp 26. The finite audit is recorded in
[CUSP_MINOR_AUDIT.json](CUSP_MINOR_AUDIT.json).

## 3. Why all 27 cusp Mellins use these four channels

For the \(\tau\) part, the squarefree Gauss coefficients in DR (5.7)
give either \(\kappa_{0,0}\) or \(\kappa_{a,-1}\). Its additive
translations in Appendix A are constant on each ramified valuation and
unit sector: for \(L\ge-3\), changing \(cd^3\) within its primary
residue class does not change \(\check e(\delta\lambda^L\zeta cd^3)\).

For \(\tau_1,\tau_2\), only \(L=-4\) occurs. Their additive factors
shift the first coordinate \(a\) of \(\kappa_{a,-1}\), as in (A2),
and introduce no new second coordinate. The sums over successive
ramified valuations have ratio of modulus \(3^{1/2-3\Re s}\).
They converge and are uniformly bounded on the strips \(\Re s>1/6\)
used in the absorption argument. Thus the entire 27-dimensional Mellin
vector is bounded by the four scalar channels on these strips, and
(A1)--(A3) give the reverse bound.

This is a statement about Mellin series. It does not assert that every
literal multiplication \(f_L(c)\mapsto f_L(hc)\) is the action of a
local compact group element on the original coefficient vectors.

## 4. Reflection of every cusp with the full Ramanujan sum

The common multiplier property in DR (5.11) and the paragraph following
it is sufficient. Let

\[
 \gamma=\begin{pmatrix}9d&b_0\\-r&9a\end{pmatrix},\qquad
 81ad+b_0r=1.
\]

DR (5.30) factors \(\gamma=\beta\widetilde\gamma\), where
\(\beta=E^3W(r,b_0)^{-1}\) and
\(\widetilde\gamma\in\Gamma_1(9)\). Because
\(b_0r\equiv1\pmod9\), the residue of \(\beta\) modulo 9 depends
only on \(r\bmod9\), independently of the residue \(d\bmod r\).

Here is the multiplier check that a reduction modulo 9 alone would
miss. For two valid choices, \(\beta\beta_0^{-1}\in\Gamma_1(9)\),
so this quotient acts by the *same scalar* \(\chi\) on every cusp.
DR (5.32) and (5.38) state that \(F_1|\beta=F_1\) for every valid
choice. Since \(F_1\) is nonzero, that common scalar for the quotient
must be one. Consequently the full action of \(\beta\) on all cusp
functions is independent of \(d\bmod r\). There are only finitely
many such actions as \(r\bmod9\) varies.

DR (5.41) computes the remaining scalar exactly:
\(\overline\chi(\widetilde\gamma)=(\lambda^4a/r)_3\).
The complete sum over \(d\bmod r\) therefore remains the same for
every cusp. With \(\psi_r=\overline{(\cdot/r)_3}\), equations
(5.69)--(5.70) give a fixed phase times
\(\overline{g(r)}c_r(\mu)\), with the full signed Ramanujan sum.
There is no residue restriction or new conductor in this operation.

Angular differentiation at \(z=0\), as in DR Corollary 5.1, commutes
with this finite constant matrix and swaps \(\ell\) with \(-\ell\).
For \(\ell\ne0\), it kills every cusp constant term. The same split
Mellin integral then gives entire continuation of each completed cusp
series, hence of the four extracted scalar channels.

## 5. Gamma factor, divisor sum, and absorption audit

DR Lemma 5.3 has common archimedean factor

\[
 G_\ell(s)=\tfrac14(2\pi)^{-2s-|\ell|}
  \Gamma(s+|\ell|/2-1/6)\Gamma(s+|\ell|/2+1/6).
\]

For \(s=1/2-\delta+it\), \(0<\delta<1/4\),
\(G_\ell(1-s)/G_\ell(s)\ll_\ell(1+|t|)^{4\delta}\).
There are no gamma poles or zeros on the two lines in use. The
row factor before divisor resummation is
\((Nr)^{1/2-2\Re s}=(Nr)^{-1/2+2\delta}\), exactly as required
by equation (7) of the proposed mean.

The exact algebraic identity in `../type_i/DUAL_RESUMMATION.md` now
acts on the four extracted scalar profiles, so it does not need the
false coefficient-level unit-shift assertion. Its deleted Euler factors
are essential for the cancellation at every prime dividing the new row.
On \(\Re(1-s)=1/2+\delta\), their product is bounded by \((Nr)^\eta\).

Squaring the divisor sum and summing multiples of \(k\) gives
\(R^{4\delta+\eta}\sum_{Nk\le R}(Nk)^{-2\delta}|Q_k|^2\), not
a larger row family. The proposed supremum argument is noncircular:
for finite \(R_{\max}\) the height-weighted supremum is finite by the
polynomial strip bound; all constants in the recurrence are uniform in
\(R_{\max}\). With
\(Y=R^{1/2+\delta/4}(1+|t|)^2\), the normalized reflected term is
\(O(R^{-\delta^2+\eta})M\). The original cubic large sieve terms have
row exponents

\[
 (1/2+\delta/4)(1-2\delta)<1,\qquad
 2/3+(1/2+\delta/4)(2/3-2\delta)
       =1-5\delta/6-\delta^2/2<1.
\]

Thus the extraction lemma removes the identified local closure gap in
the stated angular absorption argument. This review does not supply a
moving quadratic conductor estimate, a lower numerical \(B_\flat\),
or RH. Those require further mathematical input at the separate mixed
terminal described in [TERMINAL_INTERFACE.md](TERMINAL_INTERFACE.md).
