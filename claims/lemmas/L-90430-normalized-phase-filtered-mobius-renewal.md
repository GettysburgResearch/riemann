# L-90430 — Normalization-corrected phase-filtered Möbius renewal

Claim ID: `L-90430`  
Title: The phase-locked bottom charge is one centered coercive filter of the canonical Möbius Green state, with the exact spectral interval and finite affine renewal forcing  
Status: **PROPOSED COMPLETE EXACT CORRECTED THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Supersedes: the spectral-edge/forcing comparison in `L-90429`; the state and renewal identities there survive after the factor-two correction below  
Dependencies: corrected `L-90427/T-90421`; `L-90423`; finite divisor switching  
Scope: exact state compression and renewal; no sign, growth estimate, or RH conclusion

## 1. Canonical state and exact scale filter

Define

\[
\Phi(X)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}\log\frac Xn.
\tag{L-90430.1}
\]

Then

\[
\int_1^\infty\Phi(X)X^{-z-1}\,dX
 =\frac1{z^2\zeta(z+1/2)}.
\tag{L-90430.2}
\]

The phase-locked carry charge satisfies

\[
\boxed{
\mathcal C_*(X)=F_*(X)-\log X,
}
\tag{L-90430.3}
\]

where

\[
\boxed{
\begin{aligned}
F_*(X)
={}&\Phi(X)-\frac{15}{2\sqrt2}\Phi(X/2)
 +\frac{35}{4}\Phi(X/4)\\
&-\frac{15}{2\sqrt2}\Phi(X/8)+\Phi(X/16).
\end{aligned}}
\tag{L-90430.4}
\]

The scale polynomial is

\[
P_*(y)
 =1-\frac{15}{2\sqrt2}y
  +\frac{35}{4}y^2
  -\frac{15}{2\sqrt2}y^3+y^4
 =\frac12Q_*(y/\sqrt2).
\tag{L-90430.5}
\]

## 2. Correct centered spectral interval

On `|y|=1`, the centered symbol `y^-2 P_*(y)` is real and positive. From `L-90423`,

\[
\boxed{
\kappa_-
 \le y^{-2}P_*(y)
 \le\kappa_+,
}
\tag{L-90430.6}
\]

with

\[
\boxed{
\kappa_-=\frac{43-30\sqrt2}{4}>0,
\qquad
\kappa_+=\frac{43+30\sqrt2}{4}.
}
\tag{L-90430.7}
\]

Thus the **centered** dyadic operator is coercive. The uncentered polynomial carries the unitary phase `y^2`; it is not itself a positive scalar multiplier.

The earlier interval in `L-90429.8` was too large by a factor of two. Equations (L-90430.6)--(L-90430.7) are normative.

## 3. Exact divisor renewals

The canonical state obeys

\[
\boxed{
\sum_{d\le X}d^{-1/2}\Phi(X/d)=\log X.
}
\tag{L-90430.8}
\]

Since `F_*` is the full Riesz transform of the phase-locked source, convolution with the ordinary divisor source gives, for `X>=16`,

\[
\boxed{
\sum_{d\le X}d^{-1/2}F_*(X/d)
 =\kappa_-\log(X/4).
}
\tag{L-90430.9}
\]

Indeed, if `p_r` are the coefficients of `Q_*/2`, then

\[
\sum_{r=0}^4p_r2^{-r/2}=\kappa_-,
\qquad
\sum_{r=0}^4r p_r2^{-r/2}=2\kappa_-.
\tag{L-90430.10}
\]

Hence the exact causal form is

\[
\boxed{
F_*(X)
 =\kappa_-\log(X/4)
  -\sum_{2\le d\le X}d^{-1/2}F_*(X/d).
}
\tag{L-90430.11}
\]

The lower centered spectral edge and the coefficient of `log X` in the renewal forcing are now exactly the same constant `kappa_-`.

## 4. Interpretation

The finite fourteen-row packet is one scalar state with:

```text
canonical half-power Möbius Green input;
coercive centered five-scale filter;
strict positive spectral edge kappa_-;
positive divisor delays;
finite affine forcing kappa_- log(X/4).
```

The positive delay mass is not contractive and retains the reciprocal-zeta spectrum. Therefore no sign or critical-growth conclusion is inferred from (L-90430.11).

## 5. Proof boundary

Closed exactly here:

1. one-state reduction;
2. correct centered phase factor;
3. correct spectral interval;
4. positive Möbius renewal;
5. finite affine filtered renewal;
6. exact equality of the lower spectral edge and renewal forcing coefficient.

Open:

1. a Lyapunov or variation theorem for the noncontractive renewal;
2. PBVG or critical growth;
3. RH.
