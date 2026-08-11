# Macroscopic first-Hermite positivity: the remaining RH search is necessarily microscopic

**Status:** `PROPOSED COMPLETE UNCONDITIONAL PARTIAL-SIGN THEOREM — INDEPENDENT REVIEW REQUIRED`  
**RH status:** **unproved**  
**Depends on:** PR #379 first-Hermite zero-heat criterion; the standard Stirling/digamma bounds and Guinand--Weil normalization used in Anthropic Zeta23  

## 1. Purpose

PR #379 reduces RH to the sign of

\[
 \mathcal M(q,x)
 =\sum_\rho m_\rho(\gamma_\rho-x)^2
 e^{-q(\gamma_\rho-x)^2}.
 \tag{MP.1}
\]

This note proves two unconditional regions of positivity:

1. **broad heat kernels:** there exists an effective `q_*>0` such that
   \[
   \mathcal M(q,x)>0
   \qquad(0<q\le q_*,\ x\in\mathbb R);
   \tag{MP.2}
   \]
2. **far centres at fixed resolution:** for every fixed `q>0`, there is an effective `X(q)` such that
   \[
   \mathcal M(q,x)>0
   \qquad(|x|\ge X(q)).
   \tag{MP.3}
   \]

Thus a negative witness, if one exists, must move to finer heat resolution as its ordinate grows. For every fixed `q`, the unresolved centre set is compact.

The theorem does not control the diagonal regime `q -> infinity` with `x -> infinity`, which is precisely where an isolated off-line pair can be resolved.

## 2. Explicit-formula decomposition

Retain

\[
 h_{q,x}(z)=(z-x)^2e^{-q(z-x)^2}
 \tag{MP.4}
\]

and write the exact PR #379 formula as

\[
 \mathcal M(q,x)=P(q,x)+G(q,x)-\mathcal P(q,x),
 \tag{MP.5}
\]

where

\[
 P(q,x)=h_{q,x}(i/2)+h_{q,x}(-i/2),
 \tag{MP.6}
\]

\[
 G(q,x)=\int_\mathbb R h_{q,x}(\tau)\mu(\tau)d\tau,
 \tag{MP.7}
\]

\[
 \mu(\tau)={1\over2\pi}
 \left[
 \Re{\Gamma'\over\Gamma}\left({1\over4}+{i\tau\over2}\right)
 -\log\pi
 \right],
 \tag{MP.8}
\]

and

\[
 \begin{aligned}
 \mathcal P(q,x)
 ={1\over2\sqrt\pi q^{3/2}}
 \sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 &\left(1-{(\log n)^2\over2q}\right)\\
 &\cdot e^{-(\log n)^2/(4q)}\cos(x\log n).
 \end{aligned}
 \tag{MP.9}
\]

Stirling on the vertical line and compactness on bounded intervals give effective absolute constants `c_0,C_0>0` such that

\[
 \boxed{
 \mu(\tau)\ge c_0\log(2+|\tau|)-C_0
 \qquad(\tau\in\mathbb R).
 }
 \tag{MP.10}
\]

Only this coarse lower bound is needed.

## 3. Uniform lower bound for the gamma channel

Substitute `u=tau-x` and put

\[
 L(q,x)=\int_\mathbb R
 u^2e^{-qu^2}\log(2+|x+u|)du.
 \tag{MP.11}
\]

Pairing `u` and `-u`,

\[
 \begin{aligned}
 L(q,x)=\int_0^\infty u^2e^{-qu^2}
 \bigl[&\log(2+|x+u|)\\
 &+\log(2+|x-u|)\bigr]du.
 \end{aligned}
 \tag{MP.12}
\]

Since

\[
 \max(|x+u|,|x-u|)\ge u,
\]

one has the pointwise, centre-uniform inequality

\[
 \boxed{
 \log(2+|x+u|)+\log(2+|x-u|)
 \ge\log(2+u).
 }
 \tag{MP.13}
\]

For `0<q<=1`, restrict `(MP.12)` to

\[
 q^{-1/2}\le u\le2q^{-1/2}.
\]

Then `log(2+u)>=1/2 log(1/q)`, and after `v=sqrt(q)u`,

\[
 \boxed{
 L(q,x)
 \ge c_1q^{-3/2}\log(1/q)
 }
 \tag{MP.14}
\]

uniformly in `x`, where

\[
 c_1={1\over2}\int_1^2v^2e^{-v^2}dv>0.
\]

Also

\[
 \int_\mathbb R u^2e^{-qu^2}du
 ={\sqrt\pi\over2q^{3/2}}.
 \tag{MP.15}
\]

Equations `(MP.10)`, `(MP.14)`, and `(MP.15)` give

\[
 \boxed{
 G(q,x)
 \ge c_2q^{-3/2}\log(1/q)-C_2q^{-3/2}
 }
 \tag{MP.16}
\]

for `0<q<=1`, uniformly in `x`.

## 4. Pole and prime channels for small q

For the pole pair,

\[
 \begin{aligned}
 |P(q,x)|
 &\le2e^{q/4}(x^2+1/4)e^{-qx^2}\\
 &\le Cq^{-1}
 \qquad(0<q\le1),
 \end{aligned}
 \tag{MP.17}
\]

because `sup_(r>=0) r^2e^{-qr^2}=1/(eq)`.

For the prime term use `Lambda(n)<=log n` and absolute values. With `t=log n`, the all-integer envelope is

\[
 {1\over2\sqrt\pi q^{3/2}}
 {t\over\sqrt n}
 \left(1+{t^2\over2q}\right)e^{-t^2/(4q)}.
 \tag{MP.18}
\]

For sufficiently small `q`, its logarithmic derivative is negative already at `t=log 2`. Sum-integral comparison and

\[
 {t\over2}-{t^2\over4q}
 \le-{t^2\over8q}
 \tag{MP.19}
\]

for `q<=(log 2)/4` give constants `A,c,C>0` such that

\[
 \boxed{
 |\mathcal P(q,x)|
 \le Cq^{-A}e^{-c/q}
 }
 \tag{MP.20}
\]

uniformly in `x`.

Combining `(MP.16)`, `(MP.17)`, and `(MP.20)`, the positive term

\[
 c_2q^{-3/2}\log(1/q)
\]

dominates every negative allowance for all sufficiently small `q`. This proves `(MP.2)`.

### Theorem 4.1 — broad-kernel positivity

There is an effective absolute `q_*>0` such that

\[
 \boxed{
 \mathcal M(q,x)>0
 \qquad(0<q\le q_*,\ x\in\mathbb R).
 }
 \tag{MP.21}
\]

No zero-free region, zero-density estimate, or RH input is used.

## 5. Positivity at far centres for fixed q

Fix `q>0` and put `R=q^{-1/2}`. If `|x|>=2R`, then for `|u|<=R`,

\[
 |x+u|\ge|x|/2.
\]

Therefore

\[
 \begin{aligned}
 L(q,x)
 &\ge\log(2+|x|/2)
 \int_{|u|\le R}u^2e^{-qu^2}du\\
 &=c_q\log(2+|x|/2),
 \end{aligned}
 \tag{MP.22}
\]

where `c_q>0`. Equations `(MP.10)` and `(MP.15)` imply

\[
 \boxed{
 G(q,x)\ge c'_q\log(2+|x|)-C'_q.
 }
 \tag{MP.23}
\]

For fixed `q`, the prime series `(MP.9)` is absolutely convergent and its absolute value is bounded independently of `x`:

\[
 |\mathcal P(q,x)|\le B_q<\infty.
 \tag{MP.24}
\]

The pole term tends to zero exponentially as `|x|->infinity`. Hence `(MP.23)` dominates `(MP.24)` and the pole term outside an effective compact interval.

### Theorem 5.1 — fixed-resolution exterior positivity

For every fixed `q>0`, there is an effective `X(q)<infinity` such that

\[
 \boxed{
 \mathcal M(q,x)>0
 \qquad(|x|\ge X(q)).
 }
 \tag{MP.25}
\]

## 6. Compact search at every resolution

PR #379 proves that positive integer `q` and rational `x` form a complete RH criterion. Theorem 5.1 reduces each integer level to a compact interval:

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal M(n,r)\ge0
 \quad
 \begin{matrix}
 n\in\mathbb N_{>0},\\
 r\in\mathbb Q\cap[-X(n),X(n)].
 \end{matrix}
 }
 \tag{MP.26}
\]

The intervals are effective from the digamma bound and the absolutely convergent prime envelope. False RH would still be detected at a finite level and a finite rational centre.

This is not a finite proof of RH: the resolution index `n` remains unbounded.

## 7. Consequence for possible counterexamples

A fixed heat resolution cannot detect a hypothetical off-line zero at arbitrarily high ordinate, because `(MP.25)` makes the scalar positive there. Any terminal-pair witness with `|t_0|->infinity` must therefore use

\[
 q=q(t_0)\longrightarrow\infty.
 \tag{MP.27}
\]

The remaining problem is genuinely diagonal/microscopic:

```text
height x -> infinity
and
heat resolution q -> infinity together.
```

This explains in the new scalar language why fixed-band, fixed-window, and fixed-moment arguments cannot close RH.

## 8. Relation to the other live routes

- **Claude/Zeta23:** fixed normalized bandwidth yields an unconditional proportion; it does not resolve one pair. Theorem 5.1 gives the corresponding pointwise statement: fixed Gaussian resolution is eventually positive and cannot see a pair at unbounded height.
- **Terminal Gaussian residues:** PR #375 adapts the Gaussian to a target pair. PR #379 removes the depth parameter; the present theorem shows that the remaining centre/resolution diagonal is load bearing.
- **Fredholm/Pontryagin:** PR #373 makes every Gaussian-confined trace moment finite. The present result settles the broad-heat and fixed-resolution exterior portions of its first shifted moment, but not the all-order or diagonal sign.
- **Brownian raw route:** any transfer from finite Brownian approximants must preserve positivity precisely in the growing-resolution regime, not merely at each fixed `q`.

## 9. Verification and boundary

The finite replay checks the paired-log inequality, the annular lower bound, superexponential decay of the all-integer prime envelope, logarithmic fixed-`q` centre growth, and the `O(1/q)` pole estimate.

Proposed complete, pending review:

```text
uniform gamma lower bound after first-Hermite smoothing
unconditional positivity for all sufficiently small q
unconditional positivity outside a compact x interval at fixed q
compact countable RH search at each integer resolution
necessity of the joint x,q -> infinity frontier
```

Open:

```text
uniform positivity in the diagonal growing-resolution regime
first-Hermite prime inequality for all q,x
corrected-kernel floor
Riemann Hypothesis
```
