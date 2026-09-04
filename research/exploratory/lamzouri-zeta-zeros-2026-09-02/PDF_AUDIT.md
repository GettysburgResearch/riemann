# Attached PDF audit: arXiv:2609.02882v1

```text
Status: SOURCE_RECEIPT + VISUAL_AUDIT + STATEMENT MAP
Scope: the exact 14-page PDF supplied for this import pass
Mathematical status: source verification, not an independent proof
Riemann Hypothesis: unproved
```

## 1. Exact file receipt

The supplied file is the arXiv v1 paper

```text
Youness Lamzouri
A new proof that more than 2/3 of the zeros of the Riemann zeta function
are simple and on the critical line
arXiv:2609.02882v1 [math.NT]
posted 2026-09-02
manuscript date 2026-09-03
```

Receipt:

```text
SHA256:
fa33485f517b3c94d2f6e4d4366f3ab14a1e413a738db512e1862f4a0944f5f9

size:
505955 bytes

pages:
14

PDF version:
1.7

page size:
612 x 792 points
```

The metadata names Youness Lamzouri as author and records the expected full
title. The file is unencrypted, contains no JavaScript, and has no form
fields.

## 2. Render audit

All fourteen pages were rendered to PNG at 1190 by 1540 pixels and visually
inspected, both individually and in contact sheets.

No instance was observed of:

- a blank or missing page;
- unexpected page rotation;
- clipped body text, equations, footnotes, or references;
- broken-glyph blocks;
- corrupt figures or tables;
- an obvious mismatch between pagination and extracted text.

This is an importer visual audit. It does not replace a second person's
independent comparison with the public arXiv bytes.

## 3. Page-by-page theorem map

### Pages 1-3: theorem and comparison with the Claude/Alpoge-Furman proof

The abstract states the unconditional bounds

```text
more than 67.25% simple and on the critical line;
at least 83.62% distinct.
```

It identifies the conceptual change precisely: the earlier finite-dimensional
matrix representation of Weil's Hermitian form and rank-trace inequality are
replaced by one Hilbert-space inequality followed by the unconditional form of
Montgomery pair correlation.

Theorem 1.1 is on page 3:

\[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge
C_0
=
\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right),
\]

and

\[
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}
\ge
\frac{C_0+1}{2}.
\]

The page explicitly says both proofs reduce to a quadratic form over zeros and
therefore to the same Montgomery-Taylor extremal problem.

### Pages 4-5: failure of the termwise-positivity route and Proposition 2.1

The paper explains that a direct unconditional version of Montgomery's
classical diagonal majorization would require global positivity for an entire
kernel evaluated at complex zero differences. No nonconstant entire function
can provide the required global nonnegative-real behavior.

Proposition 2.1 begins on page 5. For real even
\(\eta\in L^2(\mathbb R)\), supported in \((-\lambda,\lambda)\) and normalized
by \(\widehat{\eta^2}(0)=1\), put

\[
K(\xi)=\widehat{\eta^2}(\xi).
\]

For every nonempty finite conjugation-invariant complex multiset, it gives the
simple-real and distinct-support lower bounds from the complete ordered
\(K^2\) energy. Individual off-diagonal terms need not be nonnegative.

### Pages 5-9: exact Hilbert-space mechanism

The proof defines

\[
f_z(u)=\eta(u)e^{-2\pi iuz}
\]

and its conjugation-even and conjugation-odd components \(g_z,h_z\). It proves

\[
K(z-s)=\int_{-\lambda}^{\lambda}f_z(u)\overline{f_s(u)}\,du
\]

in the paper's conventions and rewrites the whole ordered pair sum as

\[
\int_{-\lambda}^{\lambda}\int_{-\lambda}^{\lambda}|F(u,v)|^2\,du\,dv.
\]

The finite flag is

```text
U = span(multiple-real f_x, nonreal even g_z)
V = span(all-real f_x, nonreal even g_z)
W = span(all-real f_x, nonreal even g_z, nonreal odd h_z).
```

An orthonormal basis is chosen by Gram-Schmidt, adapted to
\(U\subseteq V\subseteq W\). Conjugation symmetry makes the relevant
coefficients real. Tensor squares of the basis vectors are orthonormal in the
two-variable Hilbert space, so Bessel's inequality applies.

The proof then treats three coefficient ranges with three different scalar
inequalities:

```text
first range:   a^2 + 4 >= 4a
middle range:  a^2 + 1 >= 2a
last range:    a <= 0, hence a^2 >= 2a or a^2 >= 4a as needed.
```

Pages 7-9 show exactly how multiplicity, real simplicity, and nonreal
conjugate pairs pay the dimensional terms. This is the load-bearing
mathematical mechanism and is more informative than the shorthand
description as one tensor norm.

### Pages 9-12: weighted pair correlation and exact weight removal

Lemma 3.1 on page 10 states the unconditional BGST pair-correlation formula
with

\[
w(z)=\frac4{4-z^2}.
\]

The Hilbert proposition requires the same pair sum without \(w\). Lemma 3.2
builds smooth cutoff functions approaching the Montgomery-Taylor extremal
density and sets

\[
Q_\delta=f_\delta*f_\delta,
\qquad
r_{\delta,T}
=
Q_\delta-\frac{Q_\delta''}{4(\log T)^2}.
\]

Fourier differentiation gives the exact polynomial factor that cancels the
rational weight. The proof applies the fixed-test pair-correlation theorem
separately to \(Q_\delta\) and \(Q_\delta''\); it does not silently invoke a
\(T\)-dependent test-function uniformity theorem.

The resulting constant approaches

\[
C_{\mathrm{MT}}
=
\frac12+\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)
=
1.3274992963206\ldots.
\]

### Page 12: sharp barrier of the scalar method

Remark 3.4 cites the relevant Hilbert-space extremal result to conclude that
the Montgomery-Taylor constant is optimal for this method. Consequently,
smoother cutoffs or another scalar test within the same support-one
second-moment class cannot improve the final \(0.6725007\ldots\) constant.

Any improvement must add information: several kernels, a larger admissible
support theorem, higher correlations, local/effective control, or an
individual-zero mechanism.

### Page 13: transfer to zeta and formal-certificate boundary

The proof rescales each zeta zero by

\[
i\left(\rho-\frac12\right)\frac{\log T}{2\pi}.
\]

Functional-equation reflection becomes complex conjugation; real rescaled
points are precisely critical-line zeros, with multiplicity preserved.
Proposition 2.1 and Lemma 3.2 then give Theorem 1.1 after
Riemann-von Mangoldt normalization.

Appendix A describes the formal boundary accurately:

```text
Proposition 2.1: unconditional formal certificate;
Theorem 1.1: formal certificate under BGST Lemma 5 and
             the standard Riemann-von Mangoldt asymptotic.
```

This agrees with the explicit hypotheses in the pinned Lean theorem types.

### Page 14: references

The references pin the two analytic inputs used by the Lean-facing theorem:

```text
BGST, Acta Arith. 214 (2024), Lemma 5;
Titchmarsh, The Theory of the Riemann Zeta-Function, Theorem 9.4.
```

## 4. Consequences for the import dossier

The attached PDF closes the earlier byte/provenance gap and strengthens four
parts of the dossier:

1. the exact source file is now SHA256-locked;
2. every displayed theorem and proof stage has a page locator;
3. the three-range Hilbert argument is recorded explicitly;
4. the impossibility of improving the constant within the same scalar method
   is source-backed by Remark 3.4, not merely inferred.

It does not close:

- independent mathematical review of every proof step;
- a clean local Lean/Comparator/Nanoda replay;
- formal proofs of the Riemann-von Mangoldt and BGST inputs;
- any route from a positive zero proportion to RH.
