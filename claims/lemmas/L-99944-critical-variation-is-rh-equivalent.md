# L-99944 — The critical weighted-variation condition is equivalent to RH

Claim ID: `L-99944`  
Status: **PROVED EXACT EQUIVALENCE USING THE STANDARD LITTLEWOOD CRITERION**  
Created: 2026-08-20

Define

\[
\mathcal V^-_2(X)
=3\int_1^X(\mathfrak H_1(x))_-\frac{dx}{x}.
\]

Then

\[
\boxed{
RH\iff \mathcal V^-_2(X)=X^{o(1)}.
}
\]

## Forward direction

`L-99943` proves

\[
\mathcal V^-_2(X)=X^{o(1)}\Longrightarrow RH.
\]

## Converse

Assume RH. The classical Littlewood criterion gives, for every
`epsilon>0`,

\[
M(x)=\sum_{n\le x}\mu(n)=O_\varepsilon(x^{1/2+\varepsilon}).
\]

Thus

\[
M_\beta(x)=\sum_{n\le x}\beta(n)=M(x)-M(x/67)
=O_\varepsilon(x^{1/2+\varepsilon}).
\]

The Dirichlet series of `beta` is

\[
\frac{1-67^{-s}}{\zeta(s)},
\]

whose value at `s=1` is zero. Partial summation therefore yields

\[
\sum_{n\le x}\frac{\beta(n)}n
=O_\varepsilon(x^{-1/2+\varepsilon})
\]

and

\[
\sum_{n\le x}\frac{\beta(n)}{\sqrt n}
=O_\varepsilon(x^\varepsilon).
\]

Consequently

\[
\mathfrak H_1(x)
=4\sqrt x\sum_{n\le x}\frac{\beta(n)}n
 -3\sum_{n\le x}\frac{\beta(n)}{\sqrt n}
=O_\varepsilon(x^\varepsilon).
\]

Replacing `epsilon` by `epsilon/2` before integration gives

\[
\mathcal V^-_2(X)=O_\varepsilon(X^\varepsilon).
\]

Hence the critical weighted variation is not a lower-strength routine
corollary of quadratic positivity; it is an exact reformulation of the
remaining RH-scale cancellation.
