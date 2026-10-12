# Independent audit of exact integer-count cutoffs

Verdict: **ACCEPT analytically at the complete-source/imported-input scope.**
Reviewed Q1--Q9 of [GOOD_CUTOFF_PICK.md](../heights/GOOD_CUTOFF_PICK.md)
at SHA256
`2fc4b6caf69a28eda0ebd2e6a5b0d9761efb0387155a93437706676ae540d34b`,
2026-10-10 14:56 UTC. The reviewer read the primary-source Turing record
and previously independently accepted the complete weighted/Volterra and
density proof dependencies. The subsequent scalar checker at SHA256
`c7ccf42e601860385482848ae5314be6c23c84ca12bd68a58d833bc4b190792c`
also passes independent code review. Its owner's normal/optimized receipts
are byte-identical at SHA256
`5857dd9956fbfe11d31a959100b3ccd5b272a221a258c1ac992f05b961d1877e`.
The forty weighted-sawtooth fixtures integrate the polynomial pieces
independently, with positive decreasing linear weights and all integer
cuts included. The exact Turing, cofinal, exponent, gap and census-interval
guards match the proof. No selected numerical cutoff,
published Turing computation or large critical-line census was replayed.

The complete right-continuous multiplicity count minus the smooth main term
strictly decreases between ordinates and jumps upward by positive integers.
If it never equals zero on a compact interval, a positive-to-negative
sign transition is impossible. This includes a one-sided limit equal to
zero at an upward jump: the right-continuous value either retains positive
sign or supplies an allowed negative-to-positive transition. Finiteness
of the ordinates on a compact interval makes the stated sign rule precise.

On a positive-sign interval the count is at least ceil M almost everywhere;
on a negative-sign interval it is at most floor M. After changing variable
to u=M(t), both centered envelopes have derivative 1/2-{u} off integers.
Their continuous periodic primitive F={u}(1-{u})/2 lies in [0,1/8].
The inverse-density weight g is positive and decreasing because M'>0 and
M''>0. Integration by parts therefore bounds the centered integral between
-g(a)/8 and +g(a)/8. The resulting signed count integral has magnitude
at least L/2-1/[8M'(a)], with the exact displayed constant.

The native gamma/count remainder and the literal imported unconditional
Trudgian integral theorem give Q3 with the safe error (b-a)/(3a).
If no exact cutoff occurs in the twenty-unit interval, one ten-unit half
has uniform sign and magnitude greater than 5-1/32. The same half has
Turing upper bound below 4, a contradiction. Thus the right-continuous
Delta(T)=0 cutoff exists in [H0,H0+20]. The cofinal argument with
L=ceil(log B) also checks: L<=B/2, log(B+2L)<L+1, and the linear lower
gap exceeds the conservative integral upper bound for every L>=29.
Neither argument assumes a favorable value of S(H0) or a zero spacing.

For the tail (T,infinity), Stieltjes integration by parts uses the
right-continuous Delta(T), which is exactly zero. If T is a zero ordinate,
its complete source atom belongs to the below-or-at-T packet. The
remaining derivative discrepancy is exactly 4*c_*d*q*B_R. The bound
applies to every complex numerator with the fixed denominator, including
every D^jP in the complete arbitrary-displacement exponential series.
No selected source packet or constant displacement is substituted.

The previously accepted derivative and conjugate-group arguments give the
same complete quadratic payment with the new quadrature and amplification
constants. The positive endpoint gap applies for q<=87/200. The cutoff
is common to all nodes because it depends only on the complete count.
The published critical-line census extends past H0+20, so the entire
below-or-at-cutoff source may be added as a nonnegative critical Gram
source. The strict integer guard for n=1142000 gives the stated global
order. Cofinal choices produce growing orders for selected tail cutoffs,
not the same theorem at every predetermined cutoff, all-order positivity,
or RH.
