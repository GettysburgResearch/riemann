# M-26802 — Review protocol for the critical annular split-Selberg attack

Claim ID: `M-26802`  
Status: **FAIL-CLOSED ADVERSARIAL REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Scope: review of `R-26802`, `L-26802`--`L-26805`, and `T-26802`; no RH claim

## 1. Freeze

Record exact heads before review:

```text
PR #241  independent-frequency physical block
PR #263  parity frame and finite synthesis
PR #268  corrected annular source-change continuation
PR #269  factor-five carry source and reserve
```

A later repair does not verify a frozen object.

## 2. Source identity must be checked first

Reviewers must distinguish:

```text
RH-sensitive physical coefficients:
    x=lambda_omega;
    carry coefficient W=omega_2*lambda_omega;

reserved carry profile on PR #269:
    P=lambda_omega;
    wavelet weights x=a_omega log.
```

Verify independently that the physical primitive for `x=a_omega log` is

\[
 [-\zeta'(s)+\zeta(s)E'(s)/E(s)]/s
\]

and is holomorphic at every zeta zero. Any proof treating that primitive as
containing reciprocal-zeta poles is rejected.

Verify the exact source change

\[
 a_\omega*W=\Lambda_\omega
\]

and its coefficientwise current-plus-proper-divisor form before reading any
energy estimate.

## 3. Exact replay order

1. Verify
   \[
   \mathbf1*\omega_2
   =\varepsilon-\frac32\delta_2+\frac12\delta_4.
   \]
2. Verify the compact floor source \(g_m\).
3. Verify the physical cell formula for arbitrary coefficients.
4. Verify the additive split intertwiner.
5. Verify the unfiltered and critically filtered support constants.
6. Verify oversupport rows \(16M-1\) and \(256M-1\).
7. Verify both weighted isometries.
8. Verify that `x=lambda_omega` yields the RH-sensitive feature `W`.
9. Verify that `x=a_omega log` yields `P` only in carry space and is pole blind
   physically.
10. Verify `a_omega*W=lambda_omega` and every proper-divisor destination.
11. Verify the generalized Selberg identity.
12. Verify the positive proper-divisor Selberg defect.

## 4. Production ASSD review

A claimed recurrence must export, in one metric:

```text
complete parity source fibers;
finite Bezout synthesis;
two-frequency physical matrices;
RH-sensitive annular source maps;
weighted carry split matrices for W;
source-change completion to P;
transition cells 2/3/4;
finite boundary matrices;
source-change and Selberg proper-divisor destinations;
digital atoms;
reserve and charge totals.
```

Reviewers must calculate the final reserve after completing the `P` square and
after every Schur complement. Positive current and lower blocks do not imply
strict contraction.

## 5. Mandatory mutations

The proof or checker must reject:

1. replacing `x=lambda_omega` by `x=a_omega log` physically;
2. silently replacing `W` by `P`;
3. deleting one source-change proper divisor;
4. treating `a_omega` as an `l1` contraction kernel;
5. taking absolute values before completing the `P` square;
6. changing the outer wavelet coefficient `-1/2`;
7. using oversupport `8M-1` or `128M-1`;
8. omitting the factor `e^(-t/2)` or `m^(-1/2)`;
9. summing both carry halves with the lower-half weight;
10. omitting quotient cell `4`;
11. replacing the two-frequency normal block by a diagonal integral;
12. dropping a parity channel or Bezout delay;
13. deleting the generalized Selberg defect;
14. routing the current divisor `d=1` to lower scale;
15. using finite numerical reserve as the uniform theorem.

## 6. Acceptance boundary

Classify separately:

```text
R-26802 source-scope correction
L-26802 arbitrary-source annular isometry
L-26804 critical filtered annular isometry
L-26805 half-scale source change
L-26803 positive Selberg lower-scale defect
factor-five imported sign theorem
P-profile carry Schur reserve
ASSD W-to-P square assembly
ASSD strict charge/reserve inequality
ASSD -> RH composition
```

The exact identities may pass while ASSD remains blocked. A proposed repair
cannot retroactively verify a wrong source specialization.

## 7. Decisive outcome

Acceptance requires a source-bound derivation of

\[
 \kappa_0E_{r,c}+Q_{r,c}
 \le C(1+r)^A+\sum_{\ell,d}\theta_{\ell,c,d}E_{r-\ell,d},
 \qquad
 \sup_c\sum_{\ell,d}\theta_{\ell,c,d}<\kappa_0.
\]

Rejection requires one missing current-scale term, wrong source, wrong
orientation, unrouted boundary, or charge total at least the reserve.

Until that inequality is proved, RH remains unproved.
