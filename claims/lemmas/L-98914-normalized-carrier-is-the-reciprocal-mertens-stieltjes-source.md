# L-98914 — The normalized pole-centered carrier is exactly the reciprocal-Mertens Stieltjes source

Claim ID: `L-98914`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-18  
Depends on: `L-98913`  
RH status: **not assumed**

Put

\[
 A(x)=\sum_{n\le x}\frac{\mu(n)}n,
 \qquad
 F(t)=e^tA(e^t)\quad(t\ge0),
\]

and extend `F` by zero for `t<0`. At `t=log n`, the function `A(e^t)` jumps by
`mu(n)/n`, so `F` jumps by `mu(n)`. Between jumps its derivative is
`e^tA(e^t)`. Therefore, as a signed Stieltjes measure,

\[
\boxed{
 dF(t)=\sum_{n\ge1}\mu(n)\,\delta_{\log n}(dt)
       +e^tA(e^t)\,dt.
}
\tag{L-98914.1}
\]

For `Re s>1`,

\[
\begin{aligned}
 \int_{[0,\infty)}e^{-st}\,dF(t)
 &=\frac1{\zeta(s)}
   +\int_1^\infty A(x)x^{-s}\,dx\\
 &=\frac1{\zeta(s)}+
   \frac1{(s-1)\zeta(s)}.
\end{aligned}
\]

Hence

\[
\boxed{
 \int_{[0,\infty)}e^{-st}\,dF(t)
 =\frac{s}{(s-1)\zeta(s)}
 =\mathfrak B_1(s).
}
\tag{L-98914.2}
\]

Thus the continuum carrier in `L-98913` is not an auxiliary comparison
reservoir. It is exactly the Abel/Stieltjes completion that turns the discrete
Möbius atoms into the derivative of the reciprocal-Mertens storage
`e^tA(e^t)`.

Let

\[
 \phi_{T,\tau}(t)
 =e^{-t/2-t^2/(4T)-i\tau t}.
\]

The normalized heat packet at intensity one is

\[
 \mathfrak H_{1,T}(\tau)
 =\int\phi_{T,\tau}(t)\,dF(t).
\]

Stieltjes integration by parts gives the exact Hermite-storage formula

\[
\boxed{
 \mathfrak H_{1,T}(\tau)
 =\int_0^\infty
 \left(\frac12+\frac{t}{2T}+i\tau\right)
 e^{t/2-t^2/(4T)-i\tau t}
 A(e^t)\,dt.
}
\tag{L-98914.3}
\]

No boundary term is missing: the jump `F(0)-F(0^-)=1` is encoded by the
Stieltjes integration-by-parts formula.

For general `theta>0`, `mathfrak B_theta=mathfrak B_1^theta`; its mixed source
is the fractional convolution power of (L-98914.1), equivalently the positive
continuum carrier tensored with the even/odd prime chaos of `L-98913`.

## Consequence

`NPCFHE` is a source-specific fractional smoothing theorem for the same
reciprocal-Mertens storage that drives the target zero-hinge route. It is not a
source-blind Fock trace estimate. Any proof must exploit the exact covariance
between the discrete jumps and the continuous storage in (L-98914.1); replacing
them by independent positive marginals destroys the cancellation at `s=1` and
restores the forbidden rate `1/2`.
