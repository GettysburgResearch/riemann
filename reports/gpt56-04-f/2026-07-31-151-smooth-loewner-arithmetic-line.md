# Agent report — actual smooth target to arithmetic scalar line

Agent: `gpt56-04-f`  
Branch: `agent/gpt56-04-f/151-finsler-target-completion`  
Date: 2026-07-31  
Status: **finite proof-producing pipeline completed; cofinal arithmetic theorem not proved**

## Objective

Continue after the corrected PR #173 audit and implement the requested chain

```text
actual smooth-window coefficient intervals
  -> directed canonical Loewner inertia
  -> actual arithmetic residue-line / threshold test
  -> cofinal source comparison.
```

## Opus correction audit

The latest PR #173 corrections are materially sound:

- the original census used full `Xi` samples instead of the finite target it
  defined;
- the hard-window follow-up shows that this substitution can reverse a verdict;
- Reading A, allowing arbitrary positive special completion, is equivalent to
  RH/Laguerre--Polya closure and is not a structural reduction;
- the fixed arithmetic source plus one scalar is the only noncircular reading.

The hard-window computations remain ordinary high-precision evidence, not a
directed result for the production smooth cutoff.

## L-15117 — actual smooth coefficients

For `ell=log(lambda)`, the actual CCM coefficient is

\[
 p_n^{sm}=(-1)^n(2ell)^{-1/2}
 \int chi_ell(t)K(t)e^{-i pi n t/ell}dt.
\]

The corrected full sample is

\[
 p_n^{full}=(-1)^n\Xi(pi n/ell)/(4\sqrt{2ell}).
\]

The uniform analytic radius is

\[
 |p_n^{sm}-p_n^{full}|
 \le \frac{\sqrt2 C_H}{\pi\sqrt ell}
       (lambda/e)^{5/2}e^{-\pi(lambda/e)^2}.
\]

This closes the first interface without hard-window quadrature.

## L-15118 — canonical construction and moat

The canonical source is constructed directly from the coefficient vector:

\[
 g_i=-\sum_{j\ne i}
 \frac{1+p_j/p_i}{\lambda_i-\lambda_j}.
\]

The diagonal is forced from the exact target kernel.  For simple real roots, a
Cauchy determinant gives an explicit positive moat fallback; directed
`LDL^T` is the preferred production certificate.

## L-15119 — actual arithmetic source

In the integer CCM basis, with `L=2 log(lambda)`, the exact Weil source is

\[
 \beta_n=
 32L\sinh^2(L/4)\frac{n}{L^2+16\pi^2n^2}
 +\frac1\pi\int_0^L
  \sin(2\pi nx/L)\frac{e^{x/2}}{e^x-e^{-x}}dx
 +\frac1\pi\sum_{1<q\le e^L}
  \frac{\Lambda(q)}{\sqrt q}
  \sin(2\pi n\log q/L).
\]

The last sum contains every prime power.  The arithmetic scalar line has source
`beta_n-c n`.

## L-15120 — scale correction and exact LP

The initially requested statistic

```text
inf_c E_p(c)/m_can
```

is not scale invariant.  An exact three-node control has

```text
T_p(2)=3 Q_can
```

but fails comparison with the single point `Q_can`.

The corrected statistic is

\[
 \Theta=\frac1{m_{can}}
 \inf_{t>0,q}
 \max_i\sum_{j\ne i}
 \left(1+|p_j/p_i|\right)
 |tA_{ij}-Q^{can}_{ij}-q|.
\]

It is a two-variable convex piecewise-linear rational LP.  `Theta<1` is a proof
of the actual arithmetic scalar completion.  `limsup Theta_j<1`, together with
target convergence and canonical inertia, proves RH.

## X-15106 exact control

The Fraction-only checker reconstructs the canonical source, moat, arithmetic
matrix, target kernel, complete scaled matrix difference, and independent
complement `LDL^T`.

Retained synthetic result:

```text
canonical source             (3,0,-3)
canonical positive spectrum  9,9
certified moat                8
canonical scale               3
boundary scalar               2
scaled difference             0
scaled moat                   24
arithmetic LDL pivots         54,81/2
unscaled row difference       24 > 8
```

Eight adversarial exact-Fraction replays pass.  Certificate digest:

```text
d13e9f4bf7178c356f87cba37bbea8569e531075d809aae17e2e146ed154c4ab
```

## L-15121 — polynomial differential residual

Define

\[
 R_0(s)=\sum_i p_i\beta_i\phi_i(s).
\]

The complete source mismatch is the single polynomial

\[
 E_{a,c,d}
 =R_0-c(sP+\Omega)+aP'-dP.
\]

At a node,

\[
 E(\lambda_i)/P(\lambda_i)
 =\beta_i-c\lambda_i-a g_i-d.
\]

At a simple target root,

\[
 w_k(c)-a=E(r_k)/P'(r_k).
\]

Thus exact canonical-ray equality is one polynomial identity, and direct
arithmetic residue positivity follows from the rootwise inequalities
`|E(r_k)|<a|P'(r_k)|`.  This can be sharper than the row-sum LP.

## T-15105 — completed composition theorem

The following proof-producing implication is now explicit:

```text
directed smooth coefficients
+ canonical PSD/corank-one and moat
+ directed complete arithmetic source
+ rational LP point below the moat
+ local-uniform target convergence
=> RH.
```

The finite consumers and analytic interfaces are complete.

## Exact unresolved theorem

No cofinal Riemann production sequence has been certified.  The remaining
load-bearing statement is either

\[
 \limsup_j\Theta_j<1
\]

or direct positivity of every arithmetic residue weight on an unbounded
diagonal.

This is not a numerical precision gap.  Canonical positivity for a convergent
target sequence is already RH-bearing, and the fixed arithmetic source is where
the explicit formula must supply the noncircular content.

## Repository actions

- reviewed the latest corrected head of PR #173;
- posted the scale/inertia audit to PR #173;
- updated Issue #176 with the new proof interface;
- pushed `L-15117`--`L-15121`, `T-15105`, `M-15103`, and `X-15106`.

No proof of RH is claimed.