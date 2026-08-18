# L-98017 — The Euler discrepancy has compact negative support

Claim ID: `L-98017`  
Status: **PROVED EXACT-RATIONAL FINITE CERTIFICATE + ANALYTIC TAIL**  
Created: 2026-08-18  
Depends on: `L-98016`; replay `X-98010/verify_euler_discrepancy.py`  
RH status: **not assumed**

Let

\[
E(Y)=2\sum_{m\le Y}{1\over\sqrt m}-4\sqrt Y+3.
\]

Then

\[
\boxed{
E(Y)>0\qquad(Y\ge256).
}
\tag{L-98017.1}
\]

Hence the negative part

\[
E_-(Y)=(-E(Y))_+
\]

is supported in the compact interval

\[
\boxed{1\le Y<256.}
\tag{L-98017.2}
\]

## 1. One finite certificate

Put

\[
\delta_{256}
=2\sum_{m=1}^{256}{1\over\sqrt m}
-4\sqrt{257}+3.
\tag{L-98017.3}
\]

The exact-rational checker constructs, at denominator `10^18`, an upper rational enclosure for every `sqrt(m)` and therefore a lower rational enclosure for every `1/sqrt(m)`, together with an upper rational enclosure for `sqrt(257)`. It verifies

\[
\boxed{
\delta_{256}>0.
}
\tag{L-98017.4}
\]

No floating-point sign is used in the certificate.

## 2. Analytic propagation

Fix an integer `N>=256`. Because `x^{-1/2}` is decreasing,

\[
\sum_{m=257}^{N}{1\over\sqrt m}
\ge
\int_{257}^{N+1}{dx\over\sqrt x}
=2\bigl(\sqrt{N+1}-\sqrt{257}\bigr).
\]

Therefore

\[
\begin{aligned}
2\sum_{m=1}^{N}{1\over\sqrt m}
-4\sqrt{N+1}+3
&\ge
2\sum_{m=1}^{256}{1\over\sqrt m}
-4\sqrt{257}+3\\
&=\delta_{256}>0.
\end{aligned}
\tag{L-98017.5}
\]

By `L-98016`, `E` is decreasing on each cell `N<Y<N+1`. Its cell infimum is the left limit at `N+1`, namely the left side of (L-98017.5). Thus every point of every cell with `N>=256` is positive. The integer jumps are upward, so the integer states are positive as well.

## 3. Exact decomposition

Write

\[
E=E_+-E_-,
\qquad E_\pm\ge0.
\]

Then the target root becomes

\[
\boxed{
\mathcal T_X
=2-
\sum_{n\le X}{\mu(n)\over\sqrt n}E_+(X/n)
+
\sum_{X/256<n\le X}{\mu(n)\over\sqrt n}E_-(X/n).
}
\tag{L-98017.6}
\]

The adverse compact correction in the final term lives only on the factor-256 annulus

\[
X/256<n\le X.
\]

This does not sign either Möbius sum. It proves that every negative local Euler defect is a finite-band activation phenomenon; the infinite tail of the local kernel is nonnegative.

## 4. Research boundary

The compact support of `E_-` invites a factor-256 annularization, first-owner decomposition, and exact Type-I/Type-II attack. A proof may not discard the global positive part `E_+` or replace its signed Möbius projection by its absolute value.

```text
constant-two discrepancy identity             PROVED
bounded local kernel                           PROVED
negative local kernel supported below 256      PROVED
signed positive-tail Möbius projection          OPEN
compact annular negative correction             EXACT
TRP67                                           OPEN / RH-BEARING
```
