# Full-problem attack: one annihilator, one spectral charge, and the Hausdorff saddle sectors

Agent: `gpt56-pro-global-01`  
Date: 2026-08-07  
Status: **new claims PROPOSED pending independent review; RH is not claimed proved or disproved**

## 1. Step-back verdict

The repository already contains many exact finite equivalences and proof
consumers.  Advancing another local matrix gate would not attack the full
problem.  The genuinely global objects are:

1. pole-free finite prime signals and their rightmost-zero growth;
2. critical-line spectral notches;
3. the square-screw scalar on PR #202;
4. the central Stieltjes/Hausdorff hierarchy on PR #158;
5. shifted Pick/Loewner resolvents and the kernel/operator packets.

The new work identifies one common spectral charge behind these routes and
extracts two global theorem-level consequences.

## 2. New global object: the centered all-line-zero annihilator

The finite notch widths are

\[
 r_k=2\pi/\gamma_k.
\]

Their sum diverges, but their squares are summable.  After removing the
deterministic center

\[
 \frac12\sum_{k\le M}r_k,
\]

the repeated box convolutions converge to the law of

\[
 Y=\sum_{k\ge1}V_k,
 \qquad
 V_k\sim\operatorname{Unif}[-r_k/2,r_k/2].
\]

The limiting probability kernel is smooth and subgaussian and has entire
Laplace transform

\[
 P_\infty(z)
 =\prod_{k\ge1}
  \frac{\sinh(\pi z/\gamma_k)}{\pi z/\gamma_k}.
\]

It vanishes at every critical-line zero frequency and nowhere off the imaginary
axis.  Convolving the exact triangular pole-free window with this law gives one
fixed rapidly decreasing profile `G_infty`.

The corrected prime signal

\[
 R_\infty(x)
 =\sum_n\frac{\Lambda(n)}{\sqrt n}
  G_\infty(x-\log n)-E_\infty^{\rm known}(x)
\]

satisfies

\[
 \boxed{\mathrm{RH}\iff R_\infty\equiv0.}
\]

If RH is false, its local block energy has exponential exponent exactly
`Theta_zeta`, the displacement of the rightmost zero.

This identifies the missing renormalization of the expanding finite-notch
windows:

```text
uncentered windows:
  no compact infinite limit because sum r_k diverges;

centered windows:
  one canonical subgaussian limit because sum r_k^2 converges.
```

The finite windows remain the directed approximants.  The limiting profile is a
single global target for a prime-side renewal, Selberg, or convolution identity.

File: `claims/theorems/T-21701-centered-infinite-notch-annihilator.md`.

## 3. Exact screw–Stieltjes bridge

Let

\[
 X(w)=\xi(1/2+w),
 \qquad
 G(u)=\frac{d}{du}\log\frac{X(\sqrt u)}{X(0)},
\]

and let `Psi=-g_zeta` be the square-screw signal.  The exact Laplace bridge is

\[
 \boxed{
 G(u)=\frac{\sqrt u}{2}
 \int_0^\infty e^{-\sqrt u\,t}\Psi(t)\,dt.}
\]

Under RH, the Nakamura–Suzuki Lévy charge

\[
 \sum_{\gamma>0}m_\gamma\gamma^{-2}\delta_\gamma
\]

pushes forward under `gamma -> gamma^(-2)` to the compact Hausdorff measure of
the central moment criterion.  Therefore

```text
square screw        = Fourier/Lévy coordinate,
central moments     = inverse-moment coordinate,
Jacobi–Padé model   = finite resolvent coordinate,
Pick/Loewner tests  = shifted resolvent coordinate.
```

This unification matters only because it yields new positivity.

## 4. New unconditional infinite sector of the RH-equivalent hierarchy

For

\[
 x_\rho=-1/(\rho-1/2)^2,
\]

define

\[
 \mathcal H_{m,k}(R)
 =\sum_{\Im\rho>0}m_\rho
  x_\rho^m(R-x_\rho)^k.
\]

These are the scalar Hausdorff inequalities equivalent, all together, to RH.
For every fixed `m>=1`, the new saddle calculation proves unconditionally

\[
 \boxed{
 \mathcal H_{m,k}(R)
 \sim
 \frac{\Gamma(m-1/2)}{8\pi}
 R^{k+m-1/2}k^{-m+1/2}\log k>0}
\]

as `k -> infinity`.

The proof:

1. erases the bounded horizontal displacement and evaluates the
   Riemann–von Mangoldt main integral exactly by a beta/digamma formula;
2. shows low ordinates are exponentially suppressed and high ordinates are a
   power-small tail;
3. on the saddle range `gamma ~ sqrt(k)`, uses
   `|Re rho-1/2|<=1/2` and functional-equation pairing to show the actual
   summand is `1+o(1)` times the positive real-line surrogate.

Thus every fixed Hausdorff row is eventually positive without RH.  This is an
infinite theorem sector, not finite evidence or another equivalence.

File: `claims/lemmas/L-21701-screw-stieltjes-saddle-positivity.md`.

## 5. Proposed parabolic extension

The beta saddle makes the averaged first off-line phase

\[
 O(m/\sqrt k),
\]

while the modulus error is `O(m^2/k)`.  This points to

\[
 \boxed{k/m^2\to\infty
 \Longrightarrow \mathcal H_{m,k}(R)>0.}
\]

The first-order phase cancels at the saddle, improving the previous cubic
scheduling guess to a quadratic one.  The remaining work is a uniform
Riemann–von Mangoldt Stieltjes remainder on the beta window.  This extension is
**not yet promoted as proved**.

## 6. Verified-height sector and the true transition strip

A rigorous line-zero verification to height `H` supplies a second positive
sector.  The Hausdorff saddle lies at

\[
 t_*\asymp\sqrt{k/(Rm)}.
\]

When the beta mass lies below `H`, the finite verified block is positive and the
unseen block has an off-line-safe tail.  The natural scale is

\[
 k\lesssim RH^2m,
\]

with the exact boundary supplied by directed finite data.

The global moment problem is therefore reduced to:

```text
proved:
  fixed m, k -> infinity;

finite proof data:
  saddle below the verified line-zero height;

next theorem:
  parabolic sector k >> m^2;

remaining hard region after those:
  a moving diagonal strip where the saddle has left the verified block
  but m is not small compared with sqrt(k).
```

This is a much sharper full-problem target than “prove every Hankel matrix
positive.”

## 7. Connections to kernel/operator routes

The common charge explains the repeated obstruction across the repository:

- the corrected kernel floor asks whether the charge defines a positive form
  after Schur elimination;
- the Möbius radical synthesizes test vectors probing it;
- split negative-part identities isolate its off-line component;
- central Jacobi matrices are canonical finite multiplication operators for the
  moment functional;
- the all-line-zero annihilator removes the known positive spectral support and
  leaves only the off-line residual.

A useful operator construction should be tested against the central Jacobi
moments or `R_infty`, not only a local pivot.

## 8. SERIOUS RESOLUTION PATH

**A serious full-problem path is present, but it is not complete.**

### Prime-annihilator endpoint

Prove

\[
 \sum_n\frac{\Lambda(n)}{\sqrt n}
 G_\infty(x-\log n)
 =E_\infty^{\rm known}(x)
 \quad\text{for every }x.
\]

This proves RH.  Any strict nonzero directed residual disproves RH.

### Moment-saddle endpoint

Prove the uniform parabolic asymptotic, certify the complete verified-height
saddle sector, and close the remaining diagonal strip.  All Hausdorff
inequalities then hold and the central Stieltjes criterion proves RH.  Any
negative row is a finite disproof.

Immediate ambitious tasks:

1. independently review the centered infinite-notch explicit-formula passage;
2. prove the uniform `m/sqrt(k)->0` saddle theorem with explicit constants;
3. run the complete verified-zero manifest through the saddle certificate;
4. seek a Selberg/renewal identity for the fixed subgaussian prime kernel;
5. compare its moments with the canonical Jacobi matrices and corrected
   kernel/operator moments.

No claim is made that these missing steps are routine.  They are exact
full-problem steps rather than another local proxy.