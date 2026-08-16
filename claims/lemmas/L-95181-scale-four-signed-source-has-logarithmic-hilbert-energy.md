# L-95181 — The scale-four signed channel has logarithmic Hilbert energy

Claim ID: `L-95181`  
Status: **PROPOSED COMPLETE EXACT ENERGY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95180`; `L-95051` for the contrasting absolute-cost wall  
Scope: weighted signed-channel energy; no Q4 curvature estimate

## 1. Exact dyadic energy weights

For odd squarefree `m`, write `n=2^e m`. The contribution to

\[
\sum_{n\le X}{a_4(n)^2\over g_4(n)n}
\]

is `1/m` at `e=0`, `1/(2m)` at `e=1`, and for `k>=1`,

\[
{9\over16^k m}
\quad(e=2k),
\qquad
{9\over2\cdot16^k m}
\quad(e=2k+1).
\]

The full dyadic coefficient is

\[
1+{1\over2}
+\sum_{k\ge1}{27\over2\cdot16^k}
={12\over5}.
\tag{L-95181.1}
\]

Therefore

\[
\boxed{
\sum_{n\le X}{a_4(n)^2\over g_4(n)n}
\le {12\over5}(1+\log X).
}
\tag{L-95181.2}
\]

## 2. Exact dyadic cancellation

For every odd squarefree `m` and every `k>=0`,

\[
\boxed{a_4(2\cdot4^k m)=-a_4(4^k m).}
\tag{L-95181.3}
\]

The paired Hilbert weight decays geometrically with `k`. In contrast, the positive trace weights `g_4(4^k m)/(4^k m)` are scale-neutral, producing the `Theta(sqrt X log X)` absolute majorant wall of `L-95051` in its square-root normalization.

Thus the dyadic-depth explosion is not intrinsic to the signed channel. It is created by discarding cancellation before choosing the metric.

## 3. Positive trace mass in the `1/n` geometry

In the Peano normalization used below,

\[
\sum_{n\le X}{g_4(n)\over n}=O(\log^2 X).
\tag{L-95181.4}
\]

Indeed `g_4(2^e m)/2^e` equals one on even dyadic levels and one half on odd levels. There are `O(log X)` levels, and each odd-part harmonic sum is `O(log X)`.

With one additional factor `log n`,

\[
\sum_{n\le X}{g_4(n)\log n\over n}=O(\log^3 X).
\tag{L-95181.5}
\]

These bounds are weak but unconditional and sufficient to keep the positive Peano fluxes polylogarithmic.

## 4. Boundary

```text
signed Hilbert energy O(log X)           EXACT
four-adic channel pairing                EXACT
positive 1/n trace mass O(log^2 X)       UNCONDITIONAL
positive log-flux mass O(log^3 X)        UNCONDITIONAL
critical centered-curvature map          OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```
