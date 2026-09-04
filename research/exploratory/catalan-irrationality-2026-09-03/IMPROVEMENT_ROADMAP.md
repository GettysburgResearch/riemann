# Improvement roadmap

## Priority 0: produce a corrected v2 proof packet

The smallest viable repair set is:

1. define `D := 2B` before the square matrix;
2. add `S <= B/20` to Theorem 5.1;
3. replace the literal `5B` support cutoff in Lemma 5.5 by a proved safe
   linear cutoff, for example `7B` in the final regime;
4. give unique equation numbers in Section 5.1;
5. state a uniform bound for the Pascal quotient `Psi_A(I)`;
6. expand Proposition 9.5 into a complete ledger.

The first three corrections appear not to change the final constant or
strategy.

## Priority 1: publish exact computational artifacts

### Odd-small-prime certificate

A machine-readable certificate should contain, for every merged interval:

```text
rational left and right endpoints
ordering of the marginal ladders
rational quadratic Q_0(v)
symbolic antiderivative identifier
outward-rounded endpoint enclosure
local remainder bound
```

The checker must verify:

- the union is exactly `[0,1]`;
- interiors are disjoint;
- all breakpoint events are represented;
- the displayed quadratic equals the original floor/quantile definition;
- special-function argument shifts are exact;
- Euler-Maclaurin remainder signs and magnitudes;
- the final rational interval.

### Middle-prime certificate

For each of the 235 cells, publish:

```text
t interval
affine ordering data for the six boundaries
selected marginal levels
rational affine E_{1/20}(t)
exact integral
```

The checker should sum the rational integrals and recover the displayed
fraction exactly.

## Priority 2: close Proposition 9.5

Write a master identity before taking asymptotics. Every factor in (4.5)
should have one ledger row:

```text
F_B
row factorials
column factorials
Pi_i
Cauchy denominators
V(J)
V(I)^2
Psi_A(I)
tail bounds
number of Cauchy-Binet subsets
minimal integerizer local surplus
prime 2
odd small prime powers
middle primes
large primes
higher powers
surplus rows
fixed rational denominator q.
```

For each row record:

```text
exact finite expression
B^2 log B coefficient
B^2 coefficient
uniform error
source lemma.
```

The proof should visibly cancel the `B^2 log B` column and sum the `B^2`
column to the claimed coefficient.

### Missing Pascal-height lemma

A promising exact statement is:

> If `A` is obtained from `{0,...,S+2}` by omitting
> `c_1,c_2,c_3`, then the Pascal alternant quotient has total selected-index
> degree `c_1+c_2+c_3-3 <= 3S`, and its coefficient height is at most
> `exp(O(S log(B+S)))`.

This would make its logarithm `o(B^2)` uniformly.

## Priority 3: independent formal verification

The finite core is well suited to Lean:

```text
Catalan tails and recurrence
finite differences of polynomials
Newton interpolation
rational-function pole extremality
matrix rank/minor extraction
Newton unit-vector completion
Cauchy determinant
alternating-polynomial Vandermonde divisibility
p-adic valuation of factorials and Vandermondes
balanced occupancy minimization
positive-part denominator identity.
```

The analytic layer needs:

```text
Stirling with uniform errors
PNT weighted prime-power summation
Hurwitz zeta, digamma, and log-Gamma recurrence identities
Euler-Maclaurin interval certificates.
```

Keep the finite algebra, PNT interface, and numerical certificate as separate
modules so the trust boundary remains visible.

## Priority 4: optimize the ratio rho = S/B

The paper fixes \(\rho=1/20\). Define the full margin function

\[
M(\rho)
 =
-\big(4\rho-2\rho^2\big)
-c_{\rm odd}(\rho)
+\Lambda_{\rm mid}(\rho)
+\Delta_{>B}(\rho),
\]

with signs normalized to the final contraction.

A systematic campaign should:

- derive cells symbolically as functions of rational `rho`;
- locate combinatorial phase transitions;
- optimize the certified margin;
- search for a rational `rho` with fewer cells and a larger margin;
- measure sensitivity to each prime range.

A larger margin makes all subsequent verification and quantitative work more
robust.

## Priority 5: effective bounds and an irrationality measure

The present proof is asymptotic. To obtain an explicit irrationality measure
or even an explicit contradiction threshold, one needs:

- effective Stirling remainders;
- an effective PNT error sufficient for every compact prime range;
- explicit full-row stability constants;
- an explicit upper bound for `Psi_A(I)`;
- a concrete lower bound on the negative margin after all errors.

The determinant family may then yield rational approximants with controlled
denominator and error. Whether these bounds are strong enough for a useful
irrationality measure is open.

## Priority 6: generalize to periodic L-values

Let \(\chi\) be a real or complex periodic character. Study tails

\[
T_m^{(\chi)}
 =\sum_{r\ge0}\frac{\chi(m+r)}{(m+r)^2}
\]

or residue-class-separated state vectors.

Possible architectures:

```text
period-q vector recurrence
-> weighted vector tails
-> block Cauchy/confluent-Cauchy matrix
-> block Pascal alternant
-> local prime-power occupancy
-> adelic contraction.
```

Targets include:

- other even beta values;
- \(L(2,\chi)\) for odd quadratic characters;
- linear independence of several special values;
- criteria predicting when the local gain cannot beat the real baseline.

The method may reveal a structural distinction between period three and
period four that complements the Calegari–Dimitrov–Tang result.

## Priority 7: abstract the same-scalar adelic theorem

Formulate a reusable theorem with inputs:

```text
a nonzero rational determinant Q_B
an exact local valuation lower bound for its numerator
a local saturation theorem for its denominator baseline
an archimedean Cauchy-Binet upper bound
a negative global height coefficient.
```

Conclusion:

```text
the source constant assumed rational produces a nonzero integer
whose absolute value tends to zero.
```

Such an abstraction would clarify which parts are Catalan-specific and which
can be reused in Riemann's determinant programs.

## Priority 8: RH-facing exploration

The only credible RH extension is indirect:

```text
hypothetical off-line zero
-> canonical nonzero source determinant at infinitely many scales
-> same-scalar p-adic/prime-side saturation
-> archimedean contraction
-> contradiction.
```

This would require new theorems absent from the Catalan argument:

- an individual-zero-to-determinant propagation theorem;
- coefficientwise signed source control;
- local uniformity over growing scales;
- a bridge from complex zeros to arithmetic denominators;
- complete treatment of finitely many exceptional zeros.

The Catalan proof offers a design pattern, not those theorems.
