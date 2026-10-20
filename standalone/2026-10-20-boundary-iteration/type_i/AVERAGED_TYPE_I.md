# Averaging the completed cubic series before removing its Euler factor

Date: 2026-10-20. Status: proposed theorem; proof supplied for independent
review. Scope: an actual cubic Gauss bilinear block, with every common-prime
zero retained. This does not establish the complete sextic mixed moment or
an improved Hecke zero-free half-plane.

Source identity: Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, [arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
Proposition 5.2, (5.7), (5.13)--(5.14), and the coefficient derivation
(5.74)--(5.79). The other imported estimate is their Theorem 9.1,
Heath-Brown's unconditional cubic large sieve. No GRH-dependent estimate
from Sections 8--11 is used.

The inherited normalization and fixed-character reciprocal argument are
those in `../../2026-10-20-angular-hecke-continuation/ANGULAR_TYPE_I.md`.
Write \(E=\mathbb Q(\omega)\), \(\alpha(z)=z/|z|\),
\(\widetilde g(z)=g(z)/|z|\), and use primary generators throughout.
All levels are squarefree and prime to 3.

## 1. Statement

Fix a nonzero integer \(\ell\), \(1/2\le\beta<1\), and assume

\[
 Z_1(z,3\ell)\ne0\qquad(\Re z>\beta).
 \tag{1}
\]

Put \(p=(2\beta+1)/6\). Let \(r\) be squarefree, \(R=Nr\), and let
\(W_A,W_B\) be fixed smooth compactly supported functions on
\((0,\infty)\). For arbitrary \(|b_v|\le1\), define the complete sum

\[
 T=\sum_{u,v} b_v\widetilde g(uv)\alpha(uv)^\ell
        \overline{(uv/r)_3} W_A(Nu/A)W_B(Nv/B).
 \tag{2}
\]

**Proposed theorem.** If \(A,B\ge1\) and \(1\le R\le B^2\), then

\[
 \boxed{|T|\ll_{\ell,W_A,W_B,\epsilon}
 (ABR)^\epsilon A^p B^{3/2-4p/5}R^{1/2-3p/5}.}
 \tag{3}
\]

The constant also depends on the fixed input (1). The original pointwise
bound remains available outside this range. Equivalently, with \(X=AB\),

\[
 |T|\ll (ABR)^\epsilon X^{(2\beta+1)/6}
       (B^3R)^{(2-\beta)/5}.
 \tag{4}
\]

Consequently \(B^3R\le X^{5/3-\eta}\), with fixed \(\eta>0\), gives
a strict power saving over \(X^{5/6}\). For fixed \(r\), the admissible
short-divisor exponent is \(5/9\), improving the inherited
\(4(2-\beta)/(3(5-2\beta))\). At \(\beta=7/8\),

\[
 |T|\ll (ABR)^\epsilon A^{11/24}B^{17/15}R^{9/40},
 \qquad
 A=B=X^{1/2},\ R=1\quad\Longrightarrow\quad
 |T|\ll X^{191/240+\epsilon}.
 \tag{5}
\]

Thus the balanced cubic block has a saving \(3/80\) below \(5/6\).
This assertion applies to every bounded coefficient sequence, including a
coherent Mobius short-divisor mark. It does not replace a coupled quadratic
symbol in a sextic row by independent coefficients.

## 2. A truncated absolute bound for the actual dual coefficients

For a squarefree level \(k\), write \(K=Nk\). Proposition 5.2 gives

\[
 Q_k(s)=Z_k(3s-1/2,3\ell)\mathcal R_k(s),
 \quad
 \mathcal R_k(s)=\sum_c\widetilde g(c)\overline{(c/k)_3}
       \alpha(c)^\ell(Nc)^{-s}.
 \tag{6}
\]

Since \(\ell\ne0\), \(Q_k\) is entire. Its functional equation is

\[
 Q_k(s)=\varepsilon_{k,\ell}K^{1/2-2s}C_\ell(s)D_k(1-s),
 \quad |\varepsilon_{k,\ell}|=1,
 \tag{7}
\]

where

\[
 C_\ell(s)=\frac{i^\ell(2\pi)^{4s-2}}{3^{7/2}}
 \frac{\Gamma(5/6+|\ell|/2-s)\Gamma(7/6+|\ell|/2-s)}
      {\Gamma(s+|\ell|/2-1/6)\Gamma(s+|\ell|/2+1/6)}
 \tag{8}
\]

and
\(D_k(w)=Z_k(3w-1/2,-3\ell)\mathcal R_k^\dagger(w;-\ell)\).
Fixed unit phases can be put in either \(C_\ell\) or \(D_k\), without
affecting the following absolute estimates.

The dual coefficients have the exact support

\[
 \nu=\lambda^L\zeta h w(h')^3,
 \quad L\ge-1,\quad h\mid k,\quad h'\mid k^\infty,
 \quad(w,k)=1,\quad\mu_E^2(hw)=1.
 \tag{9}
\]

The inherited coefficient calculation proves

\[
 |a^\dagger(\nu)|\le C3^{L/6}(Nh')^{1/2},\qquad
 |b_k^\dagger(\nu)|\le Nh\,N\operatorname{rad}(h').
 \tag{10}
\]

The second inequality follows directly from
\(|b_k^\dagger(\nu)|=\varphi_E((\lambda\nu,k))\) and squarefreeness
of \(k\). Overlap between \(h\) and \(h'\) only makes (10) weaker.

**Lemma.** For every fixed \(\sigma>0\), \(T\ge1\), and
\(\epsilon>0\),

\[
 \sum_{N\nu\le T}|a^\dagger(\nu)b_k^\dagger(\nu)|
                  (N\nu)^{\sigma-1}
       \ll_{\sigma,\epsilon} T^\sigma K^\epsilon.
 \tag{11}
\]

Indeed the number of primary elements of norm at most \(V\) is \(O(V)\),
so \(\sum_{Nw\le V}(Nw)^{\sigma-1}\ll_\sigma V^\sigma\) for
\(V\ge1\). Fix \(L,\zeta,h,h'\) in (9) and apply this estimate with
\(V=T/(3^LNh(Nh')^3)\), omitting an empty range when \(V<1\).
The bound for that slice is

\[
 C_\sigma T^\sigma 3^{-5L/6}
          \frac{N\operatorname{rad}(h')}{(Nh')^{5/2}}.
 \tag{12}
\]

The \(h\)-sum costs \(\tau_E(k)\ll_\epsilon K^\epsilon\).
The unit and ramified sums converge. Finally

\[
 \sum_{h'\mid k^\infty}
 \frac{N\operatorname{rad}(h')}{(Nh')^{5/2}}
 =\prod_{\mathfrak p\mid k}
 \left(1+\frac{(N\mathfrak p)^{-3/2}}
                 {1-(N\mathfrak p)^{-5/2}}\right)
 \ll_E1.
 \tag{13}
\]

This proves (11), retaining all repeated cube-prime powers. Multiplication
by the dual zeta factor in (7) adds a cube variable \(d\), coprime to
\(k\), with coefficient \((Nd)^{1/2}\). Applying (11) at
\(T/(Nd)^3\) leaves the convergent factor \(\sum_d(Nd)^{-5/2}\).
Thus the coefficients \(d_k(n)\) of the *complete* dual \(D_k\) satisfy

\[
 \sum_{Nn\le T}|d_k(n)|(Nn)^{\sigma-1}
       \ll_{\sigma,\epsilon}T^\sigma K^\epsilon.
 \tag{14}
\]

Here \(n\) is allowed the fixed ramified fractional norms from (9).
The statement remains valid for \(T\ge1/3\) after changing the constant.

As a second check on the exponent, the inherited absolute Dirichlet bound
at \(1+\eta\) implies (11) with \(T^{\sigma+\eta}\) by multiplying
each summand by at most \(T^{\sigma+\eta}\). That weaker bound, with
arbitrarily small \(\eta>0\), already suffices for every stated result.

## 3. An approximate functional equation with a free split

Fix \(0<\sigma<1/2\), \(s=\sigma+it\), and \(Y\ge1\).
Set

\[
 I_k(s;Y)=\frac1{2\pi i}\int_{(c)}Q_k(s+z)Y^z e^{z^2}\frac{dz}{z},
 \qquad c>1-\sigma.
 \tag{15}
\]

The entire continuation and finite vertical growth supplied by the completed
Mellin integrals in DR (5.49)--(5.52) justify shifting to
\(\Re z=-\sigma-\eta\), for fixed \(\eta>0\). The only crossed
pole is \(z=0\). Substituting (7) on the new line gives

\[
 Q_k(s)=I_k(s;Y)+J_k(s;Y).
 \tag{16}
\]

The sign of \(J_k\) is immaterial here. It is a Dirichlet series with
prefactor \(K^{1/2-2s}\), coefficients \(d_k(n)(Nn)^{s-1}\), and
weight

\[
 V_s(x)=-\frac1{2\pi i}\int_{(-\sigma-\eta)}
       C_\ell(s+z)x^z e^{z^2}\frac{dz}{z},
 \qquad x=\frac{NnY}{K^2}.
 \tag{17}
\]

For fixed \(\ell,\sigma\), this weight is bounded as \(x\to0\) and
decays faster than every inverse power as \(x\to\infty\), with a fixed
polynomial cost in \(1+|t|\). For \(x\le1\), move the line a fixed
distance to the right of zero, staying left of the first numerator gamma
pole \(s+z=5/6+|\ell|/2\), and include the residue at zero. For
\(x\ge1\), move left arbitrarily far; the numerator gamma factors have
no poles in that direction. Stirling's formula and \(e^{-\Im(z)^2}\)
control every horizontal segment and give the asserted polynomial costs.

For \(1\le Y\le K^2\), (14) and dyadic summation now imply

\[
 |J_k(\sigma+it;Y)|
 \ll_{\ell,\sigma,\epsilon}
 (1+|t|)^C K^{1/2+\epsilon}Y^{-\sigma}.
 \tag{18}
\]

This is an absolute dual estimate; no unexplained cancellation is used in
the dual sum.

## 4. Cubic large sieve for the original part

Fix squarefree \(r\), and average over squarefree \(v\asymp B\) with
\((v,r)=1\); then \(k=rv\) and \(K\asymp RB\). Expand (15) on its
initial line. Its coefficients are precisely

\[
 \sum_{(d,rv)=1}(Nd)^{1/2-3s}\alpha(d)^{3\ell}
  \sum_c\widetilde g(c)\alpha(c)^\ell\overline{(c/r)_3}
        \overline{(c/v)_3}(Nc)^{-s}
        V\!\left(\frac{Nc(Nd)^3}{Y}\right),
 \tag{19}
\]

where \(V(x)=\frac1{2\pi i}\int_{(c)}x^{-z}e^{z^2}dz/z\).
It is bounded near zero and rapidly decreasing at infinity. The \(c\)
coefficients are squarefree because \(|\widetilde g(c)|=\mu_E^2(c)\).
All zero extensions and \((d,rv)=1\) restrictions remain in (19).

For each fixed \(d\), restrict the \(v\)-rows to \((d,rv)=1\), and
apply the unconditional cubic large sieve. The fixed factor
\(\overline{(c/r)_3}\) is part of the column coefficients and has modulus
at most one. With \(C=Y/(Nd)^3\), the resulting square-root bound is

\[
 (BY)^\epsilon
 \left(B^{1/2}C^{1/2-\sigma}
       +C^{1-\sigma}+B^{1/3}C^{5/6-\sigma}\right).
 \tag{20}
\]

A dyadic decomposition handles the smooth tails. Minkowski's inequality
then sums over \(d\). Multiplying (20) by \((Nd)^{1/2-3\sigma}\)
leaves respectively powers \((Nd)^{-1},(Nd)^{-5/2},(Nd)^{-2}\).
The first contributes only a logarithm, and the others converge. Therefore

\[
 \left(\sum_{v\asymp B}^{*}|I_{rv}(\sigma+it;Y)|^2\right)^{1/2}
 \ll_{\sigma,\epsilon}(BY)^\epsilon
 \left(B^{1/2}Y^{1/2-\sigma}+Y^{1-\sigma}
                         +B^{1/3}Y^{5/6-\sigma}\right).
 \tag{21}
\]

The asterisk retains squarefreeness and \((v,r)=1\). The estimate is
uniform in \(t\) and the fixed angular phase on this original side.

Combining (18) and (21) gives the useful free-split bound

\[
 \|Q_{rv}(\sigma+it)\|_{\ell^2(v\asymp B)}
 \ll (1+|t|)^C(BR Y)^\epsilon
 \left(B^{1/2}Y^{1/2-\sigma}+Y^{1-\sigma}
  +B^{1/3}Y^{5/6-\sigma}+BR^{1/2}Y^{-\sigma}\right).
 \tag{22}
\]

Take \(Y=B^{4/5}R^{3/5}\). If \(1\le R\le B^2\), then
\(B^{1/2}\le Y\le B^2\) and \(Y\le(RB)^2\). Hence the first two
terms in (22) are bounded by its third term, and the last two terms are
equal. It follows that

\[
 \boxed{\|Q_{rv}(\sigma+it)\|_2
 \ll (1+|t|)^C(BR)^\epsilon
       B^{1-4\sigma/5}R^{1/2-3\sigma/5}.}
 \tag{23}
\]

In particular, at \(r=1\),

\[
 \sum_{v\asymp B}^{*}|Q_v(\sigma+it)|^2
 \ll (1+|t|)^C B^{2-8\sigma/5+\epsilon}.
 \tag{24}
\]

## 5. Return to the complete marked sum

Take \(\sigma=p+\delta<1/2\). The zero-free hypothesis (1), the fixed
Hecke reciprocal estimate, and the elementary deleted-Euler-factor bound
give

\[
 |Z_{rv}(3s-1/2,3\ell)^{-1}|
 \ll_{\ell,\delta,\epsilon}(1+|t|)^C(RB)^\epsilon.
 \tag{25}
\]

Thus (23) also bounds \(\mathcal R_{rv}(s)\), with a possibly larger
fixed polynomial height factor. Exact twisted multiplicativity gives

\[
 T=\frac1{\widetilde g(r)}\sum_{\substack{v\text{ squarefree}\\(v,r)=1}}
      b_v\alpha(v)^\ell W_B(Nv/B)
      \sum_u\widetilde g(urv)\alpha(u)^\ell W_A(Nu/A).
 \tag{26}
\]

Equivalently, Mellin inversion puts the bounded row phases
\(\widetilde g(rv)/\widetilde g(r)\) beside \(\mathcal R_{rv}(s)\).
The \(\ell^2\) norm of the outer coefficients is \(O(B^{1/2})\).
Move the common Mellin line from \(\Re s>1\) to \(\sigma=p+\delta\).
There is no residue because \(\ell\ne0\). Cauchy--Schwarz in \(v\),
(23)--(25), and the rapid Mellin decay of \(W_A\) give

\[
 |T|\ll (ABR)^\epsilon
 A^{p+\delta}B^{3/2-4(p+\delta)/5}R^{1/2-3(p+\delta)/5}.
 \tag{27}
\]

Taking \(\delta\) and the intermediate divisor losses sufficiently small
in terms of the stated \(\epsilon\) proves (3).

## 6. Scope and remaining interfaces

This is an average of the *completed cubic series* before its fixed angular
Euler factor is removed. The whole completed dual, including cubes and
common-prime factors, is controlled in (14); replacing it by only its
squarefree coefficients would not prove (18).

For a fixed nonzero angular order there is also the unconditional baseline

\[
 |T|\ll_{\ell,W_A,W_B,\epsilon}
 (ABR)^\epsilon A^{1/2}B^{11/10}R^{1/5}.
 \tag{28}
\]

To prove it, use the same approximate functional equation with
\(\sigma=1/2+\delta\), where \(0<\delta<1/8\). In the original-polynomial
bound (21), the first term becomes \(B^{1/2}\), because
\(\sum_c(Nc)^{-2\sigma}\ll_\delta1\); the \(d\)-sum for that term now
converges with power \(-1-3\delta\). The other two terms retain their
displayed powers. With \(Y=B^{4/5}R^{3/5}\), the third term is
\(B^{3/5-4\delta/5}R^{1/5-3\delta/5}\), which dominates \(B^{1/2}\)
for these \(\delta\) and \(R\ge1\). The dual bound is unchanged.
Finally \(3\sigma-1/2>1\), so the reciprocal in (25) is bounded directly
by the absolutely convergent Euler product; no hypothesis (1) is used.
The final Mellin argument proves (28). In particular the balanced block
is \(O(X^{4/5+\epsilon})\) unconditionally, saving \(1/30\) below \(5/6\).

No assertion of uniformity in a growing angular order, radial parameter,
or finite character family is needed. The finite level \(r\) can grow in
the explicit range \(R\le B^2\). The improvement concerns this actual
cubic block, not all the source's quadratic/cubic/sextic rows at once.
The map from this block to a changed critical class count remains open.
