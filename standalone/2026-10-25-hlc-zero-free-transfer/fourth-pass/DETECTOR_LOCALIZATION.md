# Localization of an actual inverse witness near the full ratio length

**Status: proposed source-dependent reduction, with a complete conditional
consumer and an open residual estimate.** This note uses the pointwise
same-bin estimate and the restricted returned-component theorem proved in
`MIDDLE_JOINT.md`. It does not establish a new zero-free half-plane.

The new conclusion is stronger than a full-family component estimate in
one particular respect: a detected large inverse cannot be supplied by
the coherent reduced-ratio head through `D/U^(1/100)`. After bounding a
further actual component, only the explicit large-divisor expression
(9) below can supply the remaining witnesses. Its norm or spike count is
still open. No independence between the different decompositions is
asserted.

## 1. Exact source and parameter scope

Use the original sixth-power-free Eisenstein physical rows of norm
`Nu` comparable to `U`, finite-order fixed ray twists, either sextic
orientation, the original natural zero extension, and the nonprincipal
inducing family. A common puncture has radical norm at most `U^C_Q`
for any prescribed fixed `C_Q`. Write

$$
 \psi_u=\psi_u^*1_{(\,\cdot\,,Q_s)=1},\qquad
 P_u=\operatorname{rad}(\mathfrak f_uQ_s).
 \tag{1}
$$

Primitive conductor primes and the redundant natural deleted primes are
both included in `P_u`; the puncture is not inserted into the primitive
conductor. Bounded principally induced exceptions have to be handled in
the complete source expression, as in the imported consumer. Nonzero
angular characters are not added to the finite-order cap.

The analytic imports are the pinned OpenAI framework
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
blob `268c4e3206d460c617d3d2129742a72b831b3def`; Xu--Sang's buffered
bins in [arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2),
Lemma 6.2; and the original Eisenstein consumer in
[arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2). Their complete
external proofs are explicit premises, not independently certified here.

The immediate new dependencies are the exact same-bin return and the
small-divisor high-ratio estimate in `MIDDLE_JOINT.md`. Their algebra
extends the third-pass `GCD_FOURTH_COMPONENT.md` and
`RATIO_CUTOFF_RETURN.md`, frozen at
`820b99562e3b458021a6de74802293baafbe5190`.

Fix

$$
 \frac{29}{25}\le r\le\frac{117}{100},\qquad D=U^r,
 \quad \alpha=\frac{2}{125},\quad \varkappa=\frac1{100},
 \quad y_1=U^\alpha,\quad y_2=2D/U^\alpha.
 \tag{2}
$$

Let `w_0,chi` be fixed smooth cutoffs taking values in `[0,1]`, equal
to one through one and zero from two onward. The profile `V` is common
and smooth, supported on the original `(1,2)` norm annulus, and may
include its licensed norm height. Put

$$
 A(q)=\sum_{ab=q}\mu_E(a)\mu_E(b)
               w_0(Na/y_1)w_0(Nb/y_2),\qquad
 C_a(P)=\sum_{(d,P)=1}\frac{A(ad)}{Nd}.
 \tag{3}
$$

All support through norm `8D` is retained in (3). The factors `a,b`
are not made coprime, and repeated-prime terms remain. The exact
unequal-cutoff identity gives, for sufficiently large `U`,

$$
 M_u(D;V)=-D^{-1/2}\sum_{m,c}A(m)\psi_u(mc)V(Nmc/D).
 \tag{4}
$$

Bounded ranges are absorbed in constants. The possibly large threshold
is not a finite zero-height verification.

## 2. Three exact coherent components

Choose the two linked scales

$$
 B=D/U^\varkappa,
 \qquad K=B/(4U).
 \tag{5}
$$

In particular `K=U^(r-1.01)/4`, so the lower exponent in the large
divisor component is at least `3/20`; throughout the interval it ranges
from `.15` to `.16`. The factor four is retained to give room for the
smooth transition.

For any bounded selector `F`, the exact inverse reflection from the
third pass is

$$
 M_{F,u}=-D^{-1/2}
 \sum_{(k,P_u)=1}\frac{\mu_E(k)}{Nk}
 \sum_{m,c}C_{km}(P_u)\psi_u(mc)
                  F(Nkm/B)V(Nmc/D).
 \tag{6}
$$

This is a finite outer sum; no condition is inserted between `m,c`.
The formula keeps the primitive dual's Euler-restoration sum before the
inverse functional equation. In particular it does not replace a
primitive value at a deleted prime by its zero natural value. The
character of `k` cancels only on `(k,P_u)=1`, leaving exactly the
displayed indicator and weight `1/Nk`.

Define the head by

$$
 H_u=M_{\chi,u}.
 \tag{7}
$$

Define the small-divisor high-ratio component by

$$
 S_u=-D^{-1/2}
 \sum_{(k,P_u)=1}\frac{\mu_E(k)}{Nk}\chi(Nk/K)
 \sum_{m,c}C_{km}(P_u)\psi_u(mc)
       [1-\chi(Nkm/B)]V(Nmc/D),
 \tag{8}
$$

and its complement by

$$
 R_u=-D^{-1/2}
 \sum_{(k,P_u)=1}\frac{\mu_E(k)}{Nk}[1-\chi(Nk/K)]
 \sum_{m,c}C_{km}(P_u)\psi_u(mc)
       [1-\chi(Nkm/B)]V(Nmc/D).
 \tag{9}
$$

Then the literal identity is

$$
                       M_u=H_u+S_u+R_u.
 \tag{10}
$$

Indeed, the three weights sum to one for every `k,m`. For the full
selector, substitution of (3), followed by `v=kd`, gives

$$
 \sum_{(k,P)=1}\frac{\mu(k)}{Nk}C_{km}(P)
 =\sum_{(v,P)=1}\frac{A(mv)}{Nv}\sum_{k\mid v}\mu(k)
 =A(m).
 \tag{11}
$$

This verifies (10) directly without appealing to a decomposition of
unsigned norms.

Every nonzero term of `R_u` obeys

$$
 Nk>K=\frac{D}{4U^{1+\varkappa}},\qquad
 Nkm>B=\frac{D}{U^\varkappa},\qquad Nkm<8D.
 \tag{12}
$$

These are restrictions on the auxiliary divisor `k` and the actual
reduced numerator `km`. They do **not** impose `Nm>B`: the returned
primal variable can still have the old critical length. This distinction
is necessary for consistency with the third-pass return theorem.

## 3. The head cannot carry a saturated buffered witness

Let `u` lie in one actual above-floor buffered bin, with
`delta=2a-1`. Use the same finite family of presentations and the
same enlarged height window for every Mellin variable. The pointwise
same-bin estimate proved in `MIDDLE_JOINT.md` is

$$
 |H_u|\ll_\epsilon (B/D)^{1/8}U^{\delta r/2+\epsilon}
       =U^{\delta r/2-1/800+\epsilon}.
 \tag{13}
$$

Fixed height and profile factors have been absorbed by the source's
order of choices: fix the desired loss, derivative orders and buffer
first, then choose the small positive height exponent, then choose
external tail orders. A sufficiently small preliminary loss in the
scalar cap `beta>7/8` gives the exponent `1/8` with the displayed
arbitrary final epsilon. It is not an assertion at `beta=7/8` without
losses. The original puncture has the prescribed polynomial radical.

For clarity, (13) is a pointwise statement before a row count is used.
On a dyad `Na` comparable to `B'`, the fixed-`k` coefficient bound
gives `(B'/D)^(1/8)(B'/Nk)^(delta/2)`; inverse reflection gives an
ordinary block of length `D/(B'/Nk)`, whose same-bin bound is
`(D/(B'/Nk))^(delta/2)`. Their product has the common factor
`D^(delta/2)`. The exact `1/Nk` weight has only logarithmic total mass;
summing the head dyads costs an arbitrary small power. This retains
the scalar gain `(B/D)^(1/8)` instead of optimizing independently over
two unrelated zero bins. The full proof pays the modified local Euler
factors and their common frequency window in the cited companion.

Suppose the actual detector supplies

$$
                   |M_u(D;V_u)|^2\ge c\,U^{\delta r-\omega}
 \tag{14}
$$

for a fixed `c>0` and an arbitrarily small detector loss `omega>0`.
Choose `epsilon+omega/2<1/800`, for example after reserving a strict
half of that gap. Then (13) is eventually at most half the lower bound
for `|M_u|` in (14). By (10), at least one of `S_u,R_u` satisfies

$$
 |S_u|\ge\tfrac14\sqrt c\,U^{\delta r/2-\omega/2}
 \quad\hbox{or}\quad
 |R_u|\ge\tfrac14\sqrt c\,U^{\delta r/2-\omega/2}.
 \tag{15}
$$

The word 'eventually' is uniform over the licensed compact profile
family and norm-height range, not over arbitrary row-dependent
coefficient vectors.

## 4. The small-divisor alternative already has a power saving

On the support of (8), `Nk<=2K=B/(2U)` and `Nkm>B`, so

$$
                              Nm>2U.
 \tag{16}
$$

The companion theorem expands `C_{km}` before using a moment.
Writing `a=g t`, where `g=gcd(a,kd)`, and `m=t n`, leaves literal
short and long Möbius polynomials with the explicitly enlarged common
punctures. It does not replace `C_{km}` by an arbitrary bounded
coefficient sequence. The short inverse has length at most `U^alpha`;
the longer inverse has exponent `b` in

$$
                         1-\alpha\le b\le r-\alpha.
 \tag{17}
$$

The original inverse second moment and the pointwise cap on the other
two factors give the same complete scalar bound as the old far theorem:

$$
 e(b)+\frac34(r-b)\le e_0(r)-\frac1{750},\qquad
 e(b)=\max\{1,(1+5b)/6\},\quad e_0(r)=(1+5r)/6.
 \tag{18}
$$

The exact harmonic `k,d` weights, divisor allocations, common punctures
and common profiles are included in that theorem. Thus

$$
                    \sum_u w_U(u)|S_u|^2
       \ll_\epsilon U^{e_0(r)-1/750+\epsilon}.
 \tag{19}
$$

Consequently, for each actual buffered class, the first alternative in
(15) contains at most

$$
                   U^{e_0(r)-\delta r-1/750+\epsilon+\omega}
 \tag{20}
$$

rows. Source parameter Sobolev estimates allow exactly the rowwise
detector tests admitted in the companion and original moment. The
reserve `1/750-1/1000=1/3000` pays the chosen losses.
For this unweighted counting application take `w_U=1` on the class;
equivalently one may use a weight bounded below by a fixed positive
constant there. An arbitrary nonnegative weight that vanishes on some
rows would not by itself bound their number.

This is a positive localization theorem: all inverse witnesses except
the already improved count (20) lie in the explicit residual spike
set for (9), with support (12).

## 5. A weaker sufficient hypothesis for the existing conditional boundary

The following sufficient input requires only a spike count on (9),
instead of a bound for a full inverse moment or for every value of (9).

**Open localized witness hypothesis.** Uniformly over the original
above-floor buffered classes, the source-compatible presentation labels,
the licensed detector profiles, and `29/25<=r<=117/100`, the rows in
the second alternative of (15) have count

$$
 \#\{u:\ |R_u|\ge\tfrac14\sqrt c\,
                   U^{\delta r/2-\omega/2}\}
 \ll_\epsilon U^{e_0(r)-\delta r-1/1000+\epsilon},
 \tag{W}
$$

where the arbitrary preliminary witness loss is chosen sufficiently
small relative to the requested final epsilon. The count is for the
actual classes and tests, not for an independently selected polynomial
on each row. Physical prime-amplitude labels, when used by the source
consumer, retain its fixed-twist relations. A uniform second-moment
saving of `1/1000` for (9) is one stronger sufficient hypothesis, with
the usual loss allocation.

Under (W), (15)--(20) bound the **original** large inverse witness
count by

$$
                   U^{e_0(r)-\delta r-1/1000+\epsilon}.
 \tag{21}
$$

This supplies exactly the long-witness input used in Section 2 of
the third-pass `CONDITIONAL_CONSUMER.md`. In particular its old
floor below `r=29/25` remains, its original short-witness bound
remains, and its four detector cutoffs remain `1.162,1.164,1.166,1.168`.
Its complete exact endpoint certificate can therefore be used without
modification. Relative to its same imported Eisenstein premises, (W)
implies

$$
 L_E(s,\eta)\ne0\qquad(\operatorname{Re}s>0.8748856)
 \tag{22}
$$

for the licensed finite-order family, and the same conditional region
for Dirichlet L-functions and zeta by the source's quadratic base-change
factorization. The principal pole at one is allowed.

**Hypothesis (W) remains unproved.** The full-family `1/1000` residual
moment is also open. The established content here is the exact
localization, the paid small-divisor alternative and the conditional
consumer. A positive result for a different ratio component or a finite
determinant model does not establish (W).

## 6. Only a narrow zero/amplitude box needs the new bound

There is a sharper sufficient hypothesis for the same boundary, using
the marked returned-component theorem in Section 6 of `MIDDLE_JOINT.md`.
It retains the same asymmetric identity and the same head scale `B`.
The new input is needed only on the source-compatible box

$$
 \mathcal C:\quad
 \frac{473}{1024}\le\delta\le\frac{487}{1024},\qquad
 \frac{49}{100}\le x=\frac g\delta\le\frac12,
 \qquad \frac{29}{25}\le r\le\frac{117}{100}.
 \tag{23}
$$

Here `delta` is the buffered **auxiliary row** zero parameter; it is
not the real part of the target zeta zero. The parameter `g` is the
source's compatible physical prime-amplitude mean. Their fixed-twist
and finite-slot relationships are part of the imported consumer.

Set

$$
 \sigma=\frac{79}{100},\qquad
 K_* = \frac{B}{4U^\sigma}
      =\frac{D}{4U^{4/5}}.
 \tag{24}
$$

Define `S_*` and `R_*` by (8)--(9) with `K_*` in place of `K`.
The exact identity is still `M=H+S_*+R_*`. Its small-divisor part
has `Nm>2U^sigma`, by the same support calculation. The long actual
Möbius factor in the literal `k,d,g` allocation then has exponent

$$
                  b\ge\sigma-\alpha=\frac{387}{500}.
 \tag{25}
$$

For `b<1`, keep the original prime product in the source's marked
inverse estimate, while removing only the new inverse puncture by exact
Euler inversion. Each resulting shorter inverse retains at least the
same admissible prime capacity. The required maximum prime length is
`(1-387/500)/2=113/1000`, below the actual supply exceeding `.21` in
the existing consumer. A fixed small capacity decrement pays strict
moment inequalities and the finite slot mesh. The proof in the
companion retains all these restrictions; this is not a transfer of
prime amplitudes to a new character or to a newly deleted prime product.

On the original compatible class, the number of rows on which `S_*`
is at least the threshold in (15) has exponent at most

$$
 \max\left\{
  1-g-(\delta-g)(\sigma-\alpha),\quad
  \frac16+(5/6-\delta)(r-\alpha)
 \right\}+\epsilon.
 \tag{26}
$$

This is a count for the complete coherent `S_*`, not a claim that a
large signed sum forces a large value of every separated term. The
proof uses a common dyadic long-length group, a compatible prime
product for that group, the bounded same-bin factors, and the exact
harmonic label weights before a Chebyshev estimate.

The margins below the old long-witness exponent
`e_0(r)-delta r` are, throughout (23), at least

$$
 \frac{372257}{153600000}=0.00242354817708\ldots
 \quad\hbox{and}\quad
 \frac{1099}{192000}=0.00572395833333\ldots,
 \tag{27}
$$

respectively. The first follows by evaluating the multilinear gap
at its worst corner `r=29/25`, `delta=487/1024`, `x=49/100`;
the second is `alpha(5/6-delta)` at the upper delta endpoint.
Both strictly exceed `1/1000`, with a fixed reserve for the losses.

The pointwise head exclusion (13)--(15) is unchanged. It follows that
every actual inverse witness in (23), except the already improved
count (26), is a large value of the following **specific** residual:
equation (9) with `K_*` from (24). Its exact support is

$$
 \boxed{\quad Nk>\frac{D}{4U^{4/5}},\qquad
               Nkm>\frac{D}{U^{1/100}},\qquad Nkm<8D.\quad}
 \tag{28}
$$

Thus the lower divisor exponent now ranges from `9/25=.36` to
`37/100=.37` on the whole interval. This is substantially stronger
than the unmarked `.15` to `.16` localization. The returned variable
`m` can remain at the old critical length; (28) makes no false support
claim about it.

### Exact coverage outside the box

The third-pass consumer already certifies its old count at the maximal
amplitude `x=1/2` outside
`473/1024<=delta<=487/1024`, as well as its small-delta, floor,
small-row, distant-row and principal interfaces. Its proved monotonicity
in `x` therefore retains those ranges here without new input.

For all remaining rows with `x<=49/100`, a new exact certificate proves
the old count sufficient as well. In the original notation let

$$
 \begin{split}
 c&=8/9,&D_x&=3-(1+c)x,&P_x&=(2-cx)(1-x),\\
 A_\delta&=5/6-\delta,&J_x&=A_\delta D_x+\delta P_x,\\
 R_{\rm old}&=1-\delta+
            \frac{A_\delta\delta P_x}{2J_x},\qquad
 E_{\rm old}&=C_0+\delta/2+K_0\delta x
                         -\frac34h(1-R_{\rm old}),
 \end{split}
 \tag{29}
$$

where, to avoid confusing the endpoint coefficient with the divisor
cutoff, `K_0` in this one display denotes the old consumer's constant
`20679931/135000000`. Its other exact constants are
`C_0=-80017/3000000`, `h=3969767/5000000`.
That consumer's certificate polynomial is
`-2 J_x (E_old+10^(-6))`.

At `x=49/100`, split `1/4<=delta<=5/6` into the 128 equal rational
intervals with endpoints

$$
                     \frac14+\frac{7j}{1536},
                           \qquad 0\le j\le128.
 \tag{30}
$$

Every Bernstein coefficient of the polynomial on every interval is
positive. Their exact minimum is

$$
                 \frac{799945092153101}{1119744000000000000}>0.
 \tag{31}
$$

Since `J_x>0` and the old endpoint increases with `x`, this proves
`E_old<-10^(-6)` throughout this range with `x<=49/100`.
The already certified small-delta rectangle covers `1/8<=delta<=1/4`.
The certificate replays the pinned producer source, including its
positivity and monotonicity checks; it does not accept an unverified
JSON summary as evidence.

Consequently it suffices to assume (W) **only for the box (23)** and
with `R_*` from (24) in place of `R`. Call this restricted hypothesis
`(W_*)`. The marked count (26) pays the other alternative there;
the old estimates pay its complete complement. On the box, the existing
four-cutoff consumer still uses its improved short/long maximum and
retains the old floor below `r=29/25`. The original exact endpoint
certificate applies there, while (30)--(31) justify the new restricted
use of that arithmetic input. Thus

$$
 (W_*)\quad\Longrightarrow\quad
 L_E(s,\eta)\ne0\quad(\operatorname{Re}s>0.8748856)
 \tag{32}
$$

at exactly the previously stated imported scope, and hence conditionally
for Dirichlet L-functions and zeta. **The restricted spike count
`(W_*)` is not proved.** The new result is that this one localized
count, on (23) and (28), suffices; a saving for the complete full-family
inverse moment is no longer required by this version of the consumer.

## 7. A thinner original-product band is the final sufficient target

The preceding sections retain the identity with `alpha=2/125` so that
their full-row statements can be compared directly with the earlier
pass. On the restricted box (23), a separate identity gives a sharper
localization. Define

$$
 \alpha_* =\frac1{250},\qquad
 y_{1,*}=U^{\alpha_*},\qquad y_{2,*}=2D/U^{\alpha_*},
$$
$$
 A_*(m)=\sum_{ab=m}\mu_E(a)\mu_E(b)
          w_0(Na/y_{1,*})w_0(Nb/y_{2,*}),\qquad
 C_{*,a}(P)=\sum_{(d,P)=1}\frac{A_*(ad)}{Nd}.
 \tag{33}
$$

This is a new exact presentation of the **same** original inverse
`M_u(D;V)`, not a substitution of a new inverse input in the source
consumer. Its unequal-cutoff identity holds for all sufficiently large
`U`; the two cutoffs have product `2D` and both lie below the primal
annulus by a fixed power. Keep their complete support through `8D`.
All preceding `alpha=2/125` expressions remain as stated.

Put

$$
 \lambda=\frac{147}{200}=0.735,\qquad
 \sigma_* =\frac{773}{1000}=0.773,
 \qquad
 W_{\rm mid}(m)=
       \chi(Nm/U^{\sigma_*})-\chi(Nm/U^\lambda).
 \tag{34}
$$

Define three **original primal** coherent components by

$$
 \begin{split}
 L_u&=-D^{-1/2}\sum_{m,c}A_*(m)\psi_u(mc)V(Nmc/D)
                                      \chi(Nm/U^\lambda),\\
 F_u&=-D^{-1/2}\sum_{m,c}A_*(m)\psi_u(mc)V(Nmc/D)
                              [1-\chi(Nm/U^{\sigma_*})],\\
 T_u&=-D^{-1/2}\sum_{m,c}A_*(m)\psi_u(mc)V(Nmc/D)
                                      W_{\rm mid}(m).
 \end{split}
 \tag{35}
$$

Their selectors sum to one term by term. Thus

$$
                         M_u=L_u+F_u+T_u.
 \tag{36}
$$

There is no loss of signs or an interchange of two different
decompositions in (36). In particular the open object `T_u` can be
stated without any coprimality-inversion labels.

### The low and high components are paid on the whole critical box

Use the original source-compatible prime system of (23). For the
ordinary fourth moment its positive-slot coefficients, before the
common mask, must be fixed finite linear combinations of finite-ray
characters from the source's fixed finite group, independent of `U`
and the row. The original ordinary character and every prime slot
retain the **same** natural zero extension and common puncture.
The broader arbitrary bounded prime coefficients allowed by the
marked inverse estimate alone are insufficient for this step.

The positive-slot ordinary moment also excludes inducing characters
in the source's fixed finite group `Theta`, not just the principal
character. For the stated sixth-power-free physical rows and fixed
`S`-supported twists, this holds at sufficiently large `U`: a prime
outside `S` in such a row has valuation one through five, gives a
nontrivial local sextic character, and cannot be canceled by the fixed
twist. The sixth-power-free rows supported entirely on the fixed set
`S` are a bounded set. Those exceptions are handled in the original
source expression before this application. If a more general
presentation is used, membership in the source's permitted row set
must instead be retained as an explicit premise; a common zero mask
does not change the primitive inducing character.

The `alpha_*` variant of Sections 6--7 of `MIDDLE_JOINT.md`, proved
in its Section 8, applies directly to (35) with the outer inversion
labels equal to one. For the low component the ordinary factor has
log-length at least

$$
                     r-\lambda\in[17/40,87/200].
$$

The marked ordinary fourth moment supplies the count exponent

$$
 P_{\rm low}=1-2\delta(r-\lambda)
                   -\frac{4g}{9}\{1-2(r-\lambda)\}.
 \tag{37}
$$

The largest selected prime length is `1/30`, with a fixed small
decrement to pay the strict capacity and mesh losses. The two inverse
factors are bounded in their **same** buffered bin; their fourth
powers cost `U^(2 delta (r-c))`. The proof multiplies the complete
component by `|Q_z|^(1/2)` before its `L^4` Minkowski estimate, so
the source moment left over is precisely `sum |S_c^2 Q_z|^2`.
It does not assume a common prime product for all different `c`
groups: select a common product for each permitted finite length
group, remove its amplitude lower bound there, and then sum the
unweighted group norms.

For the high component the longer inverse has log-length at least
`sigma_*-alpha_*=769/1000`. Its marked inverse second moment and
the same-bin bounds on the remaining factors give the count exponent

$$
 P_{\rm high}=\max\left\{
  1-g-(\delta-g)\frac{769}{1000},\quad
  \frac16+\left(\frac56-\delta\right)(r-\alpha_*)
                                \right\}.
 \tag{38}
$$

Here the largest prime length is `231/2000`, below the original
available supply. The inverse's additional puncture, when needed in
the reflected presentation, is restored without changing the prime
product. All shorter restored inverse lengths preserve its two
strict marked capacities.

The exact uniform margins below `R_0=e_0(r)-delta r` on (23) are

| Component / endpoint | Minimum margin below `R_0` | Reserve after `1/1000` |
|---|---:|---:|
| Low returned product, marked ordinary fourth moment | `23/16000` | `7/16000` |
| High returned product, inverse length below one | `371959/307200000` | `64759/307200000` |
| High returned product, inverse length above one | `1099/768000` | `331/768000` |

Each minimum is proved by the explicit derivative signs or
multilinearity on the rational parameter box, not by floating point
sampling. Their strictly positive reserves pay all finite mesh,
profile, frequency and witness losses. Consequently either of `L_u`
and `F_u` has at most

$$
             U^{e_0(r)-\delta r-1/1000+\epsilon}
 \tag{39}
$$

rows at any fixed positive constant times the witness threshold
`U^(delta r/2-omega/2)`. As before, use weight one on the class.

### The remaining count and its conditional consequence

By (36), an actual witness (14) has at least one component of magnitude
at least `sqrt(c)/3` times that threshold. After (39), the only
unpaid alternative is the **specific** original middle expression
`T_u` in (35). Its termwise support is

$$
 \boxed{\quad U^{0.735}<Nm<2U^{0.773},\qquad
                    D<NmNc<2D.\quad}
 \tag{40}
$$

The ordinary factor therefore has log-length in
`[r-0.773,r-0.735]+O(1/log U)`. Over the whole critical box this
lies in `[0.387,0.435]+O(1/log U)`.

**Open thin-band witness hypothesis `(W_thin)`.** Uniformly on the
actual classes (23), with their original compatible finite prime
systems and licensed detector profiles,

$$
 \#\left\{u:\ |T_u|\ge\frac{\sqrt c}{3}
                U^{\delta r/2-\omega/2}\right\}
 \ll_\epsilon U^{e_0(r)-\delta r-1/1000+\epsilon}.
 \tag{W_thin}
$$

The arbitrarily small preliminary witness loss is chosen relative to
the final epsilon. This hypothesis does not ask for control of every
rowwise arbitrary coefficient sequence or of the complete inverse
moment. It asks for the displayed original signed expression on the
one parameter box where the certified consumer still needs it.

Equations (36)--(39), together with the exact old-endpoint coverage
(29)--(31), prove the following implication at precisely the imported
scope of (22):

$$
 (W_{\rm thin})\quad\Longrightarrow\quad
 L_E(s,\eta)\ne0\quad(\operatorname{Re}s>0.8748856),
 \tag{41}
$$

and conditionally the same region for Dirichlet L-functions and zeta.
**The hypothesis `(W_thin)` is open.** The localization and the
paid complementary alternatives are deductions within the imported
framework; (41) is a conditional consequence.

### Exact relation to the large-divisor representation

The stronger coefficient localization remains available for an
arithmetic attack. Keep `B=D/U^(1/100)` and write

$$
 \begin{split}
 \mathcal R_u=-D^{-1/2}
  \sum_{(k,P_u)=1}\frac{\mu_E(k)}{Nk}
  \sum_{m,c}C_{*,km}(P_u)\psi_u(mc)V(Nmc/D)\\
 \hspace{35mm}\cdot[1-\chi(Nkm/B)]W_{\rm mid}(m).
 \end{split}
 \tag{42}
$$

The same-bin head theorem is stable under the extra smooth returned
cutoff `W_mid(m)`: on each fixed ratio dyad and `k`, this cutoff has
uniformly bounded logarithmic derivatives on the returned annulus.
The modified-coefficient lemma and its shared frequency buffer are
unchanged. Hence the complementary head `H_mid` satisfies

$$
                |H_{{\rm mid},u}|
                   \ll U^{\delta r/2-1/800+\epsilon}.
 \tag{43}
$$

Exact signed `k,d` inversion, now with the returned cutoff held
fixed, gives

$$
                             T_u=H_{{\rm mid},u}+\mathcal R_u.
 \tag{44}
$$

Thus the two formulations are equivalent for witness estimates with
fixed adjusted constants, after the losses are chosen. This is an
identity and a pointwise error bound; it does not create an additional
independent source of cancellation.

Every nonzero term in the expanded coefficient of (42) obeys

$$
 \boxed{\begin{gathered}
 U^{.735}<Nm<2U^{.773},\qquad
        D/U^{.01}<NkNm<8D,\\
 \frac{D}{2U^{.783}}<Nk<\frac{8D}{U^{.735}},
                       \qquad Nd<8U^{.01}.
 \end{gathered}}
 \tag{45}
$$

The last inequality uses the **full** coefficient support
`N(kmd)<8D`, not a support assertion about `m` alone. The overall
divisor exponents are consequently between `.377` and `.435`, up to
fixed scale constants; for each individual term `log_U Nk` is linked
within `.01+O(1/log U)` to `r-log_U Nm`. The short auxiliary divisor
`d` retains its exact signed arithmetic role. In particular `d=1`
survives, so its shortness alone supplies no power saving.

Nor does the displayed `mu_E(k)` make the long `k` sum an actual
inverse polynomial. Already when `d=1`, the exact allocation writes
the squarefree `k` as `g m_0` with `(g,m_0)=1`; its scalar sign is
`mu_E(k) mu_E(g) mu_E(m_0)=1`. The native inverse moment cannot be
applied to `k` after discarding the other two factors of that sign.
This is a normalization and coefficient check, not a lower bound for
the complete signed residual.

The original critical returned lengths remain inside (40). The
companion's exact resource calculation shows that the two existing
marked estimates leave a strictly positive gap even after optimizing
the asymmetric cutoff: at their old contact, a requested count saving
`eta>0` separates their thresholds by

$$
 \alpha_*+\frac{\eta}{\delta-g}
                  +\frac{\eta}{2\delta-8g/9}>0.
 \tag{46}
$$

This is a limitation of those particular moment resources. It is not
an impossibility result for `(W_thin)` or for a further arithmetic
argument.

## 8. Verification boundary

`check_detector_localization.py` checks finite versions of (6)--(12),
including natural masks and signed coefficient inversion; the cutoff
support implication (16); the exact exponent inequalities and reserves;
the marked-box corners and all 128 complete Bernstein cells in (30);
the separate `alpha_*` low/high margins, exact three-component band
partition, large-divisor and short-`d` support restrictions in (45);
and a control that rejects the false inference `Nm>B` from (12).
These finite checks do not establish the analytic imports, the companion
pointwise theorem, or the open hypothesis (W). Independent review of the
proof and its exact companion interfaces is required before its status
is promoted beyond this proposed source-dependent deduction.
