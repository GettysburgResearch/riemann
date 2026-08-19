# L-99213 — The literal score of the full Möbius component row is exactly the prime-power benchmark

Claim ID: `L-99213`  
Status: **PROVED EXACT FINITE IDENTITY**  
Created: 2026-08-19  
RH status: **not assumed**

For real `X>=1`, define the full Möbius component row

\[
 c_X(j)=\sum_{n\le X/j}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\tag{L-99213.1}
\]

The literal score of one canonical packet is

\[
 \mathcal H(Q_Y)
 =E(Y)
 :=\sum_{2\le m\le Y}
   \frac{\log m}{\sqrt m}\log\frac Ym.
\tag{L-99213.2}
\]

All sums below are finite. Therefore

\[
\begin{aligned}
 \mathcal H(c_X)
 &=\sum_{nm\le X}
   \frac{\mu(n)\log m}{\sqrt{nm}}
   \log\frac X{nm}\\
 &=\sum_{k\le X}\frac1{\sqrt k}
   \log\frac Xk
   \sum_{n\mid k}\mu(n)\log\frac kn.
\end{aligned}
\tag{L-99213.3}
\]

The divisor convolution identity

\[
 \sum_{n\mid k}\mu(n)\log(k/n)=\Lambda(k)
\tag{L-99213.4}
\]

is exactly `mu*log=Lambda`. Hence

\[
 \boxed{
 \mathcal H(c_X)
 =P_\Lambda(X)
 :=\sum_{k\le X}
   \frac{\Lambda(k)}{\sqrt k}\log\frac Xk.
 }
\tag{L-99213.5}
\]

## Consequences

1. The finite equality row does **not** have literal score `4sqrt(X)` in
   general. That number is the continuum/equality-density score datum, not the
   literal score after the finite Möbius row is formed.
2. The difference `4sqrt(X)-P_Lambda(X)` is load bearing and cannot be removed
   by scoring the resolved row last.
3. This correction does not affect a componentwise positivity argument: the
   fixed-row Mellin transform reads one row coordinate, not the total literal
   score.

Thus the constant-deficit score conclusions in `L-99022.3`, `L-99050.11` and
application-level descendants are withdrawn wherever they identify the
resolved full Möbius row with literal score `4sqrt(X)`.
