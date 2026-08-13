# L-91350 — Historical noncausal `P_79` low-prefix Hall certificate

Claim ID: `L-91350`  
Status: **SUPERSEDED — DISPLAY (L-91350.2) IS FALSE AS A CAUSAL PARENT IDENTITY**  
Created: 2026-08-13  
Corrected status: 2026-08-13 after review PR `#431` and `L-91354/X-91312`  
Superseded by: `L-91354-p79-low-prefix-hall-with-parent-causal-support.md`  
RH status: **unproved**

## 1. Historical purpose

This file attempted to prove every finite `P_79` one-prime target and declared
source-score Hall prefix by reducing the rough-prime parameter and checking
child activation cells.

For `a=4` or `a=5`, it correctly began with the causal kernel

\[
\begin{aligned}
 K_a(d;p,y)
 ={}&d^{-1/2}[a\sqrt{py/d}-3]\mathbf1_{d\le py}\\
 &-p^{-1/2}d^{-1/2}[a\sqrt{y/d}-3]\mathbf1_{d\le y}.
\end{aligned}
\tag{L-91350.1}
\]

The Hall margin at a sign-demand threshold `t` is

\[
 \mathcal H_{a,t}^{(8)}(p,y)
 =\sum_{\substack{e\le t+8\\\mu(e)=1}}K_a(e;p,y)
 -\sum_{\substack{o\le t\\\mu(o)=-1}}K_a(o;p,y).
 \tag{L-91350.2}
\]

## 2. Exact failure

The former proof then replaced the parent part of (L-91350.2) by the complete
formal prefixes

\[
 A_t=\sum_{e\le t+8,\mu(e)=1}\frac1e
     -\sum_{o\le t,\mu(o)=-1}\frac1o,
\]

\[
 B_t=\sum_{e\le t+8,\mu(e)=1}\frac1{\sqrt e}
     -\sum_{o\le t,\mu(o)=-1}\frac1{\sqrt o},
\]

without retaining the parent cutoff `d<=py`.

When

\[
 t\le py<t+8,
\]

some formal positive sources `e` in `(py,t+8]` are absent from the actual
parent.  Therefore the old display

\[
 a\sqrt y\left(\sqrt p\,A_t-rac{A_t(y)}{\sqrt p}\right)
 -3B_t+rac{3B_t(y)}{\sqrt p}
\]

is not equal to the causal margin (L-91350.2).

The retained `X-91127` certificate consequently proves a different, overfilled
prefix problem.  Its advertised minima and output schema are not evidence for
the causal theorem.

## 3. Correct replacement

`L-91354/X-91312` restores the exact parent prefix

\[
 A_{t,py},\qquad B_{t,py},
\]

and evaluates both sides of every missing activation `py=e`.  It proves the
stronger true bounds

\[
 \boxed{
 \mathcal H_{4,t}^{(8)}(p,y)>\frac74,
 \qquad
 \mathcal H_{5,t}^{(8)}(p,y)>\frac32
 }
\]

for every prime `p>=83`, every real `1<=y<83`, and every active sign-demand
threshold `t<4096`.

The corrected replay covers `18,180,604` directed inequalities.  Its score
minimum occurs at

\[
 t=79,
 \qquad p=83,
 \qquad y\to(85/83)^-,
\]

immediately before the omitted parent source at `py=85` activates.

## 4. Boundary

```text
historical convex-cell concern R-91308             RETAINED AS METHODOLOGY
old full-parent-prefix identity                     FALSE
old X-91127 causal Hall claim                       WITHDRAWN
correct causal target Hall margin                   PROVED / L-91354
correct causal declared-score Hall margin           PROVED / L-91354
source-labelled Hall flow export                    OPEN
live row provenance LRPT                            OPEN
Riemann Hypothesis                                  UNPROVEN
```
