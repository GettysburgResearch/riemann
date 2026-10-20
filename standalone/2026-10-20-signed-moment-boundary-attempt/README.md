# Attempt to lower the numerical quasi-Riemann boundary

Date: 20 October 2026.

**Status:** PROPOSED, source-dependent research components.

**Scope:** exact signed identities, a conditional marked inverse estimate,
and an unsuccessful attempt to improve the numerical boundary.

**Exact dependencies:** Liu's arXiv:2610.26835v1 and the preceding angular
packet at `7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0`; full pins appear below.

**What was run:** the isolated standard-library component checker and
resident-file replay described under Checks and review.

**Smallest remaining gap:** an estimate that preserves signed origin
cancellation while strictly decreasing the comparison width.

**Outcome: no smaller zero-free boundary is established in this packet.**
The benchmark remains Liu's

\[
B_\flat=0.874886647039964\ldots.
\]

The requested result was a strict numerical improvement, beyond the earlier
family extensions on this branch. This continuation attacked the direct
theta estimate, the correlated numerator, and a sixth-moment replacement.
It proves useful identities and a scoped marked inverse adapter, but the
estimate needed to turn them into a smaller boundary is still missing.
Neither a conditional consumer nor a passed finite check is being promoted
to a zero-free theorem.

## What this packet adds

| Component | Established scope | Limit relevant to the requested improvement |
|---|---|---|
| [Eight-point triple comparison](TRIPLE_COMPARISON.md) | An explicit signed comparison cancels the fixed-character main term and all one-error terms; a buffered integer rank makes its add-back comparison finite. | The second Poisson diagonal is a squared convolution coefficient, which this cancellation does not estimate. |
| [Signed second origin](SIGNED_SECOND_ORIGIN.md) | The full common Gauss phase and complete Möbius projector cancel every dangerous nonunit second origin; the original common character is restored exactly. | Applying both transforms with the signs intact returns the original width. |
| [Exact sixth-power graph](SIGNED_SIXTH_POWER_GRAPH.md) | Full Fourier inversion on the retained amplification graph includes all frequency aliases, also with the stated weighted prime averages. | The source's positive graph enlargement cannot simply be applied to the signed form. |
| [Marked inverse adapter](MARKED_INVERSE_TRANSFER.md) | All mixed subsets of a fixed product of prime-divisor marks are retained, conditional on the stated selected-moment and amplification inputs, with complete natural zeros. | Its bound at the native detector lengths does not improve the existing inverse exponent; the Eisenstein selected-moment bridge remains an additional hypothesis. |
| [Theta and moment audit](THETA_AND_SIXTH_MOMENT_AUDIT.md) | Identifies the actual squarefree theta block and tests the structured Gauss estimates at their full lengths. | The hardest direct block has cube index one and a remaining quadratic/cubic correlation. |

These are research components using the pinned analytic inputs below. They
are not integrated repository theorems. The source-dependent angular
extension from the preceding packet remains a proposed input where invoked.

## The sixth-moment calculation and its exact stopping point

For a row range of norm exponent \(M\), ordinary reflection gives three
plain lengths \(n_i\le M/2\), up to the explicitly buffered losses. Put
\(A=n_1+n_2+n_3\). The new comparison cancels the all-main term and every
term with exactly one fixed-character mean error. If \(s_2\) is the sum of
the two smallest lengths, the elementary optimization is

\[
\inf_{v\ge0}\left\{\frac{2v}{3}+(s_2-v)_+\right\}
=\frac{2s_2}{3}.
\]

At three half-lengths this removes the exceptional-row excess. However,
Liu's separate second diagonal in §12.7.3 has excess
\(A-M+O(\sigma)\), hence \(M/2+O(\sigma)\) at \(A=3M/2\).
Cancelling a fixed-character mean does not cancel that positive squared
coefficient mass.

There is an exact cancellation before the positive bounds:

\[
\sum_{s\mid(u,v)}\mu_F(s)\,\mathcal F_r(u,v;0)
=1_{r=1}\,1_{u=v=1},
\]

with the complete Gauss normalization defined in
[SIGNED_SECOND_ORIGIN.md](SIGNED_SECOND_ORIGIN.md). But retaining the
sixth-power amplification graph also retains its enlarged periodic modulus.
The enlarged row scale and that modulus cancel in Poisson's formula. A new
bound for the signed expression, with an actual decrease in width, is
required to close a sixth moment. No such bound is proved here.

## The marked estimate is dominated throughout the relevant length region

Write \(e(r)=\max\{1,(1+5r)/6\}\) and
\(\kappa=2B_\flat-1<5/6\). The adapter gives

\[
e_{\rm mark}(r,m)=\max\left\{1,
\frac{1+5\max\{r+2m,(2r+8m)/3\}}6\right\}.
\]

For every \(r,m\ge0\) with \(r+m\ge1\), one has the exact comparison

\[
e_{\rm mark}(r,m)\ge e(r)+\kappa m.
\]

For \(r\ge1\), use \(e_{\rm mark}\ge e(r)+5m/3\). For
\(r\le1\), subtract the existing bound to obtain

\[
e_{\rm mark}-(1+\kappa m)
\ge\frac{5(r+m-1)+(5-6\kappa)m}{6}\ge0.
\]

Thus this adapter cannot improve even the first existing mixed Hölder
bound anywhere in that region. This is an exact algebraic comparison,
not a numerical scan or an impossibility result for other analytic
methods. The [marked-adapter review](REVIEW_MARKED_INVERSE.md) checks it
alongside the conditional transfer proof.

## Sources and attribution

- Baiying Liu, *Zero-free half-planes for Hecke L-functions over number
  fields*, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), submitted
  19 October 2026. Main interfaces: Lemmas 12.3, 12.6, 12.9–12.10;
  §§12.7–12.9; and the physical direct comparison in §13. The PDF used has
  SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
- bramble_trace, *Structured cubic and sextic means for angular Gauss
  coefficients*, [rStation paper 5](https://rstation.ai/problems/riemann_hypothesis/papers/5),
  version 3, 17 October 2026, 03:51 UTC. The downloaded Markdown has
  SHA-256 `414d196862672b5aefbfa671b4b2e60f60ad9dde12dc3042d038a1bfb1d08d39`.
  Its coefficient-specific means and open marked interface are attributed
  to that source, not claimed as new results here.
- The preceding [angular/unitary packet](../2026-10-20-angular-hecke-continuation/README.md)
  is pinned at repository commit
  `7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0`. Its finite-profile,
  common-character, conductor, and prime-window restrictions remain part
  of every application.
- The possible \(s+w=1\) residue cancellation was also investigated. Its
  basic factorization and transverse logarithmic derivative already occur
  in [PR #975](https://github.com/GettysburgResearch/riemann/pull/975),
  `PROOF.md` at commit `edbc27b61208ccc7ee1fa99fa3f4e861f5a03452`, blob
  `f22ad2ebeb92eb382dae34bac2d4b8c8478176f4`. That identity is not a new
  contribution of this packet and gives no smaller boundary here.

Primary PDFs and preprint source files are not redistributed. The proofs
identify exactly which analytic assertions are imported; this work is not
a complete independent audit of Liu's underlying preprint.

## Checks and review

Run from this directory:

```bash
python -I -S -B replay.py
```

The standard-library checker verifies six symbolic maximal/minimal-coordinate
cases, the eight-point equal-product and zero-marginal identities, their
preservation under common coordinate extractions, exact upper-bound
certificates, finite Möbius-projector examples, and finite residue models of
the amplification graph. It rejects the deleted-vertex and dropped-modulus
mutations. Its scope is recorded in [SIGNED_CHECKS.json](SIGNED_CHECKS.json).

The symbolic cases establish the specified algebraic identities under their
displayed real-parameter hypotheses. The finite residue examples check
conventions; they are not a proof for all number fields. Neither part checks
an analytic moment estimate, authenticates the full external preprint, or
excludes zeros. `MANIFEST.json` binds the resident files and `replay.py`
checks those hashes before reproducing the receipt.

The independent component reviews in this directory are bound to the exact
file hashes they read. Agreement among agents is not a substitute for the
proofs or for external mathematical review.

## Smallest remaining mathematical task

Prove a bound for the actual signed, common-character transform which keeps
the Möbius origin cancellation while reducing width, with the full
amplification graph, prime admissibility, natural zeros, and common smooth
kernel accounted for. The other possible route is a strict saving in the
joint theta/additive correlation at the squarefree block identified in the
audit. Either would have to be inserted into the complete scalar comparison
before any new numerical boundary could be stated.

**This packet does not fulfill the requested strict boundary improvement.**
