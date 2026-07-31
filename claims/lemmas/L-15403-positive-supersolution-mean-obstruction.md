# L-15403 — Positive scalar supersolutions have an exponential mean obstruction

Claim ID: `L-15403`  
Title: No positive scalar Barta family can close the odd localized Weil floor  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15401`, `L-15402`; elementary symmetrization; optionally the prime number theorem for the sharp asymptotic  
Scope: the signed-edge Barta residual `b_{a,psi}^{odd}` of `L-15402`  
Related counterexample candidates: none

## Executive statement

Let `J_a^{odd}` and `W_a^{odd}` be the complete half-interval signed-edge data
from `L-15402`. For every strictly positive admissible scalar supersolution
`psi`, define

\[
 b_{a,\psi}^{\rm odd}(x)
 =W_a^{\rm odd}(x)
 +\frac1{\psi(x)}
  \int_{(0,1)}(\psi(x)-\psi(y))J_{a,x}^{\rm odd}(dy).
 \tag{L-15403.1}
\]

Whenever the displayed quantities are finite, one has

\[
 \boxed{
 \operatorname*{ess\,inf}_{0<x<1}b_{a,\psi}^{\rm odd}(x)
 \le \int_0^1 W_a^{\rm odd}(x)\,dx.}
 \tag{L-15403.2}
\]

The right side is independent of `psi` and satisfies

\[
 \boxed{
 \int_0^1 W_a^{\rm odd}(x)\,dx
 \le C-\frac{32}{a}
       \bigl(\cosh(a/2)-1\bigr)^2}
 \tag{L-15403.3}
\]

for every `a>=1`, with one absolute finite constant `C` depending only on the
normalization constant `A` in Suzuki's equation (2.2). Consequently, for all
sufficiently large `a`,

\[
 \boxed{
 \sup_{\psi>0}
 \operatorname*{ess\,inf}b_{a,\psi}^{\rm odd}
 \le -\frac{e^a}{a}.}
 \tag{L-15403.4}
\]

In particular there is **no** cofinal family of positive scalar supersolutions
satisfying

\[
 \operatorname*{ess\,inf}b_{a_j,\psi_j}^{\rm odd}
 \ge -2\varepsilon_j,
 \qquad
 a_j\to\infty,
 \qquad
 \varepsilon_j\to0.
 \tag{L-15403.5}
\]

The sharply defined missing object proposed in `L-15402` therefore does not
exist. The signed-edge Barta identity remains exact, but its scalar local term
discards the essential frustration energy carried by the `+` cross-origin
squares.

With the prime number theorem one obtains the sharper asymptotic

\[
 \boxed{
 \int_0^1W_a^{\rm odd}(x)\,dx
 =-\frac{16e^a}{a}\bigl(1+o(1)\bigr).}
 \tag{L-15403.6}
\]

## Part I — universal mean obstruction for a signed-edge Barta residual

Let `(X,mu)` have finite positive measure, let `J` be a symmetric nonnegative
edge measure, and let `sigma(x,y)` be any symmetric unit-modulus edge phase.
The signed ground-state identity of `L-15402` has the local residual

\[
 b_\psi(x)=W(x)+\frac{L_J\psi(x)}{\psi(x)},
 \qquad
 L_J\psi(x)=\int(\psi(x)-\psi(y))J_x(dy).
 \tag{L-15403.7}
\]

The edge phase does not occur in `b_psi`. Symmetry gives the exact identity

\[
\begin{aligned}
 \int_X\frac{L_J\psi(x)}{\psi(x)}\,d\mu(x)
 &={1\over2}\int_{X\times X}
 \left(2-\frac{\psi(y)}{\psi(x)}
        -\frac{\psi(x)}{\psi(y)}\right)J(dx,dy)\\
 &=-{1\over2}\int_{X\times X}
 \frac{(\psi(x)-\psi(y))^2}
      {\psi(x)\psi(y)}J(dx,dy)
 \le0.
\end{aligned}
 \tag{L-15403.8}
\]

If a singular kernel requires a diagonal cutoff, (L-15403.8) first holds for
every cutoff. Passing to the limit by monotone convergence either preserves the
identity or makes the left side `-infinity`, which only strengthens the result.

Since the essential infimum does not exceed the mean,

\[
 \operatorname*{ess\,inf}b_\psi
 \le {1\over\mu(X)}\int_Xb_\psi\,d\mu
 \le {1\over\mu(X)}\int_XW\,d\mu.
 \tag{L-15403.9}
\]

Applying this on `X=(0,1)` proves (L-15403.2).

### Why edge signs cannot repair the local term

For a negative signed edge, the nonnegative remainder contains

\[
 \psi(x)\psi(y)
 \left|{f(x)\over\psi(x)}
       +{f(y)\over\psi(y)}\right|^2.
\]

This can be very large, but it is omitted from the pointwise lower floor. The
mean identity (L-15403.8) records the resulting loss. A scalar positive
supersolution therefore cannot exploit sign frustration, regardless of how it
is fitted.

## Part II — exact mean of the odd Suzuki potential

Recall

\[
 W_a^{\rm odd}(x)=2V_a(x)-8aS_as_a(x),
 \qquad
 s_a(x)=\sinh(ax/2),
 \qquad
 S_a=\int_0^1s_a(x)dx.
 \tag{L-15403.10}
\]

The polar contribution is exact:

\[
 -8aS_a\int_0^1s_a(x)dx
 =-8aS_a^2
 =-\frac{32}{a}\bigl(\cosh(a/2)-1\bigr)^2.
 \tag{L-15403.11}
\]

For `0<delta<=2`, the degree function from `L-15401` satisfies

\[
 \boxed{\int_0^1d_\delta(x)dx=2-\delta.}
 \tag{L-15403.12}
\]

Indeed, the right-neighbor indicator has length `(1-delta)_+`, while the
left-neighbor indicator has length `1` for `delta<=1` and `2-delta` for
`delta>=1`.

The even cancellation potential satisfies

\[
 \boxed{
 \int_0^1U_a(x)dx
 =\int_0^2(2-t)F_a(t)dt.}
 \tag{L-15403.13}
\]

This follows either from the interval-difference measure or by integrating the
even function `U_a` over half of the full square.

Finally,

\[
 \int_0^1\log(1-x^2)dx=2\log2-2.
 \tag{L-15403.14}
\]

Combining (L-15403.11)--(L-15403.14) with `L-15401.11` yields the exact formula

\[
\boxed{
\begin{aligned}
 \int_0^1W_a^{\rm odd}(x)dx
 ={}&\mathcal A_a
 -2\sum_{n\le e^{2a}}{\Lambda(n)\over\sqrt n}
       \left(2-{\log n\over a}\right)\\
 &-\frac{32}{a}\bigl(\cosh(a/2)-1\bigr)^2,
\end{aligned}}
 \tag{L-15403.15}
\]

where

\[
\boxed{
 \mathcal A_a=
 -2\log a-2(2A+1)+2-2\log2
 +2\int_0^2(2-t)F_a(t)dt.}
 \tag{L-15403.16}
\]

Every summand in the prime sum is nonnegative because `log n<=2a`.

## Part III — the archimedean mean is bounded above

Put

\[
 H(u)={1\over2u}-{e^{-u/2}\over1-e^{-2u}}.
 \tag{L-15403.17}
\]

The cancellation at the origin gives `H(0)=-1/4`; thus `H` is bounded on
`[0,1]`. Since `F_a(t)=aH(at)`,

\[
 \int_0^2(2-t)F_a(t)dt
 =\int_0^{2a}\left(2-{u\over a}\right)H(u)du.
 \tag{L-15403.18}
\]

For `u>=1`,

\[
 H(u)\le {1\over2u}
 \tag{L-15403.19}
\]

because the omitted second term is positive. Hence, for `a>=1`,

\[
\begin{aligned}
 \int_0^{2a}\left(2-{u\over a}\right)H(u)du
 &\le C_0+
 \int_1^{2a}\left({1\over u}-{1\over2a}\right)du\\
 &\le C_0+\log(2a)
\end{aligned}
 \tag{L-15403.20}
\]

for one finite constant `C_0`. The `-2 log a` in (L-15403.16) cancels this
possible logarithmic growth, proving

\[
 \boxed{\mathcal A_a\le C\qquad(a\ge1).}
 \tag{L-15403.21}
\]

Dropping the nonpositive prime term in (L-15403.15) proves (L-15403.3).
For `a>=2 log 4`,

\[
 \cosh(a/2)-1\ge {1\over4}e^{a/2},
 \tag{L-15403.22}
\]

so the polar term is at most `-2e^a/a`. Exponential growth eventually dominates
the constant `C`, proving (L-15403.4).

## Part IV — optional sharp asymptotic from the prime number theorem

Let

\[
 P_a=\sum_{n\le e^{2a}}{\Lambda(n)\over\sqrt n}
       \left(2-{\log n\over a}\right).
 \tag{L-15403.23}
\]

The prime number theorem, in the form

\[
 \sum_{n\le x}\Lambda(n)=x+o(x),
\]

and partial summation give

\[
 P_a={4e^a\over a}\bigl(1+o(1)\bigr).
 \tag{L-15403.24}
\]

Also

\[
 {32\over a}\bigl(\cosh(a/2)-1\bigr)^2
 ={8e^a\over a}\bigl(1+o(1)\bigr),
 \tag{L-15403.25}
\]

while `mathcal A_a=O(1)`. Inserting these into (L-15403.15) proves
(L-15403.6).

## Consequences for the positive RH programme

1. The scalar signed-edge Barta proposal in `L-15402` cannot yield a cofinal
   lower envelope tending to zero.
2. Better splines, more knots, higher precision, and exact cellwise quadrature
   cannot overcome the obstruction.
3. The obstruction is not evidence against RH. It belongs to the **unsigned
   local minorant** created by the scalar ground-state transform, not to the
   original signed odd Weil form.
4. The cross-origin `+` squares and arithmetic phase coherence are
   load-bearing. A successful lower-floor proof must retain them globally.
5. Viable replacements include the phase-aware multiband Schur packet of
   `L-14308`--`L-14311`, or a genuinely matrix-valued/signed-system
   supersolution theorem that does not collapse all edge phases into the scalar
   local term.

## Gap audit

- The exact Suzuki decomposition and factors of two remain subject to the
  independent normalization audit already required by `L-15401`.
- Formula (L-15403.8) assumes the stated integrability; cutoff limits cover the
  singular continuous edge.
- The sharp coefficient `16` uses the prime number theorem, but the no-go result
  (L-15403.4) does not.
- This lemma refutes one proposed proof architecture. It neither proves nor
  disproves RH.
