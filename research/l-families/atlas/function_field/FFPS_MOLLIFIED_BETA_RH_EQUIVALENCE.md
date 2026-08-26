# The fixed-mollified complete beta criterion is equivalent to RH

Status: **exact analytic equivalence, conditional arithmetic target; no proof
of the criterion and no proof of RH**

Bounded replay:
[`ffps_mollified_beta_rh_equivalence.py`](ffps_mollified_beta_rh_equivalence.py).

Read first:

1. `FFPS_EXTRA_NOTCHED_MELLIN_LANDAU_CONSUMER.md`;
2. `FFPS_COMPLETE_BETA_ATOMIC_VARIATION_FIREWALL.md`;
3. `FFPS_MOLLIFIED_COMPLETE_SOURCE_ADAPTER.md`.

## 0. Outcome

Let `t=log X`, let `K_ext` be the compact signed logarithmic measure from
the extra-notched consumer, and fix any `epsilon>0`.  Put

\[
 \eta_\varepsilon(t)=\varepsilon^{-1}{\bf1}_{[0,\varepsilon]}(t),
 \qquad
 \kappa_\varepsilon=\eta_\varepsilon*K_{\rm ext},
\tag{0.1}
\]

and define the complete duplicate-`67` density

\[
 h_\varepsilon(t)
 =\sum_{n\ge1}{\beta(n)\over\sqrt n}
   \kappa_\varepsilon(t-\log n),
 \qquad
 \beta(n)=\mu(n)-1_{67\mid n}\mu(n/67).
\tag{0.2}
\]

Then, for **every one fixed** `epsilon>0`, the following are equivalent:

\[
\boxed{
\begin{array}{cl}
\mathrm{(i)}&\mathrm{RH},\\[2mm]
\mathrm{(ii)}&\displaystyle
 \int_0^T|h_\varepsilon(t)|\,dt=e^{o(T)},\\[3mm]
\mathrm{(iii)}&\displaystyle
 \int_0^T(h_\varepsilon(t))_-\,dt=e^{o(T)}.
\end{array}}
\tag{0.3}
\]

Here `e^{o(T)}` means `O_delta(e^{delta T})` for every `delta>0`.
Equivalently, in multiplicative coordinates the two integrals are
`Y^{o(1)}` with `Y=e^T` and measure `dX/X`.

Consequently

\[
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \text{(iii) holds for some fixed }\varepsilon>0
 \quad\Longleftrightarrow\quad
 \text{(iii) holds for every fixed }\varepsilon>0.
\tag{0.4}
\]

This is a calibration theorem, not an RH proof.  It says that the viable
mollified one-sided estimate left by the atomic firewall is neither a weak
surrogate nor an accidentally over-strong condition: it is an exact RH
criterion.  The arithmetic programme must still prove (iii) without using
RH.

## 1. RH gives a subpower normalized beta summatory function

Write

\[
 M(x)=\sum_{n\le x}\mu(n),
 \qquad
 A_\mu(x)=\sum_{n\le x}{\mu(n)\over\sqrt n}.
\tag{1.1}
\]

The classical Mertens formulation of RH is

\[
 \mathrm{RH}\quad\Longrightarrow\quad
 M(x)=O_\delta(x^{1/2+\delta})
 \quad(\delta>0).
\tag{1.2}
\]

Partial summation gives the exact identity

\[
 A_\mu(x)
 ={M(x)\over\sqrt x}
 +{1\over2}\int_1^x {M(u)\over u^{3/2}}\,du,
\tag{1.3}
\]

and hence, after replacing `delta` by a smaller positive exponent when
needed,

\[
 A_\mu(x)=O_\delta(x^\delta).
\tag{1.4}
\]

For the complete source,

\[
\boxed{
 A_\beta(x):=\sum_{n\le x}{\beta(n)\over\sqrt n}
 =A_\mu(x)-67^{-1/2}A_\mu(x/67),}
\tag{1.5}
\]

so RH implies `A_beta(x)=O_delta(x^delta)` for every `delta>0`.

## 2. The fixed mollified kernel is compact BV

The extra-notched audit proves that `K_ext` is a finite signed measure
supported in `[0,4 log 2]`.  Convolution with the log box makes an ordinary
density

\[
 \kappa_\varepsilon(t)
 ={1\over\varepsilon}K_{\rm ext}([t-\varepsilon,t])
\tag{2.1}
\]

up to immaterial endpoint conventions.  If `V=||K_ext||_TV`, then

\[
 \operatorname{supp}\kappa_\varepsilon
 \subset[0,4\log2+\varepsilon],
 \qquad
 \|\kappa_\varepsilon\|_\infty\le {V\over\varepsilon},
 \qquad
 \operatorname{Var}(\kappa_\varepsilon)\le {2V\over\varepsilon}.
\tag{2.2}
\]

The last inequality follows distributionally from

\[
 d\kappa_\varepsilon
 ={1\over\varepsilon}
 (K_{\rm ext}-\tau_\varepsilon K_{\rm ext}).
\tag{2.3}
\]

Thus this packet uses no smoothness of the arithmetic coefficients and no
limit `epsilon->0`.

## 3. BV summation proves RH implies the two-sided bound

For fixed `t`, the weight

\[
 x\longmapsto \kappa_\varepsilon(t-\log x)
\tag{3.1}
\]

is supported on one fixed-ratio interval and has total variation
`Var(kappa_epsilon)`.  Stieltjes summation by parts and (1.5) therefore give

\[
\begin{aligned}
 |h_\varepsilon(t)|
 &\le
 \sup_{e^{t-(4\log2+\varepsilon)}\le x\le e^t}
 |A_\beta(x)|
 \left(2\|\kappa_\varepsilon\|_\infty
       +\operatorname{Var}(\kappa_\varepsilon)\right)\\
 &=O_{\delta,\varepsilon}(e^{\delta t}).
\end{aligned}
\tag{3.2}
\]

The bounded initial interval is harmless.  Integrating (3.2) proves

\[
 \int_0^T|h_\varepsilon(t)|\,dt
 =O_{\delta,\varepsilon}(e^{\delta T})
\tag{3.3}
\]

for every `delta>0`.  Hence (i) implies (ii), and (ii) trivially implies
(iii).

## 4. One-sided negative mass implies RH

For `Re(s)>1/2`, absolute Mellin--Stieltjes Fubini gives

\[
\boxed{
 \widehat h_\varepsilon(s)
 =\widehat\eta_\varepsilon(s)M_{\rm ext}(s)
 {1-67^{-(s+1/2)}\over\zeta(s+1/2)},}
\tag{4.1}
\]

where

\[
 \widehat\eta_\varepsilon(s)
 ={1-e^{-\varepsilon s}\over\varepsilon s}.
\tag{4.2}
\]

The right side of (4.1) continues meromorphically to `Re(s)>0`.  The box
multiplier is nonzero there, while `M_ext` is nonzero in
`0<Re(s)<1/2`.  By the classical critical-strip localization, a nontrivial
zeta zero `rho` with `Re(rho)>1/2` has `0<Re(rho-1/2)<1/2`; it therefore
creates a genuine pole of (4.1) at `s=rho-1/2`.

Assume (iii), and let `N(s)` be the Laplace transform of
`h_epsilon^-`.  The subpower premise makes `N` holomorphic in `Re(s)>0`.
Unconditionally `|beta(n)|<=2` and compact support of `kappa_epsilon` give
`h_epsilon^+` a finite Laplace abscissa.  If that abscissa `sigma_c` were
positive, then, initially in `Re(s)>1/2`,

\[
 \int_0^\infty h_\varepsilon^+(t)e^{-st}\,dt
 =\widehat h_\varepsilon(s)+N(s).
\tag{4.3}
\]

The right side is holomorphic near the positive real point `sigma_c`,
because (4.1) is holomorphic at every positive real point.  This contradicts
Landau's theorem for the nonnegative density `h_epsilon^+`.  (If that density
vanishes identically, the same conclusion is immediate.)  Thus
`sigma_c<=0`.  Both positive and negative transforms now converge in
`Re(s)>0`, so their difference makes (4.1) holomorphic there.  Hence (4.1)
has no pole in `Re(s)>0`, excluding every zeta zero to the right of the
critical line.  The functional equation excludes the reflected zeros.  This
proves (iii) implies (i).

This direction applies directly to the **mollified density**.  It does not
pass through the refuted raw Jordan premise.

## 5. What the equivalence changes

The exact disposition is now

```text
raw complete Jordan negative mass        Omega(sqrt(Y)); impossible
fixed-mollified complete negative mass    equivalent to RH
fixed-mollified complete absolute mass    implied by RH; sufficient via negativity
mollified complete-source adapter         separate frozen-source theorem
proof of the mollified live estimate      open / RH-bearing
RH and GRH                                unproved
```

This makes fixed mollification the canonical analytic interface for the
complete beta route.  It also prevents two unproductive moves:

- weakening back to the raw measure, whose atoms already refute the target;
- claiming that a stronger two-sided estimate is intrinsically necessary,
  since the one-sided estimate is already equivalent to RH.

The theorem supplies no sheaf estimate, varying-conductor bound,
family-to-principal amplifier, or independent proof of (iii).

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_mollified_beta_rh_equivalence.py --check
python -B -O research/l-families/atlas/function_field/ffps_mollified_beta_rh_equivalence.py --check
python -B -m unittest tests.test_ffps_mollified_beta_rh_equivalence
python -B -O -m unittest tests.test_ffps_mollified_beta_rh_equivalence
```

The replay checks only exact source identities, support/BV ledgers, and the
logical implication graph.  It enumerates no source atom, conductor, curve,
prime, or zero.
