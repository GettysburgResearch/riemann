# A restricted short inverse gain and the exact density-feedback test

Status: a source-dependent estimate for the **actual native inverse on
specified detected amplitude classes**, followed by an exact consumer
calculation and two further analytic tests. The restricted estimate saves
a fixed power already at length `D=U^(7/5)`, before the unrestricted
`10/7` contact of the second pass. It does not improve the critical class
that determines the currently imported global boundary.

This note does not replace a restricted row set by the full physical
family. It does not claim a new zero-free half-plane or RH. The external
analytic framework remains an explicit premise.

## 1. Source scope and the new restriction

The arithmetic setting is the original sixth-power-free Eisenstein
physical family of `../second-pass/CAPPED_NATIVE_MOMENT.md`: fixed finite
ray data, either original sextic orientation, the original zero extension,
common smooth annular profiles, and norm heights. The polynomial is

\[
 M_u(D,t)=D^{-1/2}\sum_n\mu_E(n)\psi_u(n)(Nn)^{it}W(Nn/D).
 \tag{1}
\]

Thus the coefficient is the actual Möbius coefficient. No Gauss weight or
arbitrary coefficient operator norm has been substituted.

The source premises for the extra amplitude restriction are:

* Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
  Proposition 2.7, with its retained detector, coefficient, profile,
  same-character, height, and prime-supply hypotheses. The prime
  supports must satisfy the source disjointness and mesh conditions.
  Full supply means `ell/d >= 1/5+rho_sup` for a fixed positive
  `rho_sup`. The moment parameter satisfies `13/18 <= kappa <= 1`
  and the family ceiling `beta_* <= (1+kappa)/2`.
* Xu--Sang, [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
  Lemma 6.2 and its order of choices, supplies the polynomial-height
  buffered zero bins and common detector witnesses.
* The all-family finite-order cap can be the pinned `7/8` premise of
  the second pass. Alternatively Liu's Main Theorem / Theorem 17.1
  asserts the cap `B_flat` over every number field, so it applies to
  this finite-order Eisenstein family. It licenses
  `kappa=kappa_flat=2B_flat-1`, with
  `0.749773294079928 < kappa_flat < 0.749773294079929`.

These are finite-order assertions. A nonzero angular character has not
been added to their scope. The prime-amplitude character must be the
**same source character** as the two detector witnesses. A buffered
maximum over several presentation labels does not license transferring
an amplitude from one label to another. A "detected amplitude class"
below means a source-licensed class after the required presentation split,
with these compatibility conditions retained. Finite unions of compatible
classes are allowed.

The finitely excluded inducing characters are treated as in the source.
For a nonunit physical row, a fixed character supported on the fixed bad
set cannot cancel the nontrivial local character at a good prime of the
row. Principal rows are not inserted into this nonprincipal moment.

Write

\[
 \alpha=\frac56,\quad c=\frac{2}{3\kappa},\quad
 D_\kappa(x)=3-(1+c)x,\quad P_\kappa(x)=(2-cx)(1-x).
 \tag{2}
\]

If the zero bin is `a`, set `delta=2a-1`. Let `G` be the source's
absolute weighted mean prime amplitude. Its normalized value is
`x=G/delta`; the buffered pointwise prime estimate gives
`0 <= x <= 1/2`, up to the reserved rounding losses. Put

\[
 C_\kappa(\delta,x)=\frac{\delta P_\kappa(x)}{D_\kappa(x)},\qquad
 R_\kappa(\delta,x)
 =1-\delta+
   \frac{(\alpha-\delta)C_\kappa(\delta,x)}
        {2(\alpha-\delta+C_\kappa(\delta,x))}.
 \tag{3}
\]

The source counts a compatible detected class by
`U^(R_kappa(delta,x)+epsilon)`, with a fixed polynomial height factor.
This is a class count, not a bound for arbitrary externally selected
prime polynomials.

For a fixed threshold `g>1/100`, let `B_{>=g}` be a union of the
compatible classes with `G>=g`. This avoids the floor bin
`a_0=51/100`; the example below has `g=37/100`. Let the available
cap be `b<=7/8` and put `delta_b=2b-1`. We assume
`1/100<g<delta_b/2`, so the interval below is nonempty.

## 2. Actual inverse estimate on these classes

For `2g<=delta<=delta_b`, define

\[
 C_g(\delta)
 =\frac{(2\delta-cg)(\delta-g)}
        {3\delta-(1+c)g},\qquad
 R_g(\delta)
 =1-\delta+
   \frac{(\alpha-\delta)C_g(\delta)}
        {2(\alpha-\delta+C_g(\delta))}.
 \tag{4}
\]

These equal `C_kappa(delta,g/delta)` and
`R_kappa(delta,g/delta)`. Set

\[
 \mathcal E_g(r)
 =\max_{2g\le\delta\le\delta_b}
       \{R_g(\delta)+\delta r\},\qquad
 e_0(r)=\frac{1+5r}{6}.
 \tag{5}
\]

**Theorem 1 (amplitude-conditioned native moment).**
Fix `1<=r<=C`. Under the stated source premises, for each
`epsilon>0` there are finite profile and height orders `J,A` such that

\[
 \sum_{u\in B_{\ge g}}w(u)|M_u(U^r,t)|^2
 \ll_\varepsilon
 U^{\min\{e_0(r),\mathcal E_g(r)\}+\varepsilon}
 (1+H)^A p_J(W)^2.
 \tag{6}
\]

Here `w` is bounded and nonnegative; `H` bounds the norm height in
(1) and the prime-profile heights. Constants may depend on the fixed
arithmetic data, prime system, supply margin, `g,C`, and epsilon.
They are uniform in the row, `U`, and allowed profile parameters.

Additional common natural punctures of bounded-power radical are
permitted in the inverse (1). The defining prime classes retain their
source-compatible character and prime factors. This does not assert
that an arbitrary new puncture can be inserted into the amplitude
definition without checking that definition.

**Proof.** The elementary identity

\[
 \frac{\partial}{\partial x}\frac{P_\kappa(x)}{D_\kappa(x)}
 =\frac{-(4+c)+6cx-c(1+c)x^2}{D_\kappa(x)^2}<0
 \quad(0\le x\le1/2)
 \tag{7}
\]

holds in the stated range. Formula (3) is increasing in
`C_kappa`, since `alpha-delta>0`. On a bin in `B_{>=g}`,
`x>=g/delta`, so its count is at most
`U^(R_g(delta)+epsilon)`. The pointwise amplitude constraint gives
`delta>=2g`, with the small mesh errors reserved until the end.

On that same buffered bin, the local logarithm argument and finite-height
Mellin shift of `CAPPED_NATIVE_MOMENT.md` give

\[
 |M_u(U^r,t)|^2
 \ll U^{\delta r+O_C(e)+\eta}p_J(W)^2
 \qquad (|t|\le U^\tau/4).
 \tag{8}
\]

The estimate uses the Euler branch of `log L_orig` on a zero-free disk
centered at `3+iv`. The logarithm is bounded on an Euler disk of radius
one. Borel--Caratheodory and three circles then give
`|log L_orig| << (log U)^theta`, for a fixed `theta<1`, on a smaller
buffered disk. Hence `1/L_orig << U^eta` on the shifted segment.
The shifted real part is `a+8e`, producing
`D^(2a-1+16e)` in the square.

The extra natural factors have no zero in `Re s>0`. Their logarithmic
growth is `O(log U)` when the puncture radical is a bounded power of
`U`, so the same disk estimate applies. They change neither primitive
zeros nor the compatible class count.

Fix the internal moment, detector and Sobolev orders first, and then
choose `tau` to absorb their polynomial height costs. Choose the
external Mellin order afterwards using `D<=U^C`. It makes the
truncated tails negligible without increasing those internal orders.
This uses the polynomial-height buffered input; it is not an asserted
extension of a polylogarithmic-height theorem.

Multiply (8) by the class count and sum the finitely many
zero/amplitude/presentation bins. Their exponent is (5). The exponent
functions are uniformly Lipschitz on this compact range, so mesh
errors fit in the reserved epsilon. For larger `H`, the elementary
bound `O(UD)` for the squared row sum is absorbed by a fixed power of
`1+H`. Restricting the original full-row inverse bound to this
nonnegative subset gives the alternative exponent `e_0(r)`.
\(\square\)

## 3. A strict saving at length 7/5

The next corollary uses only the weaker cap `b=7/8` and
`kappa=3/4`. It is consequently also available when the stronger
Liu cap is imported.

Take `g=37/100`. For `2g<=delta<=3/4` write
`A=alpha-delta` and `C=C_g(delta)`. The inequalities

\[
 C>0,\quad C'>0,\quad C\le\frac{2\delta}{3}\le\frac12,
 \qquad A\ge\frac1{12}
 \tag{9}
\]

follow from (7) and

\[
 2D_\kappa(x)-3P_\kappa(x)=x(4+c-3cx)\ge0.
 \tag{10}
\]

Indeed `C_g(delta)=delta f(g/delta)` with `f>0,f'<0`, whence
`C_g'=f-(g/delta)f'>0`. Differentiating gives

\[
 \frac{d}{d\delta}\{R_g(\delta)+r\delta\}
 =r-1+\frac{-C^2+A^2C'}{2(A+C)^2}
 \ge r-1-\frac{18}{49}.
 \tag{11}
\]

Thus the maximum in (5) is at `delta=3/4` whenever `r>=67/49`.
At `r=7/5` the derivative margin is at least `8/245`.
Exact rational calculation gives

\[
 R_g(3/4)=\frac{87541}{310112},\qquad
 \mathcal E_g(7/5)=\frac{87541}{310112}+\frac{21}{20}
                 =\frac43-\frac{4861}{4651680}.
 \tag{12}
\]

**Corollary 2.** On the compatible classes with absolute mean
amplitude at least `37/100`,

\[
 \boxed{\displaystyle
 \sum_{u\in B_{\ge37/100}}w(u)|M_u(U^{7/5},t)|^2
 \ll_\varepsilon
 U^{\,4/3-4861/4651680+\varepsilon}
 (1+H)^A p_J(W)^2.}
 \tag{13}
\]

The original inverse exponent is `4/3`. The saving
`4861/4651680` is approximately `0.001044998796`.
The endpoint line meets the old inverse line at

\[
 r_g=\frac{107567}{77528}
       =1.3874600144\ldots<\frac75<\frac{10}{7}.
 \tag{14}
\]

For `r>r_g` the new restricted line is a strict improvement;
`r_g>67/49` ensures the endpoint argument applies. This is an
actual native mean on an explicitly restricted sector. It is not a
mean over every physical row.

## 4. Exact contact for every individual amplitude class

Fix a target class `(delta_0,g)` with
`0<2g<=delta_0<=delta_b`, and put

\[
 C_0=C_g(\delta_0),\quad A_0=\alpha-\delta_0,\quad
 t_0=1+\frac{C_0}{2(A_0+C_0)},\quad R_0=R_g(\delta_0).
 \tag{15}
\]

The old short and long count exponents are

\[
 S_0(t)=1-\delta_0+C_0(3/2-t),\qquad
 L_0(t)=\frac16+(\alpha-\delta_0)t.
 \tag{16}
\]

They meet at `t_0`. Exact substitution gives

\[
 S_0(t_0)=L_0(t_0)=R_0,\qquad
 R_0+\delta_0t_0=e_0(t_0).
 \tag{17}
\]

The class itself supplies one of the competitors in (5), hence

\[
 \mathcal E_g(t)\ge R_0+\delta_0t
 \quad\hbox{for every }t.
 \tag{18}
\]

At `t=t_0` the minimum of `e_0` and `mathcal E_g` still equals
`e_0(t_0)`. For `t>=t_0` both long counts
`e_0(t)-delta_0t` and `mathcal E_g(t)-delta_0t` are at least
`R_0`. For `t<=t_0` the short count is at least `R_0`. Therefore

\[
 \boxed{\displaystyle
 \min_{1\le t\le3/2}
 \max\{S_0(t),\min(e_0(t),\mathcal E_g(t))-\delta_0t\}=R_0.}
 \tag{19}
\]

The proof uses an included line, not sampled minimization or an assumed
monotonicity of the whole envelope. It remains valid with the stronger
`B_flat` ceiling and the refined moment parameter.

It also describes the independent density bootstrap. Starting with
the source counts (3), converting them to inverse moments by (5),
and feeding those moments through this detector returns the same
counts. Repeating that operation cannot make a strict first step.

Conditioning further on the inverse witness being large does not
automatically help. If `N` rows in one bin obey
`|M|^2 >= U^(delta_0 r-eta)`, the pointwise upper bound supplies only

\[
 \sum_{\text{those rows}}|M|^2
       \ll N U^{\delta_0r+O(e)+\eta}.
 \tag{20}
\]

Markov then gives `N << U^(O(e)+2eta) N`. A strict improvement
requires new joint information on the inverse values and row
selection. Inserting the existing bound for `N` reproduces (18).

**Detector consequence.** In particular, (13) does not exclude a new
local zero sector. Each retained class keeps its old optimized count,
which is positive. It improves the bound on the sum of long inverse
values in that sector, while this detector's conclusion is unchanged.
This is a scoped fixed-point result for the stated estimates, not an
impossibility theorem for a different detector or a new mixed moment.

## 5. Test at the actual Liu critical class

Liu Lemma 14.9 identifies the critical class for the refined numerator
consumer by `x=1/2` and the root in `(23/50,12/25)` of

\[
 (3-324\kappa^2)\delta^2+
 (756\kappa^2-54\kappa-5)\delta+
 40\kappa-300\kappa^2=0.
 \tag{21}
\]

At the limiting parameter, the diagnostic values are:

| Quantity | Value |
|---|---:|
| `kappa_flat` | `0.7497732940799282618892...` |
| `delta_c` | `0.4693448586981430674936...` |
| `g_c=delta_c/2` | `0.2346724293490715337468...` |
| `t_c` | `1.1639535765090109563153...` |
| `R_c` | `0.5903323535263557935930...` |
| `e_0(t_c)` | `1.1366279804241757969294...` |

These are evaluations of explicit formulas. Equation (17), not the
digits, proves contact at this class.

As an additional diagnostic, an interior stationary competitor in
`mathcal E_{g_c}(t_c)` has value approximately
`1.1636440766020647` near `delta=0.6620488728373521`. This
competitor alone exceeds `e_0(t_c)` by about `0.02701609618`,
so the usable minimum selects the original inverse estimate.
The high-amplitude corollary (13) does not cover `g_c`, which is
well below `37/100`.

Lowering only the family ceiling from `7/8` to `B_flat` does not
remove this class from the maximization: `delta_c<kappa_flat`.
The included-line proof survives that stronger import.

## 6. A separate simultaneous-witness test

Let the common-character inverse/plain witnesses be `M_r,S_m`,
with `r+m>=t`. Using only the supplied inverse second moment and
plain fourth moment, Hölder gives

\[
 \sum_u |M_r(u)|^{4/3}|S_m(u)|^{4/3}
 \le
 \left(\sum_u|M_r(u)|^2\right)^{2/3}
 \left(\sum_u|S_m(u)|^4\right)^{1/3}.
 \tag{22}
\]

On the simultaneous witness set, the count exponent is

\[
 \frac23\{E(r)-\delta r\}
 +\frac13\{1-2\delta m\}.
 \tag{23}
\]

This is a convex combination of the individual count exponents and
cannot beat their minimum. The same observation covers intermediate
Hölder allocations from just these marginal moments.

The exact identity `mu_E*1=delta_1` cancels the complete product of
inverse and ordinary Dirichlet series. The detector supplies truncated
dyadic blocks. Their product is a restricted divisor sum, not zero;
omitting the complementary divisor ranges destroys the identity.
A mixed estimate for these blocks is additional arithmetic information.

Asking one zero for witnesses at several cutoffs also does not by itself
give a power saving: the existing marginal estimates permit the same
rows to saturate each cutoff. A cross-scale estimate is needed.

## 7. Rough-factor parity after the growing-prefix theorem

The prefix theorem in `../second-pass/FRACTIONAL_NATIVE.md` gives
a second independent starting point. Set `Y=(log D)^2`, take a
profile supported in `(1,2)`, and form the Hilbert-space polynomial

\[
 F_D(z)=D^{-1/2}\left(
   \sum_n\mu_E^2(n)(-1)^{\omega_{\le Y}(n)}
        z^{\omega_{>Y}(n)}\psi_u(n)W(Nn/D)
                  \right)_u .
 \tag{24}
\]

Its degree is at most `R=floor(log(2D)/log Y)`, hence
`R=O(log D/log log D)`. The proven endpoint `z=1` has row-volume
norm; `z=-1` is the full Möbius vector. The low degree alone does
not control the latter value.

### 7.1 Cost in the new rough direction

At a rough prime the exact Euler quotient is

\[
 \frac{1+zX}{1+X}
 =1+(z-1)\sum_{j\ge1}(-1)^{j-1}X^j.
 \tag{25}
\]

The positive convolution transfer from the prefix endpoint has cost

\[
 \sum_{Nd\le2D}\frac{|b_z(d)|}{\sqrt{Nd}}
 \ \ge\
 |z-1|\sum_{Y<Np\le D}\frac1{\sqrt{Np}}.
 \tag{26}
\]

The prime-ideal sum has order `sqrt(D)/log D` over this fixed field.
Thus this particular transfer can retain a subpower cost only in a
window `|z-1| <= D^(-1/2+o(1))`. Its full Euler-product upper bound
does give power-thin windows, but not a fixed rough-parameter interval.
Already the first derivative, which marks one arbitrary rough prime,
contains the cost in (26).

Degree-`R` extrapolation from width `h` around 1 to -1 has a factor
of scale `(C/h)^R` in general. The example `(z-1)^R v` for a
nonzero Hilbert vector exhibits the `h^(-R)` dependence. At the
available scale,

\[
 \log(h^{-R})\asymp
       \frac{(\log D)^2}{\log\log D}.
 \tag{27}
\]

This exceeds a fixed multiple of `log D`. A subpower extrapolation
with this degree would instead need `log(1/h)=o(log log D)`.

### 7.2 Components and norm twists

Writing `F_D(z)=sum_k v_k z^k`, the endpoint bounds
`||sum_k v_k||`, not `sum_k ||v_k||^2`. For example
`v_1=v,v_2=-v` cancel at 1 and add at -1. A circle estimate would
give

\[
 \frac1{2\pi}\int_0^{2\pi}\|F_D(e^{i\theta})\|^2\,d\theta
       =\sum_k\|v_k\|^2
 \tag{28}
\]

and Cauchy--Schwarz would then cost only `sqrt(R+1)` at -1.
No such circle estimate follows from the endpoint. Formula (28)
identifies a missing positive norm, not a proved new mean.

The twist `n -> exp(i theta omega_{>Y}(n))` is neither a norm-height
character nor a fixed finite-order Hecke character. Uniform norm-height
control cannot be substituted for (28). Approximating these prime
phases by a Bohr/Kronecker argument would require a quantitative height
bound whose polynomial source cost remains subpower. That input is
absent from the supplied estimates.

### 7.3 Finite marks versus an exact full decomposition

The factorial mark theorem guarantees row volume in its stated regime
`k log Y=o(log D)`. This suffices for the finite HLC band polynomials
in the second pass, but does not cover parity at every prime up to `D`.

An elementary exact Heath--Brown truncation based on a Möbius
polynomial through `Y` instead requires `Y^K>D`. Indeed if
`M_Y(s)=sum_{Nn<=Y} mu_E(n)psi(n)(Nn)^(-s)`, then
`1-L(s)M_Y(s)` has no coefficient of norm at most `Y`, so its
`K`th power first occurs beyond `Y^K`. The exact identity through
`D` thus needs `K log Y >= log D`, up to endpoint conventions.
This is outside the guaranteed little-o mark regime. Growing `K`
also needs quantitative moments, profile orders and constants for a
growing number of factors; the fixed-factor source statements do not
supply them.

These tests do not rule out new cancellation for rough coefficients.
They show why the available prefix, finite-mark and norm-height
conclusions do not yet supply that cancellation.

## 8. Outcome and verification

The proved new component is (6), with the explicit shorter-length
saving (13). Its hypotheses retain the row restriction, character
compatibility, full prime supply, finite-order scope, masks, and
height/profile budgets.

The exact identities (17)--(19) show that the independent density
feedback leaves every class at its previous detector crossing. At
the global critical amplitude, the old inverse is still the better
available bound. Neither a new global boundary nor a new local
zero-free sector follows here.

The companion `check_short_inverse.py` checks the rational saving
and contact exactly, exercises the displayed algebraic identities on
rational inputs, and reproduces the critical decimals as diagnostics.
Finite arithmetic checks do not certify the imported analytic
theorems, extend their hypotheses, or establish RH.
