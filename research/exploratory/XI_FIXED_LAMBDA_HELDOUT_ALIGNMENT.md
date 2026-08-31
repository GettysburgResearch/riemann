# Fixed-lambda Xi held-out alignment and finite normalized Gram

Status: PROPOSED FINITE CERTIFICATE AND CONDITIONAL TRANSPORT LEMMA.
Authoring base: 0e3fc9b482f0f115a49a6209ccbfeffae640014a (FC).
All frozen parent science and review records remain unchanged.

## Exact source and held-out coverage

The primitive is the actual unrescaled f(z)=xi_R(1/2+i z), with the ONE
exact constant lambda64=[Re psi(1/4+32i)/2-log(pi)/2]^-1.
It is not refrozen at the new heights. Define R_k=f^(k)-i lambda64 f^(k+1),
C_k=f^(k)+i lambda64 f^(k+1), and raw Theta0=R0/C0 as in FC.

The three new open boxes, in this order, are exactly

    (250,262)+i(0,1), (506,518)+i(0,1), (1018,1030)+i(0,1).

These endpoints and the old fourteen FC nodes are fixed before computing
any new count, root or alignment value. There is no predicted root count,
alignment threshold, growth trend or Gram constant. No box or strip may
be silently moved or discarded. Every failed certification tier must be
retained with its literal obstruction; an unresolved boundary remains an
unresolved boundary, not a complete census.

## Declared arithmetic and search schedule

The existing pinned FLINT runtime will be used. New, explicitly labeled
primitive wrappers extend the old x<150 domain only to 20<Re z<1100,
with -1<Im z<2 for boundary rectangles. Parent wrappers are not edited.
Only 256, 512 and 1024-bit working precision are permitted.

Boundary certification tiers, attempted in order until one succeeds:

| Tier | Bits | Segment length | Taylor terms |
|---|---:|---:|---:|
| 1 | 256 | 1/16 | 32 |
| 2 | 512 | 1/32 | 40 |
| 3 | 1024 | 1/64 | 48 |

All tiers use the SAME full closed box boundary, the BC analytic Cauchy
tail proof with rho=1/8 and outer radius1/4, and exact rational polygon
winding. This is declared mesh/precision refinement, not endpoint tuning.
The series cap is at most 55, matrix order at most 64, JSON at most
24000000 bytes/600000 nodes/depth24, rational components at most4096 bits.

Uncertified root-location scouting uses the fixed real mesh j/4 across
each box and imaginary seeds 1/8,3/8,5/8,7/8, at 256 bits with at most
24 Newton steps per seed. Seed outcomes (converged candidate, duplicate,
domain exit, derivative obstruction or iteration limit) are retained.
Scouts are not proof. Candidate centers are rounded to denominator2^180;
the root discs have radius2^-120. Root certification tries256/512/1024
bits in that order, using the FC Rouche and full-rectangle noncommon guards.
The complete boundary count must match the distinct certified root discs
before any box is called exhaustive. Extra candidates or missed counts
must remain visible; no extra seed survey is preregistered.

## Finite targets and quantifier firewall

Rebuild the old fourteen FC root certificates and raw values. For them
and every new certified surviving node b=x+i y, compute the complete
normalized Hardy Gram G_ij=2sqrt(y_i y_j)/(y_i+y_j+i(x_j-x_i)), including
all old/new cross entries. Report outward row-sum Bessel upper bounds for
the old span and each nested added-box prefix. These are finite constants,
not a uniform infinite-family bound; absolute row sums can grow even if
an infinite family is Bessel.

Compute exact ball-enclosed partial sums and each new-box increment of

    sum |raw Theta0(b)|^2 Im(b)/|Re(b)|.

This is the weighted alignment in the root's proposed Laplace low-pass
criterion. Every modulus uses the entire certified root rectangle. Do not
replace raw values by reduced ones, and do not call the weighted sum a
physical trace. The finite special-function evaluations are unconditional;
operator interpretations retain the component-innerness premise. No finite
prefix establishes uniform Bessel control, divergent weighted alignment,
cofinal physical capture, native outer-metric capture or RH.

A possible separate analytic interface is transport from real simple f6
zeros t with kappa^2=-f7(t)/f5(t)>0 to R5 zeros of approximate height
1/(lambda64*kappa^2), under explicit local Taylor remainder and raw-value
conditions. Such conditions are unpaid actual-Xi hypotheses; a one-wave
Riemann--Siegel approximation is not assumed. Any lemma developed must
state those hypotheses fully and must not convert finite tests into them.

The preceding scope, with its original "no new held-out computation yet"
status, is frozen at24544028cd033ea66a6b64bec254da5ea43230c9. Its exact
historical blob is pinned as PREREG. The following results were added only
after that commit. All old science remains unchanged.

## 1. Held-out result, including the unfavorable observations

HA1. For the ONE exact lambda64, the three prescribed new boxes contain
respectively8,9,9 R5 zeros counted with complex multiplicity. All26 are
individually simple and locally noncommon: C5,R0,C0,f6,W,R5prime are nonzero
on every containing root rectangle. Together with the14 rebuilt FC nodes
this gives40 distinct certified companion zeros. Each is a simple pole of
the actual meromorphic ratio Theta0/Theta5. They are not off-critical zeros
of Xi itself. The new boxes have zero-free FULL closed boundaries, with
no omitted real-axis strip or moved vertical edge.

The256 and512 boundaries pass tier1. The1024 boundary fails tier1 at
zero-based arc194 and tier2 at arc389: the Taylor image enclosure fails
to exclude zero. It then passes the preregistered tier3, with1024bits,
1664 segments of length1/64 and48 Taylor terms. These failed enclosures
are not certified boundary zeros. Every tier outcome remains in the
fixture. A separate timing diagnostic reproduced the tier1 obstruction;
the test suite explicitly checks that same failed segment again.
All26 individual root/noncommon certificates pass at256bits.

Every one of the588 scouting seeds has a retained terminal status. Some
Newton sequences leave the declared computational domain or converge to a
candidate outside the box. Those are failed scouts, not deleted data and
not certified missing roots. Completeness comes from the argument principle
and the26 disjoint Rouche discs, not from Newton convergence.

Importantly, the first new root near250 has

    0 < |raw Theta0(b)| < 0.054 < 1/4.

Thus the earlier FC observation that its fourteen raw moduli exceeded1/4
does not persist in these held-out boxes. There was no preregistered lower
alignment floor to preserve. New moduli vary substantially; no asymptotic
approach to1 is inferred.

HA2. The following finite normalized-kernel Bessel ceilings and weighted
partial sums are certified. The approximate sums only aid reading; exact
outward rational intervals and strict rational floors are in the fixture.

| Included boxes | Nodes | Strict Bessel upper bound | Weighted partial sum | Added weighted sum |
|---|---:|---:|---:|---:|
| old32/64/128 | 14 | 2.342 | 0.037285136949 | 0.037285136949 |
| also256 | 22 | 2.396 | 0.038589794408 | 0.001304657459 |
| also512 | 31 | 2.414 | 0.039343940096 | 0.000754145688 |
| also1024 | 40 | 2.420 | 0.039719812007 | 0.000375871911 |

These are partial sums over these six fixed-width windows, not all roots
up to the displayed heights. All old/new and new/new cross terms of the
40-by40 normalized Gram are retained. The decreasing added weighted sums
do not establish convergence, and the slowly increasing finite Gram bounds
do not establish a uniform infinite-family Bessel bound. Conversely, they
do not establish the two cofinal hypotheses needed by LB3. Absolute row
sums can be a poor infinite-family norm bound even when a family is Bessel.

There is also a sampling-design limitation. If an infinite continuation of
width12 windows centered at2^j contained O(j) selected nodes per window,
with0<y<=1 and |raw Theta0|<=1, its selected weighted series would be
bounded by a constant times sum_j j*2^-j and hence converge. This follows
from x>=2^j-6. The local-count hypothesis is not asserted for Xi here;
the elementary conditional observation explains why sparse held-out
windows test local ingredients but are not themselves a proposed divergent
cofinal selection. The forty-node computation makes no infinite assertion.

## 2. Why the finite certificates prove HA1--2

The primitive remains exactly

    xi_R(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    f(z)=xi_R(1/2+i z).

Only the new wrapper's compact domain and declared precision/series caps
are enlarged. The product is analytic on all evaluated rectangles: its
s argument has nonzero imaginary part of absolute value greater than20.
The reflected xi_R(1-s) formula independently encloses the same derivative
jets in each root rectangle. No exponential gauge or new lambda is used.

For a boundary segment midpoint c and half-length h<=1/32, the radius1/4
enclosing square gives M>=sup|f| on that disc. Cauchy's derivative bounds
on the radius1/8 disc give

    sup|R5| <= M_F=M(5!*8^5+lambda64*6!*8^6).

The Taylor coefficient of ordern is exactly

    v_(n+5)*(n+5)!/n! - i lambda64*v_(n+6)*(n+6)!/n!,

where f(c+w)=sum v_j w^j. For N terms the tail is bounded by

    M_F*(8h)^N/(1-8h).

This is the same analytic proof as FC, now using the declaredN=32,40,48.
Each interval image is enlarged to contain the exact Gaussian-rational
endpoint midpoints. A strictly signed coordinate excludes zero in that
convex rectangle. These rectangles give a full homotopy of the actual
boundary image to the rational polygon. Exact signed ray crossing counts
and the argument principle give8,9,9. Sampling or argument unwrapping is
not a substitute for that homotopy. Mesh refinement leaves all endpoints
of the box and the entire coverage domain unchanged.

Each candidate center is an exact Gaussian dyadic of denominator2^180,
with radius r=2^-120. Point residual bound A, derivative lower bound D and
full-square second derivative bound M2 satisfy

    (A+M2*r^2/2)*2^50 < D*r.

Taylor's integral remainder and Rouche give exactly one zero counted
with multiplicity in each disc, hence simplicity. Full-square nonzero
guards for C5,R0,C0,f6,W,R5prime establish local survival and the simple
quotient pole. All real-coordinate intervals of the forty discs are
pairwise disjoint. Each box's root count equals its disjoint certified
disc count. The old fourteen nodes are rebuilt from their literal FC
centers through the equivalent extended source wrapper; their historical boundary census is source-pinned,
not unnecessarily repeated in this packet's producer.

The Hardy convention is boundary dx norm, with inverse kernels

    e_b(t)=sqrt(2y) exp[-(y+i x)t],  ||e_b||=1.

The inner product is conjugate-linear in its first slot. Consequently

    G_ij=2sqrt(y_i*y_j)/(y_i+y_j+i(x_j-x_i)).

Every occurrence of a node uses its full containing rectangle, and every
raw value uses its full-square Theta0 enclosure. Diagonal entries are
exactly1 by normalization. The matrix is Hermitian positive definite for
the actual distinct nodes. Its largest eigenvalue is at most its maximum
absolute row sum. Summing outward entry moduli and rounding the maximum
UP to the next multiple of1/1000 gives each strict ceiling in HA2. This
proves a finite Bessel bound for the normalized kernels themselves; it
does not require component innerness. Membership in the physical reduced
K_B and the LB operator interpretation do require that premise.

Weighted entries are exactly |Theta0(b)|^2*y/x, with x>0 for these nodes.
Outward summation and subtraction of nested partial sums give the displayed
prefix and increment intervals. The independent test route reconstructs
these from rectangular rational intervals, using exact integer-square-root
dyadic bounds for the Gram moduli. Neither eigenvalue scouts nor ordinary
floating-point arithmetic accept the ceilings or weighted floors.

## 3. A source-exact local transport lemma, with unpaid Xi hypotheses

HA3 (critical-jet transport). Let f be analytic on a neighborhood of
|z-t|<=2q, real on a neighborhood of the real t, and put g=f^(5).
Let lambda>0 be a FIXED constant. Suppose

    g'(t)=0,  a=g(t)!=0,  c=g''(t),  a*c<0,
    q=-a/(lambda*c)>0,
    M3 >= sup_(|z-t|<=2q) |g'''(z)|.

The derivative values a,c are real. Define the exact nonnegative quantity

    Delta = 2q/lambda
            +(M3/|c|)*(4q^2/(3lambda)+2q).

If Delta<1/2, then R5=g-i lambda g' has exactly one zero, counted with
multiplicity, in

    |z-(t+i q)| < 2Delta*q.

This zero is simple, lies in the upper half-plane, and has C5!=0.

Proof. Write w=z-t. Taylor's integral remainders on |w|<=2q give

    g(t+w)=a+c*w^2/2+E3, |E3|<=M3*|w|^3/6,
    g'(t+w)=c*w+E2,      |E2|<=M3*|w|^2/2.

Thus R5=L+E with L=a-i lambda c w=-i lambda c(w-i q), and on this disc

    |E| <= 2|c|q^2+M3*(4q^3/3+2lambda q^2)
         = Delta*lambda*|c|*q=Delta*|a|.

On |w-i q|=2Delta*q, |L|=2Delta*|a|>|E|. Delta>0 since q>0,
and2Delta<1 keeps this circle inside |w|<2q and C+. Rouche proves one
simple zero. The same bound gives |g-a|<=Delta|a|<|a| on |w|<=2q,
so g is nonzero there. At an R5 zero, C5=2g is therefore nonzero. QED.

If additionally f' is nonzero and

    sup_(|z-t|<=2q) |f(z)/(lambda*f'(z))| <= eta < 1,

then R0 and C0 are nonzero there and the transported zero satisfies

    |Theta0(b)| >= (1-eta)/(1+eta)>0.

This follows directly from |f +- i lambda f'| and the triangle inequality.
It also proves survival under any common inner divisor, under the inner
premise, by the same local argument as FC. If eta tends to0 along a
sequence satisfying these hypotheses, the corresponding raw modulus tends
to1. No such eta estimate for actual Xi is proved by these finite data.

For interpretation, write kappa^2=-f7(t)/f5(t), so q=1/(lambda*kappa^2).
If on a sequence t->infinity one had kappa comparable to log t and
M3/|f7(t)|=O(log t), then Delta=O(1/log t), giving

    Im b = [1/(lambda*kappa^2)]*(1+O(1/log t)),
    Re b = t+O(1/(log t)^3).

These are a proved conditional consequence of explicit source-jet bounds,
not an asserted one-wave approximation to Xi. If also eta<=eta0<1 and
the real centers had counting lower bound N(T)>=c*T*log T eventually,
and the transported discs were pairwise disjoint, then weighted alignment
on the resulting distinct-node sequence would diverge: its terms are
bounded below by a positive multiple of1/(t*(log t)^2), and Stieltjes
partial summation gives a divergent integral comparable to
integral dt/(t*log t). A uniform kernel Bessel bound would STILL be needed
to apply LB3. The critical-jet, remainder, raw-value and density hypotheses
are all unpaid for an actual cofinal Xi sequence. The held-out finite
windows establish none of their asymptotic quantifiers.

## 4. Arithmetic and source contract

The canonical arithmetic class is MIXED, consisting of
DIRECTED_BALL_ENCLOSURES, EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE.
FLINT real/complex balls round outward. All acceptance inequalities use
exact rational endpoints and strict comparisons; all boundary winding
counts are exact integers. Newton midpoint iterates are scouts only.
Their retained status records neither certify a root nor an excluded
root. The analytic arguments and their quantifiers are written proofs,
not conclusions obtained from numerical coverage.

Seven direct source bindings cover all five FC files at0e3fc9b, the exact
preregistration, and the complete frozen LB proof ata7479e85fdc2a464cdc753021435cfef7a1f3910.
All carry Git-blob and LF-SHA256 checks. FC is historical, not executed:
its authenticated frozen fixture supplies the old fourteen exact dyadic
centers, and this packet's equivalent extended Xi wrapper freshly rebuilds
every old certificate and raw value, demanding literal equality of each
complete historical root record. The frozen FC manifest authenticates all
five BC files and retains their local locks; BC.authenticate closes the
unchanged OA proof/runtime dependencies. No local FC file is required to
match a later metadata-only successor. The source-closure refactor was
checked against the pre-refactor output: all forty source-jet/root fields,
all1600 normalized Gram entries and all weighted/finite-summary fields
are bitwise unchanged (canonical scientific hash235c8ff36e3a6e00c0c86ec59be843d1a3aabe3912a4e5940351e1db5e464060).
The pinned CP counterexample remains inherited through that closure.
The runtime remains CPython3.12.10/python-flint0.9.0/FLINT3.6.0, Windows
AMD64, with the same44 native binary files and OA aggregate hash.

Strict parsing rejects duplicate keys, floats and nonfinite values, byte
counts over24000000, tree nodes over600000, depth over24 and integer
components over4096bits. Public source wrappers enforce their declared
domains, precisions and series caps; matrices are capped at64. Source
text rejects disallowed control characters. Four current artifacts and
the entire canonical payload are sealed. Check mode reconstructs all
three boundaries, all588 scouting outcomes, all40 local certificates and
the complete finite Gram/weighted data from the authenticated primitives.
A resealed but semantically changed derived report is not accepted.

The tests reconstruct the finite weighted sums and Bessel bounds by a
separate Fraction/integer-square-root route, check the retained failed
1024 segments, and exercise source, type, coverage, scope and arithmetic
attacks. This independent finite arithmetic does not constitute a second
special-function implementation. The primitive ball claims remain relative
to the pinned FLINT implementation, not a formal verification of it.

    python -B [-O] -m unittest tests.test_xi_fixed_lambda_heldout_alignment
    python -B [-O] research/exploratory/xi_fixed_lambda_heldout_alignment.py --check
    python -B [-O] research/exploratory/xi_fixed_lambda_heldout_alignment.py --emit
    python -B [-O] research/exploratory/xi_fixed_lambda_heldout_alignment.py --emit-sources

Primary API documentation is inherited literally from FC/BC:
[complex balls](https://python-flint.readthedocs.io/en/latest/acb.html),
[complex series](https://python-flint.readthedocs.io/en/latest/acb_series.html),
[complex matrices](https://python-flint.readthedocs.io/en/latest/acb_mat.html).
No novelty or priority claim is made for the finite matrix/transport tools.
