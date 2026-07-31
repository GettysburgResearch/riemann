# L-14312 — Rapid decay of an exact radical truncation residual

Claim ID: `L-14312`  
Title: A fixed exact `E`-radical has a super-polynomially small localized Weil residual  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: Connes--Consani `E`-range radical theorem and Poisson identity; the Guinand--Weil decomposition in CCM equation (3.19); elementary Schwartz and Fourier estimates  
Scope: localized Weil form on `[lambda^{-1},lambda]` and the Hardy-strip dual norm used in `L-14302`/`L-14303`  
Related counterexample candidates: none

## 1. Exact source and radical vector

Let

\[
 \mathcal S_0^{\rm ev}
 =\{f\in\mathcal S(\mathbb R): f\text{ real and even},\ f(0)=\widehat f(0)=0\}.
\]

Fix any nonzero `f in S_0^ev`; one concrete choice is

\[
 f(x)=x^2\left(x^2-\frac{3}{2\pi}\right)e^{-\pi x^2}.
 \tag{L-14312.1}
\]

Indeed `f(0)=0`; direct differentiation of the Gaussian Fourier transform gives
\(\widehat f=f\), and hence the Gaussian moment identities give
\[
 \widehat f(0)=\int_{\mathbb R}f(x)\,dx=0.
\]

Define

\[
 r(u)=E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu),
 \qquad u>0.
 \tag{L-14312.2}
\]

The imported Connes--Consani theorem says that `r` belongs to the radical of the
global Weil form:

\[
 QW(r,g)=0
 \tag{L-14312.3}
\]

for every admissible test vector `g`. Their Poisson identity gives

\[
 E(\widehat f)(u)=E(f)(u^{-1}).
 \tag{L-14312.4}
\]

Because both `f` and `hat f` are Schwartz, `r` and all logarithmic derivatives
are rapidly decreasing at both multiplicative ends.

Put

\[
 R(x)=r(e^x),\qquad x\in\mathbb R.
\]

Then for every pair of nonnegative integers `A,j` there is a constant
`C_(A,j)` such that

\[
 \boxed{
 |R^{(j)}(x)|\le C_{A,j}e^{-A|x|}
 \quad (|x|\ge1).}
 \tag{L-14312.5}
\]

## 2. Truncation and residual norm

For `lambda>1`, write

\[
 L=\log\lambda,
 \qquad I_L=[-L,L],
\]

and define

\[
 k_\lambda(x)=1_{I_L}(x)R(x),
 \qquad
 t_\lambda(x)=R(x)-k_\lambda(x).
 \tag{L-14312.6}
\]

We extend every localized test vector by zero outside `I_L`. For
`0<tau<1/2`, let

\[
 \|g\|_{L,\tau}^2
 =\int_{-L}^{L}|g(x)|^2\,2\cosh(2\tau x)\,dx.
 \tag{L-14312.7}
\]

For the moving-strip schedule

\[
 \boxed{
 \tau_\lambda=\frac12-\frac1{\log\lambda},
 \qquad \lambda\ge e^4,}
 \tag{L-14312.8}
\]

define the complete constrained residual

\[
 \mathfrak T_{\lambda,\tau_\lambda}
 =\sup_{\substack{g\perp k_\lambda\\
                   \|g\|_{L,\tau_\lambda}=1}}
 |QW_\lambda(k_\lambda,g)|.
 \tag{L-14312.9}
\]

The orthogonality may be removed when taking an upper bound.

## 3. Main estimate

For every `N>0` there is a constant `C_N`, depending only on the fixed source
`f` and the Fourier normalization, such that

\[
 \boxed{
 \mathfrak T_{\lambda,\tau_\lambda}
 \le C_N\lambda^{-N}
 \qquad(\lambda\ge e^4).}
 \tag{L-14312.10}
\]

The Rayleigh numerator has the same rapid decay:

\[
 \boxed{
 |QW_\lambda(k_\lambda,k_\lambda)|
 \le C_N\lambda^{-N}.}
 \tag{L-14312.11}
\]

Finally,

\[
 \boxed{
 \|k_\lambda\|_2^2\longrightarrow\|R\|_2^2>0.}
 \tag{L-14312.12}
\]

## 4. Proof of the rapid tail bounds

The Schwartz estimate on `f` gives, for every `A,j`,

\[
 \left|(u\partial_u)^jE(f)(u)\right|\le C_{A,j}u^{-A}
 \qquad(u\ge1).
 \tag{L-14312.13}
\]

This follows by differentiating termwise and using

\[
 \sum_{n\ge1}(nu)^B(1+nu)^{-A-B-2}
 \le C_Au^{-A}.
\]

Applying the same estimate to `hat f` and using (L-14312.4) proves
(L-14312.5). Consequently, for every `A`,

\[
\begin{aligned}
 \|t_\lambda\|_1+\|t_\lambda\|_2
 +\|t_\lambda'\|_1+|R(L)|+|R(-L)|
 &\le C_A\lambda^{-A},\\
 \int_{|x|>L}|R(x)|e^{|x|/2}\,dx
 &\le C_A\lambda^{-A}.
\end{aligned}
 \tag{L-14312.14}
\]

The exponent `A` can be increased at will, so fixed losses of powers of
`lambda` or `log lambda` are harmless.

## 5. The archimedean multiplier

The archimedean part of the polarized Guinand--Weil form is

\[
 \frac1{2\pi}\int_{\mathbb R}
 a(\xi)\overline{\widehat t_\lambda(\xi)}
 \widehat g(\xi)\,d\xi,
 \qquad
 a(\xi)=2\theta'(\xi),
 \tag{L-14312.15}
\]

up to the fixed Fourier convention. Standard digamma bounds give

\[
 |a(\xi)|\le C\bigl(1+\log(2+|\xi|)\bigr).
 \tag{L-14312.16}
\]

Let

\[
 A_0=\|t_\lambda\|_1,
 \qquad
 A_1=|R(L)|+|R(-L)|+\|t_\lambda'\|_1.
\]

The direct bound and integration by parts on the two tails give

\[
 |\widehat t_\lambda(\xi)|
 \le\min\left(A_0,\frac{A_1}{|\xi|}\right).
 \tag{L-14312.17}
\]

Since

\[
 \int_1^\infty\frac{(1+\log\xi)^2}{\xi^2}\,d\xi<\infty,
\]

we obtain

\[
 \|a\widehat t_\lambda\|_2
 \le C(A_0+A_1)
 \le C_A\lambda^{-A}.
 \tag{L-14312.18}
\]

Also `2 cosh(2 tau x)>=2`, so every unit vector in (L-14312.7) satisfies
`||g||_2<=2^{-1/2}`. Plancherel and Cauchy--Schwarz therefore make the entire
archimedean contribution `O_A(lambda^{-A})`.

## 6. The `W_(0,2)` endpoint term

The tail factors obey

\[
 |\widehat t_\lambda(\pm i/2)|
 \le\int_{|x|>L}|R(x)|e^{|x|/2}\,dx
 \le C_A\lambda^{-A}.
 \tag{L-14312.19}
\]

For a localized unit vector, weighted Cauchy--Schwarz gives

\[
 |\widehat g(i/2)|^2
 \le\int_{-L}^{L}\frac{e^x}{2\cosh(2\tau_\lambda x)}\,dx,
 \tag{L-14312.20}
\]

and similarly at `-i/2`. Since

\[
 1-2\tau_\lambda=\frac2L,
\]

the two integrals in (L-14312.20) are `O(L)`. Hence the complete endpoint
term is `O_A(lambda^{-A}sqrt(log lambda))`, and is therefore rapidly decreasing.

## 7. The complete prime-power term

In logarithmic coordinates the polarized prime part is a fixed linear
combination of

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \langle t_\lambda,S_{\pm\log n}g\rangle,
 \tag{L-14312.21}
\]

where `S_y` is translation by `y` and `g` is extended by zero.

Split the sum at `n=lambda^2`.

For `n<=lambda^2`,

\[
 |\langle t_\lambda,S_{\pm\log n}g\rangle|
 \le\|t_\lambda\|_2\|g\|_2,
\]

and the elementary estimate

\[
 \sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}
 \le\sum_{n\le\lambda^2}\frac{\log n}{\sqrt n}
 \le C\lambda\log\lambda
 \tag{L-14312.22}
\]

shows that this part is rapidly decreasing after increasing `A` in
(L-14312.14).

For `n>lambda^2`, the translated support lies wholly in one discarded tail.
Using `||g||_1<=sqrt(2L)||g||_2` and (L-14312.5), for every `A>2`,

\[
 |\langle t_\lambda,S_{\pm\log n}g\rangle|
 \le C_A\sqrt L\left(\frac n\lambda\right)^{-A}.
 \tag{L-14312.23}
\]

Therefore

\[
\begin{aligned}
 \sum_{n>\lambda^2}\frac{\Lambda(n)}{\sqrt n}
 |\langle t_\lambda,S_{\pm\log n}g\rangle|
 &\le C_A\sqrt L\lambda^A
 \sum_{n>\lambda^2}(\log n)n^{-A-1/2}\\
 &\le C_A'(\log\lambda)^{3/2}\lambda^{1-A}.
\end{aligned}
 \tag{L-14312.24}
\]

Again `A` is arbitrary. This controls every prime power; no prime number
theorem or cutoff omission is used.

## 8. Radical transport and conclusion

The exact radical identity and `r=k_lambda+t_lambda` give

\[
 QW_\lambda(k_\lambda,g)=-QW(t_\lambda,g)
 \tag{L-14312.25}
\]

for every localized test vector. Sections 5--7 and the endpoint estimate prove
(L-14312.10).

For completeness, the diagonal prime term is also rapidly decreasing. For
`n<=lambda^2`, its correlation is at most `||t_lambda||_2^2`. For
`n>lambda^2`, the two nonzero tail factors are separated by `log n`; the
triangle inequality gives
\[
 |x|+|x\mp\log n|\ge\log n,
\]
and (L-14312.5) therefore yields, for every `A`,
\[
 |\langle t_\lambda,S_{\pm\log n}t_\lambda\rangle|
 \le C_A(1+\log n)n^{-A}.
\]
The weighted sum over `n>lambda^2` is `O_A(lambda^{-A})` after increasing
`A`. The diagonal archimedean and endpoint pieces follow from the same
Fourier and weighted-moment estimates. Thus `QW(t_lambda,t_lambda)` is rapidly
decreasing, and the diagonal identity in `L-14309` proves (L-14312.11).
Finally, rapid tail decay gives `||t_lambda||_2->0`. The function `R` is
nonzero because its Mellin transform is the product of the nonzero Mellin
transform of `f` with the nonzero meromorphic function `zeta`; hence
(L-14312.12) follows. QED.

## 9. Fixed finite radical packets

The same proof applies simultaneously to any fixed finite collection
`f_1,...,f_d in S_0^ev`. Every entry of the truncated radical block and every
cross residual from that fixed block is `O_N(lambda^{-N})` for all `N`.

What is not proved here is a uniform estimate for a packet whose dimension and
source complexity grow with `lambda`.

## Gap audit

- The `E`-range radical and Poisson statements are imported and require the
  exact Fourier/Mellin normalization audit.
- The sharp cutoff creates first-kind jumps, which are allowed by the declared
  Weil class; alternatively one may pass through smooth cutoffs by dominated
  convergence.
- The theorem controls one fixed source, or a fixed finite family. It does not
  control the full growing generalized-prolate low packet.
- No lower bound for the scalar complement of `span{k_lambda}` is asserted.
- This lemma proves a residual estimate, not RH.
