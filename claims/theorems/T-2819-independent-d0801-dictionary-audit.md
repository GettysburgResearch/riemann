# T-2819 — Independent reconstruction of the D-0801 Guinand–Weil implication

Claim ID: T-2819  
Title: Independent transform, admissibility, normalization, and RH-implication audit of T-2801  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: the classical even Guinand–Weil explicit formula stated in this file; D-0801; L-0801  
Scope: analytic theorem interface for every D-0801 fixed-vector certificate  
Related counterexample candidates: any future strict negative D-0801 certificate

## Verdict

The analytic content of T-2801 **passes** this independent reconstruction:

1. the Fourier transform of the Schwarz-product carrier is the stated modulated autocorrelation;
2. the even symmetrization is real, even, compactly supported, and nonnegative on the real axis;
3. the piecewise-constant envelope produces a Guinand–Weil-admissible test with `O(|z|^-2)` horizontal-strip decay;
4. the zero sum is absolutely convergent;
5. the exact signs and constants are
   \[
   \boxed{\mathcal A+\mathcal R-hv^*S_Kv};
   \]
6. a strict negative complete value contradicts RH.

This audit recommends promotion of T-2801 from an unreviewed proposal to a reviewed analytic theorem after repository integration. It does **not** independently reproduce any production prime sum or numerical sign.

## Normalization

Use

\[
 \widehat g(\xi)=\int_{\mathbb R}g(t)e^{-2\pi it\xi}\,dt,
 \qquad
 g(z)=\int_{\mathbb R}\widehat g(\xi)e^{2\pi iz\xi}\,d\xi,
\]

and

\[
 z_\rho=\frac{\rho-1/2}{i}.
\]

The classical even explicit formula in this normalization is

\[
 \begin{aligned}
 \sum_\rho g(z_\rho)
 ={}&g(i/2)+g(-i/2)\\
 &+\frac1{2\pi}\int_{\mathbb R}
 \left(\operatorname{Re}\psi\left(\frac14+\frac{it}{2}\right)-\log\pi\right)
 g(t)\,dt\\
 &-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \left[
 \widehat g\left(\frac{\log n}{2\pi}\right)
 +\widehat g\left(-\frac{\log n}{2\pi}\right)
 \right].
 \end{aligned}
\]

Zeros are counted with multiplicity. This is the only imported theorem in the reconstruction.

## Statement

Let

\[
 I=[-\Delta/2,\Delta/2],
 \qquad
 \Delta=\frac{\log c}{2\pi},
\]

and let `w` be any finite complex piecewise-constant function supported on `I`. Define

\[
 W(z)=\int_Iw(x)e^{2\pi izx}\,dx,
 \qquad
 W^\#(z)=\overline{W(\overline z)},
\]

\[
 A_T(z)=W(z-T)W^\#(z-T),
 \qquad
 g_T(z)=\frac12\bigl(A_T(z)+A_T(-z)\bigr).
\]

Then `g_T` is admissible for the displayed explicit formula and

\[
 \widehat g_T(\xi)
 =\operatorname{Re}\left(e^{-2\pi iT\xi}R_w(\xi)\right),
 \qquad
 R_w(\xi)=\int_{\mathbb R}w(x)\overline{w(x-\xi)}\,dx.
\]

For the equal-cell D-0801 vector `v`, cell width `h=Delta/K`, and L-0801 Toeplitz matrix `S_K(T,c)`,

\[
 \boxed{
 \sum_\rho g_T(z_\rho)
 =\mathcal A(g_T)+\mathcal R(g_T)-h\,v^*S_K(T,c)v,
 }
\]

where

\[
 \mathcal R(g)=2g(i/2)
\]

and

\[
 \mathcal A(g)=\frac1{2\pi}\int_{\mathbb R}
 \left(\operatorname{Re}\psi\left(\frac14+\frac{it}{2}\right)-\log\pi\right)
 g(t)\,dt.
\]

If the right side has a certified strict negative upper endpoint for one nonzero exact vector, RH is false.

## Proof

### 1. Transform of the Schwarz product

Changing variables in the Schwarz reflection gives

\[
 W^\#(z)
 =\int_I\overline{w(-y)}e^{2\pi izy}\,dy.
\]

Thus `W` and `W#` are inverse Fourier transforms of `w(x)` and `conj(w(-x))`. Translation by `T` in the entire variable multiplies each inverse-transform density by `e^{-2*pi*i*T*x}`. The transform of their product is therefore

\[
 \begin{aligned}
 \widehat A_T(\xi)
 &=e^{-2\pi iT\xi}
 \int_{\mathbb R}w(x)\overline{w(x-\xi)}\,dx\\
 &=e^{-2\pi iT\xi}R_w(\xi).
 \end{aligned}
\]

Since

\[
 R_w(-\xi)=\overline{R_w(\xi)},
\]

the transform of `A_T(-z)` is `overline(hat(A_T)(xi))`. Hence

\[
 \widehat g_T(\xi)=\operatorname{Re}\widehat A_T(\xi),
\]

which proves the formula and shows that `hat(g_T)` is real and even.

The support of `R_w` is contained in the difference set

\[
 I-I=[-\Delta,\Delta].
\]

At `|xi|=Delta`, the two supports overlap only in a null endpoint, so `R_w(xi)=0`.

### 2. Entirety, symmetry, and real-axis positivity

Compact support makes `W` and `W#` entire of exponential type at most `pi*Delta`; their products have type at most `2*pi*Delta=log(c)`. The definition immediately gives evenness.

For real `t`,

\[
 A_T(t)=|W(t-T)|^2,
\]

so

\[
 \boxed{
 g_T(t)=\frac12\left(|W(t-T)|^2+|W(-t-T)|^2\right)\ge0.
 }
\]

Moreover `g_T(conj(z))=conj(g_T(z))`; combined with evenness this implies that `g_T(i/2)` is real and `g_T(-i/2)=g_T(i/2)`.

### 3. Horizontal-strip decay

For piecewise-constant `w`, the autocorrelation `R_w` is continuous and piecewise linear. After multiplication by the smooth carrier phase, `f=hat(g_T)` is continuous, compactly supported, vanishes at both endpoints, and has a derivative whose zero extension is of bounded variation.

For `z!=0`, one ordinary integration by parts gives

\[
 g_T(z)
 =-\frac1{2\pi iz}\int_{-\Delta}^{\Delta}f'(\xi)e^{2\pi iz\xi}\,d\xi.
\]

Extend `f'` by zero outside the support. A Stieltjes integration by parts gives

\[
 g_T(z)
 =\frac1{(2\pi iz)^2}
 \int_{\mathbb R}e^{2\pi iz\xi}\,d f'(\xi),
\]

where endpoint jumps of `f'` are included in the finite signed measure `df'`. On `|Im z|<=Y`,

\[
 |g_T(z)|
 \le
 \frac{e^{2\pi Y\Delta}}{(2\pi|z|)^2}
 \operatorname{Var}(f').
\]

Thus

\[
 g_T(z)=O_Y((1+|z|)^{-2}),
\]

which is stronger than the required `O((1+|z|)^(-1-delta))` with `delta>0`.

### 4. Absolute zero-sum convergence

For a nontrivial zero `rho=beta+i*gamma`,

\[
 z_\rho=\gamma-i(\beta-1/2),
\]

so `|Im z_rho|<1/2`. The strip estimate gives

\[
 |g_T(z_\rho)|\ll(1+|\gamma|)^{-2}.
\]

The local Riemann–von Mangoldt estimate places `O(log(2+m))` zeros, counted with multiplicity, in each unit ordinate interval near `m`. Therefore

\[
 \sum_\rho|g_T(z_\rho)|
 \ll1+\sum_{m\ge1}\frac{\log(2+m)}{m^2}<\infty.
\]

### 5. Explicit-formula constants and signs

Because `g_T` and `hat(g_T)` are even, the two prime frequencies in the classical formula combine to

\[
 -\frac1\pi\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 \widehat g_T\left(\frac{\log n}{2\pi}\right).
\]

The minus sign is therefore forced, not conventional. The pole evaluations combine as

\[
 g_T(i/2)+g_T(-i/2)=2g_T(i/2)
\]

with positive sign. The gamma density retains the positive coefficient `1/(2*pi)`.

Compact support proves exact prime truncation: if `n>c`, then

\[
 \frac{\log n}{2\pi}>\Delta;
\]

if `n=c`, the frequency is the support endpoint, where `hat(g_T)=0`.

Finally L-0801 defines

\[
 v^*S_K(T,c)v
 =\frac1{h\pi}\sum_{q=p^a\le c}
 \frac{\Lambda(q)}{\sqrt q}
 \widehat g_T\left(\frac{\log q}{2\pi}\right).
\]

Therefore the exact prime contribution is

\[
 -h\,v^*S_K(T,c)v.
\]

This proves the boxed dictionary.

### 6. RH implication

Assume RH. Every `z_rho` is real, so every summand is nonnegative by the real-axis identity. Absolute convergence permits ordinary summation, hence

\[
 \sum_\rho g_T(z_\rho)\ge0.
\]

A certified strict negative exact dictionary value contradicts RH. ∎

## Independent source comparison

The displayed formula was compared against the finite Guinand–Weil dictionary in Akiva Groskin, arXiv:2607.02828 (2026), including its Fourier orientation, zero variable, prime frequency, negative prime sign, positive pole term, and archimedean density. The derivation above does not import that paper's D-0801 transport; it independently reconstructs the transform and admissibility from the piecewise envelope.

## Adversarial audit

The proof fails, as it should, under each of the following mutations:

1. replacing `W#` by `conj(W(z))`, which is not entire;
2. omitting the reflection `w(-x)` in the transform of `W#`;
3. using `exp(+2*pi*i*T*xi)` in the first product;
4. dropping the second prime frequency before proving evenness;
5. changing the prime coefficient from `-1/pi` to `-1/(2*pi)`;
6. changing the pole sign or replacing `2g(i/2)` by a modulus;
7. asserting two ordinary integrations by parts while ignoring endpoint jumps of `f'`;
8. omitting absolute convergence before summing nonnegative zero terms;
9. replacing the cell-normalized identity by `-v*S*v` rather than `-h v*S*v`.

## Remaining uncertainty

The classical explicit formula itself remains imported, as it also is in T-2801. No unresolved error was found in the D-0801 transport, admissibility proof, zero-sum convergence, or normalization. A second human or formally independent reviewer should still compare the displayed classical formula with another primary source before marking this audit `INDEPENDENTLY_VERIFIED` under repository policy.

## Suggested next attack

If the production interval is negative, freeze all exact artifacts immediately and review only two independent layers:

1. this analytic dictionary and the X-2803 normalization fingerprint;
2. the complete prime/alpha/correction certificate and its independent producer reproduction.

No new search or eigenvector optimization should intervene between a strict negative result and those reviews.