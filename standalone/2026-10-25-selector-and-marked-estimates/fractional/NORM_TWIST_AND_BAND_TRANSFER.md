# Testing norm twists and narrow prime bands as a parity transfer

Status: proved obstruction to a single polynomial-height norm twist under
the imported fixed zero-free half-plane; explicit scope audit of a
prime-band gluing attempt. No new zero-free region follows.

Scope: one fixed number field and its fixed omitted finite primes. The
main obstruction is a statement about actual Dedekind Euler products,
not an arbitrary polynomial countermodel. It also applies to an average
harmonic prime-error condition, not only uniform prime approximation.

Exact dependencies: standard analytic properties of the fixed Dedekind
zeta function (simple pole at one, polynomial vertical growth on fixed
strips, and its absolutely convergent Euler product to the right of one),
plus the explicitly named hypothesis `ZF(beta)` below. The current
source-qualified Liu theorem supplies such a fixed `beta<1` if imported.
The ordinary-moment interface being tested is Xu--Sang,
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Theorem 2.2 and
Corollary 2.3; their common puncture has bounded-power norm and their
profile/height costs are retained.

## 1. The tempting construction

On squarefree ideals, the desired sign is

\[
 \mu(n)=\prod_{p\mid n}(-1).
\]

A norm twist is completely multiplicative, so a twist satisfying
`(Np)^(it) approximately -1` on all relevant prime ideals would imitate
that sign on squarefree products. One might then try to apply the
ordinary squarefree mean, whose norm-twist cost is a fixed polynomial
in the height.

The needed height is the issue. Approximating finitely many prime phases
by very large twists is not a bounded-height transference theorem.
The following argument gives a source-specific quantitative obstruction.

## 2. A reciprocal estimate from a fixed zero-free half-plane

Let `Z_F(s)` denote Dedekind zeta with one fixed finite set `S` of Euler
factors omitted. It has a simple pole at one with positive residue. Let

\[
 \mathrm{ZF}(\beta):\qquad Z_F(s)\ne0\quad(\Re s>\beta),
 \qquad \tfrac12<\beta<1.
 \tag{1}
\]

This is an imported hypothesis for the lemma, not a new theorem proved
by this note.

**Lemma 1.** Under (1),

\[
 |Z_F(\sigma+it)|^{-1}
 \ll_{F,S,\beta}\log\log(3+|t|),\qquad
 1\le\sigma\le3/2.
 \tag{2}
\]

At the pole, the reciprocal is interpreted by its analytic removable
value zero.

**Proof.** Choose fixed `beta<beta_0<beta_1<1`. On high positive or
negative horizontal strips the logarithm of `Z_F` can be chosen by
continuation from the Euler-product germ. There are no zeros or poles
there. Polynomial vertical growth, the bounded Euler logarithm at a
fixed line to the right of one, and the Borel--Caratheodory inequality
give

\[
 |\log Z_F(v+i\tau)|\ll_{F,S,\beta}\log(3+|\tau|),
 \qquad \beta_1\le v\le3,
 \tag{3}
\]

for sufficiently large `|tau|`. For example use disks centered at
`3+i tau`, with outer radius reaching `beta_0` and a fixed smaller
radius reaching `beta_1`; the real part of the logarithm is bounded
above by the polynomial growth estimate. These disks stay away from
the pole once `|tau|` is large.

For `s=sigma+it`, `sigma in [1,3/2]`, smooth Mellin inversion initially
on `Re w=1` gives

\[
 \frac1{2\pi i}\int_{(1)}\Gamma(w)Y^w\log Z_F(s+w)\,dw
 =\sum_{p\notin S}\sum_{j\ge1}
     \frac{(Np)^{-js}}j\exp(-(Np)^j/Y).
 \tag{4}
\]

Truncate the integral at `|Im w|=|t|/2`, and shift this truncated contour
to `Re w=beta_1-sigma`. The whole rectangle has imaginary part of
`s+w` bounded away from zero, so no pole logarithm is crossed. Since
`-1<beta_1-sigma<0`, the only Gamma pole crossed is at `w=0`, with
residue `log Z_F(s)`. Bound (3) and Gamma decay yield

\[
 \log Z_F(s)
 =\sum_{p\notin S}\sum_{j\ge1}
     \frac{(Np)^{-js}}j\exp(-(Np)^j/Y)
   +O_{F,S,\beta}(Y^{\beta_1-\sigma}\log|t|+1).
 \tag{5}
\]

Here take `Y` to be a fixed power of `log|t|`; the horizontal and
truncated-tail errors are exponentially small in `|t|`, and in particular
are absorbed into the displayed bounded error. Choosing
`Y=(log|t|)^(2/(1-beta_1))` makes the first error bounded as well.

The absolute value of the Euler sum in (5), with `sigma>=1`, is bounded
by

\[
 \sum_{p\notin S}\sum_{j\ge1}
        \frac{\exp(-(Np)^j/Y)}{j(Np)^j}
       =\log\log Y+O_{F,S}(1).
 \tag{6}
\]

For clarity, (6) does not require a new prime-ideal error term. The
terms with `j>=2` are bounded. Compare the `j=1` sum with
`sum_p (Np)^(-1-1/logY)`. Below `Y`, their difference is bounded using
`1-q^(-1/logY)<=log q/logY`, `1-exp(-q/Y)<=q/Y`, and the elementary
prime-ideal Chebyshev bound. Above `Y`, both tails are bounded by the same bound and partial
summation. The second sum is `log Z_F(1+1/logY)+O(1)`, which equals
`loglogY+O(1)` by the simple pole at one.

Taking negative real parts in (5) therefore gives
`|1/Z_F(s)|<<logY<<loglog|t|`. The bounded-height range is compact for
the reciprocal and is absorbed into the constant. QED.

The elementary prime-ideal Chebyshev bounds used here follow, for a
fixed field, from the corresponding rational-prime bounds and the fact
that there are at most `[F:Q]` prime ideals above each rational prime;
higher residue degrees contribute convergent tails where appropriate.

## 3. No polynomial-height approximation of the negative prime phase

For `X>=e^2`, set `sigma_X=1+1/logX`. The simple pole and the same
tail argument give

\[
 H_F(X):=\sum_{\substack{p\notin S\\Np\le X}}
          (Np)^{-\sigma_X}
        =\log\log X+O_{F,S}(1).
 \tag{7}
\]

**Theorem 2.** Assume (1), and fix `0<=eta<sqrt(2)`. If a real `t`
satisfies

\[
 |(Np)^{it}+1|\le\eta
 \quad\text{for every }p\notin S\text{ with }Np\le X,
 \tag{8}
\]

then, for sufficiently large `X`,

\[
 \log\log(3+|t|)
       \gg_{F,S,\beta,\eta}(\log X)^{1-\eta^2/2}.
 \tag{9}
\]

In particular (8) fails for all `|t|<=X^C`, for any fixed `C`, once
`X` is sufficiently large.

**Proof.** Since `|e^(iv)+1|^2=2+2 cos v`, (8) implies
`cos(t logNp)<=-1+eta^2/2`. The Euler logarithm at `sigma_X>1` gives

\[
 \Re\log Z_F(\sigma_X+it)
 =\sum_{Np\le X}(Np)^{-\sigma_X}\cos(t\log Np)+O_{F,S}(1).
 \tag{10}
\]

Both the higher-prime-power part and the prime tail above `X` are
bounded uniformly in `t`, as in (6)--(7). Thus, with `a=1-eta^2/2>0`,

\[
 |Z_F(\sigma_X+it)|^{-1}\gg_{F,S,\eta}(\log X)^a.
 \tag{11}
\]

Combining (11) with (2) proves (9). If `|t|<=X^C`, its left side is
`O_C(loglogX)`, which is smaller than every positive fixed power of
`logX`. QED.

The same proof applies if the uniform condition (8) is replaced by the
weaker harmonic mean-square condition

\[
 \sum_{Np\le X}\frac{|(Np)^{it}+1|^2}{(Np)^{\sigma_X}}
       \le\eta^2 H_F(X).
 \tag{12}
\]

Indeed (12) supplies the identical bound for the weighted cosine sum
in (10). For polynomial-height twists the proof also yields the explicit
lower estimate

\[
 \sum_{Np\le X}\frac{|(Np)^{it}+1|^2}{(Np)^{\sigma_X}}
 \ge 2\log\log X-2\log\log\log X-O_{F,S,\beta,C}(1),
 \quad |t|\le X^C.
 \tag{13}
\]

For bounded `t`, the right-side estimate follows after enlarging the
constant; for high `t`, take logarithms of (2) in (10).

Consequently the actual negative prime phase stays a definite harmonic
distance from every permitted bounded-power norm twist. This is why
letting a norm twist tend to a completely multiplicative parity phase
does not transfer the ordinary mean at its available polynomial height
cost. The theorem does not rule out a new arithmetic averaged method
that never requires (8) or (12).

## 4. What changes on a narrow band

If prime norms are restricted to
`P<=Np<=P^(1+delta)`, choose `t_P=pi/logP`. Then

\[
 |(Np)^{it_P}+1|\le\pi\delta.
 \tag{14}
\]

For a squarefree product of `k` such primes, telescoping products gives
an error at most `pi k delta` in the parity phase. This local observation
is valid and uses only a small height. It does not by itself estimate
the sums restricted to those products.

There are two distinct costs in the proposed gluing.

### 4.1 Prime-factor bands are not ordinary smooth columns

Factoring an ideal into the portions whose prime factors lie in each
band produces factors with arithmetic support
`P^-(n_j)>=P_j`, `P^+(n_j)<=P_(j+1)`. The source ordinary moment is for
full character sums with smooth norm profiles and licensed common
punctures. It does not state that bound for arbitrary prime-factor-band
restrictions.

Representing a band restriction literally as a common Euler puncture
requires excluding every prime outside the band up to the column
cutoff. The radical of that puncture is generally exponentially large
in the cutoff, not a bounded power. The source permits an exactly
separated common puncture of bounded-power norm; this construction
does not meet that hypothesis. An analytic sieve decomposition might
replace the huge puncture, but its full coefficient cost and rough
remainder would then need to be proved.

Similarly, multiplying many independently twisted band factors calls
for a growing product-moment theorem with its constants tracked. A
two-full-factor moment cannot silently be applied to this product.

### 4.2 Uniform approximation fine enough for a power gain uses many bands

The elementary construction (14), applied to at most
`r_D=O(logD/loglogD)` prime factors, gives total coefficient error at
most `pi r_D delta`. Covering prime norms from a fixed lower cutoff
to `2D` with relative-logarithmic-width `delta` requires on the order
of `delta^(-1) loglogD` bands.

If the remaining error is handled only by the arbitrary-coefficient
sieve, the native target in `UNIFORM_FRACTIONAL_WINDOW.md` requires
coefficient error at the fixed-power scale `U^(-kappa(r))`, up to
subpower losses. This elementary uniform approximation therefore
requires

\[
 \delta\ll U^{-\kappa(r)}/r_D,
 \qquad
 \#\text{bands}\gg U^{\kappa(r)}r_D\log\log D.
 \tag{15}
\]

These are costs of this specified approximation and separate-error
argument, not a lower bound for every conceivable band method. They
show that the tempting fixed-number-of-bands use of the existing
ordinary product theorem does not close the calculation.

## 5. Relation to the new prime-list paper

Lue--Wang--Wu,
[On the Hardy--Littlewood--Chowla Conjecture, arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1),
Section 4.2, calls its coordinate change a parity conjugacy. Its precise
content is a unitary change of integer-vector coordinates taking a
determinant coefficient `-2` to `1` on a specified parity coset. It is
not an identity that replaces `mu^2` by `mu` in an arbitrary character
column.

The paper's prime-list operators and distinct-prime moment arguments
may motivate an arithmetic treatment of the band restrictions above.
To apply them here one must first identify an actual native-character
kernel with the paper's determinant kernel and retain its restrictions.
Neither the name of the conjugacy nor a qualitative shifted-prime
cancellation statement supplies that embedding or a native power gain.

## 6. What remains viable

The local approximation (14) is useful only together with a new theorem
for prime-factor-restricted character products and controlled gluing.
The global single-twist shortcut is quantitatively excluded by
Theorem 2 at the source's available height scale. A direct estimate for
the actual signed fractional convolution, or for a prime-list operator
faithfully representing the native Gram kernel, remains a substantive
route; neither has been established in this note.
