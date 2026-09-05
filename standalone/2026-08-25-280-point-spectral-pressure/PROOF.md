# A spectral-pressure lift of the seven-gap simple-zero argument

## Theorem

Under exactly the source-locked premises of `T-105210`,

\[
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{H_0-279/140000}
{1-c_{280}/280}
>
0.67300965,
\]

where

\[
c_{280}
=
2\sqrt{726237/700000}-1+2603/700000.
\]

## Proof

Let \(G\) be a 280-point Gram block, let
\(E=\operatorname{tr}(G-I)^2\), and let
\(\Delta=\operatorname{tr}\Psi(G)\). The pinned seven-gap certificate gives

\[
E+\operatorname{span}(G)/500\ge2603/2500.
\]

Because this pressure is below \(2\), the only spectral configuration that
can reduce \(\Delta\) below \(E\) has one eigenvalue \(1+a>2\). Trace
conservation and Cauchy--Schwarz force

\[
a^2\le\frac{279}{280}E.
\]

Therefore

\[
\Delta
\ge
E-(a-1)^2
\ge
2\sqrt{\frac{279}{280}E}-1+\frac E{280}.
\]

The nonnegative span term is incorporated by monotonicity of the exact
envelope, yielding

\[
\Delta(G)+\operatorname{span}(G)/500\ge c_{280}.
\]

Pinch the global Gram into consecutive 280-point blocks and average over all
280 offsets. This gives

\[
\Delta(M)\ge(c_{280}/280)S-(279/140000)N-o(N).
\]

Finally use

\[
S\ge H_0N+\Delta(M)-o(N)
\]

and rearrange. All numerical statements are evaluated using the same pinned
interval for \(H_0\) as `T-105210`. No new external finite certificate is
claimed.
