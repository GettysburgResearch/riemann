# L-102745 — Every fixed prime-chaos sector has an alternating power-scale outer carrier

Claim ID: `L-102745`  
Status: **PROVED UNCONDITIONAL FIXED-CHAOS ASYMPTOTIC**  
Created: 2026-08-23  
Depends on: `L-102737`; the classical fixed-`k` Landau theorem for almost primes  
RH status: **not assumed**

Let `R_L` be the carrier-centered Lorentz/outer-ray kernel of `L-102737`. It is
compactly supported in `[1,8]` and

\[
 \widehat R_L(1/2)
 =\int_1^8R_L(y)y^{-3/2}dy
 =-\kappa_0,
\]

where

\[
 \kappa_0=8\log2(1-2^{-1/2})^2>0.
\]

For a fixed integer `k>=1`, define the distinct-prime `k`-chaos sector

\[
 C_k(X)
 =(-1)^k
 \sum_{\substack{n\ {m squarefree}\\\omega(n)=k}}
 \frac1{\sqrt n}R_L(X/n).
 \tag{L-102745.1}
\]

Then

\[
 \boxed{
 C_k(X)
 =(-1)^{k+1}\kappa_0
 \frac{\sqrt X}{\log X}
 \frac{(\log\log X)^{k-1}}{(k-1)!}
 +O_k\left(
 \frac{\sqrt X(\log\log X)^{k-2}}{\log X}
 \right).
 }
 \tag{L-102745.2}
\]

## Proof

The fixed-`k` Landau theorem gives

\[
 d\#\{n\le t:n\ {m squarefree},\ \omega(n)=k\}
 =
 \left[
 \frac{(\log\log t)^{k-1}}{(k-1)!\log t}
 +O_k\left(\frac{(\log\log t)^{k-2}}{\log t}\right)
 \right]dt
\]

in the partial-summation form required for a fixed compact `C1` test kernel.
Putting `t=X/y` gives the leading factor

\[
 \frac{\sqrt X}{\log X}
 \frac{(\log\log X)^{k-1}}{(k-1)!}
 \int_1^8R_L(y)y^{-3/2}dy.
\]

The second labelled `67` and repeated-prime monomials reduce the number of free
prime coordinates by at least one and enter the displayed error term.

## Consequences

The first sectors are

\[
 C_1(X)
 =+\kappa_0\frac{\sqrt X}{\log X}
 +O(\sqrt X/\log^2X),
\]

\[
 C_2(X)
 =-\kappa_0\frac{\sqrt X\log\log X}{\log X}
 +O(\sqrt X/\log X).
\]

Thus the exact first-chaos quotient of `L-102741` necessarily exposes a
power-sized **negative** second-chaos carrier. The third chaos has the opposite
power-sized sign, and so on.

No finite collection of chaos-wise regional norms can establish the outer-ray
criterion. The cancellation is genuinely all-chaos and must remain inside the
complete Wick current of `T-102800`.