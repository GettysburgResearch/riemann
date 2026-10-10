# Volterra endpoint control: global Pick order 888,000

**Status:** native quantitative refinement, submitted for independent review.
It preserves the complete source and arbitrary distinct positive nodes.
No RH claim is made.

**Scope:** the actual xi source kernel, globally to order 888,000 using the
published critical-line census through `H0=3000000000000`; and the complete
height-tail kernel, without a below-tail census, at the growing orders below.
The only arithmetic imports are the same classical strip, source/product,
published Trudgian argument bound, and published Platt–Trudgian census used
in [WEIGHTED_RATIONAL_DILATION.md](WEIGHTED_RATIONAL_DILATION.md).

**Dependencies:** W1–W19 of that independently reviewed packet, and the exact
arbitrary-node congruence in [ANNULAR_GLOBAL_PICK.md](ANNULAR_GLOBAL_PICK.md).
The theta remainder/count derivation is the native one in the latter packet,
not a new imported local-density conjecture. This note improves the constants
by a complete proof. The former 700,000 theorem remains frozen separately.

**What was run:** exact rational uniform guards, complete scalar gaps, Machin
pi and exponential enclosures, finite Volterra compressions, and exact tail
order controls in `verify_volterra_refinement.py`, normal and `python -O`.
Those are finite controls; the weighted operator and complete-source proofs
below remain essential.

## V0. Statement

Write `K_{>T}` for the complete source kernel restricted to ordinates `b>T`.
For `T>=H0`, every even integer `n>=850000` satisfying

\[
 \boxed{10000n^2\le2631T}                              \tag{V0}
\]

makes `K_{>T}` strictly positive definite on every `n` distinct positive
nodes. Every smaller size follows by appending distinct nodes and taking a
principal submatrix. The allowed maximal even order is
`sqrt(2631T/10000)+O(1)`; at `H0` it is **888,424**.
Adding the verified critical source below or at `H0` gives global Pick
order **888,000**. This is finite-order positivity for one full kernel, and
increasing orders for changing tail kernels, not all-order positivity.

## V1. Sharpen the already-derived complete count discrepancy

Use the same right-continuous multiplicity count and main term as W10:

\[
 N_+(u)=\mathcal M(u)+S(u)+\epsilon(u)/\pi,
 \quad |\epsilon(u)|<1/u,\qquad u\ge H_0.
\]

Here `7/8` is already included in `mathcal M`. The imported published bound
is `|S(u)|<=.112logu+.278loglogu+2.510`. Since `logu>28` and
`loglogu<=logu/8`, the native remainder bound gives

\[
 \frac{|N_+(u)-\mathcal M(u)|}{\log u}
 <\frac{112}{1000}+\frac{278}{8000}+\frac{2510}{28000}
                      +\frac1{84H_0}
 =\frac{6619}{28000}+\frac1{84H_0}
 <\boxed{\frac{236393}{1000000}=:c_E}.                 \tag{V1}
\]

The last available margin is exactly `1/7000000`, strictly larger than
`1/(84H0)`. Nonzero-ordinate endpoint limits extend this strict bound to
the one-sided values needed for excluding the atom at `T`. The bound uses
the published `S` estimate, not a rerun of that estimate.

## V2. A Volterra bound for the triangular endpoint matrix

For arbitrary complex numbers `e_0,...,e_(n-1)`, let `U` be the strictly
upper triangular part of `e e*`. Then

\[
 \boxed{\|U\|\le\frac2\pi\sum_i|e_i|^2.}            \tag{V2}
\]

**Proof.** Diagonal unitary conjugation makes every nonzero `e_i` real and
positive. Zero entries contribute zero rows and columns and can be removed.
Put `m_i=|e_i|^2`, partition `[0,L]`, `L=sum m_i`, into consecutive intervals
of lengths `m_i`, and embed `C^n` isometrically into their normalized constant
functions. The compression of the upper Volterra operator
`Vf(t)=integral_t^L f(s)ds` is exactly
`B=U+diag(m_i/2)`, with the indicated orientation. All its entries are
nonnegative. Thus `|Uv|<=B|v|` entrywise, so
`||U||<=||B||<=||V||=2L/pi`.

For completeness the Volterra norm follows from the mixed-boundary
Wirtinger inequality `||g||<=2L/pi ||g'||`, `g(L)=0`: even extension across
zero gives the ordinary Dirichlet inequality on `[-L,L]`. That inequality
follows, for smooth zero-boundary functions, by integrating the identity
obtained from the positive ground state `cos(pi t/(2L))`; its difference
of energies is the integral of
`cos(pi t/(2L))^2 |(g/cos(pi t/(2L)))'|^2`. Density gives the full `H1`
statement. Equality for the ground state gives the sharp norm. `L=0` is
immediate. \(\square\)

## V3. Improved uniform rational dilation

Use exactly the weighted polynomial model W2–W5 for every proper rational
function with signed imaginary poles, arbitrary positive pole scales, and
complex numerator of degree at most `n-1`. Its dilation matrix `D=t partial_t`
is upper triangular with diagonal `0,...,n-1`, and

\[
 D+D^*=E-M,\quad E=W(1)e e^*,\quad
 \operatorname{tr}E\le n^2,\quad
 M=M^*,\quad\|M\|_F\le(2n+1/28)\sqrt n.
\]

The strictly upper triangular part of a Hermitian matrix has squared
Frobenius norm at most half the full squared Frobenius norm. Hence (V2)
and the known diagonal give

\[
 \|D\|\le\frac2\pi n^2+(2n+1/28)\sqrt{n/2}+n-1.
\]

The real rational derivative adds the multiplier `1-tQ'/Q`, of modulus at
most `n+1`. Therefore

\[
 \|bR'\|_{\log b,[T,\infty)}
 \le\left[\frac2\pi n^2+(2n+1/28)\sqrt{n/2}+2n\right]\|R\|.
\]

For `n>=850000`, elementary `pi>314159/100000` and
`sqrt(2n)>1300` yield the exact uniform bound

\[
 \frac{200000}{314159}
   +\frac{2+1/(28\cdot850000)}{1300}+\frac2{850000}
 <\boxed{d:=\frac{3191}{5000}=.6382}.                 \tag{V3}
\]

Consequently both `||D||<=d n^2` and `||bR'||<=d n^2||R||` hold for the
whole signed-pole class, uniformly in the scales. This retains the exact
endpoint bound `logT |R(T)|^2<=n^2 B_R/T` from W9.

## V4. Improved complete-source quadrature

Let `q=n^2/T`. Repeating the W10 integration by parts with (V1) and (V3)
gives

\[
 \left|2\int_{(T,\infty)}|R|^2d(N_+-\mathcal M)\right|
 \le2c_E(1+2d)qB_R=\ell qB_R,
 \quad\boxed{\ell=\frac{1345312563}{1250000000}}.       \tag{V4}
\]

Every atom, one-sided endpoint, and multiplicity convention is exactly
that of W10. Since the unchanged main density lies strictly between
`(13/44)logb` and `(1/3)logb`, the reference and sampling bounds are

\[
 (13/44-\ell q)B_R<\sum_{b_\alpha>T}w_\alpha|R(b_\alpha)|^2
 \le S(q)B_R,\quad S(q)=1/3+\ell q.                   \tag{V5}
\]

These apply to every complex numerator, including each `D^jP` sharing
the fixed denominator.

## V5. Uniform displacement amplification, with the whole exponential

Keep the exact W12 dilation `P(t')=exp(gamma D)P(t)` and W13 signed-pole
prefactor control, where each ordinate independently has any displacement
`|a_b|<=A<=1/2`. Discrete Minkowski and (V3) give amplification at most

\[
 \exp[(2d n^2+4n)A/T]
 \le\exp[(d+2/n)q].
\]

Under (V0) and `n>=850000`, its exponent is strictly less than `21/125`.
A rational Taylor upper bound gives

\[
 \exp(21/125)<\boxed{\kappa:=237/200=1.185}.           \tag{V6}
\]

For example, through degree six the exponential tail is at most the next
term divided by `1-(21/125)/8`, since later successive term ratios decrease.
The exact replay checks this inequality. In particular every `D^jP` has
displaced discrete norm at most
`kappa (d n^2)^j sqrt(S(q)B_R)` with its displaced prefactor included.
This is valid for every independently selected `a_b` and every `tau a_b`
in the Taylor integral; it is not a constant-shift surrogate.

## V6. Keep the sharp first and second derivative coefficients

The exact identities W14 still hold. The allowed vertical paths have
`|B|<=3n`, `|DB|<=4n`. Consequently

\[
 \|bR'(z_b)\|_{\rm src}
 \le\kappa(d n^2+3n)\sqrt{S(q)B_R}
 \le C_1\kappa n^2\sqrt{S(q)B_R},\quad
 \boxed{C_1=6383/10000},
\]

\[
 \|b^2R''(z_b)\|_{\rm src}
 \le\kappa[d^2n^4+(6n+1)d n^2+9n^2+7n]\sqrt{S(q)B_R}
 \le C_2\kappa n^4\sqrt{S(q)B_R},\quad
 \boxed{C_2=2037/5000}.                               \tag{V7}
\]

The last two scalar inequalities hold uniformly at all `n>=850000`:
after division by the leading power, all nonconstant terms decrease with
`n`, and the exact endpoint guards are strict.

## V7. Complete conjugate-source payment and strict gap

For each real quadratic vector of either exact node moment block use
the same real-coefficient polynomial and proper functions `R_+,R_-` in
W16. Their real-axis weighted norms are the same `B>0`. Their product
`f=R_+R_-` is sampled at the actual squared poles `(b+i a)^2`.
The two outer product-rule terms and the middle term give, by weighted
discrete Cauchy–Schwarz,

\[
 \sum w_\alpha|f''(b_\alpha+i a_\alpha)|
 \le2(C_2+C_1^2)\kappa^2q^2 S(q)B.
\]

Conjugate groups cancel the first imaginary Taylor term. Since
`A^2/2<=1/8`, the complete displacement loss is at most

\[
 \frac14(C_2+C_1^2)\kappa^2q^2 S(q)B.
\]

Thus each nonzero block quadratic form is strictly greater than

\[
 \left[\frac{13}{44}-\ell q
       -\frac14(C_2+C_1^2)\kappa^2q^2(1/3+\ell q)\right]B.
                                                               \tag{V8}
\]

Every coefficient of the subtracted polynomial is positive. Its worst
point is therefore `q0=2631/10000`, where the exact gap is

\[
 \boxed{\frac{18928758577227631999353142201217}
              {220000000000000000000000000000000000}
       >0}.                                                   \tag{V9}
\]

This includes all source multiplicities and both reflected upper members
of every nonreal quartet. The exact reference measure is `2dN_+`, as in
W16–W18. Critical sources have zero displacement cost.

## V8. Complete summation and an independent old-count fallback

The convergence, invertible arbitrary-node congruence, and critical-source
addition arguments are unchanged from W19 and Section 7 of its packet.
Proper rational decay and complete `N_+(b)=O(b logb)` counting justify every
full sum, derivative sum, and Taylor remainder. This proves (V0) and its
global consequence. The exact integer global guard is

`10000*(888000)^2 < 2631*H0`.

For a fallback independent of the sharper count (V1), retain the previously
reviewed `|N_+-mathcal M|<.25logb`. Then use `ell0=1/2+d=5691/5000`,
`q<=1/4`, and `kappa0=47/40`. All the same operator and derivative guards
apply, since `exp(.16)<47/40`. The exact gap is

\[
 \frac{294672985812197}{6758400000000000000}>0.
\]

This proves a complete-tail condition `4n^2<=T` for `n>=850000` and global
order **866,000**, with only the former count constant. Both results use
the published census solely when passing from a tail to the full kernel.
RH remains open.
