# Independent review of the strip-model route

Reviewer: a separate research agent (`/root/field_audit`) from the author of
the strip route. Review date: 2026-10-18.

Verdict: **the stated deductions pass this review at the exact file hashes
below**. No substantive mathematical defect was found. The finite example was
reproduced with optimized Python. This is an independent agent review of the
specified arguments and computation, not external referee approval, a proof
assistant check, or a new zeta zero-free theorem.

The author clarified two minor points raised during review: the bounded
elementary-parameter corollary now says `0<=A<infinity`, and the local
degree-20 continuation explicitly uses the retuned `A_0` coordinate in its
fields. Neither required changing a mathematical conclusion.

## 1. Exact reviewed identity

Paths are relative to the parent research packet. SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `strip/PROOF.md` | `b80cccdafb580cc56fc66587242af93b31df6e485cd058f5ae0e4e79417fc754` |
| `strip/check_strip.py` | `7ff97d97aa9c7f44cd52712c1eddcb0fc2ba87fefbc0352c71d87d2f26d40141` |
| `strip/certificate.json` | `df722b58bf29d12287febdb843dbbad7813114654616cbb1a1f45db7ca9c8123` |
| `strip/theta_source_replay.json` | `206cc313744e3ef24796f24e07e6232d8645ea77eb0235047a1730898da41a58` |
| `strip/inherited/pr886_primitive.py` | `2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55` |
| `strip/inherited/theta_source.py` | `75a239c2724afbd6d5ab343a00c1f3c4d1e7062eaab9ff99b0379eecde27e92d` |

The two inherited Python files are bound by their expected Git blob identities
as well as their SHA-256 hashes. The checker authenticates those identities
before importing or executing them. Their recorded source is repository PR
#994, commit `c93ca65a510b6acaf167f929b9bf7e67d742b05a`.

Later changes to a load-bearing file require a new review identity. Additional
editorial files are not automatically mathematical premises of this review.

## 2. The elementary-product obstruction

Theorem S1 is correct for the exact class stated: finite products of normalized
three-point characteristic functions with `a>=0`, `w>0`, and an independent
Gaussian factor `exp(-g z^2/2)` with `g>=0`.

The sign of the Gaussian factor is correct. On the imaginary axis that factor
is at least one, as is every three-point factor. Therefore a bound for the
whole product at `iR` bounds any selected factor from above; there is no
hidden cancellation on that axis.

A zero approaching a fixed nonzero real xi zero forces its selected
elementary frequency to be bounded below, since `w|Re z|>=pi/2`. The
imaginary-axis inequality also bounds the frequency above, including the
potential escape with `a>1`. In that case
`a=cosh(w|Im z|)`, so bounded frequency and `Im z->0` force the limiting
parameter to be at most one. A subsequential limiting elementary factor thus
has an entire real arithmetic progression of zeros.

Every one of those zeros persists into the proposed entire limit. The proof
uses local uniform convergence and Rouche's theorem, so it also handles a
double limiting zero at `a=1`; a simplicity assumption is unnecessary.

The imported contradiction is correctly scoped. I independently fetched
[Li--Radziwill, arXiv:1208.2684v1](https://arxiv.org/pdf/1208.2684), Theorem 4
on printed page 3. It applies unconditionally to every fixed real offset and
every fixed positive spacing on the critical line. It excludes the full real
arithmetic progression obtained here. The argument does not use an
arithmetic-progression exclusion off the critical line, or assume RH. The
existence of a real xi zero is a separate classical unconditional input.

The bounded-`a` finite-order corollary also follows: matching the second
moment bounds total variance, the bounded parameter converts that into a
uniform Gaussian growth envelope, and cofinal moment matching would then
contradict S1. It does not identify the first infeasible finite order.

## 3. Compactness counterexample and sharp elementary cutoff

The strip-only counterexample is valid. With `a_w=cosh(bw)`, all fixed positive
moments vanish as `w` grows, and every zero lies on the two boundary lines
`Im z=+/-b`. Nevertheless the imaginary-axis values diverge above the band.
Thus convergence of all fixed moments plus a common strip is insufficient for
the whole-plane normality needed in the proposed approximation argument.

The calculation in Lemma S2 was independently checked. The factorization

`(a+y)^2-(a+1)(ay+1)=(y-1)(y+1+a-a^2)`

gives the claimed variance-sharp Gaussian bound for `0<=a<=2`; the fourth
cumulant is positive for `a>2`, giving the stated local failure. No fitted
numerical pattern is used.

## 4. Interacting fields: strip and uniform growth

Theorem S3 uses the finite multivariate ferromagnetic Lee--Yang theorem in its
proper domain. I independently checked the stated source
[Newman--Wu, arXiv:1901.06596v2](https://arxiv.org/html/1901.06596v2), Section
2.5, Theorem 11. The site measure concentrated at `+/-1` satisfies the
single-site premise. Positive real parts at every vertex give nonvanishing;
global spin reversal gives the negative case. The field/weight bound makes
all real parts have the same strict sign outside the desired band.

Zero-weight vertices are treated correctly. Their fields must be zero;
temporary positive weights give locally uniformly convergent finite
partition functions. The limiting function is entire and equals one at
zero, hence cannot be identically zero on an exterior half-plane. Hurwitz
therefore preserves nonvanishing there. The case of an identically constant
observable is harmless.

The growth estimate has three sound steps:

1. The zero-field weighted magnetization has only real Fourier zeros.
   Evenness and exponential type give the paired Hadamard product, whose
   quadratic coefficient is half its variance. The inequality `log(1+x)<=x`
   gives the variance-sharp zero-field exponential-moment bound.
2. The high-temperature graph expansion gives nonnegative zero-field spin
   correlations. It justifies replacing signed real fields by their absolute
   values and then increasing them coordinatewise.
3. Jensen's inequality gives `Z(h)>=Z(0)` even for fields of mixed signs.
   Combining these facts yields exactly the claimed bound
   `|phi_h(z)|<=exp[V_0(b+|Im z|)^2/2]`.

The reference variance is explicitly that of the graph with its fields set
to zero. Its boundedness is an additional uniform hypothesis, not a
consequence asserted from matching the biased variance. The involution
condition for symmetry and the tree path-product variance formula are also
correct as stated.

## 5. All-order implication, normalization, and finite-error estimate

Theorem S4 is a valid conditional theorem. The S3 envelope gives normality
on every compact subset of the entire plane. Exact cofinal moment matching,
or convergence of each fixed moment, identifies every possible subsequential
limit with the actual normalized xi function. Hurwitz then transfers the
strip. The argument does not import a real-zero closure theorem for the
different strip-confined class.

The exact rescaling in Section 1 is correct. If the theta variance is `v`,
the standardized characteristic function is `F_theta(z/sqrt(v))`; its band
is `sqrt(v)` times the band in the original xi variable. The finite example
uses the original variable throughout.

Equation (21) is a correct Cauchy coefficient bound. Symmetry removes odd
powers, the matched even powers vanish from the difference, and the remaining
geometric series begins at degree `2N+2`. The optimization formula explicitly
ignores its rational denominator and is presented only with that limitation.

The missing infinite premise remains visible: no models at unbounded moment
orders with the same band and a bounded reference variance have been
constructed. Neither S4 nor the finite example establishes the `5/6` zeta
boundary.

## 6. Finite computation actually reproduced

I ran, from the strip directory,

```text
python -O check_strip.py --source ./inherited
```

The run exited successfully and produced exactly the certificate hash in
Section 1. It freshly reconstructed the complete retained theta moments using
the authenticated inherited backend. The source replay hash also matched the
record in Section 1. Acceptance uses explicit exceptions, so optimized Python
does not remove the acceptance predicates.

The finite example has 18 observed spins and matches only moments 2 and 4.
Its equality proof is the exact algebraic definition of the parameters in
Section 6, not interval overlap. Direct moment-box overlap is appropriately
labeled a diagnostic. The directed calculations establish the strict
physical field band, positive weights, nonreal zeros with imaginary height
between `3/10` and `31/100`, and reference variance below `1/20`.

As a separate ordinary floating-point sanity check, I independently evaluated
the parameter formulas from the retained source moments and obtained a field
ratio approximately `0.322468`, reference variance `0.04622834`, and nonreal
zero height `0.305502`. These approximations are not certification inputs.

The exact five-spin fixture enumerates all 32 configurations and independently
all 16 edge subsets. It verifies the spin-reversal involution, the complete
set of spin correlations, and the path-product reference variance, including
a zero-weight vertex. It does not certify the infinite analytic theorems.

## 7. Conditional degree-20 continuation and boundaries

I read [the pinned T20D source](https://github.com/GettysburgResearch/riemann/blob/c93ca65a510b6acaf167f929b9bf7e67d742b05a/standalone/2026-10-18-theta20-and-native-cancellation/theta/PROOF20.md).
Its 256 type-0 leaves have identical couplings and weights, and coordinate
`A_0` is active. Swapping two such leaves is a legal involution. If its
asserted finite root and invertible active Jacobian hold, the real-analytic
implicit-function argument in Section 7 is valid, with fields proportional
to the retuned `A_0` coordinate. Positivity persists locally.

I did not rerun or independently approve T20D's 305-spin root certificate.
The new corollary correctly keeps it as an explicit proposed premise. It
supplies neither a numerical continuation radius nor an additional matched
moment order.

The imported Lee--Yang theorem, Li--Radziwill theorem, theta Fourier identity,
and inherited transcendental interval backend have not been independently
reproved in this review. Their exact statements and uses were checked. The
positive review covers the deductions and finite replay at the hashes above;
it does not promote the complete research programme to an RH proof.
