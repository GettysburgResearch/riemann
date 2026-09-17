# SPL26 — a stricter seven-point pressure bound for simple critical-line zeros

Date: 2026-09-14.
Status: **proposed computer-assisted mathematical refinement, pending independent
mathematical and implementation review**. No RH proof, new zero-free region,
formal verification, or world-record priority claim is made.

This paper strengthens a finite inequality in the existing ainta seven-point
method and propagates that improvement through its established zeta interface.
The stability inequality, kernel, and block method are credited to [A], with the
corrected spectral/block derivation in [R]. The analytic inputs are the published
unconditional results of [C], not an RH-strength premise supplied by this packet.
The new local constants, exhaustive certificate and their numerical consequences
are this contribution. General convexity and interval methods are classical.

## 1. Statement and exact constants

Let N(T,2T) count all nontrivial zeta zeros in T<Im(rho)<=2T with multiplicity.
Let S(T,2T) count those which are simple and have Re(rho)=1/2, and let Nd(T,2T)
count distinct zeros, including those off the line.

Define

    H = 3/2 - cot(1/sqrt(2))/sqrt(2),
    p = 1/3433,
    b = 13777/4000000,
    m = 308,
    q = b(m-6) = 2080327/2000000,
    c = 2 sqrt(638660389/616000000) - 1 + 2080327/616000000,
    h = (H - 921/528682)/(1-c/308).

The proposed conclusions are

    liminf S(T,2T)/N(T,2T) >= h > 0.6730308386381655,                 (1)
    liminf Nd(T,2T)/N(T,2T) >= (1+h)/2 > 0.8365154193190827.         (2)

The corresponding ratios with (0,T] in place of (T,2T] satisfy the same lower
bounds. In particular the proportion on the critical line is at least h.
No simplicity assumption about the other zeros occurs.

The existing 280-block value in [R] is
0.673009652279136912..., so the numerical improvement in (1) is
0.000021186359028615... in the proportion. This is a small finite improvement,
not evidence that the method reaches density one or excludes exceptional zeros.

The new finite input is the following inequality for EVERY six nonnegative
real gaps:

    p sum_(i=1)^6 g_i
      + sum_(r=1)^6 [2/(7-r)] sum_(i=1)^(7-r)
          w(g_i+...+g_(i+r-1)) >= b.                              (3)

Here

    K(x)=integral_(-1/2)^(1/2) cos(sqrt(2)t) cos(2pi x t) dt,
    K(0)=sqrt(2)sin(1/sqrt(2)),  k(x)=K(x)/K(0),  w(x)=k(x)^2.     (4)

Section 3 gives a complete continuum cover and primitive contract for (3).
It is not inferred from numerical optimization. Sections 2,4--6 reconstruct the
algebra and all source/limit interfaces needed to deduce (1)--(2).

## 2. Credited stability refinement, reconstructed

For t>=0 put

    Psi(t)=(t-1)^2 when t<=2, and Psi(t)=2t-3 when t>=2;
    Delta(M)=Tr Psi(M) for a positive semidefinite matrix M.

This is a nonnegative convex function with Lipschitz constant 2.

**Lemma [A].** Let V have r columns, each of norm at most one. Put P=VV*,
M=V*V, and suppose Q is Hermitian with at most b0 positive eigenvalues. Then

    ||P+Q||_F^2 >= 4Tr(P+Q)-3r-4b0+Delta(M).                    (5)

Proof. Write Q=Q_+-Q_- with Q_+Q_-=0 and rank Q_+<=b0. Since P,Q_+ are
positive semidefinite,

    ||P+Q||_F^2 >= ||P-Q_-||_F^2+||Q_+||_F^2.

Each positive eigenvalue u of Q_+ obeys u^2>=4u-4, so its term is at least
4Tr Q_+-4b0. Order the eigenvalues v_i of P and n_i of Q_- decreasingly,
padding with zeros in a common dimension. Von Neumann's trace inequality and
nonnegativity of the omitted n_i^2+4n_i give

    ||P-Q_-||_F^2+4Tr Q_- >= sum_(i<=r) [(v_i-n_i)^2+4n_i].

For v>=0 the minimum over n>=0 is v^2 for v<=2 and 4v-4 for v>=2, which
equals 2v-1+Psi(v). Extra zero eigenvalues of V*V contribute zero through
that last combination; thus the formula remains valid when r exceeds the
ambient rank or dimension. Summing and combining yields

    ||P+Q||_F^2 >= 4Tr(P+Q)-2Tr P-r-4b0+Delta(M).

Finally Tr P<=r. This proves (5). This lemma is inherited, not newly claimed.

## 3. The complete computer-assisted proof of (3)

### 3.1 Domain and primitive functions

Since w>=0, (3) follows from the linear term if sum g_i>=b/p. Let G=4000,
and let

    C = ceil(G b/p) = 47297.

Every case with any gap >=C/G is therefore settled. The remaining gaps are
covered by closed cells [i/G,(i+1)/G], 0<=i<C. The negligible excess from the
ceiling is kept in the cover, not omitted.

The generated table has 48016 complete cells and 96033 half-grid points. It is
computed at 160-bit MPFR precision with directed operations. A separate
256-bit run produced byte-identical payload rows (only the precision header
differs). MPFR's correctly rounded transcendental functions are a trusted
numerical primitive. The proof does not call ordinary precision certified.

Here is the exact normalized kernel formula used by make_table.cpp. Put

    a=pi x, q0=1/sqrt(2), c0=q0 cot(q0), D=a^2-1/2,
    N=c0 a sin a-(1/2)cos a.

Then k=N/D, with removable values supplied by (4). Its derivatives are

    N'=(c0+1/2)sin a+c0 a cos a,
    N''=(2c0+1/2)cos a-c0 a sin a,
    k' = pi (N'D-2aN)/D^2,
    k''=pi^2 [N''D^2-2ND-4aN'D+8a^2N]/D^3.                  (6)

Primes on N mean differentiation in a; primes on k mean differentiation in x.
All rational constants in (6) are exact input intervals. Pi and sqrt(1/2)
are outward MPFR intervals. Point divisions are accepted only after the
complete denominator interval is checked not to contain zero. No half-grid
point hits a removable pole in the executed calculation. Whole-cell second
 derivatives are used only for x>=3800/G=0.95, away from the poles.

The kernel k is the Fourier transform of a probability density supported on
[-1/2,1/2]. Therefore |k''(x)|<=pi^2 globally. For each cell midpoint x0 and
radius r0=1/(2G),

    |k(x)-k(x0)| <= |k'(x0)| r0 + pi^2 r0^2/2.

An outward enclosure of this expression gives a valid lower bound

    w(x) >= max(0, lower |k(x0)| - upper error)^2             (7)

on the ENTIRE closed cell. The table's squared lower value is rounded down.
The full-cell enclosure of w''=2(k'^2+k k'') from (6) supplies a lower bound
for the second derivative. Sine and cosine on an interval are enclosed by
correctly rounded evaluation at its left endpoint, widened by the complete
interval width using their unit Lipschitz constants, then intersected with
[-1,1]. This also accounts for intervals crossing extrema.

At every half-grid point the table retains outward enclosures of w and w'.
At x=0 the known values w=1,w'=0 are inserted exactly.

### 3.2 Initial reduction and complete boxes

For one gap, U(g)=p g+w(g)/3 is part of the left side of (3), with every other
term nonnegative. If a cell lower bound for U is >=b, every box containing
that cell in any coordinate is settled. The surviving cell-index components
in the final run are exactly

    [3827,4747], [7264,9268], [10673,45388].

Their sixfold Cartesian products give 729 initial boxes. A box written as
integer pairs (l_i,u_i) denotes the real product
[l_i/G,(u_i+1)/G]. For a span crossing r gaps, its possible values lie in the
closed cells from sum l_i through sum u_i+r-1. That r-1 is mandatory and is
retained by both range-minimum queries.

Range queries outside the table use w>=0. Second-derivative queries outside
the available domain return no convexity certificate. No unavailable bound is
extrapolated.

Each box is settled by one of these complete inequalities:

* its linear pressure alone suffices;
* its linear pressure plus all 21 interval kernel minima suffices;
* a rigorous lower Hessian and midpoint jet supply the lower bound below.

Otherwise a widest index interval is split at its integer midpoint. Its two
closed real children meet at their common boundary and cover the parent.
An unresolved terminal cell is an ERROR, not an acceptance. Search ends only
when the stack is empty.

### 3.3 Stronger quadratic acceptance, not a sampled minimum

For each span choose a binary rational a_span no larger than its weighted
w'' lower bound. Let v_span be its 0/1 incidence vector. The EXACT rational
matrix

    H0=sum_span a_span v_span v_span^T

is a Loewner lower bound for the true Hessian throughout the box. This is
because every coefficient in Hessian-H0 is nonnegative; an arbitrary
entrywise comparison would not suffice.

A fast ordinary LDL screen may reject use of this method but NEVER accepts a
box. Every potential acceptance recomputes an outward binary64 LDL enclosure
of this exact H0 and requires all pivot lower bounds positive. At the box
midpoint c, the complete stored point intervals give F(c) and its gradient g.
Taylor's theorem on the segment inside the convex box gives

    F(c+d)>=F(c)+g^T d+(1/2)d^T H0 d
           >= F(c)-(1/2)g^T H0^(-1)g.                     (8)

The second inequality minimizes over all real d, which only weakens the lower
bound. If H0=LDL^T, outward forward substitution encloses t=L^(-1)g and
sum t_i^2/D_i. An upper bound for that sum makes (8) a rigorous lower bound.
A separate convex-tangent box bound is also available; the larger of two
valid lower bounds is valid. The inverse is finite and all its uncertainty
is included. No eigenvalue solver, fitted stationary point, or trust-region
assumption is used for acceptance.

Every binary64 arithmetic operation participating in a bound is widened by
nextafter toward the required infinity. Products take all four endpoint
products; divisions reject zero intervals. Compilation disables fast-math
and contraction, and execution requires IEC559 53-bit doubles and round-to-nearest.
Integers converted by the accepting search are below 2^53. The explicitly
nonnegative operations may safely retain a zero lower bound.

### 3.4 Complete execution

The final target is the EXACT rational b=13777/4000000 and the pressure is
EXACTLY p=1/3433. The accepting comparison uses an upper double enclosure of b.
Both compiler/precision runs give

    initial boxes          729
    processed nodes        920463
    splits                 459867
    linear leaves          5947
    interval leaves        295184
    convex leaves          159465
    total leaves           460596
    unresolved terminals   0.

Both accounting identities hold: nodes=initial+2*splits and
leaves=initial+splits. A deterministic traversal digest and the complete table
hash are in result.json. Hashes bind an execution; they are not a substitute
for regenerating its primitive table and exhausting its boxes. verify.py does
both in a fresh temporary directory.

This proves (3) under the stated MPFR/binary64/runtime contract. The second
compiler and higher MPFR precision share the same algorithm and library family,
so they are not an independent mathematical proof.

An independent 256-bit outward dyadic Python calculation (using Fraction,
integer square roots, Machin pi and full Taylor remainders) additionally checks
19 selected point rows and 39 selected cell sample points, by the independent
sinc derivative formula. These selected checks do NOT replace the full-cell
proof (6)--(7). The same Python calculation gives a rational gap witness with

    F(g) < 0.003444256.

Thus the infimum for this particular pressure lies between 0.00344425 and
0.003444256. No optimality over other pressures, windows or point counts is
asserted. Failed scouts at more ambitious constants are recorded separately.

## 4. Converting pressure to a spectral defect

For ordered real y_1<=...<=y_m, put

    E_m=2 sum_(i<j) w(y_j-y_i),  span=y_m-y_1.

Sum (3) over the m-6 consecutive seven-point windows. Each pair crossing r
positions occurs in at most 7-r such windows, so its total coefficient is at
most 2. Each gap appears in at most six windows. Nonnegativity of all omitted
pair terms gives

    E_m+6p span >= b(m-6)=q.                               (9)

The exact kernel matrix [k(y_i-y_j)] is positive semidefinite and trace m,
since k is the Fourier transform of a positive normalized density. Its squared
spectral deviation E=Tr(M-I)^2 equals E_m.

For any trace-m positive semidefinite M, set x_i=lambda_i-1. Then x_i>=-1,
sum x_i=0, and

    Delta(M)=E-sum_(x_i>1)(x_i-1)^2.

If E<2, at most one x_i exceeds 1. Cauchy on the other coordinates gives
x_i^2 <= (m-1)E/m. Consequently

    Delta(M)>=phi_m(E),
    phi_m(E)=E,                           E<=m/(m-1),
    phi_m(E)=2sqrt((m-1)E/m)-1+E/m,        m/(m-1)<=E<2.    (10)

If E>=2, then Delta(M)>=2sqrt(2)-1. To check this last assertion: no x_i>1
gives Delta=E>=2; at least two give a sum greater than 2 from those two alone.
For exactly one a>1, if a>=sqrt(2) its contribution 2a-1 suffices. Otherwise
sum_(other) x_i^2>=2-a^2, and 2a-1+2-a^2>=2sqrt(2)-1.

The function phi_m is increasing, and phi_m(E)-E is nonincreasing. Therefore,
if z>=0, E+z>=q, m/(m-1)<q<2 and phi_m(q)<=2sqrt(2)-1, then

    Delta(M)+z>=phi_m(q).                                 (11)

For E>=q use monotonicity or the E>=2 bound. For E<q use z>=q-E and
phi_m(E)-E>=phi_m(q)-q. The stated range holds for m=308 and our q. Its
phi_m(q) is exactly the constant c in Section 1. Equations (9)--(11) give

    Delta(M)+6p span >= c.                                (12)

These spectral steps are the corrected block method already present in [R].
They are reconstructed to avoid importing an ambiguous numerical wrapper.

## 5. The actual zeta interface and its error payments

The following inputs are imported from [C], Theorem D, Lemma 2.2,
Propositions 4.1--4.4 and the prime-side trace evaluation. Their statements are
unconditional results of analytic number theory. This computation does not
formalize those results or independently reprove their prime-side analysis.
It also does not substitute Lamzouri's aggregate scalar inequality for the
extra vector-overlap information required here.

Let ell=log(T/(2pi)), L=ell, D0=sqrt(T), I'=(T-D0,2T+D0]. Use [C]'s
fixed-width tapered window

    phi(u)=cos(sqrt(2)u/ell)^(1/2) rho(L/2-|u|),
    a=(1/L)integral phi^2,
    Ghat=G/(aL^2), Ahat=A/(aL^2), d=floor(LT/(2pi)).

Here rho is the taper, not a zero. The inputs give

    Tr Ghat=N(T,2T)(1+o(1)),
    ||Ghat||_F^2=(2-H+o(1))N(T,2T),
    ||Ghat-Ahat||_trace=O(T^(-1/2)),
    N(I')=N(T,2T)+o(N(T,2T)).                              (13)

The operator norm of the difference is bounded by its trace norm. Hence the
trace and squared Frobenius replacements in (13) have errors o(N): use
||Ghat||_F=O(sqrt(N)) and the complete trace-norm tail. The original source
estimate includes all zeros outside I', not just a bounded zero window.

Separate zeros in I' into s1 simple critical-line points, s2 distinct multiple
critical-line points, and p0 unordered reflected off-line pairs. The source
matrix admits Ahat=P1+Q', where

    P1=VV^T, columns v_rho have norm<=1,
    n_+(Q')<=s2+p0, N(I')>=s1+2s2+2p0.                    (14)

Multiplicities above two only make the last inequality stronger. Using (5),
(13) and (14) gives, before trimming,

    s1 >= H N+Delta(V^TV)-o(N).                            (15)

There is also the distinct-count inequality with the SAME defect:

    Nd(T,2T) >= [(1+H)N+Delta(V^TV)]/2-o(N).              (16)

Indeed (5) gives 3s1+4s2+4p0 >= B+Delta, where
B=4Tr Ahat-||Ahat||^2. Then
4(s1+s2+p0)>=B+Delta+s1>=2B+2Delta-2N(I'), and
Nd(I')>=s1+s2+2p0>=s1+s2+p0. Removing I'\(T,2T] costs o(N).
Equation (16) is not inferred from the simple-zero percentage alone.

Trim normalized distance L^2 from both ends of the sampling grid. In physical
ordinates this removes O(L) at each end and thus O(L^2)=o(N) zeros, by the
classical unit-interval count. For remaining simple points put
x_rho=L(gamma_rho-T)/(2pi). Uniformly on each FIXED bounded separation range,

    <v_rho,v_rho'> = k(x_rho-x_rho')+o(1).                 (17)

For completeness, the full-grid sampling identity in [C] gives the normalized
Fourier transform of phi^2. Rescaling u=Lt gives its L1 limit
cos(sqrt(2)t)1_[-1/2,1/2]; the taper occupies length O(1/L). Its Fourier
transform converges uniformly on fixed compact sets to k. The excluded sampling
grid terms are O(L^-2) for points at distance L^2 from the ends, by the complete
inverse-square transform decay. This proves the use of (17) without an
unjustified global-separation claim.

The actual finite Gram diagonal is 1+o(1), NOT identically 1. Apply (12) to the
exact kernel Gram of each fixed m-point block, and compare to its actual Gram.
Weyl's eigenvalue inequality and the 2-Lipschitz property of Psi give an o(1)
error per block, uniformly when its span is bounded. If its span is at least
c/(6p), its pressure alone pays (12), because Delta>=0. All other blocks lie
in the ONE fixed compact separation interval [0,c/(6p)]. Thus (17) suffices,
and O(N) block errors total o(N).

Finally trace-convexity under pinching gives Delta(full)>=Delta(retained).
Equations (15)--(16) therefore hold with the retained Gram Mcirc and retained
simple count S, at cost o(N). This explicitly pays trace normalization,
endpoints, compact-separation uniformity, and the complete outside-zero tail.

## 6. Averaging blocks and completing the numerical consequence

Partition the retained ordered simple points into blocks of size m in each of
the m possible offsets, dropping only the incomplete blocks. For a fixed offset,
trace convexity under pinching bounds Delta(Mcirc) from below by the sum of its
complete block defects; the incomplete block defects are nonnegative.

Here trace pinching needs only scalar convexity: take an orthonormal eigenbasis
of every compressed block. Its eigenvalues are <u,Mu>, hence convex
combinations of the full eigenvalues. Scalar Jensen applied to Psi and then
summed over that complete orthonormal basis gives the trace inequality.
Operator convexity of Psi is NOT assumed.

Across all offsets there is exactly one block starting at each possible index
1,...,S-m+1. Every gap is counted in at most m-1 block spans. The total normalized
span is at most LT/(2pi)=N+o(N), by Riemann--von Mangoldt. Summing (12), applying
(17) as paid above, and dividing by m yields

    Delta(Mcirc) >= (c/m)S - 6p(m-1)N/m-o(N).              (18)

Using (15) gives

    (1-c/m)S >= [H-6p(m-1)/m]N-o(N).

The denominator is positive, and this is exactly (1). Equation (18), together
with (1), implies Delta(Mcirc)>=(h-H)N-o(N). Substitution in (16) proves (2).
The same reasoning applies at all sufficiently large T. Summing dyadic windows
down to a fixed threshold proves the (0,T] versions, then letting the threshold
increase removes the fixed small-height contribution.

The independent rational calculation in rational_audit.py encloses

    0.673030838638165527 < h < 0.673030838638165528,
    0.836515419319082763 < (1+h)/2 < 0.836515419319082764.

These are outward enclosure endpoints; the strict decimal consequences stated
in Section 1 are slightly weaker. No optimizer or transcendental oracle enters
that scalar calculation. It uses integer square roots and Taylor remainders.

## 7. What has and has not been accomplished

The only new numerical premise of (1)--(2) is (3), now backed by a complete
primitive reconstruction and continuum exhaustion. There is no new unproved
arithmetic upper estimate, no RH assumption and no all-order Ising premise in
this deduction. Published analytic inputs [C] remain imported theorems, not
outputs of the interval checker.

This is a small improvement to a proportion bound. It does not constrain a
possible finite or density-zero exceptional set, does not supply a new
zero-free region, and must not be presented as a route that now completes RH.
Independent review of the code, numerical contract, and source interface is
required before treating the proposed constant as accepted mathematics.

## References and priority boundary

[A] ainta/zeta-simple-zeros, exact commit
040c5e899e658aed7b56a2a87f501798fe10761d, paper/riemann.tex and
src/zeta_simple_zeros/verify_seven.py. MIT-licensed research draft, generated by
GPT-5.6 Sol according to its README. Kernel, pressure/block mechanism and
stability lemma are credited here. The accepting C++ code was newly written;
its interval-subdivision architecture follows the credited method, with the
quadratic lower certificate (8) and changed pressure/target.

[R] GettysburgResearch/riemann at f99d9e3908dde4865377c75d9ca051c1f545bf4f,
reviews/A/supplement/REPORT.md, S01--S02. The corrected 280-block formula and
scope repairs are inherited, not claimed as newly discovered.

[C] Claude, More Than Two Thirds of the Zeros of the Riemann Zeta Function Lie
on the Critical Line, 2026-08-10, official 35-page Anthropic paper,
https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf .
Theorem D, Lemma 2.2 and Propositions 4.1--4.4 are the precise imported
interfaces. The later Alpöge--Furman arXiv:2608.13637 is a related published
version; its bytes and every proof were not separately audited here.

[L] Y. Lamzouri, arXiv:2609.02882, September 2026: relevant literature
calibration. The primary abstract was checked; the PDF was not successfully
retrieved in this pass. Its scalar aggregate theorem is not used in place of
[C]'s normalized vector interface.

[MPFR] GNU MPFR 4.2.2 manual, rounding modes and correctly rounded functions:
https://www.mpfr.org/mpfr-current/mpfr.html .
