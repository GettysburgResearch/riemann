# Independent review of all scales and the label Euler denominator

23 October2026. This review binds:

* `work/two-hour-boundary-20261023/COHERENT_FULL_ALL_SCALES.md`, SHA256
  `55404b197241570cb4a343e7f0e53d5957a17e6077ef418312e048b9b3649dc3`;
* `work/two-hour-type-20261023/LABEL_EULER_DENOMINATOR_CLOSURE.md`, SHA256
  `53178793d23f8897af7f4848a8a42636fb119e60c0bde6decea49f036fcc636e`.

Verdict: no gap found in either deduction under the explicit common-profile
and arithmetic-family hypotheses. These extend the previously reviewed
coherent full-series vector bound; they do not establish its applicability
after selected-prime or moving-coprimality transformations.

For the all-scales note, the exact raw finite-minus-pole identity, rather than
the completed identity, is the appropriate small-U input. The finite-vector
factor `min(K,1+K^2/U)` gives the displayed coarse bound in all three ranges:
below K, `KU<=K^2` and `K U^(1/6)<=K^(7/6)`; above K, the extra nonvolume
term `K^2 U^(-5/6)` is decreasing and at most `K^(7/6)`. At
`U<=sqrt(DK)`, its volume and nonvolume terms are bounded by
`(DK)^(1/2)` and `D^(11/12)K^(1/12)`. The exact pole contributes
`U^(1/3)D^(2/3)<=D^(5/6)K^(1/6)`. The latter and the volume are absorbed
for K<=D; the imported residue bound still imposes K<=D^(1/7).

The support statement at subunit U is essential and correctly retained.
Once the finite physical annulus is empty, the raw remainder is exactly its
negative pole and decays like U^(1/6). A bounded interval between the first
physical threshold and1 requires only a fixed enlargement of the unit row
ball. No analytic inverse estimate is applied to nonexistent subunit ideals.

The final weighted-Cauchy observation is valid: for fixed delta>0,
`product_(p|R)(1-Np^(-delta))^(-1)<<_epsilon NR^epsilon`. This follows by
bounding each sufficiently large prime factor by Np^epsilon and absorbing
the finitely many smaller primes into the constant. After Cauchy, the remaining
all-ideal weight `Nk^(-2+delta)` is summable for delta<1. An internal epsilon
smaller than `(1-delta)/6` absorbs the scaled `U^-epsilon` cost. The note
explicitly leaves the fixed-k-family hypothesis to be established.

For the label-denominator note, I independently checked its direct head/tail
proof, which does not need to assume the later all-scales note. The phases
omega(R,k) lie outside the free-column sum and disappear harmlessly in the
norm. Weighted Cauchy yields exactly one outside `1/Nk` in E3. Dropping the
label-support restriction is legitimate only in this nonnegative sum of the
unchanged fixed-k vectors, as stated.

At `A=U^(1/6)(DK)^(-1/12)`, the head has only a harmonic sum. In the tail,
the volume, nonvolume and entire pole weights are respectively
`U Nk^(-7)`, `D^(5/6)U^(1/6)Nk^(-2)` and
`D^(2/3)U^(1/3)Nk^(-3)`. Summing them gives respectively
`(DK)^(1/2)`, `D^(11/12)K^(1/12)` and `D^(5/6)K^(1/6)`, all within the
claimed bound. The finite original plateau stops at `Nk<<U^(1/6)`; its
harmonic sum is not extended to infinity. The pole tail continues and is
summed separately. This also supplies convergence from finite partial sums.

Finally the Mellin normalization is correct. Expanding
`(1-nu(p)^6 Np^(5-6u))^-1` gives `nu(k)^6 Nk^(5-6u)`.
With the original factor U^(u-1), this is exactly
`nu(k)^6/Nk * (U/Nk^6)^(u-1)`, hence E1, not a different completion weight.

I independently derived these new scale sums and checked their inputs against
the already reviewed full-vector theorem. No numerical replay is needed for
these identities. This review is not a certification of upstream analytic
sources, nor of the still separate simultaneous primitive transfer. No
complement estimate, new fixed zero-free boundary or RH conclusion follows.
