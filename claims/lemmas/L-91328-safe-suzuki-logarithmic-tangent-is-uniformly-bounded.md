# L-91328 — The safe Suzuki logarithmic tangent is uniformly bounded on the entire boundary

Claim ID: `L-91328`  
Status: **PROVED EXACT SAFE-LINE BOUNDED-TANGENT THEOREM**  
Created: 2026-08-13  
Depends on: `L-91325`; the absolutely convergent logarithmic derivative of zeta on `Re(s)>1`  
Strengthens: `L-91326` from the physical Cauchy core to the entire Suzuki model space  
RH status: **unproved**

## 1. Only the imaginary logarithmic derivative survives

Fix `a>1/2` and put

\[
 \sigma=\frac12+a>1.
 \tag{L-91328.1}
\]

On the real boundary,

\[
 \Theta_a(t)
 =\frac{\xi(\sigma+it)}{\xi(\sigma-it)}.
 \tag{L-91328.2}
\]

Let

\[
 \ell_a(t)=a\partial_a\log\Theta_a(t).
\]

Since `xi` is real on the real axis and has the usual conjugation symmetry,

\[
 \boxed{
 \ell_a(t)
 =a\left[
  \frac{\xi'}\xi(\sigma+it)
  -\frac{\xi'}\xi(\sigma-it)
 \right]
 =2ia\,\operatorname{Im}
  \frac{\xi'}\xi(\sigma+it).
 }
 \tag{L-91328.3}
\]

The real logarithmic growth of the gamma factor cancels exactly. This is
stronger than the crude absolute bound used in `L-91326`.

## 2. An explicit uniform bound

For `Re(s)>1`,

\[
 \frac{\xi'}\xi(s)
 =\frac1s+\frac1{s-1}
 -\frac12\log\pi
 +\frac12\psi(s/2)
 +\frac{\zeta'}\zeta(s).
 \tag{L-91328.4}
\]

The Euler logarithmic derivative converges absolutely, so

\[
 \left|
  \operatorname{Im}\frac{\zeta'}\zeta(\sigma+it)
 \right|
 \le
 -\frac{\zeta'}\zeta(\sigma).
 \tag{L-91328.5}
\]

The rational terms satisfy

\[
 \left|\operatorname{Im}\frac1{x+it}\right|
 \le\frac1{2x}
 \qquad(x>0).
 \tag{L-91328.6}
\]

For `x>0`, the convergent digamma series gives

\[
 \operatorname{Im}\psi(x+iy)
 =\sum_{n=0}^\infty
  \frac{y}{(n+x)^2+y^2}.
 \tag{L-91328.7}
\]

The first term plus the integral comparison yields

\[
 \left|\operatorname{Im}\psi(x+iy)\right|
 \le\frac1{2x}+\frac\pi2.
 \tag{L-91328.8}
\]

Using `x=sigma/2` in (L-91328.8), equations
(L-91328.4)--(L-91328.8) give the explicit uniform estimate

\[
\boxed{
 \|\ell_a\|_{L^\infty(\mathbb R)}
 \le 2a\left[
  \frac1\sigma
  +\frac1{2(\sigma-1)}
  +\frac\pi4
  -\frac{\zeta'}\zeta(\sigma)
 \right].
}
 \tag{L-91328.9}
\]

In particular,

\[
 \boxed{\ell_a\in L^\infty(\mathbb R).}
 \tag{L-91328.10}
\]

No zero-density theorem and no information near the critical line is used.

## 3. The Suzuki tangent is bounded on the full model space

On the boundary,

\[
 \dot\Theta_a=a\partial_a\Theta_a=\Theta_a\ell_a.
\]

Since `|Theta_a|=1`, equation (L-91328.10) implies

\[
 \dot\Theta_a\in L^\infty,
 \qquad
 \|\dot\Theta_a\|_\infty=\|\ell_a\|_\infty.
 \tag{L-91328.11}
\]

Thus the multiplier derivative is bounded on `H2`, and the canonical shape
operator

\[
 \mathcal J_a
 =\sqrt2M_{\dot\Theta_a}^*P_{K_{\Theta_a}}
 =-\sqrt2P_+M_{\ell_a}\mathcal U_{\Theta_a}
 \tag{L-91328.12}
\]

extends to all of `K_(Theta_a)`, with

\[
 \boxed{
 \|\mathcal J_a\|
 \le\sqrt2\,\|\ell_a\|_\infty.
 }
 \tag{L-91328.13}
\]

Consequently the corrected domain of `L-91325` is simply

\[
 \boxed{
 \mathcal D_a=K_{\Theta_a}.
 }
 \tag{L-91328.14}
\]

The logarithmic `A2` argument of `L-91326` remains a valid stronger weighted
localization statement for the raw rational packets and bridge, but it is no
longer needed merely to define the tangent.

## 4. The corrected reciprocal-amplitude composite is defined everywhere

Retain the bounded renormalized source map `B_a`, score coisometry `C_a`, and
reciprocal-amplitude Toeplitz leg `T_(varphi,a)` from `L-91325`. For every
`g in K_(Theta_a)`,

\[
 \mathcal C_a\mathcal B_ag
 =-\frac{\varphi_a\ell_a}{a\sqrt{V_a}}
   \mathcal U_{\Theta_a}g.
 \tag{L-91328.15}
\]

Because `ell_a` is bounded,

\[
 \frac{\mathcal C_a\mathcal B_ag}{\varphi_a}
 =-\frac{\ell_a}{a\sqrt{V_a}}
   \mathcal U_{\Theta_a}g
 \in L^2.
 \tag{L-91328.16}
\]

Hence

\[
 \boxed{
 \mathcal C_a\mathcal B_a(K_{\Theta_a})
 \subseteq\operatorname{Dom}(\mathfrak T_{\varphi,a}).
 }
 \tag{L-91328.17}
\]

The corrected factorization therefore holds on the entire model space:

\[
 \boxed{
 \mathcal J_a
 =a\sqrt{2V_a}\,
  \mathfrak T_{\varphi,a}
  \mathcal C_a\mathcal B_a
 \quad\text{on }K_{\Theta_a}.
 }
 \tag{L-91328.18}
\]

Although `T_(varphi,a)` remains unbounded on ambient `L2`, its structured
composite is bounded:

\[
 \boxed{
 \|\mathfrak T_{\varphi,a}
       \mathcal C_a\mathcal B_ag\|_{H^2}
 \le
 \frac{\|\ell_a\|_\infty}{a\sqrt{V_a}}
 \|g\|_{K_{\Theta_a}}.
 }
 \tag{L-91328.19}
\]

This is a bound after parameterization by the model-space input. It does not
assert that `T_(varphi,a)` is bounded on the score range with its inherited
ambient norm, and it does not supply the required arithmetic source metric.

## 5. Correct remaining theorem

The analytic domain and raw reciprocal-amplitude amplification are no longer
obstructions on the structured Suzuki range. The RH-bearing statement is the
metric comparison

\[
 \boxed{
 C_a^{\rm Jordan+gamma+pole}
 \succeq \mathcal J_a^*\mathcal J_a
 }
 \tag{L-91328.20}
\]

on the full model space, or equivalently on the finite pole-jet packets of
`L-91327` plus the reflected and bridge blocks.

A proof must identify the completed source metric seen by the bounded composite
in (L-91328.18). Boundedness in the ordinary model-space norm alone is not the
coefficient-one source domination required by `T-91008`.

## 6. Exact boundary

```text
safe logarithmic phase tangent ell_a                   UNIFORMLY BOUNDED
multiplier derivative dotTheta_a                       BOUNDED
Suzuki shape operator on all K_(Theta_a)                BOUNDED
corrected reciprocal-xi composite domain                ALL K_(Theta_a)
structured composite norm bound                         EXACT
ambient reciprocal-xi Toeplitz operator                 STILL UNBOUNDED
arithmetic-source metric >= tangent metric              OPEN / RH-BEARING
mixed orientation and bridge arithmetic block           OPEN
Riemann Hypothesis                                      UNPROVED
```
