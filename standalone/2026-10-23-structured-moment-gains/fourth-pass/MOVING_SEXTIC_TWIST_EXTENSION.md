# Uniform moving sextic twists in the Möbius cubic Gauss moment

Status: proposed source-dependent extension; independent review requested.
The explicit ordinary exceptional saving below is separate from the
existential saving in the full moment. No new zero-free boundary is
claimed.

Scope: Eisenstein ideals in the source's primary convention, fixed
angular order and fixed initial ray data, and a moving finite character
of specified local type. The moving modulus is part of the quantified
data and is never absorbed into the fixed arithmetic constants.

Dependencies: the frozen third-pass packet at
`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`,
especially `QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md` and
`FULL_MOBIUS_CUBIC_MOMENT.md`, with the exact primary-source bindings in
its `SOURCES.json`. The needed functional equation has its standard
conductor-uniform form; only the angular order and the initial finite
ray data remain fixed.

## 1. The family of moving twists

Let $t$ be squarefree and prime to the fixed initial omitted set.
Let $\xi_t$ be a finite Hecke character, in the chosen primary
convention, with good-prime conductor exactly $t$. At every good prime
of $t$, require that its local character have a nontrivial quadratic
component: in sextic notation its exponent is odd. Thus multiplication
by a cubic character cannot make this local character principal.
Its ramified part at the fixed primes ranges over a fixed finite family.
For example, the reciprocity presentation of
$n\mapsto\overline{\chi_{6,n}(t)}$ has this form, up to fixed ray phases.
All characters have their complete zero extension.

Put $\theta_t=\Theta_\ell\nu\xi_t$, where $\ell$ and $\nu$ are fixed.
Throughout, $t$ is fixed within each character-row mean. It may change
as the length parameters change.

## 2. An explicit uniform exceptional estimate

In the notation of the frozen quantitative appendix, replace its fixed
$\nu$ by $\theta_t$ and assume

\[
Nt\le Y^{7/10},\qquad 1+|u|\le Y^{1/100}.                    \tag{1}
\]

Retain $Nv,Ne\le Y^\delta$ and the two $\delta$-neighborhoods of
$(\log_Y Np,\log_Y Nq)=(1,0)$ or $(1/3,1/3)$. Then the same explicit
choices

\[
\delta=10^{-9},\qquad \eta_{\mathrm{exc}}=10^{-6}             \tag{2}
\]

give

\[
\sum_{p,q}\left|\sum_{(b,e)=1}\mu(b)\theta_t(b)
 W(Nb/Y)(Nb)^{iu}\chi_b(vpq^2)\right|^2
 \ll Y^{7/3-\eta_{\mathrm{exc}}}.                            \tag{3}
\]

The constant is uniform in $t$ and in the allowed local sextic
characters. No zero-free hypothesis is used for (3).

### Character conductors and the full smooth factor

The exact three-factor Möbius identity commutes with $\theta_t$,
including its zeros. In the full-factor functional equation, the good
primitive conductor has norm at most a fixed multiple of $N(tvpq)$.
At primes of $t$, its quadratic component is nontrivial, so a cubic
factor at $p,q,v$ cannot cancel that conductor. At primes of $pq$
outside $t$, the surviving cubic factor is primitive. The only remaining
deleted Euler factors are the original small $ve$ factors and fixed
ones. Their treatment is exactly the appendix's treatment.

Truncate the common Mellin shifts at $Y^{1/100}$. After a fixed endpoint
enlargement, the total height is at most $Y^{1/50}$ for large $Y$.
The product of the new conductor factor and the archimedean height
factor is therefore at most

\[
Y^{7/10}(Y^{1/50})^2=Y^{37/50}=Y^{.74}.                      \tag{4}
\]

This is precisely the allowance used for the old full-factor step,
where the coefficient twist was fixed and the total height was at most
$Y^{.37}$. Hence, when the full factor exponent $a_3\ge9/10$, the
same calculations give the upper exponents

\[
\frac{349}{150}+10^{-4}\quad\hbox{and}\quad
\frac{341}{150}+10^{-4},                                    \tag{5}
\]

in the first and second configurations respectively. Both retain the
strict margins displayed in the quantitative appendix. The varying
conductor norm changes the dual scale and a modulus-one root number;
the source's common scale-supremum and Mellin argument handle the former,
and the latter stays outside the polynomial. Its dual coefficient
$\overline{\theta_t}$ is common to all the rows.
In particular no partition according to $(p,t)$ or $(q,t)$ is required:
one can use the common maximum conductor cutoff, with the varying
actual conductor and its symmetry-line phase left in the common
profile parameters and row scalars. The modulus $t$ is part of the
primitive conductor, not part of the small deleted-Euler-factor budget.

### Sieves and the Gram matrix: no hidden growing mask

Every copied product has a common coefficient of the form
$\theta_t(n)c_n$, with $c_n$ bounded by a fixed divisor power. This
follows from complete multiplicativity of the twist, including zeros.
The ordinary and cubic large sieves place $\theta_t$ in their
coefficient vector, so their constants have no $Nt$ dependence.

The same placement handles the Gram step. Take the Hilbert space of
**all** primary $n$ in the relevant fixed annulus and its row vectors
$W(Nn/Z)^{1/2}\chi_p(n)$. Put the entire $\theta_t$, including its
vanishing at $(n,t)>1$, in the common coefficient vector. Its squared
norm is at most $Z^{1+\epsilon}$. The row Gram kernel is exactly

\[
T_{p,p'}=\sum_nW(Nn/Z)\chi_p(n)\overline{\chi_{p'}(n)},        \tag{6}
\]

with the source's full unpunctured support. The inner products still
equal the desired copied polynomials, because their coefficient vector
is zero at every forbidden column. Thus the unmasked source Gram
bound applies directly. This argument does not assert monotonicity of a
masked Gram matrix and does not erase a mask from a pre-existing Gram
identity.

The remainder of the quantitative proof, with at most 29 copies and
error budget $10^{-4}$, is unchanged. Its constants depend on fixed
divisor orders and smooth seminorms, not the moving finite modulus.
Equations (4)--(6) prove (3) with the stated uniformity.

## 3. A uniform full-moment consequence

Assume the all-finite-character version of `ZF_beta` stated in Section 1
of the frozen full-moment theorem, at the fixed angular order. The
third-pass proof consumed only cubic finite twists; the present
extension also consumes the sextic twists $\xi_t$ just defined and
their products with cubic characters. This is within that stated
all-finite-character hypothesis, and is an additional use of it.

For every fixed $\beta<1$, there is $\eta_0>0$, uniform over this
moving family, such that

\[
\sum_aW(a/\sqrt A)
 \left|\sum_b\frac{\mu(b)\theta_t(b)G(b)}{\sqrt{Nb}}
             \overline{\chi_b(a)}V(Nb/B)\right|^2
 \ll(AB)^\epsilon\{A+(AB)^{2/3-\eta_0}\}                   \tag{7}
\]

for

\[
A\ge B\ge2,\qquad Nt\le B^{2/3}.                           \tag{8}
\]

Here is the parameter handoff. The literal $f,m,l$ Poisson identity and
its masks retain $\theta_t(fl)\theta_t(n)$; a zero outer factor remains
zero. The generic large-conductor and large-common-divisor estimates
use only divisor-bounded coefficients and are uniform in $t$.
The short-conductor part uses the reciprocal-Hecke estimate with
conductor at most a polynomial in $AB$, now including $Nt$; its
arbitrarily small conductor power is still absorbed in $(AB)^\epsilon$.

Only the exceptional limits require the new adapter. Their surviving
column length is $Y=B/(FL)=B^{1-o(1)}$. The strict gap
$2/3<7/10$ ensures $Nt\le Y^{7/10}$ throughout a sufficiently small
fixed exceptional neighborhood. Explicitly, if $F,L\le X^{\delta_{\rm out}}$
and $Y\ge X^c$, then

\[
Nt\le B^{2/3}=Y^{2/3}(FL)^{2/3}
 \le Y^{2/3+4\delta_{\rm out}/(3c)}<Y^{7/10}.
\]

In the remaining large-conductor range $A\le B^{2\beta}$ one can
take $c=1/4$ after decreasing $\delta_{\rm out}$. This outer cutoff
is distinct from the exceptional adapter's
$\delta_{\rm exc}=10^{-9}$ and must be much smaller. The unchanged
handoff for the other moving data is

\[
Nv\le Y^{4\delta_{\rm out}/c},\qquad
Ne\ll Y^{\rho+(7\delta_{\rm out}+2\delta')/(3c)}.
\]

Choose the exceptional neighborhood radius
$\rho\le\delta_{\rm exc}/10$, then
$\delta_{\rm out}\le c\delta_{\rm exc}/100$ (also respecting the
earlier small-conductor choices), and $\delta'\le\delta_{\rm out}/100$.
Both exponents are strictly below $\delta_{\rm exc}$, with room for
the fixed initial puncture. These choices also make the displayed
twist-conductor exponent strictly less than $7/10$.
The original fixed smooth kernels
allow the common Mellin heights to be truncated at $Y^{1/100}$ with
arbitrarily small tail loss; no preassigned $Y^{.36}$ height range is
required for the full moment with fixed tests. Thus (1)--(3) apply.
The quantitative gap in (3), combined with the source's other strict
large-conductor gaps and its compactness argument, gives a uniform
positive $\eta_0$. As in the frozen theorem, no numerical full-moment
$\eta_0$ is asserted.

## 4. Compatibility with the cubic-power rectangular extension

The identity and divisor-fibre proof in
`CUBIC_POWER_RECTANGULAR_EXTENSION.md` work verbatim with $\theta_t$:
its zeros are retained in the outer $\theta_t(d)$ and the inner row.
The conductor restriction must, however, hold at each shortened column
length $B/Nd$. With amplifier $C\asymp(B/A)^{1/3}$ it is enough that

\[
Nt\le (B/C)^{2/3},                                        \tag{9}
\]

with a fixed constant adjustment at endpoints. Under (9), (7) supplies

\[
J_t(A,B)\ll(AB)^\epsilon
\{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta_0}\},\qquad A\le B.    \tag{10}
\]

For the fourth-moment square-core application, $B=U$,
$A=U/T^{1/2}$ and $Nt\asymp T$. Then $C\asymp T^{1/6}$, and
(9) holds with room whenever $T\le U^{3/5-\delta_0}$ for a fixed
$\delta_0>0$. This includes the small-core interval needed for the
separate fourth-moment calculation when $\eta_0$ is decreased as
necessary. It does not cover arbitrary moving twists, large cores,
or row-dependent twists inside a single mean.
