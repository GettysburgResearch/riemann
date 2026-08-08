# Consolidated critical-transition review packet

Date: 2026-08-08  
Agent: `gpt56-pro-09-p`  
Repository: `gfreund123/riemann`  
Review branch: `agent/gpt56-pro-09-p/230-balanced-core-continuation`  
Status: **REVIEW-READY CONDITIONAL PROPOSAL / RH UNPROVED**

## 1. Frozen dependency graph

This packet consolidates the following live research heads:

```text
PR #229  2fc74c11b9929f694d8c13d060c9d55b99dc9621
         repository-wide gap audit and first-cell decoder

PR #234  2d5043070e15fe6be94307381f4023eaa48c17a5
         fixed-ratio shell criterion and positive Gram

PR #236  a0d5a627bd2d4e799eddf7c795df77083a3618ff
         all-ratio transfer, digital recurrence, parity/carry front end

PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
         correct independent-frequency physical normal block

PR #244  1e8bfaf0d6d2985f3f1a4bb2cac53cbc93b28fe9
         fifth-shell first-zero energy barrier

PR #263  73e24368b62f32f31e10691ebbaf3764b544f2a3
         parity-paired Euler fiber and finite Bezout reconstruction

PR #268  b67f3ee4e5c20fdd23ad0923641d452c4a89da83
         bottom two-charge scalar consumer

PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
         factor-five localization and uniform carry Schur reserve

PR #257  2f508a77a21593c7a8bc852a61e8b19c63367f8b
         independent fourth-pass status and cross-route audit
```

Later branch commits in this packet do not retroactively verify any frozen
claim.  They provide scope corrections and one consolidated proposal.

## 2. What is now genuinely established or sharply reduced

### 2.1 Fixed-ratio scalar firewall

For every fixed `0<c<1`,

\[
Q_c(t)=e^{-t/2}[M(e^t)-M(ce^t)]
\]

has a zero-safe inverse-zeta transform and a finite positive balanced Gram.
All fixed ratios are connected by mutually inverse causal `ell^1` filters.  In
particular, the dyadic shell and the exact `2/3` first Farey cell have the same
upper exponential status.

### 2.2 Correct physical localization

A physical logarithmic block is represented by an independent-frequency
`(t,s)` integral with kernel `Phi_(J,alpha)(t-s)`.  A single vertical integral is
not a physical block.  Every proposal in this packet uses the repaired normal
orientation.

### 2.3 Digital and carry source algebra

The dyadic source has:

```text
an exact atomic Sobolev factorization;
positive digit-comb kernels;
a compact parity/carry dipole;
an exact lower-scale digital recurrence;
an H1-to-L2 digital tail O(log R/sqrt R);
an explicit dyadic Green path Gram and tridiagonal inverse.
```

The infinite digital tail and the complete power-of-two Green sector are no
longer open.

### 2.4 Parity-paired finite reconstruction

The paired Euler fibers have a uniform algebraic reserve and an exact finite
positive Bezout reconstruction of the inverse-zeta source.  No infinite causal
inverse is required.

### 2.5 Factor-five carry localization

For the actual opposite-parity source:

```text
all potentially negative logarithmic Kummer rows satisfy 2m<=n<5m;
all rows n>=5m are nonnegative exactly;
the generalized-prime carry profile is a positive synthesis of the same
wavelets;
a uniform absolute Schur reserve survives the digital correction.
```

Thus the carry-side sign and reserve problems are closed outside three quotient
cells.

## 3. The crucial correction discovered during consolidation

The former `PGC(R)` requested polylogarithmic inverse conditioning for the
finite digital prefix.  `R-23008` shows this is impossible.

At a zeta zero `rho=beta+i gamma`, the prefix symbol satisfies

\[
|A_R(\rho)|\ll_\rho(1+\log R)R^{-\beta}.
\]

A critical-line mode therefore requires inverse loss of order

\[
R/(\log R)^{O(1)}.
\]

The previous polylogarithmic condition would suppress legitimate line zeros.
`T-23004` is consequently superseded.

The sharp replacement is **critical-order observability**:

\[
K_R=R^{1+o(1)},
\]

modulo a separately certified tempered channel.  This scale permits all
critical-line modes but is too small for any off-line mode, which would require
`R^(2 beta-o(1))` with `2 beta>1`.

## 4. Consolidated full conditional proposal

The active proposal is `T-23005`:

```text
fixed-ratio shell and first-cell firewall
-> independent-frequency physical block
-> parity-paired finite reconstruction
-> opposite-parity factor-five source
-> quotient cells 2,3,4 only
-> generalized-prime carry Gram
-> uniform strict carry reserve
-> critical-order physical-to-carry source transference CF5TC(R)
-> no off-line pole
-> RH.
```

The exact theorem still missing is `CF5TC(R)`:

\[
\|q_H\|_{H^1(0,J)}^2
\le
R^{1+o(1)}
\left[
D_R(J)+\|\mathcal A_Rq_H\|_{L^2(0,J+C_H)}^2
\right],
\]

for an unbounded prefix sequence, every safe localization, and a fully declared
tempered channel `D_R`.

A production proof must construct the physical-to-carry map and its adjoint,
not merely quote the carry-space reserve.

## 5. Why the current packet is not an unconditional proof

The following arrow remains open:

\[
\boxed{
\text{independent-frequency physical transition matrix}
\longrightarrow
\text{generalized-prime carry transition Gram}
}
\]

with all cross terms, boundary rows, quotient cells, and collar charges retained
and with loss at most `R^(1+o(1))`.

The repository currently proves the source algebra on both sides of this arrow,
not the bounded transference itself.  Relabeling that map as obvious would hide
the same RH-bearing local-to-arithmetic conversion identified throughout the
project.

## 6. Reviewer decision surface

A reviewer can decide the proposal by answering four questions.

1. **Critical prefix scale.** Is `R-23008` correct, including the conclusion
   that the former polylogarithmic theorem is impossible?
2. **Source completeness.** Do the parity-paired and opposite-parity manifests
   contain every translated sibling and every cross term?
3. **Physical-to-carry map.** Can an exact bounded map be constructed on cells
   `2,3,4`, with loss `R^(1+o(1))` and no target energy hidden in the defect?
4. **Consumer.** Does the resulting inequality localize every hypothetical
   off-line pole, or export the exact `2/3` Mertens mutation?

A negative answer to item 3 blocks the proposal.  A complete affirmative
production object proves RH by `T-23005`.

## 7. Final classification

```text
all-ratio shell transfer                         VERIFIED / proposed complete
correct two-frequency physical block             VERIFIED at identity scope
positive digit/parity/carry identities           proposed complete
finite digital tail reduction                    proposed complete
parity-paired finite reconstruction               proposed complete
factor-five carry localization                    proposed complete
actual carry-space Schur reserve                  proposed complete
former polylog PGC(R)                             REFUTED
critical-order CF5TC(R)                           OPEN / RH-BEARING
CF5TC(R) -> RH                                    COMPLETE CONDITIONAL
Riemann Hypothesis                                UNPROVED
```

## 8. Handoff recommendation

This packet is ready for **adversarial review as a consolidated conditional RH
proposal and scope audit**.  It is not ready to be described as a completed
proof of RH.  The reviewer should begin with `R-23008`, then `T-23005`, and then
attempt the production map under `M-23002`.
