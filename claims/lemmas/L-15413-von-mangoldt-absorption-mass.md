# L-15413 — The positive primitive is an exact one-step absorption mass

Claim ID: `L-15413`  
Title: A log-windowed von Mangoldt chain identifies the RH remainder as cancellation inside a positive hitting probability  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15410`, `L-15412`; the von Mangoldt downward transition  
Scope: probabilistic interpretation of the positive route  
Related counterexample candidates: none

## Windowed starting law

Let `H_h>=0` be the compact kernel of `L-15410`. Define

\[
 Z_h(x)=((t\nu)*H_h)(x)
 =\sum_{N\ge2}\frac{\log N}{N}H_h(x-\log N).
 \tag{L-15413.1}
\]

Whenever `Z_h(x)>0`, define a probability law on integers by

\[
 \boxed{
 \pi_x(N)=
 \frac{(\log N)N^{-1}H_h(x-\log N)}{Z_h(x)}.}
 \tag{L-15413.2}
\]

Given `N`, make one step of the von Mangoldt downward chain:

\[
 \mathbb P(N_1=N/q\mid N_0=N)
 =\frac{\Lambda(q)}{\log N},
 \qquad q|N.
 \tag{L-15413.3}
\]

The divisor identity makes these probabilities sum to one.

## Exact absorption identity

The next state equals `1` exactly when the selected prime power is `q=N`.
Therefore

\[
\begin{aligned}
 \mathbb P_{\pi_x}(N_1=1)
 &=\sum_N\pi_x(N)\frac{\Lambda(N)}{\log N}\\
 &=\frac1{Z_h(x)}
   \sum_N\frac{\Lambda(N)}N H_h(x-\log N).
\end{aligned}
\]

The last numerator is the positive primitive `A_h` of `L-15410`. Hence

\[
 \boxed{
 A_h(x)=Z_h(x)\,
 \mathbb P_{\pi_x}(N_1=1).}
 \tag{L-15413.4}
\]

Thus `A_h` is not merely a positive prime sum. It is the exact total one-step
absorption mass of a finite log-windowed divisibility ensemble.

## Joint law and renewal equation

Writing `N=qm`, the joint law of the selected prime power and residual factor is

\[
 \boxed{
 \mathbb P_x(Q=q,M=m)=
 \frac{\Lambda(q)}{qm\,Z_h(x)}
 H_h(x-\log q-\log m).}
 \tag{L-15413.5}
\]

Summing over all factorizations `qm=N` recovers the starting law because

\[
 \sum_{q|N}\Lambda(q)=\log N.
\]

This is the probability-level version of

\[
 \mu*\nu=t\nu
\]

and of the renewal equation in `L-15412`.

## Asymptotic scale

Ordinary harmonic-sum estimates for the fixed compact kernel give

\[
 Z_h(x)=x\int H_h(u)du-\int uH_h(u)du+o(1),
 \tag{L-15413.6}
\]

while `L-15410` gives

\[
 A_h(x)\to\int H_h(u)du=\frac1h.
 \tag{L-15413.7}
\]

Consequently

\[
 \boxed{
 \mathbb P_{\pi_x}(N_1=1)=\frac1x+O_h(x^{-2})+o(x^{-1}).}
 \tag{L-15413.8}
\]

Higher Euler--Maclaurin and PNT expansions improve the algebraic asymptotic, but
they do not supply the critical exponential remainder.

## RH-scale cancellation

Differentiate (L-15413.4):

\[
 A_h'(x)=Z_h'(x)p_h(x)+Z_h(x)p_h'(x),
 \qquad
 p_h(x)=\mathbb P_{\pi_x}(N_1=1).
 \tag{L-15413.9}
\]

The two terms on the right are individually of polynomial size:

\[
 Z_h'p_h\asymp x^{-1},
 \qquad
 Z_hp_h'\asymp-x^{-1}.
 \tag{L-15413.10}
\]

The prime-window signal is

\[
 \boxed{
 Q_h(x)=e^{x/2}
 \bigl[Z_h'(x)p_h(x)+Z_h(x)p_h'(x)\bigr].}
 \tag{L-15413.11}
\]

Therefore boundedness requires cancellation between the two probability terms
to absolute scale `e^(-x/2)`. Ordinary positivity, a law of large numbers, a
finite-order asymptotic expansion, or generic Markov contractivity cannot yield
that conclusion by itself.

## A precise Markov-chain target

A successful probabilistic proof would need a critical score estimate for the
moving starting law:

\[
 \sup_{X\ge1}\frac1X
 \int_{x_0}^{x_0+X}
 e^x
 \left|
 Z_h'(x)p_h(x)+Z_h(x)p_h'(x)
 \right|^2dx<\infty.
 \tag{L-15413.12}
\]

Equivalently, one needs an exact martingale or flow representation in which the
large terms in (L-15413.10) cancel before applying an inequality. Bounding them
separately is structurally incapable of reaching RH.

## Relation to current von Mangoldt-chain work

The downward transition (L-15413.3), its invariant weights, upward adjoint, and
continuous zeta process have recently proved effective in divisibility-poset
problems. The present absorption identity imports that architecture into the RH
programme, but at a much sharper scale: the needed estimate is an
`e^(-x/2)` cancellation in a moving absorption probability.

This suggests studying:

1. a compensated absorption martingale for the zeta process;
2. a carré-du-champ identity for the upward/downward adjoint pair;
3. a critical Poincare inequality for log-windowed starting laws;
4. a matrix-valued score retaining the prime-pair cancellation of `L-15411`.

## Gap audit

- The absorption identity is exact.
- The displayed algebraic asymptotic is not the RH-scale estimate.
- Standard concentration of a random chain does not control the deterministic
  arithmetic variation of its starting-law absorption probability.
- No compensated martingale with the required critical quadratic variation is
  currently constructed.
- This lemma identifies a positive probabilistic target; it does not prove it.
