# Independent review of complete Xi boxes and physical compression

Verdict: **PASS, exactly within the finite and conditional scope below.**
Reviewed scientific source: `7fbcd592042a5cc98c17d0db2fac62f8171267f2`.
Parent: `134a55016b4f3ea970dc8e5f03505d4e97afff07`.
Reviewer: root, not the author of this five-file scientific packet.
The reviewed source is unchanged. This review adds separate files only.

## Accepted statements and non-statements

For the literal unrescaled Xi function and the three exact positive constants
lambda_32, lambda_64, lambda_128 specified in BC1, the complete open rectangles
(a-6,a+6)+i(0,1) contain respectively **3, 5, 6 zeros of R5**, counted with
multiplicity. Their complete closed boundaries are zero-free. All fourteen
listed disks contain one simple zero, and C5, R0, C0, f6, W and R5prime are
nonzero throughout each containing rectangle. No RH or innerness assumption
is needed for these finite zero statements, subject to the explicit FLINT
enclosure contract.

Separately for each parameter, IF Theta0 and Theta5 are inner, removal of
their maximal common inner divisor leaves all listed denominator nodes.
The finite-input, GLOBAL-output squared Hilbert--Schmidt norm is greater than
1193/1000, 1551/1000, 1343/1000 respectively. The corresponding operator norm
is greater than 748/1000, 816/1000, 747/1000. These are lower bounds, not an
identification of raw and reduced numerators.

There is no conclusion about a Fourier output band, native outer weights,
cofinal capture, infinite HS norm, a prescribed historical high-T partition,
or RH. The three rows belong to three different parameters/operators and
must not be added together as the charge of one fixed operator. The node
near real part131.3028 has raw modulus below1/4; the stronger bound on OA's
selected nine nodes was correctly not extrapolated to the complete list.

## Analytic proof review

I read the full five-file scientific source (the large fixture by complete
machine reconstruction), the executed parent helper and parent proof, and
the pinned CP, L106610 and L106620 notes. The following steps close:

1. BC1 has the literal factor1/2, the plus-i chain rule, and the exact digamma
   phase derivative. Lambda stays constant when differentiating in z. The
   selected finite anchors are not confused with a sufficiently-high theorem.
2. For every boundary midpoint, the radius1/4 disk contains the radius1/8
   circles about all points of the smaller disk. Cauchy's derivative bound
   therefore gives BC4 for R5. A SECOND Cauchy estimate gives the geometric
   analytic remainder in BC5. Formal-series truncation alone is not used as
   a remainder estimate. The degree31 polynomial uses indices through37,
   within cap39.
3. The scalar product expression for Xi is analytic on neighborhoods of all
   these rectangles: Im(s)=Re(z) stays away from zero, so neither gamma nor
   zeta has a pole there. The scalar ball over the entire outer rectangle is
   a valid sup bound, not a sample at its center.
4. The416 oriented arcs cover all four edges, including y=0 and y=1 and
   closure. Each full image enclosure and its two rational polygon vertices
   fit in one convex zero-free rectangle. The endpoint homotopies agree,
   so the entire image loop has the rational polygon's winding number.
5. The local Rouche remainder uses a uniform eighth-derivative enclosure.
   Each disk's count is one with multiplicity, hence its zero is simple.
   Disjointness plus equality with the complete count exhausts each box.
6. With the conjugate-linear-first convention, M_J* v_b=conjugate(J(b))v_b,
   whence H_J=V_J G V_J*. The inverse-kernel Gram and the Cauchy determinant
   formula are correctly oriented. No coefficient-value identification is
   substituted for this physical metric.
7. Theta0=Gamma U gives Theta0 H2 subset U H2 and thus P_U>=P_Theta0.
   This is a GLOBAL-output projection comparison. Compression gives the
   correct trace and Rayleigh inequalities. A noncommuting Fourier output
   projection cannot be inserted into that Loewner implication.

No mathematical repair was required.

## Author-producer replay, independently performed

In a new worktree at the exact scientific SHA:

- All40 new tests pass normally (21.658s) and under `-O` (21.432s).
- All36 executed-parent tests pass normally (9.200s) and under `-O` (9.137s).
- Both new producer checks pass, rebuilding the actual special-function
  evaluations, full arcs, all roots and full matrices.
- Eight direct source bindings, the six parent bindings, and the aggregate
  of44 pinned native runtime files are checked by those authenticators.
- Three additionally resealed count/metric/scope attacks are rejected by
  FULL fresh `check_report` calls without mocking the positive rebuild.
- Replacing the primitive Xi series by zero is rejected on fresh replay.
- The full parent-to-science whitespace check passes; no reviewed blob was
  reformatted or otherwise edited.

The test suite's exact rational Schur projection comparison, wrong-orientation
falsifier, common-factor rank-one PSD control, and noncommuting-output
counterexample were read and replayed. Its separate outward Fraction interval
implementation reproduces the actual trace/Rayleigh floors without FLINT
matrix operations; this remains dependent on the Xi enclosures for its inputs.

## Additional non-author implementation

`xi_box_compression_independent_review.py` imports NO author module. It binds
the exact scientific fixture and four artifact identities, then independently
recomputes the transcendental inputs and finite conclusions using:

- unit **s**-series coefficients, followed by explicit powers of i for the
  z-chain rule;
- xi_R(1-s), with exp(logGamma(s/2)-s log(pi)/2), rather than the author's
  direct gamma-product expression in a z-series;
- lambda from the derivative of the full paired log-Gamma phase series,
  rather than a direct scalar digamma call;
- **832 half-sized boundary arcs per box**, using24 Taylor terms and the
  independent tail M_F*(1/8)^24/(1-1/8);
- a quadrant/quarter-turn winding algorithm rather than ray crossings;
- a native LU solve G X=H rather than inverse multiplication or the author's
  explicit Gauss--Jordan code.

At320 bits normally and448 bits under `-O`, each run independently certifies
all2,496 refined arcs, counts3/5/6, fourteen fresh simple/noncommon root disks,
252 derivative overlaps, and all six trace/norm floors. The changed-precision
arc enclosures also overlap their corresponding coarse source enclosures.
The fresh raw-value corridors include the sub-quarter node. This is a separate
implementation and parametrization, **not a separate special-function library**.

The two complete rational reports are resident beside this note:

- `xi_box_compression_independent_review_320.json`, payload
  `0c095a9f538a0ae886773d2eed361d9cda47a8f597692c47f62f91394df741b8`;
- `xi_box_compression_independent_review_448.json`, payload
  `84297f0d3240b5655af0bf49e989e19e72755dec8d05933dacb5247785f3f529`.

Their exact integers were retained as raw Python JSON text when written;
they were not passed through a JavaScript numeric serialization round trip.
The script LF SHA256 is
`c6bfdddcf9bb9a64b6ee4f2648336108d1dcbcbc2209489f5465ebafa9416ad8`.

## Trust and next burden

I checked the primary [ball arithmetic contract](https://python-flint.readthedocs.io/en/latest/general.html),
[series API](https://python-flint.readthedocs.io/en/latest/acb_series.html), and
[matrix inverse/solve API](https://python-flint.readthedocs.io/en/latest/acb_mat.html).
The non-approx operations used here provide enclosure arithmetic according
to that implementation contract. No formal verification of FLINT, hardware,
or the entire runtime is claimed.

The completed finite census and source-correct global compression are accepted.
The next computational experiment should hold one lambda fixed across regions
and include the joint cross-region Gram entries. A band theorem needs a new
argument; it cannot be obtained by silently inserting a band projection into
BC11. Infinite-dimensional capture remains open.
