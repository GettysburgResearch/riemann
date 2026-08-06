# L-21701 — Screw–Stieltjes bridge and unconditional Hausdorff saddle positivity

Claim ID: `L-21701`  
Title: The square-screw signal and the central Hausdorff hierarchy are transforms of one spectral charge; every fixed Hausdorff row is eventually positive unconditionally  
Status: **PROPOSED PENDING INDEPENDENT REVIEW — exact bridge and fixed-row proof supplied; uniform parabolic extension remains a proposed target**  
Authoring agent: `gpt56-pro-global-01`  
Created: 2026-08-07  
Source dependencies: the central Stieltjes/Hausdorff criterion on PR #158; the square-screw criterion on PR #202; Nakamura–Suzuki's screw-function Laplace identity; the unconditional Riemann–von Mangoldt formula  
Scope: a repo-wide synthesis and an unconditional infinite sector of the all-order RH-equivalent moment hierarchy

## 1. One spectral charge behind the screw and moment programmes

Put

\[
 X(w)=\xi(1/2+w),
 \qquad
 \mathcal E(z)=\frac{X(\sqrt z)}{X(0)},
 \qquad
 G(z)=\frac{\mathcal E'(z)}{\mathcal E(z)}.
 \tag{L-21701.1}
\]

The functional equation makes `X` even, so `mathcal E` is entire.  Let
`g_zeta(t)` be the explicit Nakamura–Suzuki screw function used on PR #202 and
put

\[
 \Psi(t)=-g_\zeta(t).
\]

Their unilateral Laplace identity, evaluated at `w=sqrt(u)>0`, gives

\[
 \int_0^\infty g_\zeta(t)e^{-wt}\,dt
 =-\frac1{w^2}\frac{X'(w)}{X(w)}.
 \tag{L-21701.2}
\]

Therefore

\[
 \boxed{
 G(u)
 =\frac{\sqrt u}{2}
  \int_0^\infty e^{-\sqrt u\,t}\Psi(t)\,dt.}
 \tag{L-21701.3}
\]

The identity first holds in the common half-plane of absolute convergence and
then by analytic continuation wherever both sides are regular.

Under RH, Nakamura–Suzuki give the Lévy charge

\[
 \nu_\zeta
 =\sum_{\gamma>0}\frac{m_\gamma}{\gamma^2}\delta_\gamma
 \tag{L-21701.4}
\]

(up to the symmetric real convention), while the central moment route uses its
pushforward by `gamma -> gamma^(-2)`.  Thus

\[
 s_n=\sum_{\gamma>0}m_\gamma\gamma^{-2n-2}
 \tag{L-21701.5}
\]

are inverse even moments of the same Lévy charge whose Fourier exponent is the
square-screw signal.

Consequently

```text
square screw        = Fourier/Lévy coordinate,
central moments     = inverse-moment coordinate,
Jacobi–Padé model   = finite resolvent coordinate,
Pick/Loewner tests  = shifted resolvent coordinate.
```

This identity is not an RH proof.  It identifies exactly where a positive proof
must act: establish positivity of the common signed charge in one coordinate
without importing it from another RH-equivalent coordinate.

## 2. Central Hausdorff functionals without assuming RH

For a zero

\[
 \rho=\frac12+a+i\gamma,
 \qquad \gamma>0,
 \qquad |a|\le\frac12,
\]

put

\[
 x_\rho=-\frac1{(\rho-1/2)^2}
        =\frac1{(\gamma-ia)^2}.
 \tag{L-21701.6}
\]

Positive-ordinate zeros occur with the symmetry `a -> -a`, so the following sum
is real.  For integers `m>=1`, `k>=0`, define

\[
 \boxed{
 \mathcal H_{m,k}(R)
 =\sum_{\Im\rho>0}m_\rho
  x_\rho^m(R-x_\rho)^k.}
 \tag{L-21701.7}
\]

With `m=n+1`, this is the scalar Hausdorff row

\[
 \sum_{j=0}^k(-1)^j\binom kjR^{k-j}s_{n+j}
 \tag{L-21701.8}
\]

whose complete nonnegativity is equivalent to RH.  Under RH every summand is
nonnegative.  The entire hierarchy is RH-bearing, but individual asymptotic
sectors can be proved unconditionally.

Fix `R` strictly larger than the inverse square of the least positive zero
ordinate, so the real-line surrogate below is nonnegative.

## 3. Positive real-line surrogate and exact beta main term

Erase only the bounded horizontal displacement and define

\[
 M_{m,k}(R)
 =\sum_{\Im\rho>0}m_\rho
  \gamma^{-2m}(R-\gamma^{-2})^k.
 \tag{L-21701.9}
\]

This is nonnegative without RH.  Stieltjes summation against the full
positive-ordinate zero count has main density

\[
 I_{m,k}(R)
 =\frac1{2\pi}\int_0^\infty
 t^{-2m}(R-t^{-2})_+^k
 \log\frac{t}{2\pi}\,dt.
 \tag{L-21701.10}
\]

The substitution `y=(Rt^2)^(-1)` evaluates the integral exactly:

\[
 \boxed{
 I_{m,k}(R)
 =\frac{R^{k+m-1/2}}{8\pi}
 B\!\left(m-\frac12,k+1\right)
 \left[
  \psi\!\left(k+m+\frac12\right)
  -\psi\!\left(m-\frac12\right)
  -\log(4\pi^2R)
 \right].}
 \tag{L-21701.11}
\]

For fixed `m`, integration by parts against the ordinary
Riemann–von Mangoldt remainder gives lower order, so

\[
 M_{m,k}(R)=I_{m,k}(R)(1+o(1)).
 \tag{L-21701.12}
\]

In particular,

\[
 \boxed{
 M_{m,k}(R)
 \sim
 \frac{\Gamma(m-1/2)}{8\pi}
 R^{k+m-1/2}k^{-m+1/2}\log k.}
 \tag{L-21701.13}
\]

## 4. Off-line displacement is lower order for every fixed row

For one zero write

\[
 q=\frac a\gamma,
 \qquad
 A(q)=(1-iq)^{-2},
 \qquad
 y=\frac1{R\gamma^2}.
\]

The ratio between its actual summand and the positive surrogate is

\[
 \mathfrak R_{m,k}(y,q)
 =A(q)^m
  \left(\frac{1-yA(q)}{1-y}\right)^k.
 \tag{L-21701.14}
\]

Choose a fixed `0<epsilon<1/6` and split the zero ordinates into

\[
 \gamma<k^{1/2-\epsilon},
 \quad
 k^{1/2-\epsilon}\le\gamma\le k^{1/2+\epsilon},
 \quad
 \gamma>k^{1/2+\epsilon}.
\]

- In the low range, `(R-gamma^(-2))^k` contributes
  `exp(-c k^(2 epsilon))`, so the complete range is negligible against
  (L-21701.13).
- In the high range, zero counting and `gamma^(-2m)` give a relative
  `O(k^(-2 epsilon(m-1/2)))` tail.
- In the middle range,
  
  \[
  q=O(k^{-1/2+\epsilon}),
  \qquad
  ky=O(k^{2\epsilon}).
  \]
  
  Taylor's formula in (L-21701.14) gives, uniformly there,
  
  \[
  \mathfrak R_{m,k}(y,q)=1+o(1)
  \]
  
  for fixed `m`; the largest uncanceled term is
  `O(k^(-1/2+3 epsilon))`.

The `a -> -a` symmetry replaces each off-line pair by twice the real part and
preserves the estimate.  Hence

\[
 \boxed{
 \mathcal H_{m,k}(R)=M_{m,k}(R)(1+o(1))}
 \qquad(k\to\infty,\ m\text{ fixed}).
 \tag{L-21701.15}
\]

Combining (L-21701.13) and (L-21701.15) gives the unconditional fixed-row
asymptotic

\[
 \boxed{
 \mathcal H_{m,k}(R)
 \sim
 \frac{\Gamma(m-1/2)}{8\pi}
 R^{k+m-1/2}k^{-m+1/2}\log k.}
 \tag{L-21701.16}
\]

Therefore

\[
 \boxed{
 \mathcal H_{m,k}(R)>0
 \quad\text{for every fixed }m
 \text{ and all sufficiently large }k,}
 \tag{L-21701.17}
\]

without RH.

This closes an infinite boundary sector of the complete RH-equivalent hierarchy;
it is not finite numerical evidence.

## 5. Proposed uniform parabolic extension

The beta density in (L-21701.11) is concentrated at

\[
 y\asymp\frac m{k+m}
\]

with width `asymp sqrt(m)/k` when `k>>m`.  The first-order phase in
(L-21701.14) contains

\[
 m-\frac{ky}{1-y},
 \tag{L-21701.18}
\]

which vanishes at the saddle.  Averaging over the beta window leaves phase size

\[
 O(m/\sqrt k)
\]

and modulus error `O(m^2/k)`.  The same scale is the reciprocal width of the
zero-counting window in the ordinate variable.

This identifies the natural uniform theorem

\[
 \boxed{
 \frac m{\sqrt k}\longrightarrow0
 \quad\Longrightarrow\quad
 \mathcal H_{m,k}(R)=I_{m,k}(R)(1+o(1))>0,}
 \tag{L-21701.19}
\]

or the parabolic positive wedge

\[
 \boxed{k/m^2\longrightarrow\infty.}
 \tag{L-21701.20}
\]

The saddle cancellation improves the earlier cubic scheduling guess to a
quadratic one.  A complete uniform proof requires a Riemann–von Mangoldt
Stieltjes remainder with constants uniform in the beta window and is **not
promoted as proved here**.

## 6. Verified-height saddle sector

Let `H` be a height through which every zero has been certified simple and on
the critical line.  The line-surrogate saddle occurs at

\[
 t_*\asymp\sqrt{\frac{k}{Rm}}.
 \tag{L-21701.21}
\]

Whenever the beta mass is concentrated below `H`, the complete finite verified
block is positive and the unverified block has an off-line-safe absolute tail.
Directed finite data can therefore certify a second sector whose natural scale
is

\[
 k\lesssim RH^2m,
 \tag{L-21701.22}
\]

with the exact boundary determined by the full selected-zero sum and tail
majorant, not by the displayed heuristic scale.

Together, the proved fixed-row sector, proposed parabolic sector, and
verified-height sector isolate the genuine global difficulty:

```text
not the whole (m,k) quadrant,
but a moving transition strip where
  the saddle has left the verified line-zero block
  and m is not yet small compared with sqrt(k).
```

## 7. Full-problem resolution path

The all-order Hausdorff inequalities are equivalent to RH.  This claim proves
one infinite sector unconditionally and identifies a second uniform sector with
one explicit remaining estimate.  A serious closure programme is:

1. prove the uniform parabolic asymptotic (L-21701.19);
2. use the complete verified-zero manifest, not only one low atom, to certify
   every saddle below the verified height;
3. derive a local zero-count/phase estimate for the remaining transition strip;
4. feed the complete positivity result into the central Stieltjes theorem, or
   equivalently into the screw transform through (L-21701.3).

If these sectors cover every `(m,k)`, RH follows.  A single directed negative
row disproves RH.

The bridge and fixed-row asymptotic are submitted as new mathematics.  The
uniform parabolic and transition-strip closures remain **PROPOSED targets**, not
claims of a completed proof.