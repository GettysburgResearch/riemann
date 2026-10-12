# Independent full derivative-amplitude review

Reviewer: operator_mechanisms, 2026-10-10. Verdict: **ACCEPT at the stated
complete imported source scope**, classical global Pick order1,476,000 and
order1,545,000 with the additional uniform complete3/8 displacement bound.
The Volterra-square and optimized count predecessors were separately
reviewed in full. No published count/census or narrower-strip proof is
rerun; no RH or all-order global claim is made.

Frozen proof `heights/final-review/SEPARATE_DERIVATIVE_AMPLIFICATION.md`, SHA
`82e928a5430916851f39cb4537546367827ffb98aa2bc67b34fd59b7e0509396`;
checker `verify_separate_amplification.py`, SHA
`91451405c4d85e36d028b6e08dca0f2caaa7a2ba0fb53aa13f15581b419e98ca`.

I proposed the separate S0/S1/S2 series bounds to the author after reviewing
the complete D-square refinement, and independently audited their actual
final integration and constants. Since D commutes with its powers,
||D^j||<=e*d^(j-2)*n^(2j) for j>=2. The P series pays j=0,1 separately;
the DP series pays j=0 separately; the D²P series uses the square bound
for every term. Their full positive exponential sums are exactly

    S0=p*[1+xi+r*(exp(xi)-1-xi)],
    S1=p*[1+r*(exp(xi)-1)], S2=p*exp(xi), r=e/d².

Discrete Minkowski permits different displacement at every source ordinate
and every intermediate path. The original signed-pole prefactor exponent
4Aq/n remains in p, rather than being silently dropped. Thus these are
complete source norms, not constant-shift operator norms.

Replacing exp(xi) by its whole positive rational upper E preserves every
bound. Since0<r<1 and E>1+xi, S1<=S0<=S2, S1>=1 and S0/S1<=S2 hold
algebraically. Their endpoint guard S2<8/5 therefore pays the first
derivative coefficient: d+3*S0/(n*S1)<d+24/(5N0)<C1. For the second
derivative all lower terms have amplitude at mostS2 and the leading
D²P term uses the sameS2; C2=.291 remains valid. The unshifted continuous
norms and twice-integrated count quadrature J are unchanged.

The full second product rule has two outer terms, costing
2*C2*S2*S0, and its middle term costs2*C1²*S1². The conjugate integral
Taylor remainder A²/2 therefore gives exactly
A²*(C2*S2*S0+C1²*S1²). No source quartet, signed-pole class, analytic
multiplicity or reflected upper member is lost. This completes the
improved whole-source scalar payment.

The complete amplitudes and every negative scalar cost increase with q.
Strict endpoint gaps thus cover every admitted smaller q. The fixed
common good cutoff and its below-or-at atom assignment remain unchanged;
its full selection interval stays inside the imported critical-line census.
The optional complete strip is an additional hypothesis, never replaced
by a finite verified source or an average density assertion.

I inspected every acceptance guard and independently ran normal and
optimized Python. Their exact outputs are byte-identical and match owner
`e66ab88d4faf4d658a3016fabb12e4a15260814a9b78dbeaa4b18b2f6553e9f5`.
The conservative global orders are1,476,000 and1,545,000; the exact maximum
even orders atH0 are1,476,820 and1,545,314. The finite scalar replay does
not authenticate an unreviewed operator theorem: that theorem was read
and audited above. Selectable tail orders still refer to changing kernels.

Independent receipts: `separate_amplification_independent_normal.json` and
`separate_amplification_independent_optimized.json`.
