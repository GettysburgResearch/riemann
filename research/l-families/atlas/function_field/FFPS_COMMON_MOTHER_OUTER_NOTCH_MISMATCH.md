# The common mother, outer construction, and explicit kernel form a three-way mismatch

Status: **exact frozen-interface correction; the common-mother detector,
self-convolution, and explicit piecewise kernel survive separately, but the
claimed identifications among them do not**

Bounded exact replay:
[`ffps_common_mother_outer_notch_mismatch.py`](ffps_common_mother_outer_notch_mismatch.py).

Frozen head: PR #751 at `98af0db6`, with explicit-kernel parent
`ec6635b4`.  The replay binds the exact blobs for `L-102500`, `L-102504`,
`L-102701`, `L-102740`, explicit-kernel `L-102880`, stable-image
`L-102885`, `L-106134`, and `T-106150`.

## 0. Outcome

The frozen programme uses two different multipliers under the same name
`m_Phi`.

Put

\[
q(s)=1-\sqrt2\,2^{-s},
\qquad
r(s)=1-2^{-s}.
\tag{0.1}

The canonical common mother of `L-102500` and its exact ratio-four
self-convolution in `L-102701` have

\[
\boxed{
m_\Phi(s)={2q(s)^2r(s)^2\over s^2(s-1/2)}.}
\tag{0.2}

But `L-102740` defines

\[
q_2(s)=q(s)r(s)^2
\]

and then prints

\[
m_\Phi(s)={2q_2(s)\over s^2(s-1/2)},
\tag{0.3}

which has only one factor of `q`.  Its final multiplier equality therefore
misses exactly one critical dyadic notch.

If

\[
Q=I-\sqrt2 S_2,
\qquad S_2f(y)=f(y/2),
\tag{0.4}

then the correct relation between the two frozen objects is

\[
\boxed{
Q\mathcal L_\sigma
={1\over2}(D-1)(5D+3/2)H_\sigma.}
\tag{0.5}

It is **not** the unnotched equality printed in `L-102740.2`.

Consequently, if

\[
H_\sigma=(2D-1)\mathcal J,
\]

then

\[
\boxed{
Q(D\mathcal L_\sigma)=
{1\over2}D(D-1)(5D+3/2)(2D-1)\mathcal J.}
\tag{0.6}

Thus the differential self-convolution of `L-106134` is an
**extra-notched** version of the `L-102740` construction.  There is a second,
independent mismatch with the explicit native kernel.

Let `R_exp` be the centered outer kernel whose piecewise derivative
`K_exp=D R_exp` is printed in `L-102880.2`, and put

\[
 V={5D+3/2\over4}={5\over4}(D+3/10).
\tag{0.7}
\]

Direct Mellin integration of those three piecewise cells gives

\[
 \widehat K_{\rm exp}(s)
 ={4q(s)r(s)^2(s-1)\over s(s-1/2)}.
\tag{0.8}
\]

By contrast, differentiating the construction in `L-102740.1` gives

\[
 \widehat{D\mathcal L_{740}}(s)
 ={q(s)r(s)^2(s-1)(5s+3/2)\over s(s-1/2)}
 =V(s)\widehat K_{\rm exp}(s).
\tag{0.9}
\]

The common-mother differential gives

\[
 \widehat{\mathcal D_{\rm out}\mathcal J}(s)
 ={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)}
 =q(s)V(s)\widehat K_{\rm exp}(s).
\tag{0.10}
\]

Thus the exact operator ledger is

\[
 \boxed{
 \mathcal L_{740}=V R_{\rm exp},
 \qquad
 \mathcal D_{\rm out}\mathcal J
 =Q(D\mathcal L_{740})=QV K_{\rm exp}.}
\tag{0.11}
\]

Consequently the polynomial right sides printed in `L-106134.13--.14` are
exactly the observations with kernels

\[
 R_+=QV R_{\rm exp},
 \qquad
 K_+=QV K_{\rm exp},
\tag{0.12}
\]

not with the explicit `R_L,K_L`.  The common-mother/Wick algebra on those
right sides is still exact; the errors are the left-side kernel label and the
downstream native-current implication.

The same correction reaches the older stable-image claim.  With `K_XD` as
in `L-102885`, the exact relation is

\[
 \boxed{
 (D+3/2)QV K_{\rm exp}
 =D(D-1)(5D+3/2)K_{\rm XD},}
\tag{0.13}
\]

not `L-102885.2` with unfiltered `K_exp` on the left.

This does not destroy the common-mother programme.  The common mother remains
exact, compact, zero-safe in the open critical strip, and has its own
conditional Mellin--Landau consumer in `L-102504`.  One may instead retain the
extra-notched current as a detector, but its complete-source gate
`EXTSRC106150` is not automatic.  Removing the filters requires the fixed
stable inverse for `V` and a source/horizon-compatible inverse for `Q`.

## 1. The frozen contradiction

The source hashes are:

| claim | frozen blob |
|---|---|
| `L-102500` | `db4590fc23b53ed601e108a77e4d064b7d9d13f9` |
| `L-102504` | `30edf4116f15984c4dfa133d7ff0609388ae2868` |
| `L-102701` | `70eb455a3b2bb0398f8bba22dee82c39ef803156` |
| `L-102740` | `ec2f3aafe1b590a11a9967e298f5dfb0e2d59f55` |
| `L-102880` explicit derivative kernel (parent `ec6635b4`) | `d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6` |
| `L-102885` stable-image claim (parent `ec6635b4`) | `045481b73474d67ded5bf9633808e8d8d39c4622` |
| `L-106134` | `cf40354ff8810a2d4bea9459cf142c300ba36237` |
| `T-106150` | `ac15f0106a26303f06779feb484a521978fe3ecf` |

`L-102500.2` defines

\[
\Phi_*=(I-\sqrt2S_2)^2(I-S_2)^2\Phi_0,
\]

so (0.2) follows immediately.  Independently, `L-102701` puts

\[
\widehat A(s)
={(1-2^{-s})(1-\sqrt2\,2^{-s})\over s(s-1/2)}
\]

and proves

\[
\Phi_*=2(D-1/2)A *_M A.
\]

Its multiplier is again (0.2).  These two interfaces agree.

In contrast, the multiplier used on the first two lines of `L-102740.1` is

\[
{q(s)r(s)^2\over s}
\left[5-{s+3/2\over s(s-1/2)}\right]
=
{q(s)r(s)^2(s-1)(5s+3/2)\over s^2(s-1/2)}.
\tag{1.1}

Applying the displayed differential to the true common mother gives

\[
{1\over2}(s-1)(5s+3/2)m_\Phi(s)
=
{q(s)^2r(s)^2(s-1)(5s+3/2)\over s^2(s-1/2)}.
\tag{1.2}

The ratio of (1.2) to (1.1) is exactly `q(s)`, proving (0.5).  The underlying
mother multipliers differ at every positive integer Mellin sample.  The two
outer multipliers differ at every integer sample `s>=2`; both share the
forced differential zero at `s=1`.  No pole, endpoint, or limiting convention
can identify the analytic multipliers.

The replay in `X-106150` does not catch this.  Its multiplier test replaces
the actual `A_hat(s)` by an arbitrary scalar `z` and verifies only the formal
identity

\[
2(s-1/2)z^2=(2s-1)z^2.
\]

It never compares the common-mother multiplier with the one-notch outer
multiplier.

### The explicit-kernel contradiction

The direct computation behind (0.8) uses only `L-102880.2`.  On a cell
`[2^a,2^b]`, integrate the constant and square-root pieces as

\[
 \int_{2^a}^{2^b}y^{-s-1},dy
 ={2^{-as}-2^{-bs}\over s},
\]

\[
 \int_{2^a}^{2^b}\sqrt y\,y^{-s-1},dy
 ={2^{a(1/2-s)}-2^{b(1/2-s)}\over s-1/2}.
\]

Substitution of the three printed cells and exact collection of the dyadic
terms is especially transparent with `x=2^(-s)`: both collections contain

\[
 q(s)r(s)^2
 =1-(2+\sqrt2)x+(1+2\sqrt2)x^2-\sqrt2x^3.
\]

The constant pieces sum to `8 q(s)r(s)^2/s`, while the square-root pieces
sum to `-4 q(s)r(s)^2/(s-1/2)`.  Their sum is exactly (0.8), as a meromorphic
identity in `s`, not an interpolation from the replay samples.  Comparing it
with the differentiated (1.1) gives

\[
 {\widehat{D\mathcal L_{740}}(s)
  \over\widehat K_{\rm exp}(s)}
 ={5s+3/2\over4}=V(s),
\tag{1.3}
\]

away from their common forced zeros.  The later common-mother expression has
the further ratio `q(s)`.  Therefore neither the `q` correction alone nor the
stable polynomial correction alone identifies all three objects.

## 2. Inverting the two extra filters

Formally, the causal inverse of (0.4) is

\[
Q^{-1}
=\sum_{k\ge0}(\sqrt2S_2)^k.
\tag{2.1}

At dyadic depth `k`, its coefficient is

\[
(\sqrt2)^k=(2^k)^{1/2}.
\tag{2.2}

Thus a horizon reaching scale `2^k` pays a square-root power loss, not a
subpower loss.  The inverse coefficients are positive, so there is an exact
causal one-sided inequality

\[
 f_-(u)
 \leq
 \sum_{k\geq0}(\sqrt2)^k
 (Qf)_-(u-k\log2),
\tag{2.3}
\]

whenever the zero-extended causal series is locally finite.  But on a horizon
of dyadic depth `K`, its `L^1` norm is bounded only with the factor

\[
 \sum_{k=0}^{K}(\sqrt2)^k\asymp (2^K)^{1/2}.
\tag{2.4}
\]

Thus plain causal inversion does transfer one-sided mass, but only with a
square-root power loss.  It does not provide the required subpower theorem.

The extra stable filter `V` in (0.7) is less dangerous.  Its causal inverse is

\[
 [V^{-1}g](u)
 ={4\over5}\int_{-\infty}^{u}
 e^{-3(u-v)/10}g(v)\,dv,
\tag{2.5}
\]

a positive kernel of logarithmic `L^1` norm `8/3`.  Thus the `V` mismatch
invalidates exact kernel naming, but it can be removed in the forward causal
one-sided direction with a fixed loss.  The critical causal loss comes from
`Q`.

### A bounded anti-causal inverse for compact zero-mass currents

The causal geometry is not the only inverse geometry.  If `g=Qf` and `f` is
compactly supported to the future, then iteration from the terminal end gives

\[
 \boxed{
 f=-\sum_{j\geq1}2^{-j/2}S_2^{-j}g,}
 \qquad
 S_2^{-j}g(y)=g(2^j y).
\tag{2.6}
\]

The series is pointwise finite for compact support and has global logarithmic
`L^1`/total-variation norm

\[
 \sum_{j\geq1}2^{-j/2}=1+\sqrt2.
\tag{2.7}
\]

If `f` and `g` are compact order-zero signed measures of total mass zero—as
the derivative currents under discussion are when their Jordan negative
variation is invoked—then positive and negative total variations agree.
Equation (2.6) therefore gives the exact global one-sided bound

\[
 \boxed{
 \int f_-
 \leq(1+\sqrt2)\int g_- .}
\tag{2.8}
\]

This is a serious possible escape, but it is anti-causal: the value at a
native horizon consumes future values and the terminal support.  The frozen
prefix theorem controls negative mass only up to the current horizon, and the
complete arithmetic source is not globally compact.  To use (2.8), one must
prove a source-faithful truncation whose terminal tail is closed and whose
zero-total-mass cancellation survives the truncation.  The atomic-shell
deletion firewall shows that such compatibility is not automatic.

The zero set of `q(s)` lies on `Re(s)=1/2`, not inside the open strip.  This
is enough for Mellin zero-safety, but it is not a one-sided physical-space
inverse theorem.  Holomorphic nonvanishing in the open strip must not be
confused with subpower control of the causal inverse on the boundary scale.

## 3. Corrected implication architecture

The exact retained chain is

```text
Boolean/Beta half-source square
  -> common mother Phi_* = 2(D-1/2) A *_M A
  -> extra-notched differential current D_out J
  -> fixed zero-safe common-mother Mellin symbol.
```

If `H_K^live` retains its inherited meaning as the explicit native derivative
outer current, the corrected version of the first line of `T-106150` is

\[
 \boxed{
 QVH_K^{\rm live}
 =\mathcal D_{\rm out}\mathcal J_U^\diamond
 +H_{\rm closed}^{+},}
\tag{3.1}
\]

where `H_closed^+=QV H_closed` remains subpower whenever the inherited closed
remainder has the corresponding fixed-shift/differential absolute closure.
The same correction applies to the ordinary self-convolution line.  The
internal Wick/ordinary comparison and reflection identities remain exact for
the extra-notched polynomial current.

In claim-number terms:

* `L-102740.3--.5` retain their positive-resolvent algebra only with
  `Q L_740` in place of `L_740`; separately, `L_740=V R_exp` has the fixed
  positive inverse (2.5);
* `L-106134.1--.12` and `.15--.16` are unaffected;
* the right sides of `L-106134.13--.14` remain exact after replacing their
  left labels by `QV R_exp,QV K_exp`;
* `L-102885.2` is exact only with `QV K_exp` in place of `K_exp`;
* `T-106150.2` and `.6` require the left side `QV H_K^live` as in (3.1);
* the internal implications `SFSC106150 -> WKSFSC106150` and
  `REFSIG106150 <-> SFSC106150` remain statements about the extra-notched
  current;
* the arrow `WKSFSC106150 -> BCI102990` in `T-106150.4`, and hence the final
  RH arrows in `.8` and `.13`, are not typed without an additional adapter or
  a subpower one-sided removal of `Q`.

The chain that is not presently typed is

```text
D_out J
  -/-> explicit native K_exp current
  -/-> inherited BCI closure under the uncorrected L-102740 adapter.
```

Three formal adapter routes are separated below.  The raw-Jordan version of
Route A has since been retired by the complete-beta atomic firewall; only a
fixed-mollified reformulation remains potentially viable.

### Route A: retain the complete extra-notched detector

The extra-notched multiplier (0.10) is itself zero-safe in the open strip.
One may therefore prove the separate exact source gate `EXTSRC106150`: the
**complete** duplicate-`67` `beta` source must equal
`D_out J_U^diamond` plus an absolute-subpower closed field.  Historically,
combining this with a raw complete-current negative-mass premise would have
given a direct Mellin--Landau route with no inverse.  The later atomic
firewall proves that raw premise false: its Jordan negative variation is
`Omega(sqrt(Y))`.  `EXTSRC106150` therefore remains only a source-accounting
question.  A viable analytic route must mollify before taking the Jordan
part, and the required `MEXTSRC106150/NATCOMP-MOLL106150` bridge is not proved.

Neither `L-102740`, `L-102880`, nor the misidentified `L-102885` supplies
`EXTSRC106150`.  They compare fixed kernels; they do not identify the complete
`beta` source with the live half-source square after every sector is restored.

### Route B: use the separate common-mother consumer

Rebase the frontier premise directly on the negative mass of the
common-mother output consumed by `L-102504`.  This requires a coefficient-exact
proof that the fully recombined Boolean source is the `beta` source seen by
that fixed Mellin--Landau detector, with every closed remainder still
subpower.  A premise only on
`D_out J=P(D)H_Phi` does **not** suffice for this route: transferring a
one-sided estimate backward through the polynomial differential `P(D)` would
be another theorem.  Redefining the premise directly on `H_Phi` avoids both
that inverse and the inverse of `Q`.

### Route C: remove the two filters

Remove `V` by its fixed positive resolvent (2.5), then remove `Q`.  The causal
`Q` inverse has the square-root loss (2.2)--(2.4).  The anti-causal inverse
(2.6) has constant global norm, but requires a new terminal-horizon and
source-truncation theorem.  Triangle inequality or source-blind positivity
does not create that missing compatibility.

Until one of these is completed, the following statements must be separated:

```text
common-mother self-convolution                         EXACT
zero-safety of the extra-notched common mother         EXACT
L-102740 unnotched polynomial identity                 FALSE AS WRITTEN
L-102740 construction = explicit R_L                   FALSE; EQUALS V R_exp
L-102885 stable image of explicit K_L                   FALSE; IMAGE IS QV K_exp
L-106134 polynomial RHS                                 EXACT FOR QV R_exp / QV K_exp
L-106134 identification with native R_L/K_L            FALSE AS WRITTEN
T-106150 Wick/reflection algebra                        RETAINED FOR D_out J
T-106150 implication D_out J -> native BCI current     NOT TYPED
EXTSRC106150                                             OPEN SOURCE ACCOUNTING
raw complete-beta Jordan premise                        REFUTED: Omega(sqrt(Y))
MEXTSRC106150 / NATCOMP-MOLL106150                       OPEN / NOT AUTOMATIC
direct adapter to L-102504                              OPEN
Q causal inverse                                       POSITIVE BUT POWER-LOSSY
Q anti-causal inverse                                  BOUNDED GLOBALLY; PREFIX GATE OPEN
RH                                                      UNPROVEN
```

## 4. Relation to the atomic-shell packet

`FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md` computes the exact kernel
of the right side of (0.6).  It is therefore a theorem about the
**extra-notched common-mother differential**, not automatically about the
explicit native outer kernel.  In the three-way ledger its fixed kernel is
`QV K_exp`.  Its source-blind/deletion-stability firewall remains useful, but
its name and downstream adapter must respect (0.11).

This distinction also explains why endpoint or dyadic atoms found in the
self-convolution kernel cannot simply be assigned to the explicit native
outer kernel without first resolving the notch mismatch.

## 5. Proof ledger

Proved exactly from the frozen multipliers:

- the one-factor conflict (0.2)--(0.3);
- the corrected operator identities (0.5)--(0.6);
- the direct piecewise transform (0.8) and three-way ledger (0.8)--(0.11);
- the corrected `L-102885` relation (0.13);
- the fixed positive inverse for `V`;
- the positive but square-root-lossy causal inverse;
- the bounded anti-causal inverse for compact zero-mass currents;
- the insufficiency of the `X-106150` arbitrary-`z` multiplier replay.

Retained:

- `L-102500` common mother and Smith--Bezout data;
- `L-102701` ratio-four self-convolution;
- `L-102504` as a conditional zero-safe analytic consumer;
- the explicit piecewise `L-102880` kernel and its derivative identity;
- the Boolean/Beta/Wick source algebra independent of the outer adapter.

Not proved:

- a direct fully recombined source adapter to `L-102504`;
- `EXTSRC106150` for the complete extra-notched source;
- terminal-horizon/source-truncation compatibility for the anti-causal inverse;
- a subpower causal one-sided inverse for `Q`;
- the native outer-current identification in `L-106134--T-106150`;
- live-source `WKSFSC106150`, `SFSC106150`, `REFSIG106150`, BCI, RH, or
  GRH;
- the fixed-mollified source bridge `MEXTSRC106150/NATCOMP-MOLL106150`.

Refuted later, for the complete duplicate-`67` beta current:

- raw complete-current Jordan negative variation `Y^o(1)`; the atomic
  firewall proves an `Omega(sqrt(Y))` lower bound.  The distinct frozen
  live-source gates above are not identified with that complete current
  without an adapter.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_common_mother_outer_notch_mismatch.py --check
python -B -O research/l-families/atlas/function_field/ffps_common_mother_outer_notch_mismatch.py --check
python -B -m unittest tests.test_ffps_common_mother_outer_notch_mismatch
python -B -O -m unittest tests.test_ffps_common_mother_outer_notch_mismatch
python -B -m ruff check research/l-families/atlas/function_field/ffps_common_mother_outer_notch_mismatch.py tests/test_ffps_common_mother_outer_notch_mismatch.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_common_mother_outer_notch_mismatch.py tests/test_ffps_common_mother_outer_notch_mismatch.py
```

The replay uses exact arithmetic in `Q(sqrt(2))` at four positive Mellin
samples, directly integrates all three `L-102880.2` cells, and checks both
causal and anti-causal dyadic inverse coefficients through depth `16`.  It
enumerates no source atom, conductor, curve, or point.
