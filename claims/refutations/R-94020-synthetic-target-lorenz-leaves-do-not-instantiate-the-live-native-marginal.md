# R-94020 — Synthetic Target–Lorenz leaves do not instantiate the live native marginal

Claim ID: `R-94020`
Status: **PROVED EXACT INTERFACE REFUTATION / SCOPE CORRECTION**
Created: 2026-08-16
Frozen base: PR #508 at `4ae97dffd1f76ed3244b8f3028560ffa80663caf`
Inputs: review #504; `L-91107`, `L-91362`; PRs #507, #509, #512, #514
RH status: **unproved**

PR #508's directed tail and typed terminal-leaf algebra are retained.  What is
refuted is the inference

```text
one or more valid terminal Target-Lorenz fixtures
        =>
the actual endpoint/native source has been compiled into those leaves.
```

## 1. The actual finite endpoint atom is not the paired SHARP atom

For integer `X`, endpoint cell `m`, and squarefree colour `k<=X/m`, the literal
finite endpoint-divergence coefficient is

\[
 a_{X;m,k}
 =\frac{\mu(k)}{\sqrt{mk}}\log\frac{X}{mk}.
\tag{R-94020.1}
\]

The paired equality and SHARP source coefficients at root parameter `x=X/m`
are instead

\[
 E_x(k)=\frac1{\sqrt k}\left(2\sqrt{x/k}-1\right),
\qquad
 T_x(k)=\frac1{\sqrt k}\left(4\sqrt{x/k}-3\right).
\tag{R-94020.2}
\]

At the exact live occurrence

\[
 X=536,
 \qquad m=8,
 \qquad k=67,
 \qquad x=67,
\]

one has

\[
 a_{536;8,67}=0,
 \qquad
 E_{67}(67)=T_{67}(67)=\frac1{\sqrt{67}}>0.
\tag{R-94020.3}
\]

Hence no atomwise coefficient-preserving identification of the finite anchored
occurrence with either paired source atom exists.  A correct proof must retain
the signed finite/continuum comparison or exhibit a genuinely aggregate
coupling; it may not silently rename the occurrence.

## 2. Actual stopping-line children cannot be positive branches

The exact paired stopping line has

\[
 \Sigma F_{61,X}=N_X+\mathcal R_X,
 \qquad
 \Sigma P_X^{\rm child}=-\mathcal R_X.
\tag{R-94020.4}
\]

For `X>134`, the `m=67` rough term at ordinary column `q=2` gives

\[
 C_{\mathcal R_X}(2)
 \ge\frac1{\sqrt{134}}
       \log\frac X{134}>0.
\tag{R-94020.5}
\]

Thus

\[
 C_{\rm child}(2)<0.
\tag{R-94020.6}
\]

At `X=536`, the corresponding ordinary and radix-four child coordinates are at
most

\[
 -\frac{
   \log4
 }{\sqrt{134}}
 <-\frac19,
\tag{R-94020.7}
\]

using `log 2>2/3` and `sqrt(134)<12`.

A separately nonnegative physical row has nonnegative ordinary response, so no
branchwise positive realization of the actual oriented child block can
preserve the native marginal.  Finite forcing and oriented children must be
coupled jointly before entry into the positive physical-row cone.

## 3. Consequences for the live lineages

The following pieces survive:

```text
PR #508 directed tail and typed (nu,B,sigma) leaf algebra;
PR #507 native-source-tree versus rough-lift distinction;
PR #509 exact anchored/Volterra hybrid marginal and owner labels;
PR #511 exact two-channel identities T=E+2R and S=2E+R;
PR #513 direct positive outer Volterra bulk;
PR #514 exact negative-coordinate obstruction and joint-cancellation gate.
```

The following inferences do not survive without a new joint compiler:

```text
a finite anchored log occurrence is already a SHARP atom;
a single hostile leaf is a generator for the complete root;
actual oriented children can be placed as separate nonnegative rows;
synthetic owner fixtures establish the live endpoint marginal;
the anchored sector is positive merely by citing the terminal AVLT;
a positive physical row may be assigned to an actual oriented child.
```

This refutation does not disprove the complete Target–Lorenz arithmetic theorem.
It identifies the exact source-to-physical interface still missing after review
#504.
