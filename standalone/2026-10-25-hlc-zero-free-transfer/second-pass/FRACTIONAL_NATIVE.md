# Growing-prime coefficient control in the original physical family

Status: proved source-dependent mean estimate, with an explicit Euler-product
cost. No improved zero-free half-plane is claimed.

Scope: the original nonprincipal sixth-power-free Eisenstein row family,
original collision zeros, fixed ray data, common profiles and licensed norm
heights. The changed primes grow with the column length. They are not inserted
as an unlicensed large moving conductor.

Exact sources: the ordinary squarefree endpoint in PR #1021,
`arithmetic/DIRECT_NATIVE_APPLICATION.md`, Git blob
`ea1a09486fc77016629f0b4307f668ac8c297953`, at head
`0f07049ff1e8cc7765f6de01b4e176ad627bba4b`; its source is Xu--Sang,
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Theorem 2.2 and
Corollary 2.3. The newer packet at that same head proves an endpoint window
for the *full* prime-factor parameter in
`standalone/2026-10-25-selector-and-marked-estimates/fractional/UNIFORM_FRACTIONAL_WINDOW.md`,
blob `15378a3d56ec8a0d16ee185f16dbc00482910079`. The result below changes a
different object: it controls a fixed parameter range on a growing set of
prime ideals, with explicit dependence on that set.

What was run: `check_fractional_prefix.py` verifies the exact scalar coefficient
convolution at five rational parameters, four prime cutoffs, and all integers
through 800, for three anchors, and 11,200 binomial-mark coefficient identities.
It is a finite algebra check, not verification of an asymptotic
moment theorem or of the imported ordinary framework.

Smallest unresolved issue: control the full fixed-parameter damping remainder,
or estimate the remaining large-prime signs jointly. Theorem 2 below does
reach the HLC prime scales for actual polynomial prime-factor marks; the
complete nonpolynomial damping is not inferred from it.

## 1. Statement with the full cost retained

Let `psi_u` be the actual completely multiplicative, naturally zero-extended
presentation on the physical rows `u`, including the original common masks.
The finite set of nonprincipal-row exceptions is handled exactly as in the
endpoint adapter; a growing coefficient conductor is not allowed silently.
For the same nonnegative row measure and one common smooth annular profile,
write

\[
 V_1(X;u)=X^{-1/2}\sum_{\mathfrak n}
    \mu^2(\mathfrak n)\psi_u(\mathfrak n)
    (N\mathfrak n)^{it}W(N\mathfrak n/X).
 \tag{1}
\]

The imported endpoint states, on each prescribed bounded-power length range,

\[
 \|V_1(X;\cdot)\|_{\ell^2(w)}
 \ll_\varepsilon U^{1/2+\varepsilon}
          (1+|t|)^A p_J(W),\qquad X\le U^C.
 \tag{2}
\]

The finitely bounded nonempty subunit scales are included; empty scales are
zero. All constants and profile/height orders have the endpoint's scope.

Let `P` be any finite set of good prime ideals. Choose arbitrary complex
parameters `z_p` on `P`, and set

\[
 a_{\mathbf z,P}(\mathfrak n)
  =\mu^2(\mathfrak n)
       \prod_{\substack{\mathfrak p\mid\mathfrak n\\\mathfrak p\in P}}
                  z_{\mathfrak p}.
 \tag{3}
\]

Define `V_{z,P}(D;u)` by replacing `mu^2` in (1) with (3).

**Theorem 1.** Under (2),

\[
 \boxed{\displaystyle
 \|V_{\mathbf z,P}(D;\cdot)\|_{\ell^2(w)}
 \ll_\varepsilon U^{1/2+\varepsilon}(1+|t|)^A p_J(W)
   \prod_{\mathfrak p\in P}
       \left(1+\frac{|z_{\mathfrak p}-1|}
                         {\sqrt{N\mathfrak p}-1}\right).}
 \tag{4}
\]

The implied constant is independent of the number, location, and parameters
of these primes. Their entire cost is displayed. In particular, arbitrary
parameters in a fixed compact set are allowed simultaneously at all primes
of norm at most `(log D)^2`, at subpower cost.

This is a statement for the actual row vector, rather than for a model with
independent row characters. The right side of (4) is an upper bound obtained
by a particular absolute convolution argument; it is not asserted to be a
lower bound for the arithmetic moment.

## 2. Exact convolution and proof

Define a multiplicative function `b` by

\[
 b(1)=1,\qquad
 b(\mathfrak p^j)=
 \begin{cases}
 (z_{\mathfrak p}-1)(-1)^{j-1},&\mathfrak p\in P,\ j\ge1,\\
 0,&\mathfrak p\notin P,\ j\ge1.
 \end{cases}
 \tag{5}
\]

There is the exact ideal-divisor identity

\[
                  a_{\mathbf z,P}=b*\mu^2.
 \tag{6}
\]

Indeed, at a changed prime the formal power-series identity is

\[
 \left(1+\sum_{j\ge1}(z-1)(-1)^{j-1}v^j\right)(1+v)
             =1+zv;
 \tag{7}
\]

at every other prime it is `1(1+v)=1+v`. In particular (6) vanishes on
nonsquarefree ideals by cancellation. Keeping only squarefree divisors in
`b`, or removing repeated prime powers from (5), would destroy this identity.

Complete multiplicativity of the original presentation, including its zeros,
now gives the finite equality

\[
 V_{\mathbf z,P}(D;u)
  =\sum_{N\mathfrak d\le cD}
    \frac{b(\mathfrak d)\psi_u(\mathfrak d)
                    (N\mathfrak d)^{it}}{\sqrt{N\mathfrak d}}
        V_1(D/N\mathfrak d;u),
 \tag{8}
\]

where `c` is the fixed upper endpoint of the support of `W`.
There is no new condition `(d,m)=1` in (8). A nonunit of the original
presentation still has zero contribution on both sides.

For each fixed `d`, the factor `psi_u(d)(Nd)^{it}` is a row multiplier of
modulus at most one. Apply the row Hilbert-space triangle inequality and
(2), then extend the nonnegative scalar divisor sum to all ideals. Its
Euler product converges because it contains only finitely many primes:

\[
 \sum_{\mathfrak d}\frac{|b(\mathfrak d)|}{\sqrt{N\mathfrak d}}
 =\prod_{\mathfrak p\in P}
     \left(1+|z_{\mathfrak p}-1|
                \sum_{j\ge1}(N\mathfrak p)^{-j/2}\right).
 \tag{9}
\]

Summing the geometric series proves (4). The profile is the same `W` at
every residual scale, so its derivative order does not grow with `P`. The
norm height is also unchanged. No character is inferred from the artificial
sign pattern `p -> z_p`; it is only a coefficient. QED.

## 3. A growing prime range with a full parameter interval

Suppose `P` is any subset of the good primes of norm at most `Y`, and
`|z_p-1|<=B`, with fixed `B`. Elementary fixed-field prime counting gives

\[
 \sum_{N\mathfrak p\le Y}
      \frac1{\sqrt{N\mathfrak p}-1}
   \ll_F \frac{\sqrt Y}{\log(2Y)}+\log\log(3Y)+1.
 \tag{10}
\]

For a proof, replace the denominator by
`(Np)^(-1/2)+O_F((Np)^(-1))`, absorbing the finitely many smallest primes
separately. Degree-one primes are bounded by a fixed multiple of rational
primes and partial summation of the Chebyshev upper bound gives
`O_F(sqrt(Y)/log(2Y))`. Prime ideals of residue degree at least two and the
reciprocal-norm correction contribute `O_F(1+loglog(3Y))`. This proves (10)
without a new prime-ideal error term.

Thus (4) implies

\[
 \mathcal M_{\mathbf z,P}(U,D)
 \ll_\varepsilon U^{1+\varepsilon}(1+|t|)^{2A}p_J(W)^2
 \exp\!\left(C_{F,B}\left\{
        \frac{\sqrt Y}{\log(2Y)}+\log\log(3Y)+1\right\}\right).
 \tag{11}
\]

When `D` and `U` lie in the same prescribed bounded-power range and

\[
              \frac{\sqrt Y}{\log(2Y)}=o(\log D),
 \tag{12}
\]

the exponential is `D^{o(1)}`. In particular, for any fixed `delta>0`,

\[
             Y\le (\log D)^2(\log\log D)^{2-\delta}
 \tag{13}
\]

is admissible after harmless bounded-length conventions. The conclusion is
uniform for every collection of parameters in the fixed disk
`|z_p-1|<=B`; no Baire argument or interpolation is needed.

Taking a common `z_p=z` gives genuine fixed-interval control of
`mu^2(n) z^{omega_Y(n)}`, where `omega_Y` counts only primes in this growing
range. At `z=-1`, every such prime receives the Möbius sign. At `z=0`, every
column divisible by any prime in `P` is deleted. The latter is a useful scope
extension: for `Y=(log D)^2`, the product of all these primes need not have
bounded-power norm. It was never inserted into the character conductor or
into the source's licensed common-puncture parameter; (8) expands its effect
against the original admissible source.

This distinction must be retained when consuming (11). The theorem changes
coefficients, with its explicit convolution cost. It does not assert that
the original moment theorem itself admits arbitrary large punctures for
free.

## 4. The same stability estimate for an inverse anchor

There is a useful general form. Let the unmodified squarefree Euler factor
be `1+z_0 v`, with `|z_0|<=1`, and suppose a mean bound `Q(U,X)` has actually
been proved for that anchor on every residual scale `X<=cD`.
Replacing its coefficient at primes in `P` by `z_p` has local ratio

\[
 \frac{1+z_pv}{1+z_0v}
    =1+(z_p-z_0)\sum_{j\ge1}(-z_0)^{j-1}v^j.
 \tag{14}
\]

If `Q(U,X)<=Q_*(U,D)` throughout those scales, the identical proof gives

\[
 \|V_{\mathbf z,P}(D)\|
 \ll Q_*(U,D)^{1/2}
       \prod_{p\in P}
          \left(1+\frac{|z_p-z_0|}{\sqrt{Np}-|z_0|}\right),
 \tag{15}
\]

with the original losses, heights, and seminorms retained. At `z_0=-1` this
extends the already licensed native inverse estimate to arbitrary bounded
changes at all primes in (13), including deleting those primes. It does not
improve the exponent of that anchor; it extends its coefficient scope.

## 5. Polynomial prime marks do reach the HLC bands

There is a stronger conclusion for a fixed number of marks than for a fixed
coefficient deformation. Put

\[
 r_{\mathfrak p}=(\sqrt{N\mathfrak p}-1)^{-1},\qquad
 S_P=\sum_{\mathfrak p\in P}r_{\mathfrak p}.
 \tag{16}
\]

Let `e_k(r_p:p in P)` be the elementary symmetric polynomial, with `e_0=1`
and `e_k=0` if `k>#P`. Write `(omega_P)_k` for the falling factorial.

**Theorem 2 (actual prime marks).** For every integer `k>=0`, the ordinary
squarefree column with coefficient `mu^2(n) (omega_P(n))_k` satisfies

\[
 \boxed{\displaystyle
 \|V_{(\omega_P)_k}(D)\|
 \ll_\varepsilon U^{1/2+\varepsilon}(1+|t|)^A p_J(W)
       k!e_k(r_p:p\in P)
 \le C_\varepsilon U^{1/2+\varepsilon}(1+|t|)^A p_J(W)S_P^k.}
 \tag{17}
\]

The constant, height order, and seminorm order do not depend on `k` or `P`.
They are the orders of the already fixed endpoint (2).
For a binomial mark `binom(omega_P,k)`, divide the explicit factor by `k!`.
For disjoint prime bands `P_i` and marks
`prod_i binom(omega_{P_i},k_i)`, the exact factor is
`prod_i e_{k_i}(r_p:p in P_i)`.

**Proof.** Put `z_p=1+h` in (5), so

\[
 b_h(d)=h^{\omega(d)}(-1)^{\Omega(d)-\omega(d)}
                  1_{\text{all prime divisors of }d\text{ lie in }P}.
 \tag{18}
\]

Differentiate the finite identity (8) exactly `k` times at `h=0`. The
derivative on the left has the asserted falling-factorial coefficient. On
the right it leaves precisely the ideals `d` having `k` distinct prime
divisors in `P`, with modulus `k!`. Each selected prime can have any positive
exponent; summing these prime powers with weight `(Nd)^(-1/2)` gives
`k! e_k(r_p)`. Apply the same endpoint and row triangle inequality. Finally
`k!e_k(r_p)<=S_P^k`, since expansion of the right side includes all ordered
distinct-prime tuples and additional nonnegative tuples. Independent
formal parameters for disjoint bands prove the multivariate assertion.
QED.

This is an arithmetic estimate for the *marked* coefficient, not a formal
differentiation of an inequality at one parameter value. The exact derivative
convolution is bounded separately. In particular every repeated prime power
in (18) is retained.

If every marked prime has norm at most
`Y=exp(O((log D)^a))`, with fixed `0<a<1`, then `log(2+S_P)=O(log Y)`.
Consequently (17) preserves row volume with arbitrarily small power losses
whenever

\[
                         k\log Y=o(\log D).
 \tag{19}
\]

This includes all fixed mark orders, and also growing orders
`k=o((log D)^{1-a})`. Thus a fixed interval of coefficient parameters needs
the smaller prime cutoff of Section 3, whereas a fixed number of genuine
prime marks reaches the HLC subpower bands. These are different proved
quantifiers.

### The actual finite damping polynomials

For a band `P_i`, define the truncation used in a binomial expansion of the
HLC mark by

\[
 B_{i,R}(n)=\frac1{V_i}\sum_{j=1}^{R}
             j(\rho-1)^{j-1}\binom{\omega_{P_i}(n)}j,
 \qquad 0<\rho<1.
 \tag{20}
\]

This is a finite polynomial. It agrees with the entire mark
`omega_{P_i} rho^(omega_{P_i}-1)/V_i` whenever `omega_{P_i}<=R`.
For disjoint bands, Theorem 2 and the triangle inequality give the exact
usable cost

\[
 \left\|V_{\prod_i B_{i,R_i}}(D)\right\|
 \ll_\varepsilon U^{1/2+\varepsilon}(1+|t|)^A p_J(W)
 \prod_i\left[
   \frac1{|V_i|}\sum_{j=1}^{R_i}
        j|\rho-1|^{j-1} e_j(r_p:p\in P_i)\right].
 \tag{21}
\]

For the HLC bands, whose prime norms are at most `exp(O((log D)^{1/5}))`,
take `R_i=O((log D)^{1/2})`. If the number of bands is `O(loglog D)` and
the nonzero `V_i` and their reciprocals are bounded, the logarithm of the
entire displayed cost is

\[
            O\bigl((\log D)^{7/10}\log\log D\bigr)=o(\log D).
 \tag{22}
\]

Indeed `e_j<=S_i^j/j!` and the logarithm of each finite sum is at most
`O(R_i log(2+S_i)+log(R_i+1))`; here `log(2+S_i)=O((log D)^{1/5})`.
This proves a family mean for the actual finite polynomial marks on the
paper's prime scales. The proof does not insert the product of all those
primes into a character presentation or a source modulus.
Here the marks are over prime ideals in the native Eisenstein family,
using the paper's band-size pattern `exp((log D)^{a_i})`,
`1/10<a_i<1/5`. No transfer of the rational shifted-prime probability law
to those ideals is being asserted.

The same argument applies to an inverse anchor in Section 4. Differentiating
at `z_0=-1` replaces the falling-factorial coefficient by its product with
the original Möbius sign and an overall sign of modulus one. Thus the source
native inverse exponent remains valid after these polynomial marks, with
the same explicit subpower cost. This is an extension of coefficient scope;
it does not decrease that exponent.

### Why (21) does not yet imply the full damped estimate

The difference between the actual damping factor and (20) is supported
where `omega_{P_i}>R_i`, but a source-faithful power estimate for its complete
physical row vector is still required. The scalar factorial-tail errors
used for logarithmic accuracy in the HLC paper do not automatically beat a
fixed-power large-sieve loss. In particular `R~(log D)^{1/2}` gives factorial
decay of logarithmic size `-O((log D)^{1/2}loglog D)`, which is subpower in
`D`. No all-row remainder theorem is proved here by that observation.

## 6. What happens to a full fixed deformation on the HLC bands

The HLC paper uses bands around `exp((log D)^a)` for a fixed positive `a`.
They are asymptotically much larger than (13). For the absolute adapter (4),
even its prime-divisor contribution already prevents a subpower coefficient
cost on such a band. If `|z_p-1|` is a fixed positive constant and a band
contains all prime ideals in a fixed multiplicative interval near `Y`, the
fixed-field prime ideal theorem gives

\[
 \log\prod_{p\in P}
      \left(1+\frac{|z_p-1|}{\sqrt{Np}-1}\right)
              \asymp_{F,B} \frac{\sqrt Y}{\log Y}.
 \tag{23}
\]

Equation (23) describes the cost of this full Euler-product upper bound,
not a lower bound for the truncated divisor sum or for the row moment.
Truncating (8) may lower that cost, and retaining its signs may lower it much
more; neither improved estimate is provided by (4).

The present theorems therefore supply actual growing-prime coefficient
control and HLC-scale polynomial marks, but they do not estimate the full
damping remainder with the fixed-power strength needed by the native
consumer.

## 7. Other routes tested in this pass

The new 25-October PR #1021 packet already controls the full parameter `z`
in a power-thin window around one. Its degree/extrapolation cost does not
permit reaching `z=-1`. Formula (4) controls a fixed parameter range, but
only a growing initial prime segment; these two quantifiers cannot be
interchanged.

The initial uncapped buffered-bin calculation does not give an exponent
improvement. In the source density calculation, writing `delta=2a-1`, its
above-floor row exponent is

\[
 R(a)=\frac{31-32a}{21-12a}\quad(a\le11/12),
 \qquad R(a)=2(1-a)\quad(a\ge11/12).
 \tag{24}
\]

Even the optimistic small-fractional-parameter limit costs
`R(a)+(2a-1)r` at column length `D=U^r`. For `1<=r<=3/2`, the maximum on
the first branch is

\[
 E(r)=\frac83+\frac{5r}{2}-\frac{10}{\sqrt6}\sqrt r.
 \tag{25}
\]

It obeys the exact identity

\[
 E(r)-\frac{1+5r}{6}
       =\frac53\left(\sqrt r-\sqrt{3/2}\right)^2\ge0.
 \tag{26}
\]

Thus even the first branch is tangent to, and never below, the existing
inverse exponent on that interval **without an additional cap on the bin
locations**. The high bins make the uncapped calculation worse: maximizing
`2(1-a)+(2a-1)r` over `11/12<=a<=1` gives `r` for `r>=1`. The uncapped
optimistic envelope is therefore at least `max(E(r),r)`. This is a statement
about that calculation, not a claim that the repository has no relevant
family cap.

In fact the pinned OpenAI `thm:main` asserts the stronger source-qualified
premise that **every finite-order Hecke L-function over the Eisenstein field**
is zero-free in `Re s>7/8`. That is the appropriate cap for this finite-order
family; a claim only about ordinary zeta would not suffice. Retaining this
premise changes the maximum to `2/7+3r/4` once `r>=200/147`, and it beats
the old inverse exponent once `r>10/7`.

The companion `CAPPED_NATIVE_MOMENT.md` completes an actual estimate at
this capped exponent. Its proof uses the buffered zero-free rectangle and
a three-circles estimate for the holomorphic logarithm to shift the
**original inverse directly**. Fractional interpolation and slit-contour
cuts are unnecessary. Thus the uncapped failed feedback is superseded,
at that explicitly stronger source-dependent scope, by a genuine native
long-length gain. The all-family cap and polynomial-height buffered row
count remain load-bearing imported premises.

The positive analytic results of this note are (4) and (17), with their
growing-prime and actual finite-mark consequences. The companion adds the
native long-length moment improvement. Neither note establishes a new RH
or global zero-free claim; the complete detector consumer still has to be
assessed with the exact length location of that gain.
