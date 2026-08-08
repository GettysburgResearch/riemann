# R-23707 — Centered little-`o` energy is too strong

Claim ID: `R-23707`  
Title: Critical-line zeros leave nonzero boundary Hardy mass, so the centered derivative energy should be `O(T)`, not `o(T)`  
Status: **SCOPE REFUTATION OF `L-23714.6`; CONDITIONAL IMPLICATION REMAINS TRUE BUT IS NOT A VIABLE HINGE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23714`; the classical existence of zeta zeros on the critical line  
Scope: normalization of the centered Hardy target

## 1. Centered multiplier

`L-23714` defines

\[
U(t)=Q'(t)-a_5
\]

with transform

\[
\widehat U(z)=\frac{h(z)-h(0)}{z}.
\tag{R-23707.1}
\]

At every nontrivial zeta zero

\[
\rho=\frac12+i\gamma
\]

on the critical line, the point

\[
z=i\gamma
\]

is a boundary pole of `h` and hence of `widehat U`. The Euler factor

\[
1-5^{-\rho}
\]

cannot vanish there, since a zero of `1-5^{-s}` has real part zero.

## 2. Boundary pole contribution

For a simple boundary pole with residue `r_gamma!=0`, the local Hardy integral satisfies

\[
\int_{|\tau-\gamma|<1}
\left|
\widehat U(\sigma+i\tau)
\right|^2d\tau
\sim\frac{\pi|r_\gamma|^2}{\sigma}
\qquad(\sigma\downarrow0).
\tag{R-23707.2}
\]

Thus

\[
\sigma\int|\widehat U(\sigma+i\tau)|^2d\tau
\]

has a nonzero boundary contribution and cannot tend to zero. A multiple zero makes the divergence stronger.

Since critical-line zeros are known to exist, the estimate

\[
\int_0^T|U(t)|^2dt=o(T)
\]

is not a viable global theorem.

## 3. Correct scale

The boundary-pole calculation is consistent with

\[
\boxed{
\int_0^T|U(t)|^2dt=O(T),
}
\]

or, more naturally for the weighted discrete boundary vector, an `O(T)` estimate after subtracting the complete positive linear mode.

Such a bound allows critical-line oscillations but excludes every interior pole: an off-line zero with shifted real part `delta>0` creates an exponentially growing physical mode and destroys every weighted Hardy norm on lines `0<sigma<delta`.

The corrected digital argument does not apply Cauchy--Schwarz directly to the primitive of `U`; it uses the base-five Abel recurrence. An `O(T)` centered boundary energy then creates only an `O(sqrt(T))` error against a positive main forcing of order `T`.

## 4. Scope

Refuted as a viable hinge:

```text
L-23714.6 / L-23714.11 centered little-o energy.
```

Not refuted:

```text
centered energy implies eventual positivity;
the `O(T)` centered digital-boundary theorem;
the cumulative shell sign;
Greedy Slack/DCRS;
RH.
```

The corrected theorem is `L-23716/T-23705`.
