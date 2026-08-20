# R-100160 — Naive critical upper-ideal positivity is false

Status: **REFUTED EXACTLY AT FINITE-CUBE LEVEL**  
Created: 2026-08-20  
RH status: **unproved**

For the critical quadratic Peano kernel, write

\[
\kappa(t)=\begin{cases}2t-t^2,&t\le1,\\1,&t\ge1.\end{cases}
\]

and extend the fully-active polynomial formula beyond activation. The correction for a source product `n>x` is

\[
\boxed{
d_x(n)=x^{-3/2}{(\sqrt{n/x}-1)^2\over(n/x)^{3/2}}>0.
}
\]

Thus the partial-activation critical cube is the explicit fully-active Euler product plus the signed upper-ideal correction

\[
\sum_{n_A>x}(-1)^{|A|}d_x(n_A).
\]

Although `d_x(n)` eventually decreases under multiplication by every rough prime, it grows immediately above activation. The worst-prime monotonicity threshold is exact:

\[
\sqrt{n/x}\ge 1+67^{-1/2}+67^{-1/4}.
\]

The corresponding multiplicative collar has width

\[
\left(1+67^{-1/2}+67^{-1/4}\right)^2<2.17<67,
\]

so one Hasse chain contains at most one collar vertex. This fact is insufficient to orient the signed upper ideal.

A direct finite-cube counterexample is obtained from the eight rough labels

```text
67, 71, 73, 79, 83, 89, 97, 101
```

at `x=144740878`. Exact/rational certification should be used before promoting numerical values, but high-precision evaluation gives the signed correction approximately

```text
-6.5694354265...
```

with the debt dominated by odd five-label products. Hence neither collar uniqueness nor one-step descendant pairing proves critical positivity.

This refutes the proposed shortcut

```text
fully-active critical positivity
 + positive activation correction
 -> global critical positivity.
```

The valid exact prefix/future-tail decomposition of `L-100160` survives. The remaining critical theorem must exploit cancellation across more than one parity level, or settle only the subpower negative-mass estimate rather than pointwise positivity.
