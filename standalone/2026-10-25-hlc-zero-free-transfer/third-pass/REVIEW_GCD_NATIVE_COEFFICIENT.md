# Independent internal review: coherent gcd cancellation

Reviewer: root research agent. Author: native_gain agent.

**Verdict: pass as a component theorem under the stated scalar zero-free,
functional-equation, and divisor-bounded sieve premises.** The remaining
large reduced-numerator component is not bounded here. Neither this
review nor the finite checker establishes an unconditional new zero-free
region.

Reviewed mathematical file: `GCD_NATIVE_COEFFICIENT.md`, SHA256
`515e0cc01061507d1de50f8dab73424c82f97d8c9db67e2201213ae046bb7c45`,
Git blob `2cac689a44863471e9a46576e096c45e93d89a35`.

Reviewed checker: `check_gcd_native.py`, SHA256
`82f35606a0d220e3053e225c6d6f0495d26c4125eee14e1a34bf2a5dc7f18ee0`,
Git blob `e69128edb0e5af8911df565bc5933e6b53d7291b`.

Reporting-only authentication update, authorized by the reviewer:
native_gain renamed the output key to
`cases_with_a_above_both_cutoff_scales` and replayed the amended checker
under `python -O`. No acceptance predicate, calculation, or count changed.
The checksum above includes that five-byte reporting correction.

The root replay used `python -O`; all predicates remained active and
passed. The algebraic checks include 98 weighted convolution identities,
3,105 coefficient-allocation identities, 30 exact masked-character gcd
returns, 81 coprime Euler factorizations, and 2,130 rational exponent
predicates. Deliberately incorrect deletion of the both-divisible term,
gcd mask, full smooth support, or primitive dual support was detected.
These are finite checks in a free-prime integer model. The analytic
arguments below require mathematical reasoning and the stated sources.

## 1. The exact identity precedes every norm estimate

I independently derived the smooth convolution identity from
`delta_1-m_y*1=(mu-m_y)*1`. Its square is supported strictly above
`y^2`, giving `mu=2m_y-m_y*m_y*1` through that norm. With
`y=sqrt(2D)` and `D>=8`, the linear term vanishes on the original
annulus. The full smooth product coefficient has support below `8D`.

Retaining this full support matters. The reflected contributions with
original outer norm greater than `2D` are individually zero only after
their complete dual sums are taken. They cannot be deleted before the
gcd grouping if one wants the factorization claimed for its coefficient.
The final note explicitly keeps them.

For `r=da`, `n=db`, and `(a,b)=1`, the primitive characters give

`psi(da) conjugate(psi_star(db))`

`=psi(a) conjugate(psi_star(b)) 1_((d,P)=1)`.

The redundant original zeros as well as the primitive conductor belong
in `P`. The transformed profile depends on `b/a` and loses its d
dependence. The surviving coefficient is exactly
`C_a(P)=sum_(d,P)=1 A_y(ad)/Nd`. The remaining coprimality condition
`(a,b)=1` is retained. No false puncture mask is put on the primitive
dual variable b.

## 2. The three-way prime allocation is exact

For `a=a_1 a_2^2`, a prime of `a_2` is forced into both original
squarefree Mobius variables. For a prime of `a_1`, I used the identity

`1_(p|h_1 h_2)=1_(p|h_1)+1_(p|h_2)-1_(p|h_1)1_(p|h_2)`.

This gives the three allocations `l,r,h` of the note. With
`d_L=a_2 l h` and `d_R=a_2 r h`, the inclusion sign and the fixed
Mobius signs reduce to the common `mu(a_1)`, and
`Na/(Nd_L Nd_R)=1/Nh`. The residual harmonic sums have exactly their
stated masks. In particular there is no additional coprimality between
the two residual variables, or with the opposite singly allocated
factor. A prime of exponent three in a forces a zero coefficient.

This reproduces equation (12), including repeated primes. Bounding the
two harmonic sums gives the coefficient factor `(Na/D)^(1-beta)`.
That pointwise estimate alone would not justify the subsequent family
sieve, because its mask varies with the row.

## 3. Mellin separation repairs that row-dependence issue

The scalar reciprocal bound is derived from a zero-free half-plane,
polynomial growth, an Euler-normalized logarithm, Borel--Caratheodory,
and three circles. The argument uses nested discs strictly within that
half-plane. Its conclusion is a subpower reciprocal on every fixed
interior line, with constants allowed to depend on that line.

For the fixed smooth cutoff, its Mellin transform has just one pole,
at zero. The reciprocal Dedekind zeta factor vanishes at one, so that
pole cancels in the harmonic Mellin integral. The deleted local Euler
factors are analytic on the shifted line. Rapid Mellin decay and the
subpower reciprocal justify the exact common contour shift. This also
handles residual harmonic scales below one, without a sharp Perron
endpoint or a row-dependent truncation height.

On the actual natural support `(a,P)=1`, every forced divisor d is
coprime to P. Thus

`F_(Pd)(1+s)=F_P(1+s) E_d(1+s)`.

This factorization separates all row dependence into two bounded row
scalars. At fixed Mellin frequencies the remaining a coefficient is
common and divisor-bounded after division by `Na^(1-beta)`. Its norm
phases need not be differentiated by the sieve. The two contour
integrals have finite absolute weighted mass, so Minkowski is licensed
after this exact separation. The final proof does not submit arbitrary
row-dependent column coefficients to a common-coefficient inequality.

## 4. Primitive conductors and powerful rows have the right costs

For a fixed powerful physical part v, the residual row length is
`W=U/Nv` and the primitive conductor scale is
`q_v=W Nrad(v)`. For a puncture divisor e of norm E and reduced
numerator scale B, the dual length is `L_0=q_v B E/D`.

The prefactor calculation in the note is correct:

`[sqrt(D/q_v)/(B E)] L_0 sqrt(B[W+B+(WB)^(2/3)])`

`=sqrt((q_v B/D)[W+B+(WB)^(2/3)])`.

In particular E cancels before its finite divisor sum is bounded. For
fixed b, the remaining `(a,b)=1` mask belongs in the common a sequence;
the primitive value at b is only a bounded row scalar. Small dual scales
are handled by the rapidly decreasing dyadic tail, whose sum is at
most a constant times L_0 even when L_0 is below one.

Finally `sum_(Nv~V) Nrad(v) << V^(1+epsilon)` supplies precisely the
three powerful-row terms displayed in the note. Their dyadic sums give
the claimed full physical-row bracket. This retains nonsquarefree
sixth-power-free rows and does not confuse their norm U with their
smaller primitive conductor.

## 5. The useful consequence and its boundary

For `B_0<=sqrt(U)`, the bracket is at most a constant times U. Dyadic
norm summation is geometric because `3-2beta>0`. At the imported scalar
cap `beta_0=7/8`, taking a fixed interior line sufficiently close to
that cap gives

`J_(<=B_0) << U^(2+epsilon) (B_0/D)^(5/4)`.

The small change in beta is absorbed only because all prescribed
lengths are bounded powers of U. For `B_0=U^(9/20)` and
`D=U^r`, the gap to the inherited complete-inverse exponent is exactly

`(1+5r)/6 - [41/16-5r/4] = (100r-115)/48`.

It is therefore at least `1/48` throughout `29/25<=r<=117/100`.
A saving of `1/1000` on the complete complement in this same
decomposition would improve the full native moment by `1/1000` and
would be another sufficient hypothesis for the conditional consumer.
This is an alternative decomposition, not an additional disjoint piece
that can be combined without an overlap estimate with the smooth
original-product cutoff in `INVERSE_POWER_COMPONENT.md`.

At reduced numerator norm comparable to D, the new coefficient factor
is only of constant size. The proof gives no complete-tail saving there.
Its positive result is the actual coherent small-ratio component,
containing all original product scales, under the explicitly imported
scalar and sieve premises. Establishing that remaining tail is still
necessary before the conditional zero-free implication can be used.
