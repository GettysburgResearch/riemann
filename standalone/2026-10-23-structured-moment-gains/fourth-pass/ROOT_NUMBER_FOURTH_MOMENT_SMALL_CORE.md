# The root-number fourth moment: a power saving for small squarefree cores

Status: proposed source-dependent component theorem. This bounds a
specified signed part of a fourth-moment approximate functional
equation. The full unamplified fourth moment already has an imported
bound of size $U^{1+\epsilon}$; the new assertion is the power saving
for the component below. It does not yet enlarge the prime capacity of
M2 or improve a zero-free boundary.

Scope: squarefree primary physical rows $u$ in an Eisenstein norm
annulus $Nu\asymp U$, fixed initial ramification and ray data, and
fixed angular order. Powerful physical rows, arbitrary detected-class
indicators, and prime-amplified moments are not included in this
component theorem.

Dependencies: `MOVING_SEXTIC_TWIST_EXTENSION.md`, frozen SHA256
`b43ee0452b171420aad77f5dc345c65b12ada1a269c8228ea9bebf95c804ee23`,
including its explicit all-finite-character `ZF_beta` hypothesis;
`CUBIC_POWER_RECTANGULAR_EXTENSION.md`, frozen SHA256
`30b3df5f463bf6735b04dc22dfb2bf62f5287d5ae3b827870302eef43ebfc96e`;
the finite Gauss identities `eq:signal` and the primitive Hecke
functional equation in the quasi-Riemann source
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The approximate functional equation below is the standard symmetric
Mellin construction applied to the fourth power, with the same
finite-seminorm and height treatment as Liu, arXiv:2610.26835v1,
Section 14.2. Its fourfold coefficient and conductor normalization
are displayed explicitly.

## 1. Exact phase and approximate-functional-equation normalization

Let $\psi_u$ be the primitive character inducing the chosen sextic
presentation. These physical $L$-functions have finite-order characters
and trivial infinite type; the fixed angular factor below occurs on
the parameter $u$ through the Gauss identity, not in $\psi_u$ itself.
Restrict first to nonprincipal primitive $\psi_u$. A fixed coefficient
twist supported in the initial omitted set cannot cancel ramification
at a good prime of the squarefree $u$, so any excluded principal
or bounded-conductor physical rows form a bounded fixed family. They
are treated separately by the corresponding fixed $L$-functions and
are absent from a sufficiently large norm annulus. No pole-free
approximate functional equation is applied to those rows.

A fixed finite ray decomposition makes its conductor
norm $Q_u=c_0 Nu$, with $c_0$ fixed in the component. Fixed coefficient
twists have their conductor inside the initial omitted set. Let
$\mathcal E_u(\tau)$ be the unit-modulus factor in the central-line
functional equation

\[
L(1/2+i\tau,\psi_u)
 =\mathcal E_u(\tau)\overline{L(1/2+i\tau,\psi_u)}.           \tag{1}
\]

Its finite root number is, up to fixed ray phases, $\gamma_1(u)$.
The source identities
$\gamma_1\gamma_2=\mu\alpha G_{\mathrm{ray}}$ and
$\gamma_2^3=\mu\alpha$ imply

\[
\gamma_1(u)^2
 =\mu(u)\alpha(u)G_{\mathrm{ray}}(u)^2\gamma_2(u),
\qquad
\gamma_1(u)^{-2}
 =\mu(u)\overline{\alpha(u)G_{\mathrm{ray}}(u)^2\gamma_2(u)}.
                                                                    \tag{2}
\]

The remaining factor in $\mathcal E_u(\tau)^{-2}$ is a common
archimedean unit phase times $Q_u^{2i\tau}$. Thus, on this squarefree
row component, it is the actual coefficient
$\mu(u)\overline{\gamma_2(u)}$ with fixed angular/ray data and a
common norm twist. It is not an arbitrary coefficient replacement.

Let $d_4(n)$ count the ordered fourfold ideal factorizations of $n$.
The conductor of $L(s,\psi_u)^4$ is $Q_u^4$, so its balanced
Dirichlet-polynomial scale is $Q_u^2$. The symmetric approximate
functional equation gives

\[
|L(1/2+i\tau,\psi_u)|^4
 =2\Re\left\{
 \mathcal E_u(\tau)^{-2}
 \sum_n\frac{d_4(n)\psi_u(n)}{(Nn)^{1/2+i\tau}}
        V_\tau(Nn/Q_u^2)\right\}.                           \tag{3}
\]

For example, insert an even Gaussian Mellin factor in the contour
integral for the fourth power. The reflected integral is the complex
conjugate after multiplication by $\mathcal E_u^{-2}$, which proves
the factor $2\Re$ in (3). There is no pole of the nonprincipal
$L$-function to cross; the residue at the Mellin origin is the fourth
power itself. The smooth function $V_\tau$ and its Euler derivatives
are bounded at zero and rapidly decreasing after the scale
$(1+|\tau|)^4$, with finite polynomial dependence on $1+|\tau|$.

Factors of $n$ at the fixed omitted primes can be expanded separately.
Their coefficient mass is bounded by the convergent product of
$\sum_{j\ge0}(j+1)^3(Np)^{-j/2}$. Their phases range over fixed ray
components, and their exact norm extraction only rescales the test.
The formulas below therefore concern the good part of $n$ and retain
all its original zero extensions.

## 2. The exact square-core family

For each good ideal $n$, write uniquely

\[
n=t h^2,\qquad t\text{ squarefree}.                          \tag{4}
\]

No condition $(t,h)=1$ is imposed. On the original support,

\[
\psi_u(th^2)=\psi_u(t)\chi_{3,u}(h)
               \times\text{a fixed coefficient phase in }h.\tag{5}
\]

For a fixed $t$, reciprocity places $\psi_u(t)$ in a common finite
sextic twist $\xi_t(u)$, up to fixed ray phases. Its local quadratic
component is nontrivial at every good prime of $t$, exactly as
required in the moving-twist theorem.

Fix a norm dyad $Nn\asymp X$ and a core dyad $Nt\asymp T$. Then

\[
Nh\asymp H=(X/T)^{1/2}.                                    \tag{6}
\]

Common Mellin separation of the smooth $n/Q_u^2$ and $Nu/U$ variables
is performed before fixing the live row $u$. It leaves a common
rapidly decreasing measure, a fixed norm-annular test on $u$, and
coefficients on $h$ independent of $u$. Those coefficients have
absolute value at most

\[
(XTU)^\epsilon T^{-1/2}H^{-1}.                              \tag{7}
\]

This is simply $d_4(th^2)/\sqrt{N(th^2)}$; no coefficient
$\mu(th^2)$ is inserted. The Möbius factor remains on the physical
index $u$ through (2).

## 3. A dyadic component estimate

Let $\eta_0$ be the positive saving in the moving-twist full moment.
Fix $0<\eta<\min(\eta_0,1/100)$, decreasing it later to reserve
height and tail losses. Suppose initially that $1\le X\le U^2$,
$1\le T\le X$, and

\[
T\le U^{2/5}X^{1/10-\epsilon_0}                              \tag{8}
\]

with any convenient fixed positive margin; alternatively one can use
$T\le U^{2/5-\epsilon_0}X^{1/10}$ away from bounded endpoints.
The power margin is needed only at the upper conductor boundary.

For each fixed $t$, the rectangular estimate with column length $U$
and row length $H$ gives

\[
J_t(H,U)\ll (XU)^\epsilon H^{1/3}U^{1-2\eta}.                \tag{9}
\]

The smaller diagonal term has been absorbed because $\eta<1/6$.
To check the shortened-column condition, the cubic amplifier has
$C\asymp(U/H)^{1/3}=U^{1/3}X^{-1/6}T^{1/6}$. The condition
$T\le(U/C)^{2/3}$ is exactly

\[
T\le U^{2/5}X^{1/10}.                                      \tag{10}
\]

Thus (8) is a sufficient quantified use of the moving-twist theorem.

The actual unnormalized sum over $u$ is $U^{1/2}$ times the normalized
column in (9), after inserting a fixed scaled norm factor in its
test. Cauchy over $h$, (7), and then the count $O(T)$ for squarefree
$t$ give the following bound for the entire signed $(X,T)$ block
in (3):

\[
\boxed{\quad
|\mathcal C_{X,T}(U,\tau)|
 \ll (XU)^\epsilon(1+|\tau|)^C
       U^{1-\eta}X^{-1/6}T^{2/3}.
\quad}                                                     \tag{11}
\]

For clarity, before summing $t$, the Cauchy bound is
$U^{1/2}(T^{-1}H^{-1})^{1/2}J_t(H,U)^{1/2}$.
Multiplication by the number $O(T)$ leaves
$U^{1-\eta}T^{1/2}H^{-1/3}$, which is (11).
The argument is also obtained by one Cauchy inequality over $(t,h)$.
It does not assume independence of the divisor coefficient $d_4(th^2)$.

The exponent $C$ is finite after fixing the source smooth orders.
For bounded heights its factor is harmless. For a small growing height
range, request the profile estimates and select that range only after
$C$ and the tail orders have been fixed.

## 4. A power saving below the full fourth-moment scale

In every dyad retain the cores

\[
T\le X^{1/4}U^{3\eta/4}.                                   \tag{12}
\]

Then (11) gives $U^{1-\eta/2+\epsilon}$, apart from its fixed
polynomial height factor. For $X\le U^2$, (12) has ample room inside
(10), since
$X^{3/20}U^{3\eta/4}\le U^{3/10+3\eta/4}<U^{2/5}$.
Bounded initial dyads are included directly, without replacing a
subunit frequency count by an extra row.

At the balanced fourth-power scale $X\asymp U^2$, the precise dyadic
conclusion is

\[
|\mathcal C_{U^2,T}|
 \ll U^{2/3-\eta+\epsilon}T^{2/3}(1+|\tau|)^C,
\qquad
T\le U^{1/2+3\eta/4}.                                     \tag{13}
\]

There are only logarithmically many dyads. One may include the
approximate-functional-equation tail as follows. Fix a small
$\zeta>0$ compared with $\eta$ and retain $X\le U^{2+\zeta}$.
For $H>U$ in this slightly enlarged range use the original $A\ge B$
moment; comparison with (9) costs at most $U^{\zeta/6}$ in that
squared moment. The tail beyond $U^{2+\zeta}$ is arbitrarily small by
choosing a fixed sufficiently large decay order. Choose the allowable
height exponent $\tau_0>0$ after that order and the finite polynomial
height exponent, with

\[
4\tau_0<\zeta/2,
\qquad C\tau_0<\eta/100,
\qquad \tau_0<1/10000.                                    \tag{14}
\]

The first inequality keeps the analytic-conductor height enlargement
inside the retained range. The last keeps the internal full-factor
heights inside the moving-twist adapter's allowance. By first decreasing
$\eta$ relative to $\eta_0$ and choosing $\zeta$ and the subsidiary
losses sufficiently small, the **sum of all the components (12)** is

\[
\ll U^{1-\eta/3}
\qquad (|\tau|\le U^{\tau_0}).                              \tag{15}
\]

Here the left side means the absolute value of the signed sum after
the componentwise upper bounds; neither its original terms nor
$\mathcal C_{X,T}$ are assumed nonnegative.

## 5. The exact remaining part

The remainder in (3) consists of the dyadic blocks

\[
T>X^{1/4}U^{3\eta/4},                                     \tag{16}
\]

with the same two-variable AFE kernel, the original squarefree $u$
sum, $d_4(th^2)$, and the full phase

\[
\mu(u)\overline{\gamma_2(u)}\,
 \theta_\tau(u)\,\chi_{6,u}(t)\chi_{3,u}(h).                 \tag{17}
\]

The finite ray and angular part of $\theta_\tau$ is fixed, and its
norm twist is common. At the main scale this includes cores larger
than $U^{1/2+3\eta/4}$. There is no arbitrary detected-class mask in
this formulation.

It is not legitimate to replace (17) by a bare quadratic family in
$t$. In sextic conventions,

\[
\chi_{6,u}(th^2)=\chi_{2,u}(t)\chi_{3,u}(t^2h),              \tag{18}
\]

with all zeros retained. The cubic $t^2$ phase remains dependent on
the same $t$ being averaged. A direct quadratic large-sieve invocation
would therefore have row-dependent column coefficients. Changing the
cubic variable to $t^2h$ creates a sparse divisibility condition and
enlarges its norm range; it cannot be done for free.

For comparison, the generic sextic large sieve is legal after fixing
$h$, but it only gives, up to small powers,

\[
|\mathcal C_{X,T}|
 \ll \{U[T+U+(TU)^{2/3}]\}^{1/2}.                          \tag{19}
\]

Indeed the $h$-coefficient squared mass over all $(t,h)$ is $O(H^{-1})$,
the squared unnormalized $u$ coefficient mass is $O(U)$, and summing
the legal fixed-$h$ sieve over $H$ choices cancels that $H^{-1}$.
At $X=U^2$, $U^{1/2}\le T\le U^2$, its cross term is
$U^{5/6}T^{1/3}$, which exceeds $U$ as soon as $T>U^{1/2}$.
This identifies the missing large-core estimate quantitatively.

The original M2 fourth-moment bound controls the complete expression
by a different two-transform induction, but its present prime capacity
cannot be strengthened merely by substituting (15). A new estimate
for (16)--(17), or a way of retaining and exploiting its signed
correlation with the prime factors, remains necessary. Prime-pair
expansion adds moving phases with even or canceled local exponents
and redundant punctures; these require their own exact uniform
extension and have not been silently placed in the odd-local-twist
theorem used above.
