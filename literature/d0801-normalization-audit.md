# D-0801 normalization and admissibility source audit

Agent: `gpt56-04-c`  
Issue: #28  
Snapshot: 2026-07-23

## Primary source inspected in full

Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail order for
the truncated Weil quadratic form*, arXiv:2607.02828v1 (2026).

Inspection points:

- Section 2 fixes
  \[
  L=\log c,\quad \Delta=L/(2\pi),
  \]
  and the inverse transform
  \[
  g(z)=\int_{-\Delta}^{\Delta}\widehat g(\xi)e^{2\pi iz\xi}d\xi.
  \]
- Lemma 2.2 states the admissible class: entire of exponential type at most
  `L`, compact Fourier support in `[-Delta,Delta]`, and `O(|Re z|^-2)` on fixed
  horizontal strips, with absolutely convergent zero sum.
- Theorem 2.5 states the exact normalization
  \[
  \sum_{z:\,\zeta(1/2+iz)=0}g(z)
  =-\frac1\pi\sum_{q=p^a\le c}
    \frac{\Lambda(q)}{\sqrt q}
    \widehat g\!\left(\frac{\log q}{2\pi}\right)
   +2g(i/2)
   +\frac1{2\pi}\int_{\mathbb R}h_+(r)g(r)dr,
  \]
  with
  \[
  h_+(r)=\operatorname{Re}\psi(1/4+ir/2)-\log\pi.
  \]
- The proof explicitly derives the negative prime sign, positive pole term,
  `log(q)/(2*pi)` frequency, and compact-support truncation at `q<=c`.

This source directly supports the fingerprint used by T-2801 and X-2803.

## Earlier primary interface located

Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
numbers, I*, Rendiconti Lincei Matematica e Applicazioni 11 (2000), 183–233.
EUDML metadata and abstract were inspected. The paper establishes Weil's
quadratic functional as a formulation of RH and studies finite-dimensional
restrictions. The exact D-0801 transport and source constants are taken from the
full-text 2026 source above, not inferred from metadata.

## Independent repository derivation

T-2801 does not merely cite Lemma 2.2 for D-0801. It proves separately that the
piecewise autocorrelation weight is continuous and piecewise linear with
endpoint zero, that its zero-extended derivative has bounded variation, and
that two integrations by parts give the required strip decay. This matters
because D-0801 is a different finite family from the trigonometric Galerkin
family constructed in the cited paper.

The imported element is the classical Guinand–Weil formula in the displayed
normalization. The admissibility check and substitution of the D-0801 transform
are internal to T-2801.

## Machine-readable fingerprint

```text
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

This digest binds the exact JSON in
`experiments/X-2803-normalization-fingerprint/certificates/`.

## Remaining source work

Before promotion beyond `PROPOSED`, a reviewer should:

1. reconstruct the formula from another primary normalization, preferably
   Bombieri or Connes–Consani–Moscovici;
2. check the translation from its zero variable to `(rho-1/2)/i`;
3. verify the pole convention at `+-i/2`;
4. confirm that the piecewise-autocorrelation strip proof meets every stated
   hypothesis of that second source.
