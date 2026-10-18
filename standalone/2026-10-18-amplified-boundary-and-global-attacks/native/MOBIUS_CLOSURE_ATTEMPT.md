# An actual Möbius attack on the remaining rational amplitude

**Status.** Exploratory analytic closure attempt. The identities and elementary
estimates below are proved. This attempt has not proved a stronger global
zero-free boundary or an exponent contraction. It is an accounting of the
specific closure that failed, not a proposed substitute for that result.

**Scope and sources.** The input is the actual Möbius function throughout.
The complete Newton source is [the native proof at commit
c93ca65a510b6acaf167f929b9bf7e67d742b05a](https://github.com/GettysburgResearch/riemann/blob/c93ca65a510b6acaf167f929b9bf7e67d742b05a/standalone/2026-10-18-theta20-and-native-cancellation/native/PROOF.md).
The preceding generic-coefficient obstruction in PR #1003 did not use
`1*mu=delta`; the present calculation does. External comparisons are
[Xu–Sang, v2](https://arxiv.org/html/2610.15291v2),
[de Faveri–Pandey, v1](https://arxiv.org/html/2610.01035v1), and
[Pliego–Wang](https://arxiv.org/abs/2610.11487). Their conclusions retain
their stated source hypotheses. No numerical experiment is used here.

## 1. The complete arithmetic expression

For an integer $Y\ge2$, set

\[
 G_Y(s)=\sum_{n\le Y}\mu(n)n^{-s},\qquad
 m(x)=\sum_{n\le x}\frac{\mu(n)}n,\qquad
 F_Y=\sum_{j\le Y}|m(j)|^2,
\]

and retain every old product in

\[
 Z_Y(x)=\sum_{a,b\le Y}\frac{\mu(a)\mu(b)}{ab}
             R\!\left(\frac{x}{ab}\right),\qquad
 R(u)=H_{\lfloor u\rfloor}-\log u-\gamma.                 \tag{1}
\]

In particular, terms with $ab>x$ remain in (1). On the complete strict
square step $Y+1\le x<(Y+1)^2$, weighted Möbius inversion gives

\[
 m(x)=2m(Y)-\sum_{a,b\le Y}\frac{\mu(a)\mu(b)}{ab}
                           H_{\lfloor x/(ab)\rfloor}
      =A_Y(x)-Z_Y(x),                                    \tag{2}
\]

where

\[
 A_Y(x)=2M_YB_Y+M_Y^2\log(Y^2/x),\quad M_Y=m(Y),\quad
 B_Y=1+\sum_{n\le Y}\frac{\mu(n)\log n}{n}
                     -(\log Y+\gamma/2)M_Y.
\]

Equation (2) is an identity on the physical output interval. In particular,
the two terms may not be estimated on incompatible windows, and neither a
frequency projection nor a quadratic norm distributes over it without its
mixed terms. For general $Y$, the available balance estimate is

\[
 \|A_Y\|_{L^2([Y+1,(Y+1)^2))}
 \le \sqrt6\,Y|M_YB_Y|+\sqrt3\,YM_Y^2.
\]

This follows by the triangle inequality and direct integration of the
logarithm, with no cancellation assumed. A uniform constant is available
only on the literal native crossing set

\[
 \mathcal X=\{Y\ge2:\mu(Y)\ne0,\ m(Y-1)m(Y)\le0\}.
\]

On this set $|M_Y|\le1/Y$, while the all-$Y$ balance identity in Section 5
of the cited source gives $|B_Y|\le1+(\gamma/2)|M_Y|$. Consequently

\[
 \|A_Y\|_{L^2([Y+1,(Y+1)^2))}<4
                  \qquad (Y\in\mathcal X).
\]

The source proves that $\mathcal X$ is unbounded; it supplies no crossing
spacing estimate. No all-$Y$ constant bound for $A_Y$ is asserted.
Our subsequent phase manipulation concerns the complete $Z_Y$; it does
not replace that crossing estimate or enlarge the strict endpoint.

## 2. Exact conversion to reciprocal phases

Put $\psi(u)=1/2-\{u\}$, using the value $1/2$ at an integer, and define

\[
 S_Y(t)=\sum_{a,b\le Y}\mu(a)\mu(b)\psi(t/(ab)).
\]

For every $u>0$,

\[
 R(u)=\frac{\psi(u)}u-\int_u^\infty\frac{\psi(v)}{v^2}\,dv. \tag{3}
\]

One direct proof differentiates between consecutive integers. Both sides
have derivative $-1/u$, both have jump $1/n$ at an integer $n$, and
both tend to zero at infinity. This also proves (3) on $0<u<1$, where
the left side is $-\log u-\gamma$. Thus no condition $ab\le x$ is needed.

Substitution $t=abv$ in the finite sum (1) gives the exact formula

\[
 \boxed{Z_Y(x)=\frac{S_Y(x)}x-
                         \int_x^\infty\frac{S_Y(t)}{t^2}\,dt.} \tag{4}
\]

The integral is absolutely convergent because the sum defining $S_Y$ is
finite and $\psi$ is bounded. All products, their signs, and the integral
tail are present. In particular, (4) does not license discarding its second
term before taking the norm.

Away from integer arguments, the usual symmetric Fourier expansion is

\[
 \psi(u)=\lim_{H\to\infty}\sum_{0<|h|\le H}
                          \frac{e(hu)}{2\pi i h}.
\]

At integers it converges to zero instead of the chosen right value. The
countable exceptional set of $t$'s does not affect a Lebesgue energy norm.
Any use of this expansion inside an integral still needs a convergence or
truncation argument; no infinite termwise energy estimate is asserted here.

## 3. What the existing Möbius bound buys in the critical box

Assume an imported Mertens estimate

\[
 \sum_{n\le T}\mu(n)\ll_\varepsilon T^{B+\varepsilon}.    \tag{5}
\]

Let $w\in C_c^2((c,C)^2)$ for fixed $0<c<C<\infty$, and let

\[
 T_{Y,h}(\lambda)=\sum_{a,b\ge1}\mu(a)\mu(b)
       w(a/Y,b/Y)e\!\left(\frac{h\lambda Y^2}{ab}\right).
\]

For $\lambda$ in any fixed compact subset of $(0,\infty)$, two
applications of partial summation to (5) prove

\[
 |T_{Y,h}(\lambda)|\ll_{w,\varepsilon}
                      (1+|h|)^2Y^{2B+\varepsilon}.       \tag{6}
\]

Indeed the partial sums in each variable are $O(Y^{B+\varepsilon})$,
and, after rescaling by $Y$, the relevant mixed derivative and boundary
variation norms of the smooth phase are $O_w((1+|h|)^2)$. Compact support
removes the endpoint boundary terms; the same conclusion holds for a fixed
finite collection of smooth boxes. This estimate uses the actual signed
Möbius sums, rather than the coefficient norm bound.

For fixed $h\ne0$, the phase on $a,b\asymp Y$, $t\asymp Y^2$ varies
by only a bounded amount. The natural $1/x$ factor in (4) then changes
(6) into the amplitude scale $Y^{2B-2+\varepsilon}$, whose squared
integral over an interval of length comparable to $Y^2$ has scale

\[
                         Y^{4B-2+\varepsilon}.          \tag{7}
\]

This is the same exponent as the existing bound for $F_{Y^2}$. Equation
(7) is the exponent delivered by this specific box estimate, not a lower
bound for the box or an upper bound for the complete expression (4).
Uncontrolled cancellation between boxes, harmonics, and the integral tail
cannot be assumed to improve it.

Using Xu–Sang's reported source-qualified boundary $B=0.8748867$, the
old energy exponent is $\kappa=2B-1=0.7497734$. The suggested target

\[
 F_{Y^2}\ll_\varepsilon Y^{1/3+\varepsilon}(1+F_Y)^{3/2}
\]

would require an additional saving of

\[
 2\kappa-(1/3+3\kappa/2)
       =0.0415533666\ldots
\]

in the exponent of $Y$ in the complete energy. Neither (6) nor the
transform identity supplies this positive power. This is the precise
unpaid amount in the attempted closure.

## 4. Why the recent phase bounds do not pay this amount

For fixed $b\asymp Y$ and $t\asymp Y^2$, the one-variable reciprocal
phase is $h t/(ab)=\alpha/a$, with $\alpha\asymp hY$. A formal
Poisson stationary point against a dual integer $v$ satisfies

\[
 |v|\asymp\alpha/Y^2\asymp |h|/Y.
\]

Consequently, in the critical box and for fixed low harmonics, there is no
nonzero stationary dual frequency once $Y$ is large. The square-root
phase $2\sqrt{\alpha|v|}$ appears only when harmonics have reached size
comparable to $Y$. Moreover direct Poisson summation with a smooth
amplitude does not apply to the coefficient $\mu(a)$; an arithmetic
decomposition would first have to justify the transformation and its
coefficient class.

Corollary 1.4 of de Faveri–Pandey concerns bounded coefficients and phases
$w(\sqrt{n/N}+\eta(n/N)^{3/2})$ in the range
$N\le W\le N^{4/3}$. It therefore does not directly estimate this
low-harmonic sector. An adapter covering only the high harmonics would
leave exactly the slowly varying sector estimated in (6).

The abstract of Pliego–Wang gives a uniform Möbius short-interval estimate
$H(\log x)^{-1/3+\varepsilon}$ for $H\ge x^{0.58+\varepsilon}$.
That logarithmic saving does not improve the fixed power $Y^B$ in (5)
for the long, slowly varying sums in (6). Splitting a length-$Y$ sum into
the allowed short intervals and summing those estimates costs
$Y(\log Y)^{-1/3+\varepsilon}$, which is larger than $Y^B$ for fixed
$B<1$. This observation concerns the stated estimate; it is not an
optimality assertion about their method.

## 5. The full convolution inverse does not itself erase a zero mode

The exact arithmetic restriction missing from the generic test in PR
#1003 is now retained. On $\Re s>1$,

\[
 A(s):=\int_1^\infty m(x)x^{-s}\,dx
       =\frac{1}{(s-1)\zeta(s)},\qquad
 H(s):=(s-1)\zeta(s),\qquad H(s)A(s)=1.                \tag{8}
\]

Hence the correlated quadratic expression obeys the exact meromorphic
identity

\[
                              H(s)A(s)^2=A(s).         \tag{9}
\]

For example, at a hypothetical simple zero $\rho$ of $\zeta$,

\[
 A(s)=\frac{c_\rho}{s-\rho}+O(1),\qquad
 c_\rho=\frac{1}{(\rho-1)\zeta'(\rho)}.
\]

Multiplication by $H$ removes one order from the double pole of
$A^2$, and leaves residue
$H'(\rho)c_\rho^2=c_\rho$. More generally, a zero of order $j$
leaves a pole of order $j$ in both sides of (9). Thus this exact
numerator–denominator correlation removes a spurious pole multiplicity;
it does not move the singularity to a smaller real part.

This is an identity of the full meromorphic functions. It is not an
asserted asymptotic formula for a finitely truncated source. To make the
finite support issue explicit, set $E_Y=1/\zeta-G_Y$ on $\Re s>1$.
Then

\[
 \zeta G_Y^2=2G_Y-1/\zeta+\zeta E_Y^2.                \tag{10}
\]

The Dirichlet series of the last term begins at $(Y+1)^2$. This proves
the strict square-step inverse identity, but the meromorphic cancellation
in (10) includes that entire tail. One cannot use the vanishing of the
finite numerator at a zero of $\zeta$ while deleting the tail that
restores the identity.

Equations (8)–(10) do not rule out a stronger estimate for the actual
Möbius coefficients. They show exactly why invoking the full convolution
inverse, after the earlier generic obstruction, is still insufficient
to justify the proposed contraction. A new arithmetic estimate must pay
the positive power identified in Section 3 for the complete retained
amplitude. This attempt did not obtain it.

## 6. Recombine globally before using the crossing

To check whether the small value of $m(Y)$ cancels the entire slowly
varying part after all boxes are recombined, define the finite transform

\[
 A_Y^{\mathrm{old}}(s)=\int_1^Y m(x)x^{-s}\,dx.
\]

Exact partial summation, with the unit coefficient included, gives

\[
 G_Y(s)=Y^{1-s}M_Y+(s-1)A_Y^{\mathrm{old}}(s).          \tag{11}
\]

This identity uses the whole prefix. No dyadic box has been removed.
At $s=1/2+it$, let

\[
 \Phi_Y(t)=\frac{\zeta(s)G_Y(s)^2}{s-1},
 \qquad H(s)=(s-1)\zeta(s).
\]

Substitution gives exactly

\[
 \begin{split}
 \Phi_Y(t)={}&H(s)A_Y^{\mathrm{old}}(s)^2\\
 &+2\zeta(s)Y^{1-s}M_YA_Y^{\mathrm{old}}(s)
   +\frac{\zeta(s)}{s-1}Y^{2-2s}M_Y^2.               \tag{12}
 \end{split}
\]

Thus the crossing condition applies to the last two complete boundary
terms. It does not multiply the interior quadratic term by $M_Y$.

This distinction has an actual norm estimate. By Plancherel,

\[
 \frac1{2\pi}\int_{\mathbb R}
       |A_Y^{\mathrm{old}}(1/2+it)|^2\,dt=F_{Y-1}\le F_Y.
\]

Using $|M_Y|\le1/Y$ on $\mathcal X$ and the critical-line bound
$|\zeta(1/2+it)|\ll_\varepsilon(1+|t|)^{13/84+\varepsilon}$
from [Bourgain, arXiv:1408.5794v2, Theorem 5](https://arxiv.org/pdf/1408.5794v2),
the two boundary terms in (12) satisfy, for $T\ge2$,

\[
 \frac1{2\pi}\int_{-T}^T
       |\Phi_Y(t)-H(s)A_Y^{\mathrm{old}}(s)^2|^2\,dt
 \ll_\varepsilon
          Y^{-1}T^{13/42+\varepsilon}F_Y+Y^{-2},
          \qquad Y\in\mathcal X.                    \tag{13}
\]

For the first term, take the supremum of $|\zeta|^2$ and apply the
displayed Plancherel identity. For the second, use
$\int_{\mathbb R}|\zeta(1/2+it)/(-1/2+it)|^2dt<\infty$;
this follows either from the same critical-line estimate or from the
complete $R$-kernel transform. Apply the squared triangle inequality to
the two terms. This proves (13) without deleting their mutual cross term.

At the already proved cutoff $T=Y^{84/71}$, (13) is

\[
 \ll_\varepsilon Y^{-45/71+\varepsilon}F_Y+Y^{-2}.
                                                               \tag{14}
\]

Multiplication by the literal physical window
$W_Y=1_{[\log(Y+1),\,2\log(Y+1))}$ contracts the $L^2$ norm.
Combining (14), the crossing-only balance estimate in Section 1, and
the complete high-frequency bound in
[PR #1003](https://github.com/GettysburgResearch/riemann/blob/669b6a01f4d4858ae1ef806b07547be95c08c935/standalone/2026-10-18-theta26-and-critical-family/arithmetic/NATIVE_FREQUENCY_TAIL.md)
therefore gives

\[
 \begin{split}
 \Bigl|\,\sqrt{F_{(Y+1)^2-1}-F_Y}
   -\bigl\|W_Y\mathcal F^{-1}
       [1_{[-T,T]}H(s)A_Y^{\mathrm{old}}(s)^2]\bigr\|_2
       \Bigr|
 \ll_\varepsilon
       Y^\varepsilon(1+Y^{-45/142}F_Y^{1/2}),
 \quad Y\in\mathcal X,\quad T=Y^{84/71}.              \tag{15}
 \end{split}
\]

The window is applied after the frequency projection. All comparisons
are in root norm, so (15) does not discard the large mixed terms in an
energy expansion. Its squared error is payable by the existing $F_Y$
term of a square-step recurrence.

What remains after this global crossing recombination is the interior
quadratic expression in (12), with the actual Möbius partial sum inside
$A_Y^{\mathrm{old}}$. For example, on a fixed frequency band the direct
Cauchy–Schwarz estimate is still only

\[
 \int_{-T}^T |H(s)A_Y^{\mathrm{old}}(s)^2|^2dt
                    \ll_T (1+\log Y)F_Y^2,
\]

because $|A_Y^{\mathrm{old}}(s)|^2\le(\log Y)F_Y$ and its total
squared norm is $2\pi F_{Y-1}$. The crossing condition has paid the
boundary terms in the complete expression, but has supplied no
subquadratic power for this remaining interior norm. That is the
unobtained signed estimate; the attempt stops here.
