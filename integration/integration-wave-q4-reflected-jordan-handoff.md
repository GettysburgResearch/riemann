# Integration-wave handoff: Q4 reflected–Jordan–inertia lineage

**Cutoff:** `2026-08-10T22:00:51Z`  
**Frozen main:** `d6409319b4041cd09bee85f55a344631508f2501`  
**Review branch:** `review/integration-wave-20260810-q4`  
**Detailed report:** `reports/integration-wave/20260810-q4-reflected-jordan-review.md`  
**Claim table:** `audits/integration-wave/20260810-q4-reflected-jordan-status.tsv`  
**Exact review artifacts:** `audits/integration-wave/20260810-q4-exact-counterexamples.md`

## Integration decision in one paragraph

Integrate the exact independent-frequency reflected identities, corrected
source/carry typing, physical endpoint placement, compact Q4 source and
row recurrence, reserve identities, zero-bare state, all-pass/Q2
dictionaries, negative-inertia lemmas, and pole-preservation firewalls.
Do **not** integrate PR #359's full RH composition as a theorem. Its
aggregate determinant lemma survives, but the composition is false.
Do **not** integrate PR #357's statement that everything outside PIG is
closed without demotion: the global source/state recurrence is not
proved, and one stated spectral-mass transfer is false. Retain PR #362
as the corrected research frontier: RH implies PIG, the compact
innovation is zero-safe, and unconditional PIG remains open. RH is not
established.

## Strongest surviving proof spine

```text
#241
exact independent-frequency bireflected Selberg block
  |
  v
#268/#354
correct RH-sensitive source typing:
ordinary prefix -> divisor convolution -> carry placement
  |
  v
#339/#341
exact real-X and integer physical/carry placement,
predecessor state, endpoint atom, one-unit collar
  |
  v
#325/#342/#345
compact Q4 source, zero-bare relative source,
critical reserve, exact own-current and delayed recurrence
  |
  v
#357/#359 components
two-state Hermitian curvature,
row and aggregate negative-mass bounds,
nonnegative aggregation and all-pass inertia telescope
  |
  v
BROKEN:
negative inertia does not bound positive innovation current
and no valid <2/5 synthesis contraction exists
  |
  v
OPEN:
PIG = polynomial integral of |I_circ|^2/n
  |
  v
CONDITIONAL:
exact global recurrence -> subexponential state energy
  |
  v
#297 + #362
vector pole-energy consumer + zero-safe Q4 multiplier
  |
  v
RH
```

## First load-bearing theorem to attack

A legitimate next theorem must address the **positive** Q4
source-convolved product/current Gram. Negative inertia is no longer
the correct statistic.

A clean target is:

> Fix one exact balanced block measure and one exact Q4 compact-source
> physical state. Prove either
> \[
> \int \frac{|I_\circ(n,j)|^2}{n}\,d\nu_J
> \le C(1+J)^A,
> \]
> or an explicitly weaker statistic that still feeds a proved
> pole-energy consumer without converting signed curvature into
> positive mass.

At the present frontier this is RH-equivalent in substance. Generic
\(\ell^2\), wavelet, or finite-filter norm estimates are too large;
new arithmetic information or a genuinely stronger finite-compression
statistic is required.

## Pre-PIG repair obligations

Before advertising a complete “PIG implies RH” assembly, close all of
the following in one theorem.

1. **One metric.** Name the coefficient/physical Hilbert metric and
   the exact block measure throughout.
2. **One source substitution.** Prove that the source in the all-pass
   state is the exact compact source in the physical recurrence.
3. **No false multiplier transfer.** Remove `L-90308.12` or replace it
   with a source-specific theorem. An \(L^\infty\) bound for a
   nonconstant multiplier does not transfer positive/negative masses
   of an integrated indefinite curvature.
4. **Final reservoir.** Bound the negative mass of the surviving
   root/base reservoir after internal Q2 states cancel.
5. **Pushforward.** Write the exact map from the predecessor block to
   the next radix-four block, including Jacobian/weights.
6. **Collars.** Insert endpoint, floor-borrow, and filter-cut collars
   into the recurrence rather than citing them separately.
7. **Terminal state.** State and bound every finite-base or terminal
   term.
8. **Pole adapter.** Map the exact PIG field and measure to the exact
   #297 vector local-energy criterion, or prove a dedicated compact-Q4
   pole-energy theorem.

## Urgent contradiction 1: #359 synthesis contraction

PR #346 proves a weighted coefficient-energy budget and a joint
jet-frame inequality. It does not prove
\(W^*W\le qI\), \(q<2/5\).

At \(z=2^{-1/2}\),

\[
|W_+(z)|^2+|W_-(z)|^2
=
\frac{751606691}{24000000}
-
\frac{277818163}{18000000}\sqrt2
\approx9.4894891256567.
\]

The exact excess above \(2/5\) is positive because

\[
2226020073^2-2(1111272652)^2
=
2485311551232699121.
\]

**Integration action:** reject the operator-contraction arrow in
#359. Preserve the valid coefficient budget and the valid joint
jet-frame theorem under their actual scopes.

## Urgent contradiction 2: #357 spectral-mass transfer

`L-90308.12` attempts to pass positive and negative curvature masses
through multiplication by \((1-4^{-s})^{-1}\) using only its
critical-line norm bound. This is false for indefinite integrated
curvature.

Identical bumps at \(0\) and \(\pi/\log4\) cancel before multiplication.
The nonconstant weight

\[
\left|1-\tfrac12e^{-it\log4}\right|^{-2}
\]

weights the first bump more strongly and destroys the cancellation.
Reversing the signs violates the corresponding negative-mass bound.

**Integration action:** remove this transfer from the proof spine.
Retain only the exact source dictionary until a valid source-specific
replacement is supplied.

## Urgent contradiction 3: negative inertia versus positive current

For the zero-bare two-state row,

\[
\det K(I)=(R-E^2)I^2+ETI-\frac{T^2}{4}.
\]

When \(R-E^2>0\), the determinant is positive for all sufficiently
large \(|I|\). Thus the negative spectral mass can be zero while the
current is arbitrarily large.

**Integration action:** integrate #357 `R-90302` as a permanent
firewall and mark any theorem using “small inertia implies small
current” as false.

## Source-order checklist

For every integrated theorem, retain this order explicitly:

```text
arithmetic source f
  -> ordinary divisor convolution 1*f
  -> finite Q2/Q4 source multiplier
  -> common Jordan path and its derivatives
  -> physical prefix/carry placement
  -> independent-frequency reflected block
  -> physical aggregation
```

A theorem may use a different equivalent order only after proving the
relevant operators commute. In particular:

- ordinary prefix is not Selberg carry;
- carry of \(f\) is built from prefix of \(1*f\);
- pure carry windows may cancel zeta poles;
- filters and Jordan differentiation commute only because the filters
  are parameter-independent and are applied to one common path.

## Scale and spending checklist

```text
own innovation:             current scale
normalized state U(n,j):    predecessor scale
gauge L_(n,j)(b4):          delayed by one radix-four step
integer endpoint atom:      explicit collar
critical reserve:           charged once in local curvature/inertia
PIG forcing:                separate positive current mass
```

Reject any composition that:

- returns a delayed gauge as current-scale forcing;
- drops the endpoint atom or floor-borrow collar;
- charges the same Q4 reserve in both local curvature and PIG;
- centers each row with a different shear before aggregation;
- changes a genuine two-frequency block into a one-frequency square.

## Pole-preservation checklist

- Reject direct pure carry-window pole consumers (#269).
- Require every finite multiplier in the final source to be nonzero at
  each hypothetical open-strip zero.
- For the compact Q4 source, retain #362's exact fact that the own
  current has pole order \(m+1\), while the delayed gauge has order
  \(m\).
- Do not infer an energy lower bound from nonvanishing alone; the exact
  block norm and measure must match the pole consumer.

## Suggested registry/lifecycle treatment

| Lineage item | Recommended lifecycle |
|---|---|
| #241, #263 exact identities | current route infrastructure |
| #268/#269 source and pole firewalls | current refutations/firewalls |
| #325, #337, #339, #341, #342, #345 exact infrastructure | current, with scoped proof boundaries |
| #346 coefficient budget and joint jet frame | current, scope corrected |
| #349 | superseded historical correction |
| #350 | current refutation/centered repair; ignore narrative-only absent files |
| #354 | current corrected source/convolution and matrix firewall |
| #357 inertia lemmas and `R-90302` | current infrastructure/firewall |
| #357 complete assembly claim | demote to UNPROVEN / GAP |
| #359 aggregate determinant lemma | current standalone theorem |
| #359 full composition | FALSE and SUPERSEDED |
| #362 RH=>PIG and zero-safety | current conditional frontier |
| #362 PIG=>RH / PIG equivalence | open/conditional pending repaired adapter |
| RH | not established |

## Retained computation handling

The review inspected but did not rerun `X-9515`, `X-32402`,
`X-34401`, `X-90301`, `X-90302`, `X-90402`, and `X-29002`.
Preserve their hashes and finite scope. Do not cite any of them as
certifying the global recurrence, PIG, pole exclusion, or RH.

## Final handoff verdict

The Q4 programme has a substantial exact infrastructure and a useful
Claude-inspired negative-inertia mechanism. The newest valid
mathematical conclusion is not a proof of RH but a sharper diagnosis:
the residual positive compact innovation energy is the RH-bearing
quantity. The integrator should preserve that diagnosis, remove the
two false transfer steps, and require one exact physical block
recurrence plus one exact pole-energy adapter before treating PIG as a
fully installed RH-equivalent criterion.
