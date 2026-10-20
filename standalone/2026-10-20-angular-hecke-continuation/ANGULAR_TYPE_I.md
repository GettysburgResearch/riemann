# Angular cubic Type-I cancellation from a fixed Hecke zero-free half-plane

Date: 2026-10-20. Status: a proved transfer theorem with the explicitly
stated input \(H_\beta(3\ell)\). Substituting the new angular Hecke theorem
uses the source-dependent candidate proved in the companion adapters; its review scope is stated in this packet. This argument does not assume
the complete mixed inverse/plain moment sought in PR #1006.

## 1. Source and conventions

Alexander Dunn and Maksym Radziwiłł, *Bias in cubic Gauss sums:
Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), 14 May 2024.
The exact inputs are (2.2)--(2.3), the theta coefficient formulas
(5.7), (5.13)--(5.14), Proposition 5.2, and its coefficient derivation
(5.74), (5.77)--(5.79). The completed Mellin representation in the proof
of Proposition 5.1, especially (5.49)--(5.52), supplies finite vertical
growth. No statement conditional on GRH in Section 8 is used.

The full HTML downloaded on 2026-10-20 is
the externally pinned HTML in `SOURCES.json`, 2,792,599 bytes, SHA-256
`3949e0f0ae87808d84fe02c12a3b68c5b66aa8d967d8ecb5e1605f1d985b956d`.
The locally derived searchable text has
SHA-256
`3262a76247d6f829fe456a68c011f001c624b2b555bffb8b2e67feb26c929d07`.

Put \(E=\mathbb Q(\omega)\), \(\mathcal O=\mathbb Z[\omega]\),
\(\lambda=\sqrt{-3}\), and \(N z=|z|^2\). All element sums below use
the unique generator \(u\equiv1\pmod3\) of an ideal coprime to 3.
Write

\[
 \alpha(u)=u/|u|,\qquad \widetilde g(u)=g(u)/|u|.
\]

Here \(g\) is exactly the cubic Gauss sum with additive character used
in the source. Its two needed identities are

\[
 |\widetilde g(u)|=\mu_E^2(u),\qquad
 \widetilde g(uv)=\widetilde g(u)\widetilde g(v)
                  \overline{(u/v)_3}.
 \tag{1}
\]

The second identity includes noncoprime \(u,v\): both sides then vanish.
The angular character \(\alpha^j\) means the Hecke character on these
primary generators, with the fixed convention at 3. Put

\[
 Z_r(z,j)=\sum_{(a,r)=1}\alpha(a)^j(Na)^{-z}
 =Z_1(z,j)\prod_{\mathfrak p\mid r}
       (1-\alpha(\mathfrak p)^j(N\mathfrak p)^{-z}).
 \tag{2}
\]

In the source this is denoted
\(\zeta_E(z;\mathbf1_r,j)\). It is the corresponding Hecke function
with the original Euler factor at 3 omitted. We do not add a family of
growing finite characters or growing angular orders to the theorem.

## 2. The theorem

Fix \(\ell\in\mathbb Z\) and \(1/2\le\beta<1\). The input is

\[
 H_\beta(3\ell):\qquad
 Z_1(z,3\ell)\ne0\quad(\Re z>\beta),
 \tag{3}
\]

with its possible pole at \(z=1\), when \(\ell=0\), permitted. Define

\[
 p_\beta=\frac{2\beta+1}{6},\qquad
 q_\beta=\frac{5-2\beta}{12}=\frac{1-p_\beta}{2},\qquad
 c_E=\frac{(2\pi)^{5/3}}{3^{7/2}\Gamma(2/3)}.
 \tag{4}
\]

**Theorem.** Assume (3). For every fixed smooth compactly supported
\(W:(0,\infty)\to\mathbb C\), every \(\varepsilon>0\), every
squarefree primary \(r\), and \(X\ge1\), writing \(R=Nr\),

\[
 \boxed{
 \sum_u\widetilde g(ur)\alpha(u)^\ell W(Nu/X)
 =\mathbf1_{\ell=0}\,c_E\widehat W(5/6)X^{5/6}
    \frac{\varphi_E(r)}{R^{7/6}Z_r(2,0)}
 +O_{\ell,W,\varepsilon}\!\left(
       X^{p_\beta+\varepsilon}R^{q_\beta+\varepsilon}\right).}
 \tag{5}
\]

Here \(\widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx\).
The constants also depend on the fixed Hecke zero-free input (3).
In particular, **there is no main term for every fixed nonzero
\(\ell\)**. Shared primes are retained through the zero extensions in
(1); the theorem does not replace them by coprimality-free phases.

For comparison, the same proof using only the absolutely convergent
Euler product shifts to \(\Re s=1/2+\varepsilon\) and gives the
baseline error \(X^{1/2+\varepsilon}R^{1/4+\varepsilon}\).
The new error in (5) improves its scale exponents by the factor
\[
 \left(\frac{R^{1/2}}{X}\right)^{(1-\beta)/3}.
\]
For fixed \(r\), this saves \(X^{(1-\beta)/3}\): the savings are
\(X^{1/36}\) at \(\beta=11/12\), and approximately
\(X^{0.041704450986679}\) at \(\beta=B_\flat\).

The bound has finite test-seminorm order on a fixed annulus. Consequently
replacing \(W(x)\) by \(x^{it_0}W(x)\) costs a fixed polynomial in
\(1+|t_0|\). There is no assertion of uniformity when \(|\ell|\) grows
with \(X,R\), or a Mellin height.

### Exact candidate substitutions

| Accepted input \(\beta\) | \(p_\beta\) | \(q_\beta\) |
|---|---:|---:|
| \(11/12\) | \(17/36\) | \(19/72\) |
| \(7/8\) | \(11/24\) | \(13/48\) |
| \(B_\flat\) | \((2B_\flat+1)/6\) | \((5-2B_\flat)/12\) |

For \(B_\flat=0.874886647039964\ldots\), the last row is approximately
\(p_\beta=0.458295549013321\) and
\(q_\beta=0.270852225493339\). These decimal values describe (4);
they do not prove the input (3).

The source-dependent angular family in [ANGULAR_BOOTSTRAP.md](ANGULAR_BOOTSTRAP.md), with descent in [FAMILY_DESCENT.md](FAMILY_DESCENT.md), is
\(\Lambda^m\xi\), with \(m\notin\{-1,1\}\) and \(\xi\) finite
order. The factor required in (3) has angular order \(3\ell\).
Every nonzero \(3\ell\) avoids the two excluded orders. Any fixed
convention difference between \(\alpha\) and \(\Lambda\) is a finite
ray character and must be retained when invoking that companion theorem.
The required input is over \(E\), so its field-descent step must also be
part of that invocation.

## 3. Absolute control of the actual dual coefficients

Set

\[
 \mathcal R_r(s;\ell)=
 \sum_u\widetilde g(u)\overline{(u/r)_3}\alpha(u)^\ell(Nu)^{-s},
 \qquad
 Q_r(s;\ell)=Z_r(3s-1/2,3\ell)\mathcal R_r(s;\ell).
 \tag{6}
\]

Proposition 5.2 expresses the dual series through the actual coefficients
\(a^\dagger(\nu)b_r^\dagger(\nu)\). We use the derivation (5.79)
to read them. Its support has the unique form

\[
 \nu=\lambda^L\zeta h w(h')^3,
 \quad L\ge-1,\quad \zeta\in\mathcal O^\times,
 \quad h\mid r,\quad h'\mid r^\infty,
 \quad (w,r)=1,\quad \mu_E^2(hw)=1.
 \tag{7}
\]

The factor in (5.79) is the coefficient \(a^\star(\lambda^{-3}\nu)\),
and, up to a phase of modulus one,

\[
 b_r^\dagger(\nu)=
 \mu_E\!\left(\frac r{(\lambda\nu,r)}\right)
 \frac{\varphi_E(r)}{\varphi_E(r/(\lambda\nu,r))}.
 \tag{8}
\]

This also specifies the ramified scaling without relying on the repeated
\(\lambda\)-power printed in the display (5.67). The proof's (5.79)
has at most one summand for each \(\nu\).

For a squarefree primary \(c\), the Gauss sums with the coprime
arguments occurring in (5.7), (5.13), and (5.14) have modulus \(|c|\).
Consequently those three formulas, applied to (7), give

\[
 |a^\dagger(\nu)|\le C\,3^{L/6}|h'|,
 \tag{9}
\]

with an absolute \(C\). To check the ramified exponents directly:
in the two branches of (5.7), respectively
\(L=3n-1\) and \(L=3n\); their multipliers are
\(3^{n/2+2}\) and \(3^{n/2+5/2}\). At \(L=-1\), (5.13)--(5.14)
give the fixed multiplier 9. Thus one may take \(C=3^{5/2}\).

**Dual coefficient lemma.** For every \(\eta,\varepsilon>0\),

\[
 \sum_{\nu\ne0}
 \frac{|a^\dagger(\nu)b_r^\dagger(\nu)|}{(N\nu)^{1+\eta}}
 \ll_{\eta,\varepsilon} R^\varepsilon.
 \tag{10}
\]

Here is the full local calculation. Put \(s=1+\eta\). The unit sum
costs at most 6, and the ramified sum is bounded by
\(C\sum_{L\ge-1}3^{-L(s-1/6)}\). The squarefree \(w\)-sum is at
most \(\zeta_E(s)\). At a prime \(\mathfrak p\mid r\), put
\(q=N\mathfrak p\), let the exponent of \(h\) be
\(a\in\{0,1\}\), and the exponent of \(h'\) be \(j\ge0\).
The factor from (8) has modulus 1 when \(a=j=0\), and \(q-1\)
otherwise. The exact resulting upper-bound factor is

\[
 F_q(s)=1+(q-1)q^{-s}
 +(q-1)(1+q^{-s})\frac{q^{1/2-3s}}{1-q^{1/2-3s}}.
 \tag{11}
\]

For \(s\ge1\), \(F_q(s)\le3\). Therefore the remaining product is
at most \(3^{\omega_E(r)}\ll_\varepsilon R^\varepsilon\).
The last inequality follows by absorbing each prime with
\(q\ge3^{1/\varepsilon}\) individually into \(q^\varepsilon\);
only a fixed finite set of smaller prime ideals remains. This proves
(10), including every power \((h')^3\), all allowed shared primes,
and the ramified branch.

## 4. Convexity for the completed cubic series

The exact functional equation of Proposition 5.2 is

\[
 Q_r(s;\ell)=
 \overline{g(r)}(\bar r/r)^{-\ell}
 \frac{i^\ell(2\pi)^{4s-2}}{3^{7/2}R^{2s}}
 G_\ell(s)
 Z_r(5/2-3s,-3\ell)\mathcal R_r^\dagger(1-s;-\ell),
 \tag{12}
\]

where

\[
 G_\ell(s)=
 \frac{\Gamma(5/6+|\ell|/2-s)\Gamma(7/6+|\ell|/2-s)}
      {\Gamma(s+|\ell|/2-1/6)\Gamma(s+|\ell|/2+1/6)}.
 \tag{13}
\]

The dual Dirichlet series in (12) is the one in (10), with the angular
phase \(\alpha(\nu)^{-\ell}\) and a fixed unit factor. No absolute
value is placed inside a coefficient sum before (10) is proved.

Choose a sufficiently small \(\eta>0\). On \(\Re s=1+\eta\), the
two original Dirichlet series in (6) converge absolutely, uniformly in
\(r\), so \(Q_r(s;\ell)\ll_\eta1\). On \(\Re s=-\eta\),
the dual zeta factor in (12) has real argument \(5/2+3\eta\), and
(10) applies at \(1-s\). Stirling's formula gives, for fixed \(\ell\),

\[
 |G_\ell(-\eta+it)|\ll_{\ell,\eta}(1+|t|)^{2+4\eta}.
\]

Since \(|g(r)|=R^{1/2}\),

\[
 Q_r(-\eta+it;\ell)
 \ll_{\ell,\eta,\varepsilon}
 R^{1/2+2\eta+\varepsilon}(1+|t|)^{2+4\eta}.
 \tag{14}
\]

Proposition 5.2 states that \(Q_r\) is entire for \(\ell\ne0\).
For \(\ell=0\), its only pole is the simple pole at \(5/6\).
In that case multiply by \((s-5/6)/(s+2)\) before interpolation.
The completed Mellin integrals (5.49)--(5.52) have exponentially
decaying theta functions at their infinite endpoints; after removing
the gamma factors they give at most exponential vertical growth on a
fixed strip. Thus the usual strip Phragmén--Lindelöf argument applies
to these two boundary estimates. Uniformly on closed substrips, away
from the stated pole when \(\ell=0\), it gives

\[
 Q_r(\sigma+it;\ell)
 \ll_{\ell,\eta,\varepsilon}
 R^{(1-\sigma)/2+O(\eta)+\varepsilon}
 (1+|t|)^{A_{\ell,\eta}}.
 \tag{15}
\]

In particular (15) holds on the line
\(\sigma=p_\beta+\delta\), for any fixed sufficiently small
\(\delta>0\). The pole-clearing factor can be restored there with
a bounded cost because that line stays a positive distance from
\(5/6\). The constant in \(O(\eta)\) is absolute; \(\eta\) may
be taken small enough in terms of the final \(\varepsilon\).

## 5. Removing the cubic completion and shifting the smooth sum

For a fixed Hecke character, (3) implies that for every \(\delta>0\)
there is a finite \(A\) such that

\[
 |Z_1(z,3\ell)^{-1}|
 \ll_{\ell,\delta}(1+|\Im z|)^A,
 \qquad \Re z\ge\beta+\delta.
 \tag{16}
\]

One may derive (16) by applying Borel--Carathéodory to a branch of
\(\log Z_1\) on fixed-radius zero-free disks, using the ordinary
polynomial upper bounds for a fixed Hecke function and its absolutely
convergent Euler product at a fixed point to the right of 1. In the
principal case first remove the pole with the factor
\((z-1)/(z+1)\). Its reciprocal is holomorphic at the original pole,
so restoring it causes no difficulty. A fixed chain of disks suffices
at every height; no number of disks grows with \(r,X\), or height.

For \(\Re z\ge\beta+\delta>0\), the local deletions in (2) satisfy

\[
 \prod_{\mathfrak p\mid r}
 |1-\alpha(\mathfrak p)^{3\ell}(N\mathfrak p)^{-z}|^{-1}
 \le\prod_{\mathfrak p\mid r}(1-(N\mathfrak p)^{-\beta-\delta})^{-1}
 \ll_{\delta,\varepsilon}R^\varepsilon.
 \tag{17}
\]

To justify the last estimate, each sufficiently large prime factor is
at most \((N\mathfrak p)^\varepsilon\), and the finitely many small
primes cost a constant. Combining (15)--(17), on
\(\sigma=p_\beta+\delta\) we obtain

\[
 \mathcal R_r(\sigma+it;\ell)
 \ll_{\ell,\delta,\varepsilon}
 R^{q_\beta+O(\eta)+\varepsilon}(1+|t|)^{A'}.
 \tag{18}
\]

The identity in (6), the input (3), and the exact pole statement for
\(Q_r\) show that there are no other poles between this line and a
line to the right of 1. This is where the angular zero-free input is
used. In particular it is the order \(3\ell\) Hecke function that
must be protected, not a finite-order substitute.

By (1), Mellin inversion writes the sum in (5) as

\[
 \frac{\widetilde g(r)}{2\pi i}
 \int_{(1+\eta)}\mathcal R_r(s;\ell)\widehat W(s)X^s\,ds.
 \tag{19}
\]

Move the line to \(p_\beta+\delta\). The Mellin transform of \(W\)
decays faster than every power on the fixed strip, whereas (18) has a
fixed polynomial height cost. The horizontal segments tend to zero.
For \(\ell\ne0\), no residue is crossed, giving the error in (5).
For \(\ell=0\), Proposition 5.2 gives exactly

\[
 \operatorname*{Res}_{s=5/6}Q_r(s;0)
 =c_E\frac{\overline{g(r)}\varphi_E(r)}{R^{5/3}}.
 \tag{20}
\]

At \(s=5/6\), the completion is \(Z_r(2,0)\). Multiplying (20) by
\(\widetilde g(r)\widehat W(5/6)X^{5/6}/Z_r(2,0)\), and using
\(\widetilde g(r)\overline{g(r)}=R^{1/2}\), gives the main term in
(5). Taking the internal \(\delta,\eta\) and divisor-loss exponents
small enough in terms of the stated \(\varepsilon\) proves (5).

Every norm-twisted common test function is handled in the same integral:
\(\widehat{(x^{it_0}W)}(s)=\widehat W(s+it_0)\). Taking a fixed
number of integrations by parts shows that its cost is a fixed
polynomial in \(1+|t_0|\). The angular parameter is fixed throughout
(12)--(19), so no angular cutoff changes with the summation variables.

## 6. A coherent short-divisor Type-I consequence

Theorem (5) also gives an actual bound for a marked cubic Gauss block.
It does not require the mark to be a positive average. Fix
\(\ell\ne0\), a squarefree primary \(r\), smooth fixed annular
\(W_A,W_B\), and any coefficients \(b_v\) with \(|b_v|\le1\).
For \(A,B\ge1\), define

\[
 T=\sum_{u,v} b_v\widetilde g(uv)\alpha(uv)^\ell
       \overline{(uv/r)_3}W_A(Nu/A)W_B(Nv/B).
 \tag{21}
\]

Then

\[
 \boxed{|T|\ll_{\ell,W_A,W_B,\varepsilon}
    (ABR)^\varepsilon A^{p_\beta}B^{1+q_\beta}R^{q_\beta}.}
 \tag{22}
\]

Indeed only squarefree \(v\) coprime to \(r\) can contribute. For
each such \(v\), (1) makes the inner sum a uniformly bounded scalar
times
\[
 \sum_u\widetilde g(urv)\alpha(u)^\ell W_A(Nu/A).
\]
For clarity the scalar is
\(b_vW_B(Nv/B)\alpha(v)^\ell\overline{(v/r)_3}
  \widetilde g(v)/\widetilde g(rv)\).
Theorem (5) at the squarefree level \(rv\) gives
\(A^{p_\beta+\varepsilon}(R Nv)^{q_\beta+\varepsilon}\).
Summing these absolute errors over \(v\) proves (22).
The possible primes shared by \(u,v,r\) have not been dropped:
the Gauss and cubic-symbol zeros implement them exactly in this
calculation. Complex conjugation supplies the conjugate Gauss version.

One may take \(b_v=\mu_E(v)\) times any bounded fixed coefficient.
Unfolding \(uv=n\) then gives a coherent short Möbius-divisor mark
on the cubic Gauss coefficient. This is a concrete estimate for one
of the structured blocks that occurs after transforming the mixed
inverse/plain expression. It does not extend (22) to a remaining
quadratic twist, an arbitrary sixth-order row, or an operator norm
without separately proving the corresponding transformation and
averaging bounds.

For a total scale \(Y=AB\), the right side of (22), with \(R\) fixed,
is

\[
 Y^{p_\beta+\varepsilon}
 B^{(5-2\beta)/4+\varepsilon}.
 \tag{23}
\]

Hence it is a power saving over \(Y\) when
\(B\le Y^{2/3-\eta}\), and is \(o(Y^{5/6})\) with a fixed power
margin when

\[
 B\le Y^{\vartheta_\beta-\eta},\qquad
 \vartheta_\beta=\frac{4(2-\beta)}{3(5-2\beta)},\quad\eta>0.
 \tag{24}
\]

At \(\beta=11/12\), \(\vartheta_\beta=26/57\); at
\(\beta=7/8\), it is \(6/13\). As throughout, these substitutions
require the corresponding accepted angular input (3). In particular
(5), (22), and (24) do not on their own improve the numerical Hecke
zero-free boundary or complete the mixed \(U^{6/5+\varepsilon}\) mean.
