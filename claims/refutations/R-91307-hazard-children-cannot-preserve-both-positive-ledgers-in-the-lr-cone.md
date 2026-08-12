# R-91307 — Least-prime hazard children cannot preserve both positive ledgers inside the `(L,R)` cone

Claim ID: `R-91307`  
Status: **EXACT CANONICAL-RETURN OBSTRUCTION / SCOPE CORRECTION**  
Created: 2026-08-12  
Depends on: `L-91336`, `L-91337`, `L-91338`  
RH status: **unproved**

## 1. General diagonal packet

Let a positive hidden packet multiply the two diagonal modes by

\[
 a\ge0,
 \qquad b\ge0.
\]

Starting from the canonical lift of `(L,R)`, its positive hidden target and score
ledgers are

\[
 T=aL+2bR,
 \qquad
 S=a(2L+R).
\tag{R-91307.1}

A positive physical return preserving both ledgers would require

\[
 L'+2R'=T,
 \qquad
 2L'+R'=S,
 \qquad
 L',R'\ge0.
\tag{R-91307.2}

The unique formal solution is

\[
\boxed{
 L'=aL+\frac{2(a-b)}3R,
 \qquad
 R'=\frac{4b-a}{3}R.
}
\tag{R-91307.3
}

Therefore universal positivity requires

\[
 a\ge b,
 \qquad
 a\le4b.
\tag{R-91307.4}

## 2. Survival versus hazard

For one rough prime,

\[
 A=1-p^{-1},
 \qquad
 B=1-p^{-1/2}.
\]

The survival packet has `a=A>b=B` and `A<2B`; the positive return of
`L-91338` is valid at that scope.

The least-prime hazard packet instead has

\[
\boxed{
 a=1-A=\frac1p,
 \qquad
 b=1-B=\frac1{\sqrt p},
}
\tag{R-91307.5
}

so

\[
 a<b.
\]

The first coefficient in (R-91307.3) is then negative on the reserve input.

## 3. Exact one-vector impossibility

Take

\[
 (L,R)=(0,1).
\]

The hazard ledgers are

\[
 T=2b,
 \qquad
 S=a.
\]

For any positive physical state with target `L'+2R'=2b`, the endpoint score
satisfies

\[
 2L'+R'\ge b,
\]

because its minimum at fixed target occurs at `L'=0,R'=b`.

But

\[
 a=\frac1p<\frac1{\sqrt p}=b.
\]

Hence no positive `(L',R')` can have both ledgers. Equivalently, the formal
solution is

\[
 L'=\frac{2(a-b)}3<0.
\]

Thus

\[
\boxed{
 \text{hazard target and score ledgers cannot both be preserved in the positive `(L,R)` cone.}
}
\tag{R-91307.6
}

## 4. Status effect

The following remain exact:

- the hidden least-prime source partition of `L-91336`;
- separate target and score ledger disintegrations in hidden coordinates;
- the positive survival return of `L-91338`;
- the common Hilbert innovation and endpoint port budgets.

What does not follow is the statement that every hazard child may be normalized
to one positive physical child with the same coefficient in both ledgers.

Consequently:

```text
hidden hazard source partition                    RETAINED EXACT
hidden target ledger partition                    RETAINED EXACT
hidden score ledger partition                     RETAINED EXACT
positive survival canonical return                RETAINED EXACT
positive hazard two-ledger canonical return       IMPOSSIBLE
T-91302 weights from naive hazard normalization   BLOCKED
hazard score subsidy / richer child cone           OPEN
Riemann Hypothesis                                UNPROVEN
```

## 5. Correct repair targets

A valid continuation must do one of:

1. retain hazard children in a richer positive hidden cone rather than returning
   immediately to `(L,R)`;
2. add an explicit positive score subsidy of at least `b-a` on the pure reserve
   ray, paid from the favorable rough dilation/endpoint port;
3. group hazard and survival packets before canonical return so their combined
   diagonal ratio lies in `[1,4]`;
4. formulate a branching consumer with separate target and score measures plus
   a proved bounded discrepancy.

No such repair is asserted here.
