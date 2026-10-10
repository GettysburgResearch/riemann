# Independent reconstruction of finite rays, cusp coefficients and support pruning

**Reviewer:** root AI agent. The author of the finite-ray proofs and checker
is finite_ray_residue; the author of the cusp and covariance notes is
scale_covariance_attack; the bootstrap author is signed_series_bootstrap.
The reviewer authored SPECTRAL_ROW_MEAN.md and FULL_CUSP_DESCENT.md and
**does not claim independent review of those two files** here.

**Verdict:** PASS for the finite-ray and cube identities, the complete
coefficient adapter including its all-cusp quantitative consequence,
the support-pruned covariance theorem, the bootstrap's local algebra
and new analytic domain, and the finite checker at the scopes below.
This is a reconstruction of source-conditional deductions, not external
human acceptance, formal certification, or fresh verification of the
imported analytic foundation. No generalized moment has been proved.

## 1. Exact content reviewed

| File | SHA-256 |
|---|---|
| [FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md) | `8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0` |
| [FINITE_CUBE_HOMOGENEITY.md](FINITE_CUBE_HOMOGENEITY.md) | `e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1` |
| [ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md) | `bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1` |
| [SUPPORT_PRUNED_COVARIANCE.md](SUPPORT_PRUNED_COVARIANCE.md) | `83ba41487ce6e0d1e81e2efbecc21be5c364134b97639afa0b12680765f0c8e3` |
| [SECOND_REFLECTION_BOOTSTRAP.md](SECOND_REFLECTION_BOOTSTRAP.md) | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` |
| [checks/check_descent_algebra.py](checks/check_descent_algebra.py) | `675187430abcfa5433f7a749da594b6121bc3fc2d06c7febb63fafb027124280` |
| [results/descent_algebra_checks.json](results/descent_algebra_checks.json) | `9a78e9d8559d6130573826a03608e8f09001c7e78b1e7956a6f56fd32c07798a` |

A subsequent receipt must bind these same blobs to the published frozen
source commit. Any altered mathematical content requires a new
assessment of the affected scope.

## 2. Actual finite-ray reunion

I read the imported source's finite Fourier expansion, reduced
numerators and denominators, CRT inverse choices, three-case
`eq:ray-multiplier`, and `eq:ray-additive-crt`, and compared them with
the exact prior exponent-3/exponent-4 scalar in PR #920. I did not
replace their actual finite multiplier by an arbitrary family.

For primary d outside S, substitution x=d squared y in the defining
finite Fourier sum gives rho(d) squared times the original coefficient
under h -> d^(-2)h. The same substitution scales the bad numerator by
d inverse, the reduced denominator by d, and the inverse numerator by
d. The source CRT construction allows the needed higher fixed bad
precision without changing the translate: changing a Fourier
representative changes the translation by 3O. The source normalizing
unit is preserved because d is primary.

The first Kubota case gives the inverse fixed numerator character
(c0/d)_3. In the middle case both denominator characters scale by d
inverse, and their product is (-c0/d)_3 inverse; the cubic character
of minus one is one. In the unramified case ordinary cubic reciprocity
for primary c0,d converts (d/c0)_3 inverse to the same result. Thus the
conjugated bad scalar cancels the good-prime supplementary factor,
leaving eta rho cubed. The cusp and the bad additive character remain
fixed. I checked these three cases individually against the actual
source formulas, including c0 a unit and nonprimitive Fourier labels.

Multiplying back the global Euler factor uses P_p=D_p exactly.
The free-prime factor is 1-x, and the frequency-prime factor is
1-x+qz. The remaining product is finite in the prime divisors of the
frequency; all primes at kS remain omitted. In the stated tube,
Re(w)>5/2 and the frequency majorant is Nm raised to
max(0,1-Re(v))+epsilon. The absolute cusp coefficient sum then
converges precisely under the two stated strict inequalities. This
checks the local normal convergence, holomorphy through v=1, zero
complete residue and removability of the former reciprocal poles on
the overlap. The estimate preserves Q^(1-2Re(s)); it is not a moment
saving by itself.

## 3. Cube covariance and all-cusp coefficients

The separate permutation h -> b cubed h gives the contragredient
Fourier factor bar(rho(b)) cubed. The reduced denominator and cusp are
unchanged, while the inverse numerator scales by b inverse cubed.
The fixed additive phase is consequently unchanged when the frequency
is multiplied by b cubed. The bad Kubota character is unchanged in
all three cases because the scaling is a cube. In the middle case
this additionally needs the source's explicit b_g=0 at sufficiently
high lambda-adic precision; the imported CRT construction supplies
it. This is the delicate ramified step, and it was checked directly.

I opened the primary Dunn–Radziwill v3 source and checked equations
(5.7), (5.8), (5.13), (5.14) and the relevant rows of Appendix A
against the imported three cusp formulas. Only these explicit
coefficient identities are used, not that paper's conditional
prime-sum estimates. The conversion is
`g(t,n)=sqrt(Nn)chi_n(lambda t)^(-2)gamma_2(n)` in the repository
additive convention. Conjugating the cusp at frequency minus ell
produces the stated Gauss factor, the stated ninth-root phases,
and the correct opposite unit sectors at the two nonstandard cusps.
The complete table, its omitted zero sectors and its bound
`27*3^(j/6)` follow.

Primary b=1+3z gives b cubed minus one in lambda to the fourth times
O. Thus the intrinsic nonstandard-cusp trace phase also stays fixed.
Multiplication by a cube preserves every support exponent modulo
three, including when b overlaps the squarefree factor. The bad
squarefree CRT factor is cubic and belongs to a fixed bad ray group;
the unrestricted bad cubes keep their summable norm weights.

Finally I reconstructed the elementary character-orthogonality
argument: covariance on cubes forces every nonzero Fourier
coefficient to satisfy varrho cubed equals bar(rho) cubed. Cubic
supplementary factors preserve that equality. This verifies the
actual canonical-family interface, without an assumption that every
individual artificial old ray label equals kappa.

## 4. Support-pruned covariance and its quantitative comparison

I read PR #915's quadratic--cubic composition, including its
`(k,e)=1` mask and divisor-Cauchy treatment, before applying the new
adapter. Each supported cusp coefficient splits in e,n' by the exact
Gauss CRT character chi_(n')(e)^4; the other fixed phases separate
by finitely many residue classes. The mask and smooth-kernel
separation requirements of the cited lemma are unchanged.

The normalized ramified coefficient is bounded by a geometric
`3^(-j/3)` weight. The fixed bad squarefree part costs a fixed
constant, and the bad cube weights sum geometrically. These facts
justify the extension of the cited good-face bound to all three
actual cusp contributions. No growing auxiliary family is inserted.

The source support zero deletes the whole projected group before
subdivision into e,f and theta norms. After this deletion,
`EFG` is comparable to A and `G` is bounded by min(A,sqrt(B)).
The inherited block bound `HE+Y+(EY)^(2/3)`, with
`Y=H^2EG^2/(BF)`, gives the three displayed terms of the new
covariance estimate. Dyadic Cauchy or Minkowski controls the actual
cross terms at a logarithmic cost. No orthogonality of allocations
has been assumed. The window refinement follows by retaining the
lower bound on G in the first term.

For the all-cusp balanced estimate, setting H=D^h gives
`max(h+1,2h+1/2,(4h+2)/3)`. The third term never dominates; the
first two cross at h=1/2. Comparison with the physical factorwise
and classical bounds gives a strict size improvement for
`0<h<3/4`, maximum D^(1/2) at h=1/2. It does not enlarge the
old admissible D-squared row range or reach the long fourth-moment
initialization. This validates the newly added Corollary 5.1 as well
as its stated limitation.

I also read the exact pinned PR #919 remainder identity (2.9) and
lower bound (2.6a). Its nonnegative norm equals S plus a target-size
error. The elementary inequality |S|<=S+2B for S>=-B proves the
stated equivalence of signed and absolute scale-integral upper
bounds at the exponent level. This does not supply either bound.

## 5. Shifted-variable proof and its scope

The canonical coefficient cube law gives Ky=x. Summing all cube
valuations for a prime outside the squarefree index gives
`1/((1-x)(1-y))`; a prime in that index gives
`(1-x+K)/((1-x)(1-y))`. The outside reciprocal cancels exactly.
Pulling K out of the squarefree index shifts t to u=v-s. The CRT
conditioning retains the auxiliary d mask and its cube L-factor.

For a=Re(u)>1/2 that cube reciprocal has an absolutely convergent
Euler product. The cited individual theta bound, used with the
appropriate derivative and local row exponent, supplies the stated
Q and d powers. With delta=1-Re(v), the divisor majorant has exponent
`-a-delta+(1-a)/2`; summability is `3a-2Re(v)>1`.
This verifies the bootstrap's analytic domain and strict margins,
including its absolute outer cube factor and polynomial vertical
control. Reciprocity changes of row orientation are handled by the
explicit finite residue partition before applying the spectral
input. The bootstrap mean implication is a correct Minkowski
consequence, with that separate spectral input kept explicit.

For its Section 5 I checked the finite inactive identity A+B/q=1
and its displayed norm exponent. I do not record a separate full
phase reconstruction of that nonessential involution narrative.
The larger-domain and mean proofs do not use that narrative. The
physical 13/16 comparison in Section 8 is correct and yields no
new moment exponent.

## 6. Exact checker review and independent execution

I inspected the checker source. Its polynomial arithmetic clears
denominators exactly; its geometric checks retain the exact infinite
remainder. The finite-field Fourier transforms are evaluated in
integer cyclotomic quotient rings, with the principal character
still zero at the origin. The finite-group character projection,
Eisenstein multiplication and strict rational domain comparisons
match the stated predicates. Acceptance uses explicit exceptions
and remains active under Python optimization.

I ran the checker independently under normal Python and `python3 -O`,
writing to separate temporary paths. Both completed successfully and
both reports were byte-identical to the retained report. The output
counts are 5 polynomial identities, 36 rational cases, 360 exact
geometric-sum identities, 27 finite omission patterns, 69 deleted-prime
terms or powers, 16,560 finite Fourier covariance equalities, 3,033
character pairs, 289 primary cubes, 7,225 lattice phases, 7 spectral
real-part cases, 2 crossover identities and 8 strict domain witnesses.
All specified negative controls were exercised.

These are finite algebra diagnostics, not authenticated primitive
replay of the global Kubota calculation or proof of the analytic
theorems. In particular the checker does not certify the theta
foundation, a sieve, normal convergence, RH, or an infinite moment
hierarchy. Those limits are explicit in both the script and report.
