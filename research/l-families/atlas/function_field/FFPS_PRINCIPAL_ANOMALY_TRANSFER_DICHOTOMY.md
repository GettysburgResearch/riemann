# FFPS principal-anomaly transfer: exact two-channel dichotomy

Status: **exact logical and scalar consequence of the frozen FFPS identities;
conditional on the source claim that the principal moment implies the native
BCI consumer**.  This is not a proof of any open family estimate, BCI, RH, or
GRH.

## Start here

The existing source algebra already performs one form of
family-to-principal extraction.  With the notation frozen in PR #756,

\[
 P=A-K=C-S,
 \tag{0.1}
\]

where `P` is the principal Wick-centered trace, `A,K` are the complete
additive and nonprincipal Kummer traces, and `C,S` are the hard-current and
selected cyclic traces.  Therefore

\[
 \boxed{
 |P|\le |A|+|K|,\qquad |P|\le |C|+|S|.}
 \tag{0.2}
\]

Conversely,

\[
 \boxed{
 \max(|A|,|K|)\ge {|P|\over2},\qquad
 \max(|C|,|S|)\ge {|P|\over2}.}
 \tag{0.3}
\]

Thus a large principal anomaly cannot be invisible to both members of either
pair.  The exact invisible direction

\[
 (C,S,R)\mapsto(C+T,S+T,R-T)
\]

allows a large *common* hard/selected background while leaving `P` unchanged;
it does not allow a large `P` while both `C` and `S` remain small.

The important architectural correction is:

> Once both signed global gates in either pair are proved, no third algebraic
> family-to-principal amplifier is required.  Principal extraction is already
> equation (0.1).  What remains open is the analytic individualization needed
> to prove those signed gates.

A positive family-moment route which discards the signs is different and
still needs domination, inversion, or rigidity.  The statement above does not
turn a positive average into a principal bound.

## 1. Frozen source contract

The imported FFPS conclusion chain is `T-106140` at live PR #751 head
`98af0db6ec7f77d6333a77a3dac53c4698852f43`, blob
`d5be8e376c88b63de0be19e0d9e8791624e99ae2`.  Its source-level statements
used here are

\[
 P_{\rm PP}(Y)=D_{\rm PP}(Y)+P(Y)\ge0,
 \tag{1.1}
\]

\[
 D_{\rm PP}(Y)=Y^{o(1)},
 \tag{1.2}
\]

and the declared implication

\[
 P_{\rm PP}(Y)=Y^{o(1)}
 \Longrightarrow \mathrm{BCI}_{102990}
 \Longrightarrow \mathrm{RH}.
 \tag{1.3}
\]

The equality `P=A-K` is the same theorem's Wick-centered decomposition.  The
equality `P=C-S` and its exact coefficient-space boundary are locked in PR
#756 at
`FFPS_CYCLIC_CLOSURE_BUDGET.md`, blob
`b576c8a114d7e502b9b474cfed0db7e4cf6e2475`.

The reviewed Mellin--Landau consumer remains a useful independent endpoint,
but it accepts only a fixed detector satisfying its complete source,
multiplier, and one-sided arithmetic contract.  No identification of the
present `P` with a new Mellin--Landau input is made here.

## 2. Qualitative anomaly-transfer theorem

Assume the frozen source implication (1.3).  If RH is false, contraposition
gives

\[
 P_{\rm PP}(Y)\ne Y^{o(1)}.
 \tag{2.1}
\]

Because the paid diagonal in (1.2) is subpower, (1.1) then forces

\[
 |P(Y)|\ne Y^{o(1)}.
 \tag{2.2}
\]

Applying (0.3) yields the exact anomaly forks

\[
 \boxed{
 \neg\mathrm{RH}
 \Longrightarrow
 \bigl(A\ne Y^{o(1)}\ \text{or}\ K\ne Y^{o(1)}\bigr),}
 \tag{2.3}
\]

\[
 \boxed{
 \neg\mathrm{RH}
 \Longrightarrow
 \bigl(C\ne Y^{o(1)}\ \text{or}\ S\ne Y^{o(1)}\bigr).}
 \tag{2.4}
\]

Here `F != Y^o(1)` means failure of the declared global subpower estimate,
not a pointwise lower bound at every scale.

This is an exact qualitative transfer of any hypothetical RH counterexample
into a failure of at least one named family trace.  It does not say which
trace fails, identify the offending conductor fibres, or compute a growth
exponent from the real part of a hypothetical zero.

## 3. Quantitative subsequence form

Suppose, more concretely, that along an unbounded sequence `Y_j` there is a
fixed `delta>0` with

\[
 P_{\rm PP}(Y_j)\ge Y_j^\delta.
 \tag{3.1}
\]

The paid diagonal (1.2) is eventually at most `Y_j^delta/2`, so

\[
 |P(Y_j)|\ge {1\over2}Y_j^\delta.
\]

Consequently, on the same sequence,

\[
 \boxed{
 \max(|A(Y_j)|,|K(Y_j)|)\ge {1\over4}Y_j^\delta,}
 \tag{3.2}
\]

\[
 \boxed{
 \max(|C(Y_j)|,|S(Y_j)|)\ge {1\over4}Y_j^\delta.}
 \tag{3.3}
\]

The factors `1/2` and `1/4` use only the diagonal split and triangle
inequality.  They are sharp at the scalar-information level.

Neither the frozen source theorem nor this packet proves (3.1) with a
specific `delta=delta(beta)` from a zero `beta+i gamma`.  Deriving such a
rate would require reopening the exact native BCI-to-zero consumer with all
fixed-multiplier and cancellation conventions.  The qualitative fork (2.3)
does not require that stronger calculation.

## 4. What the cyclic route must actually accomplish

There are two logically different architectures.

### Signed extraction route

Either pair of global estimates

\[
 |A|+|K|=Y^{o(1)}
 \quad\text{or}\quad
 |C|+|S|=Y^{o(1)}
 \tag{4.1}
\]

already gives `P_PP=Y^o(1)` after the paid diagonal and hence reaches the
declared BCI implication.  There is no additional algebraic
individualization step after (4.1).

The open difficulty is proving the estimates after the complete signed
varying-conductor recombination.  A fibrewise triangle inequality does not
establish (4.1).

### Positive amplifier route

A positive hard-mask moment with improved inverse-Gram leverage does not by
itself give either estimate in (4.1).  The positive Wick residual and the
selected-mode burden remain.  Recovering a principal statement from that
positive average still requires one of:

- domination of the principal member;
- exact inversion with affordable loss;
- a rigidity theorem excluding selected-mode cancellation;
- or a signed identity which returns to (4.1).

The Pareto theorem in `FFPS_MASK_AMPLIFIER_PARETO_FRONTIER.md` makes the
rigidity burden quantitative: at the strongest leverage point, selected
modes of comparable squared amplitude can cancel one hard observation.

## 5. Consequences for experiment design

The exact anomaly fork suggests a more focused tomography experiment than a
generic family moment.

1. Construct trace-sheaf models for both `C` and `S`, not `S` alone.
2. Determine whether their large geometric constituents coincide in the
   common invisible direction.
3. Search for a signed projector which removes that common constituent while
   preserving `C-S`.
4. Track the resulting Betti/conductor cost uniformly.

If the same invariant constituent occurs with equal coefficient in `C` and
`S`, it cancels from `P` and should not be estimated separately.  Proving two
absolute bounds would then be unnecessarily strong.  A relative trace formula
for `C-S` may be the correct arithmetic target.

This is the most ambitious consequence of the audit: **sheafify the exact
difference, not automatically its two large summands**.

## 6. Exact boundary

Proved here from frozen identities:

- a principal anomaly forces one member of each named pair to be large;
- the common-growth invisible direction cannot hide a large principal
  difference from both `C` and `S`;
- both signed gates already perform algebraic principal extraction;
- the quantitative factor-four subsequence fork under hypothesis (3.1).

Not proved:

- any of `WCADD106140`, `WCKUM106140`, `CYHARD`, or `CYSEL`;
- a trace-sheaf model or relative trace formula for `C-S`;
- the quantitative response exponent of a specified hypothetical zero;
- BCI, RH, or GRH;
- that the live PR #751 conclusion chain has received independent canonical
  review.

