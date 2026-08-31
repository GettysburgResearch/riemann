# One fixed Xi calibration: certified shrinking physical-band floors

Status: proposed finite source-bound theorem and directed-ball certificate.
Sections1-4 were frozen before new arithmetic at design
`f7cc9bea51c6ab0b969acdc6e279ed09f608acac`; this final note adds proof and
outcomes without changing that panel. Independent review is still required.
Base: HA `64165b8c805d182dbc43f2e5855e64a86cf1aaf9`.
Analytic parent: LB `a7479e85fdc2a464cdc753021435cfef7a1f3910`.
No parent scientific file is modified. This is finite physical-band
transport, not another zero census, cofinal result, or RH statement.

## 1. Literal operator and source scope

Use ONE fixed constant throughout:

    lambda_(64)=[Re psi(1/4+32i)/2-log(pi)/2]^-1.

The subscript denotes the freezing anchor. It is NOT the numerical value64
and is not changed at other node or calibration heights. Let
f(z)=xi_R(1/2+iz), R_k=f^(k)-i lambda_(64) f^(k+1),
C_k=f^(k)+i lambda_(64) f^(k+1), and raw Theta_k=R_k/C_k.

For physical interpretation ASSUME Theta0 and Theta5 are inner in C+,
with a common inner divisor Gamma and reduced factors U,B:
Theta0=Gamma U,Theta5=Gamma B. This premise remains unpaid. The forty
HA R5 roots are simple and locally noncommon, so survive as B zeros
under that premise. In boundary-dx Hardy normalization write

    e_b(t)=sqrt(2 Im b) exp[-(Im b+i Re b)t], ||e_b||=1,
    T_(D,E)=Pi_[0,D] P_(U H2) P_E.

For a surviving b=x+iy and h>0, the accepted LB theorem gives

    ||Pi_[0,D] P_(U H2) e_b|| >= l_D(b,h),
    l_D(b,h)=|raw Theta0(b)|
       [2sqrt(hy)|raw Theta0(ih)|/sqrt((h+y)^2+x^2)-exp(-hD)]_+
                                 /sqrt(1-exp(-2hD)).

Only the TWO scalar inequalities |U(b)|>=|raw Theta0(b)| and
|U(ih)|>=|raw Theta0(ih)| are used. No band-Loewner implication is
allowed. This is physical projection P_(UH2), not multiplication alone.

## 2. Full fixed numerical panel and all failures

Inherit ALL40 HA root rectangles, raw values and the complete40x40
normalized Gram as accepted source certificates; do NOT claim to rerun
their boundary census, scouting or local root construction. Authenticate
the entire frozen parent fixtures, payload/artifact hashes and recursive
source closure. Never substitute a midpoint for a containing root rectangle.

The complete new panel is exactly

    D in{1/256,1/1024,1/4096},
    h in{64,128,256,512,1024,2048,4096,8192,16384,32768,65536},
    all40 HA nodes, in their frozen order.

Retain all40*3*11=1320 witness cells, including every zero floor from an
unresolved/nonpositive bracket. The best proved h may be selected for
each fixed node and D only from this grid. No node, width or h is added,
moved or removed after seeing the answer. No positive floor is predicted.

Freshly evaluate the11 axis values with256-bit pinned FLINT balls via

    sigma=1/2+h,
    ell=1/sigma+1/(sigma-1)-log(pi)/2+psi(sigma/2)/2
                                             +zeta'(sigma)/zeta(sigma),
    raw Theta0(ih)=(1-lambda_(64) ell)/(1+lambda_(64) ell).

Require finite denominators and compare against LB's existing anchor64
axis certificates. The direct reflected Xi/gamma-product ratio is checked
at h=64,256,1024 as a second route. There is no fresh lambda(h).
Unresolved ball statements fail closed, with no precision or grid tuning.
Tail handling retains LB's conservative outward widening below2^-512.

For each D use the four frozen prefixes14,22,31,40, with EXACT inherited
strict Gram/Bessel ceilings2.342,2.396,2.414,2.420 respectively. Report

    ||T_(D,E_prefix)||_HS^2 >= sum_(j in prefix) best_l_j^2/C_prefix,
    ||T_(D,E_prefix)|| >= max_(j in prefix) best_l_j.

The same lower bounds apply to input K_B. These are12 prefix/width
cells, not weighted alignment sums mislabeled as physical traces.
Keep exact rational lower endpoints, and report strict decimal-rational
floors with12 places for norm and16 places for squared HS. A zero floor
remains0. Arithmetic is MIXED directed balls/exact rational/complete
finite coverage; all rounding is outward or deliberately downward.

## 3. Separate finite Carleson-box geometry control

Sort the40 disjoint certified real-coordinate intervals by position.
Check ALL39 adjacent conditions using full intervals:

    lower(x_(j+1))-upper(x_j) >= upper(y_j)+upper(y_(j+1)).

Retain every comparison and any failure. If they all hold, prove the
finite measure sum_j y_j delta_(x_j,y_j) has Carleson-box constant<=1:
any box containing at least two selected points has span at least the
sum of their endpoint heights plus twice the interior heights, hence at
least their total height; a singleton uses its own height<=box width.
This controls all boxes, not merely a sampled box grid.

Also check for EACH of the40 full x intervals that its integer floor
is unambiguous, and report occupancy and a certified c_cell upper bound
for every occupied half-open unit cell. If all relevant gaps pass, use1;
otherwise retain the elementary occupancy ceiling and the failed tests.
If unit membership is unresolved, explicitly mark it unresolved rather
than choosing the center's cell. This Carleson-box constant is NOT the
normalized Gram norm. It must NEVER replace C_prefix in the physical
HS calculation. No infinite-family Bessel statement follows.

## 4. Release contract

The new five-file packet will bind HA5 and LB5, this design, all relevant
recursive FC/BC/OA source records, the pinned44-native-file runtime and
its own four artifacts plus complete payload. Inherited certified values
are distinguished from newly evaluated axis/band arithmetic. No inherited
19MB boundary producer is repeated or advertised as fresh in this packet.
Full coverage, strict bool/int/rational/byte/work caps, source corruption,
resealed report attacks, normal/-O replay and independent review are required.
No actual innerness, global divisor capture, outer-metric transport,
infinite Bessel bound, weighted divergence, HS infinity or RH is concluded.

## 5. Proof of the physical finite-frame theorem

PB1. Let the conditional inner premise in section1 hold, and let E be the
span of any one of the four literal HA prefixes. All nodes are distinct
simple denominator zeros and the inherited nonzero guards show R0 is
nonzero there. Thus they survive division by the common Gamma, and their
unit Hardy kernels e_b belong to K_B. No new arithmetic identity or
assumption of free source coefficients enters this statement.

For any inner U, the normalized reproducing-kernel identity is

    P_(UH2)e_b=conjugate(U(b)) U e_b.

Use the isometric Laplace realization on L2(0,infinity). Evaluation at ih
gives the modulus of the integral of exp(-ht) Ue_b(t) as

    |U(ih)| sqrt(2y)/sqrt((h+y)^2+x^2).

Split that integral at D. Cauchy-Schwarz on the two pieces, together with
||Ue_b||=1, gives

    sqrt(2h)|Laplace(Ue_b)(h)|
       <= sqrt(1-exp(-2hD)) ||Pi_[0,D]Ue_b||+exp(-hD).

Rearrange and multiply by |U(b)|. Since |Gamma|<=1 inside C+,
|U(b)|>=|rawTheta0(b)| and |U(ih)|>=|rawTheta0(ih)|. The resulting
quantity is monotone in both nonnegative moduli, yielding exactly l_D
in section1. This is the proof of LB1-2 at the pinned LB source, repeated
to specify the operator, normalization and scalar-only substitutions.
It does NOT assert an order relation between band-compressed operators.

PB2. Write F: C^N -> E for the synthesis map of these unit kernels.
The inherited complete normalized Gram certificate says

    ||F||^2=||F*F||<C_prefix, hence FF*<=C_prefix P_E.

For S=Pi_[0,D]P_(UH2), finite-dimensional trace cyclicity and positivity
give sum_j ||S e_bj||^2 <= C_prefix ||S P_E||_HS^2. Apply PB1 for
each j, choosing only the best h in the preregistered finite set. The
operator-norm lower bound follows because every e_bj is a unit vector
in E. This proves the two inequalities of section2. Since E is a
subspace of K_B, enlarging the input space to K_B cannot decrease norm
or squared Hilbert-Schmidt norm (the latter may be infinite). No finite
lower bound here proves that it is infinite.

PB3. Every directed-ball input used in PB1 contains the exact value:
the HA root's disk is contained in its center-plus/minus-radius rectangle;
its raw value ball is already proved for that disk. The fresh axis ball
comes from the reflected completed Xi logarithmic derivative at
sigma=h+1/2>1. The functional equation and differentiation give the
formula in section2, with the SAME fixed lambda_(64). All denominators
are proved positive. Ball arithmetic is outward; an unresolved positive
part is safely replaced by zero. A positive reported endpoint is at
most the exact PB1 value. Squaring nonnegative endpoints and dividing
by the exact inherited C_prefix preserves a lower bound. Final decimal
floors are strictly below each positive rational endpoint.

## 6. Complete preregistered outcomes

The following decimals are EXACT terminating rational strict floors,
not rounded midpoint estimates. Each norm bound holds already for the
14-node prefix, and hence for each larger prefix and for K_B, subject
to the same unpaid inner premise:

| D | strict norm floor | positive cells | zero-floor cells |
|---|---:|---:|---:|
| 1/256 | 0.010246276673 | 242 | 198 |
| 1/1024 | 0.006033839168 | 160 | 280 |
| 1/4096 | 0.003284576367 | 80 | 360 |

Each of the40 nodes has a positive best witness at EVERY one of the
three widths. All838 zero-floor cells remain in the fixture; none was
dropped. There are1320 cells, exactly as preregistered. The full lower
endpoint and the Laplace, tail, bracket, denominator and raw-modulus
enclosures are retained for every cell.

| prefix | squared HS floor, D=1/256 | D=1/1024 | D=1/4096 |
|---:|---:|---:|---:|
| 14 | 0.0002763434053678 | 0.0000955538803072 | 0.0000280819286077 |
| 22 | 0.0003161629493892 | 0.0001093530249566 | 0.0000320300089711 |
| 31 | 0.0003635507425742 | 0.0001264211670816 | 0.0000368694134846 |
| 40 | 0.0004038295912204 | 0.0001432989644834 | 0.0000416271711265 |

PB4. ALL39 adjacent full-rectangle comparisons pass, including gaps
between the widely separated boxes; all40 full x-intervals lie strictly
inside unambiguous, pairwise distinct unit cells. For any horizontal
interval J of length L consider the selected nodes in its Carleson box
J x (0,L]. A singleton contributes at most L. For selected indices
i1<...<iq, q>=2, summing all consecutive original gap inequalities
between i1 and iq gives

    x_iq-x_i1 >= y_i1+y_iq+2 sum_(i1<j<iq)y_j
               >= sum_(j selected)y_j.

The actual span is at most L. Thus every box satisfies mu(box)<=L.
This proves a finite global Carleson-box constant<=1, not just the
unit-cell claim. It uses every original intermediate height, so omitted
points of a particular box cause no gap in the argument. The unit-cell
costs are also<=1. Neither conclusion replaces the normalized Gram
ceilings in PB2, nor asserts an infinite source is Bessel.

## 7. Certificate inheritance, arithmetic and audit boundary

The immutable source manifest lists35 complete Git/LF records: HA5,
LB5, the frozen preregistration and24 recursive FC/BC/OA or native
source records. Every frozen source byte string is checked against its
Git blob identity and LF-normalized SHA256. Child manifests must close
inside this list. The HA and LB full fixtures are authenticated including
their payload seals, all four artifact seals and the pinned runtime.
Only unchanged, hash-locked BC/OA helper code executes locally. The HA
19.7MB root/Gram certificate is inherited, not reproduced or freshly
certified by this producer. This is a theorem-dependency boundary, not
an assertion that hashes themselves prove root existence.

The pinned runtime is CPython3.12.10, python-flint0.9.0, FLINT3.6.0,
WindowsAMD64 with44 authenticated native binaries and aggregate
`36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc`.
Fresh computations use256-bit outward balls. Axis ell is formed before
endpoint export: zeta' at a very large positive sigma is never silently
zeroed or exported as a standalone huge-denominator rational. The
reported ell and Theta balls remain within the rational resource cap.

Arithmetic is MIXED: DIRECTED_BALL_ENCLOSURES, EXACT_RATIONAL and
CERTIFIED_INTEGER_COVERAGE. Rounding is pinned-FLINT outward rounding,
then exact rational comparisons and downward strict decimal floors.
The producer is not a machine certificate of the analytic inner premise,
the Laplace theorem, inherited root proofs, or any infinite quantifier.

Limits are explicit: source bytes24MB, report bytes8MB, integer4096bits,
JSON600000nodes/depth24, work10000units, fixed40nodes/1320cells/256bits.
The32 tests include independent exact prefix aggregation, full-interval
gap and membership checks, fixed-grid and bool/int/rational/cap guards,
runtime/source/artifact authentication and fresh fully resealed report
attacks. Negative controls force failure of the gap certificate and
unresolved unit membership; neither may be disguised as a positive
geometric statement. Normal and optimized Python must both pass.

This extends the frozen LB physical estimate to ALL40 HA nodes with
ONE lambda_(64) and two additional shrinking widths. It is a finite,
conditional physical lower bound, not a new zero-census method, proof
of actual innerness, cofinal capture, physical free energy, or RH.
