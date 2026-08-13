# L-91661 — The finite-Euler ordinary overdraw is exactly the rough-child reservoir

Claim ID: `L-91661`  
Status: **PROVED EXACT LEAST-PRIME DECOMPOSITION**  
Created: 2026-08-13  
Depends on: `R-91654`, unique factorization  
RH status: **unproved**

Let

\[
P=P_{61}=\prod_{\ell\le61}\ell
\]

and retain

\[
H_P(Z)=\sum_{\substack{n\le Z\\(n,P)=1}}
 n^{-1/2}\log(Z/n).
\]

For a prime `p>=67`, define the positive least-prime tail

\[
\boxed{
H_{\ge p}(Y)=
\sum_{\substack{m\le Y\\P^-(m)\ge p}}
 m^{-1/2}\log(Y/m),
}
\tag{L-91661.1}
\]

where `P^-(1)=+infinity` and `P^-(m)` denotes the least prime factor of `m` for
`m>1`.

Every integer `n>1` with `(n,P)=1` has a unique least prime factor `p>=67` and a
unique representation

\[
n=pm,
\qquad P^-(m)\ge p.
\]

Partitioning the defining sum of `H_P` by this least prime gives

\[
\boxed{
H_P(Z)
=
\log Z+
\sum_{\substack{p\ge67\\p\le Z}}
 p^{-1/2}H_{\ge p}(Z/p).
}
\tag{L-91661.2}
\]

All terms on the right are nonnegative.  Thus the excess in `R-91654` is not an
unstructured normalization error.  It is exactly the total ordinary-capacity
reservoir of the actual rough children.

For an endpoint `X` and physical column `q`, define

\[
C_{\ge p,X/p}(q)=
q^{-1/2}H_{\ge p}(X/(pq)).
\]

Then (L-91661.2) becomes

\[
\boxed{
C_{P,X}(q)
=
w_X(q)+
\sum_{\substack{p\ge67\\pq\le X}}
 p^{-1/2}C_{\ge p,X/p}(q).
}
\tag{L-91661.3}
\]

Consequently a proof cannot both

```text
pack the full canonical P61 row against the native ramp,
and
retain all rough-child capacities as additional positive packets.
```

That would spend the rough reservoir twice.

The constructive repair is to subtract the child before packing.  For
`r=p^(-1/2)` use the complete causal datum

\[
C_{p,u}=P_u-rU_pP_{u/p}.
\]

`L-91654` proves that this difference is nonnegative simultaneously in target,
component rows, ordinary capacities and radix-four capacities.  The exact
coefficient identity of `L-91650` then writes the parent as

\[
\text{current causal differences}
+
\text{one contracted copy of each actual child},
\]

with total child coefficient below `1/8` and no duplicated reservoir.

```text
finite-Euler excess                       EXACT POSITIVE
least-prime rough-child decomposition      EXACT
naive finite-row/native-capacity splice    FORBIDDEN
causal-difference repair                   AVAILABLE
Riemann Hypothesis                         UNPROVED
```
