# The logarithmic second term in the native cusp spectrum

Status: PROPOSED ANALYTIC THEOREM; independent review required.
Scope: the native level-one finite-part operator of Theorem K, uniformly at
every growing index `J=o(k)`. No period-zero or RH conclusion is asserted.

## 1. Statement

Retain all notation and normalizations from
[`CUSP_KRONECKER_SPECTRAL_LAW.md`](CUSP_KRONECKER_SPECTRAL_LAW.md). Thus
`nu=k-1`, the eigenvalues of the Petersson compression of the finite part
of the completed Eisenstein series are `lambda_J(k)`, and

\[
 c_0={\gamma-\log(4\pi)\over2}.
\]

Put

\[
 m_{k,J}={\nu\over24J}-{1\over2}\log {\nu\over4\pi J}+c_0. \tag{L1}
\]

Also put

\[
 R_1={2e^{-2\pi}\over(1-e^{-2\pi})^2}. \tag{L2}
\]

**Theorem L.** For every sequence of even weights tending to infinity and
integers `1 <= J_k=o(k)`, one has

\[
 m_{k,J_k}+o(1)\le \lambda_{J_k}(k)
 \le m_{k,J_k}+R_1+o(1). \tag{L3}
\]

In particular

\[
 \boxed{\lambda_{J_k}(k)
 ={k-1\over24J_k}-{1\over2}\log {k-1\over4\pi J_k}+c_0+O(1)}. \tag{L4}
\]

The `O(1)` is absolute and uniform over all such sequences. The sharper
one-sided constants in (L3) are retained because they identify the only
remaining loss: the uniform treatment of the nonconstant Fourier term on
the coefficient-flag upper subspace. This note does not silently replace
that loss by zero.

## 2. A conditional-Gamma upper symbol

On the full width-one cusp, Parseval turns the radial part of the symbol
into diagonal Gamma averages. For `a=4*pi*n`, let `Y_{nu,a}` have density
proportional to

\[
 y^{\nu-1}e^{-ay}{\bf1}_{y\ge1},
\]

and define

\[
 \mu_{\nu,a}=\mathbb E\left[{\pi Y_{\nu,a}\over6}
              -{1\over2}\log Y_{\nu,a}+c_0\right]. \tag{L5}
\]

The function inside the expectation is increasing on `y>=1`. The family
of conditional densities has monotone likelihood ratio in the rate `a`.
Consequently stochastic ordering gives

\[
 \mu_{\nu,4\pi n}\le\mu_{\nu,4\pi J}\qquad(n\ge J). \tag{L6}
\]

This is a complete diagonal estimate over all Fourier indices, not a
truncation at a fitted number of coefficients.

For `J=o(k)`, conditioning at one changes the corresponding unconditioned
Gamma moments by `o(1)`, uniformly along the sequence. Here is an explicit
check. If `Z` is Gamma of shape `nu` and rate `a=4*pi*J`, then

\[
 \Pr(Z<1)\le {a^\nu\over\Gamma(\nu+1)},\qquad
 \mathbb E[|\log Z|;Z<1]
 \le {a^\nu\over\Gamma(\nu)\nu^2}. \tag{L7}
\]

Both right sides are superpolynomially small because
`a/nu -> 0` and `Gamma(nu+1)>=(nu/e)^nu`. Integration by parts gives the
same conclusion for the first moment. The unconditioned identities

\[
 \mathbb EZ={\nu\over a},\qquad
 \mathbb E\log Z=\psi(\nu)-\log a \tag{L8}
\]

therefore imply

\[
 \mu_{\nu,4\pi J}
 = {\nu\over24J}-{1\over2}\psi(\nu)
   +{1\over2}\log(4\pi J)+c_0+o(1)
 =m_{k,J}+o(1), \tag{L9}
\]

where `psi(nu)=log(nu)+O(1/nu)`.

## 3. Min--max upper bound

Use the complete coefficient flag

\[
 W_J=\{f:a_f(1)=\cdots=a_f(J-1)=0\}.
\]

Its codimension is at most `J-1`. On `y>=1`, (L6) bounds the expectation
of the radial part of `E_0` by `mu_(nu,4*pi*J)`. The nonconstant term obeys

\[
 |r_0(z)|\le {2e^{-2\pi y}\over(1-e^{-2\pi y})^2}\le R_1. \tag{L10}
\]

The part of the fundamental domain below height one is compact, so `E_0`
has a fixed finite supremum there. Since `m_(k,J)->infinity` for `J=o(k)`,
that compact supremum is eventually below the right side of (L9) plus
`R_1`. Normalizing the Petersson mass and combining its compact and cusp
pieces therefore gives, for every nonzero `f in W_J`,

\[
 {G_k(f,T_kf)\over G_k(f,f)}
 \le m_{k,J}+R_1+o(1). \tag{L11}
\]

Min--max proves the upper half of (L3). Notice that (L10), rather than the
larger fundamental-domain bound `R_0`, is available because the Fourier
expansion is being estimated only on the full cusp `y>=1`.

## 4. Lower bound with the Fourier remainder removed asymptotically

Let `S_J=span(P_1,...,P_J)` be the native Poincare subspace used in
Theorem K. Its Gram defect `delta_(k,J)` tends to zero faster than every
power along `J=o(k)`. The same is true after multiplication by `nu/J`.
Moreover

\[
 1-Q(k,4\pi J)\le e^{4\pi J}2^{-k}, \tag{L12}
\]

again faster than every power. Hence the height lower bound of (K11)
satisfies

\[
 L_{k,J}={\nu\over4\pi J}+o(1). \tag{L13}
\]

Jensen's inequality in the full normalized Petersson measure gives

\[
 \mathbb E\left[{\pi y\over6}-{1\over2}\log y+c_0\right]
 \ge {\pi L_{k,J}\over6}-{1\over2}\log L_{k,J}+c_0
 =m_{k,J}+o(1). \tag{L14}
\]

It remains to avoid paying the fixed global bound for `r_0`. Set

\[
 H_{k,J}=\sqrt{\nu/(4\pi J)}.
\]

Keeping the same first `J` Parseval terms as in Theorem K, but now only
above this height, shows uniformly for every unit vector in `S_J` that its
mass there is at least

\[
 \alpha_{k,J}=(1-\delta_{k,J})
 Q(k-1,4\pi JH_{k,J}). \tag{L15}
\]

The Gamma threshold divided by its shape is
`sqrt(4*pi*J/nu)->0`; a negative-exponential Chernoff bound therefore gives
`1-alpha_(k,J)=o(1)`. On the retained high part, (L10) is
`O(exp(-2*pi*H_(k,J)))=o(1)`, while on its complement the original global
bound `R_0` is multiplied by `1-alpha_(k,J)`. Thus

\[
 |\mathbb E_f r_0|=o(1) \tag{L16}
\]

uniformly on the unit sphere of `S_J`. Equations (L14)--(L16) and min--max
prove the lower half of (L3).

## 5. Boundaries and next target

The theorem refines the leading `k/(24J)` law by an unbounded logarithmic
term and a uniformly bounded remainder. It does not prove convergence of
that remainder or identify a scalar correction. The remaining interval of
width `R_1` is not numerical uncertainty; it is an analytic upper-bound
loss for the nonconstant Fourier coupling.

A genuinely stronger next theorem would control that coupling in the
Poincare/flag spectral comparison and prove an `o(1)` remainder. A separate
moving-coordinate theorem would then be needed to turn individual spectral
asymptotics into growing simple period roots. Neither assertion follows
from (L3), from the fixed-compact reciprocal-Gamma determinant limit, or
from the finite directed inequality panel.
