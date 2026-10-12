# A complete native heat-trace point at u=1/64

Status: version-two finite proof-producing computation, accepted only on checker PASS.
Scope: the complete actual-Xi heat trace at one time and derivative order
r=0. This authenticates one strict positivity inequality, not complete
monotonicity or RH. It uses no finite zero list or complete zero count.
Exact dependencies: the independently reviewed complete source formula
HT6 and complete prime-tail bound HT12 in
[COMPLETE_PRIME_HEAT_TRACE.md](COMPLETE_PRIME_HEAT_TRACE.md).
What was actually run: the accompanying receipt states the native backend,
finite integral intervals, literal prime powers, tails and strict predicate.
Smallest remaining gap: all positive times and all derivative orders of the
full source. This isolated point supplies neither universal quantifier.

## HP1. A cancellation-preserving finite Gamma integral

Fix u=1/64. The integral in HT6 has integrand

\[
 I(q)=\frac{e^{-q}-e^{-q/4-4q^2}}{1-e^{-q}}.
\]

Define the entire function `H(z)=sum_(j>=0)z^j/(j+1)!`, equivalently
`H(z)=(exp(z)-1)/z` with H(0)=1, or `1F1(1;2;z)`. Then the exact
cancellation-preserving formula is

\[
 I(q)=-e^{-q}(3/4-4q)
           \frac{H(q(3/4-4q))}{H(-q)}.
 \tag{HP1}
\]

This explicitly removes the singularity at q=0; its value there is -3/4.
The remaining nonreal poles arise from zeros of H(-q). Native complex-ball
division detects any ball meeting such a pole; no unchecked logarithm or
square-root branch occurs in this meromorphic callback.

The first all-hypergeometric evaluation hit its finite time budget without
a receipt. Version two uses the algebraically identical exponential quotient
when the argument ball has real part greater than 1/4; HP1 remains the
removable-zero evaluation near zero. Both formulas are the same meromorphic
function, so this evaluation choice creates no analytical branch boundary.

The native integrator encloses the four literal intervals
`[0,1]`, `[1,4]`, `[4,16]`, `[16,100]`. Their union covers the complete
finite segment [0,100], and every returned complex ball must be finite
and contain zero in its imaginary projection. The real projection remains
an interval, rather than being replaced by a decimal midpoint.

For q>=Q=100, `1-exp(-q)>1/2`. Therefore

\[
 \int_Q^\infty |I(q)|dq
 \le 2e^{-Q}+8e^{-Q/4-4Q^2}=:B_\Gamma.
 \tag{HP2}
\]

The second term uses `exp(-4q^2)<=exp(-4Q^2)` before integrating
`exp(-q/4)`. The checker adds the full symmetric interval
`[-B_Gamma,B_Gamma]` to its finite Gamma integral and retains the uncertainty
in Euler's constant, pi and every exponential.

## HP2. The literal prime powers and complete complement

The finite prime term is exactly

\[
 \sum_{p^a\le64}\log(p)\,(p^a)^{-1/2}
                              e^{-16(\log(p^a))^2}.
 \tag{HP3}
\]

The checker enumerates the primes p<=64 by exact integer trial division,
and for each one enumerates every power p^a<=64. The von Mangoldt weight
is log p for each power. No suggested or sampled prime inventory is used.

At r=0, HT11 holds because `log64>2` and `4u=1/16`. HT12 gives the complete
remaining PRIME CONTRIBUTION TO K, including its prefactor, at most

\[
 B_P=\frac{2\sqrt u}{\sqrt\pi}
                    e^{-(\log64)^2/(8u)}.
 \tag{HP4}
\]

The missing prime contribution enters K with a minus sign. The checker
therefore subtracts the interval [0,B_P], not a midpoint or zero tail.
Combining HT6, HP2 and HP4 encloses the COMPLETE heat trace at u=1/64.

## HP3. Arithmetic, acceptance and source scope

The checker fixes python-flint 0.9.0 / FLINT 3.6.0, uses 320-bit directed
Arb/Acb arithmetic and Acb's certified complex integration, and records
the loaded primitive binary hashes. It requests finite integration goals
and also imposes finite degree, evaluation and depth budgets. Failure to
obtain a finite integral or a strictly positive complete K interval is a
failed certificate, not an inferred sign.

The sole strict mathematical acceptance predicate is `K(1/64)>0` for the
full interval after both tails and all native uncertainties. A source map
binds this proof, the checker and the complete heat formula. The formula's
infinite analytical source is imported from its separately reviewed proof;
the finite checker does not independently prove the functional equation,
Euler identity, complete product, or global heat criterion.

Normal and optimized independent replays must report their own runtime
scope. One native point has no complete-time or higher-derivative coverage.
