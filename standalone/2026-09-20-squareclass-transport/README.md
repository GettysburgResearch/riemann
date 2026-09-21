# STC26 — matched negative transport and inert-square individualization

**Proposed component proofs for independent review. RH/GRH, the full native
negative transport bound, and the full Newton covariance gain remain open.**
Continuation of PET26 on #903, parent
`862f93aad76d0768b08bd9a12f6764d15e2cad63`. All previous packets are preserved.

## 1. A bound on part of the previously missing side

PET26 controls the POSITIVE part of the full prime-extension covariance
P_b=sum_p log(p) integral_b^(b^2) M(x)M(x/p) dx/x^2. This packet addresses
an exactly specified sector of its NEGATIVE part.

Expand P_b into coefficient triples (m,n,p), and retain those for which the
outside-bank parity cores of m and p*n agree. Denote that matched sum by T
and the unmatched remainder by R. The complete absolute matched envelope is

    B <= H_(b^2-1) [product_(q in S)(1+1/sqrt(q))]^2
         * [2 sum_(p<b^2)log(p)/p + sum_(p in S)log(p)/sqrt(p)].

This includes arbitrarily large transport primes, not just primes in S.
For S contained in primes up to (log(b^2))^2 the envelope is subpower.
It controls both signs of T. The unresolved term is now stated WITHOUT
hiding it: (-P_b)_+ <= B + (-R)_+.

For the empty bank every matched summand is negative, and exactly

    -T = sum_(n<b^2) mu(n)^2 log(n) w(n)
         + sum_(p^2*r<b^2, p not dividing r) mu(r)^2 log(p) w(p^2*r),
    w(n) = 1/max(b,n)-1/b^2.

It follows unconditionally that

    0 <= -T <= (3/2)(log b)^2 + 2 log b,
    -T = (9/pi^2)(log b)^2 + O(log b).

The leading asymptotic needs only elementary squarefree counting, not PNT.
The theorem is a component estimate, NOT a bound for the unmatched native
remainder. It is not asserted identical to RCB26's harmonic covariance.

## 2. An averaging interpretation with its obstruction retained

The matched sum is exactly the average of consistently prime-sign-twisted
transport observables. The prime weight must also carry chi(p).
This average cannot be assigned to each individual source: the all-minus
signature has source mu^2 and an unmatched negative term of order b^2.
At Y=255 its full twisted transport is about -229122.51. This is an
auxiliary multiplicative counterfamily, not a counterexample on native mu.

## 3. L-family progress: the entire good inert sector is cheap to remove

At a good inert CM prime, the arithmetic reciprocal factor is 1+p*T^2.
For the center-one energy integral |sum a(n)|^2 dx/x^3, its insertion has
operator cost 1+1/p; its causal inverse costs at most (1-1/p)^(-1).
Thus ALL active odd good inert primes p<sqrt(X) may be removed/restored with
an O(log X) energy loss. Exact bounds are products, not asymptotic constants.

An auxiliary sign family on the p^2 coefficients obeys exact Parseval:

    average_energy(X) = sum_(d squarefree inert, d^2<X)
                          energy_stripped(X/d^2)/d^2.

Its mean differs from the stripped energy by a bounded factor, and the
native member can be recovered from that mean at O(log X) cost, with NO
exponential signature-count loss. These artificial signs are NOT genuine
quadratic twists. The remaining split-prime source is not controlled.

There is a crucial central-rank warning: the removed infinite inert product
behaves like C*(s-1)^(-1/2) on the real right approach to the arithmetic
center. A rank-one reciprocal's simple pole becomes a half-order singularity
after stripping. Off-center right-half-plane poles persist, but the stripped
object must NOT be fed to the old rank-one deflation test as if it were the
completed elliptic L-function. Restore the Euler product first.

## 4. Complete finite results, Y=255

| Sector bank | Matched T | Unmatched R | Full P_b |
|---|---:|---:|---:|
| empty | -25.954361615499 | +24.292872945235 | -1.661488670264 |
| {2,3} | -9.103174657733 | +7.441685987469 | -1.661488670264 |
| {2,3,5,7} | -10.867477088960 | +9.205988418696 | -1.661488670264 |

These are rounded descriptions of directed certificates. Positivity of
the tested native remainders is NOT an all-scale sign claim. The known
annular energy 0.179852003503 and completed state 1.587579815076 are retained,
not advertised as new numerical improvements.

Seven full stages and three banks give 1,588,798 matched triples, counting
overlap across banks/stages. The largest output runs through 65535. The
separate verifier uses trial factors, the three-case fibre classification,
and reverse integral sums rather than the producer's parity lookup and
forward cumulative calculation. Scalar interval primitives are shared.

The CM finite-Euler fixture uses E_17's counted good-prime factors, enumerates
256 auxiliary signatures through 4095, and checks 1,048,320 coefficient
comparisons plus exact rational Parseval and causal inverse identities.
It is NOT the full E_17 source or a global rank/zero computation.

## Read and replay

Read [PROOF.md](PROOF.md), [LFAMILY.md](LFAMILY.md), then
[VALIDATION.md](VALIDATION.md). Sources and attribution are in
[SOURCES.json](SOURCES.json). Standard library only:

```sh
python -S -B replay.py
python -S -B test_packet.py
python -S -O -B replay.py
python -S -O -B test_packet.py
```

Replay regenerates complete reports under reports/, authenticates the
committed semantic receipts, and runs the separate transport verifier.
Twelve regression methods include twelve corrupted-report variants,
numeric-type aliases, duplicate keys, exact sign averages, the squarefree
counterfamily, and family normalization/endpoint controls. All four commands
pass; direct producer and verifier entrypoints were also run in both modes.
No full repository validator, external formal build, independent mathematical
acceptance, native remainder bound, or RH/GRH proof is claimed.
