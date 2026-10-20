# Four scalar profiles extracted from the actual 27 cusp Mellins

Date: 2026-10-20. Status: proposed finite-profile closure lemma with
source-level proof and exact coefficient checks; independent review required.

This supplies the specific closure needed by
[ANGULAR_SELF_ABSORPTION.md](../average/ANGULAR_SELF_ABSORPTION.md).
It replaces an attempted coefficient-level unit-shift argument, which is
not used. The closure is at the level of complete Mellin series.

Primary source: Dunn--Radziwill,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
(5.2)--(5.16), (5.17)--(5.18), (5.29)--(5.42), (5.43)--(5.60),
and Appendix A. Its exact downloaded HTML SHA256 is
\(\texttt{3949e0f0ae87808d84fe02c12a3b68c5b66aa8d967d8ecb5e1605f1d985b956d}\).

## 1. The finite scalar family

Use the notation of [DUAL_RESUMMATION.md](DUAL_RESUMMATION.md).
For a primary element \(c\),
\[
 c\equiv1+\alpha_2(c)\lambda^2+\alpha_3(c)\lambda^3\pmod9,
 \qquad \kappa_{u,v}(c)=\omega^{u\alpha_2(c)+v\alpha_3(c)}.
 \tag{F1}
\]
All nine \(\kappa_{u,v}\) are cubic characters on the primary unit
quotient modulo 9. The scalar family needed here consists of
\[
 \mathcal K=\{\kappa_{0,0},\kappa_{0,-1},
                         \kappa_{1,-1},\kappa_{2,-1}\}.
 \tag{F2}
\]
Fix a nonzero integer \(a\). Let \(r\) be primary, squarefree and prime
to 3, and put \(\psi_r=\overline{(\cdot/r)_3}\). Set
\[
 Q_{r,\kappa}(w;a)=Z_r(3w-1/2,3a)
       \sum_c\widetilde g(c)\kappa(c)\psi_r(c)
                  \alpha(c)^a(Nc)^{-w}.
 \tag{F3}
\]
There is one common cube factor because every \(\kappa\in\mathcal K\)
has cube equal to one.

Let \(d_j(\mu)\), \(1\le j\le27\), be the source's actual Appendix A
coefficients, and define the raw cusp series
\[
 D_{j,r}(w;a)=
 \sum_{\mu\ne0}\overline{d_j(-\mu)}\psi_r(\lambda^4\mu)
                \alpha(\mu)^a(N\mu)^{-w}.
 \tag{F4}
\]
Initially all identities are in \(\Re w>1\). The fractional Fourier
indices in (F4) are retained.

**Closure lemma.** The four-vector of series in (F3) and the 27-vector
in (F4) determine one another by finite matrices that are bounded,
uniformly in \(\Im w\) and \(r\), on every closed vertical strip
\[
 1/6<\sigma_0\le\Re w\le\sigma_1<\infty.
 \tag{F5}
\]
Their only dependence on \(r\) is through its fixed unit class modulo 9.
The 27 cusp series admit a common angular reflection with a complete
Ramanujan sum at the moving level. Combining that reflection with (D5)
of the dual-resummation note leaves the four-family (F3) invariant.
All members are entire for \(a\ne0\), with polynomial growth on fixed
vertical strips.

## 2. An exact nonsingular minor

Put \(\rho=e^{2\pi i/9}\), so \(\omega=\rho^3\), and write
\((\omega/r)_3=\omega^b\), \(b\in\mathbb F_3\).
Set \(m=a-b\pmod3\) and
\[
 B_0=\omega^2,\qquad B_1=\rho\omega,\qquad B_2=\rho^{-1}.
 \tag{F6}
\]
The three source rows used are exactly
\[
 d_{22}(\mu)=\omega^2\tau_1(\mu)\check e(\omega\mu),\quad
 d_{26}(\mu)=\tau_1(\mu),\quad
 d_{27}(\mu)=\tau_1(\mu)\check e(\mu).
 \tag{F7}
\]

Order the columns by \(\kappa_{v,-1}\), \(v=0,1,2\), and the rows by
\(22,26,27\). Define \(M(m)\) by the following entries, with all column
subscripts read modulo 3:
\[
 \begin{aligned}
 M_{26,-t}(m)&=B_t\omega^{tm},\\
 M_{27,2-t}(m)&=B_t\omega^{tm}\rho^{-\operatorname{Tr}(\omega^t)},\\
 M_{22,2-t}(m)&=\omega B_t\omega^{tm}
                      \rho^{-\operatorname{Tr}(\omega^{t+1})},
 \qquad t=0,1,2.
 \end{aligned}
 \tag{F8}
\]
The traces are \(2,-1,-1\). Direct arithmetic in
\(\mathbb Z[\rho]\), using \(\rho^6+\rho^3+1=0\), gives
\[
 M(m)^*M(m)=3I,\qquad
 \det M(m)=3\omega^m(\omega-1).
 \tag{F9}
\]
Thus its inverse is exactly \(M(m)^*/3\), and the determinant has
absolute value \(3\sqrt3\).

The source coefficient identity is
\[
 \begin{pmatrix}D_{22,r}(w;a)\\D_{26,r}(w;a)\\D_{27,r}(w;a)\end{pmatrix}
 =9\,3^{4w}(-1)^a\,M(m)
 \begin{pmatrix}
 Q_{r,\kappa_{0,-1}}(w;a)\\
 Q_{r,\kappa_{1,-1}}(w;a)\\
 Q_{r,\kappa_{2,-1}}(w;a)
 \end{pmatrix}.
 \tag{F10}
\]

Here is a derivation that includes the row character. The support of
\(\tau_1\) in these rows forces
\(\mu=-\lambda^{-4}\omega^tcd^3\). The conjugate \(\tau_1\) coefficient
is
\[
 9B_t\,\widetilde g(c)\kappa_{-t,-1}(c)(Nd)^{1/2}.
 \tag{F11}
\]
Its angular and primitive row factors are
\[
 \alpha(-\omega^t)^a=(-1)^a\omega^{ta},\qquad
 \psi_r(-\omega^t)=\omega^{-tb}.
 \tag{F12}
\]
The Fourier norm contributes \(3^{4w}\).
Every primary \(d\) has \(d^3\equiv1\pmod9\).
The conjugated additive factors from (F7) therefore contribute the
fixed ninth roots in (F8) and the extra character
\(\kappa_{2,0}(c)\) in the two translated rows.
Summing the remaining cube variable gives exactly the common factor
\(Z_r(3w-1/2,3a)\), including its exclusions. This proves (F10).

For the trivial profile, the projection in DR Lemma 5.1 and the
coefficient identity in Lemma 5.4 give
\[
 D_{S,r}(w;a)
 =i^a\psi_r(\lambda)\,3^{5/2+3w}Q_{r,\kappa_{0,0}}(w;a),
 \quad
 D_{S,r}=\tfrac13(D_{1,r}+\omega D_{2,r}+\omega^2D_{3,r}).
 \tag{F13}
\]
Equations (F9)--(F13) provide a bounded left inverse on (F5).
There are no hidden zeros of a Mellin-dependent determinant.

## 3. Every source cusp uses only these four profiles

For each \(j\), expand its source coefficient at
\(\mu=\lambda^L\zeta cd^3\).
The formulas for \(\tau,\tau_1,\tau_2\) have squarefree coefficient
\(\widetilde g(c)\) times one of the four characters in (F2).
The additive factors in Appendix A have the form
\(\check e(\pm\omega^u\mu)\). They are trivial for \(L\ge-1\).
On the \(L=-3\) support of \(\tau\), they are constant on primary \(c\).
On the exceptional \(L=-4\) support, they multiply a profile
\(\kappa_{v,-1}\) by a character \(\kappa_{u,0}\), so the same
three-profile set remains.

The phases \(\psi_r(\lambda^{L+4}\zeta)\), including the dependence
on both primary coordinates of \(r\bmod9\), are retained.
Increasing \(L\) by 3 does not change them because \(\psi_r^3=1\).
The nonzero tails have common geometric ratio
\[
 i^{3a}\,3^{1/2-3w}.
 \tag{F14}
\]
Their scalar sums are bounded on (F5). The finite initial terms are
also bounded there. Hence each of the 27 Mellin series is a bounded
linear combination of the four completed scalar series (F3).
Together with Section 2, this proves the two-sided finite-span assertion.

The checker exhausts the actual 27-row table on the five representative
strata \(L=-4,-3,-1,0,2\). The two infinite tails follow from (F14),
not from a numerical truncation.

## 4. The complete 27-cusp reflection

This step uses the classical source matrices and their common multiplier.
It does not identify a literal Fourier-index shift with a local torus
action.

Let \(\Gamma=\mathrm{SL}_2(\mathcal O_E)\) and let
\(\Gamma_1(9)\) be the source's principal congruence subgroup.
It is normal. Equations (5.10)--(5.11) define a monomial action of
\(\Gamma\) on the 27 cusp functions. Every cusp function is automorphic
under \(\Gamma_1(9)\) with the same multiplier \(\chi\), as stated
immediately after (5.11).

Use the source's factorization
\[
 \gamma=\beta\widetilde\gamma,\qquad
 \beta=E^3W(r,b_0)^{-1},\qquad
 \widetilde\gamma\in\Gamma_1(9),\qquad
 \lambda^8ad+b_0r=1.
 \tag{F15}
\]
Here \(a,d\) are the source additive-residue variables; they are unrelated
to the fixed angular order in earlier formulas.
By source (5.35),
\[
 \beta=
 \begin{pmatrix}
 -1+b_0r&b_0\\-2r+b_0r^2&-1+b_0r
 \end{pmatrix}
 \equiv
 \begin{pmatrix}0&r^{-1}\\-r&0\end{pmatrix}\pmod9.
 \tag{F16}
\]
Thus its residue depends only on \(r\bmod9\), not on \(d\bmod r\).

For two valid choices with the same \(r\bmod9\), the quotient of the
two \(\beta\)'s lies in \(\Gamma_1(9)\), and hence their monomial
actions differ by a common scalar. Source (5.32) and (5.38) show that
both actions fix \(F_1\) with scalar one. Since \(F_1\) is nonzero,
the common scalar is one. Therefore the whole 27-by-27 action of
\(\beta\) is independent of the additive residue, and only finitely
many such matrices occur as \(r\) varies.

The remaining multiplier is exactly the source calculation (5.41):
\[
 \overline{\chi}(\widetilde\gamma)
        =(\lambda^4a/r)_3.
 \tag{F17}
\]
Opening the primitive Fourier twist, this same scalar is present in
every cusp row. The full sum over \(d\bmod r\) consequently remains
the complete transform (5.69)--(5.70), namely a fixed unit times
\(\overline{g(r)}c_r(u)\). No residue classes are omitted.

Applying the angular derivatives as in (5.43), evaluating at \(z=0\),
and taking the Mellin transform as in Lemma 5.3 gives a 27-vector
functional equation. Apart from unit matrices and fixed ramified
normalizations, its moving factor is
\[
 (Nr)^{1/2-2s}
 (2\pi)^{4s-2}
 \frac{\Gamma(5/6+|a|/2-s)\Gamma(7/6+|a|/2-s)}
      {\Gamma(s+|a|/2-1/6)\Gamma(s+|a|/2+1/6)}.
 \tag{F18}
\]
The reflected coefficients have angular order \(-a\) and the full
Ramanujan factor \(c_r(\lambda^4\mu)\).
This is the same source reflection applied to the complete cusp vector;
the matrix independence above is the additional verification it needs.

## 5. Analytic continuation and resummation closure

For nonzero angular order, every cusp constant term is killed by the
angular derivative. The split Mellin argument of DR (5.49)--(5.60)
then applies to the finite vector just reflected: the positive-end
Fourier expansion decays exponentially, and reflection supplies the
negative-end expansion. The completed cusp Mellins are entire.
Their common gamma factors and absolutely convergent Dirichlet series
on a right boundary, together with reflection and the finite-order
Mellin representation, give polynomial growth on fixed vertical
strips by the usual strip principle. The number of profiles and the
growth exponents are independent of \(r\).

The bounded extraction (F10)--(F13) makes every scalar series in (F3)
entire with the same type of vertical control.
On the reflected side, expand the 27 cusp coefficients as in Section 3.
A unit or ramified power multiplying \(cd^3\) does not change its
Ramanujan sum at \(r\). Each component is therefore precisely a scalar
multiple of the raw series \(\mathscr D_{r,\kappa}(1-s;-a)\)
in (D4). Apply its exact identity (D5).
Every resulting series is \(Q_{k,\kappa}(1-s;-a)\) with
\(k\mid r\) and \(\kappa\) still in the four-element set (F2).

For \(s=1/2-\delta+it\), \(0<\delta<1/4\), both Mellin arguments are
in a strip of the form (F5). Equations (D11)--(D12), the bounded
coefficient matrices above, and Stirling therefore give
\[
 \|\mathbf Q_r(1/2-\delta+it)\|
 \ll_{\delta,a,\epsilon}
 (1+|t|)^{4\delta}
 (Nr)^{-1/2+2\delta+\epsilon}
 \sum_{k\mid r}(Nk)^{1/2-\delta}
       \|\mathbf Q_k(1/2+\delta-it)\|.
 \tag{F19}
\]
The vector contains the four profiles and both angular signs.
This is the precise closure inequality required by the self-absorption
argument. No growing quadratic conductor is included.

## 6. Exact checks and corrected exploration

The companion verify_profile_closure.py operates in
\(\mathbb Z[\rho]/(\rho^6+\rho^3+1)\).
It verifies (F9), compares (F8) with the actual coefficients in
486 cases covering all angular residues modulo 6, row unit twists
modulo 3 and primary classes modulo 9, and checks the four-profile
support for all 27 source rows on 2,430 finite strata.
The full ramified row twist is accounted for; its remaining
\(\psi_r(\lambda)\) phase is a fixed nonzero scalar.

A preliminary numerical exploration transcribed several Appendix A
rows incorrectly and suggested a different minor. That minor was
rejected during review and is not used here. The rows (F7) have been
checked directly against the source table. The exact finite checker
checks coefficient algebra; the continuation and functional equation
remain the mathematical argument in Sections 4--5.
