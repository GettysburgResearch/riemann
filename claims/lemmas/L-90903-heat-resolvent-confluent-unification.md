# L-90903 — The safe-Euler resolvent hierarchy is a Gamma moment transform of first-Hermite zero heat

Claim ID: `L-90903`  
Status: **EXACT TRANSFORM IDENTITY**  
Created: 2026-08-11  
Depends on: PR #378 terminal resolvent derivatives and PR #379 first-Hermite zero-heat criterion

PRs #378 and #379 are not independent proof mechanisms.  In the confluent depth limit, the former is the Stieltjes/Gamma moment transform of the latter.

## 1. Resolvent derivatives

For \(k\ge0\), PR #378 uses

\[
 R_{k,y}(z)=k!\left[
 (1-z^2)^{-k-1}
 -\frac12(1-z^2-2yz)^{-k-1}
 -\frac12(1-z^2+2yz)^{-k-1}
 \right].
\tag{L-90903.1}
\]

A Taylor expansion in \(y\) gives

\[
 \boxed{
 \lim_{y\downarrow0}\frac{R_{k,y}(z)}{y^2}
 =-2(k+2)!\frac{z^2}{(1-z^2)^{k+3}}.
 }
\tag{L-90903.2}
\]

## 2. Gamma-moment representation

Whenever \(\Re(1-z^2)>0\),

\[
 \frac{(k+2)!}{(1-z^2)^{k+3}}
 =\int_0^\infty q^{k+2}e^{-q}e^{qz^2}\,dq.
\]

Hence

\[
 \boxed{
 \lim_{y\downarrow0}\frac{R_{k,y}(z)}{y^2}
 =-2\int_0^\infty
 q^{k+2}e^{-q}
 z^2e^{qz^2}\,dq.
 }
\tag{L-90903.3}
\]

The kernel \(z^2e^{qz^2}\) is precisely the centered first-Hermite zero-heat kernel of PR #379, up to the sign and normalization used there.

## 3. Consequences

After summing over any zero multiset for which the interchange is justified,

```text
first-Hermite heat sign for every q
    -> every safe-Euler resolvent derivative sign;
large derivative order k
    = Gamma concentration at heat q approximately k;
terminal isolation by k
    = terminal isolation by large heat time.
```

The asymptotic concentration is quantitative: the Gamma density \(q^{k+2}e^{-q}\) has mean \(k+3\) and relative width \(O(k^{-1/2})\).

Thus the minimal remaining scalar is the first-Hermite inequality of PR #379.  The resolvent/Hankel family is valuable because it evaluates at three fixed safe Euler points, but it does not create an independent source of positivity.
