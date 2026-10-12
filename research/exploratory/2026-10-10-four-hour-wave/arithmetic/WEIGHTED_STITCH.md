# Global SHARP positivity for every m>=33/25

Status: **Root-reviewed component deduction; analytic contracts, source
and independent normal/optimized replay accepted.** The exact beta source, SHARP kernel,
and two distinct source labels at 67 are preserved. The critical power one
and RH remain open.

**Component theorem A-WM1.** For every real m>=33/25=1.32 and every real
x>=1, H_m(x)>0.

The argument retains levels two and four, bounds levels one and three,
absorbs level five by the removal inequality, and pairs all later levels.
It uses exact finite weighted moments rather than enumerating every
semiprime and quartet kernel separately. A collected degree-twelve
polynomial certifies each whole unbounded tail by directed Bernstein
coefficients. The analytic contracts are fully derived in
`WEIGHTED_MOMENTS.md`, (W1)--(W8).

## 1. Fixed finite inputs and complete source coverage

Fix N=10000000 and B=N/2=5000000. The ordinary prime list through B
contains 348513 primes, last 4999999, plus the extra labelled copy at 67.
Every label in any product of two or more labels <=N is <=B, because
another label is at least two. Thus this finite list is complete for every
level-two, three and four selected product <=N. A single-label moment
is used only through B. Its remaining infinite source is added explicitly
as a positive Euler-tail upper bound when the endpoint exceeds B.

`weighted_moments.py` computes the exact seven moments C_(k,j)(a,t),
j=0,...,6, by a strictly increasing label-index recursion followed by
a last-label prefix subtraction. Source parity and duplicate-label
multiplicities are preserved; no finite census is substituted for an
infinite odd majorant. Moment metadata binds the exponent a=(m+1)/2,
selected product cutoff, and level to the normalization routines.

Infinite odd majorants W1(a) and e3(a) use the convergent prime-zeta
Möbius series with cutoff 80 and its proved entire omitted-tail bound
(P10). The third elementary identity is (F5). All transcendental finite
evaluations use Arb at 192 bits; powers and binomial coefficients have
exact rational inputs. The source, kernel and tail formulas contain no
floating acceptance condition.

## 2. The complete bounded endpoint interval

The exact power points are

\[
 1.32,1.3202,1.3205,1.321,1.3217,1.3228,1.3241,1.3259,
 1.3284,1.3318,1.3365,1.3431,1.3522,1.3652,1.385,1.4.
 \tag{S-W1}
\]

Every consecutive pair defines a closed real power slab. The exact
bounded endpoint chain is

\[
 1,10,20,40,80,160,320,640,1280,2560,5120,10240,
 20480,40960,81920,163840,327680,655360,1310720,
 2621440,5242880,10000000.
 \tag{S-W2}
\]

At every chain endpoint x and fixed power m, the directed binomial
moment bounds (W4) give upper bounds for normalized odd levels one and
three and lower bounds for normalized even levels two and four. All
selected products are active. Level three is complete at these endpoints;
level one is complete when x<=B. For x>B, its omitted upper mass is
W1(a)-C_(1,0)(a,B), explicitly added to the finite selected upper bound.
Each odd bound is also capped by its independent complete Euler majorant.
Each even lower bound is capped below at zero, valid because the selected
level is a positive sum. These directed extrema have exact dyadic
endpoints.

For each power slab [m0,m1] and each endpoint interval [L,U], use odd
upper values at (m0,U) and even lower values at (m1,L). Normalized subset
terms are nondecreasing in x and nonincreasing in m, including activation
jumps; therefore these bound the entire real rectangle. The checker
requires O1<5 and the entire-ball strict inequality

\[
 1-O_1+E_2-O_3+(1-O_1/5)E_4>0.
 \tag{S-W3}
\]

Equation (F1) then proves positive H_m throughout the rectangle. This
is 315 bounded rectangle certificates. Each certificate bounds its entire
continuous interval.

## 3. A polynomial proof for every tail endpoint

For each power slab, retain the same selected moments through N (through
B at level one) and use exact directed upper bounds for the omitted
odd Euler masses. The source removal majorant V<5 absorbs the five-label
term uniformly throughout the slab. Guards also require positive c0 and
c4 in (W5), and positive lower kernel polynomials at the activation
boundary 3/4.

`polynomial_tail.py` collects the numerator polynomial (W7), of degree
at most twelve, with directed coefficient balls. Its positivity is tested
on the full interval 0<=z<=N^-1/2, using a directed upper endpoint for
the cap. Every Bernstein coefficient must have an entirely positive
ball; exact midpoint subdivision is allowed only to cover both halves.
The retained leaves and their strict directed lower bounds bind the
whole interval proof. This proves H_m>0 for every real x>=N throughout
the power slab, without a large-height endpoint scan or an asymptotic
interpolation assumption.

Together, the 15 bounded power slabs, their 315 real rectangles, and their
15 whole-tail polynomial certificates cover every real x>=1 and every
real m in [1.32,1.4]. A-FL1 covers all m>=1.4, giving A-WM1 as a root-reviewed component deduction after every stated
finite guard passed. The infinite analytic contracts remain manually proved.

## 4. Execution and independent controls

`verify_weighted_stitch.py` is the complete acceptance checker. Its
normal and optimized JSON outputs must be byte-identical. Source hashes
bind the two engines, acceptance checker and imported finite arithmetic
helpers. The retained results and `WEIGHTED_STITCH_EXECUTION.json` record
actual runs separately from analytic review status.

`test_weighted_moments.py` supplies four independent control groups:
last-label prefix moments against direct recursive subset sums at three
exponents and seven moment orders; binomial polynomial enclosures against
the literal kernel; the Bernstein basis identity and a positive polynomial
requiring genuine subdivision, with rejection of a negative polynomial;
and exponent, cutoff and convergence-domain rejection guards. Both Python
modes are required to pass the controls.

Directed reconnaissance established that N=10^7 is insufficient for this
particular selected-level tail comparison at m=1.3. Its zero-defect margin
is negative there. No m=1.3 theorem is asserted. The finite cutoff and
power intervals in this certificate remain essential; taking a critical
limit would require an additional native cancellation theorem.
