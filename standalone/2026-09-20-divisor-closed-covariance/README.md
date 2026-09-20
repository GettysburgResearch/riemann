# DCN26 — complete divisor cancellation and larger covariance sectors

**Proposed component proofs for independent review. The full native covariance
bound and RH/GRH remain open.** Additive continuation of #903, frozen at
`530cc8f706b1f1e3dc7aff77efdced82e4ac73ad`. No previous files or claim statuses
are changed. Classical identities and inherited kernel bounds are credited.

This pass does two different things. It cancels the previous negative matched
sector using the ACTUAL native arithmetic, and it proves a broader absolute
bound directly in the ORIGINAL centered-harmonic Newton covariance. The
physical and harmonic observables are kept separate throughout.

## 1. The previous negative matched sector belongs to a favorable larger sector

For nonnegative prime weights a_p, let h(p)=a_p and A=h*mu. Expand the
physical prime transport into coefficient pairs (m,t), t=pn. Retain all
pairs for which m divides t or t divides m, counting equality once. Then

    P_div = sum_(n<X, squarefree composite n)
              [sum_(p|n) a_p] * [1/max(b,n)-1/X] >= 0.

This is exact at EVERY cutoff, even before integration. The whole forward
orientation m|t is zero by sum_(m|t)mu(m)=0; the proper reverse orientation
is a positive squarefree-composite sum. It is not inferred from finite signs.

The STC26 empty-bank matched sector has m=sf(t), hence m|t. EVERY one of
its negative terms is included in, and exactly canceled by, the complete
forward divisor fibres. Additional complete coprime-cofactor fibres are
also exactly zero; PROOF.md gives their endpoint and disjointness conditions.

For log-prime weights, 0<=P_div<=1.5(log b)^2 and
P_div=(9/pi^2)(log b)^2+O(log b). The asymptotic needs only elementary
squarefree counting and a Chebyshev bound, not an RH-strength prime estimate.

There is a full LCM version as well: every coefficient fibre
sum_(lcm(m,t)=n)mu(m)A(t) is zero. LCM.md replaces the complete kernel by

    integral_b^X 1_(max(m,t)<=x<lcm(m,t)) dx/x^2.

Only incomplete LCM fibres remain. This is an exact representation, NOT a
full covariance upper bound; high-lcm, nearly coprime pairs remain.

## 2. A broader bound in the actual Newton covariance

Let |c_n|<=K, support(c)<=L, D=L^2, z=c*c, and

    K_d(k)=[H_floor(k/d)-H_k+log d]/d,
    Q(k)=sum_d z(d) K_d(k).

For d<e let rho(d,e) be the distance of e to the nearest integer multiple
of d. For ALL pairs with rho<=H, including arbitrary large quotients,

    2 sum_(d<e, rho<=H) |z(d)z(e)| sum_(k>=1)|K_d(k)K_e(k)|
       <=128 K^4(2H+1)(1+log D)^2 H_(D+H)^7.

For exact multiples alone the bound improves to

    64 K^4(1+log D)^2 H_D^6.

Thus the entire near-multiple covariance has an absolute polylogarithmic
budget for fixed H, or a subpower budget for H=D^o(1). This includes both
signs and the infinite observation tail. There is NO small-prime or
squareclass restriction on the quotient; H=1 also includes consecutive
product indices. This is a structured subset of pairs, not most pairs.

The proof uses RCB26's full kernel overlap, shifted divisor counting and
weighted Cauchy. It is valid for every source in the specified capped class.
It does NOT solve the remaining source-specific cancellation problem.

Combine this with RCB26 by removing its within-core pairs first, then add
near-multiple pairs across different cores. The exact source and consumer are

    ||Q||^2 = D_S + C_near + C_far,
    F_B <=9 F_Y +2(B_RCB+B_near)+2 C_far.

The upper bound for native C_far remains OPEN. In particular, C_far<=0 is
FALSE already in the executed Y=255 case below for the displayed partitions.

## 3. Complete finite results at Y=255

Physical prime transport:

| Quantity | Rounded descriptive value |
|---|---:|
| Old empty-bank matched sector | -25.954361615499 |
| Complete divisor-comparable sector | +19.282142776300 |
| Full prime transport, unchanged | -1.661488670264 |
| Original-kernel incomparable remainder | -20.943631446564 |
| Full physical annular energy, unchanged | 0.179852003503 |
| Completed two-moment state, unchanged | 1.587579815076 |

The two remainders in the original max-kernel and the LCM boundary-kernel
representations are not interchanged. The table uses the original kernel.

Actual harmonic Newton covariance, with empty squareclass bank:

| Quantity | Rounded descriptive value |
|---|---:|
| Complete Q energy | 0.161625033385 |
| Individual-product diagonal | 9.455099959089 |
| Within-squareclass off-diagonal covariance | +3.155952925900 |
| Added exact-multiple, cross-squareclass covariance | -13.561618507824 |
| Remaining covariance after those removals | +1.112190656219 |
| Remaining covariance after also using width H=3 | +1.059222402032 |

The last positive value is a certified finite obstruction to an unqualified
'far remainder is nonpositive' shortcut. The universal bounds are deliberately
loose, and the finite values are NOT an asymptotic estimate or a new decrease
in the already-known output energy. Arbitrarily enlarging H need not improve
a signed remainder.

## 4. L-family relevance and a necessary correction

For a general source a, the comparable formula has the exact correction
involving d=1*a. For an elliptic reciprocal nu, a_E*nu=delta but in general
1*nu!=delta. Omitting this correction is invalid.

The actual good-prime E_17 example makes the failure concrete: at 7, a_7=5,
nu(7)=-5. Selecting h(7)=5 log 7 gives comparable contribution -20 log 7 on
7<=x<8, before the positive observation weight. Thus the favorable zeta sign
does NOT automatically extend to the CM family. See LFAMILY.md; prior inert
factor removal and rank-deflation results are preserved unchanged.

## 5. Executed checks and their exact scope

Seven full stages Y=3,7,15,31,63,127,255 are replayed, counting overlapping
ranges. The physical near-sector calculation covers 6,075,611 nonzero pairs;
27,519 disjoint zero cubes contain 146,728 terms. A separate implementation
checks every physical near-sector panel and full prime transport, and directly
sums 1,556,594 original comparable triples.

The harmonic producer evaluates 535,590 selected off-diagonal Gram entries
via 9,308,708 floor events, including products above the output endpoint.
It independently reproduces the known PCR26 Y=63 Q energy/diagonal values.
The verifier checks every one of 87,369 output coefficient indices and full
Q norms, completely re-sums the selected small sectors through Y=15
(1,317 Gram entries), and checks 42 additional kernel samples. Large harmonic
sector totals are producer replays, NOT independently re-summed in full.
All scalar interval primitives are shared; this is implementation cross-checking,
not independent mathematical review.

All reports use 112-bit integer-directed intervals; displayed decimals never
determine an accepting sign. The 14-test suite includes exact pointwise
closure, LCM fibres, crossed cutoffs, the elliptic counterexample, both
nearest-multiple orientations, moment/above-endpoint controls, ten altered
report variants, duplicate keys and nonfinite JSON. Tests run under -O too.

## Read and replay

Read PROOF.md, LCM.md, LFAMILY.md and VALIDATION.md. Standard library only:

```sh
python -S -B replay.py
python -S -O -B replay.py
```

Complete reports are regenerated under reports/ and authenticated against
EXPECTED.json. The chat archive also includes those generated reports.
No full Riemann-checkout validator, external formal build, zero calculation,
independent mathematical acceptance, global remainder bound or RH proof is
claimed. The next target is actual cancellation among the incomplete LCM
fibres / far cross-core Newton terms, not another unjustified sign assertion.
