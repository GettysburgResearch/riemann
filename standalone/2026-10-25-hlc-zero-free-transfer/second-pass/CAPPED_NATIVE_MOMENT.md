# An actual improvement for the long native inverse

Status: proved source-dependent native inverse-moment estimate, relative to
the exact imported zero-free cap and buffered row-count theorem below.
This improves the actual Möbius coefficient on part of the length range.
It does not by itself establish a smaller global zero-free half-plane.

Scope: the original sixth-power-free Eisenstein physical rows, fixed finite
ray twists and either sextic orientation, all original natural zeros,
bounded-power common punctures, common smooth profiles, and norm heights.
No nonzero angular character is silently added to the finite-order cap.

Exact source premises:

1. `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
   `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
   Git blob `268c4e3206d460c617d3d2129742a72b831b3def`, `thm:main`:
   every finite-order Hecke L-function over the Eisenstein field has no
   zero in `Re s>7/8`. This is a cap for the relevant family, not merely
   a statement about ordinary zeta. The boundary line is allowed.
2. Xu--Sang, [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
   Lemma 6.2 and Proposition 6.3: the polynomial-height buffered bins and
   their indexed physical-row counts, with their stated order of choices.
   These are stronger inputs than the polylogarithmic-height density
   assertion in its Theorem 1.2 alone. Their proof imports the pinned
   original inverse and plain moments and simultaneous detector witnesses.
3. The ordinary finite-order Hecke functional equation, uniform polynomial
   conductor/height bounds on fixed strips, and the exact natural Euler
   factors. These give the elementary logarithmic estimates used below.

The complete external framework is not independently certified by this
deduction. In particular the all-family cap is an explicit load-bearing
source premise. No finite computation is used to infer this theorem.

## 1. The new exponent and the actual coefficient

Put `E=Q(omega)` and retain its primary ideal conventions. Let the physical
rows be sixth-power-free `u`, with `U<=Nu<2U`, outside a fixed set `S`
containing the primes above 6 and the fixed ray conductors. Take a fixed
finite ray character `nu` and either source orientation. Write

\[
 \psi_u(n)=\nu(n)\chi_n(u)^{\mathrm{sign}}1_{(n,Q_0)=1},
 \qquad \mathrm{sign}\in\{-1,1\},
 \tag{1}
\]

with the source's original zero extension and any additional common
puncture satisfying `Nrad(Q_0)<=U^{C_0}`, for a prescribed fixed `C_0`.
The inverse orientation is conjugation on units with zero on nonunits.
For `U>=3` every retained inducing character is nonprincipal: at a good
prime of `u`, its valuation lies in `1,...,5`, and the fixed `S`-supported
ray factor cannot cancel that local character. Added zeros do not change
the primitive inducing character.

For one smooth profile `W` supported in a fixed compact annulus and a
bounded nonnegative row weight, define

\[
 M_u(D,t)=D^{-1/2}\sum_n\mu_E(n)\psi_u(n)(Nn)^{it}W(Nn/D),
 \qquad
 I(U,D,t)=\sum_u w(u)|M_u(D,t)|^2.
 \tag{2}
\]

This is the original native inverse, with no Gauss coefficient replacement.
Let `D=U^r`, `1<=r<=3/2`, and put

\[
 E_0(r)=\frac{1+5r}{6},
 \qquad
 E_{\mathrm{cap}}(r)=
 \begin{cases}
 \displaystyle\frac83+\frac{5r}{2}
              -\frac{10}{\sqrt6}\sqrt r,
                  &1\le r\le200/147,\\[2mm]
 \displaystyle\frac27+\frac{3r}{4},
                  &200/147\le r\le3/2.
 \end{cases}
 \tag{3}
\]

**Theorem 1.** Under the source premises, for every `epsilon>0`, there are
fixed finite orders `A,J`, depending on the prescribed scope and epsilon,
such that

\[
 \boxed{\displaystyle
 I(U,U^r,t)
  \ll_\varepsilon U^{E_{\mathrm{cap}}(r)+\varepsilon}
           (1+|t|)^A p_J(W)^2,\qquad1\le r\le3/2.}
 \tag{4}
\]

Combining this with the pinned original native estimate gives

\[
 \boxed{\displaystyle
 I(U,U^r,t)
  \ll_\varepsilon U^{E_{\mathrm{new}}(r)+\varepsilon}
           (1+|t|)^{A'}p_{J'}(W)^2,
 \quad E_{\mathrm{new}}(r)=
 \begin{cases}
 (1+5r)/6,&1\le r\le10/7,\\
 2/7+3r/4,&10/7\le r\le3/2.
 \end{cases}}
 \tag{5}
\]

In particular,

\[
 \boxed{\displaystyle
 I(U,U^{3/2},t)
  \ll_\varepsilon U^{79/56+\varepsilon}
                 (1+|t|)^{A'}p_{J'}(W)^2.}
 \tag{6}
\]

The former exponent at that endpoint was `17/12`. Their difference is
exactly `1/168`. The gain is for the actual complete physical-row inverse,
not an estimate for a favorable Gauss column or a selected component.

**Corollary 1b (any prescribed bounded-power range).** Fix `C>=3/2`.
The same conclusions hold uniformly for `1<=r<=C`, extending the second
branches of (3) and (5) to that interval. The constants and finite height
and profile orders may depend on `C`. In particular at `D=U^2` the new
exponent is `25/14`, compared with the old `11/6`, a difference of `1/21`.

To see this, the buffered row count is independent of the length being
estimated. In the proof below choose the external Mellin order using
`D<=U^C`, and choose the large-height polynomial order after `C` and `tau`.
The capped maximum remains the endpoint line for `r>=200/147`. Its floor
competitor `1+r/50` remains smaller for every `r>=3/2`, since their
difference is `-5/7+(73/100)r>0`. The original inverse estimate is itself
stated on every prescribed bounded nonnegative length range. These facts
give the stated extension without a new detector or height theorem.

## 2. The exact buffered-bin input

Use `a_0=51/100`. Choose a sufficiently small fixed `e>0`. After fixing
the source's internal moment, detector, derivative and Sobolev losses and
orders, it permits a sufficiently small fixed `tau>0` and
`H_1=U^tau`. It partitions the physical rows into `O_e(1)` bins `(i,a)`.
There is a fixed finite family of presentation labels, including the chosen
fixed ray character and both orientations. For every label on a row in
that bin, the enlarged rectangle contains no primitive zero with

\[
 \Re s\ge a+2e,\qquad |\Im s|\le3(i+1)H_1.
 \tag{7}
\]

The bottom bins have `a=a_0` and at most `O(U)` rows. Above-floor bins obey

\[
 \#\mathcal B_{i,a}\ll_{e,\eta}U^{R(a)+\eta},
 \qquad
 R(a)=\frac{31-32a}{21-12a}\quad(a\le11/12),
 \tag{8}
\]

for an arbitrarily small preassigned loss `eta`, with the polynomial-height
cost absorbed by choosing `tau` sufficiently small. The source also has a
second branch for larger `a`, but it is not needed here.

The cap in premise 1 applies to every finite-order inducing character in
these labels and at every height. Hence the rightmost-zero maxima used to
assign a bin are at most `7/8`, and every assigned bin has

\[
                         a\le7/8.
 \tag{9}
\]

This step is what was absent in the uncapped feedback calculation. A
zero at `Re s=7/8` is permitted and remains in the top bin. The buffer
still moves the contour strictly to its right.

Extra natural Euler deletions have no zeros in `Re s>0`; adding the
common puncture in (1) therefore does not invalidate (7) or alter the
primitive zero-bin assignment. Its contribution to analytic growth is
included below. No claim that a polylogarithmic density theorem is
automatically uniform at polynomial height is being made.

## 3. A local reciprocal estimate with subpower conductor cost

Let `L_orig(s,psi_u)` denote the exact natural Dirichlet series of (1).
Its primitive conductor has norm `O_S(U)`. Its extra Euler deletion radical
has norm at most `U^{C_1}`, for a prescribed fixed `C_1` depending on `C_0`
and the original presentation. The exact factorization is

\[
 L_{\mathrm{orig}}(s,\psi_u)
   =L(s,\psi_u^*)\prod_{\mathfrak p\in\mathcal E_u}
        (1-\psi_u^*(\mathfrak p)(N\mathfrak p)^{-s}).
 \tag{10}
\]

Uniform polynomial conductor/height growth of the primitive Hecke function,
together with the elementary upper bound for the finite product, gives

\[
 \log|L_{\mathrm{orig}}(\sigma+iv,\psi_u)|
       \le C\log U
 \tag{11}
\]

on every fixed strip containing `a_0<=sigma<=6`, for `|v|<=H_1`, after
enlarging the constant. An upper bound is all that is used here. For example
the logarithm of the absolute finite product is at most a constant times
`log Nrad(E_u)`, since each factor has modulus at most two and every prime
has norm at least two. The source's much finer deleted-factor estimates
are unnecessary for this bound.

**Lemma 2.** For every fixed `eta>0`, on a row in bin `(i,a)`,

\[
 |L_{\mathrm{orig}}(\sigma+iv,\psi_u)|^{-1}
  \ll_{e,\eta} U^\eta,
 \quad a+8e\le\sigma\le2,\quad |v|\le H_1/2,
 \tag{12}
\]

for sufficiently large `U`, with the bounded range absorbed into the
constant.

**Proof.** Fix `v` in the displayed range and center a disk at `3+iv`.
Put

\[
 R_0=3-a-2e,\qquad R_1=3-a-4e,\qquad R_2=3-a-8e.
 \tag{13}
\]

For the allowed small `e`, `1<R_2<R_1<R_0<3`. If `U` is sufficiently
large then the disk of radius `R_0` lies in the buffered zero-free
rectangle (7). The natural Euler factors are also nonzero there. The
nonprincipal inducing function has no pole. There is therefore a
holomorphic logarithm `f(s)=log L_orig(s,psi_u)` on this disk, fixed by
the Euler-product branch at its center.

On the concentric disk of radius one, `Re s>=2`, so the absolutely
convergent Euler logarithm is bounded by a field constant, uniformly in
the conductor, row, height and all deletions. On the disk of radius `R_0`,
(11) bounds the real part of `f` by `C log U`, while its center value is
bounded. Borel--Caratheodory consequently gives

\[
             \max_{|s-(3+iv)|\le R_1}|f(s)|
                            \ll_e\log U.
 \tag{14}
\]

Hadamard's three-circles theorem, applied to this holomorphic logarithm
between radii `1,R_2,R_1`, now gives

\[
 \max_{|s-(3+iv)|\le R_2}|f(s)|
       \ll_e(\log U)^{\theta(a,e)},\qquad
       \theta(a,e)=\frac{\log R_2}{\log R_1}<1.
 \tag{15}
\]

The parameters `a` lie in a fixed compact interval; hence their exponents
are uniformly bounded above by a number `theta_e<1`. In particular the
right side is `o(log U)`. Every point `sigma+iv` with
`a+8e<=sigma<=2` lies in the disk of radius `R_2`. Exponentiating
`-Re f` proves (12), with an arbitrarily small fixed `eta` and a
corresponding constant. The construction is uniform in `v`, since the
extra imaginary radius is less than three and fits well inside (7).
QED.

Only a local zero-free rectangle is used. A fixed global zero-free theorem
at the bin's left edge is not assumed. The nonvanishing logarithm and its
Euler normalization are the essential reason for retaining the natural
presentation and excluding principal inducing rows before this step.

## 4. Shift the actual inverse, without a fractional-power substitution

Initially on `Re s=2`, exact Euler inversion gives

\[
 M_u(D,t)=\frac1{2\pi i}\int_{(2)}
   \frac{D^{s-1/2}\widehat W(s)}
        {L_{\mathrm{orig}}(s-it,\psi_u)}\,ds.
 \tag{16}
\]

Every original natural zero in (1) is present in this inverse Dirichlet
series. In particular the coefficient in (16) is precisely `mu_E(n)psi_u(n)`.

First suppose `|t|<=H_1/4`. Put `H=H_1/4` and move only the segment
`|Im s|<=H` to `Re s=alpha=a+8e`. On this rectangle
`|Im(s-it)|<=H_1/2`, so Lemma 2 applies. There are no poles to cross.
The shifted vertical integral is bounded by

\[
        C_{e,\eta}D^{a-1/2+8e}U^\eta p_2(W).
 \tag{17}
\]

For any fixed integer `J`, the horizontal pieces are bounded by
`C D^{3/2}U^eta H^{-J}p_J(W)`. On the unshifted line, absolute Euler
convergence bounds the reciprocal independently of the row and height,
so the two tails are at most `C D^{3/2}H^{1-J}p_J(W)`.
Since `D<=U^{3/2}`, choosing `J` sufficiently large *after* `tau` makes
all these tails `O(U^{-10})p_J(W)`. These are external Mellin derivatives;
their order does not change the internal source height exponent used
to choose `tau`.

Thus, on every row in bin `(i,a)`,

\[
 |M_u(U^r,t)|
  \ll U^{r(a-1/2)+8er+\eta}p_J(W)+U^{-10}p_J(W),
       \qquad |t|\le U^\tau/4.
 \tag{18}
\]

For larger `|t|`, the elementary absolute coefficient bound gives
`I(U,D,t)<<UD p_0(W)^2`. By enlarging one fixed polynomial height order
`A` (for example any `A>4/tau` suffices after harmless bounded ranges),
this is absorbed by the right side of (4) times `(1+|t|)^A`.
Consequently proving (4) in the small-height range proves the stated
all-height version. The consumer can choose its small allowed height
only after this fixed finite `A` has been selected.

The same argument is uniform over a prescribed bounded smooth profile
family. Rowwise norm heights in the same bounded range can be retained
because (18) is pointwise and uniform in the height; no common maximizing
row or independent arbitrary-coefficient sieve is used.

## 5. Sum the actual physical rows

Square (18), sum over a bin, and use (8). Above-floor bins give

\[
 I_{i,a}(U,U^r,t)
  \ll U^{R(a)+(2a-1)r+O(e)+O(\eta)}p_J(W)^2,
        \qquad a_0<a\le7/8.
 \tag{19}
\]

The finitely many floor bins give
`U^{1+r/50+O(e)+O(eta)}`. Their exponent is at most `1.03` for this
length range. It is strictly smaller than the maximum in (19), which
at `r=1` already exceeds `1.08` and is increasing in `r`. The floor
bins therefore introduce no hidden near-critical density assumption.

The function `R` is strictly concave, and

\[
 R'(a)=-\frac{300}{(21-12a)^2}.
 \tag{20}
\]

Its unconstrained maximizer in (19) is

\[
                 a_*(r)=\frac{21-\sqrt{150/r}}{12}.
 \tag{21}
\]

This lies below `7/8` exactly when `r<=200/147`; substituting it gives
the first branch of (3). Beyond that threshold the maximum is attained
at the allowed top endpoint, where

\[
                 R(7/8)=2/7,\qquad 2(7/8)-1=3/4.
 \tag{22}
\]

This proves the second branch. Given the requested final epsilon, first
choose `e` and the preliminary count and reciprocal losses small enough;
then choose the source's internal orders and `tau`; then choose the
external Mellin order `J`. All these quantities are fixed before `U,D`
vary. Summing the `O_e(1)` bins proves (4).

On the first branch,

\[
 E_{\mathrm{cap}}(r)-E_0(r)
       =\frac53(\sqrt r-\sqrt{3/2})^2\ge0.
 \tag{23}
\]

On the capped linear branch,

\[
 E_0(r)-E_{\mathrm{cap}}(r)=\frac r{12}-\frac5{42}.
 \tag{24}
\]

It is positive exactly when `r>10/7`. This proves (5), and evaluating
at `r=3/2` gives (6).

## 6. What changed, and what still has to be consumed

The original fractional-count idea led to the question, but its interpolation
and branch cuts are unnecessary for this estimate. The buffered bins already
supply a zero-free contour for each row. Interpolating the holomorphic
logarithm between an Euler-product disk and a larger zero-free disk makes the
reciprocal cost subpower. The imported all-family `7/8` cap removes precisely
the high bins that defeated the uncapped estimate. These two facts act on the
actual inverse coefficient before any Gauss transformation.

Within the current consumer rectangle, this gain has the explicit location
`10/7<log D/log U<=3/2`. It leaves the shorter part of that rectangle at
the old exponent; Corollary 1b also controls longer bounded-power lengths.
For example the proposed `4/5` consumer at `r=3/2` asks for exponent
`1/6+(4/5)(3/2)=41/30`; the new `79/56` is still larger by `37/840`.
Thus this theorem does not establish that complete consumer.

The full detector optimization must determine whether a different consumer
can use the long-length gain. A smaller zero-free boundary is not inferred
from (6) alone. The cap, original row-count estimate, and all coefficient,
height and profile scopes must remain attached to any such application.
