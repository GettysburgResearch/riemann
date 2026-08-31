# Independent review: four-node Xi positivity by a far-zero reserve

Verdict: **PASS** for the analytic theorem and bounded controls at exact
release commit `13c236591b144dd69502e831874c0505b6d8267d`.

Review date: 2026-09-01. The proof file
`XI_FOUR_NODE_FAR_ZERO_RESERVE.md` has Git blob
`2e249f288a7d57fa252a83e531427ffec205f5ab` and normalized-LF SHA256
`f7fa6a1c62edfba4eadfa46ab1cb252bc6b00407c9287b09a424a4c78362ba00`.
The theorem was preregistered at parent
`79345ae1fd7f1721b5ef3d89f135f74c0ebd02e8`; the release adds its producer,
fixture, source manifest and tests without changing the proof. No scientific
source was edited and no push was made.

## Analytic reconstruction

The stated fixed-order result is valid: for

    Y(x)=xi_R(1/2+x),  F=Y'/Y,  p(t)=F(sqrt(t))/sqrt(t),

both `p` and `t p` have strictly positive Schwarzian on `t>1/4`.
Consequently every ordinary real safe-axis matrix

    H_ij=(F(x_i)+F(x_j))/(x_i+x_j),  x_i>1/2,

is positive definite through order four when the nodes are distinct, and
positive semidefinite with repetitions.

### Squared-pole normalization and convergence

For an upper zero `z=a+ib`, the even pair factors use
`s=-conjugate(z)^2=b^2-a^2+2iab`. An off-line quartet contributes its two
distinct upper zeros and hence the conjugate pair of `s` values; a critical
pair contributes one upper zero. In both cases logarithmic differentiation
gives exactly

    p(t)=sum_i 2*m_i/(t+s_i).

Thus `w_i=2m_i` is neither missing a factor nor counting a quartet twice.
It also explains the later identity `sum w_i=2 Delta N` in a height window.
Since `|s_i|=b_i^2+a_i^2` and `N(T)=O(T log T)`, the genus-zero series and
all derivative series used in FR3 converge absolutely and locally uniformly.
Evenness removes the possible linear Hadamard exponential; no correction
term is missing.

For `q=0,1`, the algebra

    2 f' f'''-3(f'')^2
      =12 sum_(i<j) w_i w_j Re[(s_i s_j)^q(s_i-s_j)^2
                               /((t+s_i)^4(t+s_j)^4)]

has the correct unordered-pair coefficient. The double series is absolutely
convergent by the displayed difference bound and the `S_2,S_4` products.
The derivative signs are also strict: partial RH makes every nonreal pole
phase tiny, giving `p'<0` and `(t p)'>0` without an RH assumption.

### Counts, phases and the local/far comparison

The inspected Platt--Trudgian theorem proves critical-line location beyond
the chosen `H=3,000,000,000,000`. The inspected Faber--Kadiri statement
prints Rosser's constants `0.137,0.443,1.588`; its corrigendum retains them.
With multiplicity, a local pole-weight window is exactly twice the zero-count
increment, so FR5's factor two is required. The derivative of the main term
and two endpoint errors give `W_B<16 log(B+3)`. Likewise the lower main-term
increment on `(2B,3B]` exceeds both endpoint errors, so every `B>=H` has an
anchor there. Endpoint multiplicities are safely handled by one-sided limits.

A conservative wording improvement would state that the Rosser estimate is
imported only for `T>=H` (or `T>=1467`), rather than relying on the secondary
source's sharper printed lower endpoint `T>=2`. Every use in the proof is at
least `H`, so this does not affect the theorem.

For a height-separated pair the real squared-pole difference dominates its
imaginary part. Its doubled difference phase is below `6/5`; all pole and
fourth-power denominator phases add below `1/10`. Hence a negative edge must
be height-local and have a nonreal endpoint. The local absolute-row estimate
has sufficient exact coefficient

    12*32*6^q*(64/9)^4*16 < 2^28,

while an anchor edge has coefficient

    84*2^q/24^4 > 2^(-12).

The common `A^(-8)` factor preserves these inequalities for every
`t>1/4`, including unbounded `t`. Their ratio reduces to
`B^2>2^40 log(B+3)`, which follows at `H` from the stated integer bounds and
then monotonically for larger `B`.

### Infinite allocation

The allocation spends unordered pair terms, not vertices. If two lower
indices selected the same unordered edge, they would have to select each
other in reverse; the rule `b_(j(i))>2b_i` makes that impossible. Several
lower zeros may share an anchor, but `{i,j}` and `{k,j}` are distinct terms
with their own multiplicity products. Selected edges are far and positive,
so none appears in a local negative row. Every negative edge is charged by
at least one nonreal local row; double charging is harmless.

The explicit local bounds are summable against `N(T)=O(T log T)`, and FR3 is
absolutely convergent. Therefore partitioning the infinite edge series gives

    total >= sum_nonreal_i (P_i-N_i)>0

whenever an off-line zero exists. If none exists, two distinct real poles
already give a strict positive summand. No critical-line anchor or finite
same-height truncation is being assumed.

### Schwarzian-to-four-point bridge

The real-variable bridge in section 8 is complete. If
`A_f=det[1,t,f,tf]` vanished at four ordered nodes, a nondegenerate real
Möbius map would interpolate `f`. Negative orientation contradicts
monotonicity on one side of its pole; positive orientation cannot have a
pole between the extreme nodes. Thus `g=M^(-1) composed with f` is increasing,
fixes all four nodes and has `Sg=Sf>0`. But
`v=1/sqrt(g')` then satisfies `v''=-(Sg)v/2<0`, while the mean-value theorem
forces `v=1` once in each of three consecutive gaps, contradicting strict
concavity. The confluent divided-difference limit fixes the sign:

    A_f/Vandermonde -> (f'')^2/4-f'f'''/6
                       =-(f')^2 Sf/6 < 0.

Applying this separately to `p` and `t p` makes both SP16 factors negative.
The exact positive denominator makes `det H>0`; the frozen order-at-most-three
PSD theorem supplies every proper principal minor. The principal-minor
criterion then gives order-four positive definiteness. Extension and
duplication give the stated lower-order and repeated-node conclusions.

## Finite controls and scope

At exact release bytes, all 28 tests pass normally and under `python -O`;
both producer checks pass, and normal/optimized fixture and source-manifest
emissions are LF-exact. The producer/test/fixture/source-manifest blobs are,
respectively, `ae1cdb3b229d4a63a78df07a2edc61694138b3b2`,
`2c259018bc0b6512282eff4b4476f10b8e508845`,
`e764904503f7be68ac5a5e2743973290e79948f1`, and
`ece0791a5f7e505bf914d02960bd3888631a9fc8`.

The controls verify the declared exact identities and release locks; they do
not rerun the published zero computation or machine-prove the infinite
argument. The result is fixed order four on ordinary safe real nodes. It is
not all-order kernel positivity, source-kernel PSD, a zero census, or RH.
