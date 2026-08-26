# The anti-causal terminal tail is geometrically bounded, but the frozen gate changes source

Status: **exact fixed-source support theorem and exact frozen-quantifier
no-go; one shell-uniform same-cutoff estimate remains new**

Scope: corrected native/extra-notched outer adapter at one cofinal dyadic
horizon.  This packet proves no family estimate, BCI statement, RH, or GRH.

Bounded exact replay:
[`ffps_frozen_source_terminal_horizon_audit.py`](ffps_frozen_source_terminal_horizon_audit.py).

Frozen sources: parent scientific head `ec6635b4`, and PR #751 head
`98af0db6`.  Exact blobs are listed in section 6 and authenticated by the
replay.

## 0. Outcome

There are two separate questions in `TERMFUT106150`.

The geometric question has an exact favorable answer.  Let `sigma_Y` be the
physical-product projection of one frozen real source to

\[
 {Y\over8}\le n\le2Y.
\tag{0.1}
\]

For the explicit native derivative kernel `K_nat` of `L-102880`, and the
corrected extra-notched kernel

\[
 K_{\rm ext}=QVK_{\rm nat},\qquad
 Q=I-\sqrt2S_2,\qquad
 V={5D+3/2\over4},
\tag{0.2}
\]

one has

\[
 \operatorname{supp}(K_{\rm nat}*\sigma_Y)
 \subset[Y/8,16Y],
\qquad
 \operatorname{supp}(K_{\rm ext}*\sigma_Y)
 \subset[Y/8,32Y].
\tag{0.3}
\]

Thus the same projected source needs only a fixed terminal dilation `32`, or
at most five future dyadic inverse steps from a point in `[Y,2Y]`.  Combining
the bounded anti-causal inverse of `Q` with the positive inverse of `V` gives

\[
 \boxed{
 \int_Y^{2Y}(K_{\rm nat}*\sigma_Y)_-\,{dX\over X}
 \le {8\over3}(1+\sqrt2)
 \left\|(K_{\rm ext}*\sigma_Y)_-\right\|_{[Y/8,32Y]} .}
\tag{0.4}
\]

The norm on the right is Jordan negative variation; `VK_nat` and hence
`K_ext` can contain dyadic atoms.  Every shifted native kernel has zero total
logarithmic mass, so the zero-mass conversion from the positive to the
negative Jordan part is valid after the source projection.

The frozen analytic premise does **not** supply the right side of (0.4).
`T-106150` controls the complete balanced source called `J_U` “on every
dyadic horizon”; it does not quantify uniformly over the fixed physical shell
(0.1), nor over a cutoff `U` held at its base-horizon value while future
shells are read.  At the next horizon the frozen construction resets

\[
 U_j=\lfloor2^{j/6}\rfloor.
\tag{0.5}
\]

An exact live counterfixture below changes balanced coefficient from `2` to
`0` at the first reset.  Moreover, negative mass of a complete current does
not dominate negative mass of one retained shell.  Hence the bounded inverse
removes the **analytic** obstruction but not the source quantifier.

The smallest corrected gate is:

```text
FSHELL106150:
  for every cofinal dyadic Y, freeze U=floor(Y^(1/6)) and project the
  complete labelled balanced source to Y/8 <= n <= 2Y; the Jordan negative
  variation of the corrected extra-notched observation of that SAME source
  on its complete support [Y/8,32Y] is Y^o(1), uniformly in the inherited
  shell, carrier, owner, marked-prime and incidence labels.
```

Then `FSHELL106150` and the already-proved global inverse imply the same-shell
native negative-mass premise.  The separate `NATBIND106150` parent binding
identified in the outer-notch audit is still required before invoking
`BCI102990`.

This shell-projected live-source gate must not be confused with the raw
complete-beta Jordan premise.  The later complete-source atomic firewall
refutes the latter with an `Omega(sqrt(Y))` lower bound.  It does not settle
`FSHELL106150`, whose source is one fixed physical shell, but it removes any
claim that the raw complete premise remains an open route.

## 1. Exact fixed-source terminal theorem

The explicit native kernel has support `[1,8]`.  Therefore, for
`Y<=X<=2Y`, source atoms outside (0.1) are invisible:

\[
 K_{\rm nat}(X/n)\ne0
 \quad\Longrightarrow\quad
 {Y\over8}\le n\le2Y.
\tag{1.1}
\]

This is the direct kernel form of the exact four-octave localization in
`L-102735`.  Let `P_Y` denote this physical-product projection.  Then

\[
 (K_{\rm nat}*\sigma)(X)
 =(K_{\rm nat}*P_Y\sigma)(X)
 \qquad(Y\le X\le2Y).
\tag{1.2}
\]

Differentiation by `V` does not enlarge support.  The term `S_2f(X)=f(X/2)`
dilates the upper endpoint by `2`, so (0.2) has support ratio at most `16`.
Applying it to (0.1) proves (0.3).  Notice that the complete extra support
`[Y/8,32Y]` spans eight dyadic shells, but only five future calls
`g(2^jX)`, `1<=j<=5`, can occur when `X` starts in `[Y,2Y]`.

Put

\[
 f=K_{\rm nat}*\sigma_Y,\qquad h=Vf,\qquad g=Qh.
\]

All three are compact order-zero real signed distributions and

\[
 \int f={0},\qquad
 \int h={3\over8}\int f=0,\qquad
 \int g=(1-\sqrt2)\int h=0.
\tag{1.3}
\]

The exact future inverse is

\[
 h=-\sum_{j\ge1}2^{-j/2}S_2^{-j}g,
\qquad
 \sum_{j\ge1}2^{-j/2}=1+\sqrt2.
\tag{1.4}
\]

Its minus sign first controls `h_-` by `g_+`; (1.3) gives
`||g_+||=||g_-||`.  The positive causal inverse

\[
 f(u)={4\over5}\int_{-\infty}^u
 e^{-3(u-v)/10}h(v)\,dv
\]

has norm `8/3`.  These facts prove (0.4).  No source enumeration, long
horizon, or asymptotic estimate is involved.

### Why “finite labelled source” is not enough

`L-106133` begins with a finite labelled prime set, but its Boolean cube
contains every subset of that set.  The bound `p,r<=16Y` in its source
diagonal is a label bound, not a physical-product bound.  Products of many
allowed labels can be much larger than every fixed multiple of `Y`.

Consequently, the unprojected finite Boolean cube does not itself have support
in `[1,CY]` for a fixed `C`.  The exact product projection `P_Y` is essential.
It loses nothing in the native block by (1.2), but it creates a source-specific
future estimate which is not present in the frozen theorem.

## 2. Exact cutoff-crossing live atom

The moving cutoff is not a cosmetic relabelling.  Take

\[
 Y=2^{24},\qquad U_Y=16,
\qquad U_{2Y}=17.
\tag{2.1}
\]

The second equality is exact because

\[
 17^6<2^{25}<18^6.
\]

Choose the labelled owner pair `(2,3)` and the two-prime Boolean core

\[
 C=\{17,43\}.
\]

For a prime `p`, the half-source of `L-106132` satisfies

\[
 f_U(\{p\})=
 \begin{cases}
 -1,&p>U,\\
 0,&p\le U.
 \end{cases}
\tag{2.2}
\]

Since `b_U=f_U star f_U`, ordered disjoint splitting gives

\[
 \boxed{b_{16}(C)=2,\qquad b_{17}(C)=0.}
\tag{2.3}
\]

In the canonical equal-pair allocation on all four labels, the `(2,3)` owner
coordinate therefore has coefficient share `1/3` at the base cutoff and `0`
after the reset.

Its physical product is

\[
 N=2\cdot3\,(17\cdot43)^2=3,206,166,
\]

and

\[
 {Y\over8}<N<2Y,
\qquad
 {Y\over N}\in(9/2,8).
\tag{2.4}
\]

Thus it is not a dormant remote monomial: it is active in the exact native
source window at `X=Y`.  It also contributes nontrivially to the future
extra-notched current at `X=2Y`.  Indeed, on `4<z<8`,

\[
 VK_{\rm nat}(z)=3\sqrt2-2\sqrt z,
\]

and with `z=Y/N>9/2`,

\[
 QVK_{\rm nat}(2z)
 =-\sqrt2\,VK_{\rm nat}(z)\ne0.
\tag{2.5}
\]

But the horizon-`2Y` balanced source has already reset to `U=17` and deletes
this labelled balanced coordinate.  Applying the future-horizon gate therefore
does not evaluate the same source required by (1.4).

This counterfixture uses four labels and two horizons.  It is a source typing
witness, not evidence that either current is large.

## 3. What cutoff drift does, and does not, cost

The full Boolean Vaughan identity is independent of `U`.  If

\[
 \mu_{\rm sf}=\mathcal T_U+\mathcal B_U,
\]

where `B_U` is the balanced row, then exactly

\[
 \boxed{
 \mathcal B_U-\mathcal B_{U'}
 =\mathcal T_{U'}-\mathcal T_U.}
\tag{3.1}
\]

So the atom in section 2 moves into the Type-I row; it does not disappear from
the fully recombined native detector.  This identifies a possible repair:
prove absolute, uniform closure of the **corrected extra-notched** observation
of both Type-I rows whenever `U,U'` are comparable under the fixed dilation.

That repair is not frozen.  `L-106080.7` proves the Type-I estimate for the
explicit native `K_L` with the horizon-matched cutoff.  The outer-notch audit
shows that `D_out J` is instead observed by `QVK_nat`.  In particular, the
factor `V` differentiates the piecewise native kernel and introduces atomic
terms.  No cited frozen statement proves the corresponding absolute
extra-notched Type-I comparison.  It must not be silently imported from the
misidentified kernel.

Even proving this Type-I bridge would solve only the cutoff reset.  It would
not supply the physical-shell projection required in section 1.

### Which horizon labels are actually stable

The owner coordinate is not the obstruction for a base-shell atom.
`L-102962` proves that every active Boolean balanced label is at most
`4 sqrt(Y)` and permits the canonical equal-pair gauge.  Once such an atom is
frozen, the same pair remains legal at every future horizon because the
completion threshold only increases.  No owner re-selection is needed in
(1.4).

Carrier, marked-prime, incidence, and shell provenance can likewise remain
attached algebraically, as `T-106150` requires.  What is missing is an
estimate uniform after selecting the base physical shell.  The two genuine
changes are therefore sharply separated:

```text
canonical owner and attached provenance labels   CAN BE HELD FIXED;
Boolean cutoff U                                  CHANGES COEFFICIENTS;
base physical-product shell P_Y                   NOT QUANTIFIED IN WKSFSC.
```

## 4. Shell projection is a genuine one-sided gate

Retaining a shell label inside a source is not the same as controlling its
negative mass separately.  For two scalar components, take

\[
 G_{\rm shell}=-M\varphi,
 \qquad
 G_{\rm rest}=M\varphi,
 \qquad \varphi\ge0.
\]

Then the complete current has zero negative mass while the selected shell has
negative mass `M int(phi)`.  Hence there is no source-blind inequality

\[
 \|(P_YG)_-\|\ll\|G_-\|.
\tag{4.1}
\]

`L-102959` proves that inserting shell and incidence masks is harmless in its
centered phase **energy** estimate.  It does not prove projection stability of
the conclusion-facing one-sided current.  Likewise, the sentence in
`T-106150` that shell labels remain inside the half-source preserves
provenance but does not add the quantifier required by `FSHELL106150`.

This logical obstruction is independent of how the unspecified integral in
`WKSFSC106150` is read:

- on a block reading, the next block resets `U` and sums other source shells;
- on a prefix reading, the larger prefix still uses the source indexed by its
  own horizon and does not isolate `P_Y`.

Thus “on every dyadic horizon” cannot be substituted for “the same frozen
source on its complete future support.”

## 5. Exact implication boundary

The corrected native route is

```text
exact native product localization P_Y
  -> same frozen source has extra support only through 32Y       PROVED
  -> bounded Jordan anti-causal Q inverse and positive V inverse PROVED
  -> same-U, same-shell extra negative mass FSHELL106150          OPEN
  -> explicit-native live negative mass                          CONDITIONAL
  -> NATBIND106150 to the parent BCI current                      OPEN
  -> BCI102990 / RH                                               OPEN
```

The terminal geometry is therefore not a long-range obstruction.  The missing
statement is a uniformity/projection theorem over a constant number of shells.
It is nevertheless a genuine new hypothesis because the frozen source changes
at the first future block in an active labelled coordinate.

Exact proved statements:

- native source localization (0.1) on `[Y,2Y]`;
- same-projected-source supports (0.3), with terminal dilation `32`;
- fixed-source one-sided transfer (0.4);
- the cutoff-crossing coefficients (2.3) and active physical realization;
- the Type-I difference identity (3.1);
- the source-projection no-go (4.1).

Not proved:

- `FSHELL106150`;
- corrected extra-notched Type-I absolute closure across comparable cutoffs;
- projection stability of the historical live-source `WKSFSC106150` into
  `FSHELL106150`;
- `NATBIND106150`, `EXTSRC106150`, BCI, RH, or GRH.

Refuted by the later complete-source atomic firewall:

- raw complete-beta Jordan negative variation `Y^o(1)`.  This is distinct
  from the still-open shell-projected gate above.

## 6. Frozen provenance and bounded replay

| claim | frozen blob |
|---|---|
| `L-102735` | `cb0f305b4e26b3f8553c7f6fe4bab5097b1ab97e` |
| `L-102886` | `26abf63b6a69c449f89313b151931b2dc71a42ad` |
| `L-102887` | `383aa27fee269645e45c26c12fbd4a97a6b337a8` |
| `L-102880` explicit native kernel | `d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6` |
| `L-102959` | `59f12fea22bc1871f160cf280baf62155225fdd2` |
| `L-102962` | `d8f4557df6dc37e6b605b1821c5b8ab028136398` |
| `T-102990` | `b319572db9ecc89bc528b85368cbf49aa13206d0` |
| `L-106080` | `346cc52420ec65457c2a5accc045d4a85635cc24` |
| `L-106132` | `f393a1d8583c5680b98a4b3e26d9b5a61c8d2b7a` |
| `L-106133` | `b988b14eb982504a799158eed4c76e7f033c96f0` |
| `L-106134` | `cf40354ff8810a2d4bea9459cf142c300ba36237` |
| `T-106150` | `ac15f0106a26303f06779feb484a521978fe3ecf` |

```text
python -B research/l-families/atlas/function_field/ffps_frozen_source_terminal_horizon_audit.py --check
python -B -O research/l-families/atlas/function_field/ffps_frozen_source_terminal_horizon_audit.py --check
python -B -m unittest tests.test_ffps_frozen_source_terminal_horizon_audit
python -B -O -m unittest tests.test_ffps_frozen_source_terminal_horizon_audit
python -B -m ruff check research/l-families/atlas/function_field/ffps_frozen_source_terminal_horizon_audit.py tests/test_ffps_frozen_source_terminal_horizon_audit.py
python -B -m ruff format --check research/l-families/atlas/function_field/ffps_frozen_source_terminal_horizon_audit.py tests/test_ffps_frozen_source_terminal_horizon_audit.py
```

The replay authenticates the twelve frozen blobs; reconstructs `a_U`, `f_U`,
and `b_U` by exact Boolean subset convolution; checks the sixth-root cutoffs,
physical source window, support dilation, and projection countermodel; and
enumerates no conductor, curve, or point.
