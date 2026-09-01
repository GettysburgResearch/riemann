# Invariant order product, count law, and a radial determinant criterion

Status: **PROPOSED EXACT IDENTITIES AND RH-EQUIVALENCES; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This note extracts new leverage from the invariant coordinate introduced in
[`03_E_WIDDER_SCALAR_ENDPOINT.md`](03_E_WIDDER_SCALAR_ENDPOINT.md).  The
E–Widder numbers are not merely high derivatives: after one normalization
they are the power traces of an explicit transformed zero multiset.  Their
order-generating product is a radial quotient of the invariant xi function.
Independently, the positive coefficients of the same invariant entire
function define a genuine integer-valued count law.  RH is equivalent to that
one count law being Poisson-binomial, or equivalently quasi-free, at one
positive scale.

The identities below are unconditional.  Their positivity conclusions are
carefully separated from the still-open all-order theorem.

## 1. The invariant entire function has strictly positive coefficients

Retain

\[
 \mathfrak X(s(s-1))=\xi_{\rm R}(s).
\]

Let

\[
 \psi(t)=\sum_{m\ge1}e^{-\pi m^2t}.
\]

The standard split Mellin representation of completed xi gives, for every
complex `u`,

\[
 \boxed{
 \mathfrak X(u)
 =\frac12
 +u\int_1^\infty
 \psi(t)t^{-3/4}
 \cosh\left(
  \frac{\log t}{2}\sqrt{u+\frac14}
 \right)dt.
 }
 \tag{1.1}
\]

For `tau>=0`, write

\[
 \cosh\left(\tau\sqrt{u+\frac14}\right)
 =\sum_{n\ge0}b_n(\tau)u^n.
\]

Expanding first in powers of `u+1/4` and then in powers of `u` gives

\[
 \boxed{
 b_n(\tau)
 =\sum_{r\ge0}
 \binom{n+r}{n}4^{-r}
 \frac{\tau^{2n+2r}}{(2n+2r)!}>0
 \qquad(\tau>0).
 }
 \tag{1.2}
\]

Equivalently,

\[
 \boxed{
 b_n(\tau)
 =\frac{\sqrt\pi}{2n!}
 \tau^{n+1/2}I_{n-1/2}(\tau/2),
 }
 \tag{1.3}
\]

where `I_nu` is the modified Bessel function.  The identity follows from the
standard `0F1` representation of `I_nu`.

Writing

\[
 \mathfrak X(u)=\sum_{n\ge0}c_nu^n,
\]

(1.1)--(1.2) show

\[
 \boxed{c_n>0\qquad(n\ge0).}
 \tag{1.4}
\]

In particular, for every `v>0`,

\[
 \boxed{
 P_v(z)=\frac{\mathfrak X(vz)}{\mathfrak X(v)}
 =\sum_{n\ge0}p_n(v)z^n,
 \qquad
 p_n(v)=\frac{c_nv^n}{\mathfrak X(v)},
 }
 \tag{1.5}
\]

is the probability-generating function of an integer-valued random variable
`N_v`.

## 2. A one-scale Pólya-frequency and Poisson-binomial criterion

The entire function `mathfrak X` has order at most `1/2`.  The
Aissen--Schoenberg--Whitney--Edrei theorem therefore gives the following exact
criterion.

### Theorem 2.1 — one-scale count criterion

For any fixed `v>0`, the following are equivalent:

1. RH;
2. the coefficient sequence `(p_n(v))_(n>=0)` is `PF_infinity`;
3. `N_v` is a possibly infinite Poisson-binomial count;
4. there is a positive trace-class contraction `K_v` such that
   
   \[
    \boxed{
    P_v(z)=\det(I-K_v+zK_v).
    }
    \tag{2.1}
   \]

If one of these statements holds for one `v>0`, it holds for every `v>0`.

#### Proof

Under RH, write the invariant zeros as `-a_j`, with `a_j>0` and
`sum_j a_j^(-1)<infinity`.  The genus-zero product gives

\[
 P_v(z)
 =\prod_j\frac{1+vz/a_j}{1+v/a_j}
 =\prod_j(1-p_j+p_jz),
 \qquad
 p_j=\frac{v}{v+a_j}\in(0,1),
 \tag{2.2}
\]

and `sum_j p_j<infinity`.  This is a Poisson-binomial pgf and is the Fredholm
determinant of the diagonal contraction with eigenvalues `p_j`.

Conversely, a `PF_infinity` sequence has an Edrei generating function.  Here
the generating function is entire of order below one and has nonzero constant
term, so the denominator and exponential factors in the general Edrei form
are absent.  Every zero is therefore negative real.  The same conclusion is
immediate from (2.1), whose zeros are

\[
 z=-\frac{1-\kappa}{\kappa}\le0
\]

for the nonzero eigenvalues `kappa` of `K_v`.  Since the zeros of `P_v` are
`-a_j/v`, all invariant zeros `-a_j` are negative real, which is RH by the
invariant-coordinate theorem.  `square`

This criterion is genuinely one-scale.  It does not require a limit in `v`,
a finite packet, or a choice of zero ordinate.

## 3. E–Widder quantities are transformed power traces

Let `a` run over one invariant zero for each functional-equation orbit, with
multiplicity and conjugation.  Without assuming RH,

\[
 q(u)=2\sum_a\frac1{u+a}.
\]

Define

\[
 \boxed{
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
 }
 \tag{3.1}
\]

The diagonal E–Widder identity gives

\[
 \mathcal W_k(u)
 =2(2k-1)!\sum_a\frac{a^k}{(u+a)^{2k}}.
\]

Hence the normalization

\[
 \boxed{
 C_k(u)=
 \frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u)
 }
 \tag{3.2}
\]

satisfies the unconditional exact formula

\[
 \boxed{
 C_k(u)=\sum_a\lambda_u(a)^k.
 }
 \tag{3.3}
\]

Conjugation makes the sum real.  Under RH, `a>0` and

\[
 \lambda_u(a)
 =\frac{4ua}{(u+a)^2}
 =\operatorname{sech}^2\left(\frac12\log\frac au\right)
 \in(0,1].
 \tag{3.4}
\]

Thus the E–Widder hierarchy is the positivity of every power trace of the
transformed invariant zero multiset, at every positive scale.

For complex `a`, choose a logarithm locally.  The same map has the exact
complex-hyperbolic form

\[
 \boxed{
 \lambda_u(a)
 =\operatorname{sech}^2\left(
  \frac12\log\frac au
 \right).
 }
 \tag{3.5}
\]

This is the spectral microscope seen in the previous pass.

## 4. Exact order-generating product

For a nonzero complex parameter `r`, put

\[
 \boxed{
 w=-\frac{(r-1)^2}{4r}
   =\frac{2-r-r^{-1}}4.
 }
 \tag{4.1}
\]

A direct calculation gives, for every invariant atom,

\[
 \boxed{
 1-w\lambda_u(a)
 =\frac{(a+ur)(a+u/r)}{(a+u)^2}.
 }
 \tag{4.2}
\]

Multiplication over the genus-zero product yields the central new identity

\[
 \boxed{
 \Delta_u(w)
 :=\prod_a(1-w\lambda_u(a))
 =\frac{\mathfrak X(ur)\mathfrak X(u/r)}
        {\mathfrak X(u)^2}.
 }
 \tag{4.3}
\]

The product converges normally near `w=0`, because
`sum_a |lambda_u(a)|<infinity` for fixed `u>0`.

Taking a logarithmic derivative gives the order-generating function

\[
 \boxed{
 \mathscr C_u(w)
 :=\sum_{k\ge1}C_k(u)w^{k-1}
 =-\frac{\Delta_u'(w)}{\Delta_u(w)}
 =\frac{2u\,[r^2q(ur)-q(u/r)]}{r^2-1}.
 }
 \tag{4.4}
\]

Thus all E–Widder orders are encoded in one radial two-point quotient of the
same invariant logarithmic derivative.

## 5. Unit-circle form and radial phase current

Take

\[
 r=e^{i\theta},
 \qquad
 w=\sin^2(\theta/2),
 \qquad 0\le\theta\le\pi.
\]

Because `mathfrak X` has real coefficients,

\[
 \boxed{
 \Delta_u(w)
 =\frac{|\mathfrak X(ue^{i\theta})|^2}{\mathfrak X(u)^2}.
 }
 \tag{5.1}
\]

The positive coefficients (1.4) give the unconditional triangle inequality

\[
 \boxed{
 0\le\Delta_u(w)\le1
 \qquad(u>0,\ 0\le w\le1).
 }
 \tag{5.2}
\]

Where the denominator in (4.4) is nonzero,

\[
 \boxed{
 \mathscr C_u(w)
 =\frac{2u}{\sin\theta}
  \Im\bigl(e^{i\theta}q(ue^{i\theta})\bigr)
 =\frac{4u}{\sin\theta}
  \frac{d}{du}\arg\mathfrak X(ue^{i\theta}).
 }
 \tag{5.3}
\]

This is a radial phase-current formulation of the complete Widder hierarchy.
The all-order source inequality is equivalent to every Taylor coefficient of
this current at `w=0` being nonnegative for every `u>0`.

## 6. Unconditional positive radial potential

On every zero-free subinterval of `0<=w<=1`, define

\[
 \mathcal V_u(w)=-\log\Delta_u(w).
\]

Equation (5.2) gives

\[
 \boxed{\mathcal V_u(w)\ge0.}
 \tag{6.1}
\]

Near `w=0`, (4.3) gives

\[
 \boxed{
 \mathcal V_u(w)
 =\sum_{k\ge1}\frac{C_k(u)}k w^k.
 }
 \tag{6.2}
\]

Consequently the Riemann data satisfy an unconditional all-order *averaged*
positivity theorem:

\[
 \boxed{
 \sum_{k\ge1}\frac{C_k(u)}k w^k\ge0
 }
 \tag{6.3}
\]

through the first zero/pole barrier of the order product.

This is new leverage but not the desired coefficientwise theorem.  A
nonnegative analytic function can have negative Taylor coefficients.  The
missing strengthening is absolute monotonicity of `mathcal V_u`, or
equivalently nonnegativity of every `C_k(u)`.

## 7. A single off-line invariant zero creates an interior order pole

Let

\[
 a=|a|e^{i\alpha},
 \qquad 0<|\alpha|<\frac\pi2,
\]

be a nonreal invariant zero parameter.  Choose

\[
 u=|a|,
 \qquad
 r=-e^{i\alpha}.
\]

Then `ur=-a`, and therefore `mathfrak X(ur)=0`.  The corresponding order
coordinate is

\[
 \boxed{
 w_a=\cos^2(\alpha/2)\in(1/2,1).
 }
 \tag{7.1}
\]

At this same scale,

\[
 \boxed{
 \lambda_u(a)=\sec^2(\alpha/2)=w_a^{-1}>1.
 }
 \tag{7.2}
\]

Thus `Delta_u` has an interior zero and `mathscr C_u` has an interior pole.
Conjugate and repeated atoms add their multiplicities; they do not cancel the
pole.

Under RH every `a` is positive real, every `lambda_u(a)` lies in `(0,1]`, and
all poles of `mathscr C_u` lie on `[1,infinity)`.  Hence

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathscr C_u(w)\text{ is holomorphic for }|w|<1
 \text{ for every }u>0.
 }
 \tag{7.3}
\]

This is an order-variable analogue of the earlier safe-line interior-pole
criterion.  It detects an off-line zero at its canonical invariant modulus,
without a large-order limit.

A subtle point is important: at the matching scale (7.2), the offending atom
contributes *positively* to every power trace.  The eventual negative Widder
coefficient occurs at a nearby scale where `lambda_u(a)` rotates.  The pole
criterion and the coefficient criterion are equivalent globally in `u`, but
not atom-by-atom at the matching point.

## 8. Exact leverage and exact remaining theorem

The new formulation separates three increasingly strong statements:

```text
positive coefficients of mathfrak X
    => 0 <= Delta_u(w) <= 1 on the radial real interval;

RH
    <=> no interior order pole for any u;

RH
    <=> every coefficient C_k(u) is nonnegative for every u.
```

The first is unconditional.  The second is a sharp holomorphy detector.  The
third is the E–Widder source inequality.

The next proof mechanism should therefore not differentiate the Euler series
order by order.  It should construct one of the following directly from the
source:

1. a positive trace-class contraction `K_u` with
   
   \[
    \Delta_u(w)=\det(I-wK_u);
   \]
2. a positive measure `sigma_u` on `[0,1]` with
   
   \[
    C_k(u)=\int_0^1\lambda^k\,d\sigma_u(\lambda);
   \]
3. an absolute-monotonicity proof for `-log Delta_u(w)` on the unit interval;
4. a source-side proof that the count law `N_u` is Poisson-binomial.

Any one of these closes Architecture E and proves RH.  The next note gives an
explicit theta-source decomposition of `N_u` into quasi-free fibers and names
the precise mixing theorem still required.

## 9. Review checklist

Independent review should verify:

1. the split xi integral and every normalization in (1.1);
2. coefficient positivity and the Bessel identity (1.3);
3. the one-scale ASWE/Edrei converse;
4. the factor `4u` in `lambda_u(a)`;
5. the algebraic cross-ratio identity (4.2);
6. normal convergence of the product (4.3);
7. both factors in the logarithmic-derivative formula (4.4);
8. the phase-current normalization in (5.3);
9. the distinction between radial-potential positivity and coefficientwise
   positivity;
10. the no-cancellation interior-pole statement.

The companion exact checker
[`verify_order_product_and_reciprocal.py`](verify_order_product_and_reciprocal.py)
contains finite Gaussian-rational controls for (4.2)--(4.3), the matching pole,
and the radial modulus inequality.
