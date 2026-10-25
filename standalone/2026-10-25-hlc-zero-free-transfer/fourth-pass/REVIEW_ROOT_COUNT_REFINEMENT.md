# Independent review of the refined prescribed-line root count

Reviewer: `/root/hlc_joint_paths`. Authors reviewed: `/root/middle_joint`
and `/root`. Date: 25 October 2026. The reviewer did not author the
root-count proof or its checker.

## Frozen objects and outcome

- `ROOT_COUNT_REFINEMENT.md`, SHA256
  `9749fc016f0247446f312bc48a51718840026644122b1685763fba62c06f4512`.
- `check_root_count_refinement.py`, SHA256
  `4e5d458069528fc6cfcda10978bb339934a73f6a9c21af6c5b7bb39955dd591b`.

**Outcome: accepted at its stated root-count and restricted triangle
scope.** The elementary kappa=3/4 theorem has a complete argument in
the note. The kappa=1/2 theorem explicitly imports the classical
Weil--Salié estimate. Neither version proves a full centered HLC
operator bound, the native thin-band witness hypothesis, or a new
zero-free region.

I read the full final note, inspected the checker, and independently
ran it under `python -O`; it passed. I checked the source Appendix A
congruences against `/tmp/2610.20242.txt` and the source PDF pin
`32ef255566d4f3611d2d89c3a5f3db94c792883cc713d77a7f9d33b163f55e88`.
For the classical alternative I independently opened the primary
publication, Blomer--Man, *Bounds for Kloosterman sums on GL(n)*,
[Math. Ann. 390 (2024), equation (1.2)](https://link.springer.com/article/10.1007/s00208-023-02777-6),
DOI `10.1007/s00208-023-02777-6`. That statement has exactly the
all-integer-frequency, positive-modulus scope needed here.

## 1. The elementary exponential-sum estimate is proved

The fourth moment over both frequencies counts unit quadruples with
equal ordinary sums and inverse sums. Once the fourth unit is
eliminated, clearing the unit denominators gives precisely the
three-factor divisibility condition printed in the note. The linear
map from the three remaining variables to those factors has kernel
of size at most two, including even moduli.

For each prime power dividing m, the exponent of m can be distributed
among the valuations of the three factors. Hence every admissible
triple is covered by an ordered factorization `d_1 d_2 d_3=m`.
Each factorization covers exactly `m^2` triples modulo m before unit
restrictions. This proves the stated `2m^2 tau_3(m)` upper bound.

The unit action on the frequency pair preserves its Kloosterman
phase histogram. Its stabilizer is exactly the units congruent to
one modulo `m/g`, where `g=(h,k,m)`: the two stabilizer
congruences combine to that modulus. Reduction of units from m to
the divisor m/g is surjective, as checked prime power by prime power.
Thus the orbit size is `phi(m/g)`, including the pair `(0,0)`.
Applying the fourth-moment upper bound to this orbit gives the
`m^(3/4+epsilon) g^(1/4)` estimate. The divisor and totient losses
are subpower and introduce no prescribed-modulus parameter.

The separate classical bound is correctly marked as imported. Its
divisor factor gives the same form with kappa=1/2, including zero
and noncoprime frequencies.

## 2. Fixed-u congruences retain their exact modulus factors

The congruences for c,v modulo uS exactly reconstruct
`d=(1+cv)/u` and all four entries of the prescribed matrix.
Writing `s_1=(u,S)`, `s_2=S/s_1`, `m=u s_1` is legitimate because
S is squarefree. Then s_2 and `C=u d_0-1` are units modulo m.
The second unit assertion uses `s_1|u`; it does not require the
matrix entry d_0 to be a unit.

CRT fixes both coordinates modulo s_2. Modulo m there is one unit
coordinate y, its partner is `C y^(-1)`, and the remaining condition
is `y=c_0 mod s_1`. The additive indicator for this condition has
normalizer `1/s_1`, exactly as in equation (7). There is no missing
CRT multiplicity.

For every frequency, including the axes and multiples of u, reduction
modulo u gives

`(gamma h+j u,gamma k C,u)=(h,k,u)`.

Passing from u to `u s_1` costs at most s_1, proving (8). Applying
the exponential-sum estimate therefore costs
`s_1 u^(kappa+epsilon) (h,k,u)^(1-kappa)` after a smaller
preliminary epsilon is chosen. No factor S is silently absorbed
into the epsilon: `s_1<=u` is the bound used there.

The zero frequency is also exact. It equals `phi(u s_1)/phi(s_1)`,
which simplifies to
`u product_(p|u,p∤S)(1-1/p)`, and is at most u. This is the
main term used later.

## 3. Bounded variation controls all Fourier frequencies

The proposed upper and lower functions are interval indicators,
expanded or contracted, convolved with a nonnegative probability
mollifier. Their variation is at most two. The interval Fourier
coefficient supplies the factor `1/|n|`, while the mollifier supplies
arbitrarily rapid decay beyond `1/Delta`. This proves (12) for
these specific functions, uniformly in the interval, even for very
short intervals. It is not an assertion for arbitrary moving
profiles.

Summing over `n=d r`, with n nonzero, gives the reciprocal-d factor
in (13). The estimate remains valid when `d Delta>1`, when the
whole series is a decaying tail. The gcd majorant then separates
the two genuinely nonzero frequency coordinates from the two axes.
For the former, the divisor sum is bounded by `zeta(1+kappa)`;
for the latter it is at most a subpower of u. The true zero pair
has already been treated separately.

Consequently every Fourier series used in the rectangle estimate is
absolutely summable. There is no unbounded-frequency remainder to
discard. Choosing `Delta=u^(kappa-1)/100` pays the zero-frequency
area error as well as the full nonzero sum. This justifies (17),
uniformly for arbitrary circle intervals and all squarefree S.

## 4. The matrix-class discrepancy is uniform in S

The c interval has length `|I_3|/S` in the uS circle. Splitting
the v interval into whole and partial uS blocks gives exactly the
main term (18), and at most `O(B/u+1)` copies of the rectangle
discrepancy. The larger estimate for the number of blocks only
enlarges the error; it creates no unproved cancellation.

On the one progression `u=u_0 mod S`, the gcd `(u,S)` is the
constant `d_*=(u_0,S)`. If the progression is nonempty in
`[A,16A]`, then `d_*<=16A`. Together with `d_*<=S`, this gives

`sum_(u in A I_1, u=u_0 mod S) (u,S) <=31A`.

This remains valid when S exceeds A and when the main density is
very small. Multiplying by the fixed-u estimate and using A<=B
gives the absolute error `O(B A^(kappa+epsilon))`. Thus no
modulus factor remains in the matrix-class discrepancy.

For the main term, every divisor ell retained in the Möbius
expansion is coprime to S. The two congruences therefore specify
one class modulo ell S, even when u_0 is not a unit. Summing the
counting errors with weight `1/ell` gives `O(log A)` uniformly in
S. Extending the reciprocal-square series costs `O(1/S)`.
The resulting Euler product matches the exact size of
`SL_2(Z/SZ)`. These main-term errors are smaller than the displayed
absolute discrepancy.

When B<A, the printed normalized-completion map is an involution
and has determinant one. For positive coprime u,v at least two,
its second column is normalized correctly. The ratio correction is
exactly `1/(uv)`, at most `1/(AB)`. Expanding and contracting the
reflected interval changes the unnormalized predicted main term
by O(1), which is absorbed. This checks the scale-swap step without
assuming that the correction is constant along the progression.

The theorem's error is explicitly **absolute**, not relative to
`1/|SL_2(Z/SZ)|`. For large S it can exceed the main term; no
relative equidistribution assertion is made.

## 5. Prescribed lines, parity, and the triangle corollaries

At the prime two there are exactly two determinant-one matrices
whose first column is `(1,1)`, out of six. At an odd prime p,
a fixed kernel line of `(u,-2c)` permits p-1 nonzero first rows,
each with p determinant-one second rows. CRT therefore gives
exactly `2 product_(p|S) p(p-1)` matrix classes, at most `2S^2`.
Their proportion is `1/3 product_(p|S)(p+1)^(-1)`.
Summing the absolute matrix errors proves the stated
`S^2 H^(kappa-1+epsilon)` discrepancy with the source's exact
parity and once-line normalization.

The original list-diagonal triangle has at most
`O(d_0Y^3)` label families, `O(d_0Y)` candidates per family and
used-prime modulus `O(d_0Y^3)`. The refined count hence costs
`d_0^4Y^10 H^(kappa-1+epsilon)`, equivalently
`(4J+10) beta-(1-kappa) delta` in its exponent ledger.

For the full common-D theorem, both endpoint list choices are
already paid by the separately reviewed
`COMMON_D_TRIANGLE_EXTENSION.md` at SHA256
`67769f6a6f2a9c6c8beca1aad4c94f7150d71b4d11253515e355df84c3ff7bc9`.
That theorem was independently reviewed by the coherent-identity
agent; this review does not replace that independence. The enlarged
label count and modulus each have at most J+4 primes per group,
while the h count remains J+1. Thus its ledger is exactly
`(4J+13) beta-(1-kappa) delta`, as stated in (31).

Both applications use a single first-position interval for each
fixed primitive candidate after a positive enlargement. No general
boundary conversion, no reciprocal-prime discount on the error,
and no conditional-history assumption is used. In the final
`[x^(1/800),x^(1/400)]` common-D example, the errors are exactly
`x^(-1/50+epsilon)` and `x^(-33/400+epsilon)` for the two inputs;
the main contribution is `x^(-1/800+epsilon)`. These are genuine
restricted path bounds in the source x scale. They do not establish
the native U-scale witness hypothesis.

## 6. Independent replay

The final optimized replay passed:

- 31 fourth-moment moduli, 92,349 unit-quadruple eliminations,
  11,439 unit-orbit cardinalities and 172,248 phase histograms;
- 1,549 fixed-u congruence cases, 81,258 exact CRT phases and
  211,840 gcd-frequency cases, including axes and large frequencies;
- 123,070 progression-gcd cases, 2,392 normalized completions
  and 14,352 scale-swap modulus checks;
- the exact matrix, line and parity cardinalities, 2,816
  harmonic-progression cases, both sets of 32 triangle ledgers,
  six explicit exponent examples and the negative controls.

The finite checker does not prove the analytic majorants or the
asymptotic estimates. Those steps were reviewed in the proof itself.
The accepted result is the refined root count and its stated
finite-depth raw triangle consequences, with the classical input
identified separately. The full signed arithmetic and zero-free
transfer remain open.
