# R-100103 — QPET100101 contradicts the proved positive corridor

Claim ID: `R-100103`  
Status: **PROVED EXACT LOGICAL REFUTATION**  
Created: 2026-08-20  
Depends on: `L-100101`; `T-100101`  
RH status: **unproved**

Fix an integer `k>=2`. Let

\[
N_{Z,k}=\inf\{X\ge1:\mathcal C_{3;Z,k}(X)<0\},
\]

with the convention `N_(Z,k)=infinity` when no negative point exists, and put

\[
A_k^*=\exp\!\left(\operatorname{arsinh}1-P(k)-67^{-k}\right).
\]

`L-100101` proves that for every real `A<A_k^*` there is `Z_0(A,k)` such that

\[
\mathcal C_{3;Z,k}(X)>0
\qquad(1\le X\le Z^A,\ Z\ge Z_0(A,k)).
\]

Consequently

\[
N_{Z,k}>Z^A
\qquad(Z\ge Z_0(A,k)).
\tag{R-100103.1}
\]

Choose any increasing sequence `A_m` with `A_m<A_k^*` and
`A_m -> A_k^*`. Equation (R-100103.1) gives

\[
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}\ge A_m
\]

for every `m`, and therefore

\[
\boxed{
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}\ge A_k^*.
}
\tag{R-100103.2}

This remains true if some or all `N_(Z,k)` are infinite.

But `QPET100101` was defined by the strict opposite inequality

\[
\exists k\ge2:\quad
\liminf_{Z\to\infty}
\frac{\log N_{Z,k}}{\log Z}<A_k^*.
\]

Hence

\[
\boxed{\mathrm{QPET100101}\text{ is false as stated}.}
\tag{R-100103.3}

The conclusion is unconditional. Temporarily assuming an off-line zero does
not alter the corridor theorem and therefore does not repair the contradiction.
The implication `QPET100101 -> RH` is vacuous rather than a usable closure
route.

The proposed stronger mechanism `UPE100101`, which asked for a negative
phase-matched point inside `[Z,Z^A]` with `A<A_k^*`, is likewise ruled out by
the same positive corridor.

```text
finite completion corridor       retained exact
strict-liminf QPET gate           refuted
inside-corridor UPE dominance     refuted
Riemann Hypothesis                unproved
```
