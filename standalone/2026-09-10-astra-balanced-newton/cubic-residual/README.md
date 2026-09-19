# CIR26: let the Newton orders cancel each other

**Proposed component proofs, pending independent mathematical review. No RH
proof or all-scale native covariance estimate is claimed.** This is an
addition-only continuation of PR848 at
`098acb780655eb81f8b842be201596a50198e757`.

The preceding quadratic construction isolated distinct-product covariance.
This pass changes the scale map itself: retain the bounded native completion,
but cancel the arithmetic residual to THIRD order. It generates the exact
Mobius prefix below (Y+1)^3 and introduces cancellation between quadratic and
cubic terms. Those terms are combined at each actual integer product before
any diagonal is estimated. The complete new diagonal is still only
O((1+log Y)^12), at every scale, by an elementary hyperbola proof.

## Main mathematical objects

Let m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k<=Y)m(k)^2, b=Y+1, B=b^3-1.
The clipped input c preserves mu through Y, has |c_n|<=3, P_c(1)=0,
support L<=2Y and WHOLE energy J(c)<=2F_Y. Put

```
z2=c*c, z3=c*c*c,
v=3c-3(1*z2)+(1*1*z3),
a_d(k)=z3(d)L_d(k)-3z2(d)K_d(k).
```

K is the centered harmonic packet from the preceding pass; L is the centered
second-divisor harmonic packet defined in [PROOF.md](PROOF.md), (3.4).
Every same-product cross term, including the interaction between degrees, is
inside a_d. Then

```
F_B <= 19 F_Y + 2 D_Y^(3) + 2 C_Y^(3),
D_Y^(3)=sum_d sum_(k=b)^B a_d(k)^2 = O((1+log Y)^12),
C_Y^(3)=sum_(d!=e) sum_(k=b)^B a_d(k)a_e(k).
```

The last covariance is ordered and signed, not an absolute row sum. A bound
C_Y^(3)<=0 eventually on the cubic ladder gives F_X=O((1+log X)^12), hence RH.
A suitable weaker subpower or subcubic gain also suffices. **Those native
estimates remain unproved; this covariance target retains RH strength.**

| Claim | Result | Scope |
|---|---|---|
| CIR26-1 | Bounded native source with paid tail | Reused PCR26 construction, rederived; not newly claimed |
| CIR26-2 | Exact cubic residual identity and finite output completion | Classical higher-order identity; complete output prefix, excluded boundary |
| CIR26-3 | Centered harmonic-divisor packet bound | Every d and finite cutoff X; logarithmic X cost retained |
| CIR26-4 | Combined-degree diagonal and covariance accounting | Complete integer-product diagonal at every scale; covariance open |
| CIR26-5 | Complete conditional RH chain | Does not prove the antecedent |
| CIR26-6 | Generic coefficient/moment class has cubic obstruction | Non-native family; not a Mobius or RH counterexample |

## Native finite evidence, not a sign theorem

The complete outward panels at Y=1,...,12,15,19 all have negative C_Y^(3).
For example at Y=19, 417 coalesced products and all 7,980 annular integers give

```
-70.91894136 < C_19^(3) < -70.91894135.
```

The source (1,0,...,0), completed by the SAME rule, has positive covariance
already at Y=8, and the all-parameter proof gives C_Y^(3)=Omega(Y^3) eventually.
Thus a norm-only estimate cannot replace the native divisor identities.
The latter family is explicitly excluded from the native prefix theorem.

All coefficients generated through 262143 are checked in the largest
single-stage test (Y=63). This is NOT a covariance panel through that size:
the largest covariance panel is Y=19, B=7999. The cubic ladder is
1,7,511,134217727,...; only its first two extensions are in the finite corpus.

## Whole-source boundary and review priority

The new packet estimate for L retains a log^3 X factor; it is NOT a uniform
infinite raw-stage energy theorem. We restrict the exact output to n<=B and
explicitly add its one-atom zero-at-one completion. Its WHOLE energy is exactly
F_B. A subsequent clipped completion costs at most 2F_B. No unknown raw future
has been dropped and no unsupported Hilbert-space projection is invoked.

Review [PROOF.md](PROOF.md), Sections 2--4: the native residual gap, explicit
finite completion, hyperbola remainder, centered moments and degree grouping.
Section 5 states the unproved native estimate; Section 6 rejects a generic
substitute. [SOURCE_LOCK.json](SOURCE_LOCK.json) credits the classical inputs
and distinguishes reading depths. [VALIDATION.md](VALIDATION.md) records the
executed tests, failed prototype and limitations.

## Reproduce

From this directory, Python 3.10+ and the standard library suffice:

```bash
python -S -B produce.py --check result.json
python -S -B verify.py result.json --self-test
python -S -O -B produce.py --check result.json
python -S -O -B verify.py result.json --self-test
```

The two implementations import neither each other nor repository modules.
They have the SAME author, not independent mathematical acceptance. Directed
integer intervals use elementary series and a cited digamma remainder. The
analytic all-scale proof is not inferred from the finite corpus. No existing
source, review, status, workflow, or setting is changed.
