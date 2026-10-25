# An actual arithmetic obstruction to growing integer coefficient interpolation

Status: complete analytic component argument, subject to independent review.
No improved zero-free region is claimed.

Scope: the ordinary scalar squarefree count with a positive integer
prime-factor parameter. This is not asserted for the varying sextic
character family or for a differently normalized family moment.

Sources and dependencies: the classical prime number theorem, Euler
products in their half-plane of absolute convergence, elementary
analytic continuation, and the beta-integral identity used explicitly
below. The first-pass coefficient-continuation note in PR #1021 supplies
the motivation, but its synthetic polynomial counterexample is not used
in the proof here.

Smallest remaining gap for the research programme: the fixed-parameter
fractional mean remains open. This note excludes a particular attempt
to replace it by uniform control of a growing list of positive integer
orders.

## 1. Integer orders are individually regular

For an integer \(K\ge1\), define
\[
 F_K(s)=\sum_{n\ge1}\frac{\mu^2(n)K^{\omega(n)}}{n^s}
       =\prod_p(1+Kp^{-s})=\zeta(s)^K H_K(s)
       \quad(\Re s>1),                              \tag{1}
\]
where
\[
 H_K(s)=\prod_p(1+Kp^{-s})(1-p^{-s})^K .
\]
For fixed \(K\), cancellation of the linear prime terms makes \(H_K\)
holomorphic for \(\Re s>1/2\). Thus \(F_K\) is meromorphic in that
half-plane, with only a pole at one. Zeta zeros cause no branches at an
integer parameter.

Fix a nonnegative nonzero \(W\in C_c^\infty((1,2))\), and put
\[
 A_K(X)=\sum_n\mu^2(n)K^{\omega(n)}W(n/X),\qquad
 C_K(X)=\operatorname{Res}_{s=1}
           \bigl(\widehat W(s)F_K(s)X^s\bigr).        \tag{2}
\]
The latter is \(X\) times a polynomial in \(\log X\) of degree \(K-1\).
It is exactly the integer specialization of the circle principal term
in PR #1021; the radius of that circle is immaterial here.
For each fixed \(K\), ordinary contour shifting yields
\[
 A_K(X)-C_K(X)=O_{K,W,\varepsilon}(X^{1/2+\varepsilon}). \tag{3}
\]
The dependence on \(K\) is the decisive issue. It cannot be suppressed.

## 2. A near-real resonance of the continued Euler product

**Theorem 1.** Fix \(1/2<\sigma<1\), and set
\[
 R=K^{1/\sigma},\qquad
 t_K=\frac{\pi\sigma}{\log R}
     =\frac{\pi\sigma^2}{\log K},\qquad
 C_\sigma=-\frac{\pi}{\sin(\pi/\sigma)}>0.
\]
Then, as positive integers \(K\to\infty\),
\[
 \boxed{\displaystyle
 \log|F_K(\sigma+it_K)|
       =(C_\sigma+o_\sigma(1))\frac{R}{\log R}.}      \tag{4}
\]
This is actual growth of the analytically continued arithmetic Euler
product, not merely a large upper bound for its absolute majorant.

### Proof

Write \(s_K=\sigma+it_K\), \(w=e^{-i\pi\sigma}\), and
\[
 f_K(y)=\Re\left[
   \log\bigl(1+w y^{-\sigma}e^{-it_K\log y}\bigr)
       -w y^{-\sigma}e^{-it_K\log y}\right].
\]
On compact subsets of \(y>0\), the logarithm can be chosen continuously
for sufficiently large \(K\), and its real part is simply the logarithm
of the modulus. Since \(-\pi<-\pi\sigma<-\pi/2\), the limiting argument
does not lie on the negative real axis. Thus
\[
 f_K(y)\longrightarrow
 f(y)=\Re[\log(1+w y^{-\sigma})-w y^{-\sigma}]
\]
locally uniformly.

Expanding only the second Euler factor in \(H_K\), the absolutely
convergent quadratic remainder gives
\[
 \log|H_K(s_K)|=\sum_p f_K(p/R)+O_\sigma(K).          \tag{5}
\]
Indeed \(Kp^{-s_K}=w(p/R)^{-\sigma}
e^{-it_K\log(p/R)}\), while
\(K\log(1-p^{-s_K})=-Kp^{-s_K}+O_\sigma(Kp^{-2\sigma})\).

The prime number theorem, first on any fixed interval
\(\delta\le p/R\le M\), gives
\[
 \sum_p f_K(p/R)
       =\frac{R}{\log R}
          \left(\int_0^\infty f(y)\,dy+o_\sigma(1)\right). \tag{6}
\]
Here are the tail controls needed for this passage.
For \(y\le\delta\), with \(\delta\) sufficiently small,
the modulus of the inner Euler argument is large, so
\(|f_K(y)|\ll_\sigma y^{-\sigma}\); its prime sum, normalized by
\(R/\log R\), is \(O_\sigma(\delta^{1-\sigma})\).
For \(y\ge M\), the argument is small and the linear subtraction gives
\(|f_K(y)|\ll_\sigma y^{-2\sigma}\); the corresponding normalized tail
is \(O_\sigma(M^{1-2\sigma})\).
Both bounds follow by partial summation from the prime number theorem
or its Chebyshev upper bound. The transition region is bounded away
from a zero of the local Euler factor, so its uniform convergence causes
no logarithmic singularity. Let \(\delta\downarrow0\), \(M\uparrow\infty\).

It remains to evaluate the integral. For \(1<\alpha=1/\sigma<2\) and
\(z\) off the nonpositive real axis, absolute convergence and analytic
continuation give
\[
 \int_0^\infty
       [\log(1+z y^{-\sigma})-z y^{-\sigma}]\,dy
       =\frac{\pi z^\alpha}{\sin(\pi\alpha)}.         \tag{7}
\]
For completeness, differentiate with respect to positive real \(z\),
put \(u=y^\sigma\), and use the beta integral:
\[
 \frac{d}{dz}\text{(left side)}
 =-\alpha z\int_0^\infty\frac{u^{\alpha-2}}{u+z}\,du
 =\frac{\alpha\pi z^{\alpha-1}}{\sin(\pi\alpha)}.
\]
The integration constant is zero by scaling as \(z\downarrow0\).
Both sides are holomorphic on the slit \(z\)-plane, which proves (7)
there as well.

For \(z=w=e^{-i\pi\sigma}\), the principal power is
\(w^\alpha=e^{-i\pi}=-1\). Thus the real part in (7) equals
\(-\pi/\sin(\pi/\sigma)=C_\sigma>0\).
Equations (5) and (6) establish the asserted asymptotic for \(H_K\).
Finally \(\zeta(\sigma)\ne0\), and \(t_K\to0\), so
\(K\log|\zeta(s_K)|=O_\sigma(K)=o(R/\log R)\).
This proves (4). \(\square\)

The elementary nonvanishing used in the last step is only on the real
interval \((1/2,1)\). It follows, for example, from the elementary
zero-free disk around one proved in PR #1021. No assertion about high
zeros enters this argument.

## 3. Subtracting the pole does not remove the resonance

Let \(P_K(s)\) be the principal part at one of
\(\widehat W(s)F_K(s)\). For fixed \(\sigma\) as above,
\[
 |P_K(\sigma+it_K)|\le
                 \exp(O_{\sigma,W}(K\log K)).       \tag{8}
\]
This is negligible compared with (4).

To verify (8), use a circle of radius \(r_K=1/\log K\) around one,
for \(K\) sufficiently large. On it \(|\zeta(s)|\ll\log K\).
Let \(\sigma_0=1-r_K\) and split the Euler factors at
\(P=(2K)^{1/\sigma_0}\).
For \(p\le P\), elementary absolute estimates give a total logarithmic
cost
\[
 O\!\left(K\sum_{n\le P}n^{-\sigma_0}\right)
       =O(K\log K).
\]
For \(p>P\), the linear terms cancel, giving cost
\[
 O\!\left(K^2\sum_{n>P}n^{-2\sigma_0}\right)=O(K).
\]
Consequently
\[
 \sup_{|s-1|=r_K}
       |\widehat W(s)F_K(s)|
       \le\exp(O_W(K\log K)).                       \tag{9}
\]
The Cauchy integral defining the principal part has kernel \(1/(s-w)\);
its denominator stays bounded away from zero at \(s=\sigma+it_K\).
This proves (8).

Since \(\widehat W(\sigma+it_K)\to\widehat W(\sigma)>0\), (4) and (8)
also prove
\[
 \log\left|\widehat W(s_K)F_K(s_K)-P_K(s_K)\right|
       =(C_\sigma+o(1))\,R/\log R.                 \tag{10}
\]
The pole-subtracted transform therefore retains the same large growth.

## 4. A uniform growing-order power error is actually false

**Theorem 2.** Fix any \(b<1\). There do not exist constants \(C,X_0\)
such that
\[
 |A_K(X)-C_K(X)|\le C X^b                          \tag{11}
\]
for all \(X\ge X_0\) and all positive integers
\[
                   K\le\frac{\log X}{\log\log X}.   \tag{12}
\]
Consequently a version with \(X^{b+\varepsilon}\) for every
\(\varepsilon>0\), with constants independent of \(K\) on (12), is
also false whenever \(b<1\).

### Proof

Choose \(\sigma\) with \(\max(1/2,b)<\sigma<1\), and let
\[
                         X_K=\exp(4K\log K).
\]
For all sufficiently large \(K\), condition (12) holds whenever
\(X\ge X_K\). Under the alleged estimate (11),
\[
 \left|\int_{X_K}^{\infty}
     (A_K(X)-C_K(X))X^{-s_K}\frac{dX}{X}\right|
       \le \frac{C X_K^{b-\sigma}}{\sigma-b}.        \tag{13}
\]

On \(1\le X\le X_K\), a deliberately crude bound suffices. There are
at most \(2X\) terms in \(A_K\), and
\(\omega(n)\le\log n/\log2\). Hence
\[
 |A_K(X)|\le
 \exp(O_W(K(\log K)^2))\qquad(1\le X\le X_K).        \tag{14}
\]
The residue formula for \(C_K(X)\), using the circle in (9), gives
the stronger bound \(\exp(O_W(K\log K))\) on this same range.
Thus the integral from 1 to \(X_K\), with factor \(X^{-s_K}dX/X\),
is at most \(\exp(O_W(K(\log K)^2))\).

Initially for \(\Re s>1\), the exact Mellin identity is
\[
 \widehat W(s)F_K(s)
 =E_{<1}(s)+P_K(s)+
       \int_1^\infty(A_K(X)-C_K(X))X^{-s}\frac{dX}{X}, \tag{15}
\]
where \(E_{<1}\) comes only from the unit integer and is independent
of \(K\). Under (11), the last integral continues holomorphically
to \(\Re s>b\). The finite lower interval causes no restriction.
Hence (15) holds at \(s=s_K\).

Equations (13)–(15) bound its pole-subtracted right side by
\(\exp(O_W(K(\log K)^2))\). But (10) has logarithm asymptotic to
a positive constant times \(K^{1/\sigma}/\log K\), and
\[
 \frac{K^{1/\sigma}/\log K}{K(\log K)^2}
       =\frac{K^{1/\sigma-1}}{(\log K)^3}\longrightarrow\infty .
\]
This is a contradiction. For the version with arbitrary small losses,
choose \(\varepsilon>0\) so that \(b+\varepsilon<1\), and apply the
same argument with that exponent. \(\square\)

The argument still rules out (11) multiplied by
\(\exp(O(K(\log K)^A))\) for any fixed \(A\): its logarithm remains
smaller than \(K^{1/\sigma}/\log K\). This extension concerns a fixed
growth specification in \(K\); it does not forbid arbitrarily large
constants for each fixed \(K\), as in (3).

## 5. Consequence for the attempted growing-mark strategy

A hypothetical zero of multiplicity \(m\) makes the factor
\(\zeta(s)^z\), differentiated at the integer \(K\), contribute
\((s-\rho)^{Km}\log(s-\rho)\). The exact branch order of the full
arithmetic transform is \(Km\) plus any vanishing order of \(H_K\)
and of the smoothing transform at \(\rho\). Finite Euler factors of
\(H_K\) can vanish, so they must not be assumed nonzero here.
For fixed \(K\), the resulting Hankel term is suppressed by powers
of \(\log X\), but its exponent \(X^{\Re\rho}\) is unchanged.
The naive fixed-power heuristic at
\(K\asymp\log X/\log\log X\) also omits the compensating factorial
in the inverse-Laplace coefficient. The companion
GEVREY_INTEGER_WINDOW.md, equations (15)--(16), includes that factorial
and shows that this order still gives only a subpower factor in the
bare coefficient. The remaining arithmetic factors require additional
control as well.

Theorems 1 and 2 show that the needed naive uniform scalar bound is
false for the actual arithmetic coefficients. The failure is already
visible at imaginary parts tending to zero, so rapid high-frequency
decay of the smoothing does not remove it. Subtracting the complete
pole main term does not remove it either.

This is stronger than the first pass's abstract polynomial
counterexample. It is still a route-specific result:

- It concerns the scalar positive squarefree counts and their exact
  pole main terms.
- It does not refute the fixed positive-measure fractional-parameter
  estimate proposed for the native character family.
- It does not license an unproved lower bound for a different family
  mean, centered Gauss moment, or normalization.
- It does not establish a new zero-free region.

The viable arithmetic target remains fixed-parameter signed control of
the exact discrepancy in MATCHED_PRIME_SQUAREFREE_REMAINDER.md, or a
genuinely new family mean. Merely letting an integer mark order grow
does not supply that control.

## 6. A quantitative order/error tradeoff

The same proof gives a useful finer statement. Fix
\(1/2<\theta\le1\). If a uniform bound
\[
 |A_K(X)-C_K(X)|\ll X^b
       \quad\text{for all }K\le(\log X)^\theta       \tag{16}
\]
were available, then necessarily \(b\ge\theta\).
To prove this, assume \(b<\theta\), choose
\(\max(1/2,b)<\sigma<\theta\), and split the Mellin integral at
\(X_K=\exp(2K^{1/\theta})\). The alleged bound controls the upper
tail. The lower interval contributes at most
\(\exp(O(K^{1/\theta}\log K+K\log K))\), by the same elementary
coefficient and pole-circle bounds. The resonance (10) has logarithm
of order \(K^{1/\sigma}/\log K\), which is larger because
\(1/\sigma>1/\theta\). This is again a contradiction.

This tradeoff concerns a uniform scalar power error with its exact
integer pole principal term. It does not prohibit uniform asymptotic
formulas with larger errors, different normalizations, or parameter
ranges restricted in another way. No literature-priority claim is made.
