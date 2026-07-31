# L-15602 — Explicit near-radical scalar envelope

Claim ID: `L-15602`  
Title: Compression and cross-residual norms give a closed counted inverse–Ritz floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: `L-15601`; elementary Gram algebra  
Scope: cofinal lower envelopes from exact repaired radical packets

## Statement

Retain the hypotheses and notation of `L-15601`. Let `J:C^d->H` be an injective coordinate map for the trial packet and write

\[
 G=J^*J,
 \qquad
 B=J^*AJ,
 \qquad
 \mathcal R=J^*A(I-P)AJ,
 \tag{L-15602.1}
\]

where

\[
 P=JG^{-1}J^*
\]

is the orthogonal projection onto the trial space. Assume rational numbers

\[
 0\le\alpha<t,
 \qquad
 \beta\ge0
\]

satisfy

\[
 -\alpha G\preceq B\preceq\alpha G,
 \qquad
 0\preceq\mathcal R\preceq\beta^2G.
 \tag{L-15602.2}
\]

Then the choice

\[
 \boxed{
 q=-\frac{t-\alpha}{(t+\alpha)^2+\beta^2}<0}
 \tag{L-15602.3}
\]

satisfies the inverse–Ritz inequality `qK_t-H_t>=0`, and consequently

\[
 \boxed{
 \inf\sigma(A)
 \ge
 -\frac{3t\alpha+\alpha^2+\beta^2}{t-\alpha}.}
 \tag{L-15602.4}
\]

## Proof

In coordinates on the trial packet,

\[
 H_t=B-tG.
 \tag{L-15602.5}
\]

The exact Pythagorean residual decomposition gives

\[
 K_t=(B-tG)G^{-1}(B-tG)+\mathcal R.
 \tag{L-15602.6}
\]

Conjugating by `G^(-1/2)`, (L-15602.2) implies

\[
 H_t\preceq-(t-\alpha)G
 \tag{L-15602.7}
\]

and

\[
 K_t\preceq\bigl((t+\alpha)^2+\beta^2\bigr)G.
 \tag{L-15602.8}
\]

Because `q<0`, (L-15602.8) reverses after multiplication by `q`. Therefore

\[
 \begin{aligned}
 qK_t-H_t
 &\succeq
 q\bigl((t+\alpha)^2+\beta^2\bigr)G
 +(t-\alpha)G\\
 &=0.
 \end{aligned}
\]

`L-15601` now gives `inf sigma(A)>=t+1/q`. Direct simplification yields

\[
 t+\frac1q
 =t-\frac{(t+\alpha)^2+\beta^2}{t-\alpha}
 =-\frac{3t\alpha+\alpha^2+\beta^2}{t-\alpha}.
\]

QED.

## Radical-tail specialization

Suppose the trial vectors are localized pieces of exact global radical vectors, so `L-14309` transports their complete compression and cross residual to the discarded tails. If a source/tail estimate gives

\[
 \alpha_a\to0,
 \qquad
 \beta_a\to0,
 \tag{L-15602.9}
\]

uniformly on a packet whose dimension matches the certified low-eigenvalue count, and if

\[
 t_a\ge t_0>0,
 \tag{L-15602.10}
\]

then

\[
 F_a:=-\frac{3t_a\alpha_a+\alpha_a^2+\beta_a^2}
              {t_a-\alpha_a}
 \longrightarrow0^-.
 \tag{L-15602.11}
\]

The quadratic cross term is the key weakening: eigenvector convergence would usually require `beta_a/t_a ->0`, whereas the lower floor only charges `beta_a^2/t_a`.

## Exact remaining capacity condition

Define `C(a,eps)` to be the largest dimension of an exact repaired radical packet at support `a` for which

\[
 \alpha_a\le\varepsilon,
 \qquad
 \beta_a\le\varepsilon.
\]

Let `D(a,t,Gamma)` be any certified upper bound for the number of localized Weil eigenvalues below `Gamma`, with `0<t<Gamma`. The entire cofinal problem is reduced to finding a sequence for which

\[
 \boxed{
 D(a_j,t_j,\Gamma_j)
 \le C(a_j,\varepsilon_j),
 \qquad
 \varepsilon_j\to0.}
 \tag{L-15602.12}
\]

No principal-angle estimate is needed once this rank-capacity inequality and the complete residual bounds are available.

## Gap audit

`L-15303` proves arbitrarily large near-radical packets only by a fixed-rank then-support diagonal argument. It does not by itself prove (L-15602.12), because the dangerous count may grow with support. That rank-growth comparison is now the sole structural asymptotic gate in this interface.
