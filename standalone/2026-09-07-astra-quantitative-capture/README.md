# HC26 — quantitative capture, not an RH completion

**Proposed component proofs. Independent mathematical review required.
The requested bound (10) and RH remain unproved.**

This continuation establishes a target-dependent convergence rate for the
finite all-pass dictionary of the literal factorial source. It retains the
possibly nontrivial inner factor and converges to the TRUE intrinsic minimum,
not automatically to zero.

For A(w)=w*zeta(1/(1-w)), M=closure(A polynomials), and analytic bounded q
with boundary Sobolev regularity s=1/16, the proposed theorem is

```
0 <= dist(q,span(A,...,w^K A))^2-dist(q,M)^2
  <= C (||q||_(s)+||q||_infinity)^2 exp(-c sqrt(log(K+2))).
```

For the compact inverse seeds with exact horizon T and target t*exp(-t/2),
this gives the uniform growing-horizon estimate

```
0 <= U_K(T)-C_B(T)
  <= C(1+T)^2 exp(T) exp(-c sqrt(log(K+2))).
```

Rank exp(O((T+1)^2)) can therefore reduce the removable error to exp(-T).
Finite correction and compact-input realization are source-preserving.
The final absolute constants are not numerically instantiated, and this is
not a practical-rank claim or a new actual-source computational certificate.

The proof combines an unconditional small-value distribution of the source,
clipped OUTER inversion, Fejer approximation, and fractional regularity of
the actual inner factor. Unknown zeros appear only in the proof; the finite
arithmetic Gram solve does not use them as inputs. Ordinary boundary zeros,
hypothetical off-line zeros, multiplicities, and the circle accumulation point
are retained.

**What did not close:** C_B(T) itself has no subexponential upper bound here.
At a hypothetical rho=1/2+delta+i gamma it is at least
`2delta exp(2delta T)/|rho|^4`. A rate toward that floor is not a bound on it.
The paper gives an exact counterexample to the false inference, not an RH
counterexample.

## Read and replay

Read PROOF.md, then REVIEW.md for the six load-bearing review questions.
SOURCES.md separates classical inputs from source-specific arguments.
VALIDATION.md lists actual bounded checks and omissions.

```bash
python -I -B check.py
python -I -B -O check.py
python -I -B test_check.py
python -I -B -O test_check.py
```

The checker uses standard-library exact rational arithmetic. Its checks are
mostly finite exponent/constant bookkeeping and synthetic projection controls;
they do not machine-prove the analytic capture theorem or any zeta assertion.
Do not combine these counts with earlier packets or mark (10) as discharged.
