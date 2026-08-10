# Anthropic 95-page campaign transcript — failure ledger and Q4 lessons

Date: 2026-08-10  
Authoring agent: `gpt56-sol`  
Source: user-supplied 95-page Anthropic transcript/explanation, *How the two-thirds argument was found: two agent runs and their literature*  
Status: methodology/source digest plus repository mapping; no external theorem is promoted beyond the accompanying paper

## 1. The most useful fact is the shape of the failures

The transcript is unusually valuable because it records not only the successful rank--trace idea but the routes that failed before it.  The recurring pattern is:

```text
wrong object / wrong sign / wrong coordinate
    -> apparently deep obstruction;

exact retyping / dualization / coefficient coordinates
    -> obstruction disappears;

one genuinely invariant scalar remains
    -> theorem or honest hard wall.
```

That pattern is directly relevant to the current Q4 route.

## 2. Failure: pointwise signed density was the wrong operator

R4 saw a prime-computable density `nu_X` negative on a substantial fraction of a height window and a warped-sinc operator with many negative eigenvalues.  The one-half run proved that this operator was **not** the honest compression of the Weil form.  The true Gabor Gram compression was positive in every computable RH-verified range; the apparent negative index tracked pointwise symbol dips at exactly the uncertainty scale.

Repository lesson:

> Never infer a source/state sign from a pointwise symbol or from an operator merely sharing its diagonal.  Preserve the exact physical Gram/carry map before taking inertia.

This supports the present insistence on PR #341's exact prefix/carry Gram and PR #339's independent-frequency block identity.

## 3. Failure: the negative-index route had the wrong monotonicity direction

The intended Pontryagin route asked the negative index of a compression to upper-bound off-line zeros.  Pullback can only **lose** negative squares, so the inequality pointed the wrong way.  The useful theorem came from dualizing: positive index plus the Riemann--von Mangoldt double count certifies on-line zeros.

Repository lesson:

> A controlled spectral defect is useful only when it appears with the correct sign in the final consumer.

This is exactly why `R-90302` is needed: the Q4 negative spectral mass can be tiny while the current is arbitrarily large.  Its valid use is inside the signed all-pass telescope (`L-90306`), not as an amplitude bound.

## 4. Failure: mass-matrix orthonormalization created spurious negative directions

The transcript records 33 spurious negative eigenvalues produced by an ill-conditioned mass-matrix reduction.  The successful repair was to work directly in coefficient coordinates and use the exact Poisson identity; the inertia lemmas did not require an inner product change.

Repository lesson:

> Do not solve the final Q4 metric mismatch by orthonormalizing each source/state separately.

The correct response is the fixed odd-Jordan carrier in `L-90307`: all Q2/Q4 filters are parameter-independent on one physical block metric, and the exact source/state identities are written before any inequality.

## 5. Failure: higher moments were the wrong lever

The two-thirds run explicitly tested higher spectral moments.  The third moment is available in the useful bandwidth range but cannot improve a support/count problem on an unbounded positive spectrum without an a-priori top-eigenvalue bound; the fourth moment only becomes accessible when the bandwidth is too small to certify the desired proportion.  The transcript treats the needed top-eigenvalue control as Lindelof-strength.

Repository lesson:

> Do not answer the remaining Q4 amplitude problem by manufacturing third/fourth curvature moments unless a matrix polynomial inequality is proved **first** and its prime/source side is genuinely softer.

For the present two-state matrix, `R-90302` already shows why an extra moment would have to control the positive current mass rather than the negative eigendirection.

## 6. Failure: free mass and free phase destroyed quadratic per-pair pricing

The two-thirds run tried several quadratic inequalities for off-line pair blocks.  They failed whenever the pair mass or phase was allowed to float.  What survived was the functional-equation/Poisson **phase lock** plus quantized mass, and the correct theorem was linear in the masses (the rank--trace inequality), not a per-pair quadratic lower bound.

Repository lesson:

> Before seeking a quadratic Q4 source inequality, identify what is actually quantized/phase-locked by the Euler/source algebra.  If no such invariant exists, expect a linear trace/rank statement instead.

The root-of-unity Q4 bank is promising here because its active dyadic channels are exact Fourier modes with fixed coefficients; however no claim is made yet that they provide the missing quantization of the RH current.

## 7. Failure: the de Branges tilt lost prime computability

The transcript notes that an off-centre de Branges/Krein--Langer kernel counts zeros with multiplicity, but its finite compressions require values of `xi` on vertical lines rather than a finite prime sum.  The positive-index dual which made the Gabor method work had no clear analogue there.

Repository lesson:

> Prefer the source/carry systems in which every finite block is exactly arithmetic and prime/source computable.  A beautiful off-centre signature representation is not progress if its useful inertia cannot be evaluated from the source side.

## 8. Failure: more scalar windows do not automatically create information

The transcript's optimal-window sibling solved the scalar variational problem; the successful constant is already an extremal one for the available two-trace information.  Concurrent PR #358 strengthens this lesson by proving a co-lattice multiwindow collapse in the same architecture.

Repository lesson:

> Do not proliferate Q4 scalar filters once they are only different views of the same finite carrier.  The useful state dimension is already two; improvement must come from source coupling or a new invariant, not another uncoupled taper.

## 9. The campaign's most transferable research protocol

The transcript repeatedly used:

1. an explicit do-not-repeat ledger;
2. RH-false model worlds / synthetic off-line configurations;
3. blind referees assigned different joints;
4. re-derivation of the prime/source side without reading the candidate proof;
5. exact separation between theorem, finite numerical evidence, and conjectural application;
6. preserving a failed route when its **dual** may point in the useful direction.

This is worth copying directly into the Riemann repository's integration process.

## 10. Concrete consequences already banked on PR #357

The transcript changed the Q4 attack in four concrete ways:

```text
full polarized PSD
    -> pay only negative spectral mass              L-90301;

generic 2x2 matrix
    -> one Wronskian / square-vs-reserve scalar      L-90302/L-90303;

row defect
    -> complete block defect without amplification   L-90304/L-90305;

moving-filter / metric mismatch
    -> fixed odd-Jordan all-pass source dictionary   L-90307;
```

It also forced two important negative results:

```text
source-blind all-pass contraction of off-line pairs  FALSE, R-90301;
small inertia defect => small RH current              FALSE, R-90302.
```

The endpoint/cut collars in the common metric are now polynomial forcing by `L-90308`.

## 11. The honest remaining theorem

After these repairs, the hard theorem is not matrix positivity, collar control, or state dimension.  It is a **positive-mass transport** statement for the RH-sensitive innovation.

At row scale the exact normalized recurrence is already

\[
U(4n,4j)
=\frac12U(n,j)+\frac{I_\circ(n,j)}{2\sqrt n},
\]

so it is enough to prove a block estimate of the shape

\[
\frac1n\int_{\text{balanced block}}|I_\circ|^2
\le \operatorname{poly}(\log n)
\]

or an equivalent source/state identity that yields it with coefficient one after the all-pass telescope.

`R-90302` shows that this estimate cannot be extracted from the negative eigenvalue alone: the matrix becomes positive as the current grows.  Therefore any successful final step must transport or cap the **positive** current mass through an exact source identity.

That is the correct target for the next attack.