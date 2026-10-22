# M-26801 — Final review protocol for the factor-five bottom-charge proposal

Claim ID: `M-26801`  
Title: Freeze, replay, and attempt to construct the physical bottom-charge identity without importing an equivalent sign assertion  
Status: **FAIL-CLOSED ADVERSARIAL REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `T-26801`, `R-26801`; PRs #241, #263, #268, #269  
Scope: final review packet; no RH claim

## 1. Freeze the exact heads

Record before review:

```text
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
PR #263  73e24368b62f32f31e10691ebbaf3764b544f2a3
PR #268  branch head at review start
PR #269  51ce086be09be6849c89aa69e22fcff2665b0c03
PR #271  9f5ac31cb975fd95a46eabf5af0b648e7c6bd126
PR #274  efec844e014dd716ef7822f1d368ea204e316faf
```

Do not replace a failed frozen identity by a later repair and call the original
verified.

## 2. Replay the exact source algebra

Run

```bash
python experiments/X-26201-dyadic-parity-dipole/verify.py
python experiments/X-26202-bottom-charge/verify.py
```

Require the retained verdicts

```text
EXACT_DYADIC_PARITY_DIPOLE_ALGEBRA_VERIFIED
EXACT_BOTTOM_TWO_CARRY_CHARGE_ALGEBRA_VERIFIED
```

Independently verify:

1. all four `2`-adic source layers;
2. the positive inverse coefficients;
3. the generalized von Mangoldt sequence;
4. the digital three-atom convolution;
5. the compact carry image `(-5/6,-1/2,0,...)`;
6. the formal identity
   \[
   5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X).
   \]

Every mutation deleting or changing one sibling must fail.

## 3. Audit the Mellin/Landau consumer

Starting from the finite Riesz mean, rederive

\[
 \int_1^\infty\mathcal R_\omega(X)X^{-z-1}dX
 =
 \frac{
  (1-2^{-z-1/2})(1-2^{-z-3/2})/\zeta(z+1/2)-1
 }{z^2}.
\]

Check:

- the inclusion or exclusion of the `n=1` term;
- the factor `z^-2`;
- the shift by `1/2`;
- subtraction of a finite initial interval before applying Landau;
- the exact one-sign version of Landau's theorem;
- zero safety of both Euler factors;
- multiple-zero poles;
- the final use of functional-equation symmetry.

Return one of:

```text
VERIFIED_BCP_TO_RH
VERIFIED_WITH_MELLIN_NORMALIZATION_FIXES
REJECTED_LANDAU_HYPOTHESIS_MISMATCH
```

## 4. Replay the factor-five carry programme

On PR #269, verify in this order:

1. scaled two-contact box identity;
2. pointwise opposite-parity wavelet;
3. inner and outer sign bands;
4. far-field formula and monotonicity;
5. factor-five localization `2m<=n<5m`;
6. the long constant-source run;
7. the `1/60,000,000` carry Schur reserve;
8. positive inverse synthesis of the actual generalized-prime profile;
9. the `O(log n/n)` digital correction.

The result is a carry-space theorem only.

## 5. Reconstruct the physical source

Use PR #241's independent frequencies `t,s`. For the complete source, emit:

```text
all source coefficients
all inverse coefficients
all generalized-prime coefficients
all inner-inner terms
all outer-outer terms
all inner-outer terms
block kernel Phi_(J,alpha)(t-s)
normal-Gram orientation
all quotient-cell and endpoint labels
```

The diagonal specialization `s=t` is not a physical unit block and must be
rejected as a replacement.

PR #263's parity pair must be inserted with both source polynomials, the exact
positive Bezout coefficients, and every finite shift. Reconstruction alone is
not a sign proof.

## 6. The load-bearing review object

The reviewer must either construct or refute the identity

\[
 B_X
 =\mathfrak N_{2,X}+\mathfrak N_{3,X}+\mathfrak N_{4,X}
  +\mathfrak D_X+\mathfrak O_X,
 \tag{M-26801.1}
\]

with all five terms explicitly defined and

\[
 \mathfrak N_{r,X}\ge0,
 \qquad
 \mathfrak D_X\ge0,
 \qquad
 \mathfrak O_X\ge0.
 \tag{M-26801.2}
\]

A valid proof must expose a finite physical-to-carry operator. It is not enough
to note that both sides are positive Grams in different spaces.

For every quotient row, the checker must record:

```text
physical source fiber
carry feature vector
intertwining matrix
direction of the quadratic inequality
Schur remainder
boundary destination
bottom-charge coefficient
```

## 7. Mandatory mutations

The following must break the proposed F5PBT identity:

1. `mu -> |mu|`;
2. delete the `4`-dilate sibling;
3. change `-3/2` to `-1`;
4. omit one parity source from PR #263;
5. drop one reflected cross term;
6. replace the physical block by a one-frequency integral;
7. identify carry and physical Grams without an operator;
8. discard quotient cell `4`;
9. take norms before positive inverse synthesis;
10. omit one of the digital atoms `1,2,4`;
11. route high-index transport without the bottom charges;
12. independently widen a shared transcendental input;
13. infer the sign from finite numerical positivity.

## 8. Status classifications

Review each component separately:

```text
A. source and carry algebra
B. positive inverse / generalized-prime algebra
C. bottom-charge formal identity
D. Mellin/Landau conditional consumer
E. factor-five carry localization
F. carry Schur reserve
G. parity-paired physical source frame
H. physical-to-carry transference
I. digital and outer boundary signs
J. complete RH composition
```

Use:

```text
VERIFIED
VERIFIED WITH FIXES
GAP/BLOCKED
REJECTED
```

A failure of `H` or `I` leaves the proposal `GAP/BLOCKED`; it does not refute
the exact source algebra in `A`--`G`.

## 9. Acceptance boundary

The proposal is a completed RH proof only if the reviewer verifies:

1. BCP-to-RH;
2. the exact identity (M-26801.1);
3. nonnegativity of every emitted term;
4. complete source and endpoint coverage.

Until then the correct status is

```text
FULL CONDITIONAL PROPOSAL
ONE EXPLICIT PHYSICAL TRANSFERENCE IDENTITY OPEN
RH UNPROVED
```
