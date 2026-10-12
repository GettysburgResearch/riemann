# Independent large-activation audit

Date: 2026-10-10. Read-only checkout/Git. Current verdict: scoped PASS
for the parameterized source construction, scaled analytic certificate
and independent small controls. Complete large serialized receipts are
still awaited; no completed global 19/15 execution claim is made here yet.

Claim under review: H_m(x)>0 for every real m>=19/15, x>=1, for the
literal SHARP/beta source with the duplicated labelled 67. The analytic
contracts E1–E10 and P-A1–P-A7 and the already accepted >=9/7 packet
remain explicit dependencies. Critical power one and RH remain open.

## Parameterized source construction

exclusion_power_data.py is the previously reviewed source builder with
explicit power, product cutoff and endpoint inputs. Its power domain is
1<m<2, product cutoff is an integer >=134, and all requested endpoints
are integers in [1,N]. The labelled 67 occurs twice. At N=10^8 the exact
ordinary prime sieve guard is 3001134 primes through 5*10^7, last 49999991.

Every level >=2 selected product<=N has each label<=N/2 because at least
one other label has value >=2. This argument includes the two distinct
67 slots and repeated numerical product 67^2. It proves complete ordinary
levels 2,3,4 and marked levels 2,4,6 at the larger cutoff. The prefix
recursion and used-label mark identity are unchanged; there is no missing
selected prime factor above the finite prime cap.

At x<=B the selected single-label prefix is complete. At x>B its upper
bound explicitly adds V(a)-C_(1,0)(a,B), the entire omitted positive
prime mass. This overcounts inactive primes safely. The triple-label
source remains complete through every x<=N. Metadata guards bind each
kernel exponent to a=(m+1)/2 and each selected product cutoff to its
active endpoint. Even lower bounds are clipped at zero, which is valid
for their positive subset/marked sums; odd bounds use directed upper
endpoints and the smaller valid global V upper bound.

## Scaled activation tail

The ordinary prime bins are(B,3N/4],(3N/4,N],(N,5N/4],(5N/4,3N/2],
plus the entire prime tail above 3N/2. The duplicated67 is already included
in the selected single-label mass. Thus subtracting that mass and all
four finite bins from complete V leaves exactly the full ordinary
infinite prime tail. Every finite bin is a direct positive prime sum;
the positive directed upper endpoint is used in the upper envelope.

The complete sieve through 150000000 has the guarded count 8444396 and
last 149999957. The ratios C_i/N are unchanged, so
(3/4)sqrt(C_i/N)<= (3/4)sqrt(3/2)<15/16. Each representative numerator
is positive even when its representative lies above the actual x and
the whole bin is inactive. Therefore the same upper kernel safely covers
every native activation pattern without extrapolating the literal kernel.

For 1<m<2 the coefficients b_j, j>=2, are positive and decreasing.
The upper polynomial retains j=0..31 and adds 16 b_32 v^32, which bounds
every term from degree 32 onward throughout v<=15/16. Selected kernels
use the unchanged positive degree 5 lower and degree 6 upper polynomials.
Their positivity on v<=3/4 is explicitly guarded before denominator
substitution. Thus Q_A, P_k and P_k^D are nonnegative on the actual tail
domain. The complete removal coefficient V(a0)<3 makes all retained
pair coefficients positive.

The power-slab directions are correct: negative single-label activation
is upper-bounded at m0, while positive ordinary/marked pairs are lowered
at m1. Dividing the former by the lower d_l and the latter by upper d_h^+
gives the reviewed lower rational expression. Replacing its positive
leading product d_l*d_h^+ by d_l*d_h only lowers the numerator. The final
polynomial degree is at most 38, with the complete finite moment and
infinite prime-bin budgets both retained.

## Whole real coverage

The eleven exact power points form ten consecutive closed slabs from
19/15 through 9/7. The inherited 22 endpoint points through 10^7 plus
2*10^7,4*10^7,8*10^7,10^8 form 26 points and 25 closed intervals covering
[1,N]. The four-level finite margin uses upper odd levels at (m0,U)
and lower even levels at (m1,L), with coefficient 1-odd/5 positive.
Monotonicity including activation jumps therefore covers the entire
power/endpoint rectangle, not merely the displayed endpoints.

For each slab, strict Bernstein positivity on the full outward dyadic
z cap proves every x>=N. Because N is 10000^2, the mathematical cap is
exactly 1/10000; its forty-bit outward dyadic ceiling is
109951163/1099511627776. The stored leaves must cover that entire cap,
and every allowed subdivision retains both children. The union with
the preceding >=9/7 packet gives every larger real power only once all
250 finite rectangles and ten whole-tail guards have passed.

## Independent finite controls

New parameterized tests: 3 groups passed normal and optimized modes,
including literal trial-factorized beta kernels, source/cutoff metadata,
complete omitted one-label mass and invalid domains. Existing activation
tests: 4 groups passed normal and optimized modes, including all five
representative kernels, finite-bin sums and their complete Euler tail,
inactive representatives and invalid metadata.

The independent smallest-prime-factor oracle through 1000000 counts
ordinary physical label subsets at levels 2,3,4,6 as
211614,210777,95714,1284 respectively. It distinguishes multiplicity two
when 67 occurs once from multiplicity one when both 67 labels are used.
In the weighted controls the duplicate-square counts are 1,8,6,1.
The six-label case includes 942690=67^2*2*3*5*7 with both used marks.

Direct integer-factor ordinary/marked moment sums at exact exponents
17/15 and 2267/2000 pass 98 directed checks across all seven moments.
Levels2,3,4 use products<=100000; level 6 uses products<=1000000.
The parameterized 19/15 wrapper is independently checked at N=100000,
with its correct a=17/15, B=50000, retained-level metadata and complete
omitted mass. No N=10^8 prefix/moment runtime was duplicated.

Outputs:
/tmp/review-large-activation-integer-oracle.json,
/tmp/review-large-power-data-tests-{normal,optimized}.log,
/tmp/review-large-activation-tests-{normal,optimized}.log.

## Pending large serialized execution audit

/tmp/review_large_activation_receipt.py is prepared to inspect the two
full owner receipts. It verifies their byte identity and current source
bindings, every exact power/endpoint rectangle and strict margin, all
five complete prime-bin records per slab, and the exact entire tail
domain. It reconstructs every dyadic tail tree, rejects overlaps/gaps,
and independently recomputes each serialized polynomial's Bernstein
coefficients by Horner multiplication and degree elevation. The original
power-basis shift formula is a separate consistency comparison.

Serialized rectangles contain their final margins, not all underlying
raw prefixes. Thus this audit can independently validate all stored
margins and coverage, and every whole-tail polynomial's positivity;
it cannot rebuild the raw N=10^8 source moments from the receipt alone.
Those remain supplied by the reviewed complete engine and full owner
normal/-O execution. Final receipt findings will be appended below.

## Initial frozen source hashes

Builder 8815a8db09189a56591ae74b9d9ddf50ab60aaec307a6e99d7a719dfb1035560.
Checker 36009391680551c51697dfe1acdd0150aa215a6ed81ea60a68e07211d257af3d.
Manuscript 2adf89fbbc9a876597f168d04c8f34003f19dd1ee03053d5951eb8b2e3b13ed7.
Activation tail 1122314fc57d4119c76a15a426dd1af13c6830a610fe09db34f1a05506d1c9d2.
Builder tests 99067e3dbccbc7c2e73a73a0f0cc3d383d87c084be5d14aebaae116705b07553.
Activation tests 3c4c42b6a1197d52dcba7d19af77e888a9aff2ec25daff6837bd6bf64b18daad.
