# L-21914 — Continuum log-concavity of the Xi interpolant

Claim ID: `L-21914`  
Title: The Csordas–Varga kernel theorem proves strict log-concavity of the canonical Xi Mellin–gamma interpolant on its complete positive half-line  
Status: **PROPOSED EXACT TRANSLATION OF PUBLISHED THEOREMS PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Primary source: Csordas–Varga, *Moment inequalities and the Riemann hypothesis*, Constructive Approximation 4 (1988), Theorem 2.1 and Proposition 2.3  
Dependencies: `L-21910`, `L-21912`  
Scope: the complete `n=k=0` generalized-Stieltjes inequality; no higher-order Stieltjes claim

## 1. Published input

Csordas and Varga prove for the classical Riemann kernel that

\[
 \boxed{
 t\longmapsto\log\Phi(\sqrt t)
 \text{ is strictly concave on }(0,\infty).}
 \tag{L-21914.1}
\]

Their Proposition 2.3 gives the following normalized-Mellin consequence. If
`Psi` is positive and `log Psi(sqrt t)` is strictly concave, then

\[
 \boxed{
 x\longmapsto
 \log\left[
  \frac1{\Gamma(x+1)}
  \int_0^\infty t^x\Psi(\sqrt t)\,dt
 
 \right]
 \text{ is strictly concave for }x>-1.}
 \tag{L-21914.2}

The statement is continuous in the moment order `x`; it is stronger than the
integer Turán inequality extracted in `L-21911`.

## 2. Exact identification with the canonical interpolant

Set

\[
 x=z-\frac12.
 \tag{L-21914.3}
\]

The substitution `t=u^2` gives

\[
 \int_0^\infty u^{2z}\Phi(u)\,du
 =\frac12\int_0^\infty t^{z-1/2}\Phi(\sqrt t)\,dt.
 \tag{L-21914.4}
\]

From `L-21910`,

\[
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}{\Gamma(z+1/2)}
 \frac{2}{\xi(1/2)}
 \int_0^\infty u^{2z}\Phi(u)\,du.
 \tag{L-21914.5}
\]

Therefore

\[
 \boxed{
 C_\Xi(z)
 =\frac{\sqrt\pi}{\xi(1/2)}\,4^{-z}
 \left[
  \frac1{\Gamma(x+1)}
  \int_0^\infty t^x\Phi(\sqrt t)\,dt
 \right],
 \qquad x=z-\frac12.}
 \tag{L-21914.6}

The prefactor is a positive constant times an exponential linear in `z`, so it
does not affect the second derivative of the logarithm.

Applying (L-21914.1)--(L-21914.2) yields

\[
 \boxed{
 \frac{d^2}{dz^2}\log C_\Xi(z)<0
 \qquad(z>-1/2).}
 \tag{L-21914.7}
\]

Equivalently,

\[
 \boxed{
 \mathcal S_\Xi(z)
 =-\frac{d^2}{dz^2}\log C_\Xi(z)>0
 \qquad(z>-1/2).}
 \tag{L-21914.8}

This is an unconditional continuum theorem for the actual Riemann kernel.

## 3. Exact variance inequality

Using the tilted logarithmic law of `L-21912`, equation (L-21914.8) is exactly

\[
 \boxed{
 4\operatorname{Var}_z(\log u)
 <\psi_1\!\left(z+\frac12\right)
 \qquad(z>-1/2).}
 \tag{L-21914.9}

Thus the log-coordinate variance of every Mellin tilt of the Riemann kernel is
strictly smaller than the corresponding half-log-gamma variance.

In the generalized-Stieltjes notation of `L-21912`, this proves

\[
 \boxed{
 F_{0,0}^{[2]}(x)>0
 \qquad(x>0)}
 \tag{L-21914.10}

for the translated function

\[
 f(x)=\mathcal S_\Xi(x-1/2).
\]

It does not prove the inequalities with `n+k>0`.

## 4. Continuous shift-quotient consequence

For real `z>1/2`, the canonical quotient is positive and

\[
 \log\phi_\Xi(z)
 =\log C_\Xi(z-1)-\log C_\Xi(z).
 \tag{L-21914.11}
\]

Differentiating and using strict decrease of `(log C_Xi)'`,

\[
 \boxed{
 \frac{d}{dz}\log\phi_\Xi(z)>0,
 \qquad z>1/2.}
 \tag{L-21914.12}

Hence

\[
 \boxed{
 \phi_\Xi'(z)>0
 \qquad z>1/2.}
 \tag{L-21914.13}

This is the complete real-half-line first Bernstein sign, strengthening the
integer monotonicity in `L-21911`.

## 5. Strict two-point inequalities

For any

\[
 -\frac12<a<b,
 \qquad 0<\theta<1,
\]

strict log-concavity gives

\[
 \boxed{
 C_\Xi(\theta a+(1-\theta)b)
 >C_\Xi(a)^\theta C_\Xi(b)^{1-\theta}.}
 \tag{L-21914.14}

In particular, for every `h>0` and `z-h>-1/2`,

\[
 \boxed{
 C_\Xi(z)^2>C_\Xi(z-h)C_\Xi(z+h).}
 \tag{L-21914.15}

The classical Turán inequalities are the integer, unit-step specialization.

## 6. What remains

Real-rootedness of `C_Xi` would give the stronger representation

\[
 \mathcal S_\Xi(z)
 =a+\sum_j\frac{m_j}{(z+\alpha_j)^2},
 \qquad a\ge0,\ \alpha_j\ge1/2,
 \tag{L-21914.16}
\]

and hence every Sokal inequality of `L-21912`. The present theorem proves only
positivity of the function itself on the positive ray.

Neither of the following follows from (L-21914.8):

```text
complete monotonicity of S_Xi;
generalized-Stieltjes membership of S_Xi;
real-rootedness of C_Xi;
Pick positivity of the shift quotient.
```

The gap from `TP_2`/log-concavity to the all-order total-positivity statement is
genuine.

## 7. Review boundary

Closed, subject to normalization review of the published kernel:

- exact change of variables from the Csordas–Varga normalized moment;
- strict log-concavity of `C_Xi` on `(-1/2,infinity)`;
- the continuum variance inequality;
- continuous monotonicity of the shift quotient;
- every two-point Turán inequality on the positive half-line.

Open:

- the higher Sokal inequalities;
- the positive measure in `L-21912`;
- real-rootedness of `C_Xi`;
- RH.