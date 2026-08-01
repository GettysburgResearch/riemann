# M-15603 — Production export of the actual profile-soft packet

Claim ID: `M-15603`  
Title: Directed spectral export, joint prime/polar/archimedean assembly and direct harmonic short for `P_R^soft`  
Status: `PRODUCTION PROTOCOL`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15631`; `L-15632`; `T-15606`; `L-18512`

## Objective

For each dyadic radial block, emit one exact support and one exact finite packet
whose fully shorted normalized negative part is bounded by the cofinal endpoint
in `T-15606.6`.

The workflow must not choose the soft packet before the support-average step.
The complete regularized frame is used while support varies.  The exact soft
spectral projection is exported only after a good support has been selected.

## Stage A — complete joint source/profile producer

For every candidate support `R`, emit:

```text
exact low basis U_R and metric G_R;
finite harmonic/form-core basis E_R;
exact source synthesis F_R and check L_R F_R = I;
complete joint branch amplitudes and support derivatives;
actual joint profile Gram mathcal_D_R;
regularized Gram Dhat_R;
complete prime-power manifest;
polar and archimedean matrices;
endpoint, Airy and Poisson ledgers;
harmonic cross Z_R and ambient block C_R.
```

The producer must form the complete prime/polar/archimedean matrix before taking
operator norms.  The exact terminal-prime/polar cancellation must occur inside
the matrix.

## Stage B — positive-measure support selection

On a dyadic block `[T,2T]`, use the branch envelopes to certify

\[
 \mathfrak B_T=o(\sqrt{T/\log T})
\]

and apply the support-average ledger simultaneously to:

```text
line-centered cross branches;
reflected off-line cross branches;
finite endpoint phase families;
Airy and alias families;
all joint low/harmonic graph channels.
```

The output is a nonempty directed support interval or a positive-measure support
set on which

\[
 -\varepsilon_R\log R\,\widehat{\mathcal D}_R
 \preceq
 \mathcal H_R-(\log R)\mathcal D_R
 \preceq
 \varepsilon_R\log R\,\widehat{\mathcal D}_R.
\]

A named decimal support is optional; an exact dyadic subinterval with a common
LMI is preferable.

## Stage C — exact soft spectral export

After support selection:

1. form the directed generalized spectrum of `(D_R,G_R)`;
2. search `[tau_R,2 tau_R]` for a certified empty interval;
3. freeze its midpoint `vartheta_R`;
4. enclose the Riesz projector
   \[
   P_R^{soft}=1_{[0,vartheta_R]}(G_R^{-1/2}D_RG_R^{-1/2});
   \]
5. freeze a dyadic/rational basis `Q_soft` and prove that its image equals the
   exact spectral range;
6. emit the compressed metric and profile LMIs
   \[
   Q_{soft}^*D_RQ_{soft}
   \preceq2\tau_RQ_{soft}^*G_RQ_{soft}.
   \]

The spectral gap is at least `tau_R/[2(dim U_R+1)]` after the adaptive threshold
choice, so arbitrary precision eventually exports the exact range.

## Stage D — joint direct short

Compress all exact matrices to `Q_soft`.  Put

\[
 X_0=D_E^{-1}Y_{E,soft}.
\]

Emit:

```text
main-profile trial lift J_X0;
actual harmonic residual R_X0=Z-C X0;
trial-lift complete Weil matrix;
residual penalty using exact C^-1 or a coercive directed lower metric;
fully shorted matrix S_soft;
normalized shifted LDL for
S_soft + delta_R G_soft.
```

The declared endpoint is

\[
 \delta_R
 =4(\varepsilon_R+4\varepsilon_R^2)
  (\log R)\tau_R.
\]

The level passes only when directed arithmetic proves

\[
 \mathscr S_R^{soft}+\delta_RG_{S,R}\succeq0.
\]

## Stage E — precision and independence

Every retained level requires:

```text
at least two nested directed precisions;
independent prime-side and zero-side matrix assembly;
complete source, manifest and producer hashes;
mutation of one prime-power row;
mutation of the polar sign;
mutation of one archimedean interval;
mutation of the soft threshold;
mutation of the harmonic residual;
mutation of the joint LMI endpoint.
```

The exact consumer should use rational interval endpoints and reconstruct every
compression and Schur operation independently of the producer.

## Integration with PR #191

The direct-block emitter in PR #191 already produces

```text
Q_W,P_W,E_W,Z_W,C,X_N,R_N,G_W
```

and has one actual certified positive level plus a growing finite ladder.
The minimal extension is to add

```text
joint profile Gram;
regularized Gram;
soft threshold/gap;
soft basis;
relative joint remainder LMI;
main-profile solve.
```

No change to the direct-short consumer or prime/archimedean normalization is
required.

## Failure classification

A failed level must report which gate failed:

```text
SOURCE_IDENTITY_FAIL
PROFILE_GRAM_FAIL
REGULARIZED_ENVELOPE_FAIL
SUPPORT_MEASURE_EMPTY
SOFT_GAP_UNRESOLVED
JOINT_REMAINDER_LMI_FAIL
AMBIENT_BLOCK_FAIL
DIRECT_SHORT_NEGATIVE_UNRESOLVED
```

A finite failure is not evidence against RH.  A stable strict negative interval
in the fully assembled exact matrix is a genuine low-block research candidate
and must be preserved.
