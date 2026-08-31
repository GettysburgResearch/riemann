# Fixed-lambda Xi boxes and one joint global compression

Status: PROPOSED PROOF-PRODUCING FINITE RESULT; independent review pending.
Authoring base: 7fbcd592042a5cc98c17d0db2fac62f8171267f2.
All frozen science and review records remain unchanged.

## Fixed scope, before any new count or root computation

The source is the actual unrescaled f(z)=Xi(z) and ONE exact constant

    lambda = lambda_64
           = [Re digamma(1/4+32i)/2 - log(pi)/2]^-1.

Set R_k=f^(k)-i lambda f^(k+1), C_k=f^(k)+i lambda f^(k+1),
Theta_k=R_k/C_k. This lambda does not change with z or with the box.
The three prescribed open boxes, in this fixed order, are

    (26,38)+i(0,1), (58,70)+i(0,1), (122,134)+i(0,1).

No endpoint will be moved in response to a zero count or small denominator.
The middle box is the existing BC five-node fixed-source baseline.
No count or purity/alignment threshold is predicted for the two other boxes.

Targets:

1. Certify the complete R5 argument-principle count in each box, including
   all four closed boundary edges. Enclose every interior root separately
   where possible, and record any multiplicity, cancellation, boundary or
   arithmetic obstruction literally. Do not add unreported excluded strips.
2. At certified surviving Theta5 zeros, enclose raw Theta0 using each
   complete root rectangle. Assume component innerness only for the Hardy
   interpretation; do not assume global lambda nonexceptionality.
3. Build the joint finite Hardy Gram with ALL cross-box entries. Use
   H_raw=V_raw G V_raw*, the global common-inner-factor Loewner comparison,
   and exact/rational-ball matrix acceptance. Compare each box and the
   nested first-one, first-two, first-three-box input spans of this SAME
   fixed operator. Never sum separate box traces without orthogonalization.

The global-output projection is P_(U H2), not numerator multiplication.
No Fourier-band, native outer-metric, cofinal, Hilbert--Schmidt-infinity,
parameter-stability or RH conclusion follows from these finite bounds.
Failure of a target will remain visible; no adaptive replacement survey
is authorized by this preregistration.

The preceding scope was committed before the new computations at
e669d257711d8d4a6a0ab7aeb21254fd220f7dc3. Its historical first status line
was "PREREGISTERED BOUNDED SCOPE; no result yet." That exact original blob
is pinned as PREREG; this completed note does not replace its identity.

## 1. Exact result and the important distinction

FC1. For the ONE constant lambda64 just defined, R5 has respectively
3, 5 and 6 zeros in the three prescribed open boxes, counted with complex
multiplicity. R5 is nonzero on every point of all twelve closed boundary
edges, including the real-axis edges. There is no omitted bottom strip.
All fourteen zeros are simple. At each, C5, R0, C0, f6 and
W=f f6-f1 f5 are nonzero. Thus each gives a simple zero of Theta5 and a
simple pole of the actual meromorphic ratio Theta0/Theta5. This is a
statement about companions, not about off-critical zeros of Xi itself.

FC2. Suppose, additionally, the internally reduced Theta0 and Theta5
are inner on the upper half-plane. Write Theta0=Gamma U and Theta5=Gamma B,
where Gamma is their common inner divisor and U,B the reduced components.
No assertion that this hypothesis holds is made here. Nor is it necessary
to know that lambda64 avoids the global exceptional parameter set.
Let E32, E64 and E128 be the spans of the Hardy kernels at the certified
zeros in each box. All these spaces lie in K_B. Let

    E1=E32, E2=E32+E64, E3=E32+E64+E128.

They have dimensions 3, 8 and 14. With P_U the orthogonal projection onto
U H2, the following strict bounds hold. The trace column means
||P_U P_E||_HS^2, and the norm column means ||P_U P_E||.

| Input space E | Dimension | Trace greater than | Norm greater than |
|---|---:|---:|---:|
| E32 | 3 | 1.098 | 0.734 |
| E64 | 5 | 1.551 | 0.816 |
| E128 | 6 | 1.638 | 0.766 |
| E2 | 8 | 2.657 | 0.818 |
| E3 | 14 | 4.298 | 0.819 |

These are finite input compressions of ONE global-output operator. In
particular ||P_U P_KB||>0.819 conditionally, but its Hilbert--Schmidt
finiteness or infiniteness is not decided. All fourteen raw Theta0 moduli
happen to exceed 1/4; that was not a predicted threshold or a general law.

FC3. The input orthogonal increments D2=P_E2-P_E1 and D3=P_E3-P_E2
are projections of ranks 5 and 6. Under the same innerness premise,

    ||P_U D2||_HS^2 > 1.558,    ||P_U D3||_HS^2 > 1.641.

These inequalities are proved by applying the common-factor Loewner
comparison to the increment projections themselves. They are NOT obtained
by subtracting two lower bounds for unknown reduced traces.

The computed raw joint trace is about 4.29863632983787. The sum of the
three raw individual traces is about 4.28859981094460. Their difference
is certified greater than 0.010. Thus adding separate traces does not
give the joint trace. The displayed decimals are explanatory only; every
accepted threshold is an exact rational compared with an outward bound.

## 2. Primitive source, normalization and finite coverage

FC4. The primitive is precisely

    xi_R(s)=s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2,
    f(z)=xi_R(1/2+i z).

There is no exponential rescaling or other gauge change. The fixed lambda
comes from the digamma expression in the preregistration, evaluated as a
positive real ball at 256 bits. The historical BC packet uses lambda32,
lambda64 and lambda128 in its respective boxes. This packet uses only
lambda64 in every root, boundary and matrix calculation. The five middle
box centers and all their source normalizations are unchanged from BC.
The nine centers in the other boxes are new, not reused at the wrong lambda.

The complete boundary evaluator and special-function primitives are the
literal source-pinned BC/OA implementations. For completeness, their
analytic enclosure argument is recorded here. Each box has 416 oriented
segments of length 1/16: 192 bottom, 16 right, 192 top, 16 left, traversed
counterclockwise. At a segment midpoint c take h=1/32, rho=1/8 and R=1/4.
The exact product formula above, evaluated on the enclosing square of
radius R, gives M >= sup_{|z-c|<=R}|f(z)|. All such squares avoid the
singularities of the individual factors in that product: the imaginary
part of s equals Re z>20. The product is analytic on the required discs.

At every w with |w-c|<=rho, Cauchy's derivative estimate on a radius-rho
disc lying in |z-c|<=R gives |f5(w)|<=5! M rho^-5 and
|f6(w)|<=6! M rho^-6. Therefore

    M_F=M(120*8^5+lambda64*720*8^6)

bounds |R5| on that disc. If f(c+z)=sum v_j z^j, the first 32 Taylor
coefficients of R5 are exactly

    v_(n+5) (n+5)!/n! - i lambda64 v_(n+6) (n+6)!/n!, 0<=n<32.

The uniform omitted tail on the segment is at most

    M_F (8h)^32/(1-8h).

Complex ball Horner evaluation and this analytic remainder enclose every
image point of the segment, not merely sampled values. Each endpoint is
also evaluated; its exact Gaussian-rational ball midpoint is a polygon
vertex. Enlarge each image rectangle to contain both corresponding
polygon vertices. Every enlarged rectangle has a strictly positive or
strictly negative real or imaginary coordinate interval. It excludes zero
and is convex, so the actual boundary curve and this polygon are homotopic
in C\{0}, with matching endpoint homotopies. Exact Fraction crossing
counts give winding 3,5,6. The argument principle applies to the entire
R5 and proves the full counts. No floating argument unwrapping is used.

FC5. Each individual root center is an exact Gaussian dyadic with
denominator 2^180, and radius r=2^-120. Its full containing square lies
strictly inside the prescribed box. At the center, let A be an upper bound
for |R5| and D a positive lower bound for |R5'|. On the full square let M2
bound |R5''|=|f7-i lambda64 f8|. The accepted exact inequality is

    (A+M2*r^2/2)*2^50 < D*r.

Taylor's integral remainder and Rouche's theorem compare R5 with its
nonconstant linear term on the circle. There is exactly one zero counted
with multiplicity in each disc; it is simple. The fourteen squares are
pairwise disjoint by their real-coordinate intervals, and their counts
exhaust the boundary counts. Uniform lower bounds for C5,R0,C0,f6,W,R5'
on the full square prove all noncancellation assertions without knowing
the exact root. The directly evaluated and reflected xi_R(1-s) derivative
balls overlap in orders 0 through 8, a secondary implementation control.

The raw Theta0=R0/C0 ball is evaluated on the same full root square, with
lambda held fixed during differentiation. Every occurrence of a root in
the matrix calculations is replaced by its entire square, and every
value by this full-square Theta0 ball. Independent occurrences only widen
the enclosure; no guessed center is substituted for an exact zero.

## 3. Physical Gram and cancellation-safe global comparison

FC6. Use the Fourier convention and boundary dx Hardy norm

    f(x)=(2pi)^(-1/2) integral_0^infinity h(t) exp(i x t) dt.

Take the inner product conjugate-linear in its first slot. A common
positive normalization of all kernels does not affect the compressions;
we use v_b(t)=exp[-(Im b+i Re b)t]. Then

    G_ij=<v_bi,v_bj>=1/(y_i+y_j+i(x_j-x_i)).

For an inner J, M_J* v_b=conj(J(b)) v_b. Consequently, for P_J=M_J M_J*,

    <v_bi,P_J v_bj>=J(b_i) G_ij conj(J(b_j))= (V_J G V_J*)_ij.

This is V G V*, not V* G V, and P_J is not multiplication by J.
The Gram is strictly positive for the distinct upper-half-plane nodes;
equivalently, the Cauchy determinant is

    det G = product_i (2 y_i)^(-1)
            * product_(i<j) |b_i-b_j|^2/|b_i-conj(b_j)|^2 > 0.

The producer also independently evaluates this determinant product and
the ball matrix determinant. Positivity and overlap are required.

FC7. At every certified R5 zero, Theta0 is analytic and nonzero, so
Gamma(b) cannot be zero. Since C5 is nonzero, the simple Theta5 zero
survives as a B zero. Thus v_b lies in K_B. This argument is local and
does not require lambda64 to lie outside the GC exceptional set.

The global ranges satisfy Theta0 H2=Gamma U H2 subset U H2. Hence

    P_U-P_Theta0 >= 0,    H_U-H_raw >= 0,
    H_raw=V_raw G V_raw*.

This remains valid with an unknown common singular inner factor. No
purity theorem is needed for this finite comparison. It is a comparison
of global orthogonal projections. Inserting an arbitrary output band
projection before taking norms need not preserve it: BC includes an exact
two-dimensional noncommuting-projection countercontrol. The source metric
is not replaced with a physical outer-factor metric here.

FC8. Let T map coefficients to sum c_j v_bj in E, so T*T=G and
P_E=T G^-1 T*. Finite-rank cyclicity gives

    ||P_U P_E||_HS^2=tr(G^-1 H_U)>=tr(G^-1 H_raw).

For any nonzero coefficient vector c,

    ||P_U P_E||^2 >= (c* H_U c)/(c* G c)
                     >= (c* H_raw c)/(c* G c).

The producer declares exact Gaussian-integer vectors, independently
encloses numerator and positive denominator, and accepts the rational
norm thresholds only from their resulting outward quotient. Approximate
eigenvectors were used only to select these fixed witnesses, never to
accept an eigenvalue or a norm claim. Matrix inversion, explicit
Gauss--Jordan row elimination, and a separate outward dyadic Fraction
implementation reconstruct the trace and Rayleigh floors.

FC9. The same fourteen nodes and the same fixed lambda define all five
matrices. In particular, E1 subset E2 subset E3 and their dimensions are
3,8,14 by the strict Gram determinants. Nested orthogonal projections
commute, so D_j=P_Ej-P_E(j-1) is an orthogonal projection. Apply the positive
global operator P_U-P_Theta0 to D_j, then take finite-rank trace:

    ||P_U D_j||_HS^2 >= tr(P_Theta0 D_j)
      = tr(G_j^-1 H_raw,j)-tr(G_(j-1)^-1 H_raw,j-1).

The last equality subtracts exact raw traces of nested spaces, not
unrelated raw box traces and not separate lower bounds for reduced
traces. Outward subtraction of their certified intervals gives FC3.
All cross-box entries are retained in each joint Gram. There is no claim
that a positive coupling correction holds for general node/value sets.

## 4. Arithmetic, provenance and reproducibility

The adjacent producer, fixture, manifest and tests are the remaining
four packet files. Six direct frozen bindings comprise all five BC files
at 7fbcd592042a5cc98c17d0db2fac62f8171267f2 and the original preregistration.
Every binding has its Git blob and LF SHA256 checked; all five local BC
copies must match. BC.authenticate verifies its eight direct bindings and
calls OA.authenticate for its six source notes and native runtime files.
The executed OA files are also checked literally by BC. Parent proofs,
fixtures, tests and source manifests are not edited.

The frozen native runtime is CPython 3.12.10, python-flint 0.9.0, FLINT
3.6.0, Windows AMD64. The 44 native .pyd/.dll files have the OA aggregate
SHA256 36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc.
Ball arithmetic uses 256-bit working precision; imported primitives
enforce 192 through 512 bits and their finite rectangular domains. Matrix
orders are capped at 14, coefficient magnitudes at 2048, and exact
rational components at 4096 bits. The inherited strict JSON contract
rejects duplicate keys, floats, nonfinite numbers, excessive depth above
24, more than 300000 nodes, and inputs above 12000000 bytes. Boolean
values are permitted as JSON values but never accepted as integer input
parameters; canonical fresh reconstruction prevents type substitution.

The fixture binds four current artifacts, all sources, the literal scope
contract and a canonical payload SHA256. A resealed derived report is
not accepted unless it equals a fresh primitive reconstruction. Tests
also reconstruct the actual 3,5,6,8,14-dimensional matrices using the
frozen BC test's outward 2^-160 Fraction interval route, which imports no
producer matrix operations. This checks finite arithmetic independently;
it does not independently implement the FLINT special functions. The
checker is proof-qualified relative to that pinned implementation, not a
formal verification of zeta, gamma or digamma.

Run with the source-pinned native Python runtime:

    python -B [-O] -m unittest tests.test_xi_fixed_lambda_joint_box_compression tests.test_xi_companion_box_count_compression tests.test_xi_companion_off_axis_ball_certificates
    python -B [-O] research/exploratory/xi_fixed_lambda_joint_box_compression.py --check
    python -B [-O] research/exploratory/xi_fixed_lambda_joint_box_compression.py --emit
    python -B [-O] research/exploratory/xi_fixed_lambda_joint_box_compression.py --emit-sources

Primary implementation references are inherited literally in the manifest:
[python-flint acb](https://python-flint.readthedocs.io/en/latest/acb.html),
[acb_series](https://python-flint.readthedocs.io/en/latest/acb_series.html)
and [acb_mat](https://python-flint.readthedocs.io/en/latest/acb_mat.html).
The Hardy projection normalization and analytic source dependencies are
the complete BC proof and its exact CP/L106620/L106610 parent passages.

## 5. What this adds, and what remains open

This is a finite source-locked comparison of separated boxes for one
actual Xi companion pair, including certified orthogonal input increments.
It replaces the varying-lambda comparison with a single fixed-source
joint computation, and preserves all noncommon/cancellation distinctions.
It does not establish component innerness, global coprimality at lambda64,
uniform persistence under parameter changes, any complete high-height
census, any band-limited or outer-metric capture bound, or a cofinal floor.
The CP coprime infinite-height finite-capture example remains a decisive
counterexample to inferring physical divergence from infinite heights.
No RH conclusion or priority/novelty claim is made.
