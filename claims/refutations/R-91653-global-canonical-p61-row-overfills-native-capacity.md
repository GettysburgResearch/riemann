# R-91653 — The global canonical `P_61` row overfills the native ordinary and radix-four capacities

Claim ID: `R-91653`  
Status: **EXACT REFUTATION OF THE GLOBAL ROUTE-A CAPACITY CLAIM**  
Created: 2026-08-13  
Depends on: `L-91363`, `L-91661`  
Corrects: the direct global-capacity reading of `T-91310` and the Route-A summary in the CFFP three-route packet  
RH status: **unproved**

## 1. Refuted implication

The direct canonical-row route combines:

```text
canonical P_61 row is coefficientwise nonnegative;
its ordinary and radix-four responses are nonnegative;
its literal entropy exceeds the declared finite score;
therefore it is a complete native-feasible CFFP row at every endpoint.
```

The last implication is false. A physical response must be bounded by the
**native allowance**, not merely be nonnegative.

## 2. Exact witness

For the canonical row, `L-91363` gives

\[
C_{P,X}(q)=q^{-1/2}H_P(X/q),
\]

while the native allowance is

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

At

\[
X=135,
\qquad q=2,
\]

`L-91661` proves

\[
\boxed{
C_{P,135}(2)-w_{135}(2)
=rac1{\sqrt{134}}\log\frac{135}{134}
>rac1{1620}>0.
}
\tag{R-91653.1}
\]

The same endpoint and column also violate the native radix-four allowance:

\[
\boxed{
\Theta_{P,135}(2)-\Omega_{135}(2)
=rac1{\sqrt{134}}\log\frac{135}{134}
>rac1{1620}>0.
}
\tag{R-91653.2}
\]

Thus the row is not in the native feasible cone.

## 3. Source of the error

The first rough integer `67` enters the finite-Euler response as soon as
`X/q>67`. It contributes the strictly positive term

\[
q^{-1/2}67^{-1/2}\log\frac{X}{67q}.
\]

This contribution is absent from the native allowance. Positivity of the
canonical response therefore makes the mismatch worse; it cannot establish
subordination.

The exact equality of the two dictionaries holds only while

\[
X/q\le67.
\]

## 4. Scope of the refutation

This refutation does **not** challenge:

```text
coefficientwise nonnegativity of the canonical row;
the finite/direct entropy identity;
the strict entropy surplus on its stated normalization;
the compact quotient-window identity X/q<=67;
the possibility of a provenance-causal or explicitly allowance-subordinate repair.
```

It refutes only the promotion of those facts to an all-scale native-feasible
producer without a separate coordinatewise allowance decomposition.

## 5. Corrected Route-A boundary

A repaired canonical-row route must first split off every rough activation and
prove, in the native physical coordinates,

\[
w_X=w_{\rm cur}+\sum_b w_b,
\qquad
\Omega_X=\Omega_{\rm cur}+\sum_b\Omega_b,
\]

with all terms nonnegative, before inserting current and child rows. The global
row `D_(P,X)` cannot itself be used as the current native packing.

```text
canonical row sign                              RETAINED
canonical response positivity                   RETAINED
native ordinary feasibility at all scales       REFUTED
native radix-four feasibility at all scales     REFUTED
compact quotient window <=67                    RETAINED EXACT
T-91310 direct global Route A                    NOT A CFFP PROOF
Riemann Hypothesis                               UNPROVED
```
