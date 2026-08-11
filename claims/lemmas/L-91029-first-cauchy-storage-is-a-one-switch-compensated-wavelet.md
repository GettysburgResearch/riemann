# L-91029 — The first Cauchy storage residual is a three-scale one-switch compensated wavelet

Claim ID: `L-91029`  
Status: **EXACT FOURIER/SIGN THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91020`  
RH status: **unproved**

## 1. Three-scale partial fraction collapse

Retain

\[
 n_a(u)=\frac{a^4}{(a^2+u^2)^2}
\]

and the first stored Cauchy innovation

\[
 \mathfrak D_a(u)
 =\bigl[n_{2a}(u)-n_a(u)\bigr]
 -\frac1{16}\bigl[n_{4a}(u)-n_{2a}(u)\bigr].
\]

The rational function of `L-91020` collapses exactly to

\[
 \boxed{
 \mathfrak D_a(u)
 =-n_a(u)+\frac{17}{16}n_{2a}(u)-\frac1{16}n_{4a}(u).
 }
 \tag{L-91029.1}
\]

Equivalently, with `y=u^2/a^2`,

\[
 \boxed{
 F_1(y)
 =-\frac1{(y+1)^2}
 +\frac{17}{(y+4)^2}
 -\frac{16}{(y+16)^2}.
 }
 \tag{L-91029.2}
\]

This is the exact factor-sixteen three-scale normal form.

## 2. Physical kernel

Use the Fourier convention

\[
 \widehat k(u)=\int_{\mathbb R}k(t)e^{-iut}\,dt.
\]

The standard transform

\[
 \mathcal F^{-1}\frac1{(u^2+c^2)^2}(t)
 =\frac{1+c|t|}{4c^3}e^{-c|t|}
\]

gives

\[
 \boxed{
 \begin{aligned}
 k_a(t)=a\Bigg[&-\frac14(1+a|t|)e^{-a|t|}\\
 &+\frac{17}{32}(1+2a|t|)e^{-2a|t|}\\
 &-\frac1{16}(1+4a|t|)e^{-4a|t|}\Bigg],
 \end{aligned}
 }
 \tag{L-91029.3}
\]

with

\[
 \widehat{k_a}(u)=\mathfrak D_a(u).
\]

The coefficients are supported at the three exact scales `a,2a,4a`.

## 3. Exact compensation

Since `F_1(0)=0`,

\[
 \boxed{
 \int_{\mathbb R}k_a(t)\,dt=0.
 }
 \tag{L-91029.4}
\]

Moreover

\[
 k_a(0)=\frac{7a}{32}>0,
\]

whereas

\[
 k_a(t)\sim-\frac a4(1+a|t|)e^{-a|t|}
 \qquad(|t|\to\infty).
\]

Thus the physical kernel is genuinely compensated: a positive central lobe is balanced by a negative exponential tail.

## 4. Exactly one positive sign change

By scaling it suffices to set `a=1`. Put

\[
 G(t)=32e^t k_1(t)
 =-8(1+t)+17(1+2t)e^{-t}-2(1+4t)e^{-3t}.
\]

The equation `G(t)=0` is equivalent to

\[
 H(t)=8(1+t)e^t+2(1+4t)e^{-2t}-17(1+2t)=0.
 \tag{L-91029.5}
\]

One has

\[
 H(0)=-7,
 \qquad
 H(t)\longrightarrow+\infty.
\]

Also

\[
 H''(t)=8(3+t)e^t+(16t-20)e^{-2t}>0
 \qquad(t\ge0).
\]

Indeed, for `0<=t<=5/4`, the first term is at least `24` and the second at least `-20`; for `t>=5/4`, both terms are nonnegative. Hence `H'` is strictly increasing. Since `H'(0)=-12`, the function first decreases and then increases, crossing zero exactly once.

Therefore there is one number

\[
 \tau_*=1.164606978873629\ldots
\]

such that

\[
 \boxed{
 k_a(t)>0\quad(0\le|t|<\tau_*/a),
 \qquad
 k_a(t)<0\quad(|t|>\tau_*/a).
 }
 \tag{L-91029.6}
\]

The decimal value is reconnaissance only; uniqueness and the sign pattern are exact.

## 5. Positive stop-loss primitive

Define

\[
 K_a(T)=\int_0^T k_a(t)\,dt.
\]

The kernel is positive before its unique switch, negative after it, and has zero half-line integral by evenness and (L-91029.4). Consequently

\[
 \boxed{
 K_a(T)\ge0
 \qquad(T\ge0),
 }
 \tag{L-91029.7}
\]

with strict positivity for finite `T>0` and `K_a(T)->0` as `T->infinity`.

Thus the first innovation is a one-switch compensated wavelet whose stop-loss primitive is positive.

## 6. Consequence for the arithmetic attack

The first Cauchy innovation no longer needs to be treated as a generic rational filter. In the prime explicit formula it has:

```text
three fixed horizontal scales a,2a,4a;
one central positive lobe;
one negative tail;
zero total mass;
a positive cumulative/stop-loss primitive.
```

This is precisely the geometry suited to Abel summation against a cumulative source discrepancy. A conclusion-producing proof must identify the completed prime/pole cumulative source against which (L-91029.7) may be used without discarding vertical phases.

No such completed Abel pairing, and no RH conclusion, is asserted here.