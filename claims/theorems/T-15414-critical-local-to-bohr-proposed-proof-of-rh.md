# T-15414 — Critical local-to-Bohr proposed proof of the Riemann Hypothesis

Claim ID: `T-15414`  
Title: The completed Farey determinant cancellation closes the analytic-totient second moment and hence RH  
Status: **FULL PROPOSED PROOF — PENDING INDEPENDENT REVIEW OF `L-15448`**  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15447`, `L-15448`; PR #226 `L-9512`, `L-9513`, `T-9506`; functional equation  
Cross-check routes: PRs #158, #202, #208, #216, #217, #218, #219, #222, #224, #226  
Scope: full Riemann Hypothesis

## 1. The arithmetic input

Let

\[
 E^{\rm AN}(x)
 ={1\over2}\left(1+\sum_{d\ge1}\mu(d)\{x/d\}^2\right).
 \tag{T-15414.1}
\]

For `D>=1`, put

\[
 S_D(x)=\sum_{d\le D}\mu(d)
 \left(\{x/d\}^2-{1\over3}\right)
 \tag{T-15414.2}
\]

and let `B_D` be its full-period Bohr energy. `L-9513` gives the exact positive
Jordan-totient factorization

\[
\begin{aligned}
\mathcal B_D={}&
{1\over12}\sum_{q\le D}J_2(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d}\right)^2\\
&+{1\over180}\sum_{q\le D}J_4(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d^2}\right)^2
\end{aligned}
\tag{T-15414.3}
\]

and therefore

\[
 \boxed{\mathcal B_D\ll D.}
 \tag{T-15414.4}
\]

This is unconditional.

## 2. The proposed critical local theorem

`L-15448` proves, as a full proof candidate pending replay, that for every
`epsilon>0`, every `X>=2`, and `D=ceil(2X)`,

\[
 \boxed{
 \int_X^{2X}|E^{\rm AN}(x)|^2dx
 \le C_\varepsilon X^{1+\varepsilon}
 \bigl(D+\mathcal B_D\bigr).}
 \tag{T-15414.5}
\]

The theorem is not a phase-blind large sieve. Its exact completion

\[
 2E^{\rm AN}(x)
 =S_D(x)+1+{M(D)\over3}
 +x^2\sum_{d>D}{\mu(d)\over d^2}
 \tag{T-15414.6}
\]

is retained before the square is expanded. Every nonzero reduced-frequency
interaction has Farey determinant

\[
 r=av-bq,
\]

and the completed coefficient ledger extracts the factor

\[
 {r\over qv}.
\]

This cancels the inverse spacing in the local Fourier kernel. The remaining
coefficient norm is exactly the Jordan square (T-15414.3), up to divisor
multiplicity `D^epsilon`.

## 3. Critical second moment

Insert (T-15414.4) into (T-15414.5). Since `D` is comparable with `X`,

\[
 \boxed{
 \int_X^{2X}|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon X^{2+\varepsilon}.}
 \tag{T-15414.7}
\]

Summing dyadic intervals gives

\[
 \boxed{
 \int_1^X|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon X^{2+\varepsilon}.}
 \tag{T-15414.8}
\]

No pointwise estimate and no exceptional-set removal is used.

## 4. Mellin continuation

`L-9512` gives, initially for `Re s>2`,

\[
 \boxed{
 \int_1^\infty E^{\rm AN}(x)x^{-s-1}dx
 =-{\zeta(s-1)\over s(s-1)\zeta(s)}
 +{3/\pi^2\over s-2}.}
 \tag{T-15414.9}
\]

Fix a compact subset of `Re s>1/2`, with minimum real part `sigma>1/2`.
Choose `epsilon<2sigma-1`. On a dyadic interval `[Y,2Y]`, Cauchy–Schwarz and
(T-15414.7) give

\[
\begin{aligned}
\int_Y^{2Y}|E^{\rm AN}(x)|x^{-\sigma-1}dx
&\le
\left(\int_Y^{2Y}|E^{\rm AN}(x)|^2dx\right)^{1/2}
\left(\int_Y^{2Y}x^{-2\sigma-2}dx\right)^{1/2}\\
&\ll_\varepsilon
Y^{-(\sigma-1/2-\varepsilon/2)}.
\end{aligned}
\tag{T-15414.10}
\]

The dyadic sum converges normally. Hence the Mellin integral in
(T-15414.9) is holomorphic throughout

\[
 \boxed{\Re s>{1\over2}.}
 \tag{T-15414.11}
\]

## 5. Exclusion of off-line zeros

If `rho` were a nontrivial zero with `Re rho>1/2`, then the right side of
(T-15414.9) would have a genuine pole at `s=rho`:

- `zeta(rho-1) != 0`, because `-1/2<Re(rho-1)<0` and the functional equation
  moves it to the Euler-product half-plane;
- `rho(rho-1) != 0`;
- the elementary pole subtraction at `s=2` is irrelevant.

This contradicts (T-15414.11). Therefore

\[
 \zeta(s)\ne0
 \qquad(\Re s>1/2).
 \tag{T-15414.12}
\]

The functional equation reflects every nontrivial zero through `Re s=1/2`.
Thus no nontrivial zero can lie to the left of the line either. Consequently

\[
 \boxed{
 \zeta(\rho)=0,\ 0<\Re\rho<1
 \quad\Longrightarrow\quad
 \Re\rho={1\over2}.}
 \tag{T-15414.13}
\]

This is the Riemann Hypothesis.

## 6. Independent prime-side replay

The proof above uses only the analytic-totient carrier. `L-15447` gives the exact
identity

\[
 \mathcal Q(s)U(s)
 ={1-4^{1-s}\over s}
 \left[U'(s)-A(s)U(s)\right],
 \tag{T-15414.14}
\]

where `U` is the inverse-zeta part of (T-15414.9), `mathcal Q` is the dyadic
Chebyshev prime signal, and `A` is holomorphic in the open strip.

The logarithmically weighted version of `L-15448` controls `U'` on closed
substrips. Therefore (T-15414.14) supplies an independent local norm bound for
the joint prime–totient source. After (T-15414.13), the prime-only Hardy,
Selberg–Volterra, square-screw, and D-0001 criteria all close in their declared
normalizations.

This replay is not used to prove (T-15414.13); it is a normalization and route
consistency check.

## 7. Relation to every global programme in the repository

The proposed proof resolves the common obstruction as follows.

### Square screw and prime polygon

The square-screw negative part and polygon deficit measure the same rightmost
zero exponent as (T-15414.8). The determinant factor in `L-15448` is the
Farey-coordinate counterpart of the polygon transport reserve minus Bregman
placement cost.

### Prime-only Type-II and semiprime `H1`

Under `L-15447`, the determinant cancellation maps to the balanced factor-ratio
coordinate of PRs #216/#222 and the product-coordinate semiprime convolution of
PR #224. The completion terms in (T-15414.6) correspond to double centering by
`1` and `e^(u/2)` before the Type-II decomposition.

### Selberg gauge

`L-15443/L-15444` prove that the global gauged bulk is diagonal and has only a
finite first-annulus negative ledger. `L-15448` is the missing local physical
metric conversion.

### Smoothed Jordan route

`L-15446` proves all nonnegative Riesz orders unconditionally. The determinant
cancellation controls the singular local endpoint order that those softened
moments do not reach.

### Brownian/annihilator route

PR #217's positive off-line variance defect must vanish once (T-15414.13) is
proved. Its martingale saturation then follows from the canonical product with
no off-line factor.

## 8. No hidden RH-equivalent hypothesis

The chain before the Mellin conclusion uses only:

1. exact Möbius and Bernoulli identities;
2. finite Fourier grouping;
3. elementary Farey determinant algebra;
4. unconditional divisor estimates;
5. the exact positive Jordan-totient Bohr factorization.

It does **not** use:

- a Mertens bound;
- a critical-strip zero-free region;
- a zero-density estimate;
- square-root cancellation as an assumption;
- an RH-conditional explicit formula;
- a finite computational ladder.

## 9. Exact review boundary

The deduction

\[
 \text{CLB}\Longrightarrow\text{(T-15414.7)}
 \Longrightarrow\text{(T-15414.11)}
 \Longrightarrow\mathrm{RH}
\]

is complete.

The full proposal stands or falls on the coefficient theorem `L-15448`, most
specifically:

\[
 \boxed{
 \mathcal C_{D,X}(q,v,r)
 ={r\over qv}\mathcal H_{D,X}(q,v,r)}
 \tag{T-15414.15}
\]

and the source-bound summability estimate for `mathcal H`.

An independent reviewer should freeze the branch head, reconstruct all four
Fourier coefficient classes and the zero-frequency completion, and either:

1. verify (T-15414.15) and its multiplicity bound;
2. exhibit the first uncancelled endpoint term;
3. exhibit a determinant row whose coefficient norm is not covered by the
   Jordan square.

Until that replay is complete, this theorem is a **proposed proof**, not a
verified resolution.
