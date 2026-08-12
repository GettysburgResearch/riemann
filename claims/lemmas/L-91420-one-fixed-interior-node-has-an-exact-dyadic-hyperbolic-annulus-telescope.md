# L-91420 — One fixed interior node has an exact dyadic hyperbolic-annulus telescope

Claim ID: `L-91420`  
Status: **PROVED EXACT MODEL-SPACE TELESCOPE; ARITHMETIC ANNULAR EXHAUSTION OPEN**  
Created: 2026-08-12  
Imports: `L-91313` on PR #403  
RH status: **unproved**

## 1. Nested crossed-zero Blaschke products

Use the right-half-plane horizontal Xi quotient of `L-91313`.  For `a>0`, let

\[
 B_a
\]

be the canonical Blaschke product of the crossed zeros in

\[
 \Re s>\frac12+a.
\]

Only its modulus is used, so the unimodular normalization is irrelevant.
For `0<a<b`, the crossed-zero sets are nested and

\[
 \boxed{
 B_a=B_b C_{a,b}
 }
 \tag{L-91420.1}

up to a unimodular constant, where `C_(a,b)` is the Blaschke product of the
zeros in the horizontal annulus

\[
 \frac12+a<\Re s\le\frac12+b.
 \tag{L-91420.2}

## 2. Fixed-node hyperbolic mass

Fix once and for all one real interior node

\[
 \eta>0.
 \]

Define

\[
 \boxed{
 H_a(\eta)
 =\frac{|B_a(\eta)|^{-2}-1}{2\eta}.
 }
 \tag{L-91420.3}

This is exactly the hyperbolic diagonal of `L-91313`:

\[
 H_a(\eta)=\mathcal K_a^{\rm hyp}(\eta,\eta).
 \tag{L-91420.4}

It is nonnegative and vanishes exactly when the corresponding crossed-zero
set is empty.

For the annular factor put

\[
 H_{a,b}^{\rm ann}(\eta)
 =\frac{|C_{a,b}(\eta)|^{-2}-1}{2\eta}.
 \tag{L-91420.5}

## 3. Exact annular increment

Equation (L-91420.1) gives

\[
 |B_a(\eta)|^{-2}
 =|B_b(\eta)|^{-2}|C_{a,b}(\eta)|^{-2}.
\]

Therefore

\[
 \boxed{
 H_a(\eta)
 =H_b(\eta)
  +|B_b(\eta)|^{-2}
   H_{a,b}^{\rm ann}(\eta).
 }
 \tag{L-91420.6
}

Every increment is nonnegative.  It is zero if and only if the annular
Blaschke factor is constant, equivalently if the annulus (L-91420.2) contains
no crossed zero.

No source or explicit-formula input enters this identity.

## 4. Dyadic telescope from the known zero-free half-plane

Take

\[
 a_j=2^{-j-1},
 \qquad j=0,1,2,\ldots.
 \tag{L-91420.7}

At `a_0=1/2`, the crossed half-plane is `Re s>1`, so

\[
 H_{a_0}(\eta)=0.
 \tag{L-91420.8}

Iterating (L-91420.6) gives

\[
 \boxed{
 H_{a_J}(\eta)
 =\sum_{j=1}^{J}
 |B_{a_{j-1}}(\eta)|^{-2}
 H_{a_j,a_{j-1}}^{\rm ann}(\eta).
 }
 \tag{L-91420.9}

Thus false RH produces a first nonzero dyadic annular increment at the same
fixed node.

Conversely, if every increment in (L-91420.9) vanishes, there are no zeros in
any half-plane

\[
 \Re s>\frac12+a_J.
\]

Letting `J -> infinity` and using functional-equation symmetry gives RH.

## 5. Why one node is enough

A nonconstant Blaschke factor has modulus strictly less than one at every
interior point.  Therefore one fixed `eta` detects every annulus; no carrier
density, Gram capture, or limiting interpolation theorem is required on the
model side.

The remaining arithmetic theorem is not to prove an all-packet operator
inequality.  It is to construct, at each dyadic annulus, a coefficient-one
source innovation map whose declared critical and stable outputs exhaust the
innovation before the nonnegative term in (L-91420.6) can be populated.

## 6. Exact boundary

```text
nested crossed-zero products                         EXACT
one-node hyperbolic diagonal                         EXACT
annular positive increment                           EXACT
dyadic telescope from Re s>1                         EXACT
all annular increments zero -> RH                    EXACT
arithmetic annular source exhaustion                 OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```