# L-25804 — Two-frequency adjacent-flow energy

Claim ID: `L-25804`  
Title: Signed adjacent transport has an exact divergence identity and a `j^-2` physical displacement metric inside the reviewed two-frequency block  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #258  
Dependencies: PR #241 `L-9518`; elementary summation by parts  
Scope: finite source fibers and compact physical blocks

## 1. Exact adjacent divergence

Let `H` be a finite-dimensional Hilbert space, let

\[
v_j\in H,
\qquad A\le j\le B,
\]

and let real or complex coefficients satisfy

\[
c_j=b_j+F_{j-1}-F_j,
\qquad F_{A-1}=F_B=0.
\tag{L-25804.1}
\]

Then finite summation by parts gives

\[
\boxed{
\sum_{j=A}^{B}c_jv_j
=\sum_{j=A}^{B}b_jv_j
+\sum_{j=A}^{B-1}F_j(v_{j+1}-v_j).}
\tag{L-25804.2}
\]

No positivity is required. The identity is valid source-fiber by source-fiber,
so it may be applied before packet norms or total variation.

The sequence `F_j` is the signed transport flow, `c` is its input divergence,
and `b` is the declared lower-scale or boundary remainder.

## 2. Logarithmic displacement cost

Let `U` be absolutely continuous and put

\[
v_j(x)=U(x-\log j).
\]

Write

\[
h_j=\log{j+1\over j}.
\]

Then

\[
v_{j+1}(x)-v_j(x)
=-\int_0^{h_j}U'(x-\log j-u)\,du.
\tag{L-25804.3}
\]

For every real interval `I`, Cauchy--Schwarz gives

\[
\boxed{
\|v_{j+1}-v_j\|_{L^2(I)}^2
\le
h_j^2
\sup_{0\le u\le h_j}
\|U'\|_{L^2(I-\log j-u)}^2.}
\tag{L-25804.4}
\]

Since

\[
h_j\le {1\over j},
\tag{L-25804.5}
\]

adjacent transport at index `j` naturally has a `j^-2` energy cost.

This is the same metric exposed independently by the exact parabolic carry
flow on PR #254.

## 3. Exact two-frequency Gram

Let the represented source fibers have Fourier transforms `V_j(t)`. The
physical unit-block energy of the transported current is

\[
\left\|
\sum_{j=A}^{B-1}F_j(v_{j+1}-v_j)
\right\|_{L^2([J,J+1])}^2.
\]

By the reviewed two-frequency identity `L-9518`, this is exactly

\[
\boxed{
F^*\mathcal G_{J}^{\nabla}F,}
\tag{L-25804.6}
\]

where

\[
\begin{aligned}
(\mathcal G_J^{\nabla})_{jk}
={1\over(2\pi)^2}
\iint
&[V_{j+1}(t)-V_j(t)]
\overline{[V_{k+1}(s)-V_k(s)]}\\
&\times\Phi_{J,\alpha}(t-s)\,dt\,ds.
\end{aligned}
\tag{L-25804.7}
\]

Equivalently it is the finite arithmetic normal Gram obtained after expanding
every source tuple. All cross terms are retained.

A production certificate may prove an upper bound for (L-25804.6) by:

1. an exact rational/interval LDL certificate;
2. a cellwise polynomial SOS certificate;
3. an exact source-bound domination by derivative energies using
   (L-25804.4);
4. a combination of the preceding methods.

It may not replace `G_J^nabla` by a diagonal matrix unless an independent frame
inequality is proved.

## 4. Nonnegative and signed flows

If `F_j>=0`, Jensen gives the useful sufficient bound

\[
\left\|\sum_jF_jw_j\right\|^2
\le
\left(\sum_jF_j\right)
\sum_jF_j\|w_j\|^2.
\tag{L-25804.8}
\]

For a signed flow, split into positive and negative parts or verify the complete
Gram directly. In either case the proof object must preserve the correlations
between repeated source fibers.

The signed option is essential. PR #254 proves that taking a positive part
before transporting the parabolic defect incurs a fixed square-root loss.

## 5. Source-fiber compatibility

For the prime-anchored normal form of `L-25801`, expose

\[
g_{K-1}=\Lambda*d_{K-1}.
\tag{L-25804.9}
\]

A source row may therefore retain a marked prime-power coordinate together with
the remaining divisor and Möbius coordinates. Adjacent transport is applied to
the aggregate anchor index while the full residual fiber is kept inside
`v_j`.

Every edge must export both endpoint source manifests. An edge is invalid if it
silently changes a residual cutoff, a squarefree condition, or an output cell.
Such events are boundary rows, not internal flow.

## 6. Proof boundary

Closed exactly:

- the adjacent divergence identity;
- the logarithmic `j^-2` displacement estimate;
- the exact two-frequency transport Gram;
- the distinction between signed transport and unsigned deletion.

Open:

- a source-bound flow for the depleted top source;
- a subexponential quadratic transport-cost estimate;
- `PADT(K)` or RH.
