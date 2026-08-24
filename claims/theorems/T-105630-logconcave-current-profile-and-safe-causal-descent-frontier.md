# T-105630 — Xi log-concavity pays the complete safe-region current–phase contraction

Claim ID: `T-105630`  
Status: **MAJOR UNCONDITIONAL SOURCE/SAFE-REGION ADVANCE; DESCENT BELOW THE EXTREMAL HEIGHT OPEN**  
Created: 2026-08-25  
Depends on: `T-105620`; `L-105624--L-105630`; `R-105620`  
RH status: **unproved**

## 1. The actual current is the all-order exterior-square source

For the standard positive even Xi Fourier kernel,

\[
\widehat J_H
=
\sum_{k\ge0}{H^{2k+1}\over(2k+1)!}\Lambda_{2k+2},
\qquad
\Lambda_{2k+2}\ge0,
\]

and

\[
\Lambda_2=\widehat{\Xi'^2-\Xi\Xi''}.
\]

Thus the actual denominator current and actual Turan numerator are not two
sources which need to be compared by an unknown Gram theorem. The numerator is
the first member of the complete positive current hierarchy.

At total height `H`,

\[
\widehat J_H\ge H\Lambda_2+{H^3\over6}\Lambda_4.
\tag{T-105630.1}
\]

The upper and reflected causal orientations satisfy the corresponding weighted
source contractions of `L-105621--L-105622`.

## 2. The standard Xi kernel is strictly log-concave

`L-105626` proves directly from the classical theta series that

\[
\boxed{(\log\Phi)''(u)<0\qquad(u\in\mathbb R).}
\tag{T-105630.2}
\]

The proof uses the exact positive-mixture identity

\[
(\log\Phi)''=\mathbb E b_n+\operatorname{Var}(a_n)
\]

and a uniform elementary tail bound whose final rational margin is

\[
{1881\over7000}<1.
\]

No assertion that ordinary log-concavity implies RH is used or valid.

## 3. Log-concavity makes the physical source profile monotone

For every total height `H>0`, define

\[
\boxed{
R_H(\xi)
={H e^{-H\xi}\Lambda_2(\xi)\over\widehat J_H(\xi)},
\qquad \xi\ge0.
}
\tag{T-105630.3}
\]

The exterior-square conditional law and its quantile flow give

\[
\boxed{R_H\text{ nonincreasing on }[0,\infty).}
\tag{T-105630.4}
\]

For a base `b` and microscope scale `h`, the actual profile is

\[
\boxed{
r_{b,h}={h\over b+h}R_{b+h}.}
\tag{T-105630.5}
\]

Hence it is also nonincreasing. The distinction between total height `b+h`
and physical scale `h` is load bearing.

## 4. Safe-height derivative phases are inner and causal

If

\[
H\ge\beta_1,
\]

where `beta_1` is the highest imaginary part of a zero of `Xi'`, then

\[
U_H(x)
={\Xi'(x-iH)\over\Xi'(x+iH)}
\]

is the boundary value of an inner function. The proof uses the shifted
Cartwright product and the positive Xi Laplace moments to orient its exponential
factor.

Under Paley--Wiener, multiplication by `U_H` is a causal isometry. Every
nonincreasing diagonal source weight therefore contracts:

\[
V_H^*M_rV_H\preceq M_r.
\tag{T-105630.6}
\]

In particular, for every safe base

\[
b\ge\beta_0
\]

and every `h>0`, `H=b+h` lies above `beta_1`, so

\[
\boxed{
V_H^*M_{r_{b,h}}V_H
\preceq M_{r_{b,h}}.
}
\tag{T-105630.7}
\]

This is an unconditional contraction of the actual base-Xi current/Turan
source by the actual Xi-prime all-pass throughout the complete zero-free safe
region.

## 5. The source-owned finite bank is canonical

For an inner all-pass `U`, the Hankel operator `H_(bar U)` is a partial
isometry whose initial space is exactly

\[
K_U=H^2\ominus UH^2.
\]

For finite Blaschke `U`,

\[
\dim K_U=\deg U.
\]

Every source-owned finite section of this model bank inherits
(T-105630.7) exactly after current-Gram whitening. Therefore finite source
cutoffs, source tapers, source bases and source Gram normalization do not
create a new phase-collision debt.

The physical finite-rectangle count still requires its argument-principle
endpoint and common-zero ledger; model-space degree is not silently identified
with a parent Xi rectangle count.

## 6. The raw shell-energy gate is overstrong

For the completely real-rooted family

\[
p_N(z)=z^N
\]

and heights `h_2=2h_1`, every positive-height shell is empty on every rung, but
each adjacent shell all-pass has

\[
\mathcal E_+=\mathcal E_-={1\over9}.
\]

Across nineteen rungs,

\[
\sum\mathcal E_-={19\over9}>2
\]

although the signed winding is zero. Thus `HSHE105602<2` remains a valid
sufficient condition but is not a natural real-rootedness invariant. The
balanced positive Hardy compensation must be retained.

## 7. Exact remaining gates

The safe-region theorem does not descend itself below the unknown `beta_0`.
At a lower base, small total heights can encounter zeros of `Xi'`, destroying
the inner/causal geometry; even before that happens, an energy contraction is
not automatically the pointwise differential-microscope inequality.

The remaining conclusion-facing gates are:

```text
SAFEDESC105628
  continue the source/phase control below beta_0 without a denominator pole
  or positive zero-height charge;

ENDIDX105630
  for integrated/proportion routes, identify cofinal finite model-space degree
  with the precise Xi zero-count index and one endpoint ledger;

POINTID105630
  promote the source-owned weighted contraction to the physical pointwise
  differential microscope, retaining the two-trace evaluation map.
```

Any proof of `POINTID105630 AND SAFEDESC105628` yields

\[
\mathcal C_{0,b}(a,h)\le0
\qquad(0\le b\le1/2),
\]

and the zero-height variational theorem then gives RH.

## 8. Exact status

```text
current = all-order exterior-square hierarchy          PROVED EXACT
actual Turan = first current chaos                      PROVED EXACT
standard Xi kernel strict log-concavity                 PROVED / REVIEW
current-normalized source profile monotonicity          PROVED / REVIEW
safe-height Xi-prime all-pass innerness                 PROVED / REVIEW
safe-region causal weighted contraction                PROVED / REVIEW
source-owned model-space bank                           PROVED EXACT
raw negative shell-energy naturality                    REFUTED
POINTID105630 physical point evaluation                 OPEN / RH-BEARING
SAFEDESC105628 descent below beta_0                     OPEN / RH-BEARING
ENDIDX105630 finite endpoint/index ledger               OPEN
Riemann Hypothesis                                      UNPROVEN
```

## 9. Scope

This theorem gives a substantial unconditional safe-region structure but does
not prove RH. Log-concavity is only a second-order source property; causal
weighted energy is not pointwise positivity; and an inner all-pass exists only
above its denominator zeros. Those distinctions are binding.
