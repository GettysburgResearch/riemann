# L-97630 — Corrected all-real `P_61` scalar bias from cutoff 239

Claim ID: `L-97630`  
Status: **RECONSTRUCTED CANDIDATE STATEMENT; ORIGINAL FULL EVIDENCE NOT INCLUDED**  
RH status: **not assumed**

With the definitions in `R-97630`,
\[
\boxed{F(x)\ge0\qquad(1\le x<239),}
\tag{L-97630.1}
\]
and
\[
\boxed{
\frac1{40}M(x)\le F(x)\le\frac18M(x)
\qquad(x\ge239).
}
\tag{L-97630.2}
\]

The integer `239` is the smallest cutoff surviving the directed integer sweep.

## Exact coefficient reduction

For any integer sequence `b(n)`, define
\[
\mathscr H_b(x)=\sum_{n\ge1}\frac{b(n)}{\sqrt n}H_x(n).
\]
Finite divisor switching gives
\[
F(x)=\mathscr H_f(x),\qquad M(x)=\mathscr H_m(x),
\]
where
\[
f=q_**\prod_{p\le61}(\delta_1-\delta_p),\qquad
m=q_**\prod_{p\le61}(\delta_1+\delta_p).
\]
For integer `N` and `K=floor(N/4)`,
\[
\mathscr H_b(N)
=(\log4)\sum_{n\le K}\frac{b(n)}{\sqrt n}
+(\log N)\sum_{K<n\le N}\frac{b(n)}{\sqrt n}
-\sum_{K<n\le N}\frac{b(n)\log n}{\sqrt n}.
\tag{L-97630.3}
\]

Every activation or saturation breakpoint is an integer (`n` or `4n`).
On every cell `N<x<N+1`, each quantity in (L-97630.1)–(L-97630.2)
is affine in `log x`; endpoint signs therefore control the complete real cell.

## Directed finite range reported by the unavailable original packet

The quoted digest reports a 256-bit outward-rounded verification through
`2,500,000`:

```text
F(N) >= 0,                         1 <= N <= 238;
40F(N)-M(N) > 0,                 239 <= N <= 2,500,000;
M(N)-8F(N) > 0,                  239 <= N <= 2,500,000;
40F(184)-M(184) < -18.11;
last failing integer endpoint = 238.
```

## Analytic tail

The positive source satisfies
\[
\boxed{
12\sqrt x-19\le A_*(x)\le12\sqrt x-9
\qquad(x\ge1).
}
\tag{L-97630.4}
\]
For `x>=16`, this follows from the exact scale-four integral representation and
a square-root harmonic estimate. The compact range `1<=x<=16` is enclosed by
outward-rounded interval subdivision.

For the lower inequality use `a_d=40\mu(d)-1`; for the upper inequality use
`a_d=1-8\mu(d)`. The active divisor set changes only at `x=2d`. On each interval
between consecutive thresholds, the resulting lower envelope is affine in
`sqrt x`, so checking its endpoints closes the entire tail.

The reconstructed `src/certify.cpp` does not implement this tail and does not
execute the reported sweep through `2,500,000`; it checks only the `x=184`
witness and endpoints `67..238`. Therefore this file records the candidate
statement and its intended proof contract, not a locally complete replay.
