# R-91310 — The `P_79` active-threshold prefix bound does not extend to the first real one-prime splice cell

Claim ID: `R-91310`  
Status: **EXACT COUNTEREXAMPLE / DIRECT-EULER SCORE-SURPLUS CLAIM REFUTED**  
Created: 2026-08-13  
Frozen main: `d688cc7cb73eea9e50f10352a50516ab2c4f4625`  
Depends on: `L-91345`, `L-91351`, `T-91304`; exact replay `X-91310`  
RH status: **unproved and undisproved**

## 1. The domain that was proved

Put

\[
 P=P_{79}=\prod_{q\le79}q,
 \qquad
 A_P(x)=\sum_{\substack{d\mid P\\d\le x}}\frac{\mu(d)}d.
\]

`L-91345` proves a lower bound for the prefix `A_0(t)` at the declared **active odd squarefree divisor thresholds** `t`.  Its exact minimum in the stated large-threshold regime occurs at the active threshold `t=105`.

That theorem does not imply

\[
 A_P(x)>\frac1{25}
 \qquad\text{for every real }x\ge83.
 \tag{R-91310.1}
\]

The passage from an active Hall threshold `t` to an arbitrary real splice endpoint `x=py` is load-bearing in `L-91351.11` and `T-91304.5`.

## 2. Exact first-cell prefix

There are 51 squarefree divisors of `P` not exceeding `83`.  Exact common-denominator summation gives

\[
 \boxed{
 A_P(83)
 =-
 \frac{1401629533229069216211617003}
 {107254825578022430263302818471}
 <0.
 }
 \tag{R-91310.2}
\]

There is no divisor of `P` at `83` or `84`, so the same negative prefix persists throughout the first real splice cell beginning at `83` and ending before the activation at `85`.

For comparison, the intended active-threshold statement is not contradicted: the checker also verifies

\[
 A_P(105)
 =
 \frac{6955816909665487849457015781}
 {153221179397174900376146883530}
 >\frac1{25}.
 \tag{R-91310.3}
\]

## 3. Exact score-surplus counterexample

Take the admissible one-prime parameters

\[
 p=83,
 \qquad y=1,
 \qquad x=py=83.
\]

Since `A_P(1)=1`, the exact score-minus-target identity of `L-91351.10` becomes

\[
\begin{aligned}
 \mathfrak S_{Pp}(83)-\mathfrak T_{Pp}(83)
 &=\sqrt{83}\left(A_P(83)-\frac1{83}A_P(1)\right)\\
 &=-\sqrt{83}\,
 \frac{223590076836035175208867029720}
 {8902150522975861711854133933093}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 \mathfrak S_{Pp}(83)-\mathfrak T_{Pp}(83)<0.
 }
 \tag{R-91310.4}
\]

The rational coefficient is approximately `-0.02511641161975008`; after multiplication by `sqrt(83)` the score deficit is approximately `-0.2288213998`.

The exact directed radical enclosure in `X-91310` also gives

\[
 0<\mathfrak T_{Pp}(83)<1.813,
 \qquad
 \mathfrak S_{Pp}(83)<\mathfrak T_{Pp}(83).
 \tag{R-91310.5}
\]

Thus the counterexample is not a failure of residual target positivity.  It is specifically a failure of the claimed favorable score orientation.

## 4. Consequences

The following statements are false as written:

```text
L-91351.11: uniform positive score-over-target surplus;
T-91304.5:  S_(Pp)(py)-T_(Pp)(py) > (58/2075)sqrt(py);
T-91304 Section 7: the current arithmetic residual is favorable solely by that scalar inequality.
```

Accordingly, `T-91304` is **false as submitted**.  The displayed recurrence `T-91304.6` does not follow from its current score argument.

This does not refute:

```text
the exact Euler row split;
the directed inherited-row positivity theorem L-91346;
the corrected finite Hall theorem L-91350;
residual target positivity;
the possibility of a bounded score debt;
the Riemann Hypothesis.
```

## 5. Repair frontier

The scalar source score is not the literal physical entropy of the component row, as independently fenced by `R-91552`.  Therefore the correct continuation is to compute the actual component-row entropy of the direct Euler residual and compare that physical score with the target.

`L-91352` gives an exact nonnegative entropy normal form and proves that the present first-cell witness is **not** a physical-score obstruction: already the single `n=2` entropy atom exceeds the complete residual target.  The remaining RH-bearing statement is a uniform physical-score domination or bounded-debt theorem over

\[
 p\ge83,
 \qquad 1\le y<83.
\]

```text
active-threshold P79 prefix theorem              RETAINED AT ITS DECLARED DOMAIN
arbitrary-real-endpoint extension                FALSE
first-cell scalar score surplus                  FALSE EXACTLY
first-cell physical entropy obstruction          ABSENT / L-91352
corrected all-parameter physical score theorem   OPEN
Riemann Hypothesis                               UNPROVEN
```
