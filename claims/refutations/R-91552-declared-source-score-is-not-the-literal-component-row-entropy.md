# R-91552 — The declared source score is not the literal entropy score of the positive component row

Claim ID: `R-91552`  
Status: **EXACT SCORE-INTERFACE REFUTATION / CANDIDATE CLOSURE DOWNGRADED**  
Created: 2026-08-13  
Depends on: `L-24501`; retained component row `L-91112.25`; `L-91339/L-91341`; `T-91551`  
RH status: **unproved**

## 1. The positive component row

For real `Y>=1`, put

\[
 h_Y(m)=m^{-1/2}\log(Y/m)\mathbf1_{m\le Y},
 \qquad
 S_Y(n)=\sum_{m\ge n}h_Y(m),
 \tag{R-91552.1}
\]

and

\[
 Q_Y(n)
 =(n+1)\Delta^2\left[\frac{S_Y(n)}{n-1}\right]
 \qquad(n\ge2).
 \tag{R-91552.2}
\]

The row is coefficientwise nonnegative.

Let

\[
 G_n=\frac1{n+1}\sum_{j=0}^n\log\binom nj
 \tag{R-91552.3}
\]

be the actual entropy score of row `n`.

## 2. Exact entropy of the component row

Apply the double-summation identity `L-24501.4` with

\[
 c_n=Q_Y(n),
 \qquad
 b_m=S_Y(m).
\]

Then

\[
\begin{aligned}
 \sum_{n\ge2}Q_Y(n)G_n
 &=\sum_{m\ge2}S_Y(m)\log\frac m{m-1}\\
 &=\sum_{q=2}^{\lfloor Y\rfloor}h_Y(q)
   \sum_{m=2}^q\log\frac m{m-1}.
\end{aligned}
\]

The inner sum telescopes to `log q`.  Therefore

\[
 \boxed{
 \mathcal E(Y)
 :=\sum_{n\ge2}Q_Y(n)G_n
 =\sum_{q=2}^{\lfloor Y\rfloor}
  \frac{\log q}{\sqrt q}\log\frac Yq.
 }
 \tag{R-91552.4}
\]

This is the literal average-binomial entropy represented by the positive row.

## 3. Exact counterexample

At `Y=2`, the only active logarithmic atom is

\[
 h_2(2)=2^{-1/2}\log1=0.
\]

Hence

\[
 Q_2(n)=0\quad(n\ge2),
 \qquad
 \boxed{\mathcal E(2)=0.}
 \tag{R-91552.5}
\]

By contrast, the source-level endpoint-score kernel used in
`L-91339/L-91343` is

\[
 W_S(Y)=5\sqrt Y-3,
\]

so

\[
 \boxed{
 W_S(2)=5\sqrt2-3>0=\mathcal E(2).
 }
 \tag{R-91552.6}
\]

Thus

\[
 \boxed{
 \mathcal E(Y)\ne W_S(Y)
 }
 \tag{R-91552.7}
\]

in general.

The same issue persists for a source atom `k`: the actual row score is

\[
 k^{-1/2}\mathcal E(x/k),
 \tag{R-91552.8}
\]

not

\[
 k^{-1/2}(5\sqrt{x/k}-3).
\]

## 4. What remains valid

This refutation does **not** affect:

```text
coefficientwise positivity of Q_Y;
component-row endpoint monotonicity;
normalized row monotonicity used by Hall;
target exactness of the binary state telescope;
positive Hall residual source decomposition;
fixed-67 target subprobability.
```

Those are target/capacity statements.

It invalidates only the inference

```text
positive source measure has declared score S
+
its component row is positive
->
the component row has entropy score S.
```

The last arrow is false.

## 5. Consequence for the candidate closure

`T-91551` used the declared source score as though it were already represented
by the physical row.  Equations (R-91552.4)--(R-91552.6) show that this interface
is not exact.  Therefore the status

```text
candidate complete factor-54 proof chain
```

must be withdrawn unless one proves either:

1. a score-realization theorem comparing `mathcal E(Y)` with the declared
   source score on every inherited/current sector; or
2. a bounded generationwise debt theorem for their difference in the exact
   native normalization.

The companion continuation `L-91553` attacks the first option.  Until that
continuation is integrated through the native loss, RH remains unproved.

```text
exact component-row entropy kernel                  PROVED
source-score = component entropy                     REFUTED
T-91551 exact native score realization               INVALID AS WRITTEN
positive target/row architecture                      RETAINED
corrected score recurrence                            OPEN
Riemann Hypothesis                                   UNPROVEN
```
