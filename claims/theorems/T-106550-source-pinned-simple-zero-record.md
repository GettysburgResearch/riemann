# T-106550 — A source-pinned 67.3009652279% simple-zero record

Claim ID: `T-106550`  
Status: **PROPOSED UNCONDITIONAL THEOREM; SAME EXTERNAL FINITE CERTIFICATE, INDEPENDENT REVIEW PENDING**  
Created: 2026-08-25  
Depends on: `L-105210`, `L-106550`, `L-106551`; pinned Anthropic Theorem D normalization  
RH status: **unproved**

Let

\[
H_0=
\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right).
\]

Assume the same analytic and zero-side inputs pinned in `T-105210`, and the
same seven-gap Arb certificate pinned at

```text
ainta/zeta-simple-zeros
040c5e899e658aed7b56a2a87f501798fe10761d
```

No new numerical certificate is assumed.

Put

\[
c_{280}
=
2\sqrt{\frac{726237}{700000}}
-1+\frac{2603}{700000}.
\]

Then

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{
H_0-\dfrac{279}{140000}
}{
1-\dfrac{c_{280}}{280}
}
=
0.6730096522791369\ldots .
}
\tag{T-106550.1}
\]

In particular,

\[
\boxed{
\liminf
\frac{N_0^s(T,2T)}{N(T,2T)}
>
0.67300965.
}
\tag{T-106550.2}
\]

## Deduction

The stability-enhanced rank--inertia inequality gives

\[
S\ge H_0N+\Delta(M)-o(N).
\]

`L-106551` gives

\[
\Delta(M)
\ge
\frac{c_{280}}{280}S
-\frac{279}{140000}N
-o(N).
\]

Substitution gives

\[
\left(1-\frac{c_{280}}{280}\right)S
\ge
\left(H_0-\frac{279}{140000}\right)N
-o(N),
\]

which is (T-106550.1).

Using the same pinned interval

\[
0.67250070367941164
\le H_0\le
0.67250070367941166,
\]

the new lower-bound interval is

\[
0.6730096522791369062\ldots
\le B_{280}\le
0.6730096522791369264\ldots .
\]

The lower endpoint exceeds the upper endpoint of the `T-105210` bound by more
than

\[
1.1243513571\times10^{-6}.
\]

## Scope

This is a proposed computer-assisted unconditional theorem with exactly the
same external trust boundary as `T-105210`. The present packet proves the new
finite-dimensional spectral conversion and global averaging. It does not
rerun the external Arb certificate and does not prove ninety percent, density
one, or RH.
