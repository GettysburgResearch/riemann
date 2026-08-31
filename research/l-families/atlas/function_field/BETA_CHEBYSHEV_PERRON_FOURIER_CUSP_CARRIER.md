# T-108004 — The cubic edge has an exact Perron–Fourier source carrier

Status: **exact finite frequency-splitting identity, right-half-plane
complex extension of the T-108002 cubic cusp, exact two-parameter edge
profile on the natural Fourier window, and exact cubic-phase dual carrier on
the natural log-ratio window; no estimate for the reciprocal-zeta/beta
source correlation, no new zero-free region, and no proof of RH.**

Bounded replay:
[`beta_chebyshev_perron_fourier_cusp_carrier.py`](beta_chebyshev_perron_fourier_cusp_carrier.py).
Canonical output:
[`beta_chebyshev_perron_fourier_cusp_carrier.json`](beta_chebyshev_perron_fourier_cusp_carrier.json).

This packet continues
[T-108002](BETA_CHEBYSHEV_CUBIC_CUSP_EDGE_PROFILE.md).  T-108002 determined
the finite first-edge profile only at Fourier frequency zero.  The assembled
Perron formula does not use that isolated value: it integrates the tilted
Fourier kernel against

\[
 B_\beta(s-it)B_\beta(s+it),
 \qquad
 B_\beta(w)=\frac{1-67^{-w}}{\zeta(w)}.
\]

The purpose here is to determine the complete local kernel seen by that
signed source before any absolute value is taken.

## 0. Outcome

Let \(n=r+1\), let \(R_r\) be the unit-height Chebyshev-step
autocorrelation, and retain

\[
 \kappa_r=
 \frac{1-\cos(\pi/n)}{12(1+2\cos(\pi/n))}.
\]

For \(c\ne0\) and real Fourier frequency \(t\), define

\[
 \Psi_n(c,t)
 =\frac{1}{nc\kappa_r}
 \int_{\mathbb R}R_r(x)e^{-nc|x|/2}e^{-itx}\,dx.
 \tag{0.1}
\]

The zero-frequency profile of T-108002 is

\[
 \Phi_n(c)=\Psi_n(c,0).
\]

### Exact finite frequency split

Evenness of \(R_r\) gives, without approximation, whenever the two shifted
arguments are nonzero,

\[
 \boxed{
 \Psi_n(c,t)
 =\frac12\left[
 \frac{c+2it/n}{c}\Phi_n\!\left(c+\frac{2it}{n}\right)
 +
 \frac{c-2it/n}{c}\Phi_n\!\left(c-\frac{2it}{n}\right)
 \right].}
 \tag{0.2}
\]

At the isolated values where one shifted argument vanishes, the corresponding
product is understood by its removable analytic continuation.  The first-edge
window below never meets those exceptional values.

Thus the full local Fourier kernel is obtained from two translated copies of
the scalar edge profile.  The identity is also replayed independently by
exact integration over every ordered pair of Chebyshev cells.

Put

\[
 c_n(\lambda)=4i+\lambda n^{-2/3},
 \qquad \lambda>0,
 \tag{0.3}
\]

and use the forced local frequency scale

\[
 t=\tau n^{1/3}.
 \tag{0.4}
\]

### Theorem T-108004

Locally uniformly for \((\lambda,\tau)\) in compact subsets of
\((0,\infty)\times\mathbb R\),

\[
 \boxed{
 n^{-1/3}\Psi_n\!\left(c_n(\lambda),\tau n^{1/3}\right)
 \longrightarrow \mathcal C(\lambda,\tau),}
 \tag{0.5}
\]

where

\[
 \boxed{
 \mathcal C(\lambda,\tau)
 =\frac12\bigl(
 \mathcal A(\lambda+2i\tau)
 +\mathcal A(\lambda-2i\tau)
 \bigr).}
 \tag{0.6}
\]

Here \(\mathcal A\) is the analytic continuation, for \(\Re\zeta>0\), of
the T-108002 cubic profile:

\[
 \mathcal A(\zeta)
 =\frac{36\sqrt2}{\pi^3}e^{-i\pi/4}
 \int_0^\infty u^{-1/2}
 \exp\!\left(-\frac{\pi\zeta}{4}u
 +i\frac{\pi^3}{24}u^3\right)du.
 \tag{0.7}
\]

Equivalently,

\[
 \boxed{
 \mathcal C(\lambda,\tau)
 =\frac{36\sqrt2}{\pi^3}e^{-i\pi/4}
 \int_0^\infty u^{-1/2}
 e^{-\pi\lambda u/4+i\pi^3u^3/24}
 \cos\!\left(\frac{\pi\tau u}{2}\right)du.}
 \tag{0.8}
\]

In particular \(\mathcal C(\lambda,\tau)\) is even in \(\tau\), and
\(\mathcal C(\lambda,0)=\mathcal A(\lambda)\).

### Exact dual log-ratio carrier

Use the Fourier convention

\[
 \widehat f(v)=\int_{\mathbb R}f(\tau)e^{-i\tau v}\,d\tau.
\]

For \(\lambda>0\), define

\[
 \boxed{
 H_\lambda(v)=
 \frac{72}{\pi^{5/2}}e^{-i\pi/4}
 |v|^{-1/2}
 \exp\!\left(-\frac\lambda2|v|+i\frac{|v|^3}{3}\right),
 \qquad v\ne0.}
 \tag{0.9}
\]

The singularity at zero is locally integrable and the exponential factor
makes \(H_\lambda\in L^1(\mathbb R)\).  Direct substitution in (0.8)
proves the ordinary inverse-Fourier identity

\[
 \boxed{
 \mathcal C(\lambda,\tau)
 =\frac1{2\pi}\int_{\mathbb R}
 H_\lambda(v)e^{i\tau v}\,dv.}
 \tag{0.10}
\]

Consequently the tempered Fourier transform of the local cusp is exactly
\(H_\lambda\).  The source-facing edge is therefore not an anonymous Airy
or stationary-phase envelope.  It is the explicit lag carrier

\[
 \boxed{
 |v|^{-1/2}e^{-\lambda|v|/2}e^{i|v|^3/3}}
 \tag{0.11}
\]

with fixed phase \(e^{-i\pi/4}\) and fixed normalization.

## 1. Proof of the exact split

Write

\[
 J_r(z)=\int_{\mathbb R}R_r(x)e^{-z|x|/2}\,dx.
\]

Because \(R_r\) is even,

\[
 \begin{aligned}
 \int_{\mathbb R}R_r(x)e^{-z|x|/2}e^{-itx}\,dx
 &=\int_0^\infty R_r(x)
 \left(e^{-(z/2+it)x}+e^{-(z/2-it)x}\right)dx\\
 &=\frac12\bigl(J_r(z+2it)+J_r(z-2it)\bigr).
 \end{aligned}
 \tag{1.1}
\]

The finite profile normalization is

\[
 \Phi_n(c)=\frac{J_r(nc)}{nc\kappa_r}.
 \tag{1.2}
\]

Substituting \(z=nc\) in (1.1) and using (1.2) proves (0.2).
No asymptotic, positivity argument, or interchange with the beta source is
used.

The replay checks (1.1) against a second formula.  On two disjoint cells
\([a,b]\) and \([c,d]\), \(b\le c\), the ordered integral factors as

\[
 \left(\int_a^b e^{\alpha x}dx\right)
 \left(\int_c^d e^{-\alpha y}dy\right),
 \qquad \alpha=z/2+it,
 \tag{1.3}
\]

and the reverse orientation uses \(z/2-it\).  On one cell of width \(L\),
the triangular contribution is

\[
 \int_0^L(L-x)e^{-\alpha x}dx
 =\frac L\alpha-\frac{1-e^{-\alpha L}}{\alpha^2}.
 \tag{1.4}
\]

Summing (1.3)--(1.4) with the alternating cell signs reproduces the jump
Green-kernel formula to machine precision in the retained finite checks.

## 2. Complex extension of the cubic cusp

T-108002 proves the edge asymptotic for real \(\lambda\ge0\).  On every
compact set

\[
 K\Subset\{\zeta:\Re\zeta>0\},
\]

the same proof is uniform with \(\lambda\) replaced by \(\zeta\).
Indeed:

1. the midpoint/difference Taylor expansion is polynomial in \(\zeta\);
2. the critical damping is
   \(\exp(-\pi\Re\zeta\,u/4)\), uniformly exponential on \(K\);
3. the stationary-row amplitude and its variation remain uniformly bounded;
4. the macroscopic-difference summation is unchanged.

Therefore

\[
 n^{-1/3}\Phi_n\!\left(4i+\zeta n^{-2/3}\right)
 \longrightarrow\mathcal A(\zeta)
 \tag{2.1}
\]

locally uniformly on the open right half-plane.

Now set \(t=\tau n^{1/3}\).  The two arguments in (0.2) are

\[
 4i+(\lambda\pm2i\tau)n^{-2/3}.
 \tag{2.2}
\]

Their prefactors tend uniformly to one.  Applying (2.1) to both terms proves
(0.5)--(0.6); averaging the two exponentials proves (0.8).

This packet deliberately keeps \(\lambda>0\).  The direct physical boundary
\(\lambda=0\) has additional interior stationary points when
\(\tau\ne0\) and requires a separate uniform boundary-tail statement.  The
Abel boundary of (0.8) exists, but no unproved direct finite-order boundary
claim is inserted here.

## 3. Proof of the dual carrier

The proposed density (0.9) is integrable for every \(\lambda>0\).  Its
inverse Fourier transform is

\[
 \frac{72e^{-i\pi/4}}{\pi^{7/2}}
 \int_0^\infty v^{-1/2}
 e^{-\lambda v/2+iv^3/3}\cos(\tau v)\,dv.
 \tag{3.1}
\]

Putting \(v=\pi u/2\) changes (3.1) exactly into (0.8).  This proves
(0.10), including every constant and phase.

The retained replay evaluates (0.8) in the nonsingular coordinate
\(u=x^2\), evaluates (3.1) independently in the coordinate \(v=x^2\), and
checks agreement at \(\lambda=2\), \(\tau=0,1,2\).  It also evaluates the
exact finite Chebyshev transform at
\(n=32,64,128,256\); the errors to (0.8) descend in every retained row.
The slow real convergence is inherited from the parent cubic-edge chart.

## 4. Exact Perron-source coordinate

The sharp assembled Perron formula has the kernel

\[
 \widehat{R_{r,z}}(t)
 =\int R_r(x)e^{-z|x|/2}e^{-itx}\,dx
 \tag{4.1}
\]

multiplying

\[
 B_\beta(s-it)B_\beta(s+it),
 \qquad s=\frac{1+z}{2}.
 \tag{4.2}
\]

At the first edge,

\[
 z_n=nc_n(\lambda)=4in+\lambda n^{1/3},
 \qquad
 s_n=\frac12+2in+\frac\lambda2n^{1/3}.
 \tag{4.3}
\]

The exact local source window is therefore

\[
 t=\tau n^{1/3},
 \tag{4.4}
\]

and the two reciprocal-zeta factors are sampled symmetrically around height
\(2n\):

\[
 B_\beta(s_n-i\tau n^{1/3})
 B_\beta(s_n+i\tau n^{1/3}).
 \tag{4.5}
\]

Equations (0.5) and (0.10) identify the complete geometric multiplier in
that window.  In the original log-ratio variable
\(x=\log(m/n)\), the dual scaling is

\[
 v=n^{1/3}x.
 \tag{4.6}
\]

Thus the exact source-facing local carrier is (0.9), attached to primitive
pairs satisfying

\[
 \log(m/n)\asymp n^{-1/3}.
 \tag{4.7}
\]

This is the first checkpoint on this branch that retains both local Perron
coordinates needed by the assembled beta source.  It does not estimate
(4.5), move the contour, or control the outer \(t\)-ranges.

## 5. What changes in the beta programme

The earlier target `BETACUSPSOURCE108004` asked for insertion of the cubic
edge into the guarded source.  The insertion coordinate is now explicit:

```text
finite Chebyshev edge
  -> t = tau n^(1/3)
  -> C(lambda,tau)
  <-> H_lambda(v), v=n^(1/3) log(m/n)
  -> symmetric reciprocal-zeta/beta correlation around height 2n.
```

Three possible but invalid shortcuts are now excluded.

1. The zero-frequency value \(\mathcal A(\lambda)\) is not the whole local
   Perron kernel.
2. An absolute-value estimate on the two translated profiles in (0.2)
   discards the cosine/cubic phase in (0.8)--(0.11).
3. A source estimate at fixed \(t\) does not control the natural
   \(n^{1/3}\)-wide frequency window.

The next named gate is

```text
BETACUSPCORR108006

Retain the complete assembled beta local states and prove a signed estimate
for

  C(lambda,tau)
  B_beta(s_n-i tau n^(1/3))
  B_beta(s_n+i tau n^(1/3))

on the full tau window, together with the outer-frequency tails.  Equivalently,
work in the primitive-pair coordinate with the exact carrier

  |v|^(-1/2) exp(-lambda |v|/2) exp(i |v|^3/3).

No channelwise absolute value may be taken before the four-state local Euler
factorization is assembled.
```

A bound of the required RH-bearing size is not proved here.

## 6. Scope ledger

| statement | status |
|---|---|
| exact finite frequency split (0.2) | **PROVED** |
| independent exact cell-pair replay | **PROVED** |
| complex cusp extension on \(\Re\zeta>0\) | **PROVED** |
| natural local frequency scale \(n^{1/3}\) | **PROVED** |
| two-parameter cusp \(\mathcal C(\lambda,\tau)\) | **PROVED** |
| exact cubic-phase dual carrier \(H_\lambda\) | **PROVED** |
| direct \(\lambda=0\), \(\tau\ne0\) finite boundary theorem | **OPEN** |
| signed beta-source correlation estimate | **OPEN** |
| full contour and outer-frequency control | **OPEN** |
| new zero-free half-plane | **NOT PROVED** |
| RH | **UNPROVED** |

## 7. Replay boundary

```text
python -B research/l-families/atlas/function_field/beta_chebyshev_perron_fourier_cusp_carrier.py --check
python -B -O research/l-families/atlas/function_field/beta_chebyshev_perron_fourier_cusp_carrier.py --check
python -B -m unittest tests.test_beta_chebyshev_perron_fourier_cusp_carrier
python -B -O -m unittest tests.test_beta_chebyshev_perron_fourier_cusp_carrier
```

The producer authenticates six exact predecessor blobs.  It performs only
bounded deterministic cell sums and Simpson integrals.  It contains no beta
summation, zeta-zero enumeration, random sampling, conductor census, or
claim that its numerical rows prove the analytic limit.
