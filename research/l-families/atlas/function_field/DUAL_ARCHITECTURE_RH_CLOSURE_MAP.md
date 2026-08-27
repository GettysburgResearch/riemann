# Two non-blended RH architectures after PR #757

Status: **exact route map plus two new reviewable reductions; RH remains
unproved**

Frozen base for this packet: PR #757 head
`b870366141fe8d5f43d5b81f6e50a67d2a888070`.

This handoff deliberately keeps the two architectures separate.  They share
only the final proposition `RH`; no estimate, averaging theorem, or geometric
object is silently transferred between them.

---

## Architecture A — direct beta / primitive-pair route

```text
fixed mollified beta detector
  -> compact boundary field
  -> ratio-16 autocorrelation Gram
  -> high balanced primitive pairs
  -> full product-shell Möbius wavelet
  -> weighted core-wavelet square function
  -> PRIMCAR -> PRIMLS -> RH.
```

### Imported exact spine

PR #757 already supplies:

1. a fixed source-faithful mollified beta detector whose boundary-field mass
   is RH-equivalent;
2. an exact positive ratio-sixteen Gram criterion;
3. unconditional removal of fixed/subpower primitive rays;
4. the three high primitive channels `alpha=0,1,2`;
5. `PRIMCAR -> PRIMLS -> RH` as a conditional implication;
6. the rho-tilt convolution isomorphism and the divisor-wavelet coordinates.

### New reduction in this packet

For every dyadic height block `I`, the **full** primitive panel is

\[
 \mathcal P_I^\alpha(d)
 =\sum_{(N,d)=1}{\mu(N)\over\sqrt N}\mathcal W_I^\alpha(N)
 =\sum_{r\mid d}{\mathcal Z_{I,r}^\alpha\over\sqrt r}.
\]

The transform has the exact inverse

\[
 \mathcal Z_{I,r}^\alpha
 =\sqrt r\sum_{s\mid r}\mu(r/s)\mathcal P_I^\alpha(s).
\]

Define

\[
 \mathrm{COREAGG}:\qquad
 \sum_r{\tau(r)\over r^2}
 \sum_{I\in\mathscr D_H}|\mathcal Z_{I,r}^\alpha|^2
 \ll_\varepsilon(2H)^\varepsilon.
\]

On the actual factor-64 support, the divisor transform and its inverse both
have subpower weighted norm.  Therefore

\[
 \boxed{\mathrm{COREAGG}\Longleftrightarrow\mathrm{PRIMCAR}}
\]

at the repository's all-positive-exponent scale.  This is the principal
Architecture A advance: the entire finite-sieve incidence burden is one
weighted family of **one-variable signed Möbius/divisor-wavelet square
functions**.  No separate zero-mode theorem and nonzero-mode theorem are
logically required.

A stronger memberwise gate is

\[
 \mathrm{COREWAVE}:\qquad
 \sum_I|\mathcal Z_{I,r}^\alpha|^2
 \ll_\eta(2Hr)^\eta,
\]

which implies COREAGG because the outer series is
`sum tau(r)/r^(2-eta)` and converges for `eta<1`.

### Smallest remaining theorem

The exact conclusion-bearing target is now simply:

```text
For alpha in {0,1,2}, uniformly in H,

sum_(r squarefree, 67-free) tau(r)/r^2
  sum_(I in D_H)
    | sum_(M squarefree, (M,67r)=1)
        mu(M)/sqrt(M) W_I^alpha(rM) |^2
  <<_epsilon (2H)^epsilon.
```

This is COREAGG, equivalently PRIMCAR.  It remains open and is of essentially
RH strength.

### Analytic execution order

1. Replace each hard block by two smoothed height prefixes.
2. Use the exact Fourier--hyperbola formula
   \[
   W_{\le T}^\alpha(N)
   ={1\over2\pi}\int |\widehat K(\xi)|^2A^{i\xi}N^{-i\xi}
   \sum_{N/T\le a\le T/A,\ a\mid N}a^{2i\xi}\,d\xi.
   \]
3. Split `xi=0`, small frequency, and oscillatory frequency rather than
   taking a uniform absolute bound.
4. Hyperbola/Vaughan-decompose the outer `mu(M)` while preserving the common
   divisor polynomial.
5. Prove the weighted mean square after summing over `r` with `tau(r)/r^2`;
   do not demand a stronger pointwise-in-`r` theorem unless needed.
6. Unsmooth with a bounded-variation or Carleson argument that retains the
   dyadic block sum.

### Mandatory falsification checks

- retain the `xi=0` half-divisor component;
- treat `alpha=1,2` with their actual `67^alpha` height geometry;
- keep the block sum, not only one terminal interval;
- do not replace the signed Möbius sum by its absolute divisor mass;
- verify uniformity at both `r=1` and `r` near the product-shell ceiling;
- preserve the literal ratio-sixteen kernel and the exceptional Euler factor.

Primary packet:
[`FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md`](FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md).

---

## Architecture B — family / sheaf amplification

```text
hard physical restriction
  -> one common native torsor/source object
  -> relative projector C-S=Pi_0
  -> relative-only partial Frobenius
  -> closed-point Adams-Mobius extraction
  -> uniform signed relative trace estimate
  -> exact principal binding
  -> RH.
```

### Imported exact spine

PR #757 already supplies:

1. a universal clean ternary norm/Kummer torsor with bounded physical ranks;
2. the honest endomorphism identity `C-S=Pi_0` on every genuine cyclic
   torsor and survival under common additive cleanup;
3. one- and separable two-place closed-point Adams--Möbius extraction;
4. the exact full-cycle selector mass no-go;
5. the principal identities `P=C-S=A-K` and the warning that positive family
   moments still need individualization;
6. a precise list of unassembled native owner/Boolean/Artin--Schreier/
   incidence/Wick interfaces.

### New reduction in this packet

The order of operations can be sharpened:

```text
Do not first prove that C and S are separately separable.
Transport the honest projector through the common source cleanup,
form R=F(im Pi_0), and ask for partial Frobenius only on R.
```

Once the relative object `R` exists in the partial-Frobenius category,
closed-point extraction applies directly:

\[
 abP_{a,b}(R)
 =\sum_{e\mid a,f\mid b}\mu(e)\mu(f)
 A_{a/e,b/f}^{\partial}(\psi_1^e\psi_2^fR).
\]

Thus on the signed route:

- common hard/selected resonances cancel before estimation;
- the selected cubic characters cancel before Adams;
- no separate `CYSEL` estimate is needed;
- no later algebraic family-to-principal amplifier is needed.

For the clean physical deck layer, `R=R_2 boxtimes R_2` and every partial
Adams transform has one of four parity profiles, all of absolute weighted
line mass `16`.  This removes the cubic mod-three case split and lowers the
finite physical package from hard mass `24` to relative mass `16`.

The caveat is load-bearing: source-pushforward Frobenius eigenvalues are still
raised to their full exponents `e,f`.  The four finite-deck profiles are not a
four-case Betti theorem.

### Smallest remaining geometric stack

```text
NATREL
  Construct the complete native common source and identify its transported
  invariant-projector image with the exact principal difference.

RELPARTFROB
  Prove only that this relative image has commuting partial Frobenii or a
  finite external-product presentation.

RELTRACE
  Bound the signed double Adams-Mobius trace recombination uniformly in
  conductor, degree, horizon, and every source cleanup.

PRINCIPAL_BINDING
  Match that closed-point trace coefficientwise to the frozen principal
  moment consumed by the RH implication.
```

Conditional closure is

\[
 \boxed{
 \mathrm{NATREL}+\mathrm{RELPARTFROB}+\mathrm{RELTRACE}
 +\mathrm{PRINCIPAL\_BINDING}\Longrightarrow\mathrm{RH}.}
\]

None of these native/global gates is proved in this packet.

### Geometric execution order

1. Build the image of `Pi_0` directly on the complete owner/core source,
   rather than separately sheafifying large hard and selected summands.
2. Pull both source-selected Artin--Schreier phases through the projector and
   test whether their coupled part cancels, factors externally, or produces
   an explicit partial-Frobenius obstruction.
3. Perform shared incidence, equal-product, root, and Wick cleanup only by
   common equivariant maps.
4. Prove the relative class lies in the partial-Frobenius category before
   introducing degree selectors.
5. Apply exact closed-point inversion.  Retain the equal-degree distinct-place
   correction.
6. Estimate the signed Adams sum as assembled; use the termwise
   `2^(omega(a)+omega(b))` bound only as a fallback.
7. Audit total compactly supported Betti/conductor growth after source
   pushforward.  Rank `16` of the physical quotient is not this total.
8. Bind the resulting trace to the exact native principal horizon and invoke
   the existing principal consumer.

### Mandatory falsification checks

- failure of partial Frobenius after the relative projection, not merely
  before it;
- asymmetric cleanup on hard and selected sources;
- a coupled Artin--Schreier phase surviving `Pi_0`;
- diagonal Frobenius masquerading as two partial Frobenii;
- missing equal-place correction when degrees agree;
- Betti growth hidden behind bounded physical rank;
- a positive family bound substituted for the signed relative trace;
- a clean local trace substituted for the native principal normalization.

Primary packet:
[`FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md`](FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md).

---

## Final scientific status

Architecture A now has a single exact one-variable aggregate estimate between
PR #757 and RH.  Architecture B now has a smaller relative-only categorical
adapter and a signed closed-point extraction theorem between the physical
mask and the principal consumer.

Neither remaining estimate is proved.  **RH and GRH remain open.**
