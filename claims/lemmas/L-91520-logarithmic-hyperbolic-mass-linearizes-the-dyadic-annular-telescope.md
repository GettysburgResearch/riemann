# L-91520 — Logarithmic hyperbolic mass linearizes the dyadic annular telescope

Claim ID: `L-91520`  
Status: **PROVED EXACT ADDITIVE BLASCHKE/GREEN TELESCOPE; ARITHMETIC EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91420`; `L-91313` on PR #403  
RH status: **unproved**

## 1. Multiplicative mass behind the previous telescope

Retain the crossed-zero Blaschke product `B_a` and fixed interior node
`eta>0` from `L-91420`. Put

\[
 H_a(\eta)
 =\frac{|B_a(\eta)|^{-2}-1}{2\eta}.
 \tag{L-91520.1}

\]

Define instead the logarithmic hyperbolic mass

\[
\boxed{
 \Lambda_a(\eta)
 =\log(1+2\eta H_a(\eta))
 =-2\log|B_a(\eta)|.
}
\tag{L-91520.2}

\]

This is nonnegative and vanishes exactly when the crossed-zero product is
constant.

For an annular factor `C_(a,b)` define

\[
\boxed{
 \Lambda_{a,b}^{\rm ann}(\eta)
 =-2\log|C_{a,b}(\eta)|.
}
\tag{L-91520.3}

\]

## 2. Exact additive annular identity

For `0<a<b`, `L-91420` gives

\[
 B_a=B_bC_{a,b}
\]

up to a unimodular constant. Taking logarithmic modulus yields

\[
\boxed{
 \Lambda_a(\eta)
 =\Lambda_b(\eta)
  +\Lambda_{a,b}^{\rm ann}(\eta).
}
\tag{L-91520.4}

\]

There is no multiplicative weight. The earlier hyperbolic-mass identity is
recovered by exponentiation:

\[
\boxed{
 H_a(\eta)
 =H_b(\eta)
  +e^{\Lambda_b(\eta)}
   H_{a,b}^{\rm ann}(\eta),
}
\tag{L-91520.5}

\]

because

\[
 H_{a,b}^{\rm ann}(\eta)
 =\frac{e^{\Lambda_{a,b}^{\rm ann}(\eta)}-1}{2\eta}.
\]

## 3. Dyadic additive telescope

For

\[
 a_j=2^{-j-1},
\]

one has `Lambda_(a_0)(eta)=0` at `a_0=1/2`, since `Re s>1` is zero free. Thus

\[
\boxed{
 \Lambda_{a_J}(\eta)
 =\sum_{j=1}^J
  \Lambda_{a_j,a_{j-1}}^{\rm ann}(\eta).
}
\tag{L-91520.6}

\]

Every term is nonnegative and vanishes exactly when its horizontal annulus
contains no crossed zero. Hence

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \Lambda_{a_j,a_{j-1}}^{\rm ann}(\eta)=0
 \quad\text{for every }j\ge1
 }
\tag{L-91520.7}

\]

for any one fixed interior node `eta>0`.

## 4. Why the logarithmic form is a real simplification

The source side of the repository is multiplicative:

```text
Euler products;
completed Xi quotients;
Jordan cocycles;
dyadic returned-state amplitudes.
```

Their natural innovations are logarithmic and additive. Equation
(L-91520.6) puts the model hyperbolic obstruction in the same additive
coordinates. It removes the factor

\[
 |B_{a_{j-1}}(\eta)|^{-2}
\]

from every generation and prevents old hyperbolic mass from being charged
again.

## 5. Determinant reading

At one node,

\[
 1+2\eta H_a(\eta)=|B_a(\eta)|^{-2}
\]

is the scalar determinant of the crossed-zero port. Therefore
`Lambda_a(eta)` is its log determinant. The dyadic annulus decomposition is a
literal determinant product and (L-91520.6) is its log-determinant chain rule.

This suggests replacing one-node norm exhaustion by a source-ordered
log-determinant or relative-entropy exhaustion. Such an identification remains
open; no determinant is defined from the unknown target kernel.

## 6. Exact boundary

```text
hyperbolic mass -> logarithmic mass                EXACT
annular logarithmic additivity                     EXACT
dyadic unweighted telescope                        EXACT
one fixed node detects every annulus               EXACT
all log increments zero -> RH                      EXACT
arithmetic log-determinant exhaustion              OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```
