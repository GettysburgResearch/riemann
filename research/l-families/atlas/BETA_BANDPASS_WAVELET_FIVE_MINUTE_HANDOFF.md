# Beta band-pass and curve-wavelet successor: five-minute handoff

Status: **eight exact theorem packets and two sharp no-go results; RH and
GRH remain open**

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

Read this file once, then choose exactly one lane:

1. **Direct beta/RH lane:** read
   [FFPS_INFINITE_DYADIC_BOX_BANDPASS_SMOOTHER.md](function_field/FFPS_INFINITE_DYADIC_BOX_BANDPASS_SMOOTHER.md),
   then
   [FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md](function_field/FFPS_BANDPASS_ASSEMBLED_PERRON_LEAKAGE.md).
   The live target is the signed beta energy inside the critical window
   \(e^{\sqrt{(\log2)(\log X)}}\), or the equivalent bilateral contour
   problem. The exterior frequency range is already harmless at the
   \(X^{o(1)}\) scale.
2. **Function-field lane:** read
   [FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md](function_field/FUNCTION_FIELD_BASEWAVE_CURVE_EXTENSION.md).
   The live target is an incomplete/source-faithful family, or an
   inverse-designed observable which cancels selected Frobenius residue
   channels.
3. **Sheaf/Adams lane:** read
   [FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md](function_field/FFPS_NATIVE_PARTIAL_FROBENIUS_VERDICT.md).
   Do not try another termwise bounded-rank externalization of the universal
   phase block. Classify actual source occupancy, build the signed relative
   complex, or develop a correspondence-level closed-point formula.

Do not begin with finite scouts. Do not infer a number-field estimate from a
complete function-field identity. Do not call any open energy gate proved.

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

## 6. The native sheaf does not pass termwise Adams compression

For \(m\) distinct physical residue cells in a field of size \(Q\), the
nonzero native Artin--Schreier Fourier block has Gram

\[
 QI_m-J_m
\]

and rank

\[
 \operatorname {rank}(QI_m-J_m)=
 \begin{cases}m,&m<Q,\\Q-1,&m=Q.\end{cases}
\]

Since \(Q=q^a\), a source-independent presentation on a full physical
degree-\(a\) sector has exponential rank in \(a\). Wick centering gives
\(I_m-Q^{-1}J_m=Q^{-1}(QI_m-J_m)\), so it retains the same rank.
Geometrically, the natural line \(\mathcal L_\psi(hx)\) fails each
independent partial Frobenius, and
partial Frobenius moves the diagonal \(x=y\) to \(x^Q=y\).

Therefore the clean rank-\(48\) ternary Adams compression cannot simply be
tensored termwise with the universal native phase/incidence kernel.

This is not a no-go for:

- a sparse actual source image;
- cancellation inside a complete signed relative complex before
  externalization;
- a correspondence-level closed-point formula which retains diagonal
  graphs.

The actual occupancy theorem and full relative complex remain unbuilt.

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
| termwise bounded-rank native Adams adapter | **REFUTED ON THE UNIVERSAL PHASE/INCIDENCE BLOCK** |
| beta energy inside the critical frequency window | **OPEN; RH-EQUIVALENT** |
| bilateral boundary-contour estimate | **OPEN; RH-STRENGTH** |
| incomplete/source-faithful function-field shadow | **OPEN** |
| actual native physical occupancy | **OPEN** |
| complete signed relative sheaf complex and uniform trace estimate | **OPEN** |
| CYSEL, WCADD, WCKUM, principal extraction, RH, or GRH | **NOT PROVED** |

## 8. Best next ambitious experiments

### A. Low-frequency beta interferometry

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

### B. Frobenius-residue inverse design

Use the all-curve formula to solve for small virtual combinations which
annihilate specified axis residues or repeated-root channels. Then add one
owner/Boolean restriction and identify exactly which inverse-zeta zeros and
Frobenius terms survive. This could generate a genuine family moment theorem
rather than another complete-family toy.

### C. Relative-correspondence Adams theory

Keep the centered diagonal and Artin--Schreier graphs as correspondences.
Attempt closed-point inversion after the selected/unselected difference is
formed, rather than externalizing each term. A clean failure would be a new
categorical no-go; success would reopen the sheaf amplifier without paying
rank \(q^a\).

## 9. Verification and computation boundary

The eight new packet producers and the amended rho-wavelet predecessor
producer pass normally and under optimized Python. Their nine relevant test
modules contain 78 tests, all passing in both modes. Ruff lint and format
checks pass on all seventeen changed producer/test Python files.

The largest exact matrix has dimension 24. The function-field recurrence
uses bidegree at most 35 for \(q=3,5,7\), without polynomial or point
enumeration. The all-curve extension is symbolic. No zeta zero, curve,
closed point, conductor family, or L-function is enumerated.
