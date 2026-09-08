# Sources and exact scientific boundaries

## Frozen repository inputs

Repository: `GettysburgResearch/riemann`.
PR #805, branch `research/astra/20260906-dilation-observability`.
Current parent observed in this pass:
`0f8724bbd86c1de8f40eacbf30129321e0ebc8aa`.
Original main base: `051808c1f8367b4320c52f94b40908eb2173d622`.

The authenticated GitHub read reconfirmed the current PR head and the original
code blobs at that head:

```
intervals.py  54e216c0ef0bb52913cee86387e0e838d062b3c2   6922 bytes
replay.py     87e66bacc507bae4dee3a4b6b288056aebcd1844  15375 bytes
```

SOURCE_LOCK.json pins the SHA-256 of those two files and three proof/numerical
notes. The local predecessor packets match those pins. The new code compiles
only the two authenticated source modules; it does not trust their pyc cache.
The parent mathematical identities used here are the weighted parity split,
Jordan Gram, and positive Mobius-square detail tail. Their all-scale bound is
not misidentified as an original full-norm bound. Every new constraint,
coefficient estimate, source identity, and growth implication is proved here.

## Primary literature inspected in this pass

1. Luis Baez-Duarte, *A strengthening of the Nyman--Beurling criterion for the
   Riemann Hypothesis*, arXiv:math/0202141v2 (2002).
   https://arxiv.org/abs/math/0202141
   The integer approximation criterion is classical. The main sufficient
   implication in this packet is also derived directly by Mellin evaluation;
   it does not import a converse theorem for the particular new coefficients.

2. Michel Balazard, *An arithmetical function related to Baez-Duarte's criterion
   for the Riemann hypothesis*, arXiv:1812.04309v1 (2018).
   https://arxiv.org/abs/1812.04309
   The step Hilbert space, projection notation, and Vasyunin dual background
   were checked in the paper, including Proposition 10 and the relevant PDF
   page. These are established ingredients, not claimed inventions here.

3. Werner Ehm, *On certain Gram matrices and their associated series*,
   arXiv:2405.06349v2 (2024).
   https://arxiv.org/html/2405.06349v2
   Sections 1 and 8 were inspected. The paper separates explicit Gram
   decomposition from the difficult Mobius-weighted quadratic form. Its
   discussion of optimally tapered coefficients retains the RH/zero-derivative
   hypotheses of Bettin--Conrey--Farmer. Neither its unbounded quadratic-form
   conclusion nor a general rate for arbitrary coefficients is used here.

4. Sandro Bettin, J. Brian Conrey, David W. Farmer, *An optimal choice of
   Dirichlet polynomials for the Nyman--Beurling criterion*,
   arXiv:1211.5191 (2012).
   https://arxiv.org/abs/1211.5191
   The hypothesis boundary was checked: RH and control of inverse squared
   zeta derivatives enter the reported optimal asymptotic. That conditional
   result is not an unconditional estimate for this new rational trial.

5. Helmut Maier and Michael Th. Rassias, *Explicit estimates of sums related
   to the Nyman--Beurling criterion for the Riemann Hypothesis*,
   arXiv:1806.05070v1.
   https://arxiv.org/abs/1806.05070
   The abstract, introductory Gram/cotangent formulas, and Theorem 2.1 were
   read; its printed theorem page was also rendered. Its fixed-power saving
   concerns `sum_(k^D<=n<2k^D) mu(n)g(n/k)`, D>=2. No adapter from the entire
   constrained two-variable norm here to that range is established. The
   source is credited as a possible analytic input, NOT an imported proof of
   BL26.E. The full twenty-page proof was not independently audited.

The Jordan-totient identity, divisor Mobius inversion, constrained quadratic
minimization, Cauchy--Schwarz, and elementary Mellin uniqueness are classical.
The elementary coefficient estimates here use no PNT, Mertens power saving,
zero-free region inside the critical strip, zero census, or numerical spectrum.
The standard Euler product on Re(s)>1 and the functional equation are used
only in the proved zero-to-growth/RH implication.

No external novelty or priority is asserted for the synthesis. The computational
checks are authored here, not an independent mathematical referee opinion.
