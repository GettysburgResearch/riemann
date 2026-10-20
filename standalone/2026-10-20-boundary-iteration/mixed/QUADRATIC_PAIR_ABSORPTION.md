# A closed quadratic/sextic pair for the cubic theta mean

20 October 2026. Status: proposed analytic lemma with complete argument;
independent review requested. This is a uniform estimate at each fixed
quadratic conductor. It does not assert cancellation when those
conductors are averaged.

Dependencies: Dunn--Radziwill (DR),
[2109.07463v3](https://arxiv.org/html/2109.07463v3), Section 5; the exact
cusp extraction and reflection in [AUDIT_CUSP_REFLECTION.md](AUDIT_CUSP_REFLECTION.md)
and `../type_i/FINITE_PROFILE_CLOSURE.md`; the exact divisor identity in
`../type_i/DUAL_RESUMMATION.md`; the unconditional cubic large sieve.

## 1. The two characters and their full completion

Work in the Eisenstein field. Let \(S\) be primary and squarefree,
prime to 6, with norm \(H\), and let \(\xi_S\) be a primitive quadratic
character of conductor \(S\). Let \(\chi_S=(\cdot/S)_3\), and put

\[
 \eta_j=\xi_S\chi_S^j,\qquad j\in\{0,2\}.
\]

These characters are zero on nonunits at \(S\); both are primitive.
Let \(r\) be primary and squarefree, \((r,S)=1\). For a fixed
nonzero angular order \(\ell\) and one of the four ramified cubic
profiles \(\kappa\) from the cusp extraction, define

\[
 Q_{r,S,j,\kappa}(s;\ell)=
 Z_{rS,\xi_S}(3s-1/2,3\ell)
 \sum_c\widetilde g(c)\kappa(c)\eta_j(c)
          \overline{(c/r)_3}\alpha(c)^\ell(Nc)^{-s},
 \tag{Q1}
\]

where

\[
 Z_{rS,\xi_S}(3s-1/2,3\ell)
 =\sum_{(d,rS)=1}\xi_S(d)\alpha(d)^{3\ell}(Nd)^{1/2-3s}.
 \tag{Q2}
\]

The twist in (Q2) follows from \(\eta_j(d)^3=\xi_S(d)\).
It must not be replaced by the untwisted cube factor. The vector
\(\mathbf Q\) below includes both \(j\)'s, all four \(\kappa\)'s,
and both angular signs.

For \(0<\delta<1/6\), set

\[
 F_\delta(R,H)=R+R^{1/2-\delta}H^{1-2\delta}
                    +R^{1-\delta}H^{2/3-2\delta}.
 \tag{Q3}
\]

**Proposed mean.** Uniformly in \(S\),

\[
 \sum_{Nr\le R,(r,S)=1}^{*}
 \|\mathbf Q_{r,S}(1/2+\delta+it)\|^2
 \ll_{\ell,\delta,\epsilon}(RH)^\epsilon
          F_\delta(R,H)(1+|t|)^C.                         \tag{Q4}
\]

For \(1/3<p<1/2\), reflection gives

\[
 \begin{split}
 \sum_{Nr\le R,(r,S)=1}^{*}\|\mathbf Q_{r,S}(p+it)\|^2
 \ll (RH)^\epsilon(1+|t|)^C\{&
 R^{2-2p}H^{2-4p}\\
 &+R^{1-p}H^{2-2p}
 +R^{3/2-p}H^{5/3-2p}\}.
 \end{split}                                               \tag{Q5}
\]

## 2. The exact moving-conductor reflection

Use DR's periodic twist at modulus \(rS\), with
\(\psi=\overline{\chi_r}\eta_j\). Its finite Fourier transform is
supported on units because the character is primitive. At primes of
\(r\), the calculation is the cubic one already used in the four-profile
proof: the cubic character cancels the Kubota factor and leaves the full
signed Ramanujan sum \(c_r(u)\), together with a Gauss factor of modulus
\((Nr)^{1/2}\).

At \(S\), the Fourier transform contributes a Gauss sum times
\(\overline{\eta_j}(d)\). The reflection variable satisfies
\(d=(\lambda^8a)^{-1}\pmod S\). Up to a fixed unit factor this turns
\(\overline{\eta_j}(d)\) into \(\eta_j(a)\). Multiplication by the
Kubota factor \(\chi_S(a)\), followed by the additive transform in
\(a\), gives

\[
 \overline{\eta_j\chi_S}(u)
       =\xi_S(u)\chi_S(u)^{-j-1}=\eta_{-j-1}(u).           \tag{Q6}
\]

Thus \(j=0\) and \(j=2\) are interchanged. Each of the two primitive
Gauss sums at \(S\) has modulus \(H^{1/2}\); their product has modulus
\(H\). Coprimality \((u,S)=1\) is retained by the character zero.
CRT introduces unit factors only, and no incomplete residue sum occurs.
The modulus factor in the Mellin reflection is therefore

\[
 (Nr)^{1/2-2s}H^{1-2s}.                                  \tag{Q7}
\]

The same 27-cusp reflection applies at modulus \(rS\): its finite
matrix depends only on the modulus modulo 9. Four-profile extraction
remains valid. Indeed \(\xi_S(\omega)=1\), so the three-cusp minor
only changes its integer \(m\); \(\xi_S(-1)\) is a common unit scalar.
The ramified geometric ratio acquires the factor
\(\eta_j(\lambda)^3=\xi_S(\lambda)\), again of modulus one.
Its convergence region remains \(\Re s>1/6\).

The exact divisor resummation is performed only at primes dividing
\(r\), all coprime to \(S\). It is valid with the multiplicative
coefficient \(\kappa\eta_{-j-1}\); its local cube parameter becomes
\(\xi_S(\mathfrak p)\alpha(\mathfrak p)^{-3\ell}
 (N\mathfrak p)^{1/2-3(1-s)}\). The completed factor (Q2), including
every deleted Euler factor, is restored exactly. New rows are divisors
\(k\mid r\), so they remain coprime to \(S\).

For \(s=1/2-\delta+it\), the resulting norm inequality is

\[
 \|\mathbf Q_{r,S}(s)\|
 \ll (1+|t|)^{4\delta}H^{2\delta}
 (Nr)^{-1/2+2\delta+\eta}
 \sum_{k\mid r}(Nk)^{1/2-\delta}
       \|\mathbf Q_{k,S}(1-s)\|.                         \tag{Q8}
\]

All these completed series are entire for \(\ell\ne0\): angular
differentiation kills every constant term in the finite cusp reflection.
The source split Mellin integral gives polynomial strip growth with
height order independent of \(r,S\).

## 3. Absorption at the natural length

Write \(\mathcal A_\sigma(R,S,t)\) for the left side of (Q4).
Squaring (Q8) and summing multiples of \(k\) yields

\[
 \mathcal A_{1/2-\delta}(R,S,t)
 \ll H^{4\delta}(1+|t|)^{8\delta}R^{4\delta+\eta}
 \sum_{Nk\le R,(k,S)=1}(Nk)^{-2\delta}
       \|\mathbf Q_{k,S}(1/2+\delta-it)\|^2.             \tag{Q9}
\]

For the original side of the free-split integral with Gaussian kernel,
the cubic large sieve in \(r\), followed by Minkowski in the complete
cube variable, gives

\[
 \sum_{Nr\le R}^{*}\|\mathbf I_{r,S}(1/2+\delta+it;Y)\|^2
 \ll(RY)^\eta\{R+Y^{1-2\delta}
                         +R^{2/3}Y^{2/3-2\delta}\}.     \tag{Q10}
\]

The coefficient \(\kappa(c)\eta_j(c)\) is bounded, so it has no cost
in this cubic sieve. At each fixed cube \(d\), the condition
\((r,dS)=1\) is a restriction of a positive row sum and can be retained.
The factor \(\xi_S(d)\) has modulus at most one. The three cube sums
have the same convergent exponents as in the angular untwisted proof.

Normalize a supremum over finite ranges of \(r,S\) and all heights by
\((RH)^{\epsilon_0}F_\delta(R,H)(1+|t|)^C\). It is finite before
absorption by the polynomial strip bounds. Each of the three powers
of \(R\) in (Q3) is greater than \(2\delta\), because
\(1/2-\delta>2\delta\) is exactly \(\delta<1/6\).
Partial summation in (Q9) therefore bounds the shifted integral, relative
to this normalization, by a constant times

\[
 M Y^{-4\delta}H^{4\delta}R^{2\delta+\eta}
                  (1+|t|)^{8\delta}.                    \tag{Q11}
\]

Choose

\[
 Y=C_0 R^{1/2+\theta}H(1+|t|)^2,
 \qquad 4\delta\theta>\eta.
\]

Choose the fixed \(C_0\) sufficiently large to make the coefficient
of \(M\) at most one half for every \(R\ge1\). Choose \(\eta,\theta\)
sufficiently small that all increases in (Q10) fit within
\((RH)^{\epsilon_0}\). Its three terms are then (Q3), up to this
allowed loss. This proves a uniform bound for the finite supremum;
letting both finite conductor cutoffs grow proves (Q4).

Finally apply (Q9) to (Q4), with \(\delta=1/2-p\). The three terms
respectively become
\(R^{1+2\delta}H^{4\delta}\),
\(R^{1/2+\delta}H^{1+2\delta}\), and
\(R^{1+\delta}H^{2/3+2\delta}\), which are exactly (Q5).

## 4. Consequence for a quadratic-twisted bilinear block

For \(|b_v|\le1\), define

\[
 T_\xi(A,B)=\sum_{u,v}b_v\widetilde g(uv)\alpha(uv)^\ell
                       \xi_S(uv)W_A(Nu/A)W_B(Nv/B).
\]

The natural character zeros impose coprimality with \(S\). Exact Gauss
multiplicativity converts Mellin inversion in \(u\) to the \(j=0\)
series (Q1), with cubic row \(r=v\). Cauchy--Schwarz in \(v\) and
(Q4), on a line arbitrarily close to \(1/2\), give

\[
 |T_\xi(A,B)|\ll(ABH)^\epsilon A^{1/2}
       \{B+B^{3/4}H^{1/2}+BH^{1/3}\}.                   \tag{Q12}
\]

The reciprocal cube factor is uniformly bounded on this line by absolute
Euler convergence. This step requires no zero-free assumption.

If a zero-free premise and its uniform reciprocal estimate permit the
line \(p+\epsilon\), \(1/3<p<1/2\), for the *quadratic-twisted angular*
Hecke factor in (Q2), then (Q5) gives

\[
 |T_\xi(A,B)|\ll(ABH)^\epsilon A^p
 \{B^{3/2-p}H^{1-2p}
  +B^{1-p/2}H^{1-p}
  +B^{5/4-p/2}H^{5/6-p}\}.                            \tag{Q13}
\]

An input concerning only the untwisted Hecke factor is not enough for
this conditional statement. The value \(p=(2\beta+1)/6\) is available
when the applicable family is zero-free to the right of \(\beta\), with
the required conductor-uniform reciprocal control.

## 5. What this does and does not improve at the actual terminal

The exact substitution in [TERMINAL_INTERFACE.md](TERMINAL_INTERFACE.md)
is \(A=U,B=L,H=K\). Its coefficient \(b_P(R)\) depends on the fixed
quadratic row, but (Q12)--(Q13) allow arbitrary bounded coefficients
at every fixed row. Dividing by \(\sqrt{UL}\), squaring, and summing
the \(O(K)\) quadratic rows is therefore legitimate and gives

\[
 U^{2p-1}\{L^{2-2p}K^{3-4p}
          +L^{1-p}K^{3-2p}
          +L^{3/2-p}K^{8/3-2p}\}.                       \tag{Q14}
\]

This improves the older pointwise-conductor envelope. Nevertheless,
at the binding scale \(U=KL\), its terms are

\[
 K^{2-2p}L,\qquad K^2L^p,\qquad K^{5/3}L^{p+1/2}.
 \tag{Q15}
\]

For the adverse range \(K\gg L\), the middle term alone exceeds the
inherited \(KL\) bound by \(K/L^{1-p}\). Thus this particular endpoint
does not improve that boundary-determining face. Interpolation of upper
bounds cannot improve a point where both available endpoints exceed
the existing one. This observation concerns that face only; it is not a
general barrier to new joint means.

The remaining candidate is a true joint \((r,S)\) mean that exploits
their two-character closure while preserving the row-dependent marked
coefficients. Separate cubic and quadratic/sextic large sieves at the
natural length \(Y\asymp\sqrt R H\) do not yet provide a natural-count
\(RH\) estimate. A theorem for spherical primitive sextic Kubota series
does not by itself supply this angular cubic-theta family.
