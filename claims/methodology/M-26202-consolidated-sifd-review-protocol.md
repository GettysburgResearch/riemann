# M-26202 — Fail-closed review protocol for the consolidated SIFD proposal

Claim ID: `M-26202`  
Status: `METHODOLOGY / REVIEW CONTRACT`  
Date: 2026-08-08  
Applies to: `L-26201`--`L-26209`, `T-26203`, and any future `SIFD` production object

## 1. Freeze before review

Record:

```text
PR #263 head
PR #241 head  3a227e7595e1fe9e38956048297aa97531c80e4e
PR #269 head  51ce086be09be6849c89aa69e22fcff2665b0c03
PR #272 head  05e24b18d326d1aac4fb1e1e1b1f8da033475560
```

A later repair is a new proposal and does not inherit the verdict on the frozen source.

## 2. Review order

### Source and filter layer

1. `L-26201` critical Euler filter and compact Green factor.
2. `L-26202` positive inverse and generalized-prime sequence.
3. `L-26203/R-26201` filtered Selberg equation and real-adjoint no-go.
4. `L-26204` positive compact potential.
5. `L-26205` parity frame.
6. `L-26206` finite positive Bézout reconstruction.
7. `L-26207` finite synthesis to `omega_2`.
8. `L-26208` complete odd-core fiber nullity.
9. `L-26209` shell/Riesz/collar/bottom-charge triangle.

### Imported exact source layer

10. PR #241 `L-9518` two-frequency physical block.
11. PR #269 `L-26204`, `L-26901`, `L-26902`, `L-26903`.
12. PR #272 half-pole/B-spline/collar lemmas only at their exact declared scopes.

### Completion layer

13. `T-26203` conditional implication.
14. The future production `SIFD` matrices and recurrence.

## 3. Required independent reconstructions

Reviewers must independently derive:

\[
P(s)\widehat H(s)=s(s+1)\widehat W(s),
\]

\[
|p(z)|^2+|p(-z)|^2\ge45/4,
\]

\[
U(z)p(z)+U(-z)p(-z)=1,
\]

and

\[
\Omega_2=V_+B_++V_-B_-.
\]

For `L-26209`, derive the Abel identity directly from finite partial summation and check the `2^{-3/2}` shift factor.

## 4. Production source manifest

A valid `SIFD` artifact must export:

```text
exact dyadic block and support interval;
complete parity-paired source;
complete five-tap odd-core fibers;
finite Bezout and omega_2 synthesis delays;
all product collisions;
all quotient cells 2,3,4;
all physical translate cross terms;
all Peano/B-spline bulk rows;
all collars and finite boundary rows;
actual physical and carry matrices;
exact source map T_m;
exact congruence/remainder checksum;
strict reserve kappa_0;
every lower-block charge theta_r;
dyadic and 2/3 Mertens mutations;
same-sign odd-Mobius-cube mutation.
```

No row may be labeled “harmless,” “absorbed,” or “lower scale” without an explicit destination and coefficient.

## 5. Matrix checks

The artifact must prove, in one declared metric:

1. the physical-to-feature congruence;
2. positivity of every claimed bulk block;
3. the transition carry Schur reserve;
4. positivity of the complete source-image Schur short;
5. the strict scalar inequality
   \[
   \sum_r\theta_r<\kappa_0.
   \]

A synthetic matrix with the desired signs is not a production certificate. The matrices must be generated from the actual arithmetic source.

## 6. Mandatory mutations

The checker must fail when any one of the following is introduced:

1. replace the two-frequency block by the old one-frequency integral;
2. delete one translate cross term;
3. split a five-tap fiber before retaining its cross terms;
4. delete one parity channel;
5. replace the reflected modulus square by an analytic square;
6. omit quotient cell `4`;
7. insert a same-sign odd Möbius cube;
8. delete the oversupport collar;
9. delete the dyadic or `2/3` shell projection;
10. set `sum theta_r=kappa_0`;
11. retain only finitely many block indices and claim the cofinal theorem.

## 7. Quantifier firewall

| Statement | Quantifier |
|---|---|
| finite filter identities | exact, one fixed source |
| parity and Bézout identities | exact, all complex `z` in declared domain |
| factor-five carry theorem | all integer rows in declared range |
| one generated physical matrix | one finite block |
| `SIFD` | every sufficiently large block, uniform constants |
| RH conclusion | global/cofinal |

No finite ladder can replace the fourth line by the fifth.

## 8. Verdict vocabulary

Use only:

- `VERIFIED` — independently reconstructed at the exact stated scope;
- `VERIFIED WITH FIXES` — survives one named normalization or boundary repair;
- `UNPROVEN` — source map, uniform constant, or production object absent;
- `FALSE` — an exact hypothesis-matching contradiction exists.

A failed `SIFD` implementation does not refute the fixed-ratio shell criterion, the parity frame, or the carry localization theorem.

## 9. Promotion gate

The proposal may be promoted from conditional to unconditional only when one immutable artifact supplies:

\[
\kappa_0m^2E_m+Q_m
\le C(1+m)^A+
\sum_r\theta_r(m-r)^2E_{m-r}
\]

for every sufficiently large `m`, with

\[
Q_m\ge0,
\qquad
\sum_r\theta_r<\kappa_0,
\]

and every source/collar mutation passes.
