# Generic positive parameters remove common native Xi companion zeros

Status: PROPOSED ACTUAL-SOURCE THEOREM; independent exact-SHA review required.
Scope: an unconditional countable exceptional-set theorem for the literal
zeroth/fifth Xi companions; conditional reduced-height and BARE low-pass
consequences under the existing inner premise. RH remains unsolved.
Authoring base: cce5552c9de8a6ec0206977fdd7119a7fab3d874.
Exactly five new files; NA, GH, XL, LP, CP and the historical source are unchanged.

## 1. Native object and exact exceptional set

Keep XL1--XL4's unrescaled standard normalization:
\[
 f(z)=\Xi(z)=\xi_{\rm R}(1/2+iz)
       =\int_{\mathbb R}\Phi(u)e^{izu}\,du,\qquad
 \xi_{\rm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{GC1}
\]
The ACTUAL kernel is Phi=2phi_0, positive, even and superexponentially
decreasing. Let g=f^(5), and fix one positive constant lambda, independent
of z. Define the meromorphic quotients after every removable cancellation:
\[
 R_h=h-i\lambda h',\qquad C_h=h+i\lambda h',\qquad
 \Theta_h=R_h/C_h,\qquad \Theta_0=\Theta_f,\quad\Theta_5=\Theta_g .
 \tag{GC2}
\]
These are exactly the L-106620.4--.6 companions; their native ratio is
Theta_0/Theta_5. A variable lambda(z) or a Fourier multiplier is NOT used.

Define the parameter-independent entire function
\[
 W=f g'-f'g=f f^{(6)}-f'f^{(5)}
 \tag{GC3}
\]
and the following set using actual, not sampled, Xi values:
\[
 \mathcal Z=
 \left\{b\in\mathbb C_+:
 W(b)=0,\ f'(b)g'(b)\ne0,\
 \frac{f(b)}{i f'(b)}\in(0,\infty)\right\},\qquad
 \mathcal E=\left\{\frac{f(b)}{i f'(b)}:b\in\mathcal Z\right\}.
 \tag{GC4}
\]
The membership condition is an EXACT positive-real condition on a complex
ratio. Zeros of W alone are not enough.

**Unconditional theorem.** E is at most countable, possibly empty. For
every fixed lambda>0, the two meromorphic companions have a genuine common
zero in C+ if and only if lambda belongs to E. More precisely,
\[
 \Theta_0(b)=\Theta_5(b)=0
 \quad\Longleftrightarrow\quad
 b\in\mathcal Z,\quad \lambda=f(b)/(i f'(b)).
 \tag{GC5}
\]
The equality on the left means the values of the reduced meromorphic
quotients, not just two vanishing raw numerators.

For R>0, put E_R equal to the image in GC4 restricted to |b|<=R.
Then E_R is finite and
\[
 \#E_R\le\#\{b\in\mathcal Z:|b|\le R\}
 \le\sum_{\substack{W(b)=0\\|b|\le R}}\operatorname{ord}_b W<\infty .
 \tag{GC6}
\]
No O(R log R) estimate is claimed here. E is not asserted to be finite or
locally finite in PARAMETER space: bounded lambda need not bound |b|.
In particular E may be dense; no open stability or explicit good lambda
is proved. Its complement is dense and has full Lebesgue measure, simply
because E is countable. That measure statement does not classify a
prescribed rational lambda or a prescribed countable physical sequence.

## 2. Internal cancellation cannot masquerade as a companion zero

Let h be either f or g. These are nonzero entire functions by GC1.
Neither R_h nor C_h is identically zero: the equation h'=constant*h
would force an exponential; the nonconstant even f and nonzero odd g
cannot have that form. Nonconstancy/nonvanishing also follows from their
strict nonzero even kernel moments.

At any zero b of h of order r>=1, write
h(z)=(z-b)^r a(z), a(b)!=0. With lambda>0,
\[
 \begin{split}
 R_h(z)&=(z-b)^{r-1}
 \{(z-b)a(z)-i\lambda[r a(z)+(z-b)a'(z)]\},\\
 C_h(z)&=(z-b)^{r-1}
 \{(z-b)a(z)+i\lambda[r a(z)+(z-b)a'(z)]\}.
 \end{split}                                                    \tag{GC7}
\]
Both braces are nonzero at b. Thus precisely r-1 powers cancel, and
Theta_h(b)=-1. This holds at COMPLEX zeros as well as real ones, without
RH or simplicity. For r=1 there is no common factor, with the same value.

Conversely, if Theta_h has a genuine zero at b, h(b) cannot vanish by GC7.
Therefore C_h(b) cannot vanish together with R_h(b); adding and subtracting
their equations would force h(b)=h'(b)=0. Hence C_h(b)!=0, R_h(b)=0,
and h(b)=i lambda h'(b) with h'(b)!=0.

Apply this to f and g at a genuine common zero. It gives W(b)=0 and
the unique positive lambda=f(b)/(i f'(b))=g(b)/(i g'(b)).
Conversely, the right side of GC5 gives f=i lambda f'; then W=0 and
f'!=0 give g=i lambda g'. Both derivatives are nonzero, so
C_f=2i lambda f' and C_g=2i lambda g' are nonzero. Both quotients really
vanish. This proves the exact equivalence, including all cancellation cases.
The parameter lambda=0 is excluded throughout; both reduced quotients
would then be identically one.

## 3. Nonzero Wronskian, countability and multiplicities

Write mu_j=integral_R u^j Phi(u)du. The actual kernel gives mu_0,mu_6>0,
finite moments of every order, and
f^(j)(0)=i^j mu_j, with odd moments zero. Thus
\[
 W(0)=f(0)f^{(6)}(0)-f'(0)f^{(5)}(0)
     =-\mu_0\mu_6<0.                                      \tag{GC8}
\]
Differentiation under the entire Fourier integral is justified locally
uniformly by XL's superexponential tail. In particular W is a nonzero
entire function. At any zero its Taylor series has a first nonzero
coefficient, giving an isolated zero of finite order. An infinite zero
set in a closed bounded disk would have an accumulation point there and
force W identically zero by the identity theorem. Therefore every such
disk has only finitely many W zeros. Taking the union of integer-radius
disks proves GC6 and countability of E, with NO RH assumption.

There is useful local multiplicity information. If the common genuine
Theta_0 and Theta_5 zero has orders m,n, respectively, then
\[
 W=R_f g'-f'R_g,\qquad
 \min(m,n)\le\operatorname{ord}_b W.                       \tag{GC9}
\]
Here f'(b)g'(b)!=0, and the denominators are nonzero, so R_f,R_g have
orders m,n. The displayed identity proves the bound; if m!=n equality
holds. When m=n, cancellation of leading terms can make the W order
strictly larger. No W'(b)!=0 or companion simplicity is inferred.
For any fixed lambda, summing minimum common multiplicities in |b|<=R
is bounded by the W zero multiplicity sum in GC6.

For completeness NA's AX7 excludes the positive imaginary axis directly.
Put h(y)=f(iy). The exact phases give
\[
 W(iy)=-\{h(y)h^{(6)}(y)-h'(y)h^{(5)}(y)\}
       \le-\mu_0\mu_6<0\quad(y>0).                        \tag{GC10}
\]
Thus Z contains no such point. Since W is even and real entire,
b in Z implies -bar b in Z, and the positive lambda is the same:
f(-bar b)=bar f(b), f'(-bar b)=-bar f'(b).
The upper-half-plane points therefore occur in distinct reflected pairs.
This does not decide whether E is empty or exhibit a member.

## 4. Conditional native reduction and bare low-pass consequence

Fix lambda outside E. Assume exactly GH's two-component premise: both
Theta_0 and Theta_5 are inner in C+. RH is a sufficient single premise
for all lambda>0, by GH's real-zero/derivative argument; it is NOT proved
here. GH's meromorphic continuation and imaginary-axis limit exclude
both finite-boundary singular factors and a singular factor at infinity.
Consequently both components are PURE Blaschke products, and GH3 states
that both global unweighted zero-height sums are infinite.

Let G be the maximal common inner divisor and write
Theta_0=G U, Theta_5=G B. A divisor of a pure Blaschke product is pure,
with zero multiplicities bounded by those of the product. GC5 says there
are no common C+ zeros when lambda is outside E. Thus G is unimodular
constant, and
\[
 \sum_{U(b)=0,\ \Im b>0}\Im b
 =\sum_{B(b)=0,\ \Im b>0}\Im b=\infty ,
 \qquad U/B=\Theta_0/\Theta_5.                             \tag{GC11}
\]
Zeros have their full multiplicities. This closes GH's cancellation gate
for these generic fixed parameters, not for every positive parameter.
Under the inner premise lambda in E is equivalently nonconstant G.
Nothing here bounds the height removed by G at an exceptional parameter.

Use LP's boundary dx norm and its unitary Fourier convention
F(z)=(2pi)^(-1/2) integral_0^infinity v(t)e^(izt)dt. For either
V=B or V=U, LP3 and GC11 yield, for EVERY fixed L>0,
\[
 \operatorname{tr}
 \bigl(\Pi_{[0,L]}P_{K_V}\Pi_{[0,L]}\bigr)=\infty,\qquad
 K_V=H^2\ominus VH^2.                                    \tag{GC12}
\]
These are extended nonnegative BARE traces, with no inner numerator
projection inserted. No assertion about arbitrary shifted or shrinking
bands is made: LP Section 6 prohibits that inference.

Most importantly, GC12 does NOT imply divergence, a uniform lower bound,
or a cofinal capture theorem for
\[
 C_I(B,U)=\|\Pi_I P_{UH^2}P_{K_B}\|_{\mathcal S_2}^2,
 \qquad P_{UH^2}=M_U M_U^* .
\]
CP gives an explicit coprime pure infinite-height pair with even GLOBAL
corrected capture <1/9. Its numerator-transmitted M_U quantity is different
again. The present native coprimality theorem does not supply numerator
samples, confluent jets, Riesz bounds, or the physical outer metric.

L-106620 prescribes lambda_j=1/omega(t_j). A countable prescribed sequence
may lie entirely in a countable exceptional set. We have NOT proved that
any prescribed lambda_j avoids E, authorized changing the gauge, or
interchanged lambda, physical T, radius and cofinal limits. NA's finite-axis
sampling theorem remains a separate statement.

## 5. Exact finite controls, not native zero samples

The producer checks Gaussian-rational polynomial identities, with actual
derivative linkage g=f^(5), for the following explicitly NONNATIVE controls:

| f | point and parameter | genuine common orders | W order |
|---|---|---|---|
| 5-z^6 | b=i, lambda=1 | 1,1 | 1 |
| (5-z^2)^3 | b=i, lambda=1 | 1,1 | 1 |
| 5-15z^2-5z^4-z^6 | b=i, lambda=1 | 1,1 | 3 |
| 1-25z^2-60z^4-42z^6-9z^8-z^10 | b=i, any lambda>0 | neither; both values -1 | 4 |

In the third control g=-30240z(z^2+1)^2; both f and g vanish to order two,
so both raw numerators have simple zeros that disappear internally.
The second has W=-3600(z^2+1)^3 and disproves equality in GC9 in general.
For the first, g=-720z and W=-3600(1+z^6); the positive-real ratio condition
forces b=i lambda, hence lambda^6=1 and lambda=1. This finite model has
exceptional set {1}, but is NOT an enumeration of E for Xi.
The additional real-rooted control (5-z^2)^3 has g=-720z and
W=-3600(5-z^2)^2(1+z^2). Thus even real-rooted polynomial companions can
have an exceptional positive parameter. Its multiple real roots give the
same removable value -1 by GC7, separately from the genuine common zero i.
The table's axis points do not contradict GC10: these polynomial controls
are not actual-Xi functions or positive-kernel surrogates.

Coefficientwise checks also retain R_5=R_0^(5) and
R_0 C_5-C_0 R_5=2i lambda W. Local derivative evaluation determines all
cancellation orders exactly. Independent tests use symbolic coefficient
expansion and shifted Taylor coefficients; no numerical Xi, zeros, logs,
exponentials, gamma, infinite trace or analytic-limit evaluation occurs.

Arithmetic is MIXED: EXACT_RATIONAL plus CERTIFIED_INTEGER_COVERAGE.
Public rational components have at most32 bits; internal components4096;
input polynomial degree<=16, internal degree<=32, local charged work<=200000,
UTF-8 input<=2000000 bytes, JSON nodes<=20000 and depth<=24.
Strict bool/int separation, complete typed reconstruction, all six frozen
source identities, four artifact seals and a canonical payload seal are
mandatory, including under Python -O. Machine caps do not restrict the
analytic theorem and do not prove its unbounded quantifiers.

The six complete pinned notes were personally read: NA for moments,
axis exclusion and the native W identity; XL for the actual kernel;
GH for the conditional pure component heights; LP for the zero-start
bare trace theorem; CP for the corrected-capture obstruction; L-106620
for the fixed-parameter source allocation. No ancestor code is executed.
The isolated-zero/identity theorem and inner-factor divisibility are
classical facts, not claimed as new principles. No exhaustive novelty,
global-zero classification, critical-line density, or RH claim is made.

Smallest result-invalidating burden: GC5's cancellation-safe equivalence
or GC8's actual-kernel nonvanishing. The conditional downstream import
additionally requires the existing inner premise and GH/LP theorems.
Smallest remaining native burden: decide a prescribed parameter's
exceptional membership, and independently control the corrected physical
numerator/jet operator; generic coprimality pays neither of those gates.
