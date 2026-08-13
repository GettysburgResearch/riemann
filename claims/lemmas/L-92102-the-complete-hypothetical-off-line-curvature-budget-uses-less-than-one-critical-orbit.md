# L-92102 — The complete hypothetical off-line curvature budget uses less than one critical orbit

Claim ID: `L-92102`  
Status: **PROPOSED COMPLETE GLOBAL BUDGET — EXTERNAL VERIFICATION INPUT DECLARED**  
Created: 2026-08-13  
Depends on: `L-92101`; Platt–Trudgian source lock on PR #438; Riemann–von Mangoldt  
RH status: **unproved**

## 1. Verified height

Let

\[
 \boxed{
 H_*=3{,}000{,}175{,}332{,}800.
 }
 \tag{L-92102.1}

The external source lock on PR #438 imports the rigorous Platt–Trudgian
verification that every nontrivial zero with

\[
 0<\Im\rho\le H_*
\]

lies on the critical line.  The published computation also reports simplicity,
but the present argument needs only one unit of one critical orbit.

The Riemann–von Mangoldt formula ensures that there is a critical-line zero

\[
 \rho_0=\frac12+i\gamma_0
 \qquad\text{with}\qquad
 0<\gamma_0\le H_*/2.
 \tag{L-92102.2}

Put

\[
 r_0=\gamma_0^2\le H_*^2/4
\]

and retain one unit of its contribution

\[
 R_0(t)=\frac2{t+r_0}.
 \tag{L-92102.3}

Every hypothetical off-line orbit has ordinate `b>H_*`.

## 2. Allocation to one off-line orbit

For every right-side off-line orbit representative

\[
 \lambda_\alpha=a_\alpha+ib_\alpha,
 \qquad
 a_\alpha>0,
 \quad b_\alpha>H_*,
\]

of multiplicity `m_alpha`, define the exact fraction from `L-92101`

\[
 \epsilon_\alpha
 =\frac{2m_\alpha\kappa_\alpha}
       {1-\kappa_\alpha},
 \qquad
 \kappa_\alpha
 =\frac{4a_\alpha^2b_\alpha^2}
 {(b_\alpha^2-a_\alpha^2-r_0)^2}.
 \tag{L-92102.4
}

The hypotheses of `L-92101` hold.  Moreover,

\[
 \boxed{
 0<\epsilon_\alpha
 \le\frac{9m_\alpha}{b_\alpha^2}.
 }
 \tag{L-92102.5
}

## 3. Reciprocal-square zero tail

Let `N(T)` count nontrivial zeros with positive ordinate up to `T`, including
multiplicity.  The standard explicit Riemann–von Mangoldt estimate gives the
very coarse bound

\[
 N(T)\le T\log T
 \qquad(T\ge H_*).
 \tag{L-92102.6}

Stieltjes integration by parts yields

\[
\begin{aligned}
 \sum_{\gamma>H_*}\frac{m_\rho}{\gamma^2}
 &=\int_{(H_*,\infty)}t^{-2}\,dN(t)\\
 &=-\frac{N(H_*)}{H_*^2}
   +2\int_{H_*}^{\infty}\frac{N(t)}{t^3}\,dt\\
 &\le\frac{2(\log H_*+1)}{H_*}.
\end{aligned}
 \tag{L-92102.7}

The off-line orbit representatives form only a subcollection of these zeros,
so (L-92102.5) gives

\[
\boxed{
 \sum_\alpha\epsilon_\alpha
 \le\frac{18(\log H_*+1)}{H_*}
 <1.8\times10^{-10}<1.
}
\tag{L-92102.8}

The displayed decimal is only for scale; the strict inequality `<1` follows
immediately from the exact integer `H_*` and elementary logarithm bounds.

## 4. One reserve orbit is enough

Set

\[
 \epsilon_0=1-\sum_\alpha\epsilon_\alpha>0.
 \tag{L-92102.9}

Then the single critical orbit decomposes coefficient one as

\[
 \boxed{
 R_0
 =\epsilon_0R_0
 +\sum_\alpha\epsilon_\alpha R_0.
 }
 \tag{L-92102.10}

For each hypothetical off-line orbit `q_alpha`, `L-92101` gives

\[
 \mathcal E[q_\alpha+\epsilon_\alpha R_0]\ge0.
 \tag{L-92102.11}

The leftover block `epsilon_0 R_0` has zero reciprocal curvature.

Thus one already verified critical-line orbit contains vastly more curvature
reserve than is required to absorb every possible off-line orbit above the
verified height.

## 5. Exact boundary

```text
verified critical-line reserve below H*/2       EXTERNAL + RVM
per-orbit required fraction                      EXACT
reciprocal-square zero-tail bound                STANDARD EFFECTIVE
sum of all fractions <1                          PROPOSED COMPLETE
one critical orbit sufficient                    PROPOSED COMPLETE
full actual-Xi reciprocal concavity               L-92103
Riemann Hypothesis                               UNPROVED
```
