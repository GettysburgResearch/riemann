# Pass 2: actual mixed inequalities, infinite regions, and an exact failure rate

Status: PROPOSED PROVED COMPONENTS; independent review pending.
The unrestricted inequality and RH remain UNPROVED.
Scope: continuation of PR #790, not a new branch or canonical integration.
Exact parent: bc3c35d8f434949748a2185783bf831d3afd9126.
What was run: 875 exact controls in each interpreter mode, parent controls,
negative-control refusals, and local SHA/Git-blob checks. See VALIDATION.md.
Smallest remaining gap: the subexponential source trace bound (P6) below.

The target remains

    H_(a,b)(v)=sum_(j=0)^b (-1)^j binom(b,j)p_(a+j+1)^*(v)>=0,
    p_n^*(v)=(-1)^(n-1)n[y^n]log[X(v(1+y))/X(v)].

All statements below concern the ACTUAL invariant xi, except the explicitly
identified synthetic polynomial control. Read [PROOF.md](PROOF.md).

## What this continuation proves

**P1: twenty-two formerly open mixed layers, with unbounded first index
and every scale.** For all a>=0, v>0, and 0<=b<=22,

    H_(a,b)(v)>(1-C_b)196^b v^(a+1)/(v+226)^(a+b+1)>0,
    C_b=20000(2500/49)^b(60/163)^97<3/5.

For b<=20, C_b<1/4096. This follows from the all-time strengthening

    (-1)^b S^(b)(t)>(1-C_b)196^b exp(-226t),       every t>0.

It uses the parent's V100 and Z14/15 and pays the entire unverified tail.
No derivative or zero grid is extrapolated. Claim ASTRA-MD-01.

**P2: an unbounded small-ratio cone at the fixed scale v=1.**

    a>=2, 0<=b<=100a
       ==> H_(a,b)(1)>(1/2)227^(-a-1)(196/197)^b.

A separate exact phase rectangle proves positivity whenever
`a+1<=100` and `bv<=100(10000+v)`. Claim ASTRA-MD-02.

**P3: the other unbounded direction.** At the fixed scale v=1,

    0<=a<=19, every b>=0: H_(a,b)(1)>0;
    every a>=0, b>=max(10^6,8000(a+1)^3): H_(a,b)(1)>0.

In the large-b regimes an explicit bound is

    H_(a,b)(1)>(1/4)((a+1)/(15b))^(a+1).

This adds one classical input: a weakened Trudgian zero-count estimate,
from which the proof derives existence of a zero in every [T,2T], T>=100.
Those high zeros need NOT be on the critical line. Claim ASTRA-MD-03.

**P4: the exact exponential obstruction.** Set

    V_N(v)=sum_(a=0)^N binom(N,a)|H_(a,N-a)(v)|.

Then, retaining multiplicities and every invariant zero A=rho(1-rho),

    limsup V_N(v)^(1/N)=sup_A (v+|A|)/|v+A|.

The right side equals one exactly under RH. Any nonreal invariant zero
forces exponential growth of the NEGATIVE binomial-row mass along a
subsequence. No zero simplicity or linear-independence assumption is used.
This supplies an exact defect size, not a bound proving it vanishes.
Claim ASTRA-MD-04.

**P5: a source formula and the narrow unresolved angular region.** For

    Q_N(z)=sum_(a=0)^N binom(N,a)H_(a,N-a)(v)z^a,

    Q_N(z)=integral_0^infinity exp(-x)S(x/v)L_N((1-z)x)dx,
    sum_(N>=0)Q_N(z)t^N = v/(1-t) h(v(1-zt)/(1-t)).

The manuscript also gives the literal Euler/gamma derivative formula for
H, with a finite Laurent-polynomial recurrence for each prime kernel.
Actual prime terms already have both signs at the first mixed derivative.
V100 bounds Q_N uniformly outside the arc
`|arg z|<2 arctan(1/100)`; the punctured arc is not controlled.
These are exact formulas and scope statements, not a source sign theorem.

**P6: the explicit remaining theorem.** At ONE fixed v>0 prove

    for every epsilon>0, sup_(|z|=1)|Q_N(z)|
                         <=C_(epsilon,v) exp(epsilon N), all N>=0.

Then P4 proves RH and therefore every H_(a,b)>=0. This subexponential bound
is RH-equivalent. It is not proved by P1--P5. The manuscript records why
positive heat, termwise prime signs, and a uniform Euler-safe continuation
do not currently give it.

## What is not claimed

The expanding intermediate region remains infinite. At v=1 it is contained
in `a>=20, 100a<b<max(10^6,8000(a+1)^3)`; the phase rectangle pays additional
cells. There is no claim that the remaining region can be checked finitely,
that a small positive exponential rate is zero, or that the synthetic
countermodel is actual zeta. External novelty has not been established.

No main, predecessor, formal-spine, or canonical file is changed. All twelve
files of the original PR790 checkpoint are preserved byte-for-byte.

## Review and replay

1. PROOF.md Sections 1--3: normalization, weighted tail, all-time derivatives.
2. Sections 4--6: cone, explicit imported count boundary, whole columns/wedge.
3. Sections 7--10: meromorphic noncancellation, exact rate, source endpoint.
4. REVIEW.md: adversarial audit priorities and failed full-proof shortcuts.

From this directory:

    python verify.py --check checks.json
    python -O verify.py --check checks.json
    sha256sum -c SHA256SUMS

The checker proves the stated finite rational identities and comparisons,
not the analytic theorems or the imported zero counts. Publication-specific
commit metadata is recorded in the PR comment, avoiding a self-hash cycle.
