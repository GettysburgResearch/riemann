# Theta degree 20 and complete native cancellation components

**Status: proposed standalone mathematical components, with complete proofs,
directed finite certificates, and separately authored reviews. RH remains open.**

This packet continues #988 at the exact parent
`86c156baa3f10296a26e066f5f4d276776b79c27`. It adds three concrete results.
All inherited files and integrated scientific status retain their identities.

## Results and what they change

| Component | Result established here | Remaining full-proof problem |
|---|---|---|
| [Theta realization](theta/PROOF20.md) | A connected 305-vertex ferromagnetic tree matches all original theta moments through degree 20 exactly. | Construct admissible real-zero laws at unbounded matching orders. |
| [Native denominator bounds](native/PROOF.md) | Control low reduced denominators from every old product, automatically remove both balances at cofinal crossings, and pay every square denominator and a growing small-core sector at subpower energy cost. | Bound the retained large-denominator, large-squarefree-core amplitude with a subquadratic power of the old native energy. |
| [Fixed-shift bridge](critical/PROOF.md) and [signed arithmetic](critical/ARITHMETIC.md) | One fixed shift has two-sided bounded critical norms with the unchanged native Gaussian. Fixed additive bands have a signed asymptotic, and the complete infinite divisibility sector has a certified negative logarithmic coefficient. | Prove the critical one-sided upper bound for the complete nondivisibility contribution. |

The statements are unconditional at their displayed scopes, except for the
explicit RH-assuming necessity directions and the explicitly open sufficient
premises. Tao's logarithmic two-point theorem is an identified external input
to the fixed-band result. Classical Lee--Yang is the real-zero input for the
finite Ising law. Neither a finite certificate nor these imported theorems
prove the missing global estimates.

## 1. The actual next theta target is reached

The new graph has 256 single-spin components and 24 unequal dimers, joined
through one zero-weight hub. It has 305 vertices, 304 observed spins, and
304 strictly positive finite couplings. Its observable Y has support inside
(-11,11), variance 1, and

    E Y^(2r) = E T_*^(2r),  1<=r<=10;
    E Y^(2r+1) = 0.

Here T_* is the variance-one normalization of the original, undeformed theta
density. Multiplying only the observable weights by sqrt(v), with v the
original variance, gives the unstandardized moment equalities.

The accepted model is an interior ferromagnet with 10^-11<J_e<3. A rational
center and a ten-coordinate cube of radius 10^-30 give a full-source Banach
certificate with center displacement below 1.561e-39 and contraction below
1.371e-10. The checker reconstructs the infinite theta source through order
20 with all Taylor, time and index tails. The exact receipt carries the
rational bounds; these decimals are explanatory.

The successful search changed the graph architecture: an observed sign can
be split into an almost-aligned unequal dimer; at the independent-dimer
boundary it can be decomposed into two signs and split again. The two boundary
distribution identities are exact. Only the final interior model is certified;
the exploratory continuation is not used as a proof or an all-order rule.

This closes the specific degree-20 target left open by #981, #988 and #992.
The #981 compactness consumer already handles convergence once cofinal moment
feasibility is established. A separate uniform graph-size, coupling or inverse-
Jacobian bound is not required by that consumer. Feasibility at unbounded
orders remains the missing theorem.

## 2. A smaller native arithmetic target

Set g_Y(n)=mu(n)1_(n<=Y), z_Y=g_Y*g_Y and

    C_Y(q)=sum_(q|d,d<=Y^2) z_Y(d)/d.

Every old product is included in this coefficient, including d greater than
the current output k. The exact Ramanujan modes are

    S_q(x)=sum_(n<=x)c_q(n)/n+Lambda(q),  q>=2.

For 1/2<rho<2/3, removing q<=X^rho on each output annulus has complete
squared error O_rho(Y^(-(2-3rho))(1+log Y)^4) throughout the strict square
step Y<k<(Y+1)^2. This removes reduced-denominator contributions that #988's
product cutoff retained. The proof uses the actual masked reciprocal sums
and the bound sum_(q<=Q)q^2|C_Y(q)|^2<=32Q(1+log Q)^3.

At an unbounded sequence of native sign crossings, |m(Y)|<=1/Y. The second
logarithmic balance tends to zero by PNT alone. Thus both balance coordinates
are paid without an additional balance conjecture or a crossing-gap estimate.

There is also a whole large-denominator result. Write a cubefree q uniquely
as r^2s with r,s coprime and squarefree. Uniformly for arbitrary measurable
per-q multipliers bounded by 1, the complete square sector has squared L2 norm
at most 27 H_Y^2. The entire sector with squarefree core s<=S has squared norm
at most

    144 S H_Y^2 H_S^6.

The norms include coherent cross terms. Since the multiplier may depend on
the output annulus, these bounds remove the sector in the actual native
decomposition without an extra factor for the number of annuli. Any schedule
log S=o(log Y) costs only subpower energy. The error after this additional
removal is subpower; it is no longer asserted to vanish.

The retained object is explicit: q>X^rho and core(q)>S(Y), with the original
C_Y(q), centering and physical windows. A Jordan-polynomial Mellin identity
realizes its exact energy as a sum of full frequency norms. No sampling
approximation or artificial sharp frequency cutoff is inserted.

Using the independently reconstructed #848 all-prefix energy-growth theorem,
the remaining sufficient estimate is

    ||Vrough_(Y,rho,S(Y))||_2^2
       <=Y^o(1)(1+F_Y)^(2-delta),

for some fixed 0<delta<1 along an unbounded sequence of native crossings.
That estimate is open. The all-prefix exponent theorem, not any assumed
density of crossings, is why such a sequence would suffice for RH.

## 3. Actual signed arithmetic on one fixed member

For the unchanged Gaussian Mobius source A and the h=1 deformation

    a(n)=n^(-1) product_(p|n)(1-p),
    S(X)=sum_n a(n) W_c(n/X),

the all-past critical root norms satisfy, for every horizon and every
1<=p<=infinity,

    N_p(S;T)<=zeta(3/2) N_p(A;T),
    N_p(A;T)<=zeta(3/2)/zeta(3) N_p(S;T).

The complete continuum correction also has finite critical norm. The theorem
extends to each fixed number field and every h>1/2 at its stated constants.
A separate zero-propagation argument shows that any legal single fixed h>0
gives a qualitative field-RH criterion: an isolated shifted-numerator zero
cannot cancel an entire forward chain of denominator zeros.

For ordinary zeta, the full finite-horizon quadratic kernel is explicit.
Its diagonal is C_c C_a log T+O(1), where

    C_a=product_p(1-3/(p^2+p+1))>0.

Tao's logarithmic correlation theorem pays every fixed additive band.
More unusually, the COMPLETE infinite set of pairs comparable by divisibility
has asymptotic C_c C_a L_div log T+o(log T), where

    beta(p^j)=-(p^2-1)/(p^j(p+2)),
    L_div=1+2 sum_(r>=2) beta(r)r^(-1/2)exp(-log(r)^2/8).

Two different directed implementations include the full omitted tail. The
second proves the strict bound -9/5<L_div<-17/10. The divisibility sector
therefore contributes negatively; the remaining signed sector must compensate.
This establishes an actual infinite signed contribution, without assuming that
an incomplete Gram sector is positive.

The full primitive-ratio double series cannot be summed by the same argument:
its absolute limiting coefficients diverge on comparable prime ratios. The
finite-horizon Gaussian CDF factor remains essential. The needed one-sided
upper estimate for the nondivisibility sector is still open.

## Reproduce and review

Run from this packet directory with Python 3.12 and its standard library:

```sh
python verify_packet.py --replay
```

The runner authenticates the complete manifest, runs the full theta source
and contraction, replays each finite arithmetic check in ordinary and optimized
Python, compares reports, and executes the specified negative controls. The
root's independent theta check constructs the complete generating product and
its derivative directly, agreeing with every raw order 0--20 and all 100
center-Jacobian entries. It does not reuse the author's cumulant recurrence
to construct those expected values. The second divisibility checker uses
different logarithm and exponential primitives.

See [VALIDATION.md](VALIDATION.md) for the exact executed coverage and limits,
[SOURCES.md](SOURCES.md) for frozen dependencies and concurrent PRs, and
[REVIEW.md](REVIEW.md) for separately authored, hash-bound reviews. No external
human referee, Lean proof, repository-wide build, remote CI or integrated
acceptance is claimed. The contribution is these concrete components and
certificates, with the full-proof estimates still explicitly identified.
