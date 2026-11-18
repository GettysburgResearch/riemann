# Third review and independent replay: compact Lagarias concavity certificate

Reviewer: li_advocate. Date:2026-11-17. I read all of `experiments/code/lagarias_compact_arb.py`, inspected its serialized certificate, and independently ran its verification mode using the installed python-flint runtime. All170 rational cells covering exactly[1,2048] passed. Combined with the independently reviewed analytic x≥2048 proof, this gives g''(logx)<0 for every real x≥1, subject to the explicitly stated Arb computational trust boundary. This does not prove Lagarias's inequality for every integer and is not a novelty claim.

## Exact analytic reduction checked

H(x)=ψ(x+1)+γ has the positive-series representation

H(x)=∑_(k≥1)x/[k(k+x)], x>0.

It follows, for example, by expanding (1−t^x)/(1−t) in its integral representation and applying positivity/Tonelli. For fixed x>0, the summand as a function of real k is positive and decreasing. Thus if S_M(x)=∑_(k=1)^M x/[k(k+x)],

S_M(x)+log(1+x/(M+1))≤H(x)≤S_M(x)+log(1+x/M).

The integrals from M+1 and M to infinity give these lower and upper bounds respectively. The direction is correct; it is not an asymptotic expansion. Each summand is increasing in x, so H is increasing. On a cell[a,b], the lower approximation at a and upper approximation at b therefore enclose every H(x) on that cell.

Write h=H(x), B=h+exp(h)logh, Bp=1+exp(h)(logh+1/h). Direct algebra gives

N:=BB''−Bp²
 =−exp(2h)(logh+1)/h²
  +exp(h)[(h−2)logh+2−3/h]−1,

where B'' denotes differentiation in h. I independently expanded the products and found the expression correct.

For t=logx, the previously checked bounds h'≥x/(x+1),0<h''≤1/(2x) imply, whenever B>0,Bp>0,N<0,

g''(t)=N(h')²/B²+(Bp/B)h''
≤[N(x/(x+1))²+BpB/(2x)]/B².

Thus the additional sign P:=N(x/(x+1))²+BpB/(2x)<0 suffices for strict concavity. The sign N<0 is necessary to replace h' by its lower bound in this direction; the code checks it explicitly. Bp>0 is similarly needed for the upper h'' substitution and is also checked.

## Interval and arithmetic audit

The code uses exact Fraction endpoints and python-flint Arb balls at160 bits. Rational midpoint/radius construction is outward enclosing; Arb may inflate the radius, which is conservative. At each endpoint the finite32-term sum and logarithmic tails are evaluated as balls. Their union encloses the lower approximant at a and the upper approximant at b, hence the whole true H range.

The subsequent expressions are evaluated on the full x-ball and full h-ball, sacrificing correlation but preserving enclosure. Acceptance requires the strict ball comparisons B>0,Bp>0,N<0,P<0. An independent sanity check confirmed that a ball overlapping0 compares neither greater nor less than0. No ordinary floating-point value determines acceptance. If a log were not defined on a positive enclosing interval, it could not produce a valid accepted strict-sign witness; the replay passed with well-defined enclosures.

The verification mode checks the first left endpoint, ordered exact adjacency of every cell, strict cell widths, and the final right endpoint. The observed JSON domain is exactly['1','2048'], with170 cells,32 harmonic terms and160-bit precision. There are no uncovered gaps or reliance on a finite set of midpoint samples.

The serialized rational witness bounds have their asserted signs checked. The verifier does not compare their numerical values against newly recomputed enclosures, but it independently recomputes the full witness and requires success on every cell. This is sufficient to certify the asserted domain; it means the JSON is a reproducible grid/certificate accompanied by an Arb verifier, not a standalone rational proof of transcendental bounds.

## Replay performed

Executed successfully:

`PYTHONPATH=/workspace/riemann-runtime python experiments/code/lagarias_compact_arb.py --verify experiments/results/lagarias_compact_arb.json`

The returned result was `verified:true`, `cells:170`, `domain:["1","2048"]`. This was a new replay by this reviewer, distinct from the author's generation run. Runtime was approximately0.071 seconds. The installed library is python-flint0.9.0/FLINT3.6.0, matching the certificate metadata inspected here.

No Lean proof-kernel replay or independent implementation of Arb's exp/log functions was performed. The rigorous numerical conclusion relies on the standard enclosure guarantees of the indicated Arb/FLINT library, Python integer/Fraction correctness, and the audited analytic reduction. It must be described as validated interval computation, not merely high-precision floating evidence and not proof-assistant formalization.

## Consequence and remaining scope

The earlier analytic review established strict g''<0 on x≥2048. This compact computation covers every real1≤x≤2048, including endpoints, so together they establish strict concavity throughout x≥1 under the disclosed computational trust boundary.

Accordingly a certified shared-support-line chord argument can begin at integer1. If an endpoint has equality, strict concavity still makes the interior chord inequality strict; endpoint status itself remains whatever was separately proved. This does not certify an infinite CA endpoint list or imply RH: Lagarias's inequality at all required arithmetic support endpoints remains a separate task.

Classification: independently replayed validated compact computation, with no issue found in the inspected reduction, enclosures, strict comparisons, or interval coverage.

## Independent standard-library integer backend replay

A second implementation, `experiments/code/lagarias_compact_integer.py`, subsequently removed reliance on Arb/FLINT for the finite conclusion. I read it in full, audited its interval operations and elementary log/exp tails, and independently replayed

`python experiments/code/lagarias_compact_integer.py --cells experiments/results/lagarias_compact_integer.json`.

All170 cells over exactly[1,2048] passed at192-bit fixed-point scale, with32 harmonic terms,128 atanh terms and80 exponential terms. Runtime was approximately1.33 seconds. The output explicitly lists no external packages.

Addition/subtraction are exact on the scaled endpoints. Multiplication takes the minimum/maximum of all four exact integer products and rounds down/up. For a nonzero-sign interval[lo/S,hi/S], the reciprocal endpoints are floor(S²/hi) and ceil(S²/lo). The implementation's `−((-S*S)//lo)` is the correct ceiling even when lo is negative, since ceil(a/b)=−floor(−a/b) for every nonzero denominator. I additionally checked240 positive/negative integer endpoint intervals against independent Fraction comparisons; all enclosed the exact reciprocal endpoints.

For log, integer bit lengths choose k exactly so z/S=2^k y with1≤y<2. Outward rational conversion retains1≤y≤2, as asserted. The atanh variable r=(y−1)/(y+1) is nonnegative and at most1/2 in the computed enclosure. After M terms the positive log-series remainder is bounded by

2∑_(j≥M)r^(2j+1)/(2j+1)≤(4/3)2^(−2M)<3·2^(−2M).

The integer-rounded positive tail therefore encloses it. Multiplication of the log2 interval by a possibly negative k uses the general interval multiplication, so negative logarithms are enclosed in the proper direction. Monotonicity allows log of a whole positive interval to use the lower point's lower bound and upper point's upper bound.

For exp, bit lengths reduce a nonnegative argument to0≤y≤1, add the positive Taylor terms through degree80, and add a remainder bound3/81! using e<3. Repeated squaring restores the original scale. Negative arguments use reciprocal of a positive exponential enclosure. All intermediate arithmetic rounds outward. Monotonicity again supplies endpoint evaluation for a whole interval. The cached log2 value is safe in this script because the one requested precision is set before the first function call; changing global precision later without clearing caches would require additional care but does not occur in the replayed execution.

The H enclosure and N/P analytic reduction are the same valid ones audited above. Thus the finite strict-concavity certificate is now independently replayed using only Python integers/Fraction and explicitly proved elementary Taylor tails. It remains a finite computational proof whose code and analytic lemmas must be trusted/audited, not a Lean kernel theorem. The earlier Arb replay supplies a second numerical backend rather than the sole transcendental-enclosure trust boundary.
