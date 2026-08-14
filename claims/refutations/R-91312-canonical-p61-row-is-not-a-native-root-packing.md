# R-91312 — The canonical `P_61` row is not a native-root packing

Claim ID: `R-91312`  
Status: **EXACT NORMALIZATION FIREWALL / COUNTEREXAMPLE**  
Created: 2026-08-14  
Corrects: any reading of historical `L-91374/T-91310` that identifies the canonical finite-Euler capacity with the native endpoint capacity  
RH status: **unproved**

## 1. Two distinct capacities

Let

\[
 P=P_{61}=\prod_{p\le61}p
\]

and retain the canonical finite-Euler row

\[
 D_{P,X}(j)=\sum_{d\mid P}\frac{\mu(d)}{\sqrt d}Q_{X/d}(j).
\tag{R-91312.1}
\]

Its ordinary physical response is

\[
\boxed{
 C_{P,X}(q)=\frac1{\sqrt q}H_P(X/q),
}
\tag{R-91312.2}
\]

where

\[
 H_P(Z)=\sum_{\substack{n\le Z\\(n,P)=1}}
 \frac1{\sqrt n}\log\frac Zn.
\tag{R-91312.3}
\]

The native endpoint capacity is only

\[
\boxed{
 w_X(q)=\frac1{\sqrt q}\log\frac Xq\,\mathbf1_{q\le X}.
}
\tag{R-91312.4}
\]

The `n=1` term of (R-91312.3) is (R-91312.4). Every further rough integer is an additional positive reservoir. Therefore

\[
\boxed{
 C_{P,X}(q)-w_X(q)
 =\frac1{\sqrt q}
 \sum_{\substack{2\le n\le X/q\\(n,P)=1}}
 \frac1{\sqrt n}\log\frac{X}{qn}
 \ge0.
}
\tag{R-91312.5}
\]

## 2. Strict finite counterexample

Take

\[
 X=136,
 \qquad q=2.
\]

The only rough integer in `(1,68]` beyond one is `67`. Hence

\[
\boxed{
 C_{P,136}(2)-w_{136}(2)
 =\frac1{\sqrt{134}}\log\frac{68}{67}>0.
}
\tag{R-91312.6}
\]

Thus the canonical finite-Euler row overdraws the native ordinary column.
Applying the radix-four difference gives the corresponding distinction between
its detail capacity and the native detail capacity.

## 3. Consequence

The following inference is invalid:

```text
canonical P61 row >= 0
+ canonical P61 response >= 0
--------------------------------
canonical P61 row is a native endpoint packing.
```

The canonical row is admissible for the **combined native-plus-rough-reservoir
packet**, not automatically for the native root packet alone. Packing the whole
canonical row and then recursively packing the same rough reservoir spends that
reservoir twice.

Any complete proof must instead provide a positive physical disintegration

```text
canonical finite-Euler packet
 = native current packet
   + source-disjoint recursive rough packets
```

in rows, ordinary columns, radix-four columns, literal entropy, and every
retained port coordinate.

```text
canonical P61 ordinary response        EXACT / POSITIVE
native ordinary response               EXACT / SMALLER
strict overdraw witness                 EXACT
historical native-admissibility claim  FALSE
positive physical reservoir split      OPEN / RH-BEARING
Riemann Hypothesis                      UNPROVEN
```
