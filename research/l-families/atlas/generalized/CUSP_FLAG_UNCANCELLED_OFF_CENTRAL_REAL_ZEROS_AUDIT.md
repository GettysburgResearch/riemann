# Independent audit: uncancelled canonical cusp-flag real zeros

Accepted: 2026-08-31, at the exact scientific source below.
This is a theorem about the actual canonical period quotient, not zeta.

## Frozen identity and accepted conclusion

Scientific source: bcd3ad5ff0c42e7b205663b68a010e2dbde6d941.
Authoring parent: a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717.
Programme import: 97b24811ada2d9ff9a2d3641b5811a0683c810ba.

Exactly five additions were independently reviewed. Their PROPOSED
status is retained as frozen history; this separate audit records
acceptance without changing their scientific bytes.

For the literal level-one space S_k with k=12d, ell(f)=[q]f and
W=ker ell, write Q_k=det I_k/det I_W in the existing completion.
The [proof](CUSP_FLAG_UNCANCELLED_OFF_CENTRAL_REAL_ZEROS.md) proves that
for every sufficiently large such weight:

    I_W(s) is negative definite throughout [1-18/k,1).
    I_(Delta E4^(3d-3))(1-18/k)>0.
    Q_k has an uncancelled zero in (1-18/k,1),
    and an equal-order reflected zero in (0,18/k).

At least one pair has odd zero order. The denominator is nonzero on
both intervals. At these zeros the full matrix has corank one and its
kernel has nonzero first coefficient. The canonical inverse-matrix
observable 1/Q has a genuine pole.

The onset is existential. This acceptance DOES NOT inherit the separate
full-parent threshold 6144, certify another numerical threshold, or assert
simplicity, uniqueness, all weights, or a theorem about every cusp minor.

## Independent analytic review

Root read the complete proof, producer, manifest and test source, parsed
the fixture and checked its finite data independently. The relevant
complete frozen CF and CZ proofs had already been read and reviewed in
this continuing pass. The separate non-author reviewer read all five new
files and the complete relevant parent notes, and checked the same exact
scientific identity without author contact or edits.

The main points that make this more than a full-parent zero argument are:

1. The first-q flag is an actual Fourier vanishing condition. For ANY
   cusp form whose coefficients below N vanish, Parseval on the full
   cusp rectangle and integration by parts give

       integral_F max(1,y) y^k |f|^2 dmu
           <= [1+(k-1)/(4pi N)] G(f).

   The boundary term at y=1 is retained. Below y=1, max(1,y)=1.
   Tonelli applies to the nonnegative Fourier coefficient sum.
   Setting N=2 covers every complex vector in W, including every
   cross term. No basis-vector census or free coefficient choice is used.

2. The exact CF/CZ Eisenstein completion has the decomposition

       E*(z,sigma)=Lambda(2sigma)y^sigma
                   +Lambda(2sigma-1)y^(1-sigma)+R_sigma(z).

   The half-lattice normalization gives the cosine coefficient 4 sqrt(y).
   For orders 0<=nu<=1/2, the positive-real K integral bounds K_nu
   by K_(1/2). Thus, with r=exp(-2pi y)<1/100 on F,

       |R_sigma(z)| <= 2 sum_(n>=1) n r^n < 1,

   uniformly for 3/4<=sigma<1 and throughout the domain.

3. With epsilon=1-sigma, the fixed special function has

       Lambda(2-2epsilon)=pi/6+O(epsilon),
       Lambda(1-2epsilon)=-1/(2epsilon)+O(1).

   Both remainders are uniform on one punctured interval, independent
   of k and f. The negative constant term must use y^epsilon>=a^epsilon,
   where a=sqrt(3)/2. Multiplication by a^epsilon changes its singular
   part by O(1); simply assuming y^epsilon>=1 would be wrong below y=1.

4. The all-W moment bound then yields, simultaneously for every f in W,

       I_f(1-epsilon)/G(f)
           <= k/48-1/(2epsilon)+O(1)
           <= -k/144+O(1)<0,  0<epsilon<=18/k.

   The C-coefficient error is O(epsilon*k)=O(1). The other errors are
   absolute constants. This proves negativity on the ENTIRE interval
   for all sufficiently large k, not only at one point.

5. The outside witness is the actual g_1=Delta E4^(3d-3), with ell=1.
   It is not Miller f_d. For all beta in [0,1], its moment is compared
   with Gamma(k-1+beta)/(4pi)^(k-1+beta).

   On y>=log k, the actual complex modular products satisfy a uniform
   relative squared-modulus bound 1+O(k^-5). Below log k, the bound
   |Delta|<1, |E4|<4 gives at most (2 log k)^k.
   A comparison-integral lower bound on
   [k/(4pi),k/(4pi)+1] makes that ratio smaller than every fixed power
   of 1/k. This proof is uniform in beta and in the growing dimension.

6. Integrating the positive-real digamma estimate over an interval
   of length beta proves the required UNIFORM Gamma ratio.
   At epsilon=18/k, the two normalized moments give

       I_(g_1)(1-18/k)/(k G(g_1))
           =1/24-1/36+O(log k/k)=1/72+O(log k/k)>0.

   The full low-cusp period contribution is controlled either by the
   same decomposition or its O(k+log k) multiplier. No integral,
   eigenvalue, or zero sampling is used.

7. In the adapted basis (g_1,f_2,...,f_d), the W block D is negative.
   Therefore the actual Schur quotient a-b^t D^-1 b is at least a>0.
   This is Schur algebra after negative definiteness, not an indefinite
   minimization principle.

8. The existing positive Petersson residue gives
   Q_k(s)=r_k/(s-1)+O_k(1), r_k>0. For each fixed eligible weight it
   is negative sufficiently close to 1. A common near-pole neighborhood
   across all weights is neither required nor asserted.

   The denominator is nonzero along the whole real path. Holomorphy,
   real type and the sign change force an odd-order zero.
   Block elimination proves corank one and nonzero ell on its kernel.
   Nonvanishing det D proves that this zero cannot cancel.
   Entrywise reflection transfers everything to the other endpoint.

The earlier central positive W witnesses do not contradict item 4:
they concern s=1/2, outside this shrinking near-endpoint interval.

## Replay, source locks and independent finite mathematics

Root's named suite passed 32 tests normally (5.120 seconds) and under
-O (4.997 seconds). Both producer checks, Ruff check and format, and the
complete authoring-base-to-source whitespace check passed.

Root's separate exact reconstruction passed in BOTH modes:

- 13 incomplete-Gamma polynomials obtained by differentiating
  exp(-c)/c symbolically, after removing the exponential;
- all 48 recorded tail arrays, positive gaps and rational ratios;
- eight actual modular prefixes, 72 coefficients, reconstructed by
  formal logarithmic differentiation and exponentiation;
- all three actual Miller flags, using a dense inverse of the separately
  reconstructed integral leading-coefficient matrix;
- four native scale margins, four modular envelopes and 24 held-out ratios;
- 27 independently resealed attacks against actual full reconstruction;
- all ten primitive Git-blob/LF bindings, four artifact seals, five frozen
  imported blobs, and four LF-byte report/manifest emissions.

The non-author reviewer independently reconstructed all 48 tail controls,
eight prefixes and three flags by other finite arithmetic routes.
It passed 32 tests in each mode and separately rejected 32 resealed report
attacks, six manifest attacks, five constructor attacks and 33 cap/type/
parser attacks per mode. Three resealed attacks additionally exercised
actual reconstruction instead of a substituted baseline.

Fixture LF SHA-256:

    cc120e9d2af305db0e26fbb7a3635062b94eb3cf95d34c1f58d8168e41b1acce

Payload SHA-256:

    eb9ed773298162876d456abc91fb2d26fa62754b4d0a6733ad31548ec782e98f

Frozen Git blobs:

    proof     5c6472b64dc70930bba76dea115ea8e745233c8d
    producer  816dbff2bd777bdec0322eb27d60e2064f32c544
    fixture   0c569db7bf4336cc987e1187421747eefb1ecaee
    manifest  42f86fe7bd6a40250ff5fd69f4047c6aea4e17ce
    tests     e2697a6bdb4a71bdc4503ba7c35c1539acb3e8fb

Finite arithmetic and hashes authenticate the stated finite controls and
source identities. They do not machine-prove the uniform analytic limits,
the existence of k_0, the number or location of actual zeros, or RH.

## Primary inputs and scope

The classical inputs are Parseval, Tonelli, integration by parts,
the existing Eisenstein continuation and residue, and Schur algebra.
Root directly checked the additional
[K integral](https://dlmf.nist.gov/10.32.E9),
[half-integer K value](https://dlmf.nist.gov/10.39.E2), and
[digamma expansion and positive-real remainder](https://dlmf.nist.gov/5.11).
Their positive-real hypotheses match the proof. The root and non-author
reviewer also visually checked the relevant Zagier/Venkatesh pages in the
parent normalization review. The documented printed discrepancies are
not silently imported or rewritten.

This accepts a native canonical-quotient off-central real-zero theorem.
It does not assert a new automorphic family, a positive Weil formula,
a critical-line law for this quotient, a zeta/RH counterexample, or
exhaustive external novelty. Denominator zeros elsewhere and the global
separate unsigned zero/pole distributions remain independent questions.
