# L-91031 — The completed safe-side Cauchy–Jordan factor has an explicit positive Stinespring measure

Claim ID: `L-91031`  
Status: **EXACT CONDITIONAL-ON-DENSITY STINESPRING THEOREM**  
Created: 2026-08-12  
Depends on: `L-9506`, `L-91020`, `L-91026`  
RH status: **unproved**

## 1. Completed centered ratio

Retain the completed one-Green factorization of `L-9506`:

\[
 \mathcal G_s(q)
 =R_s(q)B_s(q)
 \left[Z_s(q)-\frac{c_s}{q}\right],
 \qquad q>0,
 \tag{L-91031.1}
\]

where

\[
 R_s(q)=\frac{q+1}{(q+s)(q+s+1)},
\]

\[
 B_s(q)=\pi^{s/2}
 \frac{\Gamma((1+q)/2)}{\Gamma((1+s+q)/2)},
\]

and both `R_s` and `B_s` are Laplace transforms of explicit positive densities.

Set `s=2a`, and let

\[
 \alpha+\beta=\frac{163}{14},
 \qquad
 \alpha\beta=16.
\]

Define the stable Cauchy spectral factor

\[
 \boxed{
 \Psi_a(q)
 =\sqrt{378}\,a^3
 \frac{q(q+\sqrt\alpha a)(q+\sqrt\beta a)}
 {(q+a)^2(q+2a)^2(q+4a)^2}.
 }
 \tag{L-91031.2}

## 2. Completed source transfer

Define

\[
 \boxed{
 \mathcal S_a(q)
 =\frac{\Psi_a(q)}{\sqrt{378}\,a^3q^3}
 \mathcal G_{2a}(q).
 }
 \tag{L-91031.3}

A direct rearrangement gives

\[
 \boxed{
 \begin{aligned}
 \mathcal S_a(q)
 ={}&R_{2a}(q)B_{2a}(q)
 \frac1{(q+a)^2(q+2a)^2(q+4a)^2}\\
 &\cdot
 \left[
 q(q+\sqrt\alpha a)(q+\sqrt\beta a)
 \frac{Z_{2a}(q)-c_{2a}/q}{q^3}
 \right].
 \end{aligned}
 }
 \tag{L-91031.4}

The bracket is exactly the Green-removed arithmetic channel of `L-91026`.

## 3. Positive representing measure

Assume

\[
 \mathcal B_{2a,a}(t)\ge0
 \qquad(t\ge0).
 \tag{L-91031.5}

Then `L-91026` expresses the bracket in (L-91031.4) as the Laplace transform of the positive measure

\[
 \boxed{
 d\omega_a
 =\delta_0
 +\sum_{n\ge2}\frac{F_{2a}(n)}n\delta_{\log n}
 +\mathcal B_{2a,a}(t)\,dt.
 }
 \tag{L-91031.6}

Let `r_(2a)(t)` and `b_(2a)(t)` be the positive rational and beta/Gamma densities of `L-9506`. Let `g_a` be the positive Erlang convolution with Laplace transform

\[
 \widehat g_a(q)
 =\frac1{(q+a)^2(q+2a)^2(q+4a)^2}.
 \tag{L-91031.7}

Explicitly,

\[
 g_a
 =\bigl(te^{-at}\bigr)
  *\bigl(te^{-2at}\bigr)
  *\bigl(te^{-4at}\bigr).
\]

Then

\[
 \boxed{
 \mathcal S_a(q)
 =\int_0^\infty e^{-qt}\,d\mu_a(t),
 \qquad
 \mu_a=r_{2a}*b_{2a}*g_a*\omega_a\ge0.
 }
 \tag{L-91031.8}

Hence `S_a` is completely monotone.

For complex `z,w` with positive real parts,

\[
 \boxed{
 \mathcal S_a(z+\overline w)
 =\left\langle e^{-\overline w(\cdot)},
                    e^{-z(\cdot)}\right\rangle_{L^2(\mu_a)},
 }
 \tag{L-91031.9}

so every finite safe-side matrix is positive semidefinite, with one explicit Stinespring space.

## 4. Unconditional scale ranges

The density hypothesis (L-91031.5) is already unconditional in the following regimes:

1. every `a>=1/3`, by `L-91030`;
2. every sufficiently small `a>0`, by `L-91028`.

Therefore the completed safe-side source transfer (L-91031.8) is unconditional in both ranges.

## 5. What this closes

The gamma and rational pole factors do not create an additional sign problem after the arithmetic numerator has been removed. They are positive convolution channels. Likewise the six stable Cauchy denominator states are ordinary positive Erlang channels.

Thus the completed safe-side Stinespring construction is explicit:

```text
Green-removed arithmetic contact/atoms/density
  * rational completed density
  * beta/Gamma completed density
  * six Erlang Cauchy states.
```

No existential square root or unspecified same-scale port remains on the safe side.

## 6. What remains

The theorem does **not** identify the non-tangential critical-boundary limit of this safe Stinespring feature with the Weil/Clark Cauchy-square Gram. That identification is precisely where an off-line xi zero can create a hyperbolic expanding mode.

The final CJHI obligation is now:

\[
 \boxed{
 \text{prove that the explicit measures }\mu_a
 \text{ admit the required completed boundary limit,}
 }
\]

with coefficient-one state return and without a hidden hyperbolic boundary port.

This boundary theorem remains RH-equivalent. Positivity of (L-91031.9) at safe points alone does not prove RH, as emphasized by the control examples on PR #398.