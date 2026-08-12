# R-91304 — `L-91325` uses fractional-column feasibility not proved by the positive-functor theorem

Claim ID: `R-91304`  
Status: **EXACT LOGICAL SCOPE REFUTATION / REPAIR TARGET**  
Created: 2026-08-12  
Depends on: `L-91318`, `L-91324`, `L-91325`  
RH status: **unproved**

## 1. The load-bearing step

`L-91325.16` asserts, for a rough color `m` and physical integer column `Q`,

\[
 \operatorname{Resp}^{\rm parent}_b(Q)
 =m^{-1/2}\operatorname{Resp}^{\rm child}_b(Q/m)
 \le \Omega_b^{\rm parent}(Q).
\tag{R-91304.1}
\]

The exact equality is the real-column affine covariance of `L-91318/L-91324`.
The inequality is a different statement: it requires the **finite child packing**
to be feasible at the generally noninteger column `Q/m`.

## 2. What `L-91324` actually proves

`L-91324` proves that quantization, affine Pascal lifting, physical-column
evaluation and summation over colors are positive linear maps. Consequently a
pointwise positive-semidefinite port domination survives those operations.

Its scope firewall explicitly states that it does **not** prove either

```text
integer-column feasibility -> feasibility at every real column;
ordinary positive domination -> radix-four domination by subtracting two values.
```

The exact identity

\[
 \overline\beta_{m(n+1)-1}(Q)=\overline\beta_n(Q/m)
\]

does not supply an inequality against the real target unless that real-column
inequality has been proved independently.

## 3. Why the finite collar results do not fill the gap

`L-91114/L-91115` prove feasibility of the **summed, once-quantized parent
packing at physical integer columns** after one global safety factor and one top
omission. They do not prove branchwise feasibility of separately quantized child
packings at every fractional `Q/m`.

In particular, the following inference is invalid:

```text
child feasible on integer columns
+ exact affine covariance
+ parent finite collar theorem
-> child feasible at Q/m for every physical Q.
```

The parent collar estimate is applied after colors have been summed. Applying it
separately to every color would duplicate both the safety loss and the target
ledger.

## 4. Status of the transport-disintegration argument

The abstract Markov-kernel disintegration in `L-91325.2--10` is exact. Linear
quantization also preserves a positive measure partition exactly.

The correct repair is therefore:

```text
partition the continuum source and target measures;
push every branch to the parent continuum endpoint coordinate;
sum all colors there;
quantize the total measure once;
apply the finite mismatch/collar repair once at physical integer columns.
```

That **sum-before-quantize** construction never invokes feasibility of an
arbitrary finite child at a noninteger column.

## 5. Consequence

Equations `L-91325.16--19` and the proposed complete RH composition do not follow
from the cited dependencies. This refutation does not disprove the underlying
transport-disintegration strategy; it isolates the exact missing assembly
identity.

```text
abstract source/target disintegration              RETAINED EXACT
positive functorial color erasure                   RETAINED EXACT
branchwise finite feasibility at Q/m                NOT PROVED
one-use target inequality L-91325.17                GAP
proposed complete composition L-91325.19            BLOCKED
sum-before-quantize repair                           OPEN / NEXT TARGET
Riemann Hypothesis                                  UNPROVEN
```
