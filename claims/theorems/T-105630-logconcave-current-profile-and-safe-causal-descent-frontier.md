# T-105630 — Xi log-concavity pays the current–phase contraction down to the adjacent derivative height

Claim ID: `T-105630`  
Status: **MAJOR UNCONDITIONAL SOURCE/ONE-RUNG ADVANCE; ZERO-HEIGHT DESCENT AND POINTWISE IDENTIFICATION OPEN**  
Created: 2026-08-25  
Depends on: `T-105620`; `L-105624--L-105632`; `R-105620`; `R-105630`  
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

## 4. The actual phase contracts down to beta_1

Let

\[
\beta_j=\sup\{\Im z:\Xi^{(j)}(z)=0\},
\qquad \beta_1\le\beta_0.
\]

If

\[
H>\beta_1,
\]

then

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

For **every base `b>=beta_1`** and every `h>0`, the total height
`H=b+h` exceeds `beta_1`. Hence

\[
\boxed{
V_H^*M_{r_{b,h}}V_H
\preceq M_{r_{b,h}}.
}
\tag{T-105630.7}
\]

This is an unconditional contraction of the actual base-Xi current/Turan
source by the actual Xi-prime all-pass down to the adjacent derivative's
extremal height. The entire source-energy interval `[beta_1,beta_0]` is paid
without assuming that the Xi numerator is zero-free there.

## 5. The source-owned finite bank and signed tail are canonical

For an inner all-pass `U`, the Hankel operator `H_(bar U)` is a partial
isometry whose initial space is exactly

\[
K_U=H^2\ominus UH^2.
\]

For finite Blaschke `U`,

\[
\dim K_U=\deg U.
\]

Every source-owned finite section inherits (T-105630.7) exactly after current-
Gram whitening. Finite source cutoffs, source tapers, source bases and source
Gram normalization therefore create no new phase-collision debt.

Moreover, for every source projection `P`, innerness gives

\[
\boxed{
\Delta_P(U)
=-\|H_{\overline U}P^\perp\|_{\mathcal S_2}^2
\le0.
}
\tag{T-105630.8}
\]

Thus the positive part of the signed Paley--Wiener complement is identically
zero whenever the total height exceeds `beta_1`. Absolute model-space coverage
is unnecessary there. A positive signed tail can first appear only when an
anti-inner Xi-prime denominator factor enters below that threshold.

Finite model-space trace formulas are exact after finite/source regularization.
The continuum multiplication weight is not trace class; no difference of two
infinite traces is silently taken. The cofinal endpoint carrier remains in the
argument-principle ledger.

## 6. Two binding firewalls

### Raw shell energy

For `p_N(z)=z^N` and `h_2=2h_1`, every positive-height shell is empty on every
rung, but each adjacent shell all-pass has

\[
\mathcal E_+=\mathcal E_-={1\over9}.
\]

Across nineteen rungs the raw negative energy is `19/9>2` although the signed
winding is zero. `HSHE105602<2` is therefore a valid but overstrong sufficient
condition; the balanced positive Hardy compensation must be retained.

### Pointwise evaluation

`R-105630` gives a two-frequency decreasing source profile and a perfectly
inner unilateral shift for which the full weighted contraction holds but the
corresponding off-diagonal physical trigonometric evaluation has the wrong
sign. Hence causal energy does not itself imply the differential microscope.
`POINTID105630` is a genuine Xi-specific interface.

## 7. Exact remaining gates

The source-energy descent is now complete to `beta_1`, not merely to
`beta_0`. Below `beta_1`, small total heights can encounter zeros of `Xi'`,
destroying the inner/causal geometry. Independently, an energy contraction is
not automatically the pointwise differential-microscope inequality.

```text
SAFEDESC105628
  continue below beta_1 without an anti-inner Xi-prime factor, denominator
  pole, or positive zero-height charge;

POINTID105630
  promote the source-owned weighted contraction to the physical pointwise
  differential microscope, retaining the actual two-trace evaluation;

ENDIDX105630
  for integrated/proportion routes, identify cofinal model-space degree with
  the precise Xi zero-count index and one endpoint/common-zero ledger.
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
Xi-prime all-pass innerness for H>beta_1                PROVED / REVIEW
source-energy phase descent to b=beta_1                 PROVED / REVIEW
source-owned model-space bank                           PROVED EXACT
positive signed complement above beta_1                 EXCLUDED
raw negative shell-energy naturality                    REFUTED
causal energy -> pointwise sign shortcut                REFUTED
POINTID105630 physical point evaluation                 OPEN / RH-BEARING
SAFEDESC105628 descent below beta_1                     OPEN / RH-BEARING
ENDIDX105630 finite endpoint/index ledger               OPEN
Riemann Hypothesis                                      UNPROVEN
```

## 9. Scope

This theorem gives a genuine one-rung source-energy descent but does not prove
RH. Log-concavity is only a second-order source property; causal weighted
energy is not pointwise positivity; and the inner all-pass can fail when the
total height crosses a zero of `Xi'`. Those distinctions are binding.
