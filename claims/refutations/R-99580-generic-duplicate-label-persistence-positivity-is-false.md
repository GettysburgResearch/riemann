# R-99580 — Generic duplicate-label persistence positivity is false

Claim ID: `R-99580`  
Status: **EXACT REFUTATION**  
Created: 2026-08-20

Take six labels, all of cost `2` and activity

\[
r=2^{-1/2},
\]

and distinguish one. At `X=8`, so `L=3log2`, only subsets of sizes one and two
have nonzero stop-loss contribution. The relative persistence divided by
`log2` is

\[
\begin{aligned}
&\binom61r(3-1)-\binom62r^2(3-2)-r(3-1)\\
&=10r-15r^2\\
&=5\sqrt2-\frac{15}{2}<0,
\end{aligned}
\]

because `200<225` after squaring the positive sides and multiplying by four.

Thus

\[
\boxed{
\text{duplicate label + critical activity + threshold complex}
\not\Longrightarrow
\text{nonnegative relative persistence}.
}
\]

A proof of IHR67 must exploit the actual dyadic multiplicities, distinct prime
log-costs, the duplicated `67` factor, or an equally source-specific analytic
mechanism. A source-blind Morse, Gram, or generic complete-monotonicity proof is
invalid.
