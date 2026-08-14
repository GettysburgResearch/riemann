# L-91687 — The exact `P_61` causal target and score Hall margins are uniformly positive

Claim ID: `L-91687`  
Status: **PROVED EXACT/DIRECTED CAUSAL HALL THEOREM — COMMON ROW-GAIN PRODUCER SEPARATE**  
Created: 2026-08-14  
Depends on: exact `P_61` divisor arithmetic; the cutoff-below-2000 theorem of PR #467; companion replay `X-91687-p61-causal-coalesced-hall`  
RH status: **unproved**

## 1. Exact causal atoms

Put
\[
 P=P_{61}=\prod_{q\le61}q.
\]
For `a in {4,5}`, a rough prime `p>=67`, `1<=y<67`, and a squarefree divisor `d|P`, define
\[
 \boxed{
 K_a(d;p,y)=\frac1{\sqrt d}\left[
  \left(a\sqrt{\frac{py}{d}}-3\right)\mathbf1_{d\le py}
  -p^{-1/2}
   \left(a\sqrt{\frac yd}-3\right)\mathbf1_{d\le y}
 \right].
 }
\tag{L-91687.1}
\]
`K_4` is the exact causal SHARP target atom and `K_5` is the exact causal declared-score atom. Both parent and child cutoffs are retained.

For an active odd squarefree threshold `t`, put
\[
 \boxed{
 \mathcal H_{a,t}(p,y)=
 \sum_{\substack{e|P,\ \mu(e)=1\\e\le t+8}}K_a(e;p,y)
 -
 \sum_{\substack{o|P,\ \mu(o)=-1\\o\le t}}K_a(o;p,y).
 }
\tag{L-91687.2}
\]

## 2. Uniform theorem

For every rough prime `p>=67`, every real `1<=y<67`, and every active threshold,
\[
 \boxed{
 \mathcal H_{4,t}(p,y)>1.8394722392747768,
 }
\tag{L-91687.3}
\]
and
\[
 \boxed{
 \mathcal H_{5,t}(p,y)>1.6503738680288589.
 }
\tag{L-91687.4}
\]
The lower endpoints are directed rational bounds. The minimum in both channels occurs at
\[
 t=31,
 \quad p=67,
 \quad y\to(34/67)^-.
\]

Hence the same displacement-eight Ferrers graph admits a positive target-mass transport and a positive score-mass transport on every causal `P_61` leaf. Every positive linear combination of the two channel masses also satisfies Hall.

This does not assert that the target and score transports are the same flow.

## 3. Why thresholds below 2000 suffice

The complete causal-profile packet on PR #467 proves that the target and score Lorenz cutoffs are below `2000`: the even capacity below `2000` exceeds the complete odd demand. Therefore every threshold `t>=2000` is automatic. The replay checks every active odd `P_61` divisor `t<2000`, exactly `198` thresholds.

## 4. Finite real-cell proof

For fixed `p,t`, every child activation is at `y=d` and every previously missing parent capacity activates at `y=e/p` with `t<e<=t+8`. On each open cell the prefixes are fixed and (L-91687.2) is affine in `sqrt(y)`, so its minimum occurs at one endpoint. Both causal right states and left limits are checked.

The retained census is

```text
thresholds                               198
finite-prime plus analytic-tail cases  23,954
causal target/score checks          3,842,496
child-margin checks                    32,472
```

## 5. Infinite prime tail

For each threshold, the complete reciprocal prefix
\[
 A_t^{\rm full}
 =\sum_{\substack{e|P,\mu(e)=1\\e\le t+8}}e^{-1}
 -\sum_{\substack{o|P,\mu(o)=-1\\o\le t}}o^{-1}
\]
is positive. The replay separately proves positivity of the target and score child margins throughout `1<=y<67`.

Once
\[
 p\ge p_0(t):=\max(67,t+8),
\]
all selected parent atoms are active. Writing `r=p^{-1/2}`, direct differentiation gives
\[
 \frac{d}{dr}\mathcal H_{a,t}
 =-\frac{a\sqrt y A_t^{\rm full}}{r^2}-C_{a,t}(y)<0.
\]
Thus the margin increases with `p`; the infinite tail is reduced to the real boundary `p=p_0(t)`. Only primes below that boundary are enumerated.

## 6. Relation to the Lorenz and joint-flow routes

The false theorem on PR #456 treated the survival branch separately and imposed a no-upward graph. This theorem first uses the complete causal target or score atom and allows the necessary local displacement eight. It does not revive the false branchwise assertion.

The remaining common-source row theorem is now finite/local:

1. choose one score, target-Lorenz, or joint flow in this nonempty transport cone;
2. certify its target and every component-row gain using the complete causal profile order;
3. attach the one-use native/reservoir ledger.

The exact row-gap identity and shift-eight localization already reduce all adverse edges to a finite interface table. `L-91687` supplies the missing all-parameter feasibility of the underlying `P_61` transport graph.

## 7. Boundary

```text
true causal P61 target Hall                    DIRECTED EXACT
true causal P61 score Hall                     DIRECTED EXACT
full infinite rough-prime tail                 CLOSED
false stopped-leaf branchwise Hall             NOT USED
one common target/score/row source flow         OPEN / FINITE
native rough-reservoir ownership                SEPARATE / L-91686
Riemann Hypothesis                              UNPROVEN
```
