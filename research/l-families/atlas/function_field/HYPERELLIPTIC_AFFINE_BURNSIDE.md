# Odd-degree hyperelliptic affine quotients in every genus

Status: **DRAFT exact all-field theorem with bounded replay**

Scope: monic squarefree polynomials of degree `2g+1` over an odd finite
field, modulo affine changes of the base coordinate that retain the rational
branch point at infinity. This is not the full moduli stack of unpointed
hyperelliptic curves.

Exact source: `hyperelliptic_affine_burnside.py` and its generated JSON
certificate. The checker evaluates a divisor sum only. It does not enumerate
a field, polynomial family, curve, orbit, or Frobenius class.

Smallest next question: determine how the nonfree strata correlate with a
chosen Frobenius statistic. The theorem below counts presentations and
stabilizers in aggregate; it does not by itself determine a statistic's
coarse-versus-stack bias.

## The quotient and its stack mass

Fix `g>=1`, put `n=2g+1`, and let `H_n(q)` be the monic squarefree degree-`n`
polynomials over `F_q`. The affine group acts by

\[
 D(T)\longmapsto \alpha^{-n}D(\alpha T+\beta).
\]

Since

\[
 |H_n(q)|=q^{n-1}(q-1),\qquad |AGL(1,q)|=q(q-1),
\]

orbit-stabilizer gives the all-genus identity

\[
 \boxed{\sum_{[D]}\frac1{|\operatorname{Stab}(D)|}=q^{n-2}=q^{2g-1}.}
\]

Consequently uniform averaging over equations is exactly stabilizer-weighted
averaging on this declared affine quotient. Uniform averaging over coarse
orbit representatives is a different ensemble.

## Exact coarse-orbit formula

Write `p=char(F_q)` and define

\[
 S_m(q)=\#\{\hbox{monic squarefree polynomials of degree }m\},
\]

so that `S_0=1`, `S_1=q`, and `S_m=q^m-q^(m-1)` for `m>=2`. Also let
`A_m(q)` count those polynomials with nonzero constant term. For `m>=1`,

\[
 A_m(q)=\frac{(q-1)(q^m-(-1)^m)}{q+1}.
\]

The number `N_(g,q)` of coarse affine orbits is

\[
\boxed{
\begin{aligned}
N_{g,q}=q^{2g-1}
&+\sum_{\substack{d\mid q-1,\ d\ge2\\
                   n\bmod d\in\{0,1\}}}
 \varphi(d)\frac{q^{\lfloor n/d\rfloor}
                    -(-1)^{\lfloor n/d\rfloor}}{q+1}\\
&+\mathbf1_{p\mid n}\frac{S_{n/p}(q)}q .
\end{aligned}}
\]

Every displayed summand is an integer. This is a closed formula for every odd
prime power and every genus; it is not a fit to the frozen fields.

## One rational series across every degree

The fixed-locus classification can be assembled before selecting an odd
degree. Let

\[
S_q(u)=\sum_{m\ge0}S_m(q)u^m=\frac{1-qu^2}{1-qu},
\qquad
A_q(u)=\frac{S_q(u)}{1+u}.
\]

If `O_(q,n)` is the number of affine orbits of monic squarefree degree-`n`
polynomials under the degree-normalized action, then

\[
\boxed{
\sum_{n\ge0}O_{q,n}u^n=
\frac{
S_q(u)+q\displaystyle\sum_{\substack{d\mid q-1\\d\ge2}}
\varphi(d)(1+u)A_q(u^d)+(q-1)S_q(u^p)
}{q(q-1)}.}
\]

Indeed, an order-`d` scaling contributes `A_m(q)` in degrees `md` and
`md+1`, while a nonidentity translation contributes `S_m(q)` in degree `pm`.
The series is rational and exposes an exact automorphism-resonance spectrum:

- multiplicative resonances lie in degree classes `0,1 mod d` for divisors
  `d|q-1`;
- additive resonances lie in degrees divisible by `p=char(F_q)`.

The odd-degree theorem is the coefficient extraction `n=2g+1`. This series
also covers even-degree affine presentations, but no claim is made that the
even- and odd-degree presentations define the same marked moduli problem.

## Fixed-locus proof

Take a nonidentity affine element with multiplier `alpha!=1`, of order `d`.
Translation to its unique fixed point conjugates it to `S->alpha*S`. A fixed
monic polynomial has the form

\[
 D(S)=S^r h(S^d),\qquad r=n\bmod d.
\]

If `r>=2`, the root at zero is repeated. If `r` is zero or one, `D` is
squarefree exactly when `h` is squarefree and `h(0)!=0`: the order `d` is
prime to the characteristic, so the nonzero fibres of `S->S^d` are separable.
Thus one order-`d` affine element fixes `A_floor(n/d)(q)` models. There are
`q*phi(d)` such affine elements, including all translations of the scaling's
fixed point.

For a pure translation `S->S+beta`, `beta!=0`, invariant theory gives

\[
 F_q[S]^{\langle S\mapsto S+\beta\rangle}
 =F_q[S^p-\beta^{p-1}S].
\]

Hence a degree-`n` invariant exists only when `p|n`; it is
`h(S^p-beta^(p-1)S)`. The inner additive polynomial has nonzero derivative,
so composition is squarefree exactly when `h` is. Each of the `q-1`
nonidentity translations therefore fixes `S_(n/p)(q)` models. Substitution in
Burnside's lemma gives the formula.

The formula for `A_m` follows from the squarefree Euler series with the factor
for `T` removed:

\[
 \sum_{m\ge0}A_m(q)u^m
 =\frac{1-qu^2}{(1-qu)(1+u)}.
\]

## A universal involution defect

Because `n=2g+1` is odd, order two always contributes. Its exact correction
to the coarse orbit count is

\[
 \boxed{\frac{q^g-(-1)^g}{q+1}.}
\]

Every other scaling has order at least three, and every translation exception
has `p>=3`. At fixed genus this yields

\[
 N_{g,q}=q^{2g-1}
 +\frac{q^g-(-1)^g}{q+1}
 +O_g\!\left(q^{\lfloor(2g+1)/3\rfloor-1}\right).
\]

Thus the leading coarse-orbit excess, relative to the affine-stack mass, is
`q^(-g)`. Increasing genus rapidly suppresses this normalization defect, even
though an individual high-automorphism orbit can still dominate a tail-sensitive
statistic. The statement concerns the orbit-count excess; a total-variation
or moment correction still needs the stabilizer/statistic joint distribution.

## First three genera

For genus one,

\[
 N_{1,q}=q+1+2\mathbf1_{3\mid q-1}
 +\mathbf1_{\operatorname{char}F_q=3}.
\]

For genus two, the theorem recovers the independently frozen formula

\[
 N_{2,q}=q^3+q-1+2\mathbf1_{4\mid q-1}
 +4\mathbf1_{5\mid q-1}
 +\mathbf1_{\operatorname{char}F_q=5}.
\]

For genus three,

\[
\begin{aligned}
N_{3,q}=q^5+(q^2-q+1)
&+2(q-1)\mathbf1_{3\mid q-1}
 +2\mathbf1_{6\mid q-1}\\
&+6\mathbf1_{7\mid q-1}
 +\mathbf1_{\operatorname{char}F_q=7}.
\end{aligned}
\]

The test suite independently enumerates only the tiny prime-field cases
`(q,n)=(3,3),(5,3),(3,5)`, obtaining `5,6,29` orbits. The generated packet
then checks genera one through eight over seven prime powers using only the
closed divisor sum. Its genus-two values `29,132,349` agree with the earlier
full affine-orbit certificate.

## Interpretation firewall

The quotient remembers an odd-degree equation and its rational Weierstrass
point at infinity. A projective change moving infinity, and any resulting
non-affine automorphism, is outside this action. Therefore `N_(g,q)` is not a
count of unpointed hyperelliptic curves, and `q^(2g-1)` is not being asserted
as the cardinality of their full moduli stack.

No Frobenius distribution, monodromy group, L-function moment, Jacobian
realization theorem, number-field transfer, RH, or GRH follows from this
presentation census. Its use is narrower and concrete: it types the family
measure before a detector average is formed and predicts which affine
stabilizer orders can create finite-field corrections.
