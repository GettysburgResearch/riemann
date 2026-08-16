# L-93261 — The Q4 cubic is a minimal two-switch kernel with a double Mellin zero

Claim ID: `L-93261`  
Status: **PROPOSED COMPLETE EXACT KERNEL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: the reconstructed kernel `K` of `L-93250`  
Scope: scalar kernel geometry only; no prime estimate or RH conclusion

## 1. The ordinary-prime Q4 kernel

Extend

\[
K(x)={x(1-x)(2x-1)\over3}
\]

by zero outside `[0,1]`, and put

\[
\boxed{
W(x)=K(x)-4K(4x).
}
\tag{L-93261.1}
\]

Then

\[
W(x)=
\begin{cases}
5x-63x^2+170x^3,&0\le x\le1/4,\\
(-x+3x^2-2x^3)/3,&1/4\le x\le1,\\
0,&x>1.
\end{cases}
\tag{L-93261.2}
\]

The two pieces agree at `x=1/4`, where both equal `-1/32`.

## 2. Exactly two sign changes

The first piece factors as

\[
x(170x^2-63x+5).
\]

Its roots are

\[
\alpha={63-\sqrt{569}\over340},
\qquad
\alpha'={63+\sqrt{569}\over340}.
\]

Exactly one lies in `(0,1/4)`, namely `alpha`; the second exceeds `1/4`.
The second piece has its only interior zero at `1/2`. Consequently

\[
\boxed{
W>0\text{ on }(0,\alpha),\quad
W<0\text{ on }(\alpha,1/2),\quad
W>0\text{ on }(1/2,1).
}
\tag{L-93261.3}
\]

Thus the Q4 cubic has exactly two sign changes.

## 3. Double zero at the main Mellin pole

For `Re s>-1`,

\[
\boxed{
\widehat W(s)
=(1-4^{1-s})\widehat K(s)
=(1-4^{1-s}){s-1\over3(s+1)(s+2)(s+3)}.
}
\tag{L-93261.4}
\]

Hence `What` has a zero of exact order two at `s=1`. Equivalently,

\[
\boxed{
\int_0^1W(x)dx=0,
\qquad
\int_0^1W(x)\log x\,dx=0,
}
\tag{L-93261.5}
\]

while

\[
\widehat W''(1)={\log4\over36}\ne0.
\tag{L-93261.6}
\]

The first vanishing moment cancels the uniform prime density. The second is the
extra Q4 cancellation that makes the elementary Mobius forcing below decay by
one full endpoint power.

## 4. One-switch double-zero no-go

Let `U` be a nonzero integrable real kernel. Suppose that for some `a in (0,1)`

```text
U(x)>=0 for 0<x<a,
U(x)<=0 for a<x<1,
int_0^1 U(x) dx = 0.
```

Then

\[
\int_0^1U(x)\log x\,dx
=
\int_0^1U(x)(\log x-\log a)dx<0.
\tag{L-93261.7}
\]

Indeed both pieces of the final integrand are nonpositive and at least one has
positive measure. Therefore a nontrivial one-switch kernel cannot have both
Mellin moments in (L-93261.5).

It follows that **two sign changes are minimal** for any scalar real kernel
which simultaneously:

1. cancels the main prime density;
2. cancels the logarithmic first variation at `s=1`;
3. is not identically zero.

The cubic Q4 kernel attains this minimum.

## 5. Consequence for kernel redesign

A scalar redesign can simplify `W` to one switch only by spending one of the two
zeros at `s=1`. That trade removes the bottom-free forcing gain used by
`L-93265`. A successful one-switch continuation therefore needs a genuinely
vector, bilinear, or nonlocal cancellation; it cannot be obtained by a
one-component sign rearrangement preserving both moments.

## 6. Boundary

```text
piecewise cubic formula                 EXACT
two sign changes                        EXACT
double Mellin zero at s=1               EXACT
one-switch + double-zero scalar kernel  IMPOSSIBLE
prime cancellation estimate             NOT PROVED
RH                                      UNPROVED
```
