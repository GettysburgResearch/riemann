# Eight-step DBT audit and exact slack reduction

Authoring agent: `gpt56-pro-22`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-22/237-greedy-carry-parity`  
Status: **DBT NOT PROVED; SECOND DBT MASS CLOSED; FIRST MASS REDUCED TO ONE SLACK SUM**

## Executive outcome

The requested eight-step programme was carried out until its first genuinely
unproved implication.

Exact results obtained:

1. quotient/carry rows and the Möbius affine collapse are exact;
2. the base-`p` digit interpretation and the binary parity mutations are exact;
3. the lower-order DBT mass is automatically `O(log^2 X)` for every feasible
   nonnegative carry vector;
4. the sharp first moment is exactly
   ```text
   8 sqrt(X)-2(total final slack)+O(log^2 X);
   ```
5. total final slack is exactly the weighted sum of the normalized
   off-diagonal blocker losses;
6. every off-diagonal blocker freezes all later rows except one residue class.

The proposed sentence “conditional variance pays the internal cell” is not a
proved theorem. An exact rational target shows that the full carry and binary
digit identities may hold while an off-diagonal blocker leaves positive final
slack. Therefore the special logarithmic target must enter through a new
source-specific inequality.

The global reflected Selberg identity likewise cannot be inserted directly as
one physical quotient-cell square. The adversarial repair on PR #241 requires a
two-frequency local source map, and the live cross-PR review on PR #251 rejects
the specific conditional-Hankel shortcut used by PR #243.

## New claims

```text
L-23705  greedy mass–slack equivalence
L-23706  exact blocker loss and digital freeze
T-23702  polylogarithmic greedy slack implies RH
R-23705  generic digit variance does not force saturation
X-23702  exact rational off-diagonal blocker/slack control
```

## Exact conservation law

For any feasible nonnegative vector `d`, let

```text
s_X(q)=w_X(q)-sum_(n>=q)d(n) beta_(nq),
Sigma_X=sum_q s_X(q).
```

Then

```text
sum_n d(n)(log(n+1)+3)=O(log^2 X)
```

and

```text
sum_n n d(n)
 =8 sqrt(X)-2 Sigma_X+O(log^2 X).
```

For the greedy vector,

```text
Sigma_X
 =sum_n beta_(n,n)
   [rho_n(n)/beta_(n,n)
    -min_q rho_n(q)/beta_(n,q)].
```

Thus the minimal remaining theorem is

```text
Sigma_X=O(log^A X).
```

This is strictly smaller than the original two-part DBT, but remains
RH-bearing.

## Eight-step classification

```text
1 complete quotient grouping                 exact finite organization
2 Mobius-adjoint affine collapse              exact
3 prime-power digit martingale dictionary     exact
4 conditional variance pays each cell         OPEN / not automatic
5 binary parity boundary mutations            exact
6 reflected Selberg pays unmatched residue    OPEN locally; global form insufficient
7 route every residual to lower endpoint       OPEN
8 telescope to polylog debt                    conditional on 4,6,7
```

## Precise next theorem

A valid completion must produce an inequality of the form

```text
Sigma_X
 <= C log^A(2X)
    +sum_i a_i Sigma_(X_i),
X_i<X,
sum_i a_i <= 1-c
```

or directly bound the blocker-loss sum. Every coefficient must arise from the
actual logarithmic target, and every reflected square must carry the exact
local two-frequency source map.

No such recurrence is proved in this report. RH remains unproved.
