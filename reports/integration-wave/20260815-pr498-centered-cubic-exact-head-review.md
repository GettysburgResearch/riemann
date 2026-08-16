# Independent exact-head review of PR #498

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-15T23:51:56Z
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
proposal PR:      #498
proposal base:    agent/first-hermite-q4-prime-coherence
base SHA:         87bd7ad2127f98b6141b4c03355556f2b95f6404
proposal branch:  research/gpt56-pro/93250-centered-q4-cubic-closure
reviewed head:    6cc0da2fa5711017e260ebdcea4ba8c22e453288
```

This review is confined to the centered-Q4/cubic packet. PR #508 and every factor-67 construction are excluded and are not treated as corroboration. No large computation was rerun.

## Executive verdict

```text
mathematical type:  RH-EQUIVALENT CRITERION + ROUTE INFRASTRUCTURE
review verdict:     VERIFIED WITH FIXES
RH status:          UNPROVEN
first open theorem: CPBD, or a strictly stronger deterministic
                    distinct-prime coherence estimate
```

The packet contains durable new mathematics. The mean-zero Bernoulli projection gives a single centered scalar whose Mellin multiplier is nonzero at every nontrivial zeta zero. This proves that the centered Q4 energy, without the mean coordinate, is itself RH-equivalent. The prime-block and major-arc reductions then remove the same-prime diagonal, the zero mode, and all minor modes unconditionally.

The packet does **not** prove the remaining prime-coherence estimate. `CPBD` is exactly a bound for the scalar already proved to be an RH detector. The implications `CPBD => RH` and `RH => CPBD` are both correct, making CPBD an exact RH-equivalent criterion rather than an independently established closure theorem.

## 1. Centered field and normalization

On `j/N < theta < (j+1)/N`,

\[
R_N(j)=C_\circ(N)-C_\circ(j)-C_\circ(N-j-1).
\]

The predecessor `N-j-1`, rather than `N-j`, is essential. Put

\[
M_N=\frac1N\sum_{j=0}^{N-1}R_N(j),
\qquad
\mathscr V_\circ(N)=\frac1{N^2}\sum_j|R_N(j)-M_N|^2.
\]

Since each cell has length `1/N`,

\[
\int_0^1|Q_{\circ,N}-M_N|^2=N\mathscr V_\circ(N).
\]

This is exactly the normalization used by the projection inequality.

**Disposition:** `VERIFIED`.

## 2. Bernoulli weight and cubic projection

Let

\[
w(\theta)=\theta(1-\theta)-\frac16=-B_2(\theta).
\]

Then

\[
\int_0^1w=0,
\qquad
\int_0^1w^2=\frac1{180}.
\]

The antiderivative kernel is

\[
K(x)=2\int_0^xw(u)du=\frac{x(1-x)(2x-1)}3,
\]

with

\[
K(0)=K(1)=0,
\qquad K(1-x)=-K(x),
\qquad \|K\|_\infty^2=\frac1{972}.
\]

For

\[
\mathcal A_\circ(N)=\int_0^1w(\theta)Q_{\circ,N}(\theta)d\theta,
\]

mean zero and Cauchy give

\[
|\mathcal A_\circ(N)|^2\le\frac N{180}\mathscr V_\circ(N).
\]

Reversing the endpoint prefixes gives the exact finite identity

\[
\boxed{\mathcal A_\circ(N)=\sum_{m\le N}c_\circ(m)K(m/N).}
\]

No asymptotic passage is used, and the `m=N` term vanishes because `K(1)=0`.

**Disposition:** `VERIFIED`.

## 3. Mellin argument

The cubic multiplier is

\[
\widehat K(s)=\int_0^1K(x)x^{s-1}dx
=\frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

For `Re(s)>1`,

\[
\begin{aligned}
\int_1^\infty\mathcal A_\circ(X)X^{-s-1}dX
={}&\widehat K(s)\\
&\times\left[(1-4^{1-s})\left(-\frac{\zeta'}\zeta(s)\right)
+3(\log4)\frac{4^{-s}}{1-4^{-s}}\right].
\end{aligned}
\]

At a nontrivial zero `rho` in the open strip, none of

```text
rho-1,
1-4^(1-rho),
1-4^(-rho),
(rho+1)(rho+2)(rho+3)
```

vanishes. Hence the logarithmic-derivative pole survives.

For `N<=X<N+1`, the active integer set is unchanged. Since `||K'||_infty<=1/3` and `sum_(m<=N) m|c_circ(m)| << N^2`,

\[
\mathcal A_\circ(X)-\mathcal A_\circ(N)=O(1).
\]

**Disposition:** `VERIFIED WITH FIXES`; the weighted-source interpolation bound should be pinned as an explicit elementary lemma.

## 4. Both directions of the equivalence

Under RH, von Koch gives

\[
\psi(x)=x+O(\sqrt x\log^2x).
\]

The Q4 main terms cancel in `psi(x)-4psi(x/4)`, so `C_circ(x)=O(sqrt(x)log^2x)`. Uniformly in `j`,

\[
R_N(j)=O(\sqrt N\log^2N),
\]

and therefore

\[
\mathscr V_\circ(N)=O(\log^4N).
\]

Conversely, if `V_circ(N) << log^A N`, the projection inequality gives

\[
\mathcal A_\circ(N)=O(\sqrt N\log^{A/2}N).
\]

After real-endpoint interpolation, the Mellin integral is holomorphic in `Re(s)>1/2`. The exact formula would have a nonremovable pole at every zeta zero there, so no such zero exists. Functional-equation symmetry gives RH.

Thus

\[
\boxed{\mathrm{RH}\iff\mathscr V_\circ(N)\ll\log^A N\text{ for some fixed }A.}
\]

**Disposition:** `VERIFIED`, mathematical type `RH-EQUIVALENT CRITERION`.

## 5. Prime blocks

The source partitions exactly by prime base:

\[
c_\circ=\sum_pc_{\circ,p},
\qquad
\mathcal A_\circ(N)=\sum_pZ_{p,N},
\]

where

\[
Z_{p,N}=\sum_{m\le N}c_{\circ,p}(m)K(m/N).
\]

The four-adic gauge belongs to the `p=2` block. If

\[
A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|,
\]

then `|Z_p|<=||K||_infty A_p`. The imported complete-tower estimate

\[
\sum_pA_{p,N}^2\le80N\log(2N)
\]

gives

\[
\boxed{\sum_p|Z_{p,N}|^2\le\frac{20}{243}N\log(2N).}
\]

The coherence conclusions are valid inverse theorems: a large total forces many positively projecting blocks. They do not bound the total from above.

**Disposition:** `VERIFIED WITH FIXES / ROUTE INFRASTRUCTURE`.

## 6. Mean-free major arc

Center each prime row. Centering deletes only the zero Fourier coordinate. The imported exact bounds give

\[
\frac1{N^2}\sum_p\|\widetilde R_{N,p}\|_2^2\le720\log(2N)
\]

and

\[
|\mathfrak C_{\ne p}^{\rm min}(N)|\le744\log(2N).
\]

If `C_nep^(maj,0)` contains only distinct-prime nonzero modes with

\[
d_N(a)=\min(a,N-a)<\lceil\sqrt N\rceil,
\]

then

\[
\boxed{|\mathscr V_\circ(N)-\mathfrak C_{\ne p}^{\rm maj,0}(N)|\le1464\log(2N).}
\]

The surviving reduced additive moduli satisfy `q=N/(a,N)>sqrt(N)`.

**Disposition:** `VERIFIED WITH FIXES`, conditional on the exact imported `L-93015` bounds pinned in the source lock.

## 7. CPBD boundary

CPBD is

\[
\left|\sum_pZ_{p,N}\right|^2\ll N\log^B N.
\]

Its left side is exactly `|A_circ(N)|^2`. Therefore

\[
\boxed{\mathrm{CPBD}\iff\mathrm{RH}.}
\]

This is a clean producer interface, not a proved decorrelation theorem. The shared one-dimensional coherence ratio with First-Hermite supplies common Hilbert-space geometry but transfers no arithmetic upper bound between the routes.

**Disposition:** `VERIFIED RH-EQUIVALENT CRITERION`; `CPBD OPEN`.

## Durable mathematics

The following survive independently of CPBD:

1. the mean-zero cubic test preserves every nontrivial zeta pole;
2. centered Q4 energy alone is RH-equivalent;
3. the arithmetic detector is an exact cubic Riesz sum;
4. its same-prime scalar diagonal is `O(N log N)`;
5. the zero mode, same-prime terms and all minor modes are removed from the remaining obstruction;
6. the cardinality-only shortcut is exactly refuted.

## Computational artifact

The retained `X-93250` object is an exact-rational finite regression. It does not prove the analytic zeta inputs, the imported `L-93015` bounds, CPBD, or RH.

The review adds a smaller independent replay:

```text
PASS_PR498_CENTERED_CUBIC_REVIEW_ALGEBRA
d37db9d9d5b3bbd2dec8ab844a55e3994256f53455ec30eeb94a9fc870dc5c04
```

## Claim status

```text
L-93250  VERIFIED WITH MINOR PROVENANCE FIX
T-93251  VERIFIED / RH-EQUIVALENT CRITERION
L-93252  VERIFIED WITH FIXES / ROUTE INFRASTRUCTURE
T-93253  VERIFIED WITH FIXES / RH-EQUIVALENT CRITERION
R-93254  VERIFIED / REFUTATION
T-93255  VERIFIED CONDITIONAL COMPOSITION; CPBD OPEN
X-93250  VERIFIED FINITE REGRESSION ONLY
RH        UNPROVEN
```

## Integration recommendation

Retain the cubic projection, centered-energy equivalence, prime-block diagonal and mean-free major-arc theorem with explicit `RH-EQUIVALENT CRITERION` labels. Do not promote CPBD or the common heat/Q4 coherence geometry as an unconditional theorem.