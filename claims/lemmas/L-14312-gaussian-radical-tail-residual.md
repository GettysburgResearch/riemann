# L-14312 — Gaussian decay of an exact Riemann-radical truncation residual

Claim ID: `L-14312`  
Title: A fixed exact Riemann source gives a cofinally Gaussian-small localized Weil cross residual  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: the Connes--Consani global `E`-range radical theorem; the standard polarized Weil explicit formula; elementary Gaussian tails  
Scope: one explicit global radical vector, every compact multiplicative support, and every finite localized low packet  
Related counterexample candidates: none

## 1. Exact source and global radical

Use the additive Fourier convention

\[
 \widehat f(y)=\int_{\mathbb R}f(x)e^{-2\pi ixy}\,dx.
\]

Define the even Hermite source

\[
 h_R(x)=\frac{\pi}{2}x^2(2\pi x^2-3)e^{-\pi x^2}.
 \tag{L-14312.1}
\]

It satisfies exactly

\[
 h_R(0)=0,
 \qquad
 \widehat h_R=h_R,
 \qquad
 \int_{\mathbb R}h_R(x)\,dx=\widehat h_R(0)=0.
 \tag{L-14312.2}
\]

For completeness, if `z=pi*x^2`, the Fourier transform sends

\[
 1\mapsto1,
 \qquad
 z\mapsto\frac12-z,
 \qquad
 z^2\mapsto z^2-3z+\frac34.
\]

Thus it fixes `z^2-(3/2)z`, proving (L-14312.2) without an appeal to a
numerical Hermite normalization.

Let

\[
 r(u)=\mathcal E(h_R)(u)
 :=u^{1/2}\sum_{n\ge1}h_R(nu),
 \qquad u>0.
 \tag{L-14312.3}
\]

The imported global `E`-range theorem applies because both codimension-two
source constraints in (L-14312.2) hold.  Hence

\[
 Q_W(r,g)=0
 \tag{L-14312.4}
\]

for every test vector in the declared Weil class.  Poisson summation gives

\[
 \mathcal E(\widehat h_R)(u)=\mathcal E(h_R)(u^{-1}),
\]

so self-Fourier invariance yields

\[
 r(u)=r(u^{-1}).
 \tag{L-14312.5}
\]

Put

\[
 R(x)=r(e^x),\qquad x\in\mathbb R.
 \tag{L-14312.6}
\]

Then `R` is real, even, smooth, nonzero, and rapidly decreasing more strongly
than any ordinary exponential at both ends.

## 2. Localized vector, tail, and cross residual

For `lambda>1`, put

\[
 L=\log\lambda,
 \qquad I_L=[-L,L],
\]

and define

\[
 k_\lambda=1_{I_L}R,
 \qquad
 t_\lambda=R-k_\lambda.
 \tag{L-14312.7}
\]

The sharp truncation belongs to the localized logarithmic form domain: its
zero extension is piecewise smooth with two finite jumps, so its Fourier
transform is `O(1/|xi|)`, which is square integrable against
`1+log^+|xi|`.

For `0<tau<1/2`, define the Hardy source norm

\[
 \|g\|_{L,\tau}^2
 =\int_{-L}^{L}|g(x)|^2\,2\cosh(2\tau x)\,dx.
 \tag{L-14312.8}
\]

Let `S_lambda` be any finite-dimensional subspace of the localized form domain
containing `k_lambda`, with orthogonal complement taken in ordinary `L2`.  Put

\[
 \mathfrak T_{\lambda,\tau}(S_\lambda)
 :=\sup_{\substack{g\in \mathfrak D(Q_W^L)\cap S_\lambda^\perp\\
                   \|g\|_{L,\tau}=1}}
       |Q_W^L(k_\lambda,g)|.
 \tag{L-14312.9}
\]

For smooth compactly supported `g`, extension by zero and (L-14312.4) give

\[
 \boxed{
 Q_W^L(k_\lambda,g)=-Q_W(t_\lambda,g).}
 \tag{L-14312.10}
\]

The estimates below prove that the right side is continuous in the Hardy norm,
so the identity extends to the stated complement by form-core density.  No RH
assumption or spectral approximation occurs here.

## 3. Gaussian tail bounds

For every fixed integer `j>=0`, there are explicit constants `C_j` and integers
`A_j` such that, for `u>=1`,

\[
 \left|(u\partial_u)^j r(u)\right|
 \le C_j u^{A_j}e^{-\pi u^2}.
 \tag{L-14312.11}
\]

Indeed, each derivative of `h_R` is a polynomial times `e^{-pi x^2}`.  Termwise
differentiation gives a sum bounded by

\[
 C_j u^{A_j}\sum_{n\ge1}n^{A_j}e^{-\pi n^2u^2},
\]

and the last sum is at most a fixed multiple of `e^{-pi u^2}` for `u>=1`.
Equation (L-14312.5) supplies the lower multiplicative tail.

Consequently there are constants `C,M`, independent of `lambda`, such that for
`lambda>=2`,

\[
\begin{aligned}
 &\|t_\lambda\|_1+\|t_\lambda\|_2
 +\|\partial_xt_\lambda\|_{L^1(\mathbb R\setminus I_L)}+|R(L)|\\
 &\qquad+
 \sum_{\varepsilon=\pm1}
 \left|\int_{\mathbb R}t_\lambda(x)e^{\varepsilon x/2}\,dx\right|
 \le C\lambda^M e^{-\pi\lambda^2}.
\end{aligned}
 \tag{L-14312.12}
\]

The derivative is taken on the two open tails; the two cutoff jumps are
charged separately by `2|R(L)|` below.

## 4. Moving Hardy schedule

For `L>=4`, choose

\[
 \tau_L=\frac12-\frac1L.
 \tag{L-14312.13}
\]

Then `tau_L` increases to `1/2`.  If `g` is supported in `I_L` and
`||g||_(L,tau_L)=1`, then

\[
 \|g\|_2\le2^{-1/2},
 \qquad
 \|g\|_1\le L^{1/2}.
 \tag{L-14312.14}
\]

Moreover

\[
 \left|\int_{-L}^{L}g(x)e^{\pm x/2}\,dx\right|
 \le C_0L^{1/2}.
 \tag{L-14312.15}
\]

For example,

\[
 \int_{-L}^{L}\frac{e^x}{2\cosh(2\tau_Lx)}\,dx
 \le 1+\int_0^L e^{2x/L}\,dx=O(L),
\]

and Cauchy--Schwarz proves the `+` case; the other sign follows by symmetry.

## 5. Archimedean term

In logarithmic coordinates the archimedean part of the polarized Weil form is
an exact real Fourier multiplier `a(xi)=2 theta'(xi)` up to the fixed Fourier
normalization.  The digamma asymptotic gives

\[
 |a(\xi)|\le C_a\bigl(1+\log(2+|\xi|)\bigr).
 \tag{L-14312.16}
\]

Set

\[
 A_0=\|t_\lambda\|_1,
 \qquad
 A_1=2|R(L)|+
 \|\partial_xt_\lambda\|_{L^1(\mathbb R\setminus I_L)}.
\]

The elementary Fourier bounds

\[
 |\widehat t_\lambda(\xi)|\le A_0,
 \qquad
 |\widehat t_\lambda(\xi)|\le A_1/|\xi|
 \quad(|\xi|\ge1)
 \tag{L-14312.17}
\]

follow by one Stieltjes integration by parts on each tail, including both
jumps.  Since

\[
 \int_1^\infty
 \frac{(1+\log(2+x))^2}{x^2}\,dx<\infty,
\]

(L-14312.12) gives

\[
 \|a\widehat t_\lambda\|_2
 \le C\lambda^M e^{-\pi\lambda^2}.
 \tag{L-14312.18}
\]

Plancherel and (L-14312.14) give the same bound for the complete archimedean
cross term.

## 6. The `0,2` term

The two rank-one terms in the Weil explicit formula are products of the Mellin
evaluations at `+i/2` and `-i/2`.  Equations (L-14312.12) and
(L-14312.15) therefore imply

\[
 |W_{0,2}(t_\lambda,g)|
 \le C\lambda^M L^{1/2}e^{-\pi\lambda^2}.
 \tag{L-14312.19}
\]

## 7. Prime-power translations

In logarithmic coordinates the polarized prime part is, up to the fixed sign,

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \left(
  \langle t_\lambda,T_{\log n}g\rangle
 +\langle t_\lambda,T_{-\log n}g\rangle
 \right),
 \tag{L-14312.20}
\]

where every function is extended by zero when necessary.

For `n<=lambda^2`, Cauchy--Schwarz and

\[
 \sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}
 \le\sum_{n\le\lambda^2}\frac{\log n}{\sqrt n}
 \le C\lambda\log\lambda
 \tag{L-14312.21}
\]

bound this part by a polynomial in `lambda` and `log lambda` times
`e^{-pi lambda^2}`.

For `n>lambda^2`, each shifted copy of `g` lies wholly in one exterior tail.
On its support, the relevant multiplicative argument is at least `n/lambda`.
Equations (L-14312.11) and (L-14312.14) give

\[
 |\langle t_\lambda,T_{\pm\log n}g\rangle|
 \le C L^{1/2}
 \left(\frac n\lambda\right)^M
 \exp\left[-\pi\left(\frac n\lambda\right)^2\right].
 \tag{L-14312.22}
\]

Using only `Lambda(n)<=log n` and comparison with the corresponding Gaussian
integral,

\[
 \sum_{n>\lambda^2}\frac{\log n}{\sqrt n}
 \left(\frac n\lambda\right)^M
 e^{-\pi(n/\lambda)^2}
 \le C\lambda^{M+1}\log\lambda\,e^{-\pi\lambda^2}.
 \tag{L-14312.23}
\]

Thus the entire prime contribution has the same Gaussian scale.  No prime
number theorem is used.

## 8. Main residual theorem

Combining Sections 5--7 with (L-14312.10) proves the following.

### Theorem

There exist constants `C<infinity`, `M>=0`, and `lambda_0` such that for every
`lambda>=lambda_0`, every finite localized subspace `S_lambda` containing
`k_lambda`, and `tau_L` from (L-14312.13),

\[
 \boxed{
 \mathfrak T_{\lambda,\tau_L}(S_\lambda)
 \le C\lambda^M(1+\log\lambda)^{3/2}
 e^{-\pi\lambda^2}.}
 \tag{L-14312.24}
\]

In particular, after increasing `lambda_0`,

\[
 \boxed{
 \mathfrak T_{\lambda,\tau_L}(S_\lambda)
 \le C e^{-\pi\lambda^2/2}.}
 \tag{L-14312.25}
\]

Also,

\[
 \boxed{
 \|k_\lambda\|_2\longrightarrow\|R\|_2>0.}
 \tag{L-14312.26}
\]

The convergence follows by dominated convergence.  Positivity of the limiting
norm follows, for example, from the asymptotic
`r(u)=u^(1/2)h_R(u)+O(u^A e^{-4 pi u^2})` as `u->infinity`.

The same estimates applied to both tail arguments also give

\[
 |Q_W^L(k_\lambda,k_\lambda)|
 =|Q_W(t_\lambda,t_\lambda)|
 \le C\lambda^M e^{-2\pi\lambda^2}.
 \tag{L-14312.27}
\]

## 9. Fixed finite radical packets

The proof applies entrywise to any fixed finite collection of exact Schwartz
sources in the global `E`-radical whose logarithmic representatives satisfy a
common Gaussian envelope.  Every fixed finite block of their truncations has
Gaussian-small diagonal entries and Gaussian-small cross map into an arbitrary
localized complement.

This statement does not cover a packet whose source complexity grows without a
uniform tail envelope.

## Analytic and gap audit

- The Gaussian estimates and explicit-form contractions are unconditional.
- The radical identity imports the exact `E`-range theorem and its source/Fourier
  normalization.
- The estimates are first proved on the smooth compact form core and then
  extended by the established Hardy-norm bound.
- A smooth support cutoff may replace the sharp cutoff; the stated sharp cutoff
  already belongs to the logarithmic form domain.
- The theorem closes the numerator only.  It does not prove complement
  coercivity or control a growing low block.
- No form of RH is assumed.
