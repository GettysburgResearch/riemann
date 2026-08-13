# R-91303 — Positive one-prime endpoint renewals do not tensorize across distinct rough primes

Claim ID: `R-91303`  
Status: **EXACT COUNTEREXAMPLE / SCOPE CORRECTION**  
Created: 2026-08-12  
Depends on: `L-91325`  
RH status: **unproved**

## 1. The valid one-prime theorem

`L-91325` proves that for every integer `R>=64`,

\[
 \eta_R(x):=\varrho(x)-\varrho(x/R)>0
 \qquad(x\ge R),
\]

where

\[
 \varrho(x)=
 \frac{2\lfloor x\rfloor}{\sqrt x}
 -\sum_{k\le x}k^{-1/2}.
\]

Consequently the endpoint port has a positive geometric renewal along repeated
powers of one fixed rough scale.

## 2. The tempting tensorization

For distinct scales `R,S`, one might try to use the mixed detail

\[
 \eta_{R,S}(x)
 =\varrho(x)-\varrho(x/R)-\varrho(x/S)+\varrho(x/(RS))
\tag{R-91303.1}
\]

as a positive joint port block. Positivity of each one-prime detail does not
imply positivity of this second mixed difference.

## 3. Exact counterexample

Take

\[
 R=67,
 \qquad
 S=71,
 \qquad
 x=4690.
\]

Then

\[
 \left\lfloor\frac{x}{67}\right\rfloor=70,
 \qquad
 \left\lfloor\frac{x}{71}\right\rfloor=66,
 \qquad
 \frac{x}{67\cdot71}<1.
\]

The directed exact checker evaluates every inverse square root with rational
lower and upper enclosures of denominator `10^70`. It proves

\[
 \boxed{
 \eta_{67,71}(4690)<-1.33<0.
 }
\tag{R-91303.2}

The retained interval is approximately

\[
 -1.339566780300142
 <\eta_{67,71}(4690)
 <-1.339566780300140.
\]

No floating sign decision is used.

## 4. Consequence

The following inference is false:

```text
positive endpoint detail for every individual rough prime
    -> positive independent product decomposition over all rough primes.
```

Repeated powers of one fixed prime are governed by the positive geometric
renewal of `L-91325`. Distinct-prime composition must instead retain the coupled
positive state or matrix port, such as the three-state dilation of `L-91323` and
the Schur port of `L-91316/L-91320`.

In particular, least-prime source labels prevent source duplication but do not,
by themselves, prove that scalar endpoint-port pieces assigned to distinct
branches are disjoint.

## 5. Correct frontier

```text
one-prime endpoint-port renewal                     EXACT / POSITIVE
same-prime geometric powers                         EXACT / CONSERVATIVE
two-prime scalar mixed detail                        NEGATIVE AT (67,71,4690)
scalar tensor-product rough port                     REFUTED
distinct-prime matrix/three-state colligation        OPEN
positive ordinary color erasure of assigned ports   EXACT (`L-91324`)
all-generation conservative port ledger              OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVEN
```
