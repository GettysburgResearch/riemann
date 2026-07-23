# T-2801 — D-0801 admissibility and exact Guinand–Weil dictionary

Claim ID: T-2801  
Title: The piecewise autocorrelation carrier is admissible and its exact source signs are `A + R - S`  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: the classical Guinand–Weil explicit formula in the normalization displayed below  
Scope: D-0801 for the Riemann zeta function  
Related counterexample candidates: any D-0801 fixed-vector certificate

## Fourier and zero conventions

Use

\[
 \widehat g(\xi)=\int_{\mathbb R}g(t)e^{-2\pi i t\xi}\,dt,
 \qquad
 g(z)=\int_{\mathbb R}\widehat g(\xi)e^{2\pi i z\xi}\,d\xi.
\]

For a nontrivial zero `rho` of `zeta`, define its Weil coordinate

\[
 z_\rho=\frac{\rho-1/2}{i}.
\]

Thus RH is exactly the assertion that every `z_rho` is real.

Put

\[
 h_+(t)=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi.
\]

The explicit formula used in this theorem is

\[
 \boxed{
 \sum_\rho g(z_\rho)
 =2g(i/2)
 +\frac1{2\pi}\int_{\mathbb R}h_+(t)g(t)\,dt
 -\frac1\pi\sum_{n=2}^{\infty}
  \frac{\Lambda(n)}{\sqrt n}
  \widehat g\!\left(\frac{\log n}{2\pi}\right),}
\]

for even admissible `g`, with zeros counted with multiplicity. The zero sum is
absolutely convergent for the class verified below.

## Statement

Fix `c>1`, let

\[
 L=\log c,\qquad \Delta=\frac{L}{2\pi},
\]

and use any finite D-0801 piecewise-constant envelope `w_v` on
`I=[-Delta/2,Delta/2]`, with any real carrier `T`. Then:

1. `g_{T,v}` is an admissible Guinand–Weil test function in the displayed
   normalization: it is even and entire of exponential type at most `L`, its
   Fourier transform is continuous with support in `[-Delta,Delta]`, and on
   every fixed horizontal strip
   \[
   g_{T,v}(z)=O((1+|z|)^{-2}).
   \]
2. The zero sum `sum_rho g_{T,v}(z_rho)` converges absolutely.
3. The infinite prime sum truncates exactly to prime powers `q<=c`; a term at
   `q=c` is zero because the autocorrelation vanishes at the support endpoint.
4. With the normalized D-0801 Gram value
   \[
   h\,v^*v,\qquad h=\Delta/K,
   \]
   and with `S_K(T,c)` as in L-0801, the exact fixed-vector formula is
   \[
   \boxed{
   \sum_\rho g_{T,v}(z_\rho)
   =\mathcal A(g_{T,v})+\mathcal R(g_{T,v})
    -h\,v^*S_K(T,c)v,}
   \]
   where
   \[
   \mathcal A(g)=\frac1{2\pi}\int_{\mathbb R}h_+(t)g(t)\,dt,
   \qquad
   \mathcal R(g)=2g(i/2).
   \]
5. Consequently, if a complete certified interval proves the right side is
   strictly negative for one nonzero exact vector, then RH is false.

The prime sign is negative. The pole sign is positive. The archimedean density
is exactly `h_+(t)/(2*pi)`. The prime frequency is exactly
`log(q)/(2*pi)`.

## Proof

### 1. Fourier transform and compact support

D-0801 defines

\[
 W_v(z)=\int_Iw_v(x)e^{2\pi izx}\,dx,
 \qquad
 W_v^\#(z)=\overline{W_v(\overline z)},
\]

and

\[
 g_{T,v}(z)=\frac12\left\{
 W_v(z-T)W_v^\#(z-T)+
 W_v(-z-T)W_v^\#(-z-T)
 \right\}.
\]

The transform of `W_v` is `w_v`; the transform of `W_v^#` is
`x -> conjugate(w_v(-x))`. Their product therefore has transform the compact
autocorrelation

\[
 R_v(\xi)=\int_{\mathbb R}w_v(x)\overline{w_v(x-\xi)}\,dx.
\]

Translation by `T` multiplies by `exp(-2*pi*i*T*xi)`, while the even
symmetrization takes the real part. Hence

\[
 \widehat g_{T,v}(\xi)
 =\operatorname{Re}\left(e^{-2\pi iT\xi}R_v(\xi)\right).
\]

Since `supp(w_v) subset I`, the difference support is
`I-I=[-Delta,Delta]`.

### 2. Admissibility of the piecewise family

For a finite piecewise-constant `w_v`, the autocorrelation `R_v` is continuous
and piecewise linear. It vanishes at `+-Delta`. Its derivative is piecewise
constant with finitely many jumps. Multiplication by the smooth carrier phase
and taking the real part preserves:

- continuity;
- compact support;
- endpoint vanishing;
- piecewise `C^1` regularity;
- bounded variation of the derivative after zero extension.

Fourier inversion makes `g_{T,v}` entire of exponential type at most
`2*pi*Delta=L`. On a strip `|Im z|<=Y`, one ordinary integration by parts uses
the endpoint vanishing. A second integration by parts in the Stieltjes sense
against the finite signed measure `d(hat(g)')` gives, for `|z|>=1`,

\[
 |g_{T,v}(z)|
 \le\frac{e^{2\pi Y\Delta}}{(2\pi|z|)^2}
 \operatorname{Var}\!\left((\widehat g_{T,v})'\right).
\]

Thus `g=O((1+|z|)^-2)` uniformly on each fixed horizontal strip. This is the
standard Bombieri/Guinand–Weil admissibility class: even, entire of finite
exponential type, continuous compactly supported Fourier transform, and
`O((1+|z|)^(-1-delta))` strip decay with `delta=1`.

No mollification is required for this class. The cell jumps occur in `w_v`, not
in `hat(g)`: autocorrelation has already raised the Fourier-side regularity to
continuous piecewise linear.

### 3. Absolute convergence of the zero sum

Every nontrivial zero lies in `0<Re(rho)<1`, hence

\[
 |\operatorname{Im}z_\rho|<1/2.
\]

The strip bound therefore gives

\[
 |g(z_\rho)|\ll(1+|\operatorname{Re}z_\rho|)^{-2}.
\]

The local Riemann–von Mangoldt estimate gives `O(log(2+t))` zeros with ordinate
in a unit interval near height `t`. Therefore

\[
 \sum_\rho|g(z_\rho)|
 \ll1+\sum_{m>=1}\frac{\log(2+m)}{m^2}<\infty.
\]

This also removes every ordering ambiguity in the nonnegative RH implication.

### 4. Exact source identification

Apply the displayed explicit formula to `g_{T,v}`.

Because `hat(g)` is even, the usual pair of prime frequencies `+-log(n)/(2*pi)`
combines to

\[
 -\frac1\pi\frac{\Lambda(n)}{\sqrt n}
 \widehat g\!\left(\frac{\log n}{2\pi}\right).
\]

If `n>c`, then `log(n)/(2*pi)>Delta`, so the term is zero. If `n=c`, the
frequency is the support endpoint and the autocorrelation is zero. Thus the
prime side is the exact finite sum

\[
 -\frac1\pi\sum_{q=p^a\le c}
 \frac{\Lambda(q)}{\sqrt q}
 \widehat g\!\left(\frac{\log q}{2\pi}\right).
\]

L-0801 proves that, after division by the cell Gram factor `h`, the positive
quantity without the leading minus sign is exactly `v^*S_K(T,c)v`. Hence the
prime contribution is `-h v^*S_Kv`.

The two polar evaluations in the unsymmetrized formula are `g(i/2)` and
`g(-i/2)`. Evenness gives `2g(i/2)` with a positive sign. The gamma-factor term
is exactly the displayed `h_+/(2*pi)` integral. This proves the boxed identity
and fixes all signs and `2*pi` factors.

### 5. Counterexample implication

Assume RH. Every `z_rho` is real. D-0801 gives

\[
 g_{T,v}(t)=\frac12\left(
 |W_v(t-T)|^2+|W_v(-t-T)|^2
 \right)\ge0
\]

for real `t`. Absolute convergence then implies

\[
 \sum_\rho g_{T,v}(z_\rho)\ge0.
\]

The contrapositive proves that a strict certified negative exact source value
falsifies RH.

## Normalization fingerprint

The machine-readable fingerprint in X-2803 binds the proof and every future
producer to:

```text
Fourier forward exponent      -2*pi*i*t*xi
Fourier inverse exponent      +2*pi*i*z*xi
zero coordinate               (rho-1/2)/i
prime frequency               log(q)/(2*pi)
prime coefficient/sign        -Lambda(q)/(pi*sqrt(q))
pole term/sign                 +2*g(i/2)
archimedean density/sign       +(Re digamma(1/4+i*t/2)-log(pi))/(2*pi)
exact matrix convention        A + R - h*S_K
```

Any mismatch is a different theorem and must fail closed.

## Source audit

Primary interfaces inspected for this normalization:

- Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of
  prime numbers, I* (2000), especially the admissible test class and quadratic
  functional;
- Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order
  for the truncated Weil quadratic form*, arXiv:2607.02828 (2026), Lemma 2.2
  and Theorem 2.5;
- the completed-zeta convention D-0301.

The theorem above independently checks the transport from D-0801 to that
class and the source signs; it does not reprove the classical explicit formula
from contour integration.

## Analytic domain audit

- The digamma argument `1/4+it/2` avoids all poles for real `t`.
- `g` is entire; no logarithmic branch is used.
- The prime side is finite.
- The archimedean integral converges absolutely because `h_+(t)=O(log(2+|t|))`
  and `g(t)=O(t^-2)`.
- Zero multiplicities are retained.
- The pole at `s=1` and trivial zeros are represented by the pole and gamma
  terms, not inserted into the nontrivial zero sum.

## Gap audit

1. The classical Guinand–Weil formula is an imported theorem, not reproved here.
2. A producer must use the exact D-0801 function encoded by its frozen vector;
   another Toeplitz orientation is not interchangeable.
3. A complete prime stream with an incorrect phase or knot assignment does not
   satisfy the boxed identity.
4. A negative quantitative checker verdict still requires this normalization
   fingerprint and theorem to be reviewed independently.
5. Positivity of one fixed vector proves nothing about RH.

## Adversarial tests

X-2803 rejects every single-field mutation of the normalization fingerprint,
including prime sign, pole sign, `2*pi` frequency, zero coordinate, Fourier
orientation, and matrix assembly order.

## Remaining uncertainty

No unresolved admissibility or source-sign step is known after accepting the
classical explicit formula. Independent review should reconstruct the Fourier
transform of the Schwarz product and compare the displayed formula with a
second primary normalization before status promotion.

## Suggested next attack

Attach the X-2803 fingerprint digest to every alpha, vector, phase, prime-shard,
and final fixed-vector artifact. The remaining quantitative work is then the
frozen-vector complete prime interval, not the logical formula interface.
