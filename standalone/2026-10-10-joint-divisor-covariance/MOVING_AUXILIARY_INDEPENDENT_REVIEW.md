# Independent review of the moving auxiliary adapter

**Reviewer:** `/root/joint_divisor_attack`.

**Reviewed file:** `MOVING_AUXILIARY_ADAPTER.md`.

**Exact SHA-256:**
`e91e0f7b3c3d885587fc9197539beaf1caa8e0c80ed9c8bba5c15340090b5eda`.

**Decision:** the new deductions in Sections 1–6 pass this independent
review at their expressly source-conditional scope. No blocking algebra,
mask, row-range, or norm-accounting error was found. The review does not
approve a generalized moment theorem, a new zero-free boundary, or a
global A2 functional equation; the reviewed file makes none of those
claims.

The reviewer authored the separate `JOINT_DIVISOR_MEAN.md` in this
packet. That file is not an input to the reviewed adapter. The author of
the adapter did not supply the argument used for the independent local
and norm reconstructions below. The earlier observation that a fixed
extra ray character may be put on one axis was exchanged during
research; its exact cube-factor change was independently checked here.

## 1. Sources actually compared

I read the complete reviewed file and compared its load-bearing steps
against these pinned sources:

- OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, local
  repository copy of October 5 `paper2.tex`: the local factors
  `eq:theta-local-factors`, `eq:ray-local-transform`, its active and
  inactive exceptional cases, and the complete scalar after
  `eq:dual-cusp-mellin-series`.
- PR #918 at `cfa102748b26f840ccc4b963a660711424db0ec3`,
  `INTERFACE_COMPARISON.md`: the complete physical mixed family,
  outer-mask cube inverse, A2 child normalization and mask overlaps.
- PR #921 at `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`,
  `ARBITRARY_ROW_MOMENTS.md`: the full local scalar calculation,
  completed and inverse fixed-sector block estimates, ordinary
  powerful-row summation and the exact three-way auxiliary-prime
  reindexing in Corollary 7.2. I also read the load-bearing parts of
  its `CUBE_INVERSE.md`: the literal cube identity, common-divisor
  removal for the two scalar variables, exact support insertion,
  fixed-block expression and surviving masks.
- PR #923 at `1a1152008706f7e24fa1efe4990588f8f99c5d8d`,
  `ALL_ROW_COMPLETION_AND_RAW_GAIN.md`: Theorem 1.1, its outer-mask
  uniformity, arbitrary-row scalar and support calculation, repeated
  row-prime factors and fixed bad-prime reduction.
- PR #914 at `0cc0428fedbbfc340044c7451b3d392c1da9a103`,
  `A2_COMPLETION.md`, Sections 1–5: normalized prime-power table,
  five-label coefficient formula, exact forward and inverse
  projection including the phase composition law, and normalizers.

The imported theta automorphy, all-cusp coefficient machinery and
classical large sieves are retained inputs. I did not independently
rebuild those foundations, run their Lean code, or certify the angular
reciprocal theorem. In particular, the strengthened value
`beta=11/12` remains conditional on the precise uniform scalar
premise (0.1). The choice `beta=1` uses counting for that scalar
premise but still retains the stated theta and sieve inputs.

## 2. Exact physical encoding and masks

Equations (1.3)–(1.4) have the same normalization as the pinned mixed
family. Expanding the inner theta definition gives the factor
`sqrt(Nb)/sqrt(AB)`, and the Gauss CRT law combines the outer and
inner squarefree coefficients into `a_xi(an)`. The lack of an
`(n,b)=1` condition is correct and necessary.

I checked (1.5) by multiplying the local symbols before any
reflection. On the cube index, the extra f power is twelve and
therefore a unit indicator. The q power is six and is also a unit
indicator on every original physical factor. This gives exactly
`chi_(an)(f)^4 1_(anb,qf)=1`, including when q,f,k overlap. No
factor is replaced by one at a nonunit.

The identity encodes the label `k f^4 q^6`, but the proof does not
apply a norm bound to all rows up to its much larger norm. It keeps
the physical k annulus and records its valuations at each moving
prime. This distinction is maintained throughout Section 2.

## 3. New local principal-prime calculation

For a prime in `q/(q,f)` with physical valuation zero, the effective
local symbol is the exponent-zero unit mask. The source Fourier
transform has precisely two branches. The inactive branch has
scalar `1-1/z` and no denominator prime; the active branch has
unit scalar and the local factor `z^(-1/2)chi_p(x)^(-2)`.

Using the full source scalar, I recomputed its dependence on the
outer variable a. The active local factor contributes exponent
`2j+2`; the a-prime factor and Gauss CRT leave exponent `2j`;
the original row factor leaves exponent `3j`. The new shifts by
4 and 6 preserve the parity of the physical valuation, so the
scalar character in (2.3) is indexed by the physical odd radical.
The moving masks stay in its exclusion. Thus the scalar bound is
applied before a positive row-norm enlargement, at an allowed
squarefree scalar index of norm `O(H)`.

The active principal prime multiplies the effective theta length
by `z^2` and the squared amplitude by `z^(-1)`. Its contributions
to the three energy monomials are therefore `z^(-1)`, z, and
`z^(1/3)`. Combining it with the inactive branch by Minkowski
gives exactly the three bounds (2.4). The first cost is bounded,
not a norm factor z. Multiplying a fixed branch constant per
moving prime costs a subpower on the stated polynomial support;
the file correctly avoids claiming a convergent uniform Euler
product for those constants.

The support calculation also uses the correct active set. The
new prime belongs to both the reflected denominator and the
second projection period only in the active branch. Hence its
radical cancels from their squared ratio, and the inherited
complete-group cutoff remains `G^2 << B`. There is no cutoff
asserted for an individual allocation before the reunion.

## 4. Auxiliary primes and every physical valuation

The exponent-four reindexing in (2.5)–(2.7) agrees with the
literal source factor and the exact reindexing in PR #921.
The second branch uses `n_0=p n_1`, retains `p` prime to n_1,
and has squared amplitude one and relative length z. The third
uses `b'=p b_1`, retains `p` prime to n_0 and allows arbitrary
remaining p powers in b_1; it has squared amplitude `z^(-1)`
and relative length `z^(-1)`. The negative branch has squared
amplitude `z^(-1)` and length `z^2`.

The extra Gauss CRT characters after extraction are separate
bounded coefficients in the two positive columns. The row phase
is a contraction on the true row subset. Neither scalar variable
g nor the inverse variable v acquires a character involving a
positive theta column. These are the hypotheses needed for the
pinned quadratic–cubic block proof; no arbitrary replacement of
theta coefficients is assumed.

When q and f overlap, adding six changes neither the exponent-four
symbol nor its zero mask. Counting such a prime once gives the
correct costs `1,z,z^(2/3)`, rather than multiplying a principal
and an auxiliary penalty.

For positive physical valuations I checked the six progressions
in (2.10). At a principal moving prime, the smallest valuation
gives powers `z^(-1),1,1`; the extra amplitude at valuations
4 modulo 6 and the branch count at valuations 0 modulo 6 do not
make a larger order. For an auxiliary prime the shifted exceptional
classes agree with PR #921 (7.11). The three sums are respectively
`O(z^(-1)),O(1),O(1)`. The physical valuation strata are disjoint,
so their energies are added directly.

Away from the moving primes, the powerful-row sums have local
errors `O(z^(-2)),O(z^(-2)),O(z^(-4/3))`, all summable over
prime ideals. The fixed bad-prime valuations give finite products
of geometric sums and a finite ray family. This includes all
units and nonempty terminal subunit row intervals. There is no
squarefree-row or sixth-power omission in Theorem 2.1.

The three allocation expressions in (2.12), their optimization
using `EJG` comparable with A and the prior support cutoff, and
the resulting costs `(1,L_(q,f),M_(q,f))` are algebraically
consistent. Rescaling the normalized test ratios after each local
extraction preserves the cited smooth seminorm bounds. The stated
uniform outer mask remains an exclusion in the scalar and a
separate positive-column mask; the stronger estimate is not
silently generalized to arbitrary outer coefficients.

## 5. Cube inversion and A2 norm transfer

The finite identity (3.2) has the correct coefficient `1/Nv`.
Grouping the combined cube index vb gives the exact Möbius
divisor sum. The original outer `(a,v)=1` mask is inside the
completion, and no mask `(v,n)=1` is inserted. The row cube
character retains its qf zeros as in (3.3).

The inherited two-scalar proof applies after enlarging its fixed
moving exclusions by qf. Its common-divisor norm factors remain
`(Nell)^(-2beta)` and the two positive-column extraction factors
remain `(Nd)^(-beta-1/2)`, so all three converge for beta>1/2.
The proof retains the combined support `G^2 Z^3 << B` before
taking norms. I recomputed the powers in (3.5)–(3.6); they give
precisely `delta=(2beta-2)/3` in Theorem 3.1. The subsequent axis
swap is valid for the finite raw polynomial, not an assertion
that two one-axis completions are identical.

The child scales, overlap `q_t/(q_t,f_t)=r c d`, and normalized
multiplier `1/(Nc Nd (Ne)^(3/2))` agree with the exact source
projection. Its inverse includes the full Möbius sign and the
source's phase composition law. I recomputed all six exponents
in the correction-norm table directly from (4.2), (4.3) and
(4.6). Each is strictly greater than one for `delta>-1/3`.
Therefore the correction-label norm sums converge absolutely in
both operator directions, with no polynomial loss hidden in a
cutoff.

As an auxiliary finite check, a direct `Fraction` calculation
recomputed those exponents at beta equal to `3/5,3/4,11/12,1`.
All four rational checks passed. This verifies those algebraic
instances only and is not used to prove the infinite theorem.

The fixed separate ray-twist paragraph changes the inner theta
character and its cube coefficient together. In particular the
cube inverse uses `(lambda eta_2)^3`; retaining the old cube
coefficient would be wrong. The added correction phase (4.10)
is multiplicative on disjoint triples and has modulus one, so
it preserves the stated norm sums. This paragraph assumes (0.1)
for the finite character family actually produced by those fixed
twists, as the opening contract specifies.

## 6. Weighted rows and the signed boundary

The row-ball and Schwartz-weight extension uses positive powers
`H,H^2,H^(4/3)` and therefore the stated dyadic sums converge.
It does not extend the result to an arbitrary signed or jointly
column-dependent row kernel.

The reconstruction factors in (6.2)–(6.4) are correct. In
particular the inverse theta reconstruction depends on the
combined cube index vb. A product-column kernel may be lifted
before the finite signed divisor sum because it is constant on
all subdivisions of a fixed reconstructed product. If a kernel
depended on the subdivision itself, that condition would fail;
the file explicitly states the required constancy.

The review approves the exact coefficient identity, single positive
norm estimates, and correction-operator stability at the scope
above. It does not approve replacing the remaining strict
two-column off-diagonal by these positive norms, equating
different correction labels, or discarding the outer signed
auxiliary sum. The remaining estimate identified in the final
section is still open.

## 7. Freeze and later changes

This report applies only to the SHA-256 recorded at the start.
A later mathematical edit needs a new content identity and
review. The source commit containing these bytes should be
recorded in the packet's frozen validation receipt; this report
does not by itself assert that such a commit has been published.
