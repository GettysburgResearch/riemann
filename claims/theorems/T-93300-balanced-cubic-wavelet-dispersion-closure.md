# T-93300 — Higher-order balanced wavelet dispersion is the explicit remaining Q4 closure theorem

Claim ID: `T-93300`  
Status: **CANDIDATE CLOSURE INTERFACE / OPEN ARITHMETIC ESTIMATE**  
Created: 2026-08-16  
Depends on: `R-93300`, `L-93300`--`L-93304`, `R-93301`; frozen `T-93251`  
RH status: **unproved**

For fixed `r>=1`, let

\[
\eta_r=1-\frac1{2(r+1)},
\qquad
U=\lfloor N^{1/3}\rfloor,
\]

\[
a_U(q)=\sum_{\substack{d\mid q\\d>U}}\mu(d),
\]

and

\[
B_r^\sharp(N)=
\sum_{\substack{m,q>U\\N^{\eta_r}<mq\le N}}
\Lambda(m)a_U(q)W_r(mq/N).
\]

The proposed balanced dispersion estimate is

\[
\boxed{|B_r^\sharp(N)|\ll_r\sqrt N(\log(2N))^A}
\tag{T-93300.1}
\]

for one fixed `r` and one fixed `A`.

## Exact composition

`L-93302` proves unconditionally

\[
A_r(N)=r!B_r^\sharp(N)+O_r(\sqrt N\log^2(2N)).
\]

Thus (T-93300.1) gives the square-root endpoint bound. The zero-safe Mellin multiplier of `L-93300` then excludes every zero with real part greater than `1/2`; the functional equation yields RH.

Conversely RH implies (T-93300.1). The estimate remains RH-bearing. The advance is that its coefficients, product annulus, and carrier factorization are explicit, while every Type-I and deep-hyperbola range has been proved separately.

For `r=1`, the hard annulus begins at `N^(3/4)`. For `r=2`, it begins at `N^(5/6)`. Fixed higher order pushes the unresolved products arbitrarily close to the top hyperbola without introducing a zero in the critical strip.

## No completeness claim

This packet does **not** prove (T-93300.1). It is not a rename of CPBD: it is a Vaughan-derived Möbius-prime bilinear form with a specified compact wavelet and a provably thin product annulus.

The next attack should use the exact carrier Fourier coefficient `L-93303.5` or the sparse endpoint forcing `L-93304.1`. A coefficient-blind estimate is ruled out by `R-93301`.

```text
PR #498 centered cubic spine                 VERIFIED WITH FIXES
zero-safe endpoint-order family              PROVED EXACT
prime-power compression                      PROVED
Vaughan Type-I ranges                        PROVED
products mq<=N^(eta_r)                       PROVED SAFE
balanced top-hyperbola Type-II               OPEN / RH-BEARING
First-Hermite carrier bridge                 EXACT STRUCTURAL INTERFACE
Riemann Hypothesis                           UNPROVED
```
