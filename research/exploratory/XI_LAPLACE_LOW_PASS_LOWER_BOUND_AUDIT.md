# Independent exact-SHA audit: actual-Xi low-pass lower bound

Verdict: **PASS** for the frozen source and its stated conditional scope.
No scientific repair is required. This review adds no cofinal Xi-capture or
RH assertion, and does not modify any of the five scientific files.

Reviewed science: `a7479e85fdc2a464cdc753021435cfef7a1f3910`.
Preregistration: `2df9e543c07eba1f17d18043afc7dda110304b03`.
BC base: `7fbcd592042a5cc98c17d0db2fac62f8171267f2`.
Reviewer: independent non-author period/Hecke lane, 2026-08-31.
Review branch: `codex/xi-laplace-low-pass-independent-audit-pass3`, created
at the science SHA in a separate worktree. No author proof coordination,
source edits, main/front edits, or push was performed.

## 1. What is accepted

The complete frozen proof, producer, manifest, tests and structured fixture
were read. The BC and OA proofs and primitive implementations, together
with the load-bearing passages of their frozen normalization/inner-source
notes, were inspected. The full frozen positive-theta-kernel note was read.
The original preregistration already specifies all fourteen nodes, three
separate constant companion scales, four widths and eleven heights.

The accepted mathematical assertions are these:

- LB1 is a general one-kernel physical low-pass lower bound for an inner U.
- LB2 transfers a raw actual-Xi lower bound through common-inner reduction
  by two scalar modulus inequalities, without a band Loewner assertion.
- For every fixed positive lambda satisfying the inner premise, every
  locally surviving node has positive physical output in every [0,D], D>0.
- The finite Gram upper bound supplies the stated squared-HS lower bound;
  it does not identify a nonorthogonal diagonal sum with a trace.
- The weighted cofinal alignment criterion is sufficient. Its actual-Xi
  uniform Bessel and divergent-alignment hypotheses remain unproved here.
- The declared finite grid has the published strict rational norm and
  squared-HS floors, subject to the explicit pinned FLINT enclosure contract.
  Its operator interpretation, unlike its primitive evaluations, is conditional.

The proof's lines 163--167 and 190--192 retain the correct open boundaries.
Neither bare infinite height nor generic coprimality supplies the missing
physical alignment. The CP countercontrol is not bypassed.

## 2. Independent analytic derivation

With the boundary-dx Fourier convention, the inverse normalized kernel is
sqrt(2y) exp(-(y+ix)t). Its analytic image is
i sqrt(y/pi)/(z-conjugate(b)); the harmless constant phase does not change
the reproducing-kernel projection identity. For w=F^{-1}(U e_b),

    integral_0^infinity w(t) exp(-ht) dt
       = sqrt(2y) U(ih)/(h+y+ix),
    P_U e_b = conjugate(U(b)) U e_b.

Splitting the integral at D and applying Cauchy--Schwarz gives exactly
the two factors sqrt(1-exp(-2hD)) and exp(-hD) in LB1. In particular the
outer scalar |U(b)| is necessary. No multiplication-only norm is substituted
for the physical projection at proof lines 39--52.

If Theta0=Gamma U and Theta5=Gamma B, the two inequalities
|U(b)|>=|Theta0(b)| and |U(ih)|>=|Theta0(ih)| follow separately from
|Gamma|<=1. This proves LB2 because its positive-part expression is monotone
in both nonnegative moduli. A raw noncommon node survives in B. No phase of
Gamma and no inequality after inserting Pi_D into a projection order is used.

For s=1/2+h, the functional equation gives f(ih)=xi_R(s) and
f'(ih)=-i xi_R'(s). Consequently the numerator is xi_R-lambda xi_R',
not xi_R+lambda xi_R'. This reproduces the exact Cayley ratio in LB3.
The rational terms, the digamma asymptotic and the absolutely convergent
zeta derivative give ell(s)=log(h/(2pi))/2+O(1/h). For fixed lambda>0,
Theta0(ih) tends to -1. Thus 2 sqrt(hy)|Theta0(ih)| divided by
sqrt((h+y)^2+x^2) is asymptotic to 2 sqrt(y/h), and exceeds exp(-hD)
eventually for every fixed D>0. This is an analytic quantifier argument,
not a conclusion from the eleven-height grid.

The direct primary check used [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2)
for psi and [DLMF 25.4.4](https://dlmf.nist.gov/25.4.E4) for the standard
completed Xi normalization. Only these classical identities/asymptotics
are imported at this step; no quantitative uniform-in-lambda assertion is used.

For the normalized kernel synthesis map T, T*T=G and TT*<=C P_E.
For A=Pi_D P_U, positivity of A(CP_E-TT*)A* gives
sum_j ||Ae_j||^2 <= C ||AP_E||_HS^2. Since E is a subspace of K_B,
the lower bound also applies to the full input space. A separate unit-vector
test gives the operator-norm lower bound. Each sum uses just one lambda.

For the cofinal statement, h=|x|, y<=|x| and |Theta0(ih)|>=1/2 give
A>=sqrt(y/(5|x|)). The elementary inequality
[a-e]_+^2>=a^2/2-e^2 then yields

    ||Pi_D P_U e_b||^2
      >= |Theta0(b)|^2 y/(10|x|) - exp(-2D|x|).

The uniform Bessel bound, divergent weighted sum and summable exponential
error suffice by finite prefixes. No Riesz lower bound or completeness is
silently needed. Repeated-zero jets are not asserted to be covered.

The exponential-error summability is legitimately supplied by an actual
R5 zero count under y<=|x|: the frozen, correctly doubled positive kernel
satisfies Phi(t)<=C exp(9|t|/2-pi exp(2|t|)). For fixed j<=6,
|t|^j<=j! exp(|t|), followed by u=exp(2|t|), bounds the derivatives on
|z|<=R by exp(O(R log(R+2))). Also R5(0)=-i lambda f6(0) is nonzero
because f6(0) is a strictly negative sixth moment. Jensen on radii R,2R
gives O(R log(R+2)) zeros. This pays the tail condition, not Bessel or alignment.

## 3. Independent primitive and finite reconstruction

This review did not rely only on calling the producer a second time.
An independent in-memory calculation, importing FLINT but none of the three
packet modules, used 384-bit balls. It formed the reflected variable
s=1/2-i z, expanded xi_R(s+X), and multiplied the jth coefficient by
j!(-i)^j. The gamma/pi factor was formed as exp(logGamma(s/2)-s log(pi)/2),
rather than by the producer's gamma-product assembly in its z-series.

That reconstruction checked:

- all 14 exact dyadic centers and full containing rectangles;
- all 14 rational Rouché inequalities, including the factor 2^50 slack;
- 252 point/rectangle derivative enclosures through order eight against
  the frozen balls, with an independent chain rule and factorial assembly;
- all six nonzero guards at each root, and each raw Theta0 corridor;
- all 33 axis values via the full completed-Xi series quotient, rather
  than the producer's logarithmic-derivative formula;
- all 616 node/width/height values in an independent bound calculation.

The last calculation used exact Fraction arithmetic and integer-isqrt
outward bounds on a 2^-300 grid for every square root and the normalized
Gram row sum. Root coordinates retained their entire radius 2^-120.
Moderate exponentials used 384-bit outward balls; for x>=512 the elementary
e>2 bound supplied exp(-x) in [0,2^-512], so no tiny exponential was dropped.
The calculation reconstructed all twelve published strict norm and
squared-HS floors independently. It found 504 positive grid bounds and
112 zero bounds, with every node having a positive witness at each width.

For D=1/256 the independently validated strict norm floors are
0.013492, 0.009297 and 0.005122. The corresponding squared-HS floors are
0.0002733628, 0.0001128045 and 0.0000341993, respectively. The other nine
operator/width cells were checked as well, not inferred by monotonicity.

An additional exact Gaussian-rational calculation used 27 complex-node
one-Blaschke-factor controls, with three Laplace heights per control.
All 81 Laplace/projection identities and all 27 whole-line unit norms
were verified. It retained the physical scalar |U(b)| and nonzero real
parts, independently exercising conjugation and transfer orientation.

These are independent algebraic assemblies on the SAME pinned FLINT
special-function implementation, not independent implementations or a
formal verification of its transcendental enclosure algorithms.
The [official series API](https://python-flint.readthedocs.io/en/latest/acb_series.html)
was checked against the operations used. This trust boundary is explicit.

## 4. Authentication, replay, and hostile-input checks

Independent Git-object hashing used git --no-replace-objects show and the
literal blob header. All 20 declared source edges across LB/BC/OA passed
both Git blob and LF-SHA256 checks, covering 17 distinct frozen blobs.
The six direct LB bindings and all four local artifact seals match.
All five scientific files pass a C0/C1 control-character scan.
The installed native-file hash map independently reproduces all 44 files
and the aggregate runtime seal.

Fixture LF SHA256:
`1f6b37f040eff6fc9d67f98a9b9af4ff2dd0e96ac84d3019a7d15f82ee529252`.
Canonical payload SHA256:
`592f4e465a088c33521b0c41cad1329c1e4ff4d2f14b71d28fa363a587e41349`.
Runtime: CPython 3.12.10, python-flint 0.9.0, FLINT 3.6.0, Windows AMD64.
Native-file aggregate:
`36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc`.

Fresh test replay in the separate worktree:

| Module | Normal | -O |
|---|---:|---:|
| LB | 21 passed, 15.882 s | 21 passed, 16.237 s |
| BC | 40 passed, 23.162 s | 40 passed, 23.737 s |
| OA | 36 passed, 10.964 s | 36 passed, 11.917 s |

Thus 97 tests passed in each mode. Both LB --check commands passed.
Both --emit and --emit-sources outputs matched the frozen files after
LF normalization in each mode: four exact comparisons. Ruff check and
Ruff format --check passed. The entire BC-base-to-science diff passes
git diff --check and contains exactly the intended five new files.

Thirty-two additional fully resealed payload mutations were rejected
with genuine unmocked primitive reconstruction in each Python mode.
They covered physical/scalar and band-order claims, inner/cofinal scope,
arithmetic/rounding, coverage/type substitutions, source/runtime/artifact
seals, operator/root/band/height omission, lambda/axis/root boxes, raw values,
nonzero and Rouché guards, Gram bounds, omitted tails and inflated floors.
An additional twenty parser/domain/resource guards passed in each mode,
including duplicate keys, float/NaN/Infinity, byte/node/depth/bit caps,
boolean or off-grid heights, nonpositive lambda, invalid direct flag,
non-upper-half-plane nodes, nonrational widths and negative axis modulus.
No assertion-stripping acceptance path was observed under -O.

The checker requires full canonical equality with a fresh primitive report,
not merely a matching attacker-recomputed payload seal. Missing failed grid
cells and optimistic tiny-tail replacements therefore do not authenticate.

## 5. Decision and remaining gate

PASS applies only to the exact source SHA named above. Finite quantitative
band floors and the analytic every-fixed-D positivity are meaningful native
payoffs, under the existing component-inner premise. They do not imply
physical capture divergence, a high-T retained/outer-metric estimate, a
parameter-selection theorem, or RH. The first unpaid cofinal gate remains
the actual normalized-kernel Bessel bound and weighted native alignment
divergence, not an additional finite root residual.
