# Independent audit: all complex weight-24 period flags

Verdict: **PASS**, with no actionable scientific or certificate-contract finding.
Reviewed source: `7d59b841e522d6afe2ec59c3986416489554deea`.
Parent: `ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf` (FI).
Date: 2026-08-31. Reviewer: independent non-author period/Hecke lane.

The five scientific files, the five frozen FI inputs and the separate FI
review were read. All six direct bindings were authenticated. This audit
was conducted in a new worktree on branch
`codex/cusp-weight24-complex-flag-independent-audit-pass3`, initially at the
exact science SHA. There was no author coordination for proof acceptance,
scientific-file edit, front/main change, or push. The review does not certify
effective widths, divisor locations, simplicity, exact unsigned asymptotics,
optimal escape exponents, or RH.

## 1. The actual complex-flag quotient

Proof lines 16--77 retain the actual full-domain completed Eisenstein period.
Direct unfolding with Gamma_infinity including -I gives

    I_s(f_i,f_j)=A(s) zeta(2s)
       sum_n a_i(n)a_j(n) n^(-s-23),
    A(s)=pi^(-s) Gamma(s) (4pi)^(-s-23) Gamma(s+23).

The eigenforms have real Fourier coefficients, so the cross entries agree
meromorphically, without inserting conjugation of s. The local Hecke identity
has numerator 1-X^2; zeta(2s) removes that numerator, giving the matrix
A[[ZS_+,C],[C,ZS_-]]. The cross period remains nonzero. Choosing an eigenbasis
does not diagonalize the Eisenstein period matrix.

For normalized coefficients a,b, the congruence is P* I P, not P^t I P.
Its line entry is A D_W with D_W=pX+qY+dC and d=2 Re(conjugate(a)b).
The complementary vector (-conjugate(b),conjugate(a)) makes det P=-1,
so Q_W=A N/D_W, N=XY-C^2. This uses a coordinate-Euclidean normalization,
not a Petersson normalization. For an unnormalized pair of squared norm S,
normalizing the pair first gives A S N/D_un, as in line 75. Using both raw
unnormalized vectors instead would multiply the result by S; that harmless
positive scalar is not being used as the canonical FC4 normalization.

For the antidiagonal line, p=q=1/2,d=-1, D_W=H/2, hence Q_W=2Q_1.
All divisors agree with the original FI quotient on that line. Conjugate
flag coordinates have the same p,q,d and hence the same quotient, as the
finite controls record. There is no holomorphic dependence on the flag
coordinate being assumed.

## 2. Imported joint-value theorem and cancellation protection

The four Euler products are the same verified FI inputs of degrees 1,3,3,4.
The level-one GL2 representations are non-dihedral and not twist equivalent:
a possible twist must be quadratic, finite ramification contradicts their
unramified local parameters, and no nontrivial quadratic character of Q is
unramified at every finite prime. The trivial twist is excluded by distinct
T2 eigenvalues. The two symmetric-square coefficients at two differ by
25920 sqrt(144169)/2^23. Thus the degree-three inputs are distinct too.
Deligne's unit-modulus GL2 Satake parameters give the required finite-place
Ramanujan bounds for the explicit lifted parameters.

The primary passages were rechecked, including visual inspection of
[Gelbart--Jacquet Theorem 9.3(3), p.534](https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf)
and [Ramakrishnan Theorem M, p.54](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf).
Their cuspidality hypotheses match these inputs; no new automorphic
representation or unproved general GL4 Ramanujan assertion is introduced.

[Booker--Thorne Proposition 3.1, p.2034](https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf)
does supply the closed coordinate annulus using one common prime phase
system. The contour/vertical-shift mechanism on pp.2040--2041 was read too.
Both pages of the [2018 correction](https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf)
were checked: its repaired error still tends to zero and preserves the
needed proposition. No rate from the incorrect original uniform estimate
is used. Taking prime cutoff 3/2 includes every prime, with no omitted
finite Euler factor.

For a mixed line p,q>0, direct substitution into FC5 gives

    D_W=0,
    N=(1-pq-id)/q^2,
    Re N=(1-pq)/q^2 >= 3/(4q^2)>0.

This remains true when d=0, so an imaginary mixture is not an exception.
All four target coordinates are nonzero. If p,q>=epsilon>0, the radius
R=2/epsilon^2 bounds every target modulus above and below as claimed.
For zeros, C=sign(d), with sign(0)=1, and Z=S_+=S_-=1 give
N=0 and D_W=1+|d|>=1. The fixed annulus R=2 works for every line.

These targets alone are not treated as a divisor proof. D_W has coefficient
1+d at index one. If it vanishes, the unique possible weights are
p=q=1/2,d=-1, and index two is 1297521/262144, not zero.
N has nonzero index-two coefficient 1297521/131072. A common prime twist
multiplies the first nonzero coefficient by chi(n), so neither function
becomes identically zero. In particular the square-divisor multiplier from
zeta(2s) must also be twisted: chi(m^2), not 1. This was independently checked.

## 3. Entire tails, counts, and compact-uniform quantifiers

The coefficient bounds 2 d_4(n) for D_W and 2 d_8(n) for N are uniform in
all normalized flags and common phase systems. They follow by Dirichlet
convolution from the Euler degree bounds, not pointwise multiplication.
Their full tails tend to zero uniformly on every Re s>=sigma_1>1, by FI13.

At the pole target, a sufficiently small closed disk has N_chi nonzero
throughout and D_W,chi nonzero on the boundary; isolated zeros exist because
the latter is not identically zero. One finite cutoff and one open prime-phase
box approximate both functions there, with both twisted and untwisted tails
paid. Rouche gives a denominator zero, while the full-disk numerator margin
prevents cancellation. Interchanging the targets gives genuine zeros.
A is holomorphic and nonzero throughout these disks and their vertical
translates, so it needs no almost-periodic approximation.

Positive lower density of good positive shifts follows from the finite
torus flow and rational independence of prime logarithms. A fixed divisor
belongs to a translated radius-rho disk for at most 2rho measure of shifts.
This proves distinct-point linear lower counts, without bounding divisor
multiplicity or asserting simplicity.

For a compact set of mixed lines, p and q have a positive common minimum,
so the annulus argument gives one positive width. At a fixed substrip,
strict contour and full-disk margins persist in a flag neighborhood.
There is also uniformity in the vertical shifts: on Re s>=sigma_1 the
absolute Euler/Dirichlet bounds uniformly bound X,Y,C, and the finite-prefix
approximation and omitted tails can therefore be chosen uniformly on that
neighborhood. A finite subcover supplies a minimum positive count constant
and maximum onset. No continuity of the selected infinite phase systems is
needed. The identical argument for the zero targets applies on all CP^1.

For either eigenline the denominator is X or Y, a nonvanishing Euler product
on Re s>1. A and N are holomorphic there, so that quotient has no poles.
This does not say that the quotient has no zeros, or confuse Q_W with the
scalar eigenline period I_s(w,w). Combined with the protected pole construction
for every mixed line, it proves exactly the claimed two-line classification.

## 4. Uniform-in-height escape bound

In Y/X, the common zeta factor and common symmetric-square (1-X)^-1
factor cancel. There are two remaining factors on either side, not three.
Thus the correct factor count in the stated elementary estimate is

    |Y/X| <= M4(sigma)=zeta(sigma)^4/zeta(2sigma)^2.

The four-versus-four estimate for C/X gives
M8(sigma)=zeta(sigma)^8/zeta(2sigma)^4. These are complete absolutely
convergent products, uniformly bounded in the imaginary part. Their positive
local majorants decrease with sigma. Hence FC13 excludes denominator zeros
on the entire closed half-plane Re s>=sigma_0, not just on a bounded contour.

For 0<delta<=1, zeta(1+delta)<=2/delta gives M4<=16 delta^-4 and
M8<=256 delta^-8. With

    delta_r=4 max(|r|^(1/2), |Re r|^(1/8)),

the two terms are bounded by 1/16 and 1/128. Their sum is 9/128<1.
The condition delta_r<=1 is retained. For purely imaginary r the second
term vanishes exactly. Exchanging the eigenlines gives the other chart.
Therefore the stated sufficient horizontal widths tend to zero as either
eigenline is approached, uniformly in height. They are not asymptotic pole
locations or optimal exponents. A single positive width for every mixed
line would contradict this exclusion on a fixed substrip, so its failure
is proved rather than merely left unestablished.

## 5. Independent exact finite reconstruction and replay

An independent helper imported no author module. It reconstructed
Delta=(E4^3-E6^2)/1728 through q^64, a different route from FI's logarithmic
recurrence and the resident tests' Euler product. Put G_n,J_n,B_n for the
square-divisor lifts of g^2, gb and b^2, respectively. The helper used

    D_n = (1+d)G_n
       + [1080(1+d)+24(p-q)sqrt(d0)]J_n
       + [540^2+144d0+d(540^2-144d0)
                            +12960(p-q)sqrt(d0)]B_n,

where d0=144169. All 2048 quadratic-field coefficients for the 32 flags agree.
It independently checked all 128 inherited H,N coefficients from the
coefficient-basis Gram determinant, including every square-divisor term.
The reconstruction passed normally and under -O.

Further independent exact checks covered 2712 admissible rational mixed-weight
triples and their protected pole/zero targets and annuli; 96 common-twist
square-divisor identities; 35 complex congruence matrices with arbitrary
complex symmetric entries; and the symbolic common Euler-factor cancellation.
These bounded checks support the written universal algebra, not the analytic
prime-twist existence theorem or a numerical zero census.

Fresh tests in the separate worktree:

| Module | Normal | -O |
|---|---:|---:|
| CF | 32 passed, 39.623 s | 32 passed, 32.341 s |
| FI | 32 passed, 13.070 s | 32 passed, 13.956 s |

Both CF producer checks passed. The fixture and manifest emits match the
frozen LF bytes in both modes, for four exact comparisons. Twelve CF/FI
source bindings were independently authenticated with replace objects disabled,
literal Git blob headers and LF SHA256. The four CF artifact hashes and
canonical payload seal match, and all five files pass the C0/C1 scan.

Fixture LF SHA256:
`00e277e28856f38fc2b8485c0551badf8d44aaee9086ace93031d96e6e88f919`.
Payload SHA256:
`3a4ba5065eddd60d0717e7a0c01a3da7646a45108977abd516d2cad3a3f82786`.
The recorded work is 316053 under the fixed 1000000 cap; fixture size is
560836 bytes, below the 3000000-byte cap.

Thirty-two additional fully resealed mutations were rejected by unmocked
validator calls in each mode (35.562 s normal, 39.235 s optimized).
They covered schema/base/weight/field/scope/taxonomy, omitted or duplicated
flags and coefficients, conjugation weights, targets and cancellation guards,
annuli, M4/M8 data, escape budget, canonical scale, prime cutoff and seals.
Twenty-five additional strict parser/domain/resource checks passed per mode:
bool/null/float/nonfinite/duplicate inputs, byte/bit/depth/node/container/string
caps, work limits, nonreduced or zero-denominator rationals, and invalid weights.
Fresh reconstruction, rather than merely the attacker-recomputed seal, controls
acceptance. No assert-dependent acceptance gate was found.

Ruff lint and format checks passed. The entire parent-to-science whitespace
check passed and contains exactly five new files. No frozen scientific
content, test cache, source archive, or unrelated file was altered by this audit.

## 6. Final boundary

The exact-SHA packet establishes the stated all-complex-line classification,
protected zero/pole counts, compact-uniform versions and sufficient pole-escape
bound for the actual weight-24 period family. It makes no effective onset,
sharp exponent, simplicity, unsigned asymptotic, new representation, or RH
claim. No mathematical repair is required for this scope.
