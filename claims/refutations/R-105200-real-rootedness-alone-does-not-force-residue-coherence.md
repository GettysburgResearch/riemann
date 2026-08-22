# R-105200 — Real-rootedness alone does not force residue coherence above one half

Claim ID: `R-105200`  
Status: **PROVED EXACT ASYMPTOTIC COUNTERFAMILY**  
Created: 2026-08-23  
Depends on: `L-104522`; `L-105203`  
RH status: **not assumed**

For `R>2`, let

\[
p_R(x)=x(x-1)(x-2)(x-R).
\tag{R-105200.1}
\]

It has four simple real roots. Its derivative has one simple zero in each of

\[
(0,1),\qquad(1,2),\qquad(2,R).
\]

At any critical point `c`, logarithmic differentiation gives

\[
\frac{p_R''(c)}{p_R(c)}
=-\sum_{z\in\{0,1,2,R\}}\frac1{(c-z)^2}.
\]

Hence every residue is negative and

\[
\boxed{
-\rho_c
=-\frac{p_R(c)}{p_R''(c)}
=\left(\sum_z\frac1{(c-z)^2}\right)^{-1}>0.
}
\tag{R-105200.2}
\]

Let `c_R` be the critical point in `(2,R)`. Put `c_R=lambda_R R`. Its critical
equation is

\[
\frac1{c_R}+\frac1{c_R-1}+\frac1{c_R-2}+\frac1{c_R-R}=0.
\]

Every limit point `lambda in (0,1)` therefore satisfies

\[
\frac3\lambda+\frac1{\lambda-1}=0,
\]

so

\[
\boxed{\lambda_R\longrightarrow\frac34.}
\tag{R-105200.3}
\]

Using (R-105200.2),

\[
\boxed{
-\rho_{c_R}
=\frac{3}{64}R^2(1+o(1)).
}
\tag{R-105200.4}
\]

The two remaining critical points converge to the two critical points of
`x(x-1)(x-2)`, and their residue magnitudes remain bounded. Thus, with the
three critical residues denoted `rho_1,rho_2,rho_3`,

\[
-\sum_j\rho_j
=\frac{3}{64}R^2(1+o(1)),
\]

\[
\sum_j\rho_j^2
=\frac9{4096}R^4(1+o(1)).
\]

The residue coherence is consequently

\[
\boxed{
\frac{(-\sum_j\rho_j)^2}{3\sum_j\rho_j^2}
\longrightarrow\frac13.
}
\tag{R-105200.5}
\]

Therefore a polynomial may be completely real-rooted, with every critical
point Rolle-generating, while the two-moment coherence remains below the
`1/2` threshold of `L-104522`.

This does not contradict reverse Rolle: the count is already perfect. It shows
that the moment criterion is a sufficient quantitative mechanism, not a
necessary characterization of real-rootedness. In particular, the high-band
coherence theorem `L-105203` uses the Xi saddle's near-monochromatic residue
amplitudes; it cannot be replaced by the statement that the high derivative is
real-rooted.
