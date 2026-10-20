# A conductor-uniform signed inverse consequence of a fixed Hecke boundary

Status: a written analytic implication of the imported universal zero-free
theorem. This note proves no smaller zero-free boundary. It turns the
import into a quantitative bound for the actual signed ideal-Mobius
coefficients, uniformly over the finite-order characters of a fixed field.
The tools are classical complex analysis and Perron inversion; no novelty
claim is made for this general implication.

## 1. Statement and quantifiers

Fix a number field K of degree n. Suppose that for one B in [1/2,1),
every primitive finite-order Hecke L-function of K is zero-free in
Re(s)>B, with the simple principal pole at one allowed. Let f_chi be the
finite conductor, q_chi=N(f_chi), and extend chi by zero on ideals not
coprime to f_chi. For every delta>0 and every e>0,

\[
 \frac1{|L_K(\sigma+it,\chi)|}
 \ll_{K,\delta,e}
 \{q_\chi(3+|t|)^n\}^{e},
 \qquad \sigma\ge B+\delta.                         \tag{1}
\]

At the principal pole, the reciprocal is defined by its holomorphic
continuation, whose value is zero. In addition, for every epsilon>0,

\[
 \boxed{\left|\sum_{N\mathfrak a\le X}
       \mu_K(\mathfrak a)\chi(\mathfrak a)\right|
       \ll_{K,\epsilon}q_\chi^\epsilon X^{B+\epsilon},
       \qquad X\ge2.}                              \tag{2}
\]

The implicit constants are independent of chi, q_chi, X and t, once K
and the displayed positive gaps are fixed. They are not asserted to be
uniform in K. The proof of Liu's theorem need not provide a bound for its
own target-dependent constants: its common zero-free half-plane, together
with the classical conductor-uniform growth of Hecke functions, is enough.

Liu's Theorem 17.1 supplies B=B_flat=0.874886647039964... as an external
preprint theorem. Thus (2) applies over every fixed number field, with the
same exponent and field-dependent constants. It includes the principal
character and its actual signed ideal-Mobius sum.

## 2. Uniform control of the logarithm

Write e_chi=1 for the principal character and zero otherwise, and set

\[
 F_\chi(s)=\left(\frac{s-1}{s+1}\right)^{e_\chi}L_K(s,\chi).
                                                               \tag{3}
\]

The residue of the principal zeta function at one is nonzero, so F_chi
is holomorphic and nowhere zero throughout Re(s)>B, including one.
The factor s+1 has no zero in this half-plane. Consequently it admits
a holomorphic logarithm h_chi, chosen by the absolutely convergent Euler
logarithm and the indicated rational factor on Re(s)>1.

For Re(s)>=3/2, h_chi is uniformly bounded in chi and Im(s). The Euler
series is bounded by that of zeta_K, and the rational factor and its
chosen logarithm are bounded in the same region. The functional equation
and the Euler product also give, on every fixed bounded real strip contained in Re(s)>B,
a polynomial upper bound for the pole-removed F_chi:

\[
 |F_\chi(\sigma+it)|\ll_K
       \{q_\chi(3+|t|)^n\}^{A_K},                 \tag{4}
\]

with an exponent depending only on the strip and K. This is the usual
Hecke convexity/growth input; finite-order real infinity types range
over a finite set. Only an upper polynomial bound is used here.

It suffices to take 0<delta<1-B. For a point on the line sigma=B+delta,
center three disks at c=2+it, with radii

\[
 r_0=\tfrac12,\quad r=2-B-\delta,\quad
 R=2-B-\tfrac\delta2,\quad R_+=2-B-\tfrac\delta4.
\]

They satisfy r_0<r<R<R_+, and the largest disk lies inside Re(s)>B.
The real-part bound for h_chi on that disk follows from (4):
Re(h_chi)=log|F_chi| is at most O_{K,delta}(log Q), where
Q=q_chi(3+|t|)^n. Borel-Caratheodory, using the uniformly bounded value
h_chi(c), gives

\[
 \max_{|s-c|\le R}|h_\chi(s)|
       \ll_{K,\delta}\log Q.
\]

On the smaller disk of radius r_0, the Euler logarithm is uniformly
bounded. Hadamard's three-circles theorem therefore yields

\[
 |h_\chi(B+\delta+it)|
 \ll_{K,\delta}(\log Q)^\vartheta,
 \qquad
 \vartheta=\frac{\log(r/r_0)}{\log(R/r_0)}<1.       \tag{5}
\]

The same bound holds to the right of this line up to Re(s)=2 by the same
disk, and further right by the Euler product. Polynomial conductors at
points of a disk of bounded radius are comparable with Q uniformly in
chi and t. Thus all constants in (5) have the stated uniformity.

For every e>0, exp(C(log Q)^vartheta)<=C_e Q^e because vartheta<1.
Since Re(s)>0 gives |(s-1)/(s+1)|<=1, (3) shows that
|1/L_K(s,chi)|<=exp(|h_chi(s)|). This proves (1), with the continued
reciprocal at the principal pole included.

## 3. Perron inversion keeps the signed coefficients

In the absolute-convergence half-plane,

\[
 \frac1{L_K(s,\chi)}
 =\sum_{\mathfrak a}\frac{\mu_K(\mathfrak a)\chi(\mathfrak a)}
                         {(N\mathfrak a)^s}
 =\sum_{m\ge1}\frac{a_\chi(m)}{m^s}.              \tag{6}
\]

The coefficients obey |a_chi(m)|<=d_n(m), where d_n is the coefficient
of zeta(s)^n. At each rational prime, the number of prime-ideal factors
is at most n and their residue degrees are positive; this bounds the
ideal-counting Euler coefficients by those of (1-p^-s)^-n. Hence, for
each fixed eta>0, |a_chi(m)|<<_{K,eta}m^eta uniformly in chi.

Let x=floor(X)+1/2, c=1+1/log(x), and T=x^2. Every ideal norm is an
integer, so the sums up to x and X are equal. The usual truncated Perron
formula on Re(s)=c has an error bounded by

\[
 \sum_{m\ge1}|a_\chi(m)|(x/m)^c
       \min\{1,(T|\log(x/m)|)^{-1}\}.             \tag{7}
\]

The distance |x-m|>=1/2, the bound by d_n(m), and a split into m near x
and its complement bound (7) by O_{K,eta}(x^{1+eta}(log(2x))^{n+1}/T).
A weaker O_{K,eta}(x^eta) bound is sufficient below. This estimate is
uniform in chi and does not estimate the signed sum by an unsigned
main term.

Choose 0<epsilon<1-B, delta=epsilon/2 and
e=epsilon/(8n). Move the contour to sigma_0=B+delta. The reciprocal
has no poles in the enclosed region, including at one, so no residue
is crossed. By (1) its new vertical integral is

\[
 \ll q_\chi^e x^{\sigma_0}
       \left(1+\int_1^T t^{ne-1}\,dt\right)
 \ll_{K,\epsilon}q_\chi^e x^{B+3\epsilon/4}.
\]

Each horizontal integral is at most
O_{K,epsilon}(q_chi^e x^c T^{ne-1}), which is smaller. Select the eta
in (7) sufficiently small and absorb any logarithms in the remaining
epsilon/4 margin. Since e<=epsilon and q_chi>=1, this proves (2).
For larger epsilon, use any smaller positive epsilon first.

No estimate for 1/L is used on or left of the imported boundary. The
proof therefore cannot be recycled to claim convergence of (6) in the
unknown part of the critical strip.

## 4. The exact benefit to the repository

Partial summation in (2) gives ordinary locally uniform convergence of
the signed Dirichlet series (6) on Re(s)>B, for each fixed chi. On a
compact set a positive distance from B, the tail satisfies the usual
X^{B+epsilon-sigma} bound, with polynomial dependence on |s| and the
same q_chi^epsilon loss. Thus the import supplies actual signed
reciprocal coefficients and an explicit conductor-uniform estimate in
its available half-plane.

This does not prove the complete mixed U^(6/5) mean of PR #1006, which
uses different coupled variables and requires control where this
simple reciprocal estimate is insufficient. It also does not apply to
the infinite-order angular character in the quartic numerator. It is a
usable consequence of the new source, not a replacement for either
missing analytic step.

Source: Liu, arXiv:2610.26835v1, Theorem 17.1, for the zero-free input;
its Lemma 14.2 and Section 18 record the finite-order Hecke functional
equation and field scope. The logarithmic argument here is written out
from Borel-Caratheodory and Hadamard three-circles, and the signed
inversion is written out from Perron's formula. Standard Hecke analytic
properties are also recorded in Thorner-Zaman, arXiv:1803.02823v3,
Section 2.3. None of the finite checkers in this packet certify the
external analytic theorem or this contour argument.
