# R-99900 — The unweighted collar window is not the literal normalized-box source

Claim ID: `R-99900`  
Status: **PROVED EXACT STATEMENT-TO-USE SEPARATOR**  
Created: 2026-08-20  
Frozen target: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
RH status: **not assumed**

Let

\[
T(y)=(4\sqrt y-3)\mathbf 1_{y\ge1},
\qquad
h(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}T(X/n),
\]

where

\[
\beta=(\varepsilon-\delta_{67})*\mu.
\]

For `R>1`, set

\[
(\mathcal S_Rh)(X)=\int_{X/R}^{X}h(t)\frac{dt}{t}
\]

with zero extension below one, and put

\[
W_R(y)=\int_{\max(1,y/R)}^yT(v)\frac{dv}{v},
\qquad
\Phi_R(y)=\frac{W_R(y)}{\sqrt y}.
\]

Finite Fubini gives

\[
(\mathcal S_Rh)(X)
 =\sum_{n\le X}\frac{\beta(n)}{\sqrt n}W_R(X/n).
\]

Since

\[
W_R(X/n)=\sqrt{X/n}\,\Phi_R(X/n),
\]

we obtain the exact normalized identity

\[
\boxed{
\frac{(\mathcal S_Rh)(X)}{\sqrt X}
 =\sum_{n\le X}\frac{\beta(n)}n\Phi_R(X/n).
}
\tag{R-99900.1}
\]

Consequently the native prime-adjoining operator on the normalized potential is

\[
\boxed{I-p^{-1}U_p,}
\tag{R-99900.2}
\]

not `I-p^-1/2 U_p`.

The two operators correspond to different objects:

```text
unnormalized kernel W_R       -> coefficient p^-1/2;
normalized kernel Phi_R       -> coefficient p^-1.
```

PR #664 `L-99819` applies `I-p^-1/2 U_p` to the normalized collar formula

\[
\Phi_{67}(u)=8+(-8-3u)e^{-u/2}.
\]

For a shifted subset product `d`, the factor `d^-1/2` is cancelled by the
factor `d^1/2` arising from the translated exponential, producing the
unweighted coefficient `mu(d)`. In the native normalized box the source
coefficient is instead `d^-1`; only one square-root is cancelled, leaving
`mu(d)/sqrt(d)`.

Thus the displayed unweighted ratio-67 Mertens window in `L-99819` is an exact
coefficient identity for an auxiliary half-order operator, but it is not the
literal collar coefficient of (R-99900.1).

This correction does not refute the two-prime positivity computations at their
stated auxiliary normalization. It blocks their promotion to the
conclusion-facing normalized box until the source exponent is repaired.
