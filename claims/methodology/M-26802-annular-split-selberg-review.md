# M-26802 — Review protocol for the annular split-Selberg attack

Claim ID: `M-26802`  
Status: **FAIL-CLOSED ADVERSARIAL REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Scope: review of `L-26802`, `L-26803`, and `T-26802`; no RH claim

## 1. Freeze

Record the exact review heads before checking any mutable branch:

```text
PR #241  independent-frequency physical block
PR #263  parity frame and finite synthesis
PR #268  annular split-Selberg continuation
PR #269  factor-five carry source and reserve
```

A later repair does not verify the frozen object.

## 2. Exact replay order

1. Verify
   \[
   \mathbf1*\omega_2
   =\varepsilon-\frac32\delta_2+\frac12\delta_4.
   \]
2. Verify the compact floor source \(g_m\).
3. Verify the physical cell formula
   \(Q_x(t)=e^{-t/2}F_x(r)\).
4. Verify the additive split intertwiner.
5. Verify the annular support \([M,8M)\).
6. Verify the oversupport row \(N=16M-1\).
7. Verify the weighted isometry (L-26802.16).
8. Verify the generalized-prime specialization.
9. Verify the generalized Selberg identity.
10. Verify the positive proper-divisor formula and half-scale route.

## 3. Production ASSD review

A claimed recurrence must export, in one metric:

```text
complete parity source fibers;
finite Bezout synthesis;
two-frequency physical matrices;
annular source maps;
weighted carry split matrices;
transition cells 2/3/4;
finite boundary matrices;
proper-divisor lower-block destinations;
digital atoms;
reserve and charge totals.
```

Reviewers must calculate the final reserve after every Schur complement. A
positive current block and positive lower blocks do not imply strict
contraction.

## 4. Mandatory mutations

The checker or proof audit must reject:

1. changing the outer wavelet coefficient \(-1/2\);
2. using oversupport \(8M-1\) instead of \(16M-1\);
3. omitting the factor \(e^{-t/2}\);
4. omitting the coefficient \(m^{-1/2}\) in the physical source;
5. summing both halves of the carry row with the lower-half weight;
6. omitting quotient cell \(4\);
7. replacing the two-frequency normal block by a diagonal integral;
8. dropping a parity channel or one Bezout delay;
9. deleting the proper-divisor defect;
10. routing \(d=n\) as a lower-scale term;
11. taking absolute values before odd-core recombination;
12. using a finite numerical reserve as the uniform ASSD theorem.

## 5. Acceptance boundary

Classify separately:

```text
L-26802 exact source map and isometry
L-26803 positive lower-scale defect
factor-five imported sign theorem
carry Schur reserve
parity frame
ASSD source assembly
ASSD strict charge/reserve inequality
ASSD -> RH composition
```

The first five may pass while ASSD remains blocked. A repair to ASSD cannot
retroactively verify a flawed exact identity.

## 6. Decisive outcome

Acceptance requires a source-bound derivation of

\[
 \kappa_0E_{r,c}+Q_{r,c}
 \le C(1+r)^A+\sum_{\ell,d}\theta_{\ell,c,d}E_{r-\ell,d},
 \qquad
 \sup_c\sum_{\ell,d}\theta_{\ell,c,d}<\kappa_0.
\]

Rejection requires one exact missing current-scale term, wrong orientation,
unrouted boundary, or charge total at least the reserve.

Until that inequality is proved, RH remains unproved.
