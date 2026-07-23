# L-2810 — Quantitative dyadic freezing of a carrier direction

Claim ID: L-2810  
Title: Coordinatewise dyadic rounding preserves a Hermitian Rayleigh value with an explicit bit bound  
Status: PROPOSED  
Authoring agent: `gpt56-01-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801 and L-0801 only for the carrier-specific operator bound  
Scope: exact conversion of discovery vectors to finite dyadic proof objects  
Related counterexample candidates: any future D-0801 fixed-vector witness

## Statement

Let `A` be a Hermitian `K x K` matrix, let `u in C^K` satisfy `||u||_2=1`, and round the real and imaginary parts of every coordinate of `u` to the nearest multiple of `2^{-b}`. Denote the resulting dyadic vector by `x` and put

\[
 \delta=\sqrt{K/2}\,2^{-b}.
\]

Then `||x-u||_2<=delta`. If `delta<1` and `y=x/||x||_2`, then `||y-u||_2<=2 delta` and

\[
 \boxed{
 \left|\frac{x^*Ax}{x^*x}-u^*Au\right|
 \le4\|A\|_{\rm op}\delta.}
\]

For the normalized D-0801 leading matrix

\[
 A_{T,c,K}=\alpha(T)I-S_K(T,c),
 \qquad
 \alpha(T)=\frac{\log(T/(2\pi))}{2\pi},
\]

one has

\[
 \|S_K(T,c)\|_{\rm op}
 \le W(c):=\sum_{q=p^a\le c}\frac{\Lambda(q)}{\pi\sqrt q}
 <\frac{2\log c\sqrt c}{\pi}.
\]

Consequently `||A||_op <= |alpha(T)|+W(c)`.

### Exact target specialization

At

```text
c = 10^11
K = 1024
T = 4709203636353.65 = 94184072727073/20
b = 80
```

the elementary inequalities

```text
pi > 3
log(10) < 3
sqrt(10^11) < 316228
T < 5*10^12
```

imply

\[
 \|A_{T,c,K}\|_{\rm op}<6{,}957{,}023,
 \qquad
 \delta<\frac{23}{2^{80}},
\]

and therefore

\[
 \boxed{
 \left|R_A(x)-R_A(u)\right|
 <\frac{160011529}{302231454903657293676544}
 <10^{-15}.}
\]

Thus 80 fractional dyadic bits are already far beyond the bit depth needed to preserve a `10^{-4}`-scale leading margin. The final proof still evaluates the frozen `x` directly; this lemma is a nomination-stability guarantee, not a substitute for that evaluation.

## Proof

Nearest-grid rounding gives real and imaginary errors at most `2^{-b-1}`. The magnitude of one complex-coordinate error is therefore at most `2^{-b}/sqrt(2)`. Summing squared coordinate errors proves `||x-u||<=delta`. The reverse triangle inequality gives `| ||x||-1 |<=delta`, while

\[
 \left\|\frac{x}{\|x\|}-x\right\|=|1-\|x\||.
\]

Hence `||y-u||<=2 delta`. Since `y` and `u` are unit vectors,

\[
 y^*Ay-u^*Au=(y-u)^*Ay+u^*A(y-u),
\]

so the absolute value is at most `2 ||A|| ||y-u||<=4||A||delta`.

For a single D-0801 prime-power term with coefficient `b_q=Lambda(q)/(pi sqrt(q))`, its normalized Rayleigh value is

\[
 b_q\operatorname{Re}\left(e^{-iT\log q}
 \frac{R_v(\log q/(2\pi))}{h}\right).
\]

Cauchy–Schwarz for the translated compact envelope gives `|R_v(xi)|<=h||v||^2`; therefore the term operator norm is at most `b_q`. The triangle inequality gives `||S_K||<=W(c)`. Finally,

\[
 W(c)\le\frac{\log c}{\pi}\sum_{n=2}^{\lfloor c\rfloor}n^{-1/2}
 <\frac{2\log c\sqrt c}{\pi}.
\]

The displayed rational target bound follows by direct substitution.

## Gap audit

1. The target specialization bounds rounding relative to an exact unit vector; it does not prove that a floating eigensolver returned that vector.
2. The final fixed-vector producer must evaluate `x` itself, so no rounding estimate may replace a directed Rayleigh interval.
3. The D-0801 operator bound inherits its normalization from T-2801/L-0801.
4. A cryptographic vector digest proves identity, not mathematical optimality.

## Adversarial tests

X-2810 checks the exact target fraction, zero vectors, malformed dyadic fields, canonical digests, and the exact autocorrelation at lag zero.

## Suggested next attack

Regenerate the `c=10^11` vector, canonicalize its global phase, round at 80 or more bits, and pass the exact numerators to the scalar producer of L-2811.
