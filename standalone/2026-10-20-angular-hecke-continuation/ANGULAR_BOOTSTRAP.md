# Closing the angular family at Liu's refined boundary

Date: 20 October 2026.

Status: proposed source-dependent analytic theorem. This note supplies the
family and quantifier argument after the new angular theta, inverse-moment,
and product-moment adapters. It imports the explicitly identified estimates
and scalar comparison of Baiying Liu's preprint; it is not an independent
certification of the complete upstream proof.

Source: [Baiying Liu, arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1).
The immutable PDF digest is
5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5.

## 1. The correct family supremum

Fix a number field \(F\supset\mu_{12}\). Let \(\Lambda\) be the unitary
character in source Lemma 4.2, with complex angular vector
\(\lambda=(\lambda_v)_{v\mid\infty}\), \(\lambda_v\in\{-1,1\}\).
The sign convention is the ideal-character convention of that lemma.

Let \(\Omega\) be an actual unitary Hecke character of \(F\), with pure
angular infinity type

\[
 \Omega_\infty(z)=\prod_{v\mid\infty}(z_v/|z_v|)^{a_v},
 \qquad a_v\in\mathbb Z.
 \tag{1.1}
\]

Changing between the idelic and ideal-character conventions reverses all
these signs together and does not affect the following condition:

\[
 \mathbb Z a\cap\{\lambda,-\lambda\}=\varnothing.
 \tag{1.2}
\]

Since every coordinate of \(\lambda\) is \(1\) or \(-1\), condition (1.2)
is equivalent to \(a\notin\{\lambda,-\lambda\}\).
Indeed, \(na_v=\pm\lambda_v\) forces the integer \(n\) to divide one.

Define the full arithmetic family

\[
 \mathcal A_\Omega(F)
 =\{\Omega^h\xi:
       h\in\mathbb Z,\quad
       \xi\text{ a finite-order Hecke character of arbitrary conductor}\}.
 \tag{1.3}
\]

Let \(\beta_\Omega(F)\) be the supremum of the real parts of its nontrivial
zeros. Norm twists are included by translating the imaginary coordinate;
they do not change this supremum. Principal poles are excluded.

This is deliberately larger than the group of fixed coefficient
characters unramified outside a chosen finite set \(S\).
The moving Kummer characters in a moment can ramify outside \(S\).
Every use below of a zero-free premise refers to (1.3).

If \(a=0\), the pure angular character \(\Omega\) has finite order,
so (1.3) is the already covered finite-order family. In the new
angular argument below assume \(a\ne0\). Then \(h\mapsto ha\) is
injective, as used to identify the finite realized exceptional
character lists in the product moment.

### Theorem

Under the upstream analytic inputs identified in the companion adapters,

\[
 \boxed{\quad
 L_F(s,\Omega^h\xi)\ne0
 \quad\text{for every }h\in\mathbb Z,\ \xi\text{ finite order},\
 \operatorname{Re}s>B_\flat .
 \quad}
 \tag{1.4}
\]

Here \(B_\flat\) is the root in \((0.8748,0.8750)\) of

\[
 133488B^4-376596B^3+384534B^2-167541B+26231=0,
 \qquad B_\flat=0.874886647039964\ldots .
 \tag{1.5}
\]

The assertion concerns an open half-plane. A principal simple pole at one
is permitted. Analytic constants can depend on \(F,\Omega,h,\xi\), and
the chosen finite data. No bound uniform in a growing angular weight is
asserted.

## 2. What changes in the analytic comparison

The proof uses the numerical exponents of source Sections 13 and 14.
Here are the actual analytic interfaces behind that reuse.

| Source object | Angular replacement and reason |
|---|---|
| The theta function, Sections 4--5 | At place \(v\), use the actual root-derivative vector of degree \(ha_v-\lambda_v\). At least one degree is nonzero by (1.2). Its Weyl rotation reverses that degree. The new Mellin multiplier has the same permitted strip and vertical exponent. |
| Inverse moments, Theorems 10.4 and 11.2 | The companion proof retains the cube-divisor coefficients and the separated terminal angular phases. The two transforms close in a finite conjugation and unit-twist orbit for each fixed target. |
| Ordinary product moment, Theorem 12.14 | The companion adapter retains the same two ordinary factors, complete prime annuli, common character, natural zeros, and moving radical width. Its prime-bound premise is \(\beta_\Omega(F)\le(1+\kappa)/2\). |
| Nonprincipal annular estimates, Lemma 13.1 | A fixed angular primitive Hecke function has the ordinary functional equation with fixed gamma shifts and is entire unless principal. Mellin shifts retain arbitrary large-length decay and polynomial height cost. |
| Direct compensated theta average, Section 13.2 | The finite-place table, selected-prime allocation, additive Gram sum, and norm scales are unchanged. The higher angular phases stay in the separated row, column, and tuple coefficients. The replacement radial profiles have all the same decay and finite-seminorm properties. |
| Principal correction, Section 13.3 | Its identities are polynomial identities in the target phases. The estimates on pages 96--97 use \(|\eta(\mathfrak p)|=1\), not finite order. The identity-ray prime normalizer contains no angular target character. |
| Detector and prime amplitudes, Section 13.4 | Take a fixed finite list of presentations \(\Omega^h\theta\chi_u^{\pm1}\). To express a physical prime factor in one such presentation, its original coefficient gains \(\Omega^{-h}\theta^{-1}\), an allowed fixed coefficient in the angular product moment. |
| Reflected numerator, Section 14 | It remains \(L_F(w,\chi_u)\), where \(\chi_u\) is finite order. The approximate functional equation and the amplified numerator average do not acquire a new angular gamma factor. |

The angular theta argument is therefore an analytic change of input. The
subsequent scalar comparison does not posit a smaller moment exponent.

### 2.1 Fixed archimedean types do not add a power of the row length

For a fixed angular vector \(b=(b_v)\), the completed primitive Hecke
function has archimedean factors proportional to

\[
 \prod_{v\mid\infty}
      \Gamma\!\left(s+\frac{|b_v|}{2}\right).
 \tag{2.1}
\]

The ratio in ordinary reflection is correspondingly

\[
 \prod_{v\mid\infty}
  \frac{\Gamma(s+|b_v|/2)}
       {\Gamma(1-s+|b_v|/2)}.
 \tag{2.2}
\]

On fixed vertical strips its polynomial height exponent is unchanged by
the fixed shifts. Its reflected small-norm profile is no worse than the
spherical logarithmic bound used in source Lemma 12.6; a positive shift
only moves its left poles farther left. The finite family of fixed shifts
changes constants and required seminorm orders, not a norm exponent.

The analytic conductor may be written with the factor
\(\prod_v(1+|t|+|b_v|)^2\). In every individual moment application only
finitely many \(b_v\) occur. Thus the original polynomial dependence on
the norm-twist height remains valid, with fixed constants.

### 2.2 The positive prime normalizer survives

For target \(\eta=\Omega^h\xi\), keep exactly the finite compensated
operation in source (13.4). A selected prime contributes the scalar
\(\overline{\eta(\mathfrak p)}\) in its divisibility branch.
This is legal for any unitary phase.

At the principal residues, source (13.9) gives

\[
  G_{\mathfrak p}/H_{\mathfrak p}
      =-1+O((N\mathfrak p)^{-437/500})
 \tag{2.3}
\]

on the principal extraction box, uniformly in every target phase of
modulus one. The principal normalizer is

\[
 A_T(Z)=(-1)^K Z^{-\ell/6}
       \prod_{i=1}^{K}
       \sum_{\mathfrak p\text{ in the fixed identity-ray annulus }i}
       W_i(N\mathfrak p/P_i)(N\mathfrak p)^{-5/6}.
 \tag{2.4}
\]

There is no \(\eta(\mathfrak p)\) in (2.4). The fixed-ray prime ideal
theorem and the nonnegative profiles give the same eventual
nonvanishing and \(Z^{o(1)}\) reciprocal. No assertion that an
infinite-order character equals one on these primes is made or needed.

For the unselected principal factor, the exact local calculation in the
previous packet, with the earlier Eisenstein case credited in
ATTRIBUTION_CORRECTION.md, gives

\[
 H_\eta(s)=
 L_F^S(6s-3,(\overline\Lambda\eta)^6)\,K_\eta(s),
 \qquad K_\eta\text{ a holomorphic unit on }\operatorname{Re}s>1/2.
 \tag{2.5}
\]

The local proof only requires unitary phases, so it applies to this
angular \(\eta\). In particular the ordinary Euler domain protects
\(H_\eta\) on \(\operatorname{Re}s>2/3\), which contains the entire
principal box used in the comparison. We do not need a new zero-free
theorem for the extracted character in order to prove (1.4).

### 2.3 The detector sees the enlarged family

All finite corrections, including ray selectors and
\(\Upsilon_S\), are fixed before bins are selected. They form a finite
group \(\Theta_0\). For a fixed target, transformed whole coefficients
have angular types in a finite set, and their finite components lie
in a finite \(\Theta_0\)-orbit.

A moving presentation and each of its fixed prime-coefficient twists
belongs to \(\mathcal A_\Omega(F)\).
The Borel--Caratheodory, three-circles, and Mellin arguments used for
the reciprocal, the ordinary factors, and prime amplitudes therefore
use a valid common zero-free half-plane whenever

\[
 \beta_\Omega(F)\le \frac{1+\kappa}{2}.
 \tag{2.6}
\]

For each fixed list of angular exponents, the same convexity bounds
are uniform in the moving finite conductor. The height exponent may
depend on that list.

The finite-conductor Kummer ramification argument still identifies
exceptional rows. Every member of the fixed coefficient group is
unramified outside \(S\); a nontrivial Kummer inertia character at an
exterior row prime cannot be canceled by an angular character
unramified there. The exact residue and centered-mean treatment of
the exceptional terms is provided in the product-moment adapter.

## 3. The bootstrap, without circularity

The angular inverse theorem first gives

\[
 \beta_\Omega(F)\le11/12.
 \tag{3.1}
\]

This step uses the new angular theta reflection, the source inverse
recursion, and sixth-power row amplification. It uses no angular
zero-free hypothesis and no product-moment prime-bound premise.

Write \(\beta=\beta_\Omega(F)\).

### 3.1 From \(11/12\) to \(7/8\)

Suppose \(\Delta=\beta-7/8>0\). Use the source initial geometry

\[
 (b,\ell,l_x,l_y,h)
 =\left(\frac18,\frac16,\frac{17}{48},
                  \frac{23}{48},\frac{13}{16}\right),
 \quad
 \kappa=\frac34+2\Delta=2\beta-1.
 \tag{3.2}
\]

By (3.1), \(\kappa\le5/6<1\), and (2.6) holds with equality.
The count, direct estimate, principal normalization, and remainder
estimates have the same norm exponents as source Section 13.6.
In particular the moderate endpoint relative to the presumed
supremum has the strict upper bound

\[
 -\frac{49}{440640}
 -\left(1-\frac h4\right)\Delta<0.
 \tag{3.3}
\]

The small, lowest-bin, intermediate, far, and principal remainders
retain the source's strict numerical margins. For every fixed target
this continues the principal Mellin quotient through a common
half-plane to the left of \(\beta\), a contradiction.
Thus \(\beta\le7/8\).

### 3.2 The pointwise comparison

The implication in source (13.21) now applies with the same family
supremum and \(\kappa=2\beta-1\). Its source cubic comparison gives

\[
 \beta\le B_\infty,\qquad
 B_\infty=0.874957019420098946\ldots <7/8.
 \tag{3.4}
\]

This is the source scalar theorem with the already justified angular
analytic interfaces. It is not the application of a finite-order
zero-free theorem to a new character.

### 3.3 The averaged numerator reaches \(B_\flat\)

Suppose \(\beta>B_\flat\). Set \(\kappa=2\beta-1\), so

\[
 \kappa_\flat<\kappa\le2B_\infty-1<3/4,
 \qquad \kappa_\flat=2B_\flat-1.
 \tag{3.5}
\]

The product-moment premise (2.6) again holds with equality.
Source Lemmas 14.9--14.10 supply tangent parameters
\((b_*(\kappa),\ell_*(\kappa))\), with

\[
 F_\flat(\kappa)=\frac{11}{12}-\frac{\ell_*(\kappa)}4
             <\frac{1+\kappa}{2}=\beta.
 \tag{3.6}
\]

Choose \(\ell<\ell_*(\kappa)\) sufficiently close that the source
admissibility conditions hold and
\(B(\ell)=11/12-\ell/4<\beta\).
The reflected numerator is the same finite-order function
\(L_F(w,\chi_u)\). Source Proposition 14.3 therefore gives its
amplified average with the original prime factors; their admissibility
is supplied by the angular product-moment adapter.
The remainder assembly of Proposition 14.6 and the strict endpoint
comparison yield \(\beta\le B(\ell)<\beta\), a contradiction.
This proves (1.4).

The quartic, tangent inequalities, and their source certificates are
imported scalar inputs. The small local checker in this packet does
not purport to certify those source computations or the 136-page
analytic argument.

## 4. Constants and the supremum argument

It is not necessary for \(\beta\) to be the real part of an attained
zero. If \(\beta\) exceeded the stated boundary, its positive
comparison gap would determine the numerical geometry, prime-length
mesh, and target-independent continuation boundary first.

For each fixed \(\eta=\Omega^h\xi\), choose its finite data, the finite
angular coefficient list, seminorm orders, and polynomial height
orders next. The height cutoff power can be chosen sufficiently
small after those orders. The onset and multiplicative constant
may depend on \(\eta\).

The Mellin continuation then excludes every such target's zeros in
the same open half-plane
\(\operatorname{Re}s>\sigma_{\rm cont}\), with
\(\sigma_{\rm cont}<\beta\) depending only on the numerical gap.
This contradicts the definition of the supremum over the whole
family, regardless of target-dependent constants.

Omitted Euler factors have their zeros on \(\operatorname{Re}s=0\).
A principal pole creates a zero of the reciprocal and is harmless.
This also explains why the argument proves a common boundary but
does not supply uniform analytic constants as angular weights grow.

## 5. Scope of the advance

The exponent \(B_\flat\) for the already covered all-field finite-order
family has not decreased. The new assertion extends that boundary
to explicitly specified infinite-order angular families, using a new
archimedean and coefficient-family argument.

The exceptional angular vectors \(a=\lambda\) and \(a=-\lambda\)
are not included by this proof. Their coefficient orbit reaches the
all-spherical theta case; the constant-term cancellation used here
then fails. Nothing in this note deletes those constant terms.
Their treatment is a separate analytic problem.
