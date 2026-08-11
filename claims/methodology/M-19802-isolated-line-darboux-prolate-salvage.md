# M-19802 — Isolated-line/Darboux prolate salvage

Claim ID: `M-19802`  
Title: Replace RH-bearing ground selection by prime-side spectral isolation and a finite real-zero Darboux bridge  
Status: **PROPOSED — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Dependencies retained: `T-14301`, `L-14302`, `L-14303`, `L-14304--L-14306`, exact CCM matrix assembly, finite Schur/LDL infrastructure  
Scope: salvage architecture after `R-21501`, `R-19846` and `R-19847`  
Nonclaim: RH is not proved

## 1. Motivation

The historical prolate resolution used two invalid or RH-bearing transfers:

1. its off-line support-average application failed the parent scaled-derivative
   hypothesis;
2. after that repair, complete ground-state coercivity would still exclude the
   even negative Xi-cardinal vector produced by any hypothetical off-line zero.

Therefore no improvement of high-frequency constants can by itself rescue the
complete ground-line proof.

The correct salvage is to separate two questions:

```text
Can the Xi-like line be isolated spectrally?
Can a suitable finite real-zero theorem be applied without requiring that line
be the bottom of the complete Weil spectrum?
```

The first is compatible with lower negative modes.  The second is the genuinely
new conceptual theorem.

## 2. Finite setup

Let `lambda>1`, let `N` be a finite Fourier cutoff and let

\[
 A_{\lambda,N}=QW_\lambda^N
\]

be the exact real symmetric CCM matrix in the audited centered convention.  Let

\[
 p_{\lambda,N}=P_Nk_\lambda
\]

be the projected CCM prolate target, or let `p_(lambda,N)` be the exactly
normalized Xi-radical projection supplied by a separately reviewed source
construction.

Let `M_(lambda,N)` be the positive Hardy metric in the chosen moving strip, and
put

\[
 \mu_{\lambda,N}
 ={\langle A_{\lambda,N}p_{\lambda,N},p_{\lambda,N}\rangle
   \over\|p_{\lambda,N}\|^2},
\]

\[
 r_{\lambda,N}
 =P_{p^\perp}(A_{\lambda,N}-\mu_{\lambda,N}I)p_{\lambda,N}.
\]

The finite producer must use only prime, pole and archimedean data.  Zeta zeros
may be used for validation or falsification but not to construct the matrix or
the certificate.

## 3. Prime-side isolated-line gate

The primary finite target is the two-sided estimate

\[
 \boxed{
 \|(A_{\lambda,N}-\sigma_{\lambda,N}I)w\|_{M^{-1}}
 \ge g_{\lambda,N}\|w\|_M,
 \qquad w\perp p_{\lambda,N},
 }
\tag{M-19802.1}
\]

combined with

\[
 \boxed{
 \|(A_{\lambda,N}-\sigma_{\lambda,N}I)p_{\lambda,N}\|_{M^{-1}}
 \le b_{\lambda,N},
 \qquad {b_{\lambda,N}\over g_{\lambda,N}}\to0.
 }
\tag{M-19802.2}
\]

Unlike a one-sided lower floor, (M-19802.1) allows eigenvalues below
`sigma_(lambda,N)`.  It is therefore not contradicted merely by the off-line
Xi-cardinal direction in `R-19846`.

Standard a posteriori spectral theory then yields a unique simple eigenline
`xi_(lambda,N)` near `p_(lambda,N)` and

\[
 \inf_{c\ne0}
 \|c\xi_{\lambda,N}-p_{\lambda,N}\|_M
 \ll {b_{\lambda,N}\over g_{\lambda,N}}.
\tag{M-19802.3}
\]

Parity must be certified simultaneously.  An exact even target and parity-
commuting matrix imply that a unique nearby line is even, provided the odd
sector has the same exclusion moat around `sigma_(lambda,N)`.

## 4. Three-block producer

Use the orthogonal decomposition

\[
 H_N
 =\operatorname{span}\{p\}\oplus L\oplus H,
\]

where:

- `L` is a finite central block containing every constant, pole, endpoint,
  certified-zero and low boundary coordinate that cannot be treated as a tail;
- `H` is the exterior/high-frequency complement.

Write

\[
 A-\sigma I
 =\begin{pmatrix}
 a&r_L^*&r_H^*\\
 r_L&B&Z^*\\
 r_H&Z&C
 \end{pmatrix}.
\]

The producer should certify:

1. exact candidate-row bounds for `r_L,r_H`;
2. an absolute high-block gap
   \[
    C^*M_H^{-1}C\succeq g_H^2M_H;
   \]
3. an exact finite low-block singular-value moat after Schur correction;
4. the odd-sector analogue;
5. perturbation survival under all directed assembly radii.

Current square-support all-prime tail bounds are naturally useful for `r_H` and
`Z`.  Packet-leverage/bathtub estimates may supply a high-block floor.  The
anchor/Christoffel and interval-LDL machinery may certify `L`.

A one-sided claim `C\succeq hM_H` is optional; the load-bearing result is the
absolute exclusion moat around `sigma`.

## 5. Required finite real-zero bridge

Spectral isolation alone does not imply that the Fourier--Mellin transform of
`xi_(lambda,N)` has only real zeros.  One of the following must be proved.

### 5.1 Non-ground CCM real-zero theorem

Prove, for the exact finite CCM matrix and rank-one perturbation, that a
specified simple isolated even eigenline has a real-zero transform under
explicit finite hypotheses not requiring it to be the lowest line.

The proof must expose the precise replacement for the ground-state variational
step in the existing CCM theorem.  Abstract self-adjointness is not sufficient.

### 5.2 Darboux/Christoffel groundification

Construct an exact finite modification `A -> A^D` and transform
`xi -> xi^D` such that:

1. `xi^D` is the simple even ground line of an allowed CCM/Caratheodory--Fejer
   object;
2. `hat(xi^D)=P_N(z)hat(xi)(z)` with `P_N` explicitly real-rooted and
   nonvanishing on every nonreal compact under consideration;
3. every lower finite line is removed or lifted by a source-bound operation;
4. normalization and determinant convergence are uniform in the moving strip.

The positive-anchor/Christoffel and corrected Darboux/Fredholm stacks are the
natural finite algebra for this task, but no existing claim proves all four
properties.

## 6. Moving-Hardy closure

Let `tau_j -> 1/2`, `lambda_j -> infinity` and choose `N_j` beyond the explicit
weighted projection-tail threshold.  The final quantitative target is

\[
 \boxed{
 \|(I-P_{N_j})k_{\lambda_j}\|_{\lambda_j,\tau_j}
 +{b_{\lambda_j,N_j}\over g_{\lambda_j,N_j}}
 \longrightarrow0.
 }
\tag{M-19802.4}
\]

If Section 5 supplies finite real-zero transforms, (M-19802.4), the audited CCM
prolate limit and Hurwitz give RH.

## 7. Why this architecture uses later repository work correctly

- `R-21501/L-21503` are not needed if the matrix is assembled directly from the
  prime side; no actual-zero selector is compared with a line-centered model.
- `R-19846` is respected: negative cardinal modes may lie below the target.
- `L-19862` is reinterpreted as a source of an isolated target/residual geometry,
  not a ground-state floor.
- Current PR #202 tail estimates are used for finite row/cross errors, not to
  assert positivity of the RH-equivalent constant coordinate.
- `T-14301` is retained only after a new finite real-zero bridge has been proved.

## 8. Binary falsifiers

The proposal fails if any of the following is proved:

1. a finite CCM example with a well-isolated simple even interior eigenline whose
   transform necessarily has a nonreal zero, ruling out Section 5.1 in the
   required class;
2. a proof that every admissible Darboux groundification introduces a pole or
   nonreal zero factor incompatible with Hurwitz;
3. a prime-side model in which the Xi target is never isolated from the complete
   finite spectrum on any cofinal sequence;
4. a directed lower bound showing `b/g` remains bounded away from zero.

## 9. Exact remaining deliverables

1. source-bound prime-side interval matrices at several growing supports;
2. reconnaissance tables for the two-sided target singular gap, not the ground
   gap;
3. one theorem proving the asymptotic isolation moat;
4. one theorem of type 5.1 or 5.2;
5. a final moving-Hardy directed ledger.

Until items 3 and 4 are proved, this remains a serious research proposal rather
than a proof of RH.
