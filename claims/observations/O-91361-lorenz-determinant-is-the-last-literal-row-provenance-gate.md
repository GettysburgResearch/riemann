# O-91361 — Corrected frontier after the causal-monotonicity refutation

Claim ID: `O-91361`  
Status: **CURRENT SYNTHESIS / NO RH CLAIM**  
Created: 2026-08-13  
Corrected after: `R-91311`  
RH status: **unproved**

## 1. Lorenz route correction

The historical version of this handoff treated continuous causal row-per-score ordering as closed by `L-91360`. That premise is false. `R-91311` proves that the causal profile has negative logarithmic derivative at

\[
 j=66,
 \qquad p=67,
 \qquad z=133/2.
\]

Accordingly:

```text
continuous causal row-per-score ordering       REFUTED / R-91311
discrete ordering on actual P61 divisors       OPEN
full Lorenz determinant                        OPEN
Lorenz row provenance                          NOT CLOSED
```

The abstract bathtub theorem `L-91358` remains valid whenever its order hypothesis is supplied.

## 2. Surviving exact packet route

The robust conclusions on this branch are:

```text
nonduplicating causal packet budget            L-91355
positive two-ledger map rigidity               L-91356
uniform finite Lorenz cutoff                   L-91357
single-endpoint normalized row monotonicity    L-91359
same-index multiplicative child functor        L-91361
P61 stopping-line packet decomposition         L-91362
packet-envelope reduction                      T-91307
```

The last three results replace both the Lorenz dependence and the unsafe affine child map.

## 3. Exact current gate

`L-91362` writes every paired root packet as

\[
 P_X=F_{61,X}
 +\sum_{d\mid P_{61}}
  \sum_{p\ge67}(dp)^{-1/2}P_{X/(dp)}^{(d,p)}
\]

with source-disjoint actual child packets. `L-91361` embeds every child packing by same-index scaling in all row, ordinary, radix-four and score coordinates. `T-91307` then reduces the complete route to one fixed producer theorem:

> **Complete Finite-Forcing Producer (`CFFP`).** For each of the two fixed labelled `P_61` finite-forcing packets, construct one nonnegative physical row realization with ordinary and radix-four capacities, literal entropy, terminal correction, collar and common port, and bound its local deficit by a uniform constant times packet mass.

A proof gives

\[
 \Lambda(X)\le C_{\rm fin}+\Lambda(X/67),
\]

hence `O(log X)=o(log^2 X)` endpoint loss and RH through the resident consumer.

## 4. Correct boundary

```text
parallel-parent duplication                    CLOSED
actual rough-child source disjointness         CLOSED
same-index child row/capacity embedding        CLOSED
packet-envelope recursion                      CLOSED CONDITIONAL
continuous causal Lorenz ordering              FALSE
CFFP complete finite-forcing producer          OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```
