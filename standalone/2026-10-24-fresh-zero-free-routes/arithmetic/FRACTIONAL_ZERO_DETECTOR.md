# Fractional coefficients turn zeros into mild branch points

Status: proved local and Mellin-transfer lemmas; the averaged slit-contour estimate is an open research target.
Scope: one fixed number field and one fixed nonprincipal finite-order Hecke character in Sections 1–3; the same proof allows any unitary character whose L-function is entire. Pure norm twists of the principal character require their pole to be treated separately. Section 4 is a conditional exponent calculation for a varying family.
Exact sources: ordinary Hecke analytic continuation and Euler products; Xu–Sang [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Theorem 2.2 for the source-dependent ordinary moment framework and Theorem 1.2 for the density formula. The latter is stated only for `51/100<sigma<=7/8`, polylogarithmic heights, fixed omissions, and its specified indexed sextic family. Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), Theorem 12.14 and Sections 14.2–14.3 provide related general-field moment context.
What was actually run: exact rational identities for the density envelope and numerical evaluations of that explicit scalar envelope. No contour theorem was tested or certified numerically.
Smallest remaining gap: bound the complete branch-cut contribution in the correct family mean, with all conductors, heights, multiplicities, masks, and contour profiles retained.

## 1. A softened squarefree coefficient

Let `psi` be a fixed nonprincipal finite-order Hecke character, with its usual
zero values at omitted primes. For `0<z<1`, define on integral ideals

\[
 a_z(n)=\mu^2(n)z^{\omega(n)}\psi(n).
\]

In the absolutely convergent half-plane `Re s>1`,

\[
 F_z(s)=\sum_n\frac{a_z(n)}{(Nn)^s}
       =\prod_p(1+z\psi(p)(Np)^{-s})
       =L(s,\psi)^z H_z(s),                         \tag{1}
\]

where the power is initially determined by the Euler-product logarithm
and

\[
 H_z(s)=\prod_p (1+z u_p)(1-u_p)^z,
 \qquad u_p=\psi(p)(Np)^{-s}.                       \tag{2}
\]

**Lemma 1.** `H_z` has a single-valued holomorphic nonvanishing
continuation to `Re s>1/2`.

**Proof.** For `Re s>0`, `|u_p|<1` and `|z u_p|<1`, so the logarithms
in (2) have their canonical power-series branches. Their linear terms
cancel:

\[
 \log(1+zu)+z\log(1-u)=O_z(|u|^2).
\]

The sum over prime ideals converges absolutely and locally uniformly
for `Re s>1/2`. Its exponential is holomorphic and never zero. A prime
where `psi(p)=0` contributes one. QED.

The restriction `0<z<1` avoids even finite-prime zeros in the
correction. It is not an approximation to the coefficient.

## 2. A single irrational parameter detects every zero multiplicity

**Lemma 2 (monodromy detector).** Let `1/2<=b<1` and let `z in (0,1)` be
irrational. If `F_z`, initially defined by (1), has a single-valued
holomorphic continuation throughout `Re s>b`, then `L(s,psi)` has no
zero there.

**Proof.** Suppose `rho` is a zero of positive integer multiplicity `m`
in that half-plane. In a sufficiently small disk,

\[
 L(s,\psi)=(s-\rho)^m g(s), \qquad g(\rho)\ne0.
\]

Analytic continuation of the germ (1) once around `rho` multiplies it
by `exp(2 pi i m z)`. The nonvanishing correction `H_z` and the local
nonzero factor `g` contribute no monodromy. Since `m z` is not an
integer, the multiplier is not one. This is incompatible with a
single-valued holomorphic continuation. QED.

For rational `z=a/q` in lowest terms, the same argument only forces
the multiplicity of every surviving zero to be divisible by `q`.
There is no reason to replace that weaker conclusion by zero-freeness.

**Lemma 3 (smoothed-sum version).** Retain `1/2<=b<1` and an irrational
`z in (0,1)` as in Lemma 2. Let `W` be any nonzero smooth
compactly supported function on `(0,infinity)`. Put

\[
 S_z(X)=\sum_n a_z(n)W(Nn/X).
\]

If for every `epsilon>0`,

\[
 S_z(X)\ll_{\epsilon,W,\psi,z}X^{b+\epsilon}
       \qquad(X\ge1),                              \tag{3}
\]

then `L(s,psi)` is zero-free for `Re s>b`.

**Proof.** The Mellin integral of `S_z(X)` converges locally uniformly
for `Re s>b`, using (3) with a smaller epsilon on any compact set.
The bounded lower range causes no singularity; `S_z(X)=0` for all
sufficiently small `X`. In `Re s>1`, absolute convergence gives

\[
 \int_0^\infty S_z(X)X^{-s}\frac{dX}{X}
       =F_z(s)\widehat W(s),
 \qquad \widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx.  \tag{4}
\]

The left side continues holomorphically to `Re s>b`. At a putative
zero `rho`, `widehat W` has some finite nonnegative integer zero order
`k`, since it is entire and is not identically zero. The right side
has local fractional order `m z+k`, still nonintegral. The same
monodromy contradiction applies. In particular there is no need to
choose a smoothing whose Mellin transform avoids the unknown zero.
QED.

These statements use a nonprincipal character so there is no
fractional pole at `s=1`. For a principal character, that branch at the
known pole must be subtracted or excluded explicitly. It cannot be
called a zero obstruction. The lemmas are not a new zero-free bound:
they identify precisely what a successful fractional-coefficient
estimate would establish.

## 3. Even one coefficient derivative sees the zeros

The infinitesimal version is useful because it replaces an inverse
pole by a milder logarithmic singularity. At `z=1`,

\[
 F_1(s)=\frac{L(s,\psi)}{L(2s,\psi^2)}.
\]

Differentiation of the absolutely convergent Euler product gives

\[
 D(s):=\sum_n\frac{\mu^2(n)\omega(n)\psi(n)}{(Nn)^s}
     =F_1(s)\{\log L(s,\psi)+h(s)\},               \tag{5}
\]

where

\[
 h(s)=\sum_p\left\{
      \frac{u_p}{1+u_p}+\log(1-u_p)\right\}          \tag{6}
\]

is holomorphic for `Re s>1/2`, since its local linear terms cancel.
Here `log L` denotes continuation of the Euler-product germ, not an
assumed global logarithm across its zeros.

At a zero of multiplicity `m`, the singular part of (5) is a nonzero
analytic multiple of

\[
 (s-\rho)^m m\log(s-\rho).                         \tag{7}
\]

Going once around the zero adds `2 pi i m F_1(s)`, which is not
identically zero in a punctured disk. Therefore a bound of the form
(3) for the **single marked coefficient** `mu^2(n) omega(n) psi(n)`
also forces zero-freeness in `Re s>b`, by exactly the Mellin argument
above. A zero of the Mellin smoothing does not cancel the logarithm.

This identifies a concrete new target: control a complete ordinary
character sum with one `omega(n)` mark. A formal differentiation of a
fixed-parameter bound is not such a proof. Nor does the exact divisor
identity for `omega` make its long-prime contribution small. The
possible advantage is analytic: the unknown zero creates a vanishing
logarithmic branch (7), rather than the blow-up of `1/L`.

There is a related caution for perturbative arguments. For each fixed
noninteger `z` near one, the local branch has exponent `m z`. Its
amplitude tends to zero as `z` tends to one, but its location and its
real-part exponent do not move. Consequently an `O(|z-1|)` coefficient
perturbation does not automatically give an `O(|z-1|)` improvement in a
length exponent.

## 4. A family mean may absorb branches: exact exponent test

The fixed-row lemma does **not** rule out a useful family mean. A
small collection of exceptional rows can have large individual branch
terms while their total remains acceptable. Here is a quantitative
test before trying to prove the full contour argument.

Suppose that, on a family of physical row scale `Q`, the number of rows
with a relevant low-height zero of real part at least `sigma` has the
bound `Q^(R(sigma)+epsilon)`, with

\[
 R(\sigma)=\frac{31-32\sigma}{21-12\sigma}
          =\frac83-\frac{25}{21-12\sigma},
 \qquad \frac12\le\sigma\le B_\flat.               \tag{8}
\]

For the calculation down to `sigma=1/2`, (8) is an **optimistic algebraic
extension of the source's formula**. Xu–Sang's actual Theorem 1.2 starts
at `sigma>51/100`, and its `Q` is the physical sixth-power-free index
norm rather than the primitive conductor alone. A proof using that
source must also cover the intervening near-critical strip and retain
the physical row multiplicities, height range, and fixed exclusions.
Equation (8) must not be cited as a proved estimate on the enlarged
interval or for arbitrary moving twists.
Suppose also that the complete family has a suitable fourth moment
`sum |L|^4 << Q^(1+epsilon)` at the points needed in the contour. For
`0<z<=2`, Holder gives on that exceptional set

\[
 \sum_{\rm exceptional}|L|^{2z}
       \ll Q^{(1-z/2)R(\sigma)+z/2+\epsilon}.        \tag{9}
\]

If a normalized branch term has length multiplier
`X^(sigma-1/2)`, write `X=Q^r`. Ignoring only subpower factors, its
candidate squared-mean exponent is then

\[
 E_{r,z}(\sigma)
   =(1-z/2)R(\sigma)+z/2+r(2\sigma-1).              \tag{10}
\]

Equation (10) is an implication of the **stated model inputs**. It
does not prove that a slit-contour representation has no additional
conductor, height, multiplicity, or cut-overlap costs. Those are
essential unresolved analytic requirements.

Put `a=1-z/2`. Since

\[
 R'(\sigma)=-\frac{300}{(21-12\sigma)^2},
 \qquad R''(\sigma)<0,
\]

the volume threshold `max E<=1` holds precisely when

\[
 r\le\frac{2a}{3}.                                \tag{11}
\]

Indeed `E(1/2)=1` and `E'(1/2)=-4a/3+2r`; concavity proves both
directions. In the limiting sparse-coefficient regime `z -> 0+`, this
allows `r<=2/3`. The limiting interval does not include `z=0` as a
nontrivial coefficient theorem: at exactly zero only the unit ideal
remains. Any application requires a positive nondegenerate interval.

When the critical point lies inside `(1/2,B_flat)`, the exact maximum is

\[
 E_{\max}(r,z)=\frac z2+\frac{8a}{3}
                  +\frac{5r}{2}
                  -\frac{10}{\sqrt6}\sqrt{ar},      \tag{12}
\]

and its location satisfies `21-12 sigma=sqrt(150a/r)`. If this point
is beyond `B_flat`, evaluate (10) at that endpoint instead.

At the optimistic limit `z=0`, `r=8/9`, the value is about `1.039887`.
Thus even the optimistic density envelope still pays a fixed loss in
a rectangle of that shape; it does not give a row-volume theorem
there. At `r=2/3`, the limiting maximum is exactly one. This suggests
a possible shorter-column range to investigate, conditional also on
closing the near-critical strip omitted by the published statement.
It is not an achieved fractional-coefficient mean.

### The exact deficit at the native `4/5` target

The raw native target of the companion note has envelope

\[
 T(r)=\max\{1,\tfrac16+\tfrac45r\},
 \qquad 1\le r\le\tfrac32.
\]

In the optimistic `z->0+` branch model, requiring
`R(sigma)+(2sigma-1)r<=T(r)` throughout this range is equivalent to

\[
 R(\sigma)\le1-\frac{25}{24}(2\sigma-1).            \tag{13}
\]

Indeed `T` changes branch at `r=25/24`. Since
`0<=2sigma-1<=3/4<4/5`, the minimum of
`T(r)-(2sigma-1)r` on the full range is exactly at that corner.
At `sigma=3/4`, the current density formula is `7/12`, whereas the
right side of (13) is `23/48`: the deficit is exactly `5/48`.
This is also the maximum deficit on the interval, because the
derivative vanishes there and `R` is concave.

This exact comparison is useful for selecting the next experiment:
independent zero counts plus absolute branch bounds are substantially
too weak at an interior zero class. A successful native continuation
proof needs stronger joint zero/value control or signed cancellation
among the branch contributions, rather than only parameter tuning of
the quoted density formula.

## 5. What the combination would accomplish

The continuation theorem in `COEFFICIENT_CONTINUATION.md` can turn a
family estimate on a nondegenerate interval of softened coefficients
into the missing Mobius/no-Mobius coefficient estimate, at subpower
cost. Section 4 shows how rare zero branches might be controlled in
mean even though Section 2 forbids assuming pointwise control.

The exact next attempt is therefore:

1. Keep the physical family, original zeros, and complete conductor
   presentation fixed.
2. Derive an honest slit-contour formula for its fractional ordinary
   coefficients, including the principal-character branch separately.
3. Prove the mean of every cut contribution in the actual rectangle,
   using the appropriate joint zero-density/value information.
4. Apply coefficient continuation to the centered moment, and only
   then assemble the full inverse consumer.

Steps 2–4 have not been completed here. The result of this packet is a
proved coefficient-transfer mechanism, a precise softer zero detector,
and an explicit test of one possible density input. It does not turn
the inherited `B_flat` into a smaller unconditional boundary.
