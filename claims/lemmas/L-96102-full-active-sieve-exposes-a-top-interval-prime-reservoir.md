# L-96102 — At full activation the positive rough reservoir is exactly a top-interval prime reservoir

Claim ID: `L-96102`  
Status: **PROVED EXACT ARITHMETIC REFORMULATION**  
Created: 2026-08-16  
Depends on: `L-96100`  
RH status: **unproved**

## 1. Full active prime product

Fix `j>=2` and `Y>=j^2`. Put

\[
 z=\frac Yj
\]

and let

\[
 P(z)=\prod_{p\le z}p.
\]

This is the complete active Euler product for the row at endpoint `Y`: any
prime larger than `z` can occur only in a divisor `d>Y/j` and its row term is
zero by triangular support.

## 2. Rough numbers below the endpoint

If `1<n<=Y` is composite, then it has a prime divisor at most

\[
 \sqrt n\le\sqrt Y\le\frac Yj=z.
\]

Thus every composite `n<=Y` has a prime divisor in `P(z)`. Conversely, every
prime `p` with `z<p<=Y` is coprime to `P(z)`. Therefore

\[
 \boxed{
 \{n\le Y:(n,P(z))=1\}
 =\{1\}\cup\{p:\ z<p\le Y,\ p\text{ prime}\}.
 }
\tag{L-96102.1}
\]

## 3. Exact full-row reservoir/frontier identity

Let

\[
 \mathcal F_j(Y)
 =\sum_{d\mid P(z)}\frac{\mu(d)}{\sqrt d}
   Q_{Y/d}^{\rm tail}(j).
\tag{L-96102.2}
\]

Using `L-96100.11` and (L-96102.1),

\[
\begin{aligned}
 \mathcal F_j(Y)
={}&
 \frac{C_j}{\sqrt1}\log Y
 +C_j\sum_{Y/j<p\le Y}
   \frac{\log(Y/p)}{\sqrt p}\\
&+
 \sum_{m=1}^{j+1}
 \frac{h_j(m)}{\sqrt m}
 \sum_{\substack{d\mid P(z)\\d\le Y/m}}
   \frac{\mu(d)}{\sqrt d}
   \log\frac{Y}{dm},
\end{aligned}
\tag{L-96102.3}
\]

where

\[
 h_j(m)=
 \begin{cases}
 -C_j,&m<j,\\
 (j+2)/j,&m=j,\\
 -1,&m=j+1.
 \end{cases}
\]

Every term and cutoff in (L-96102.3) is finite and exact.

## 4. Consequence for proof architecture

At the full active sieve, the infinite positive reservoir is not an abstract
collection of all integers. It is a weighted prime sum in the top multiplicative
interval

\[
 \left(\frac Yj,Y\right].
\]

The remaining signed frontier consists of explicit truncated Möbius Riesz sums.
Thus a universal multi-prime transport cannot be justified by a local
four-template capacity calculation that ignores cross-`n` ownership and prime
availability.

This does not prove that the transport is impossible. It identifies its actual
arithmetic content.

```text
full active rough reservoir          1 plus top-interval primes
frontier correction                  finite truncated Mobius sums
local all-integer reservoir           unavailable
universal positivity                  OPEN / RH-BEARING
Riemann Hypothesis                    UNPROVED
```
