# Canonical good-prime coefficients at all three theta cusps

**Status:** proposed exact coefficient theorem and finite-character adapter.
The arithmetic conclusions retain the imported theta coefficient formulas
as their stated analytic source. The character-support conclusion in
Section 4 assumes the explicit cube-covariance identity stated there;
when that identity is supplied by the companion finite-ray proof, it
becomes an exact composition. No higher-moment estimate or new zero-free
boundary is asserted in this note.

**Authorship:** scale_covariance_attack. Independent review is to be
recorded separately against the final contents.

**Sources and normalization.** The repository source is the October 5
`paper2.tex`, OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, physically retained in the
October 7 import. Its labels `eq:cusp-fourier-coefficients` and
`eq:conjugate-cusp-coefficients` specify the three cusp sequences.
Its Appendix on fixed rays states
`e(z) = breve-e(z/lambda)`. The explicit arithmetic input is Dunn and
Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), dated
May 14, 2024, equations (5.7), (5.8), (5.13), and (5.14).
Those coefficient identities are used here, not that paper's
GRH-conditional dispersion or prime-sum estimates.

The formulas below are derived in the repository's normalization. In
particular they concern `d_sigma`, the Fourier coefficients of the
conjugate theta functions; using the formulas for theta without that
conjugation would change both the Gauss coefficient and the ninth-root
phases.

## 1. Convert the additive character before reading the coefficients

Write

\[
\omega=e^{2\pi i/3},\qquad
\lambda=1+2\omega=i\sqrt3,\qquad
\zeta_9=e^{2\pi i/9},\qquad Nn=|n|^2.
\tag{1.1}
\]

The repository uses

\[
e(z)=\exp(4\pi i\operatorname{Im}z/\sqrt3),
\qquad
\breve e(z)=\exp(2\pi i(z+\overline z)),
\qquad e(z)=\breve e(z/\lambda).
\tag{1.2}
\]

Let `n` be a squarefree primary ideal generator outside the fixed set
`S`, where `S` contains the primes above 6. The normalized sextic Gauss
coefficient is

\[
\gamma_2(n)=\frac1{\sqrt{Nn}}
  \sum_{x\bmod n}\chi_n(x)^2e(x/n).
\tag{1.3}
\]

The cubic Gauss sum in the external coefficient formulas uses the
trace character:

\[
g(t,n)=\sum_{x\bmod n}\chi_n(x)^2\breve e(tx/n).
\tag{1.4}
\]

For `(t,n)=1`, changing variables by `lambda t` in the residue field
gives the exact identity

\[
\boxed{
g(t,n)=\sqrt{Nn}\,\chi_n(\lambda t)^{-2}\gamma_2(n).
}
\tag{1.5}
\]

The values of `t` needed below are `1`, `lambda^2`,
`omega lambda^2`, and `omega^2 lambda^2`, all coprime to `n`.
In particular,

\[
\frac{g(1,n)}{\sqrt{Nn}}
 =\chi_n(\lambda)^{-2}\gamma_2(n),
\qquad
\frac{g(\omega^j\lambda^2,n)}{\sqrt{Nn}}
 =\chi_n(\omega)^{-2j}\gamma_2(n),\quad j=0,1,2.
\tag{1.6}
\]

The latter equality uses `chi_n(lambda)^(-6)=1`, on precisely these
good indices. Thus the conversion does not introduce any nontrivial
infinity type, and all the extra multiplicative factors have cube one.

## 2. An explicit table for every supported cusp sector

Every supported Fourier index has the unique decomposition

\[
\ell=\varepsilon\lambda^m n b^3,
\qquad
\varepsilon\in\{\pm1,\pm\omega,\pm\omega^2\},
\tag{2.1}
\]

where `n,b` are primary, `n` is squarefree, and initially `(nb,S)=1`.
The squarefree `n` is permitted to overlap `b`. The table states when
a coefficient is nonzero. Every omitted sector is zero, as is an
index having a nonramified prime exponent congruent to two modulo
three and therefore not admitting (2.1).
Define

\[
\delta_\lambda(n)=\chi_n(\lambda)^{-2},\qquad
\delta_j(n)=\chi_n(\omega)^{-2j}\quad(j=0,1,2),
\tag{2.2}
\]

and

\[
(a_0,a_1,a_2)=(1,\zeta_9,\zeta_9^{-1}),\qquad
(c_0,c_1,c_2)=(1,\omega^2\zeta_9,\omega\zeta_9^{-1}).
\tag{2.3}
\]

Here the scalars `c_j` are local notation in this table, unrelated to
the bad denominator factor called `c_0` in the reflection formulas.

### Theorem 2.1. Complete good-prime factorization

In every nonzero sector,

\[
\boxed{
d_\sigma(\ell)
=C_{\sigma,m,\varepsilon}\sqrt{Nb}\,
 \gamma_2(n)\delta_{\sigma,m,\varepsilon}(n)
 E_\sigma(\ell),
}
\tag{2.4}
\]

with `E_0(ell)=1`, `E_-(ell)=E_+(ell)=breve-e(ell)`, and the
following exact choices.

| Cusp | Ramified exponent and unit | Scalar `C` | Cubic ray factor `delta(n)` |
|---|---|---|---|
| `0` | `m=3r-3`, `r>=0`, `epsilon=+1` or `-1` | `3^(r/2+5/2)` | `delta_lambda(n)` |
| `0` | `m=3r-4`, `r>=1`, `epsilon=+omega^j` or `-omega^j`, `j=0,1,2` | `3^(r/2+2) a_j` | `delta_j(n)` |
| `-` | `m=-4`, `epsilon=-omega^(j+1)`, `j=0,1,2` | `9 c_j` | `delta_j(n)` |
| `+` | `m=-4`, `epsilon=omega^(j-1)`, `j=0,1,2` | `9 c_j` | `delta_j(n)` |

All factors `delta` are fixed cubic ray characters supported at the
ramified prime, and in particular

\[
\delta(n)^3=1,
\qquad
|C_{\sigma,m,\varepsilon}|
\le27\cdot3^{m/6}.
\tag{2.5}
\]

### Proof

The imported definitions are

\[
\begin{split}
t_0(\ell)&=\tau(\ell),\\
t_-(\ell)&=\omega^2\tau_1(\omega^2\ell)\breve e(\ell),\\
t_+(\ell)&=\omega\tau_2(\omega\ell)\breve e(\ell),\\
d_\sigma(\ell)&=\overline{t_\sigma(-\ell)}.
\end{split}
\tag{2.6}
\]

The external formulas express `tau`, `tau_1`, and `tau_2` as their
listed sector scalar times `conjugate(g(t,n)) |b/n|`.
Conjugating (2.6) therefore gives `g(t,n)|b/n|`, not its conjugate.
Applying (1.5) removes `sqrt(Nn)` and leaves `sqrt(Nb) gamma_2(n)`
times (1.6). For `tau`, evenness removes the extra minus sign in
`tau(-ell)`; conjugating its ninth-root factors gives `a_j`.

For the two remaining cusps, (2.6) becomes

\[
d_-(\ell)=\omega\,
 \overline{\tau_1(-\omega^2\ell)}\breve e(\ell),
\qquad
d_+(\ell)=\omega^2\,
 \overline{\tau_2(-\omega\ell)}\breve e(\ell).
\tag{2.7}
\]

The support of `tau_1` consists of units `omega^j` at exponent `-4`;
solving `-omega^2 epsilon = omega^j` gives
`epsilon=-omega^(j+1)`. The support of `tau_2` consists of units
`-omega^j`; solving `-omega epsilon = -omega^j` gives
`epsilon=omega^(j-1)`. Substituting and conjugating the three scalar
entries in each source formula gives in both cases `9 c_j`.
This proves the table and every zero sector.

The supplementary cubic reciprocity laws show that the characters in
(2.2) depend only on a fixed residue class at the ramified prime.
Alternatively, their being cubic is immediate from their exponents:
the sextic character to the power `-2` has order dividing three.
The source's fixed-ray convention supplies the finite modulus.
For the first table row the scalar magnitude is exactly
`27 * 3^(m/6)`; for the other rows the displayed upper bound is
immediate. This proves (2.5). \(\square\)

## 3. Exact cube homogeneity, including the intrinsic additive phase

### Corollary 3.1

For every primary `c` coprime to 3 and every nonzero Fourier index
`ell` in the source lattice,

\[
\boxed{d_\sigma(c^3\ell)=\sqrt{Nc}\,d_\sigma(\ell),
\qquad \sigma\in\{0,-,+\}.}
\tag{3.1}
\]

No condition `(c,n)=1` is needed. The conclusion includes zero sectors.

### Proof

Multiplication by `c^3` preserves the unit, ramified exponent, and all
prime exponents modulo three. It preserves whether the good
squarefree/cube decomposition lies on the theta support. On support,
its only change in (2.1) is `b -> bc`. Thus the Gauss coefficient and
the cubic ray factor of `n` are unchanged and `sqrt(Nb)` is multiplied
by `sqrt(Nc)`.

For the nonstandard cusps one must also check `E_sigma`. Since
`c=1+3z` for some `z` in the Eisenstein integers,

\[
c^3-1=9z+27z^2+27z^3\in9\mathcal O_K
=\lambda^4\mathcal O_K.
\tag{3.2}
\]

Every source Fourier index belongs to `lambda^(-4) O_K`. Hence
`(c^3-1)ell` is an algebraic integer, whose trace is an integer, and

\[
\breve e(c^3\ell)=\breve e(\ell).
\tag{3.3}
\]

This verifies the intrinsic phase as well. The same proof directly
uses the trace Gauss sums for the finitely many additional good
prime factors not covered by the repository's sextic notation;
it needs only `c` primary and coprime to 3. \(\square\)

### Fixed bad-prime parts

The reflected indices are not restricted to be coprime to the
arbitrarily enlarged set `S`. Write

\[
n=n_0n_1,\qquad b=b_0b_1,
\tag{3.4}
\]

where `n_0` is squarefree and supported on `S` away from the ramified
prime, `b_0` is arbitrary and supported on those primes, and
`(n_1b_1,S)=1`. The possible `n_0` form a finite set. Cubic Gauss CRT
splits the `n_0,n_1` factor into a fixed scalar and the same
`gamma_2(n_1)`, with an additional factor

\[
\chi_{n_1}(n_0)^4.
\tag{3.5}
\]

This is a cubic ray character with conductor supported on `S`, so its
cube is one. At a prime where the sextic notation was originally
excluded, this statement can be written with the ordinary cubic
symbol; it is the same power-four character on the good `n_1`.
The normalized Gauss scalar of the fixed squarefree `n_0` has
modulus one. The factor of `b_0` is exactly `sqrt(Nb_0)`, while the
additive phase and every original local zero remain present.

Thus (2.4) continues to have the same canonical structure in the
varying good indices `n_1,b_1`, with the indicated frozen bad labels.
No bad-prime coefficient is deleted. There are only finitely many
residue patterns modulo any fixed bad modulus, even though the
actual norm of `b_0` can grow. In a completed Dirichlet series its
remaining bad-cube factors are geometric series and converge for
every strictly positive real cube exponent. In the smoothed reflected
sum the usual `1/Nb_0` factor and fixed-prime geometric sums give the
same harmless bound. The ramified normalization contributes
`3^(-m/3)` in the normalized theta sum, which is summable for
`m>=-4`.

## 4. Character expansion with a prescribed cube

Fix a modulus `M` supported on `S` and containing the primary modulus.
Let `G` be the finite group of its unit classes represented by primary
elements. Let `rho` be a fixed character of this group. Suppose a
function `F:G -> C` satisfies the exact covariance

\[
F(x y^3)=\overline{\rho(y)}^{\,3}F(x)
\quad\text{for every }x,y\in G.
\tag{4.1}
\]

This is the precise finite identity to be verified for the reunited
Fourier ray coefficient. It must include its original local zero
masks and its transformed argument, not an isolated one of its
Fourier summands.

### Lemma 4.1

The multiplicative Fourier expansion of `F` has the form

\[
\boxed{
F(x)=\sum_{\psi^3=\overline\rho^{\,3}}\widehat F(\psi)\psi(x).
}
\tag{4.2}
\]

### Proof

Use

\[
\widehat F(\psi)=\frac1{|G|}\sum_{x\in G}F(x)\overline{\psi(x)}.
\tag{4.3}
\]

Replace `x` by `x y^3` in this finite sum and use (4.1).
It follows that

\[
\widehat F(\psi)
=\overline{\rho(y)}^{\,3}\overline{\psi(y)}^{\,3}
 \widehat F(\psi).
\tag{4.4}
\]

If the coefficient is nonzero, then for all `y`
`psi(y)^3=conjugate(rho(y))^3`. This is exactly the restriction in
(4.2); ordinary finite character orthogonality proves the expansion.
\(\square\)

### Corollary 4.2. The required all-cusp canonical family

Freeze a supported ramified/unit sector, and any bad-prime parts as in
(3.4). Suppose the actual reunited finite multiplier of its varying
good index satisfies (4.1). Include the intrinsic factor
`E_sigma(ell)` in that multiplier. By (3.3), it has cube covariance
one, so including it does not change (4.1).

Then the complete good-part coefficient is a finite sum of terms

\[
\boxed{
C_{\rho'}\sqrt{Nb_1}\,
 \gamma_2(n_1)\rho'(n_1)\rho'(b_1)^3,
\qquad \rho'^3=\overline\rho^{\,3}.
}
\tag{4.5}
\]

The family of `rho'` is finite and has conductor supported on a fixed
bad modulus, independent of the varying row conductor. It may be
chosen to cover all supported ramified sectors because their
residue data have only finitely many values.

Indeed Lemma 4.1 expands the multiplier at `n_1 b_1^3` as
`psi(n_1) psi(b_1)^3`. Multiply by the cubic ray factor `delta` of
(2.4), including (3.5), and put `rho'=delta psi`. Since `delta^3=1`,
the extra factor on `b_1` is one, and `rho'^3=psi^3` is unchanged.
This proves (4.5) without assuming that one individual finite-ray
character equals the original character.

With the angular and row factors restored, the coefficient in (4.5)
is exactly the canonical structure

\[
\overline{\alpha(n_1)}\gamma_2(n_1)\rho'(n_1)\chi_k(n_1)
\;\rho'(b_1)^3\overline{\alpha(b_1)}^{\,3}\chi_k(b_1)^3.
\tag{4.6}
\]

Every coprimality mask at `k` and the fixed bad primes is retained.
The resulting good cube character is therefore

\[
\chi'_{{\rm cube},k}
=\overline\rho^{\,3}\overline\alpha^{3}\chi_k^3.
\tag{4.7}
\]

This is the character identity needed for the second dominant-divisor
conditioning. Its proof requires the actual finite covariance (4.1)
as well as the coefficient identities above. The cube law of a
supplementary character alone would not supply it.

## 5. Consequence for the coupled quadratic--cubic estimate

There is also an independent quantitative application of Theorem 2.1.
At fixed `m`, unit, cusp, and bad-prime parts, its good-prime Gauss
factor obeys

\[
\gamma_2(e n')
=\gamma_2(e)\gamma_2(n')\chi_{n'}(e)^4,
\qquad (e,n')=1.
\tag{5.1}
\]

The supplementary `delta` splits multiplicatively. Every remaining
fixed periodic additive phase may be separated by finite residue
classes before estimating norms. Thus the separated `e,n'`
coefficient class is exactly the one used in PR #915,
`COUPLED_THETA_COMPLETION.md`, Lemma 6.1. Its quadratic--cubic
composition applies at every source cusp, not only the previously
selected good standard face, with the same moving `(k,e)=1` mask.

On an `E,F,G` allocation the squarefree theta scale is
`Y/3^m` before its cube factors, where

\[
Y=\frac{H^2EG^2}{BF}.
\tag{5.2}
\]

The normalized ramified amplitude is at most a fixed multiple of
`3^(-m/3)` by (2.5); hence its norm sum over `m>=-4` converges, even
after replacing `Y/3^m` by a fixed multiple of `Y`. Bad cube factors
have the same summable norm weights as in the original component
proof. Therefore its all-cusp block conclusion is

\[
\boxed{
\sum_{k\sim H}^{*}|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon\left[HE+Y+(EY)^{2/3}\right].
}
\tag{5.3}
\]

This uses only the coefficient identities and the original classical
sieves, not the cube-covariance assumption (4.1). It is still a
squarefree-row bound. Growing extra auxiliary twists would require
their own local scalar computation.

After applying the PR #920 complete-group support zero at all cusps,
the proof of the companion `SUPPORT_PRUNED_COVARIANCE.md`, Theorem 2.1,
now gives its same displayed bound for the full source coupled
completion:

\[
\boxed{
\sum_{k\sim H}^{*}|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon
\left[HA+\frac{H^2A\min(A,\sqrt B)}{B}
 +\left(\frac{H^2A^2}{B}\right)^{2/3}\right].
}
\tag{5.4}
\]

The complete vanishing group is removed before any decomposition into
ramified sectors or norms. The newly justified all-cusp factorization
then permits (5.3) on all remaining blocks. This is a theorem for the
full source family with its stated squarefree rows and auxiliaries;
it does not extend the growing mixed family required by the A2
projection.

The classical physical bound in the companion note remains available.
At `A=B=D`, the minimum of that bound, the original factorwise bound,
and (5.4) can be used. In particular (5.4) gives the smaller value
`O(D^epsilon[HD+H^2 D^(1/2)+H^(4/3)D^(2/3)])` on some short row
ranges, but it does not reach the difficult initial fourth-moment
dual scale `H` of order `D^(3-theta)` at the needed size. The analytic
continuation built from (4.5) requires a separate proof of its domains
and conductor bounds.

### Corollary 5.1. The exact short-row quantitative improvement

Set `A=B=D` and `H=D^h`, with `h>=0`. The exponent in (5.4),
apart from an arbitrarily small loss, is

\[
\begin{aligned}
P(h)
&=\max\{h+1,\ 2h+\tfrac12,\ \tfrac43h+\tfrac23\}\\
&=\begin{cases}
h+1,&0\le h\le\tfrac12,\\
2h+\tfrac12,&h\ge\tfrac12.
\end{cases}
\end{aligned}
\tag{5.5}
\]

Indeed the third term is no larger than the first when `h<=1`,
and no larger than the second when `h>=1/4`; it never controls
the maximum in (5.5). The two previously available physical bounds
are `D(H+H^2)` and `H+D^2+(HD^2)^(2/3)`, with their usual
subpower losses. Their minimum has exponent `1+2h` on
`0<=h<=1/2` and exponent `2` on `1/2<=h<=1`.
Consequently the new all-cusp bound improves that minimum by the
power

\[
\begin{cases}
D^h,&0<h\le\tfrac12,\\
D^{3/2-2h},&\tfrac12\le h<\tfrac34,
\end{cases}
\tag{5.6}
\]

up to arbitrarily small exponent losses. The largest saving is
`D^(1/2)` at `H=D^(1/2)`, where the energy bound improves from
`D^(2+epsilon)` to `D^(3/2+epsilon)`. For `h>=3/4`, the
classical physical bound is at least as strong as (5.4). Thus
`0<h<3/4` is precisely the range of strict power improvement
over the old minimum.

This is an improvement in the bound for the original completed
source family with squarefree rows, rather than only for a selected
cusp term. It does not enlarge the already available balanced
`D^(2+epsilon)` row range: the classical physical estimate already
has that size throughout `H<=D`, whereas (5.4) alone has it only
through `H<=D^(3/4)`. No conclusion for the long fourth-moment
core or for growing mixed auxiliary twists follows from (5.6).
