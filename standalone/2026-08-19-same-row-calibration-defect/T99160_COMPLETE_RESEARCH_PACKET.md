# T99160 — Same-row calibration defect: overthinning no-go and augmented resolvent

Status: **binding compositional correction; RH unproved**  
Base: PR #631 at `fe265f3a09f7511a8be5fba7d83348b8d269b8bf`  
Parent resolvent: PR #628 at `1c21389c7442f81b6bd99649e08177eebc667abc`  
Parent candidate: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`

## 1. The monotonicity-of-constructions firewall

Let `D_X` be one nonnegative physical row and let `O_X` be one positive
omission. Suppose the constant thinning asserted in `L-99023` is

\[
\tau_X^{(0)}=
\frac{\sqrt K}{\sqrt K+24},
\qquad
K=\lfloor X/67\rfloor+1,
\]

and suppose the same row also has the equality-frame score asserted in
`L-99022/L-99120`:

\[
\mathcal H(D_X)=4\sqrt X,
\qquad
\mathcal H(O_X)=O(1).
\]

Then

\[
\widetilde d_X=	au_X^{(0)}(D_X-O_X)
\]

is the row produced by the constant-thinning composition. Since

\[
4\sqrt X(1-\tau_X^{(0)})<96\sqrt{67},
\]

it satisfies

\[
\mathcal H(\widetilde d_X)\ge4\sqrt X-O(1).
\tag{1}
\]

If the ordinary/detail feasibility and endpoint consumer of PR #620 also
hold, that consumer implies RH. Under RH, however,

\[
P_\Lambda(X)=4\sqrt X-\kappa\log X+O(1),
\qquad
\kappa=\frac{\zeta'}{\zeta}(1/2)>0,
\]

while feasibility gives

\[
\mathcal H(\widetilde d_X)\le P_\Lambda(X).
\]

This contradicts (1).

Now choose any stronger thinning

\[
0<\tau_X^{(1)}<\tau_X^{(0)}
\]

and report only

\[
d_X^{(1)}=\tau_X^{(1)}(D_X-O_X).
\]

The row `d_X^(1)` may have the desired logarithmic loss, but its existence does
not destroy the already-constructed row `widetilde d_X`. Therefore:

\[
\boxed{
\text{voluntary extra thinning cannot repair an inherited stronger feasible row.}
}
\tag{2}
\]

Consequently PR #631 cannot be a complete repair while the constant-thinning
same-row claim of PR #620 remains in force. At least one of the following must
be withdrawn or replaced:

```text
exact equality score on the physical row;
constant-thinning all-column feasibility on that same row;
same-row identification across score and capacity;
the endpoint consumer.
```

The safe-point computation in PR #631 remains a valuable falsifier: it proves
that a mandatory logarithmic loss must appear somewhere. It does not show that
an optional extra thinning is where that loss actually occurs.

## 2. The exact missing interface in the published chain

The symbols used by the current candidate are not yet connected by one proved
same-row identity:

1. `L-99022.1` defines a positive direct-integral **current** row and defines
   aggregate children separately.
2. `L-99022.3` states the score of a continuum equality row denoted
   `D_X^eq`.
3. `L-99023` proves a discrepancy estimate for the row entering the native
   column calculation.
4. `L-99120` obtains exact score inheritance only after assuming

   \[
   E_X=J_X+E_XT_X
   \]

   in the actual physical row space.

No primitive calculation currently identifies all four objects without a
residual term. The constant-deficit contradiction proves that such a residual
cannot simply be zero if the remaining arrows are correct.

The correct review question is therefore not “how much extra thinning should
we voluntarily apply?” It is:

\[
\boxed{
\text{what is the mandatory source-prescribed defect between the continuum
 equality row and the finite feasible physical row?}
}
\]

## 3. Augmented nilpotent defect resolvent

Let `S_X` be the finite labelled source space and `R_X` the actual physical-row
space. Let

\[
T_X:S_X\to S_X
\]

be the positive child operator, nilpotent at fixed `X`, and let

\[
J_X,E_X,C_X:S_X\to R_X.
\]

Assume:

- `J_X` is the positive current map;
- `E_X` is the continuum equality-row map;
- `C_X` is a primitive, source-prescribed calibration-defect map;
- the exact local identity is

\[
\boxed{
E_X=J_X+E_XT_X+C_X.
}
\tag{3}
\]

The sign of `C_X` as a row need not be prescribed, but it must be constructed
without using the unknown completed sign or score.

Since `T_X` is nilpotent,

\[
R_X^{\rm src}:=(I-T_X)^{-1}
=I+T_X+\cdots+T_X^{L_X}
\]

is a finite polynomial. Rearranging (3) gives

\[
E_X(I-T_X)=J_X+C_X,
\]

hence

\[
E_X=(J_X+C_X)R_X^{\rm src}.
\]

For a positive root source `s_X`, define

\[
D_X:=J_XR_X^{\rm src}s_X\ge0,
\qquad
\mathfrak C_X:=C_XR_X^{\rm src}s_X.
\]

Then the complete same-row identity is

\[
\boxed{
E_Xs_X=D_X+\mathfrak C_X.
}
\tag{4}
\]

For every linear physical-row functional `ell`,

\[
\boxed{
\ell(D_X)=\ell(E_Xs_X)-\ell(\mathfrak C_X).
}
\tag{5}
\]

In particular, if the equality frame has score `4sqrt(X)`, then

\[
\boxed{
\mathcal H(D_X)=4\sqrt X-\mathcal H(\mathfrak C_X).
}
\tag{6}
\]

This is the exact place where a mandatory logarithmic calibration may occur.
Unlike voluntary thinning, a nonzero `mathfrak C_X` removes the stronger row
from the theorem itself.

## 4. The corrected closure contract

A repaired direct-integral proof must establish one theorem, here called
`SCDR99160`:

1. construct `C_X` directly from the finite/continuum, anchored, terminal and
   source-ownership data;
2. prove the local identity (3) in every actual component-row coordinate;
3. prove that the positive row `D_X=J_X(I-T_X)^(-1)s_X` is exactly the row used
   for every ordinary `q`, ordinary `4q`, detail and score calculation;
4. prove

   \[
   0\le\mathcal H(\mathfrak C_X)\le C\log X;
   \]

5. prove all-column feasibility for `D_X` after only the losses explicitly
   included in `C_X`, one positive omission, and any independently necessary
   thinning;
6. retain one-use provenance under the finite resolvent.

Then

\[
\mathcal H(d_X)\ge4\sqrt X-O(\log X),
\]

and the existing endpoint argument would give

\[
J_\Lambda(X)-\mathcal H(d_X)=O(\log X)=o(\log^2X).
\]

The conditional RH safe-point expansion supplies a consistency audit:
whenever the endpoint consumer is correct, the total mandatory loss of every
feasible construction must satisfy

\[
4\sqrt X-\mathcal H(d_X)
\ge\kappa\log X-O(1).
\tag{7}
\]

Equation (7) is not used as an RH input. It is a fail-closed diagnostic for the
source-side accounting.

## 5. Local stress tests that survive

The new exact replay independently retains two local facts:

- the compact Hall prefix at the worst discovered threshold satisfies

  \[
  H_{13}(67)>0.3593176602>7/20;
  \]

- the abstract nilpotent resolvent and its augmented-defect identity are exact
  in a nontrivial rational matrix fixture.

Thus this pass does not reject the compact Hall margin or the abstract
resolvent. It rejects only the composition that simultaneously uses zero
calibration defect, constant-thinning feasibility, and the endpoint consumer
on one physical row.

## 6. Exact status

```text
compact Hall worst-prefix fixture             survives exact stress test
abstract nilpotent two-sort resolvent          survives exact stress test
constant-deficit same-row composition          impossible
voluntary logarithmic overthinning             not a logical repair
augmented source-calibration resolvent          proved exact
same-row defect theorem SCDR99160               open / conclusion-producing
PR #631 “complete on frozen inputs” status     withdrawn
Riemann Hypothesis                              unproved
```
