# A fixed-progression residue vector and the coherent pole-tail split

23 October 2026. Proposed source-dependent deduction; independent review
requested. The unconditional statement here is the fixed-progression lemma
below. Its application to reassembled primitive local blocks requires the
explicit interface in section2 and is not asserted merely from a scalar
primitive proof.

The input is V1 of `LOCAL_SUPPORT_RESIDUE_RANGE_EXTENSION.md`, SHA256
`a2b88fdc3f2d2685f5567b80d5a18d90d2b3de97e69a62960c52d2ddf53463e0`,
with its inherited fixed-section full-residue periodicity. Paper8 version1,
equation(2.6), gives `rho_full(n p^6)=rho_full(n)` at every good prime,
and its Section3 shows that fixed modulus punctures preserve this identity.
No corresponding continuous-series identity is used.

## 1. Fixed progression lemma

Let b be fixed squarefree, and Q a puncture fixed throughout the label
average. Impose b|n on the original normalized Mobius coefficient and any
additional fixed coprimality restrictions on n/b. Write the resulting full
residue pairing as P_b(D;R). Labels R are good and sixth-power-free, NR<=K.
Then, provided b^2 K<=D,

    sum_R |P_b(D;R)|^2
      << (DbKNQ)^epsilon
          [D^(2/3)b^(-5/3)+D^(1/2)K b^(-1/2)].       (F1)

Indeed put n=bm. The outside coefficient has modulus b^(-1/2), the free
length is D/b, and the free puncture is fixed Qb (together with any other
fixed restrictions). The actual Mobius coefficient and permitted fixed
ray/norm profiles are preserved. At the residue only, replace the new
label bR by its sixth-power-free reduction. The map from sixth-free R
to this reduced label is injective: at every prime its exponent is
translated by v_p(b) modulo6. Its norm is at most bK. Fixed numerator-ray
filters are partitioned into the same finite sections before using
periodicity. V1 therefore applies exactly when bK<=D/b. Multiplication
by b^-1 gives F1.

This allows b and R to share primes. It does not allow an extra moving
restriction `(m,R)=1` or an arbitrary coefficient depending on m and R.
A fixed restriction `(d,R)=1` only selects a subset of labels and is harmless.
If b^2K>D, the scalar label-uniform estimate, summed over at most O(K)
labels, instead gives

    sum_R |P_b(D;R)|^2
      << (DbKNQ)^epsilon
          [D^(2/3)K b^(-5/3)+D^(1/3)K^(4/3)b^-1].    (F2)

## 2. Exact interface required for a primitive partial pole

Suppose the primitive local operations have first been reassembled so each
partial pole is the original full-residue progression P_b with b=Gdv,
only fixed selected-prime/b punctures, and no moving remaining-label mask.
Suppose also its exact reciprocal-tail multiplier, after selected residue
phases collapse, is

    (DK)^(1/12) P^(-1/2) d^(-1/2) k^-1,              (F3)

as obtained from common cutoff
`C=U^(1/6)(DKP^6)^(-1/12) k^-1 d^-1/2` and the original coefficient
`U^(1/6)P^-1 d^-1 k^-2`. The label-supported denominator is restored
separately. The selected P divides the original label radical. All v-only
primes occur in k, and the remaining fixed local weights are bounded by
the exact PR1015 positive Euler weights.

These are required arithmetic identities, not consequences of an exponent
check. Under them, the following whole-b split is valid. Apply divisor
Cauchy for the selected choices at each original label first; only then
sum their squared P^-1 weights. The supported ideal sum is subpower,
and the divisors G of P cost a subpower too.

Take M=D^(1/7), and assume K<=D^(1/6). For b<=M, F1 is legal since
M^2K<=D. Its first term contributes amplitude at most

    D^(5/12)K^(1/12)
       sum d^(-4/3) k^-1 G^(-5/6)v^(-5/6),

which converges up to the selected subpowers. Its second term is at most

    D^(1/3)K^(7/12)
       sum_(Gdv<=M) d^(-3/4) k^-1 G^(-1/4)v^(-1/4)
      << D^(1/3)K^(7/12)M^(1/4).                     (F4)

Summing d up to M/(Gv) leaves the stronger G^-1/2 v^-1/2 weight.
The k/v ideal sum converges because every v-only prime occurs in k.

For b>M use F2. In its first amplitude extract
`(Gdv)^(-1/3)<=M^(-1/3)`. The remaining weights are
`d^-1 k^-1 G^-1/2 v^-1/2`. The d sum is supported by the original
annulus and costs a subpower; the k/v sum converges. This tail costs
amplitude `D^(5/12)K^(7/12)M^(-1/3)`. The scalar second term can be
summed everywhere, with squared cost `D^(1/2)K^(3/2)`.

Consequently the squared partial-pole resource under the exact interface
above is

    D^(5/6)K^(1/6) + D^(31/42)K^(7/6)
                    + D^(1/2)K^(3/2)
       << D^(5/6)K,       K<=D^(1/6).                (F5)

Both head and tail middle terms have exponent31/42 after M=D^(1/7).
The second comparison in F5 requires only K<=D^(4/7), and the third
only K<=D^(2/3), so the stated range is safe.

F1 is the new fixed-progression deduction. F5 is a conditional consumer
until the exact reassembled primitive interface has been proved. In
particular it must not be inserted into a block retaining the old scalar
proof's moving exact-gcd restriction. Neither statement controls the
complementary inverse operator or proves a zero-free boundary improvement.
