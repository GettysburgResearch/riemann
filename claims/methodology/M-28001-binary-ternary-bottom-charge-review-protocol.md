# M-28001 — Adversarial review protocol for the binary–ternary bottom-charge route

Claim ID: `M-28001`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08

## Frozen objects

Review the proposal at one exact commit.  Record separately:

```text
parent PR #277 head
the continuation head
PR #241 two-frequency source head
any imported factor-five source head
square-screw/Landau consumer head
```

A later repair is a new proposal.

## Review order

1. `R-28001-fixed-abel-producer-positivity-fails.md`.
2. `X-28001-binary-ternary-source/verify.py`.
3. `L-28001-dyadic-bottom-charge-collapse-of-binary-ternary-producer.md`.
4. `L-28002-binary-ternary-euler-source-and-factor-eighteen-localization.md`.
5. `T-28001-binary-ternary-euler-boundary-full-rh-proposal.md`.
6. `O-28001-global-bottom-charge-source-triangle.md`.
7. The full report and integration handoff.
8. Frozen dependencies `L-23810/L-23811`, PR #241, and the Landau consumer.

## Exact reconstruction obligations

### A. Abel witnesses

Regenerate, without using retained output files,

```text
S^(3)(15,520)   = -91/256;
S^(4)(15,3559)  = -84,999,795/2048.
```

Check that the producer weights, ceiling/floor conventions, central-child
multiplicity, and zero extension agree exactly with PR #279.

### B. Dyadic bottom source

Reconstruct

\[
\mathbf1*b_2=\varepsilon-\delta_2
\]

and the pointwise identity

\[
\sum_qb_2(q)\chi_{n,j}(q)
=-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
\]

Then derive, rather than merely numerically test,

\[
\sum_qb_2(q)w(q)=-2A_w(2)-A_w(3).
\]

Audit the omitted `q=1` term and the `-1` in the Laplace transform.

### C. Landau orientation

Check:

1. integer-endpoint sign controls every interval because the derivative sign is
   constant between knots;
2. the nonnegative function is `-R_2`, not `R_2`;
3. zeta has no positive-real-axis zero in the relevant interval;
4. `1-2^-rho` cannot cancel an off-line zero;
5. the positive-part version invoked in `T-28001` really supplies the claimed
   pole exclusion.

### D. Binary–ternary Euler source

Independently verify

```text
omega_(2,3)=mu*(epsilon-delta_2)*(epsilon-delta_3);
1*omega_(2,3)=epsilon-delta_2-delta_3+delta_6;
a_(2,3)(n)=(v_2(n)+1)(v_3(n)+1);
Lambda_(2,3)>=0.
```

Enumerate every source row in the factor-eighteen band.  Confirm the exact
threshold `n>=18m-2` and all rounding exceptions immediately below it.

### E. Carry reserve

Reconstruct the constant-run argument.  Count all source jumps, central-interval
points, and variance factors.  A different conservative constant is acceptable;
a missing uniform positive constant is not.

The carry reserve is not the physical reserve.  Do not promote it without the
explicit source map.

## Required production object for BTEBC

A proposed completion must export machine-readable ledgers containing:

```text
all omega_(2,3) source coefficients;
all scaled wavelet rows m<=n<18m-2;
all binary and ternary split channels;
all generalized-prime synthesis coefficients;
all independent-frequency physical matrices;
all translate and reflection cross terms;
all finite-boundary rows;
all lower-scale destinations;
the exact Schur complement;
the final R_(2,3) boundary-charge recurrence;
the b_2 and 2/3 Mertens mutations.
```

## Mandatory mutations

The checker must reject:

1. deletion of either Euler sibling;
2. changing `ceil(n/3)` to `floor(n/3)`;
3. counting a central child once instead of twice;
4. replacing the physical modulus square by an analytic square;
5. dropping one cross term in the positive synthesis;
6. claiming transition support below the exact rounding threshold;
7. setting the carry reserve equal to the physical reserve;
8. importing third-Abel positivity;
9. deleting the `q=1` correction;
10. losing the first fixed-ratio Mertens mode.

## Classification vocabulary

Use:

```text
VERIFIED
VERIFIED WITH FIXES
UNPROVEN
FALSE
```

`FALSE` requires a witness satisfying every hypothesis of the exact claim.
A missing source map or reserve is `UNPROVEN`.

## Promotion boundary

Do not promote the branch to a proof of RH until:

1. `L-28001/L-28002` are independently reconstructed;
2. a production BTEBC ledger is emitted and replayed;
3. the physical source map and strict reserve pass every mutation;
4. the bottom positive-part recurrence is proved cofinally;
5. the Landau and fixed-ratio consumers are independently normalized.
