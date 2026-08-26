# Audit of the proposed mollified complete-source adapter

Status: **the exact Boolean half-source and extra-notched kernel identities
survive, but `MEXTSRC106150` is not proved by the frozen source chain; one
native-to-completed source bridge and one horizon-semantic binding remain
open**

Bounded source-lock replay:
[`ffps_mollified_complete_source_adapter.py`](ffps_mollified_complete_source_adapter.py).

Frozen sources: the Boolean/Hodge chain at `ec6635b4`, the half-source chain
at `98af0db6`, and the corrected extra-notched packets in this successor PR.
Read first:

1. `FFPS_COMMON_MOTHER_OUTER_NOTCH_MISMATCH.md`;
2. `FFPS_EXTRA_NOTCH_CLOSED_SECTOR_TRANSPORT.md`;
3. `FFPS_FROZEN_SOURCE_TERMINAL_HORIZON_AUDIT.md`;
4. `FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md`.

## 0. Exact target and verdict

Let

\[
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67),
\]

and let `K_ext` be the compact signed measure with multiplier

\[
 \widehat K_{\rm ext}(s)
 ={q(s)^2r(s)^2(s-1)(5s+3/2)\over s(s-1/2)},
\quad
 q(s)=1-\sqrt2\,2^{-s},\quad r(s)=1-2^{-s}.
\tag{0.1}
\]

Fix `epsilon>0`, independently of the physical horizon, and put, in
logarithmic coordinate,

\[
 k_\varepsilon=\eta_\varepsilon*K_{\rm ext},
 \qquad
 \eta_\varepsilon={1\over\varepsilon}1_{[0,\varepsilon]}.
\tag{0.2}
\]

The function `k_epsilon` is fixed, compactly supported and BV.  It has zero
logarithmic mass: `r(s)^2/s` has a simple zero at `s=0`, every other factor in
(0.1) is finite there, and `eta_epsilon` has mass one.  Define the complete
mollified density

\[
 H_{\beta,\varepsilon}(X)
 =\sum_{n\ge1}{\beta(n)\over\sqrt n}
 k_\varepsilon(\log X-\log n).
\tag{0.3}
\]

The correct blockwise raw live object must be a signed Borel measure.  In log
coordinate set

\[
 B_j=[j\log2,(j+1)\log2),
 \qquad U_j=\lfloor2^{j/6}\rfloor,
\]

and define, with every endpoint atom assigned once by the half-open
convention,

\[
 \boxed{
 L_{\rm fr}
 =\sum_j
 \left.
  (\mathcal D_{\rm out}\mathcal J_{U_j}^{\diamond})
 \right|_{B_j}.}
\tag{0.4}
\]

Here `J_(U_j)^diamond` is the complete canonical equal-pair Boolean/Wick
half-source measure of `L-106133--L-106134`; all literal labels, both copies
of `67`, and every balanced sector remain present.

The desired fixed-mollified source gate is

\[
 \boxed{
 H_{\beta,\varepsilon}
 =\eta_\varepsilon*L_{\rm fr}+E_\varepsilon,
 \qquad
 \int_{2^j}^{2^{j+1}}|E_\varepsilon(X)|{dX\over X}
 =2^{o(j)}.}
\tag{0.5}
\]

Call (0.5) `MEXTSRC106150`.  The frozen claims do **not** prove it.  They prove
the two ends of the proposed chain but not the load-bearing arrow

```text
native beta / harmonic balanced observation at k_epsilon
  -> completed x_p x_q y_C equal-pair observation at k_epsilon
     modulo an additive absolute-subpower field.
```

The distinction is mathematical, not bibliographic.  The available
completion theorem gives a multiplicatively invertible polylogarithmic gauge;
it does not say that the gauge difference is an additive `L1`-small field.
Section 2 gives the exact obstruction.

The correct one-sided premise for the direct consumer is likewise mollified:

```text
MWKSFSC106150:
  (eta_epsilon * L_fr)_- has Y^(o(1)) logarithmic mass
  on every finite horizon.
```

Thus the valid implication matrix is

```text
MEXTSRC106150 [OPEN]
  + MWKSFSC106150 [OPEN]
  + the direct fixed-mollified extra-notched Mellin--Landau consumer
  -> RH.
```

This is not raw `EXTSRC106150`.  The unmollified complete beta current has
atoms, and no raw complete-current Jordan premise is asserted here.

## 1. Components which are exact

### 1.1 Labelled beta scaling

On a finite labelled horizon, with label set `mathcal L` and two distinct
labels above the physical prime `67`, the labelled-squarefree Euler source is

\[
 \prod_{\ell\in\mathcal L}(1-x_\ell).
\tag{1.1}
\]

The malformed labelled product in the draft has been replaced by (1.1).
After physical collapse, the local factor at `67` is

\[
 (1-x_{67,1})(1-x_{67,2})=1-2x_{67}+x_{67}^2.
\]

Thus physical `67` exponents `0,1,2` have coefficients `1,-2,1`, exactly the
coefficients of `beta(n)/sqrt(n)`.  The source is squarefree in the labelled
Boolean algebra, not in the physical integer after the two labels collapse.

### 1.2 Hodge and Boolean identities

`L-102951` gives the local identity

\[
 M(x)^2
 =(1-x)+x^2\left(-{3\over4}+{x\over2}+{x^2\over4}\right).
\tag{1.2}
\]

The actual global Hodge transfer is `L-102906.3--.4`: the ratio and its
inverse have zero linear coefficient and polylogarithmic source norm at the
frozen observation scope.  `L-102505` alone is not that theorem; it controls
only its displayed squared-core operator.

The finite Boolean Vaughan identity is exact:

\[
 \mu_{\rm sf}
 =2\mu_U-\mu_U\star\mu_U\star1_{\rm sf}
  +a_U\star a_U\star\mu_{\rm sf}.
\tag{1.3}
\]

`L-102952` shows that owner restriction commutes with this identity.  For the
balanced coefficient, `L-106132` puts

\[
 h(S)=(-1/2)^{|S|},\qquad f_U=a_U\star h,
\]

and proves exactly

\[
 f_U\star f_U
 =a_U\star a_U\star\mu_{\rm sf}.
\tag{1.4}
\]

This is a Boolean square, not a positive physical square and not ordinary
convolution.

### 1.3 Canonical equal-pair Beta average

Inside the already-completed Boolean source, `L-106133.12` proves

\[
 \boxed{
 \mathfrak B_U^{\rm eq}
 =\int_0^1(1-\theta)
   \mathfrak G_{U,\theta}\star
   \mathfrak G_{U,\theta}\,d\theta.}
\tag{1.5}
\]

For a support of depth `k`, the two owner orders contribute `2`, while

\[
 \int_0^1(1-\theta)\theta^{k-2}\,d\theta
 ={1\over k(k-1)}.
\]

Their product is `1/binom(k,2)`, exactly the canonical unordered-pair share.
`L-102962` proves that these shares sum to one and that every pair is
completion-safe.  This redistributes owner labels in the completed source; it
does not itself replace a native atom `U_p` by a completed atom `U_(p^2)`.

The source `B_U^eq` in (1.5) is complete.  Equal-core and one-sided-core
sectors remain inside it.  They must not be deleted and then silently restored
after a signed filter.

### 1.4 Exact extra-notched kernel identity

`L-106134.8` gives, coefficientwise in the labelled source algebra,

\[
 \mathcal O_{\Phi_*}[\mathfrak B_U^{\rm eq}]
 =(2D-1)\mathcal J_U^\diamond.
\tag{1.6}
\]

Apply

\[
 {1\over2}D(D-1)(5D+3/2)
\]

to both sides.  Since

\[
 \widehat\Phi_*(s)
 ={2q(s)^2r(s)^2\over s^2(s-1/2)},
\]

the left multiplier is exactly (0.1), and the right side is exactly
`D_out J_U^diamond`.  The sign and the factor `2D-1` are correct.  This is the
extra-notched identity; it does not use the false native-outer naming corrected
by the mismatch packet.  Positive mollification commutes with this exact
fixed-source identity.

## 2. The missing native-to-completed adapter

The native balanced source in (1.3) uses first-power atoms

\[
 x_p=p^{-1/2}U_p.
\]

The half-source in (1.5) uses, for every nonowner core label,

\[
 y_p=p^{-1}U_{p^2}.
\]

These are different physical translations.  Equal-pair allocation changes
only the owner coordinate and cannot identify them.

The closest frozen bridge is `L-102706`.  Its exact statement is

\[
 H_\tau=G_\tau E_\tau,
 \qquad
 \|G_\tau\|+\|G_\tau^{-1}\|\ll(\log Y)^C,
\tag{2.1}
\]

where every nonconstant local coefficient of `G_tau` begins at squared
activity.  Equation (2.1) is a bounded multiplicative gauge equivalence.  It
does not imply

\[
 \|\mathcal O_{k_\varepsilon}[H_\tau-E_\tau]\|_{L^1}
 =Y^{o(1)}.
\tag{2.2}
\]

Indeed, `(G_tau-I)E_tau` still contains the unresolved critical field
`E_tau`; a polylogarithmic operator norm only bounds it by the norm of that
field.  Treating `G_tau-I` as an independently closed squared packet spends a
gauge before the regional physical recombination, contrary to the scope
firewall in `L-102706`.

`L-102709.1` is coefficient-exact when the **full** homotopy current with
common endpoints is retained.  Its intermediate-switch paragraph again
invokes (2.1); it does not identify that full current with the specific
`x_p x_q y_C` field of (1.5), and it does not prove (2.2).

`L-102954.1` supplies an additive reduction only for its frozen
fixed derivative/common-mother observation.  Moving that statement to the
new mollified `K_ext` requires a claim-by-claim replay of the completion and
homotopy rows `L-102602--L-102604` and `L-102706--L-102709`.  The generic
Type-I and absolute-sector theorem does not perform that replay.  In
particular, the following row is still absent:

```text
NATCOMP-MOLL106150:
  at the fixed kernel k_epsilon, the native labelled balanced observation
  equals the complete x_p x_q y_C equal-pair observation plus an additive
  absolute-Y^(o(1)) field, with the full homotopy kept through physical
  collapse.
```

`NATCOMP-MOLL106150` is precisely the missing source arrow in (0.5).  The
exact identities in section 1 do not prove it by composition.

## 3. What does transport to `k_epsilon`

The following rows have a valid generic mechanism once their exact source
binding is already in hand.

| row | frozen source | fixed-`k_epsilon` mechanism |
|---|---|---|
| Boolean Type I | `L-102953`, `L-106080` | compact BV, zero mass lattice theorem; final `Y^(-1/12+o(1))` |
| diagonal and equal product | `L-102702`, `L-102883` | source energy and representation multiplicity with a fixed `L2` kernel |
| same-owner square cores | `L-102705` | fixed compact-kernel autocorrelation bound |
| pair-owner collapse | `L-102747`, `L-102962` | exact allocation and `O(log^2 Y)` multiplicity |
| very-large common square | `L-102887` | absolute common-square summation |
| source-`l1` squared/higher rows | `L-102601`, `L-102904--L-102906` | Tonelli after the exact source packet has been isolated |
| finite and terminal rows | `L-102886`, `L-106080` | fixed finite support, with a constant depending on `k_epsilon` |

For a Hilbert row, logarithmic Cauchy--Schwarz on one block gives

\[
 \|F\|_{L^1([2^j,2^{j+1}),dX/X)}
 \le(\log2)^{1/2}\|F\|_{L^2(dX/X)}.
\tag{3.1}
\]

For a source-`l1` row, Tonelli gives the corresponding fixed-kernel bound.
These facts verify the rowwise kernel transport; they do not manufacture the
missing source decomposition `NATCOMP-MOLL106150`.

The equal-core and one-sided-core estimates of `L-102955` are not rows to
discard in the proposed (0.5).  Those sectors stay inside the complete
`J_U^diamond` premise.  No ordinary self-convolution is used; the Wick
projection in (1.5)--(1.6) remains exact.

## 4. Block freezing and the WKSFSC fence

`L-102886` proves an exact blockwise decomposition with `U_j` fixed on
`B_j`, but only after Type I and balanced rows are recombined before taking a
negative part.  It does not define the terse raw WKSFSC sentence in
`T-106150` as the Jordan variation of the piecewise measure (0.4).

If one separately assumes

```text
FRWKSFSC106150:
  L_fr^-([0,T])=exp(o(T)) for the half-open piecewise measure (0.4),
```

then positivity and the one-sided support of `eta_epsilon` give the
finite-horizon contraction

\[
 \int_0^T(\eta_\varepsilon*L_{\rm fr})_-(t)\,dt
 \le L_{\rm fr}^-([0,T]).
\tag{4.1}
\]

Thus `FRWKSFSC106150 -> MWKSFSC106150`.  No global total-variation norm is
used; it may be infinite.

The phrase “on every dyadic horizon” in `T-106150` does not specify the
half-open restriction, ownership of boundary atoms, or whether the same
cutoff is retained on the support enlargement used by a mollifier.  Therefore

```text
literal raw WKSFSC106150 wording
  -/-> FRWKSFSC106150 or MWKSFSC106150
without an additional source/horizon semantic lemma.
```

This is a local cutoff/source quantifier issue, not an anti-causal future
problem.  Defining (0.4) also avoids differentiating a moving cutoff: each
`D_out J_(U_j)^diamond` is formed before the Borel restriction.

## 5. Exact boundary

Proved by the audited sources:

- the labelled duplicate-`67` beta coefficients and physical scaling;
- the local Hodge formula and exact Boolean Vaughan identity;
- owner-restriction functoriality and the Boolean half-source square;
- the canonical Beta coefficient `1/binom(k,2)` inside the completed source;
- retention of equal-core and one-sided balanced sectors in complete
  `J_U^diamond`;
- the extra-notched multiplier, sign, and `L-106134` differential identity;
- the rowwise generic transport mechanisms listed in section 3;
- the half-open signed-measure construction (0.4) and contraction (4.1).

Not proved:

- `NATCOMP-MOLL106150`;
- the proposed adapter `MEXTSRC106150` in (0.5);
- `FRWKSFSC106150` or `MWKSFSC106150`;
- the identification of the literal terse `WKSFSC106150` wording with either
  piecewise gate;
- RH or GRH.

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_mollified_complete_source_adapter.py --check
python -B -O research/l-families/atlas/function_field/ffps_mollified_complete_source_adapter.py --check
python -B -m unittest tests.test_ffps_mollified_complete_source_adapter
python -B -O -m unittest tests.test_ffps_mollified_complete_source_adapter
```

The replay authenticates the frozen blobs, the source-path disposition, the
duplicate-`67` coefficients, the kernel multiplier, the Type-I exponents, and
the horizon fence.  It enumerates no conductor, source family, curve, prime
interval, or point.
