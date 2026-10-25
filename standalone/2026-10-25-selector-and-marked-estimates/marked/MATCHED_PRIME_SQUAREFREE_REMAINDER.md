# The exact prime–squarefree discrepancy and complete principal matching

Status: complete arithmetic and analytic component proofs; no improved
zero-free half-plane is claimed.

Scope: ordinary zeta, one fixed nonzero smooth profile \(W\) compactly
supported in \((1,2)\). The profile may be nonnegative. No family moment
or shifted-prime cancellation theorem is assumed in Sections 1–4.

Source: the marked-count construction in PR #1021, mathematical commit
742e952be4ef7843de86ea12678c0bdd3d3579c3, specifically
POSITIVE_MARKED_COUNT_TARGET.md, SHA-256
18e58007abfa604c3e884e60b4721e6b15c86e63335e23c147dcff13364540af.
The principal term below uses exactly its branch and circle conventions.

What was actually run: the companion finite coefficient checker verifies
the prime-power convolution identities. It does not prove the analytic
estimates below.

Smallest remaining gap: a fixed-power improvement for the signed
discrepancy \(\Delta_W(X)\) in (6). Main-term matching is no longer an
unproved step.

## 1. Exact elimination of the squarefree puncture

Put
\[
 S_W(Y)=\sum_{m\ge1}\mu^2(m)W(m/Y),\qquad
 c_W=\widehat W(1)/\zeta(2),\qquad E_W(Y)=S_W(Y)-c_WY.
\]
These definitions apply to every \(Y>0\); in particular \(S_W(Y)=0\)
for \(Y\le1/2\). The elementary square-divisor expansion gives
\[
 E_W(Y)=O_W(Y^{1/2}),\qquad
 E_W'(Y)=O_W(Y^{-1/2})\quad(Y\ge1/2).                 \tag{1}
\]
For the derivative, differentiate the finite smooth sum and apply the
same squarefree estimate to \(-xW'(x)\). Its integral equals
\(\int W\), by integration by parts. On \(0<Y<1/2\),
\(E_W(Y)=-c_WY\) exactly.

Define prime-power coefficients
\[
 \kappa(p^j)=1/j,\qquad
 h(p^j)=(-1)^{j-1}-1/j\quad(j\ge2);
\]
they are zero elsewhere, and \(h(p)=0\).
Then, as exact Dirichlet-convolution identities,
\[
 \mu^2\omega=\mu^2*(\kappa+h).                       \tag{2}
\]
Indeed \((\kappa+h)(p^j)=(-1)^{j-1}\), and the local
generating functions are
\[
 (1+q)\frac{q}{1+q}=q.
\]
Differentiating the full squarefree Euler product with respect to its
prime-factor parameter gives (2), including the contribution at each
distinct prime. This is the exact removal of the condition \(p\nmid m\)
in the first-pass prime/squarefree decomposition; all higher prime powers
are retained.

The correction series
\[
 h_1(s)=\sum_{p,j\ge2}
       \left((-1)^{j-1}-\frac1j\right)p^{-js}          \tag{3}
\]
is absolutely convergent for \(\Re s>1/2\), and is exactly the function
called \(h_1\) in PR #1021. Equation (2) therefore gives
\[
 A_\omega(X)=
 \sum_{p,j\ge1}\frac1j S_W(X/p^j)
 +c_WXh_1(1)+R_h(X),\qquad
 R_h(X)=O_W\!\left(\sqrt X\log\log(3X)\right).         \tag{4}
\]

To prove the remainder bound, apply (1) to the nonempty prime-power
scales. The \(j=2\) errors cost
\(\sqrt X\sum_{p\le\sqrt{2X}}p^{-1}\ll\sqrt X\log\log(3X)\);
the \(j\ge3\) errors cost \(O(\sqrt X)\). The standard Chebyshev upper
bound for prime counting suffices for the reciprocal-prime estimate.
Completing the absolutely convergent correction main term costs
\[
 X\sum_{\substack{p,j\ge2\\p^j>2X}}p^{-j}\ll\sqrt X.
\]
For this last assertion, the number of prime powers with exponent at
least two up to \(t\) is \(O(\sqrt t)\), even by the integer upper bound,
and partial summation completes the proof.

## 2. A continuous prime-power model with no unknown zero data

Let
\[
 J(u)=\sum_{p^j\le u}\frac1j,\qquad
 J_0(u)=\int_1^u a(v)\,dv,\qquad
 a(v)=\frac{1-v^{-1}}{\log v}\quad(v>1),              \tag{5}
\]
with the removable value \(a(1)=1\), and set \(R=J-J_0\).
Both functions vanish below one. Define the finite signed discrepancy
\[
 \boxed{\displaystyle
 \Delta_W(X)=\int_{1^-}^{\infty}S_W(X/u)\,dR(u).}    \tag{6}
\]
Only \(u<2X\) can contribute. Explicitly it is the difference between
the actual prime-power convolution and the entirely specified continuous
model
\[
 T_0(X)=\int_1^\infty S_W(X/u)a(u)\,du.              \tag{7}
\]
There is no implicit asymptotic main term in these definitions.

For \(\Re s>1\), Frullani's integral gives
\[
 \int_1^\infty a(u)u^{-s}\,du
 =\int_0^\infty
      \frac{e^{-(s-1)v}-e^{-sv}}v\,dv
 =\log\frac{s}{s-1}.                               \tag{8}
\]
Consequently the Mellin transform of (7) is exactly
\[
 \widehat W(s)\frac{\zeta(s)}{\zeta(2s)}
                   \log\frac{s}{s-1}.              \tag{9}
\]
The logarithm is initially the real branch on \(s>1\), and continues
in the half-plane \(\Re s>0\) cut along \((0,1]\).

## 3. Exact principal matching, including the cutoff contribution

Fix \(1/2<b<1\), and let \(C_{\omega,b}(X)\) be the exact principal term
of PR #1021 with circle radius \(1-b\). Write
\[
 F_1(s)=\frac{\zeta(s)}{\zeta(2s)},\qquad
 C_b^{(0)}(X)=C_{\omega,b}(X)-c_WXh_1(1).           \tag{10}
\]

**Theorem 1.** For every fixed \(c\) with \(1/2<c<b\),
\[
 \boxed{\begin{aligned}
 A_\omega(X)-C_{\omega,b}(X)
  ={}&\Delta_W(X)
     +\int_c^b F_1(v)\widehat W(v)X^v\,dv\\
    &+V_{c,W}(X)+R_h(X),\\
 V_{c,W}(X)={}&O_{c,W}(X^c).
 \end{aligned}}                                                   \tag{11}
\]
In particular
\[
 A_\omega(X)-C_{\omega,b}(X)
 =\Delta_W(X)+O_{b,c,W}\!\left(
      \frac{X^b}{\log(2X)}+X^c\right).             \tag{12}
\]
All the terms except \(\Delta_W\) on the right of (11) are explicitly
known or already bounded below the requested \(X^{b+\varepsilon}\) scale.

**Proof.** On the elementary zero-free disk around one, let
\(G(s)=(s-1)\zeta(s)\), with \(\log G(1)=0\).
The difference
\[
 \log\zeta(s)-\log\frac{s}{s-1}
       =\log G(s)-\log s
\]
is holomorphic there and vanishes at one. Multiplication by \(F_1(s)\)
therefore leaves a holomorphic function. Its circle integral, including
the factors \(\widehat W(s)X^s\), is zero. The analytic correction
\(F_1h_1\) contributes exactly its simple-pole residue
\(c_WXh_1(1)\). Thus \(C_b^{(0)}\) is precisely the circle principal
term of (9), not merely its first few asymptotic coefficients.

Move the Mellin line for (9) from \(\Re s>1\) to the two halves of
\(\Re s=c\), detouring counterclockwise around the branch point at one.
The detour is \(C_c^{(0)}(X)\), while the remaining two vertical
half-lines define \(V_{c,W}(X)\).
This contour argument assumes no high zero-free region: \(F_1\) is
meromorphic for \(\Re s>1/2\), with only its pole at one, and the
logarithm in (9) has only the specified real cut.
Euler summation bounds \(\zeta(c+it)\) polynomially, while
\(1/\zeta(2c+2it)\) is bounded by its absolutely convergent Dirichlet
series. The Mellin transform of \(W\) decays faster than any power.
The vertical integrals are therefore absolutely convergent and
\(O(X^c)\); horizontal segments tend to zero.

The lower-minus-upper jump of \(\log(s/(s-1))\) on \((c,b)\) is
\(2\pi i\). With the orientation just specified,
\[
 C_c^{(0)}(X)-C_b^{(0)}(X)
       =\int_c^bF_1(v)\widehat W(v)X^v\,dv.          \tag{13}
\]
This sign also follows by differentiating the real-integral formula in
PR #1021 with respect to its radius. Hence
\(T_0=C_b^{(0)}+\int_c^bF_1\widehat WX^v\,dv+V_{c,W}\).
Combine this identity with (4), (6), and (7) to obtain (11).
The real integrand coefficient is bounded on \([c,b]\), so its integral
is \(O(X^b/\log(2X))\). The correction \(R_h\) is \(O(X^c)\)
because \(c>1/2\). This proves (12). \(\square\)

For nonnegative nonzero \(W\), \(F_1(b)\widehat W(b)<0\), and the
cutoff contribution has the more precise endpoint expansion
\[
 \int_c^bF_1(v)\widehat W(v)X^v\,dv
 =\frac{F_1(b)\widehat W(b)X^b}{\log X}
  +O\!\left(\frac{X^b}{(\log X)^2}+X^c\right).       \tag{14}
\]
This is a known cutoff effect. Fitting the first-pass remainder directly
at exponent \(b\) can be dominated by (14), even when the genuinely
arithmetic discrepancy is much smaller. The model (7) removes that
interpretive ambiguity.

## 4. The old hyperbola exponent loss can be removed

Here is a real-variable baseline recovery theorem. It is conditional only
on a stated bound for \(R\), not on separate estimates in the two
hyperbola rectangles.

**Theorem 2.** Suppose, for some \(1/2<\beta<1\),
\[
 |R(u)|\le C_Ru^\beta\qquad(u\ge1).                \tag{15}
\]
Then
\[
 \Delta_W(X)=O_{\beta,W,C_R}(X^\beta).              \tag{16}
\]
The same conclusion, with arbitrarily small exponent losses, holds if
(15) is known with those losses.

**Proof.** Under (15), the Stieltjes integral
\(\int_1^\infty u^{-1}dR(u)\) converges. For \(\Re s>1\),
\[
 \int_1^\infty u^{-s}\,dR(u)
 =\log\zeta(s)-\log\frac{s}{s-1}
 =\log\frac{G(s)}s .
\]
Integration by parts using (15) continues the left side through \(s=1\).
The right side has value zero there. Thus the exact reciprocal moment is
\[
                    \int_1^\infty u^{-1}\,dR(u)=0. \tag{17}
\]
Consequently (6) can be written, with convergent infinite integrals,
\[
 \boxed{\displaystyle
 \Delta_W(X)=\int_1^\infty E_W(X/u)\,dR(u).}         \tag{18}
\]

Integrate (18) by parts. The boundary at one is zero, since \(R(1)=0\);
the boundary at infinity vanishes by \(E_W(X/u)=-c_WX/u\) there
and \(\beta<1\). On \(1\le u\le2X\), (1) gives
\[
 \left|\frac{d}{du}E_W(X/u)\right|
       \ll_W X^{1/2}u^{-3/2}.
\]
Therefore this range contributes at most
\[
 X^{1/2}\int_1^{2X}u^{\beta-3/2}\,du\ll X^\beta,
\]
because \(\beta>1/2\). On \(u>2X\), the exact derivative has size
\(|c_W|X/u^2\), whose contribution is also \(O(X^\beta)\).
This proves (16). \(\square\)

The first-pass separate-bound exponent \((1+\beta)/2\) is thus not
intrinsic. The exact zero reciprocal moment removes it. For a
source-qualified zero-free half-plane \(\Re s>\beta\), the corresponding
standard prime-power error with small losses recovers the same
marked-count exponent \(\beta+\varepsilon\), without the artificial
hyperbola loss. It does not improve \(\beta\).

The hard range in (18) is \(u\asymp X\): the squarefree kernel then has
bounded-scale argument and does not itself supply a long oscillatory
average. A new power improvement must exploit cancellation of this
signed prime-error convolution, rather than only insert a sharper
absolute estimate in (1).

## 5. Why the zero cancellation saves logarithms, not a power

The Mellin germ of \(\Delta_W\) is
\[
 \widehat W(s)F_1(s)\log\frac{G(s)}s.                \tag{19}
\]
At a zero \(\rho\) with \(\Re\rho>1/2\), of multiplicity \(m\), write
\(\zeta(s)=(s-\rho)^m g(s)\), \(g(\rho)\ne0\).
Here \(1/\zeta(2\rho)\) is finite and nonzero by the Euler product.
Its nonanalytic local germ is
\[
 \frac{m\,g(s)\widehat W(s)}{\zeta(2s)}
      (s-\rho)^m\log(s-\rho).                     \tag{20}
\]
Thus the factor \(\zeta(\rho)=0\) cancels the leading logarithmic
prime-zero term, but leaves a branch of order \(m\).
If \(\widehat W(\rho)\ne0\), then for a contour localized around an
isolated such branch the leading Hankel contribution has the scale
\[
 (-1)^{m+1}
 \frac{m\,\zeta^{(m)}(\rho)\widehat W(\rho)}
      {\zeta(2\rho)}
 \frac{X^\rho}{(\log X)^{m+1}}.                    \tag{21}
\]
This follows from the elementary inverse-Laplace identity for
\((s-\rho)^m\log(s-\rho)\), or by differentiating the fractional-power
Hankel formula at the integer \(m\).
If the Mellin transform vanishes at \(\rho\), its integer vanishing
order produces further logarithmic suppression; it does not remove
the branch or change its real-part exponent.
Equation (21) describes a localized germ; it is not asserted as a global
zero expansion without the additional contour/separation estimates.
In particular its real-part exponent remains \(\Re\rho\).

Taking a larger fixed integer mark order increases logarithmic
suppression but does not change that exponent. The companion note
GROWING_INTEGER_RESONANCE.md proves an actual arithmetic obstruction to
making the needed integer-order constants uniform as the order grows.

There is also a precise local limitation on shrinking a fractional
parameter toward one. At a zero of multiplicity \(m\), the fractional
germ has Hankel coefficient proportional to \(1/\Gamma(-mz)\).
Writing \(z=1-\eta\), this coefficient satisfies
\[
 \frac1{\Gamma(-m+m\eta)}
       =(-1)^m m!\,m\eta+O_m(\eta^2).              \tag{22}
\]
Thus the zero contribution disappears only linearly in the distance
from the integer endpoint. A subpower-sized distance, such as
\(1/\log\log X\), changes logarithmic or subpower factors, not the
real-part exponent of that localized contribution. A distance
comparable to \(X^{-\delta}\) could supply a fixed power in this
mechanism. But the generic worst-case Chebyshev amplification for
extrapolation from a width-\(\eta\) interval, at degree \(d\), has
logarithm \(\Theta(d\log(1/\eta))\) when the target stays a fixed
distance from that interval. At the squarefree degree scale
\(d\asymp\log X/\log\log X\) and \(\eta=X^{-\delta}\), this is
\(\Theta(\delta(\log X)^2/\log\log X)\). Generic polynomial
extrapolation therefore supplies no subpower guarantee in this window.
This is a worst-case conditioning statement, not a lower bound for
the particular arithmetic family. The argument describes the direct
single-zero mechanism; it does not rule out joint cancellation in a
family mean or establish a global zero expansion.

## 6. Relation to the newly supplied shifted-prime paper

Lü–Wang–Wu, arXiv:2610.20242v1, states cancellation for
\(\sum_{p\le x}\mu(p+2)\), with a fixed additive shift. Its Section 5.3
takes the length limit with a fixed number of auxiliary groups and only
then lets the group count tend to infinity. It does not state a fixed
power saving, nor an estimate for (18).

The marked convolution is multiplicative. For squarefree \(m\) coprime
to \(p\), \(\mu(pm)=-\mu(m)\), so the corresponding product of two
Möbius signs equals \(-\mu^2(m)\) exactly. The parity signs cancel in
this positive marked observable. An additive-shift parity theorem
cannot be substituted for the signed discrepancy estimate without a
new quantitative transference argument.

## 7. Literature and final scope

Kohnen, “A simple note on the number-theoretic function \(\Omega(n)\)
and Dirichlet L-functions,” European Journal of Mathematics 9, 33 (2023),
[primary text](https://link.springer.com/article/10.1007/s40879-023-00629-w),
records prior relations between prime-factor counts, fractional
Dirichlet series, and zero multiplicities. Its introduction cites
Wolke, “Über die zahlentheoretische Funktion \(\omega(n)\),”
Acta Arithmetica 55 (1990), 323–331, for a corresponding full-remainder
RH criterion. This packet makes no novelty claim for that general
monodromy principle.

The new completed component here is the exact model (7), the full
principal matching (11), and the cross-scale reciprocal-moment
cancellation (18). The fixed-power bound for \(\Delta_W\) below the
imported boundary remains open.
