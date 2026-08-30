# R-104512 — Proportion-only reverse Rolle and open-side flux are insufficient

Claim ID: `R-104512`  
Status: **EXACT FIREWALLS**  
Created: 2026-08-22  
RH status: **not assumed**

## 1. No source-free positive proportion constant

There is no universal constant `c>0` for which

\[
\text{real-zero proportion of }f'
\quad\Longrightarrow\quad
c\times\text{that proportion for }f
\]

holds for arbitrary real entire functions, even after imposing evenness,
order one and Cartwright growth.

The polynomial

\[
p(x)=x^4-2x^2+2
\]

has no real zero, whereas

\[
p'(x)=4x(x^2-1)
\]

has only real zeros.

The even Cartwright entire function

\[
f(z)=2+\cos z
\]

has no real zero because `f(x)>=1` for real `x`, whereas

\[
f'(z)=-\sin z
\]

has only real zeros.  Thus derivative line proportion `1` can coexist with
parent line proportion `0`.

Any positive quantitative descent theorem must therefore use structure
specific to Xi, not only:

```text
real-entire symmetry;
Cartwright growth;
evenness;
or a high derivative line proportion.
```

## 2. The vertical-side integral is not an index by itself

For a regular rectangle `Omega`, the argument principle applies to the complete
closed boundary:

\[
{1\over2\pi i}\int_{\partial\Omega}{G'(z)\over G(z)}\,dz
\in\mathbb Z.
\]

It does not apply to the two vertical sides alone.  Even for

\[
G(z)=z-a,
\]

the contribution of one vertical segment from `T-iH` to `T` is

\[
{1\over2\pi i}
\log {T-a\over T-a-iH},
\]

which is generically neither real nor integral.

Therefore the quantity called `VFLUX104515` in the first version of
`L-104515` cannot be treated as an integer merely because the horizontal
segments are zero-free.  Zero-freeness gives a continuous logarithm on those
segments; it does not make their argument variation vanish.

The correct exterior charge is the integral over the **entire complementary
boundary**

\[
\partial_{\rm ext}\Omega
=
\partial\Omega\setminus (a,b),
\]

namely the two vertical sides together with the lower horizontal side.  This is
used in `L-104518`.

## 3. Consequence

Two tempting shortcuts are bindingly rejected:

```text
global derivative percentages alone          INSUFFICIENT;
vertical-side winding without closure         NOT AN INTEGER INDEX.
```

The surviving quantitative descent in `L-104517` is Xi-specific and comes from
the positive Fourier kernel plus uniform saddle concentration.  The surviving
last-defect boundary theorem in `L-104518` uses a closed contour decomposition.
