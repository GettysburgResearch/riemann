# L-99940 — Exact distributional descent from the quadratic SHARP power to the critical linear transform

Claim ID: `L-99940`  
Status: **PROVED EXACT DISTRIBUTIONAL IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99939` only for positivity, not for the identity  
RH status: **not assumed**

For real `m>=1` put

\[
\mathfrak H_m(x)
=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n)^m,
\]

where `beta` and `T` are as in `L-99939`. Define

\[
G_2(u)=e^{-u}\mathfrak H_2(e^u).
\]

Then, as a signed Radon measure on `[0,infinity)`,

\[
\boxed{
dG_2(u)
=\sum_{n\ge1}\frac{\beta(n)}{n^{3/2}}\delta_{\log n}(du)
 +3e^{-u}\mathfrak H_1(e^u)\,du.
}
\tag{L-99940.1}
\]

## Proof

Fix one `n` and write `y=e^u/n`. For `u>log n`, its contribution is

\[
\beta(n)n^{-3/2}\frac{T(y)^2}{y}.
\]

Since `T(y)=4sqrt(y)-3`, direct differentiation gives

\[
y\frac d{dy}\left(\frac{T(y)^2}{y}\right)
=\frac{3T(y)}{y}.
\]

Therefore the absolutely continuous derivative of the `n`th term is

\[
3\beta(n)n^{-3/2}\frac{T(y)}{y}\,du
=3e^{-u}\frac{\beta(n)}{\sqrt n}T(e^u/n)\,du.
\]

At `u=log n`, `T(1)=1`, so the term jumps by `beta(n)n^(-3/2)`.
Summing the finitely many active terms on compact `u` intervals proves
(L-99940.1).

Equivalently, for `1<=A<B`,

\[
\boxed{
3\int_A^B\mathfrak H_1(x)\frac{dx}{x^2}
=\frac{\mathfrak H_2(B)}B
 -\frac{\mathfrak H_2(A)}A
 -\sum_{A<n\le B}\frac{\beta(n)}{n^{3/2}}.
}
\tag{L-99940.2}
\]
