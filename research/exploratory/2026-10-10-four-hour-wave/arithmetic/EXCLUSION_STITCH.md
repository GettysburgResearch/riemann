# Global SHARP positivity from exact label-exclusion corrections

Status: **Root-reviewed component deduction; analytic contracts, source
and independent normal/optimized replay accepted.**
The source is literal beta, including both labelled 67 factors. The native
critical power and RH remain open.

**Component theorem A-EP1.** H_m(x)>0 for every real m>=13/10=1.30 and
every real x>=1.

The new tail mechanism is the exact used-label correction (E4), fully
derived in `EXCLUSION_PAIRS.md`. It retains positive removal pairs
beginning at levels 2,4,6. The whole unbounded tail uses marked weighted
moments and a collected Bernstein polynomial, with no infinite negative
three- or five-label majorant. The bounded interval uses the independently
reviewed complete four-level lower bound (F1). The checker also evaluates
the valid exclusion lower bound there and may select its larger directed
margin.

## Complete finite source and coverage

Fix selected product cutoff N=10000000 and prime cap B=N/2=5000000.
There are 348513 ordinary primes through B, last 4999999, plus the extra
67 label. Every label in a selected product at levels 2,3,4,6 is <=B,
so the ordinary and marked prefix engines are complete for these selected
products. Both label indices at 67 are retained. Single-label moments
are selected only through B; the omitted infinite single-label mass is
explicitly bounded using V=P(a)+67^-a and its directed prime-zeta
Möbius tail (P10).

The eleven exact rational power points are

\[
 1.3,1.3002,1.3005,1.301,1.3018,1.303,1.3048,1.3075,
 1.3115,1.3175,1.32.
 \tag{S-E1}
\]

Each consecutive pair defines a closed real power slab. The endpoint
chain is the same complete chain (S-W2), from 1 through 10000000, with
21 consecutive closed intervals. At every right endpoint and lower power,
the checker bounds normalized levels one and three above. Level three is
complete there. At every left endpoint and upper power, it bounds levels
two and four below. Its complete four-level rectangle margin is

\[
 1-O_1+E_2-O_3+(1-O_1/5)E_4.
 \tag{S-E2}
\]

The guard V<3 implies O_1<5. All finite evaluations use Arb at 192 bits,
exact rational powers and the proved binomial enclosures (W2)--(W4).
Monotonicity in the real endpoint and power gives the entire rectangle,
including activation jumps. A valid alternate lower margin uses (E6)
with ordinary and marked selected even moments and the global V upper
bound. The larger of these two directed lower bounds is still a valid
lower bound; the entire resulting ball must be strictly positive.

For each slab, the whole unbounded tail x>=N is certified by (E10).
The numerator has degree at most twelve. Its exact dyadic cap is
ceil(2^40 upper(N^-1/2))/2^40; it contains the full required real z domain.
Every subdivision midpoint is exact because the cap has at most forty
binary fractional places and the allowed subdivision depth is fourteen.
Every entire Bernstein coefficient ball must be positive. Both children
of any subdivision are retained, and failure to certify is an error.

The ten power slabs, 210 bounded rectangles, and ten whole unbounded
polynomial certificates cover all x>=1 and m in [1.30,1.32]. The reviewed
A-WM1 certificate covers every larger m>=1.32. The executed finite guards and root-reviewed analytic and implementation
contracts give A-EP1 as a component deduction.

## Independent controls and rejected reconnaissance

`test_exclusion_moments.py` independently compares every ordinary and
marked moment with direct recursive subsets through product 40000, at
two exponents and seven moment orders, including nonempty six-label
levels. It checks the exact finite elementary identity
D_k=V e_k-(k+1)e_(k+1), the two duplicate-67 pair multiplicities, literal
kernel removal, marked kernel enclosures, a positive polynomial requiring
actual dyadic subdivision, rejection of a negative polynomial, and
invalid selected-level/cutoff guards. All four groups must pass in normal
and optimized Python modes.

Reconnaissance at N=10^7 gave a negative zero-defect exclusion margin
-0.0067112 at m=1.28 and positive margin 0.0270398 at m=1.30. The candidate
9/7 has a positive zero-defect limiting comparison but its finite static
comparison is negative at intermediate endpoints and at N. No 9/7 theorem
is asserted here. A separate exact all-parity Euler-tail comparison at
m=1.30 failed with zero-defect margin -0.0465491. Those failed bounds were
rejected; they supply no positivity claim.

`EXCLUSION_STITCH_EXECUTION.json` binds source hashes and actual normal/
optimized receipts separately from analytic review. Numerical output is
a directed finite certificate for the stated contracts; the infinite
analytic lemmas are not machine-proved.
