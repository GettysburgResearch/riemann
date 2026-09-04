# Review contract and retained full-proof attempt

Status: author proof pass and author self-audit only. No independent referee
or formal-kernel acceptance is claimed. RH remains unproved.

## The hypothesis audit

The parent's positive heat theorem was reread in full. Its V100 statement
is a finite ZERO-LOCATION input, not just the existence of many line zeros.
The selected zero between 14 and 15 gives 196<A_0<226, not a census and not
a claim of lowest-zero status. The Jensen count, tail integration,
reflection-orbit convention, and h versus 2h normalization were retained.
No error requiring a change to the parent's heat proof was identified in
this pass. This is not an independent review verdict.

Only the opposite-direction column/wedge theorem uses the extra
Trudgian input. Its exact weakened statement, version discrepancy, pages,
and endpoint convention are stated in PROOF.md Section 5. The result used
is merely a dyadic reservoir of zeros of unrestricted real part.

## Claims and the most important checks

ASTRA-MD-01: The phase k arg A-t Im A is a DIFFERENCE of quantities of the
same sign. Its bound is a maximum, not their sum. Check the weighted-tail
monotonicity condition before the Stieltjes integration; dropping the -2k
term is an upper bound. The integer incomplete-gamma bound must remain
uniform in the selected k. Recheck C22<3/5 and C20<1/4096 exactly.

ASTRA-MD-02: The selected positive term is only a lower bound; other
verified terms must not be counted negatively. The unknown-tail absolute
bound requires a>=1, and the displayed uniform cone requires a>=2.
For the phase rectangle distinguish arg A from arg(A+v).

ASTRA-MD-03: The positive high zero may be off the line. Check that
L=sqrt(b/n)>=T=b^(1/3), so it lies in the proved positive-phase region.
The only possible negative interval is 100<gamma<T. Its amplitude bound
is increasing on that interval only when .99T>=n. Both theorem regions
pay that condition. There is no numerical extrapolation in T or n.
The decreasing comparison evaluated at 20n is scalar algebra, not an
application of a zero-count theorem below height 100.

ASTRA-MD-04: The exact rate proof needs normal meromorphic convergence on
compact subsets of |t|<1, the attainment of a rate >1, injectivity of the
map A->1-k_A+k_A z when z!=1, and nonzero multiplicity-weighted residues.
These prevent cancellation by other zeros. At rate one use actual
triangle equality and Re A>0. Do not infer the conclusion merely from an
upper bound close to one. Sum k_A is real/positive but sum |k_A| is the
constant used in the unconditional norm upper bound.

Source endpoint: The generating identity is initially local. Its Mobius
parameter is not always in the Euler-safe half-plane when |t|<1. The
1/u term is killed in the mixed derivative only for b>=1. The prime
series may be differentiated at every FIXED order on a positive-u compact
set; no uniform-in-order estimate is supplied by that fact.

## Attempts to fill the remaining region

1. Extend the all-time heat proof to every derivative order by moving the
verified height with the order. This is NOT a proof: finite V100 would be
replaced by an unproved family of zero-location statements. Its explicit
error constants and phase conditions cease to supply a bound at arbitrary
order. The completed proof stops at its declared k=22 range.

2. Use positivity of S inside the signed Laguerre integral. The polynomial
countermodel has positive S and a strictly larger-than-one row growth rate.
It therefore refutes this inference. The parent already supplies a stronger
smooth positive-source counterfeit. Neither is a refutation of RH.

3. Bootstrap from the two infinite boundary strips and two cones using
H_(a,b)=H_(a+1,b)+H_(a,b+1). A positive parent does not imply positive
children. No sign-preserving induction across the expanding intermediate
region was found. The positive regions are not claimed cofinal in the
sense required to force every inequality.

4. Bound Q_N by its source generating function on the full unit disk.
The generating function is an explicit Mobius pullback of h. Continuing
it through a possible nonreal h pole would assume exactly the desired
zero exclusion. The rate theorem makes that obstruction quantitative.

5. Estimate each prime kernel with a common positive sign. At r=1 and the
first mixed derivative, the kernel has opposite signs for primes 2 and 7.
An aggregate signed bound remains possible, but has not been proved.

## What a closure proof still must do

Prove the subexponential bound (10.5) from the literal theta cumulants or
complete Euler/gamma expression, retaining cancellation at unbounded order.
An alternative construction is welcome, but it must not import global
innerness, Stieltjes positivity, or the desired spectrum as a premise.
The exact rate theorem then gives a complete contradiction to any off-line
zero without a density-to-individual inference.

## Literature and novelty boundary

The heat/derivative normalization and count law are inherited from PR790
and PR785. Hausdorff moment criteria, Bernstein functions, Laguerre
identities, Cauchy--Hadamard, and Stieltjes integration are classical.
This pass adds explicit proof regions and the quantitative rate identity
in this particular source setting. It does not establish an external
priority claim. Related probability/positivity literature was searched;
no unchecked claimed GGC/RH proof was imported as a theorem.
