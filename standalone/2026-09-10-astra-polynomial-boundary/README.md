# Direct attack on the polynomial inequality — still open

**The positive-eta, degree-uniform inequality was NOT proved.** This packet
is the record of a direct boundary attack, not a replacement closing theorem.
AC29-1--4 are **PROPOSED component proofs pending independent review**.

The exact target from AC28-7 is, for every eta>0, one finite C_eta such that

```
||Q_p(1)-sum_(n>=3, odd)p(t/n)/n||^2_(1,3)
 <= eta||p||^2_(0,1)+4C_eta||t Q_p'(t)||^2_(0,1)
```

for all odd polynomials, where Q_p(t)=sum_(n>=1, odd)p(t/n)/n.
No uniform upper bound for C_eta is established in this packet.

## What was actually proved in the manuscript

1. **AC29-1:** a controlled C1 completion of the odd-polynomial test domain.
   An explicit Bernstein-primitive construction approximates every C1 function
   vanishing at zero in all three quantities in the target inequality.
2. **AC29-2:** exact smoothed odd Euler summation with complete O(v^-Re(s))
   bounds for both the remainder and its logarithmic derivative. The pole
   contribution becomes a constant after rescaling and cancels exactly.
3. **AC29-3:** actual odd-polynomial graph realizations of t^(s-1) for
   1/2<Re(s)<1, with explicit cutoff errors. A HYPOTHETICAL zero gives finite
   polynomial counterexamples below the parent's stated eta threshold.
   No such zero is asserted to exist.
4. **AC29-4:** averaging cutoff functions over a long logarithmic interval at
   an EXISTING critical-line zero yields direct polynomial witnesses against
   eta=0. It also gives a coarse necessary C_eta>=c/eta cost. This does not
   refute positive eta; the parent already has a sharper multiplicity result.

The new mechanism is the quantitative REAL-INTERVAL construction of the
boundary modes, independent of the earlier holomorphic feature-map argument.
The previous zero-exclusion conclusion is not being counted again as progress
on the missing positive upper bound.

## Reviewer entry

Read [PROOF.md](PROOF.md), especially the complete discrepancy integral in
Section 2 and the simultaneous graph limits in Sections 3--4. Inspect the
pole cancellation BEFORE taking any cutoff limit. Polynomial degrees may
increase without an explicit upper bound. No singular function is treated
as having an ordinarily convergent uncut Q series.

The checker provides bounded controls, not a proof of the analytic statements
or RH. Three tested real strip values 1/4, 1/2, 3/4 are NOT zeta zeros. No
critical-zero ordinate, complex-power numerical integral, or conjectured-zero
location is used in the accepted payload.

```
python -B check.py --check results.json --self-test
python -O -B check.py --check results.json --self-test
python -OO -B check.py --check results.json --self-test
sha256sum -c MANIFEST.sha256
```

[VALIDATION.md](VALIDATION.md) records the actual evidence, failed scouting
run, complete-tail inputs, and exclusions. [SOURCES.json](SOURCES.json) pins
prior work and classical inputs. All parent files remain unchanged.
