# L-90429 — The phase-locked charge is a coercive filter of one Möbius Green state

Claim ID: `L-90429`  
Title: The fourteen-row charge is one critically phase-locked dyadic filter of the canonical half-power Möbius Riesz state, and its full version satisfies an exact positive divisor-renewal equation with affine forcing  
Status: **PROPOSED COMPLETE EXACT GREEN/RENEWAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: corrected `L-90427/T-90421`; `L-90425`; finite divisor switching  
Scope: exact state compression and renewal; no sign, growth estimate, or RH conclusion

## 1. Canonical half-power Möbius state

Define the full Möbius Riesz state

\[
\boxed{
\Phi(X)
 =\sum_{1\le n\le X}\frac{\mu(n)}{\sqrt n}
   \log\frac Xn.
}
\tag{L-90429.1}
\]

For `Re z>1/2`,

\[
\boxed{
\int_1^\infty\Phi(X)X^{-z-1}\,dX
 =\frac1{z^2\zeta(z+1/2)}.
}
\tag{L-90429.2}
\]

The multiples-Möbius state of `T-90421`, with the target column `w_X(1)=0`, is

\[
u_1(X)=\Phi(X)-\log X,
\tag{L-90429.3}
\]

and, for every `m>=2`,

\[
\boxed{
u_m(X)=m^{-1/2}\Phi(X/m).}
\tag{L-90429.4}
\]

Thus all five adjoint coordinates in `T-90421.17` are samples of one scalar state.

## 2. Exact phase-locked scale filter

Put

\[
\boxed{
\begin{aligned}
(\mathcal P_*\Phi)(X)
={}&\Phi(X)-\frac{15}{2\sqrt2}\Phi(X/2)
 +\frac{35}{4}\Phi(X/4)\\
&-\frac{15}{2\sqrt2}\Phi(X/8)
 +\Phi(X/16).
\end{aligned}}
\tag{L-90429.5}
\]

Substituting (L-90429.3)--(L-90429.4) in the corrected five-state formula gives

\[
\boxed{
\mathcal C_*(X)
 =(\mathcal P_*\Phi)(X)-\log X.
}
\tag{L-90429.6}
\]

The scale polynomial of `mathcal P_*` is

\[
\boxed{
P_*(y)
 =1-\frac{15}{2\sqrt2}y
  +\frac{35}{4}y^2
  -\frac{15}{2\sqrt2}y^3+y^4
 =\frac12Q_*(y/\sqrt2).
}
\tag{L-90429.7}
\]

On the unit circle it is, after centering, the positive Fejer square of `L-90425`. Hence the dyadic operator `mathcal P_*` is boundedly invertible on critical `ell^2` scale packets, with spectral interval

\[
\boxed{
\left[\frac{43}{2}-15\sqrt2,
      \frac{43}{2}+15\sqrt2\right].
}
\tag{L-90429.8}
\]

There is no hidden family of low-row states: the finite packet is one well-conditioned filter of `Phi`.

## 3. Exact positive divisor renewal for `Phi`

Since `mathbf1*mu=epsilon`, multiplicative convolution and the scaling law for full Riesz transforms give

\[
\boxed{
\sum_{d\le X}\frac1{\sqrt d}\Phi(X/d)=\log X.
}
\tag{L-90429.9}
\]

Equivalently,

\[
\Phi(X)
 =\log X-\sum_{2\le d\le X}d^{-1/2}\Phi(X/d).
\tag{L-90429.10}
\]

Every delayed argument is at most `X/2`; the delay weights are positive. Their total mass is not contractive, so no sign is inferred.

## 4. Phase-locked renewal with finite affine forcing

Let

\[
F_*(X)=(\mathcal P_*\Phi)(X)
 =\mathcal R_{b_*}^{\rm full}(X).
\tag{L-90429.11}
\]

Because `mathbf1*b_*` is the five-atom source of `L-90427.3`, its full Riesz transform is elementary. For every `X>=16`,

\[
\boxed{
\sum_{d\le X}\frac1{\sqrt d}F_*(X/d)
 =\delta_*\left(\frac12\log X-\log2\right),
}
\tag{L-90429.12}
\]

where

\[
\boxed{
\delta_*=\frac{43}{2}-15\sqrt2>0.
}
\tag{L-90429.13}
\]

Indeed the right side is

\[
\sum_{r=0}^4 p_r2^{-r/2}\log(X/2^r),
\]

and the two exact moment sums are

\[
\sum_{r=0}^4p_r2^{-r/2}=\delta_*/2,
\qquad
\sum_{r=0}^4r p_r2^{-r/2}=\delta_*.
\tag{L-90429.14}
\]

Thus

\[
\boxed{
F_*(X)
 =\delta_*\left(\frac12\log X-\log2\right)
  -\sum_{2\le d\le X}d^{-1/2}F_*(X/d).
}
\tag{L-90429.15}
\]

The phase-lock spectral gap and the renewal forcing constant are the same algebraic number `delta_*`.

## 5. Interpretation

The entire route has now collapsed to one scalar causal system:

```text
canonical state Phi;
positive divisor renewal;
strictly coercive five-scale phase filter;
finite affine filtered forcing;
column-one output C_*=F_*-log X.
```

A proof of the critical growth or eventual sign of `C_*` would prove RH by `T-90421`. Equations (L-90429.9) and (L-90429.15) do not themselves give such a proof: the positive delay mass is supercritical and retains the reciprocal-zeta spectrum.

## 6. Proof boundary

Closed exactly here:

1. five states reduce to one `Phi`;
2. exact phase-locked filter;
3. critical scale coercivity;
4. positive renewal for `Phi`;
5. finite affine renewal for `F_*`;
6. equality of the renewal forcing and spectral-gap constants.

Open:

1. a Lyapunov, variation, or source theorem controlling the supercritical renewal;
2. critical growth or eventual sign of `C_*`;
3. RH.
