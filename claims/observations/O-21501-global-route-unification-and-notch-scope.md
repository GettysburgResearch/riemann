# O-21501 — Global-route unification and infinite-notch scope correction

Claim ID: `O-21501`  
Title: The square-screw, prime-energy, notch, Hausdorff, and prime-polygon routes are coordinates of one spectral obstruction  
Status: `PROPOSED INTEGRATION/AUDIT OBSERVATION`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Scope: current integrated main, reverted full-problem drafts `351c444/78eec31`, draft PR #217, and draft PR #219

## 1. Four global observables, one rightmost-zero exponent

The repository now contains four genuinely global scalar architectures:

1. **Square screw:** the negative-growth exponent of one finite prime-power cutoff sequence is `Theta_zeta`.
2. **Phase-complete prime energy:** the local `L2` growth exponent of one pole-free finite prime-window signal is `Theta_zeta`.
3. **Centered notch residual:** after annihilating critical-line frequencies, every remaining off-line mode retains exponent `Theta_zeta`.
4. **Prime polygon:** the positive vertex-deficit exponent of the finite prime-power moment polygon is `Theta_zeta`.

These are not four independent routes around the hard theorem. They are one-sided value, positive energy, spectrally filtered, and convex-dual coordinates of the same signed spectral charge.

The practical distinction is the proof object:

```text
square screw:
  finite prime prefix, but sparse sign excursions;

prime energy:
  positive finite prime-pair form, but a global subexponential bound is open;

centered notch:
  perfect line-spectrum removal, but the kernel uses the complete critical-line zero set;

prime polygon:
  finite prime prefix and complete negative semidecision with no zero input;
  positive route is a cumulative quantile-transport theorem.
```

## 2. What the phase-energy theorem contributes

Reverted draft commit `351c4445a2f6a3c02c33d022fe48dbe0c267aa4c` proposed the exact identity

\[
\Theta_\zeta
=
\limsup_{X\to\infty}
{\log(1+\int_X^{X+1}|Q_h(x)|^2dx)\over2X}
\tag{O-21501.1}
\]

for one compact pole-free triangular prime window. Subject to independent review of its explicit-formula continuation, this is a useful phase-complete positive target. It does not prove the required prime-only estimate

\[
\int_X^{X+1}|Q_h(x)|^2dx=e^{o(X)}.
\]

Thus it removes sparse phase cancellation as an excuse, but not the RH-strength arithmetic growth theorem.

## 3. Finite and infinite notches

Reverted draft commit `78eec318f654f2b14ec39279c57982320e342367` proposed finite critical-line notch exhaustion. Draft PR #217 centers that cascade and constructs the entire product

\[
P_\infty(z)
=
\prod_k{\sinh(\pi z/\gamma_k)\over\pi z/\gamma_k}.
\tag{O-21501.2}
\]

The square-summability of `1/gamma_k` makes the centered random convolution plausible and useful: its transform vanishes at all critical-line frequencies and nowhere off the imaginary axis. This is a canonical spectral projector onto the off-line residual.

Its positive endpoint remains exactly the arithmetic identity that the corrected prime residual vanishes. Since the kernel itself is built from the complete list of critical-line ordinates, this is a classification and annihilation theorem rather than a zero-free finite prime proof.

## 4. Required correction to `T-21701.19`

Draft PR #217 defines

\[
R_\infty=Q_\infty-E_\infty^{\rm known}
\tag{O-21501.3}
\]

and then writes

\[
\mathcal L R_\infty(z)
=-\widehat G_{\infty,L}(z)
 {\zeta'\over\zeta}(z+1/2).
\tag{O-21501.4}
\]

As written, this omits the transform of the subtracted known term. It is also incompatible with the preceding RH implication: under RH the draft proves `R_infty=0`, while the right side of (O-21501.4) is not identically zero in its initial half-plane.

The repair is straightforward but load bearing. One must write either

\[
\boxed{
\mathcal L R_\infty(z)
=-\widehat G_{\infty,L}(z)
 {\zeta'\over\zeta}(z+1/2)
-\mathcal L E_\infty^{\rm known}(z),}
\tag{O-21501.5}

or define an explicitly renormalized meromorphic transform in which the pole, trivial-zero, endpoint, and initial terms have already been removed. The correction term must be shown holomorphic in the open shifted critical strip. Then any off-line zeta pole remains visible because `Ghat_infty` is nonzero there, and the intended converse can still be proved.

This correction does not refute the centered-notch construction; it prevents the raw and corrected Laplace identities from being conflated.

## 5. Hausdorff saddle sector

`L-21701` proposes an unconditional fixed-row asymptotic

\[
\mathcal H_{m,k}(R)>0
\qquad(k\to\infty,\ m\text{ fixed}).
\tag{O-21501.6}
\]

Unlike another equivalence, this would close a genuine infinite sector of the complete Hausdorff hierarchy. The proposed uniform extension `m/sqrt(k)->0` and the moving transition strip remain open. Even if the fixed-row proof passes review, it does not cover the diagonal regime carrying the full RH content.

The Hausdorff and polygon routes should therefore exchange estimates:

- the beta saddle identifies where spectral mass concentrates in inverse-moment coordinates;
- the polygon quantile recurrence identifies the exact cumulative barycentric surplus required in prime-prefix coordinates.

A successful uniform saddle estimate may suggest block sizes for `L-21502.11`, but fixed-row positivity alone cannot imply polygon domination.

## 6. Full attack selected

The strongest combined programme is now:

1. use the prime polygon for finite negative semidecision and the exact positive barrier;
2. use phase-complete energy to forbid reliance on favorable scalar phases;
3. use finite/centered notches to isolate the off-line spectral component;
4. use Hausdorff saddle asymptotics to prove genuine positive sectors;
5. translate any new uniform sector into a block quantile transport or finite-Euler curvature inequality.

The missing theorem remains arithmetic and global:

\[
B_j-F^*(A_j)\ge0
\quad\text{cofinally},
\]

or an equivalent phase-energy/notch/Hausdorff statement proved from the prime side without assuming the zero geometry it is meant to establish.

## 7. Status boundary

- The global-route connection is proposed pending independent review.
- The correction in Section 4 is an algebraic scope correction, not a verdict on all of PR #217.
- The phase-energy and notch drafts do not prove RH.
- The Hausdorff fixed-row asymptotic is not independently verified here.
- No RH resolution or counterexample is claimed.
