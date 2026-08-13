# Direct Euler factor-54 score audit and physical-entropy repair

Date: 2026-08-13  
Reviewed main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Verdict: **one advertised scalar surplus is exactly false; a stronger physical component-entropy theorem repairs that interface; RH remains unproved**

## Executive finding

The direct-row proposal correctly identified an exact Euler row split, but
`L-91351` then used an invalid extension of a Hall-threshold prefix bound. At

```text
p=83,
y=1,
x=83,
```

the exact coefficient of `sqrt(83)` in residual score minus residual target is
negative. Thus the sentence “the current arithmetic residual has score larger
than target” is false.

This does not refute the direct-row architecture. It reveals that the proof was
using the wrong score. The native loss is governed by the literal entropy of
the positive component row, not by its declared source-score label.

## Exact counterexample

For `P=P_79`,

\[
 A_P(83)
 =-
 \frac{1401629533229069216211617003}
 {107254825578022430263302818471}.
\]

Hence

\[
 A_P(83)-\frac1{83}A_P(1)
 =-
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}<0.
\]

The active-demand threshold theorem in `L-91345` cannot be promoted to every
real endpoint `x>=83`.

## New repair theorem

Let

\[
 \mathcal E_P(x)=\sum_jD_P(x;j)G_j
\]

be the actual component-row entropy. Exact Möbius convolution gives

\[
 \mathcal E_P(x)
 =\sum_{ab\le x,(a,P)=1}
  \frac{\Lambda(b)}{\sqrt{ab}}
  \log\frac{x}{ab},
\]

which is coefficientwise positive.

For the one-prime residual,

\[
 \mathcal E_{P,p}(py)
 =\mathcal E_P(py)-p^{-1/2}\mathcal E_P(y),
\]

every summand remains positive. Keeping only `a=1` reduces the problem to the
von Mangoldt ramp

\[
 R(X)=\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

The formally proved estimate `psi(x)>=0.9x` for `x>=41` yields a uniform
derivative moat. It reduces the complete two-parameter corridor

```text
p>=83,
1<=y<83
```

to the single base point `(83,1)`. Nine explicit prime-power terms certify

\[
 R(83)-\frac43\sqrt{83}>rac{41}{50}.
\]

Therefore

\[
 \mathcal E_{P,p}(py)>rac43\sqrt{py}.
\]

Meanwhile positive Euler monotonicity and the fully active `P_30` block give

\[
 \mathfrak T_{Pp}(py)<\frac{16}{15}\sqrt{py},
 \qquad
 \mathfrak S_{Pp}(py)<\frac43\sqrt{py}.
\]

Thus the actual current row has favorable physical loss with the explicit
margin

\[
 \mathcal E_{P,p}(py)-\mathfrak T_{Pp}(py)
 >\frac4{15}\sqrt{py}.
\]

## Consequence for the proof DAG

The corrected direct-row score joint is

```text
exact Euler row split
    +
inherited residual-row positivity L-91346
    +
exact physical entropy formula
    +
formal Chebyshev lower bound
    ->
strictly favorable current-row physical loss.
```

The false scalar score-over-target sentence should be deleted from every full
composition. `T-91304` may use the physical theorem instead.

## Remaining review frontier

This work does not certify RH. The surviving load-bearing interfaces are:

1. independently replay `L-91346/X-91125` from its actual source branch;
2. verify the terminal `P_79` row typing and child normalization;
3. verify exact realization of all current rows `j>y`;
4. verify one-use frontier, collar and radix-four assembly;
5. verify that the exact native loss functional is additive under that assembly;
6. replay the substochastic recurrence and the final loss-to-RH consumer.

## Replay

```bash
cd experiments/X-91130-direct-euler-score-interface
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained result:

```text
PASS_DIRECT_EULER_SCORE_INTERFACE_AUDIT_AND_REPAIR
```

```text
false real-prefix scalar surplus                 REFUTED EXACTLY
literal direct-row entropy                       COMPUTED EXACTLY
positive von Mangoldt convolution                PROVED EXACTLY
uniform physical score moat                      PROPOSED COMPLETE
full factor-54 recurrence                        INDEPENDENT REVIEW REQUIRED
Riemann Hypothesis                               UNPROVEN
```
