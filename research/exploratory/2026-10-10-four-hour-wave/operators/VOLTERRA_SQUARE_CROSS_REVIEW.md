# Independent Volterra-square complete-source review

Reviewer: operator_mechanisms, 2026-10-10. Verdict: **ACCEPT at the stated
imported source scope**, including classical global Pick order 1,462,000
and order 1,536,000 with the additional uniform complete 3/8 displacement
hypothesis. This is an analytic/code review and exact normal/optimized
replay; no published Turing, census, or quasi-RH proof is rerun.

Frozen proof `heights/final-review/VOLTERRA_SQUARE_DOUBLE_COUNT.md`, SHA256
`f749951aa06421b4856d26ff795127f22649980371d16b619e4003df0dba6629`;
checker `verify_volterra_square.py`, SHA256
`515a76589d1fc874105ab5f0102a189fb19fdfe3b92a2014eb6502b772a21050`.
The optimized double-count predecessor was separately fully reviewed.

The compression identity is exact. With m_i=|e_i|^2 and disjoint consecutive
intervals of those lengths, the compression of V^2 has upper entries
e_i*e_j*[sum_between m_k+(m_i+m_j)/2] and diagonal m_i^2/6. The strictly
upper endpoint matrix square has the same upper entries without either
endpoint half-mass and has zero diagonal. After unitary phase removal,
entrywise nonnegative domination gives norm domination for all complex
vectors through absolute values. It is not a PSD matrix comparison.
Zero endpoint coordinates may be removed without changing any contribution.

The complete Volterra-square kernel is (s-t)*1_(s>t); its squared
Hilbert--Schmidt norm is L^4/12. Compression cannot increase the norm.
Thus ||U^2||<=L^2/sqrt(12), with L=tr(E)<=n^2. The exact upper-triangular
identity D+D*=E-M gives D=U+B with the stated diagonal minus strict-upper
Hermitian M. Its Frobenius bound pays the entire B. Expanding D^2 before
taking norms gives U^2+UB+BU+B^2, requiring no commutativity. The rational
endpoint guards uniformly imply ||D^2||<.2907*n^4 for n>=850000.

The improved bound is valid for the original fixed-denominator polynomial
class. D commutes with D^2 and its own powers, so applying the full
variable-path Minkowski series to D^2 P preserves the new leading second
derivative coefficient. The original prefactors, DB, and lower-order
derivative terms are all retained. This is the decisive reason the
unshifted continuous and independently displaced sampled derivative
bounds both admit C2'=.291; the first coefficient and full amplification
remain unchanged. No higher-pole rational class is substituted.

The reviewed twice-integrated count argument then uses exactly
J'=4*cA'*(C2'+C1^2). The conjugate second-order remainder price is exactly
A^2*(C2'+C1^2)*kappa^2*q^2*(U*+J'*q^2). All signed-pole, upper reflected,
quartet and multiplicity factors remain included. Exact endpoint
positivity decreases monotonically with q and covers the entire allowed
range. The normal and optimized exact replays are byte-identical and
match owner receipt `b8b00c6e2baf62faba0671656ccdd5dcdcc4fd7a94f32ffa63c8f5a4be28ec9f`.

I inspected all 24 independently integrated compression fixtures and every
uniform rational, square-root, exponential-tail, complete-source gap and
global order guard. The maximal even orders at H0=3e12 are 1,462,532 and
1,536,554. The conservative headline orders stay strictly inside the
same complete good-cutoff interval and imported critical-line census.

The classical result adds no narrower-strip assumption. The second
requires the explicitly imported complete strip, with actual displacement
at most 3/8. Both remain finite global orders; selectable tail orders
refer to changing kernels. Neither gives all-order global positivity or RH.

Independent receipts: `volterra_square_independent_normal.json` and
`volterra_square_independent_optimized.json`.
