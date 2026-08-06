# L-15440 — Uniform positivity in the small-product boundary corner

Claim ID: `L-15440`  
Title: The smoothed-Jordan density is uniformly positive whenever `st` stays below any fixed value smaller than `log 2` and the translation is sufficiently large  
Status: `PROPOSED — COMPLETE ELEMENTARY PROOF; CLOSES THE s t -> 0 ESCAPE CORNER`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15430`, `L-15431`, `L-15435`; elementary beta-tail bounds and the integral comparison for zeta  
Scope: the first of the two escape corners isolated by `L-15438`  
Related counterexample candidates: none

## 1. Setup

For `0<s<1`, retain

\[
 F_s(n)=\prod_{p\mid n}(1-p^{-s}),
 \qquad
 c_s={1\over\zeta(1+s)},
 \tag{L-15440.1}
\]

and the positive beta-resolvent kernel

\[
 n_s(t)
 ={\pi^{s/2}\over\Gamma(s/2)}
 e^{-st}
 B_{1-e^{-2t}}
 \left({s\over2},{3\over2}-{s\over2}\right),
 \qquad t\ge0.
 \tag{L-15440.2}
\]

Put

\[
 I_s(t)=\int_0^t n_s(r)\,dr
 \tag{L-15440.3}
\]

and

\[
 \boxed{
 Y_s(t)
 =\sum_{\log n\le t}{F_s(n)\over n}
 n_s(t-\log n)
 -c_s I_s(t).}
 \tag{L-15440.4}
\]

This is the regular density whose global nonnegativity is the surviving
smoothed-Jordan gate of `L-15430`.  Since

\[
F_s(1)=1,
\]

the single `n=1` term already gives

\[
 \boxed{Y_s(t)\ge n_s(t)-c_sI_s(t).}
 \tag{L-15440.5}
\]

The proof below shows that this elementary lower bound is sufficient in an
entire two-parameter wedge.

## 2. Complete-beta amplitude and the omitted-tail ratio

Write

\[
 a={s\over2},
 \qquad
 b={3-s\over2},
 \qquad
 \delta=e^{-2t}.
 \tag{L-15440.6}
\]

Then

\[
0<a<\frac12,
\qquad
1<b<\frac32,
\qquad
a+b=\frac32.
\]

Define the complete-beta amplitude

\[
 \boxed{
 \kappa_s
 =\pi^{s/2}{\Gamma((3-s)/2)\over\Gamma(3/2)}>0.}
 \tag{L-15440.7}
\]

Since

\[
{\pi^{s/2}\over\Gamma(a)}B(a,b)=\kappa_s,
\]

there is an exact representation

\[
 \boxed{
 n_s(t)=\kappa_s e^{-st}\bigl(1-\varepsilon_s(t)\bigr),}
 \tag{L-15440.8}
\]

where

\[
 \varepsilon_s(t)
 ={1\over B(a,b)}
 \int_{1-\delta}^1u^{a-1}(1-u)^{b-1}\,du
 \tag{L-15440.9}
\]

is the relative omitted beta tail.

### Uniform tail bound

Substitute `v=1-u`.  Since `a-1>-1` and `a-1<0`,

\[
\begin{aligned}
 \int_{1-\delta}^1u^{a-1}(1-u)^{b-1}du
 &=\int_0^\delta(1-v)^{a-1}v^{b-1}dv\\
 &\le{\delta^b\over b(1-\delta)}.
\end{aligned}
 \tag{L-15440.10}
\]

On the other hand,

\[
\begin{aligned}
 B(a,b)
 &\ge\int_0^{1/2}u^{a-1}(1-u)^{b-1}du\\
 &\ge 2^{-(b-1)}{2^{-a}\over a}
 ={2^{-1/2}\over a},
\end{aligned}
 \tag{L-15440.11}
\]

because `a+b=3/2`.  Therefore

\[
 \varepsilon_s(t)
 \le {\sqrt2a\over b(1-\delta)}\delta^b.
 \tag{L-15440.12}
\]

Using `2a=s<1`, `b>1`, and `0<delta<1`, one obtains the completely uniform
bound

\[
 \boxed{
 0\le\varepsilon_s(t)
 \le
 {e^{-2t}\over\sqrt2(1-e^{-2t})}
 =:\varepsilon_*(t).}
 \tag{L-15440.13}
\]

The function `epsilon_*` is strictly decreasing and tends to zero
exponentially.

## 3. Uniform primitive upper bound

The incomplete beta function is bounded by the complete beta function, so

\[
 \boxed{0\le n_s(r)\le\kappa_s e^{-sr}.}
 \tag{L-15440.14}
\]

Consequently

\[
 \boxed{
 I_s(t)
 \le {\kappa_s\over s}\bigl(1-e^{-st}\bigr).}
 \tag{L-15440.15}
\]

A decreasing integral comparison gives

\[
 \zeta(1+s)
 =\sum_{n\ge1}n^{-1-s}
 >\int_1^\infty x^{-1-s}dx
 ={1\over s}.
 \tag{L-15440.16}
\]

Thus

\[
 \boxed{0<{c_s\over s}<1.}
 \tag{L-15440.17}
\]

No asymptotic expansion of zeta is needed.

## 4. Explicit lower moat

Put

\[
 \lambda=st.
 \tag{L-15440.18}
\]

Combining (L-15440.5), (L-15440.8), (L-15440.15), and
(L-15440.17) gives

\[
\begin{aligned}
Y_s(t)
&\ge
\kappa_s e^{-\lambda}(1-\varepsilon_s(t))
-c_s{\kappa_s\over s}(1-e^{-\lambda})\\
&>
\kappa_s\left[
 e^{-\lambda}(1-\varepsilon_s(t))
 -(1-e^{-\lambda})
\right].
\end{aligned}
 \tag{L-15440.19}
\]

Hence

\[
 \boxed{
 Y_s(t)
 >\kappa_s\left[
 2e^{-\lambda}-1-e^{-\lambda}\varepsilon_s(t)
 \right].}
 \tag{L-15440.20}
\]

Using (L-15440.13),

\[
 \boxed{
 Y_s(t)
 >\kappa_s\left[
 2e^{-st}-1-arepsilon_*(t)
 \right].}
 \tag{L-15440.21}
\]

This is a fully explicit, unconditional lower bound on the regular density.

## 5. Uniform small-product positivity theorem

Fix any

\[
 \boxed{0<\Lambda<\log2.}
 \tag{L-15440.22}
\]

Choose `T_Lambda` so that

\[
 \boxed{
 \varepsilon_*(T_\Lambda)
 <2e^{-\Lambda}-1.}
 \tag{L-15440.23}
\]

Such a finite value exists because the right side is positive and
`epsilon_*(t)->0`.  For every

\[
0<s<1,
\qquad
t\ge T_\Lambda,
\qquad
st\le\Lambda,
 \tag{L-15440.24}
\]

one has

\[
\begin{aligned}
Y_s(t)
&>\kappa_s
 \left[2e^{-st}-1-\varepsilon_*(t)\right]\\
&\ge\kappa_s
 \left[2e^{-\Lambda}-1-\varepsilon_*(T_\Lambda)\right]
>0.
\end{aligned}
 \tag{L-15440.25}
\]

Therefore

\[
 \boxed{
 \forall\Lambda<\log2\ \exists T_\Lambda:\quad
 t\ge T_\Lambda,\ st\le\Lambda
 \Longrightarrow Y_s(t)>0.}
 \tag{L-15440.26}
\]

The theorem is uniform in the entire shift range `0<s<1`.

An explicit admissible threshold is obtained by solving

\[
 {e^{-2T}\over\sqrt2(1-e^{-2T})}
 <2e^{-\Lambda}-1.
 \tag{L-15440.27}
\]

No prime estimate, zero-free region, or finite computation enters the result.

## 6. Closure of the first escape corner

`L-15438` proves that any negative endpoint sequence with

\[
s_j\downarrow0,
\qquad
t_j=\log N_j\to\infty
 \tag{L-15440.28}
\]

must escape through one of

\[
s_jt_j\to0
\qquad\text{or}\qquad
s_jt_j\to\infty.
 \tag{L-15440.29}
\]

The first alternative is impossible.  Indeed, choose any fixed
`Lambda<log2`; eventually

\[
s_jt_j\le\Lambda,
\qquad
t_j\ge T_\Lambda,
\]

and (L-15440.26) gives `Y_(s_j)(t_j)>0`, a contradiction.

Thus every possible counterexample sequence is forced into the sole remaining
corner

\[
 \boxed{
 s_j\downarrow0,
 \qquad
 t_j\to\infty,
 \qquad
 s_jt_j\to\infty.}
 \tag{L-15440.30}
\]

This is a strict global reduction: the small-product corner is closed by an
explicit positive moat, not merely by vague or local-uniform convergence.

## 7. Why the proof works

The mechanism is elementary but structural.

1. The arithmetic measure contains the exact atom `n=1` with coefficient one.
2. On the scale `st<log2`, the surviving value of that atom is larger than the
   maximum possible continuous beta mass accumulated before time `t`.
3. Every further arithmetic atom is nonnegative and therefore only strengthens
   the inequality.
4. The incomplete-beta boundary loss is exponentially small in the untranslated
   variable `t`, uniformly in `s`.

The constant `log2` is the point at which the limiting elementary moat

\[
2e^{-st}-1
\]

changes sign.  The theorem does not claim that `log2` is the optimal boundary
once the positive `n>1` atoms are used.

## 8. Consequence for the full RH attack

Combining `L-15436`--`L-15440`, the smoothed-Jordan route now has the following
geometry:

```text
fixed s away from zero:
    eventual positivity;

s -> 0 with bounded positive st:
    local-uniform positive limit;

s -> 0 with st -> 0:
    uniform explicit positive moat (this lemma);

sole surviving regime:
    s -> 0, t -> infinity, st -> infinity.
```

A complete proof of positivity in that last large-product corner would prove
`Y_s(t)>=0` everywhere after a finite compact verification, then close the
regular Volterra form and the RH-bearing operator route.

The next attack should therefore target a uniform version of the rightmost-pole
asymptotic of `L-15436` in the regime `st->infinity`, or an arithmetic
prime-adjoining invariant that is strengthened rather than weakened by large
`st`.

## 9. Proof boundary

- Every inequality in this file is elementary and explicit.
- The result uses only the `n=1` term and therefore makes no hidden
  prime-distribution assumption.
- It closes the entire `st->0` counterexample corner and a larger uniform wedge
  `st<=Lambda<log2`.
- It does not control the remaining large-product corner `st->infinity` and
  does not by itself prove the global smoothed-Jordan inequality or RH.
