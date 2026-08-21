# L-91358 — The `P_61` score-Lorenz cutoff is uniformly below `2000`

Claim ID: `L-91358`  
Status: **PROVED EXACT FINITE-PREFIX / GLOBAL-CUTOFF STRENGTHENING — DIRECTED REPLAY PROVIDED**  
Created: 2026-08-13  
Frozen input: PR `#439` at `87c34e48b5839e81183302a4f2c48a83bb5c38a6`, especially `L-91357`  
Depends on: `L-91328`, `L-91345`, `L-91348`; replay `X-91135`  
RH status: **unproved**

## 1. Causal score atoms

Let

\[
 P_{61}=\prod_{q\le61}q,
 \qquad p\ge67,
 \qquad1\le y\le67,
 \qquad x=py,
 \qquad r=p^{-1/2}.
\]

For a squarefree divisor `d|P_61`, put

\[
 K_S(d)=W_S(x,d)-rW_S(y,d),
 \tag{L-91358.1}
\]

where

\[
 W_S(X,d)=
 \left(\frac{5\sqrt X}{d}-\frac3{\sqrt d}\right)
 \mathbf1_{d\le X}.
 \tag{L-91358.2}
\]

Let `E_S` and `O_S` be the positive even- and odd-parity score measures. The score-Lorenz projection removes a leftmost portion of `E_S` whose total mass is `|O_S|`. Its cutoff is at most a number `C` once

\[
 E_S([1,C])\ge |O_S|.
 \tag{L-91358.3}
\]

## 2. Fixed prefix at `C=2000`

Set `C=2000` and define

\[
 A_C=
 \sum_{\substack{d\mid P_{61}\\\mu(d)=1,\ d\le C}}\frac1d
 -
 \sum_{\substack{d\mid P_{61}\\\mu(d)=-1}}\frac1d
 \tag{L-91358.4}
\]

and

\[
 B_C=
 \sum_{\substack{d\mid P_{61}\\\mu(d)=1,\ d\le C}}\frac1{\sqrt d}
 -
 \sum_{\substack{d\mid P_{61}\\\mu(d)=-1,\ d\le C}}\frac1{\sqrt d}.
 \tag{L-91358.5}
\]

The exact reciprocal computation gives

\[
 \boxed{
 A_C=
 \frac{852772323997294585715}
 {23457676271881394196654}>0.
 }
 \tag{L-91358.6}
\]

The fixed-denominator radical replay proves the stronger gate

\[
 \boxed{
 5\sqrt C\,A_C-3B_C-\frac{335}{\sqrt C}
 >\frac14.
 }
 \tag{L-91358.7}
\]

The directed lower endpoint is larger than `0.287287954277`.

## 3. Parent reserve at the fixed cutoff

Assume first that `x>=C`. Every even source through `C` is active. Let

\[
 H_X^{\rm par}(C)
 =
 \sum_{\substack{e\mid P_{61}\\\mu(e)=1,\ e\le C}}W_S(x,e)
 -
 \sum_{\substack{o\mid P_{61}\\\mu(o)=-1,\ o\le x}}W_S(x,o).
 \tag{L-91358.8}
\]

For the reciprocal coefficient, replacing the active odd set by all odd divisors can only decrease the expression. For the square-root coefficient, every odd divisor at most `C` is active and every additional active odd term is favorable after the sign is expanded. Hence

\[
 \boxed{
 H_X^{\rm par}(C)
 \ge5\sqrt x\,A_C-3B_C.
 }
 \tag{L-91358.9}
\]

## 4. Uniform child subtraction

Because `y<=67<C`, the cutoff contains every active child source. The child bracket is the complete finite `P_61` endpoint-score forcing at `y`. The positive-Euler-factor upper corridor gives

\[
 0<F_S^{(61)}(y)<5\sqrt y.
 \tag{L-91358.10}
\]

Therefore

\[
 rF_S^{(61)}(y)
 <5r\sqrt y
 =\frac{5y}{\sqrt x}
 \le\frac{335}{\sqrt x}.
 \tag{L-91358.11}
\]

Combining (L-91358.9)--(L-91358.11),

\[
 \boxed{
 E_S([1,C])-|O_S|
 >5\sqrt x\,A_C-3B_C-\frac{335}{\sqrt x}.
 }
 \tag{L-91358.12}
\]

The right side is strictly increasing in `x`, since `A_C>0`. Its minimum on `x>=C` is the positive quantity in (L-91358.7). If `x<C`, every active source already lies below `C`. Thus in all cases the Lorenz cutoff is at most `C`. Since `2000` is not a squarefree divisor of `P_61`, the cutoff itself satisfies

\[
 \boxed{c_{\rm Lorenz}<2000.}
 \tag{L-91358.13}
\]

## 5. Exact finite frontier

There are exactly 184 positive-parity `P_61` divisors in `[2,2000)`. The largest is `1995`. Hence the remaining row-provenance family has only these 184 possible cutoff nodes, rather than the 425 nodes below `10000` left by `L-91357`.

The still-open family is

```text
cutoff c: 184 even P_61 divisors, 2<=c<2000;
row j:    2<=j<=66;
child y:  1<=y<=67;
rough p:  p>=67.
```

The next theorem `L-91359` removes every cutoff with `c<=y`.

## 6. Replay

```bash
cd experiments/X-91135-p61-score-lorenz-cutoff-2000
python3 verify.py
sha256sum -c SHA256SUMS
```

Retained verdict:

```text
PASS_P61_SCORE_LORENZ_CUTOFF_2000
```

The checker uses exact `Fraction` arithmetic for reciprocal sums and fixed-denominator outward radical intervals of denominator `10^60`.

## 7. Boundary

```text
fixed reciprocal prefix A_2000>0                EXACT
fixed radical prefix enclosure                   DIRECTED EXACT
reserve at C=2000 >1/4                           DIRECTED EXACT
Lorenz cutoff c<2000                             EXACT
possible cutoffs                                 184
common target/score source typing                RETAINED / L-91348
common literal-row subordination                 OPEN / LRPT
Riemann Hypothesis                               UNPROVEN
```
