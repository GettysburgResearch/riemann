# Beta band-pass and curve-wavelet successor: five-minute handoff

Status: **frozen exploratory theorem atlas; the current head adds a universal
compact-kernel information theorem, the unique all-order Chebyshev BV
extremizer, an exact moving safe-factor phase diagram, finite autocorrelation
geometry, a global max-cusp Stieltjes/primitive hierarchy and compensation
law, near-notch and endpoint-layer asymptotics, and ensemble firewalls; RH
and GRH remain open**

Parent release: draft PR #757 at
\(b870366141fe8d5f43d5b81f6e50a67d2a888070\).

This successor advances:

- [Programme I #736](https://github.com/gfreund123/riemann/issues/736),
  the Dirichlet-character completion of the canonical detector;
- [Programme II #737](https://github.com/gfreund123/riemann/issues/737),
  the function-field mirror and physical-occupancy programme;
- [Programme VI #741](https://github.com/gfreund123/riemann/issues/741),
  the general detector atlas.

The complete replay and scope ledger is in
[BETA_BANDPASS_WAVELET_RELEASE_AUDIT.md](BETA_BANDPASS_WAVELET_RELEASE_AUDIT.md).

## If you are the next agent, start here

The fastest route into the current head is:

1. Read
   [FFPS_CHEBYSHEV_BV_KERNEL_EXTREMIZER.md](function_field/FFPS_CHEBYSHEV_BV_KERNEL_EXTREMIZER.md),
   then
   [FFPS_SHARP_BV_SAFE_FACTOR_PHASE_DIAGRAM.md](function_field/FFPS_SHARP_BV_SAFE_FACTOR_PHASE_DIAGRAM.md)
   and
   [FFPS_CHEBYSHEV_STEP_AUTOCORRELATION_NORMAL_FORM.md](function_field/FFPS_CHEBYSHEV_STEP_AUTOCORRELATION_NORMAL_FORM.md),
   followed by
   [FFPS_CHEBYSHEV_MAX_CUSP_COMPENSATION.md](function_field/FFPS_CHEBYSHEV_MAX_CUSP_COMPENSATION.md).
   Two independent Chebyshev duals prove that the alternating step uniquely
   minimizes the *complete* universal forward size
   \(\|K\|_\infty+\operatorname{Var}K\) at every information order. The
   resulting safe-factor constants

   \[
    A_r=\frac{16^r(2r+3)^2}
    {(2r+1)\binom{2r}{r}^2}
   \]

   increase strictly from \(A_0=9\), with \(A_r\sim2\pi r^2\). Thus an extra
   vanished moment never improves the universal BV certificate. Its value
   must come from kernel/source-specific geometry. The third packet supplies
   exactly that next coordinate: a finite atomic formula for \(-R_r''\), the
   exact cusp \(R_r(s)/R_r(0)=1-(2r+1)|s|\) on its maximal disjoint-jump
   window, and the exact order-\(2r\) Fourier notch.

   The fourth packet reconnects this geometry to the assembled Perron max
   cusp. Its normalized linear refill coefficient is exact and decays like
   \(r^{-2}\), but its product with the sharp BV cost decreases to the
   nonzero limit \(\pi^3/36\). The isolated zero-mode expansion has a
   sharp uniform Young-envelope error bounded by \((3/16)z\) on unit
   support. More strongly, the complete positive-tilt transform is a strict
   Stieltjes function with a finite difference formula, global alternating
   causal-primitive bounds, an exact terminal even cusp coefficient, and a
   uniform complex kernel-transform zero-free half-disk.

2. Read
   [FFPS_COMPACT_KERNEL_INFORMATION_ORDER.md](function_field/FFPS_COMPACT_KERNEL_INFORMATION_ORDER.md)
   and
   [FFPS_CARRIER_ENSEMBLE_CONDITION_FIREWALL.md](function_field/FFPS_CARRIER_ENSEMBLE_CONDITION_FIREWALL.md).
   Every fixed nonzero real compact BV kernel gives an RH-equivalent normalized
   beta energy; its first surviving moment determines the reverse power.
   Positive direct sums cannot beat the best constituent condition number,
   coherent sums factor through their first surviving moment, and order zero
   is a genuine low-pass loophole rather than a derivative-rung competitor.

3. Read
   [FFPS_SPECTRAL_NEAR_NOTCH_CONDITIONING.md](function_field/FFPS_SPECTRAL_NEAR_NOTCH_CONDITIONING.md)
   and
   [FFPS_TILT_ENDPOINT_LAYER_PHASE_DIAGRAM.md](function_field/FFPS_TILT_ENDPOINT_LAYER_PHASE_DIAGRAM.md).
   The first resolves the singular perturbation around every Bessel notch,
   including its exact quadratic energy excess and shifted local profile. The
   second proves the large-tilt Gamma endpoint layer and the exact moving-tilt
   RH-safe phase boundary. These close two tempting numerical extrapolations
   without using heavy root searches or beta sums.

4. Then read
   [FFPS_HIGHER_DERIVATIVE_CARRIER_HIERARCHY.md](function_field/FFPS_HIGHER_DERIVATIVE_CARRIER_HIERARCHY.md).
   This is now the strongest direct-beta front door. At every fixed
   derivative rung \(m\ge1\),

   \[
    (\log X+S_X)^{2m+1}\mathcal E_{m,S_X}(X)
    =
    C_m|B(X)|^2
    +(\log X+S_X)^{2m+1}\|H_X-H_{X,*}\|_2^2,
   \]

   where
   \(C_m=(m!)^2(2m+1)\binom{2m}{m}^2\). The positive beta polynomial is
   the unique optimum even among signed carriers. For its complete
   translated field and **any** schedule \(S_X\ge1\),

   \[
    \mathrm{RH}
    \Longleftrightarrow
    (\log X+S_X)^{2m+1}\mathcal E_{m,S_X}(X)=X^{o(1)}.
   \]

   After division by \(C_m\), the equivalence remains valid in the safe
   growing window
   \(m=o(\log X/\log\log X)\) at fixed width. This is an exact
   criterion, not the missing estimate. The best next analytic problem
   is still to exploit source cancellation in the translated beta
   convolution; support, positivity, derivative order, and diagonal
   normalization are now closed sharply.

5. Then read
   [FFPS_BETA_CARRIER_LEGENDRE_MOMENT_TOWER.md](function_field/FFPS_BETA_CARRIER_LEGENDRE_MOMENT_TOWER.md)
   and
   [FFPS_SPECTRAL_ZERO_FREE_CARRIER_TILT.md](function_field/FFPS_SPECTRAL_ZERO_FREE_CARRIER_TILT.md).
   The first proves that every fixed signed field moment is itself
   RH-equivalent, organizes all logarithmic beta moments into a
   complete Legendre Parseval tower, and gives an RH-forward
   growing-order window. The second constructs positive carriers with
   no real Fourier zeros whose energies approach the sharp optimum.
   Real spectral zero-freeness has no uniform energy gap; moreover only
   the positive tilt orientation is zero-free in the right Laplace
   half-plane.

6. For the original first-derivative phase diagram and its provenance,
   read
   [FFPS_MOVING_SUPPORT_CARRIER_PHASE_DIAGRAM.md](function_field/FFPS_MOVING_SUPPORT_CARRIER_PHASE_DIAGRAM.md),
   [FFPS_UNIFORM_MOVING_CARRIER_BETA_CRITERION.md](function_field/FFPS_UNIFORM_MOVING_CARRIER_BETA_CRITERION.md),
   and
   [FFPS_VARIATIONAL_PROBABILITY_CARRIER_OPTIMUM.md](function_field/FFPS_VARIATIONAL_PROBABILITY_CARRIER_OPTIMUM.md).

7. For the arithmetic-geometric mirror, read
   [FUNCTION_FIELD_MOBIUS_CARRIER_CALIBRATION.md](function_field/FUNCTION_FIELD_MOBIUS_CARRIER_CALIBRATION.md),
   then
   [FFPS_FUNCTION_FIELD_BETA_DIVISOR_WAVELET_PILOT.md](function_field/FFPS_FUNCTION_FIELD_BETA_DIVISOR_WAVELET_PILOT.md).
   The first proves the exact curve-zeta analogue of the carrier energy;
   the second identifies the surviving twisted \(L\)-channel in the
   divisor-wavelet port. Known function-field RH is imported only as a
   calibration theorem.

8. For the sheaf/Adams route, read
   [FFPS_MARKED_PLACE_BIFROBENIUS_GLUING_GATE.md](function_field/FFPS_MARKED_PLACE_BIFROBENIUS_GLUING_GATE.md)
   and
   [FFPS_TERNARY_RELATIVE_CORRESPONDENCE_NORMAL_FORM.md](function_field/FFPS_TERNARY_RELATIVE_CORRESPONDENCE_NORMAL_FORM.md).
   The corrected obstruction is the crossed source graph under partial
   Frobenius, not an unsupported claim that every local
   Artin--Schreier/incidence block fails. A signed
   pushforward/correspondence realization remains open.

9. Use
   [BETA_BANDPASS_WAVELET_RELEASE_AUDIT.md](BETA_BANDPASS_WAVELET_RELEASE_AUDIT.md)
   as the claim and replay ledger. Older sections below remain useful
   provenance, but this list supersedes their original entry order.

Do not begin with finite scouts. Do not infer a number-field estimate
from a complete function-field identity. Do not treat an RH-equivalent
criterion as progress on its open arithmetic estimate. Do not revive a
carrier-sign or compact-kernel-zero argument without first quotienting
the exact spectral surgery and chirality firewalls.

## Current-head synthesis: eight new theorem packets

The newest continuation starts with a local spectral question and ends with a
complete compact-kernel design theorem.

1. Near every positive Bessel notch, the tilted Fourier floor and energy
   excess are both quadratic in the tilt. The local notch profile has an exact
   shifted quadratic normal form; the high-notch condition product is
   explicit.
2. At large tilt, the normalized beta carrier converges after endpoint
   rescaling to a Gamma layer. Its derivative energy has a two-term exact
   asymptotic, producing the moving tilt/support phase diagram.
3. Positive detector ensembles obey a convex condition firewall, while
   coherent combinations factor through the first surviving moment. The
   order-zero low-pass row remains RH-equivalent for arbitrary finite support
   and must not be silently excluded.
4. Every fixed nonzero compact real BV kernel has a finite information order
   and an RH-equivalent normalized energy. This is a classification of
   observables, not a cancellation estimate.
5. For a prescribed information order and sensitivity, the unique minimizer
   of zero-extended variation is also the unique minimizer of the complete BV
   size. Its derivative lives on Chebyshev--Lobatto extrema, and the kernel is
   the alternating sign of a second-kind Chebyshev polynomial.
6. After width normalization, the exact universal safe factor is

   \[
    A_r\left(1+\frac{\log X}{W}\right)^{2r+2}.
   \]

   The constants \(A_r\) grow strictly and log-concavely. The packet also
   upgrades the normalized RH corollary to variable information order and
   identifies the exact power-law safe region.
7. The optimal step's autocorrelation has finite atomic curvature. Its local
   cusp steepens like \(r\), but its disjoint-jump window shrinks like
   \(r^{-2}\); from order four onward the local linear branch ends before its
   formal zero. This is a concrete warning against turning a spectral notch
   into an unsupported resolution claim.
8. The max-cusp refill can be evaluated exactly. Its normalized coefficient
   shrinks quadratically with order, but the sharp BV cost grows quadratically;
   their product decreases strictly to \(\pi^3/36\). An exact primitive
   \(L^1\) formula makes the relative linear refill uniform in order. The
   global resolvent is strictly Stieltjes on positive tilt, every causal
   primitive supplies an alternating upper or lower bound, and the first
   surviving moment forces the terminal even cusp coefficient. After the
   Perron \(1/z\) and the sharp BV cost are charged, the local Chebyshev
   zero mode has a nonvanishing \(\pi^3/36\) floor; this remains a geometric
   family-specific barrier, not a beta estimate.

The scientific direction is now sharper: universal carrier geometry is
closed enough that another gain must preserve the signs in the beta
primitive-pair/Fourier coupling or exploit a genuinely arithmetic
function-field/sheaf channel.

## 0. What the aggressive continuation actually established

### A. The first moment is one row of an all-order detector tower

For one fixed unit-mass carrier \(Q\), the complete field moments obey

\[
 M_k(X)
 =-k\sum_{j=0}^{k-1}\binom{k-1}{j}q_jB_{k-1-j}(X).
\]

The transform is triangular and has the exponential generating
identity

\[
 \mathscr H_X(z)=-z\mathscr Q(z)\mathscr B_X(z).
\]

Every one fixed \(M_k(X)=X^{o(1)}\) is RH-equivalent. Higher \(k\)
magnifies an off-line pole order but does not improve the Mertens power
exponent. The complete shifted-Legendre decomposition resolves every
logarithmic beta moment into an exact nonnegative energy channel. RH
also pays a forward growing-order window
\(k=o(\log X/\log\log X)\) at fixed carrier support; no diagonal
growing-order converse is inferred.

### B. Higher derivatives give an exact fixed- and growing-rung hierarchy

The positive beta carrier

\[
 Q_{m,S}(t)=
 \frac{(2m+1)!}{m!^2S^{2m+1}}t^m(S-t)^m
\]

is the unique minimizer of \(\|D^mQ\|_2\) among all signed unit-mass
carriers on \([0,S]\). Its detector is exactly a shifted Legendre
polynomial. The matched field moment remains
\(M_m=(-1)^mm!B(X)\), so it cannot be tuned away by a moving carrier.

The critical width power is \(2m+1\). Below it, Young dilation makes
the premise trivial; above it, an adaptive width forces a macroscopic
renormalized energy along an infinite subsequence. After the sharp
factorial normalization, the criterion remains RH-equivalent for
growing \(m\) whenever

\[
 \log((2m+1)(2m+3)^2)
 +(2m+2)\log((\log X+S)/S)=o(\log X).
\]

### C. Real spectral zero-freeness has no carrier-energy gap

Exponential tilts of the beta optimizer are positive and have no real
Fourier zeros for every nonzero real tilt. Their \(D^m\)-energies are
strictly above the optimum but converge to it as the tilt tends to
zero. Hence the real-Fourier-zero-free positive class has the same
sharp infimum, which it does not attain.

The sign of the tilt remains decisive for Landau-style use: the
Laplace zero lattice lies on
\(\Re z=-2\tau/S\). Positive tilt is right-half-plane zero-free;
negative tilt moves the lattice into that half-plane. This is a
spectral-factor design theorem and firewall, not beta cancellation.

### D. The carrier problem has a sharp universal first-rung solution

For every compact unit-mass carrier \(Q_X\), signed or positive, whose
zero-extended derivative is in \(L^2\), the complete beta field obeys

\[
 \int H_X=0,\qquad
 \int tH_X(t)\,dt=-B(X).
\]

Centered Cauchy--Schwarz gives the optimal constant \(12\), realized by
the parabolic one-atom field. It also gives:

- an exact Pythagorean Mertens-plus-shape decomposition;
- an exact signed-autocorrelation second moment
  \(\int u^2\mathcal C_X(u)\,du=-2B(X)^2\);
- a projected finite-abscissa Laplace inequality converging to the
  centered moment law;
- a raw-energy zero-free wedge
  \(\Re\rho\le1/2+3\gamma/2\) when
  \(S_X\le X^{\gamma+o(1)}\);
- a critical renormalization exponent \(p=3\): every \(p<3\) admits a
  trivially diluted schedule, while the current all-support RH forward
  theorem does not pay \(p>3\).

The result does not prove a beta-energy bound. It identifies exactly
which part of such a bound is the classical Mertens signal and which
part is carrier geometry.

### E. Several attractive compact-kernel shortcuts are now closed

The continuation proves that:

- energy does not determine carrier chirality;
- compact carrier zeros can be flipped without changing the energy;
- all finite compact spectral-factor surgeries preserving the
  autocorrelation can be classified;
- the signed beta Gram problem has an exact annular primitive normal
  form, but positivity/diagonal interpolation alone cannot close it;
- the critical moving-order scale found earlier is a boundary of one
  Fourier-comparison method, not a boundary of RH-equivalent carriers.

These are design firewalls. Future detectors must use source arithmetic,
not the sign or zero set of a chosen compact factor.

### F. The function-field calibration is exact

For a fixed smooth projective curve \(C/\mathbf F_q\), the normalized
Möbius coefficients of \(1/Z_C(u)\) and a short parabolic carrier give
disjoint degree translates and the exact energy

\[
 \mathcal E_N={96\over(\log q)^3}
 \sum_{n\le N}|q^{-n/2}M_C(n)|^2.
\]

The corresponding subpower criterion is equivalent to the curve's
reciprocal roots lying on \(|\alpha|=\sqrt q\). Weil RH supplies that
fact; the packet does not reprove it. This is the cleanest exact
calibration of the number-field carrier mechanism now in the atlas.

## 1. The strongest new analytic localization

For every fixed positive \(\ell,\varepsilon\) and integer \(r\ge1\), one
compact \(C^\infty\) source-faithful kernel satisfies, for every fixed
\(\kappa>0\),

\[
 {1\over2\pi}\int_{|t|\ge e^{\kappa\sqrt{\log X}}}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt
 \le X^{1-\kappa^2/\log2+o(1)}.
\]

At the threshold \(\kappa=\sqrt{\log2}\), this gives

\[
 \boxed{\mathrm{RH}\Longleftrightarrow
 {1\over2\pi}\int_{|t|\le
 e^{\sqrt{(\log2)(\log X)}}}
 |\widehat B_{r,\infty}(t)|^2|D_X(t)|^2dt=X^{o(1)}.}
\]

The constant is the threshold of the exact Fourier stair bound plus the
trivial beta estimate, not an asserted arithmetic optimum. For any
\(\kappa>\sqrt{\log2}\), the exterior tail has a fixed power saving.

There is also an every-power refinement. For each fixed
\(0<\theta<1/2\), set

\[
 T_\theta(X)=\exp\!\left((\log X)^{1/2+\theta}\right)=X^{o(1)}.
\]

Then

\[
 {1\over2\pi}\int_{|t|\ge T_\theta(X)}
 |\widehat B_{r,\infty}(t)|^2
 \left|\sum_{n\le X}{\beta(n)\over n^{1/2+it}}\right|^2dt
 =O_A(X^{-A})
\]

for every \(A>0\), again without Möbius cancellation. The RH criterion
also holds with \(T_\theta(X)\) in place of the smaller critical cutoff.

The infinite dyadic box convolution is fixed independently of \(X\). Its
Laplace product is zero-free in the open right half-plane, so it preserves
the Mellin--Landau pole detector, while its Fourier transform has explicit
log-square decay. This is a real closure of the exterior-frequency lane.
It is not an estimate inside either remaining window.

## 2. The assembled beta problem is genuinely one-variable

Every nonzero complete beta pair has the unique form

\[
 m=67^iga,\qquad n=67^jgb,\qquad N=ab,
\]

with \(i,j\in\{0,1,2\}\) and pairwise-coprime squarefree
\(67\)-free \(g,a,b\). The full positive prefix energy is therefore

\[
 \boxed{\mathcal E(X)=
 \sum_{\substack{N\ {\rm squarefree}\\67\nmid N}}
 {\mu(N)\over\sqrt N}\mathscr W_X(N).}
\]

All three exceptional orientations, every divisor orientation, the common
factor, and the sharp endpoints remain assembled inside
\(\mathscr W_X(N)\). The \(N=1\) term is exactly the complete logarithmic
diagonal; every \(N>1\) term is off-diagonal. Thus RH is equivalent to one
explicit one-variable signed Möbius-wavelet bound.

The complete local Euler algebra closes with no correction product:

\[
 1+p^{-2s}-p^{-s+it}-p^{-s-it}
 =(1-p^{-s+it})(1-p^{-s-it}).
\]

The difficulty is boundary control of the signed reciprocal-zeta pair, not
a missing local factor.

Read
[FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md](function_field/FFPS_ASSEMBLED_BETA_PERRON_FOURIER_BRIDGE.md).

## 3. Arbitrary fixed notches are valid, but the max cusp defeats a shortcut

Every fixed kernel

\[
 B_{r,j}=\eta_\ell^{*j}*\Delta_\varepsilon^rK_{\rm bd}
\]

is a nonzero compact BV beta detector and gives an exact RH-equivalent
prefix energy. Its autocorrelation has an exact zero of order \(2r\) at
Fourier frequency zero, with independently selectable fixed
high-frequency decay.

Read
[FFPS_BANDPASS_BETA_ENERGY_LADDER.md](function_field/FFPS_BANDPASS_BETA_ENERGY_LADDER.md).

The sharp double-Perron coordinate retains that notch. But eliminating the
relative contour creates the max cusp exactly:

\[
 {1\over2\pi i}\int_{\Re v=a}
 {e^{-vx}\over(z/2+v)(z/2-v)}\,dv
 ={e^{-z|x|/2}\over z}.
\]

Here \(\Re z>0\) and \(-\Re z/2<a<\Re z/2\); outside that strip the
displayed Barnes identity is not valid.

For every nonzero compact mean-zero band \(B\), with cumulative \(F\),

\[
 \int_{\mathbf R}|x|R(x)\,dx=-2\|F\|_2^2<0
\]

and hence

\[
 \widehat{R(x)e^{-z|x|/2}}(0)
 =z\|F\|_2^2+O(z^2).
\]

Therefore increasing the fixed notch order never improves the max-tilt
leakage beyond linear order. The live analytic choice is exact:

- retain the relative contour and face a bilateral reciprocal-zeta problem;
- eliminate it and explicitly pay the forced linear cusp channel.

No contour estimate is proved on either side.

## 4. A hierarchy correction: BASEWAVE is not easier than PRIMCAR

At coherent core \(u=1\),

\[
 \mathcal C^\alpha_{d,1}(I)
 =\mathcal P^0_{67^\alpha,1}(d;I)
 =\mathcal P_I^{(\alpha,0)}(d)
\]

predicate by predicate. Therefore

\[
 \boxed{\mathrm{BASEWAVE}=\mathrm{PRIMCAR}.}
\]

The corrected conditional graph is

\[
 \begin{aligned}
 \mathrm{AUXCOLORPRIMCAR}
 &\Longrightarrow\mathrm{PRIMCAR}
 \Longrightarrow\mathrm{PRIMLS}\Longrightarrow\mathrm{RH},\\
 \mathrm{WAVEPRIMCAR}
 &\Longrightarrow\mathrm{BASEWAVE}
 (=\mathrm{PRIMCAR})
 \Longrightarrow\mathrm{PRIMLS}\Longrightarrow\mathrm{RH}.
 \end{aligned}
\]

The outer \(\eta<1/2\) condition is irrelevant to direct selection of
\(u=1\). None of these open estimates is proved. This correction prevents a
future agent from treating the base wavelet as a smaller intermediate
theorem.

Read
[FFPS_BASEWAVE_PRIMCAR_IDENTITY.md](function_field/FFPS_BASEWAVE_PRIMCAR_IDENTITY.md).

## 5. The function-field shadow exposes exact Frobenius channels

For the complete affine genus-zero shadow, the oriented Euler product has
the exact factorization

\[
 F_{q,e}(X,Y)=
 {(1-\sqrt qX)(1-\sqrt qY)(1-XY)\over
  (1-q^{-e/2}X^e)(1-q^{-e/2}Y^e)
  (1-q^{-e}(XY)^e)}
 \mathcal J_{q,e}(X,Y).
\]

The diagonal channel is the zero \(1-XY\), not a pole, and every fixed
complete degree shell decays as

\[
 O_\varepsilon(q^{-(1/3-\varepsilon)h}).
\]

Read
[FUNCTION_FIELD_BASEWAVE_SHADOW.md](function_field/FUNCTION_FIELD_BASEWAVE_SHADOW.md).

For every fixed smooth projective curve \(C/\mathbf F_q\) and finite deleted
set \(\Sigma\), the exact extension is

\[
 \boxed{
 F_{C,\Sigma}=
 {\mathcal J_{C,\Sigma}\over
 Z_C(X/\sqrt q)Z_C(Y/\sqrt q)Z_C(XY/q)D_\Sigma}.}
\]

Positive genus replaces the affine exponential decay by explicit normalized
Frobenius residues. If \(m_C\) is the largest multiplicity of a normalized
Frobenius root, then

\[
 [X^iY^j]F_{C,\Sigma}
 =O((i+1)^{m_C-1}(j+1)^{m_C-1}).
\]

More sharply, every fixed-offset shell is a finite unit-circle
exponential-polynomial plus an exponentially decaying error. Simple
Frobenius roots give bounded complete shells; repeated roots permit the
displayed polynomial upper bound, though residue cancellation can lower it.
No general decay or square-summability follows in positive genus.

This provides a concrete inverse-design target: cancel selected axis
Frobenius residues while preserving a chosen mixed or source-specific
channel. It still omits incomplete owner/Boolean restrictions, nontrivial
cores, harmonic sieve averaging, and nonzero incidence modes.

## 6. The native Adams obstruction is a crossed source graph

The earlier internal-rank calculation

\[
 \operatorname {rank}(QI_m-J_m)=
 \begin{cases}m,&m<Q,\\Q-1,&m=Q\end{cases}
\]

is correct but was initially applied across the wrong tensor axes. The
closed-point Adams factors are the two **marked-place blocks**
\(\ell\mid\rho\), not phase versus residue inside one block. An internal
kernel \(H_\ell\) times an internal kernel \(H_\rho\) has marked-block
separation rank one regardless of the two internal matrix ranks.

Under simultaneous Frobenius of a complete marked block, the local
Artin--Schreier line and centered incidence are ordinary Weil objects.
The natural raw source fails the marked-place external-product gate for
a different reason:

\[
 \boxed{
 \ell=P^-(c),\quad c\mapsto Pc^2\bmod\rho;
 \qquad
 \rho=P^-(d),\quad d\mapsto Qd^2\bmod\ell.}
\]

Each reduced core is selected on one side and evaluated on the other.
Common-core, Boolean, coprimality, owner, shell, and cleanup conditions
add further crossed relations.

Therefore:

- the clean rank-\(48\) ternary norm/Kummer package passes the separable
  gate;
- the natural raw complete native source does not currently pass it;
- large internal \(QI-J\) rank is **not** a marked-place Adams no-go;
- a complete signed pushforward could still erase the crossed support;
- a graph-shift or correspondence-level Adams formula remains viable.

No such pushed-forward bifrobenius class or uniform trace estimate has
been constructed.

## 7. What is closed, refuted, and open

| object | verdict |
|---|---|
| exterior spectral energy beyond \(e^{\sqrt{(\log2)(\log X)}}\) | **\(X^{o(1)}\) UNCONDITIONALLY FOR ONE FIXED DETECTOR** |
| exterior energy beyond \(e^{(\log X)^{1/2+\theta}}\), fixed \(0<\theta<1/2\) | **EVERY-POWER SAVING UNCONDITIONALLY** |
| complete beta reindexing into one \(N\)-wavelet | **PROVED EXACT** |
| arbitrary fixed finite-difference notch remains RH-equivalent | **PROVED EXACT** |
| repeated notching removes max/Perron leakage | **REFUTED: LEAKAGE IS FORCED LINEAR** |
| BASEWAVE is a smaller gate than PRIMCAR | **REFUTED: THEY ARE IDENTICAL** |
| complete genus-zero shadow | **PROVED WITH EXPONENTIAL SHELL DECAY** |
| complete fixed-curve shadow | **PROVED WITH FROBENIUS RESIDUE EXPANSION** |
| large internal \(QI-J\) rank proves large marked-place separation rank | **REFUTED** |
| natural raw native source has a marked-place external product | **OBSTRUCTED BY THE CROSSED SOURCE GRAPH** |
| width-renormalized parabolic carrier energy for arbitrary support | **RH-EQUIVALENT; ESTIMATE OPEN** |
| raw moving-support energy at exponent \(\gamma\) | **ZERO-FREE WEDGE PROVED; FULL RH ONLY AT \(\gamma=0\)** |
| carrier chirality or compact zero set is determined by energy | **REFUTED** |
| curve-zeta parabolic carrier calibration | **PROVED EXACT; WEIL RH IMPORTED** |
| beta energy inside the critical frequency window | **OPEN; RH-EQUIVALENT** |
| bilateral boundary-contour estimate | **OPEN; RH-STRENGTH** |
| incomplete/source-faithful function-field shadow | **OPEN** |
| actual native physical occupancy | **OPEN** |
| complete signed relative sheaf complex and uniform trace estimate | **OPEN** |
| CYSEL, WCADD, WCKUM, principal extraction, RH, or GRH | **NOT PROVED** |

## 8. Best next ambitious experiments

### A. Arithmetic control of the carrier shape defect

Start from the exact decomposition

\[
 (\log X+S_X)^3\mathcal E_Q(X)
 =
 12|B(X)|^2
 +(\log X+S_X)^3\|H_X-H_{X,*}\|_2^2.
\]

The abstract support/moment problem is solved optimally. A meaningful
advance must now use the discrete translated beta convolution. Promising
coordinates are:

- higher centered moments of \(H_X\) and their exact beta-weighted
  polynomial statistics;
- the signed autocorrelation curvature identity together with local
  spectral information away from zero;
- an assembled primitive-pair or divisor-wavelet bound for the shape
  defect before taking absolute values;
- a function-field port that identifies which Frobenius constituent
  carries the defect.

Do not spend another pass optimizing an arbitrary compact carrier norm:
the parabolic solution and the \(L^{3/2}\) information barrier are sharp.

### B. Low-frequency beta interferometry

Work directly with

\[
 |t|\le \exp\!\left(\sqrt{(\log2)(\log X)}\right).
\]

Preserve the complete exceptional factor, common-factor state, divisor
orientations, and signed \(t\)-integral. Compare:

- a bilateral Perron/hyperbola decomposition which retains the notch;
- a reflection/differential identity before the max cusp;
- short multiplicative-interval mean values for the complete beta
  Dirichlet polynomial.

The goal is not a channelwise negative-moment estimate. It is one assembled
signed theorem at the \(X^{o(1)}\) scale.

### C. Frobenius-residue inverse design

Use the all-curve formula to solve for small virtual combinations which
annihilate specified axis residues or repeated-root channels. Then add one
owner/Boolean restriction and identify exactly which inverse-zeta zeros and
Frobenius terms survive. This could generate a genuine family moment theorem
rather than another complete-family toy.

### D. Relative-correspondence Adams theory

Keep the centered diagonal and Artin--Schreier graphs as correspondences.
Attempt closed-point inversion after the selected/unselected difference is
formed, rather than externalizing each term. A clean failure would be a new
categorical no-go; success would reopen the sheaf amplifier without paying
rank \(q^a\).

## 9. Verification and computation boundary

At the continuation head:

- all 62 changed bounded producers pass normally and under optimized
  Python;
- all 622 tests in the 61 changed focused modules pass in both modes;
- Ruff lint and format pass on all 123 changed Python files;
- all 67 changed Markdown files are free of forbidden control bytes;
- the two front-door documents have resolving local links and balanced
  math/fence delimiters;
- the working diff passes the Git whitespace check.

The sweep is broad but light. The original largest exact matrix has
dimension 24; the original function-field recurrence uses bidegree at
most 35 for \(q=3,5,7\). The newest moving-support packet evaluates no
beta sum, prime, zeta zero, curve, point, polynomial, conductor family,
or \(L\)-function. Its replay is closed-form arithmetic on four
variance rows and five support exponents.
