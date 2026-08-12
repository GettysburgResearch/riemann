# R-91330 — No fixed contraction can send the completed Fisher curve to all safe Suzuki phase multipliers

Claim ID: `R-91330`  
Status: **PROVED EXACT ALL-SCALE FIXED-COLLIGATION NO-GO THEOREM**  
Created: 2026-08-13  
Refutes: the unaugmented fixed scattering observation left open in `L-91309.6`--`L-91309.8`  
Does not refute: a local construction at one scale, an augmented source with extra all-pass curvature, or an unbounded observation  
RH status: **unproved**

## 1. The proposed completed Fisher isometries

Retain the fixed Riemann-density source space and the normalized tilt vectors
of `L-91309`:

\[
 \mathcal S=L^2(\mathbb R,Q(y)dy),
 \qquad
 q_a(y)=\xi(\tfrac12+a)^{-1/2}e^{-ay/2}.
 \tag{R-91330.1}
\]

Let

\[
 (V_af)(t,y)=e^{ity}q_a(y)f(t)
 \tag{R-91330.2}
\]

on `L2(R_t)`. Each `V_a` is an isometry. The exact Fisher tangent is

\[
 \partial_aq_a(y)
 =-\frac12(y-\mathbb E_aY)q_a(y),
 \tag{R-91330.3}
\]

so

\[
 \boxed{
 \|\partial_aV_a\|
 =\|\partial_aq_a\|_{\mathcal S}
 =\frac12\sqrt{\operatorname{Var}_a(Y)}.
 }
 \tag{R-91330.4}
\]

The desired output family is multiplication by

\[
 \Theta_a(t)
 =\frac{\xi(\frac12+a+it)}
        {\xi(\frac12+a-it)},
 \qquad a>\frac12.
 \tag{R-91330.5}
\]

## 2. A fixed contraction imposes a speed inequality

Suppose that one Hilbert space `T` contains every range of `V_a` and that a
single contraction

\[
 C:\mathcal T\to L^2(\mathbb R_t)
 \]

satisfies

\[
 \boxed{CV_a=M_{\Theta_a}}
 \tag{R-91330.6}
\]

for every `a` in an interval. Differentiating in operator norm gives

\[
 C\partial_aV_a=M_{\partial_a\Theta_a}.
 \tag{R-91330.7}
\]

Therefore

\[
 \boxed{
 \|\partial_a\Theta_a\|_{L^\infty}
 \le\frac12\sqrt{\operatorname{Var}_a(Y)}.
 }
 \tag{R-91330.8}
\]

Since `|Theta_a|=1` on the boundary,

\[
 |\partial_a\Theta_a|
 =|\partial_a\log\Theta_a|.
 \tag{R-91330.9}
\]

Equation (R-91330.8) is a necessary condition for the unaugmented fixed
completed-Fisher colligation.

## 3. The safe phase speed is at least pi/2

Put `sigma=1/2+a>1`. By `L-91328`,

\[
 \partial_a\log\Theta_a(t)
 =2i\operatorname{Im}\frac{\xi'}\xi(\sigma+it).
 \tag{R-91330.10}
\]

Use

\[
 \frac{\xi'}\xi(s)
 =\frac1s+\frac1{s-1}
 -\frac12\log\pi
 +\frac12\psi(s/2)
 +\frac{\zeta'}\zeta(s).
 \tag{R-91330.11}
\]

As `t to +infinity`, the rational imaginary parts tend to zero and

\[
 \operatorname{Im}\frac12\psi((\sigma+it)/2)
 \longrightarrow\frac\pi4.
 \tag{R-91330.12}
\]

It remains to suppress the absolutely convergent Euler logarithmic derivative
along a sequence. For fixed `sigma>1`,

\[
 \frac{\zeta'}\zeta(\sigma+it)
 =-\sum_{p^k}\frac{\log p}{p^{k\sigma}}
   e^{-itk\log p}
 \tag{R-91330.13}
\]

converges uniformly in `t`. Given `epsilon>0`, choose finitely many primes so
that the omitted tail has modulus below `epsilon`. The numbers `log p` for
distinct primes are rationally independent: an integer relation would
contradict unique factorization. Kronecker approximation therefore supplies
arbitrarily large `t` for which every retained `t log p` is within an
arbitrarily small distance of an integer multiple of `2pi`. Every retained
prime-power term is then arbitrarily close to real. Hence there is a sequence
`t_j to infinity` with

\[
 \operatorname{Im}\frac{\zeta'}\zeta(\sigma+it_j)
 \longrightarrow0.
 \tag{R-91330.14}
\]

Combining (R-91330.10)--(R-91330.14) yields

\[
 \boxed{
 \|\partial_a\Theta_a\|_{L^\infty}
 =\|\partial_a\log\Theta_a\|_{L^\infty}
 \ge\frac\pi2
 \qquad(a>1/2).
 }
 \tag{R-91330.15}
\]

Continuity gives the same lower bound for the essential supremum.

## 4. The completed Fisher speed tends to zero

Since

\[
 \operatorname{Var}_a(Y)
 =\partial_a^2\log\xi(\tfrac12+a),
 \tag{R-91330.16}
\]

putting again `sigma=1/2+a` gives

\[
\begin{aligned}
 \operatorname{Var}_a(Y)
 ={}&-\frac1{\sigma^2}
    -\frac1{(\sigma-1)^2}
    +\frac14\psi_1(\sigma/2)\\
 &+\left(\frac{\zeta'}\zeta\right)'(\sigma).
\end{aligned}
 \tag{R-91330.17}
\]

The trigamma asymptotic and absolute Euler convergence give

\[
 \boxed{
 \operatorname{Var}_a(Y)
 =\frac1{2\sigma}+O(\sigma^{-2})
  +O(2^{-\sigma})
 \longrightarrow0
 \qquad(a\to\infty).
 }
 \tag{R-91330.18}
\]

Thus, for all sufficiently large safe scales,

\[
 \frac12\sqrt{\operatorname{Var}_a(Y)}<\frac\pi2.
 \tag{R-91330.19}
\]

Equations (R-91330.8), (R-91330.15), and (R-91330.19) are incompatible.

## 5. No-go conclusion

There is no single contraction `C` satisfying (R-91330.6) for all safe scales
`a>1/2` with the source isometries (R-91330.2). More generally, no such fixed
contraction exists on any interval containing all sufficiently large scales.

The obstruction is geometric:

```text
completed exponential-tilt state speed -> 0;
all-pass Suzuki phase speed             >= pi/2.
```

The gamma all-pass phase retains a nonvanishing asymptotic rotation that is not
present in the Fisher norm of the normalized amplitude state.

## 6. Correct repair boundary

The theorem does not rule out:

1. a colligation constructed only locally near one chosen scale where a
   separate speed inequality is verified;
2. a larger source isometry carrying an additional all-pass/gauge tangent of
   norm at least the missing phase speed;
3. an `a`-dependent observation, although that cannot be inserted into
   `L-91305` without connection terms;
4. an unbounded observation on a structured domain, such as the reciprocal-xi
   leg isolated in `L-91325`.

Any corrected fixed-colligation route must therefore augment the completed
Fisher curve. The source-normal curvature can no longer be identified solely
with `Var_a(Y)/4`.

## 7. Exact boundary

```text
completed Fisher source speed                       EXACT
necessary fixed-contraction speed inequality         EXACT
safe Suzuki phase speed >= pi/2                      EXACT
completed Fisher speed -> 0                          EXACT
one fixed contraction for all safe scales            IMPOSSIBLE
local or augmented fixed colligation                  NOT RULED OUT
unbounded structured observation                      NOT RULED OUT
completed source-minus-output block positivity        OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
