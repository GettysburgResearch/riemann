# Independent audit: actual full-period off-central real zeros

Status: PASS for the corrected frozen release. This audit preserves both
the original scientific packet and the separate typographic repair.

Scientific packet: 3c867a1174085cceed27901ea2bc2fda9261f5a0.
Scientific authoring base: 24bfc73fc9aa3ba115902340affa8727dfa18970.
Corrected release: a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717.
Programme scientific import: d9d12b766.
Programme release import: da741ffe920a6fcfd9e239e8d408a0a1b856466a.
Review date: 2026-08-31.

Root and a separate non-author reviewer completely read the
[proof](CUSP_PERIOD_OFF_CENTRAL_REAL_ZEROS.md), producer, fixture,
manifest and tests. Both checked the native source, analytic estimates,
all-weight threshold, inertia and precise quotient boundary. The separate
reviewer also independently checked the later three-file repair.

## Accepted result

For every k=12d>=6144, the ACTUAL full level-one cusp-period determinant
det I_k(s) has at least one real zero in (1/2,1) and a reflected zero
in (0,1/2), with equal positive finite multiplicity.

The witness is h_d=Delta E4^(3d-3), the original cusp basis vector g_1.
It is not Miller f_d=Delta^d. The theorem first establishes
I_(h_d)(1/2)>0 and then uses the positive Petersson residue to force a
singularity of the full Hermitian matrix before s=1.

This packet alone proves no uncancelled zero or pole of
Q_k=det I_k/det I_W, no sharp onset, no simplicity or uniqueness, and
no statement for every weight or every minor. It is not an RH
counterexample: the function in this theorem is not Riemann zeta.

## Normalization and primary-source audit

The completion is unchanged:

    E*(z,s)=pi^-s Gamma(s) zeta(2s)
             sum_(Gamma_infinity\SL2(Z)) Im(gamma z)^s,

with signs identified in the primitive quotient. It equals one half
of the nonzero lattice theta Mellin integral. Poisson summation in the
second coordinate gives the phase exp(2pi i m ell x), not a y-phase.

The nonzero Mellin integral contributes a factor two, cancelling the
half-lattice coefficient. Two same-sign divisor pairs for each positive
frequency and the joining of positive/negative frequencies give

    E*(z,s)=Lambda(2s)y^s+Lambda(2s-1)y^(1-s)
      +4 sqrt(y) sum_(n>=1) n^(s-1/2) sigma_(1-2s)(n)
                       K_(s-1/2)(2pi n y) cos(2pi n x).

Root independently checked this multiplicity and the cancelling Laurent
constant. At s=1/2 it is

    sqrt(y)[log(y)+gamma-log(4pi)]
      +4 sqrt(y) sum tau(n) K_0(2pi n y) cos(2pi n x).

Two genuine printed discrepancies were checked visually against the PDFs.
[Zagier, pp.276--278](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf)
fixes this completion but prints coefficient 2 in equation (14).
[Venkatesh, pp.1067--1068](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p05-p.pdf)
has the same completion and coefficient 4 in (10.6), but prints y
rather than x in the cosine. The packet explicitly records both;
its own half-lattice calculation is load-bearing, not either typo.

The [Bessel integral](https://dlmf.nist.gov/10.32),
[zeta Laurent expansion](https://dlmf.nist.gov/25.2), and
[psi value at one half](https://dlmf.nist.gov/5.4) were also read directly.
These are classical inputs, not newly proved special-function results.
Remote paper bytes are not claimed to be offline authenticated.

## Root analytic checks

1. On the full standard fundamental domain, y>=sqrt(3)/2 and
   r=exp(-2pi y)<1/100. The displayed positive Taylor sums establish
   the elementary exponential comparisons without numerical samples.

2. K_0(t)<=exp(-t)sqrt(pi/(2t)) follows directly from its integral.
   With tau(n)<=2sqrt(n), the entire nonconstant Fourier contribution
   is bounded by 4r/(1-r)<4/99. This bound is uniform in x and y
   on the domain; it does not use Fourier cancellation.

3. The exact generating function for sum n^4 r^n gives
   C(1/100)=3703670000/3169966833<2 and
   240 r C(r)<3. Thus |E4|<4 and |E4-1|<=480r.
   The finite-product inequality, followed by a monotone limit,
   gives |Delta/q|>=1-24r/(1-r)>25/33>1/2. The separate upper
   product bound gives |Delta|<1.

4. The compact part y<=32 has |E*|<43, and the rest y>=32 has
   E*>1. Area(F)<2. For h_d, the total potentially negative
   compact contribution is greater than -86*64^k and hence
   greater than the chosen -100*64^k envelope.

5. On the entire unit slab L<=y<=L+1, L=k/(4pi), and all
   -1/2<=x<=1/2, the Bernoulli bound gives
   |E4|^(6d-6)>1/2. The error reserve is valid already at k=24
   because 240*24/16^4=45/512<1/2 and k exp(-k/2) decreases.
   Combined with the Delta bound, |h_d|^2>exp(-4pi y)/8.

6. The native measure remains y^k dx dy/y^2. Therefore the slab
   contribution is greater than L^(k-2)exp(-k-4pi)/8. Replacing
   pi<4 and e<3 gives the lower bound
   [32/(k^2 3^16)](k/48)^k. No analytic period or eigenvalue
   has been substituted by a finite coefficient evaluation.

7. Positivity follows from (k/3072)^k>(25/8)3^16 k^2.
   For every integer k>=6144, the left side is at least 2^k.
   The sequence 2^k/k^2 increases for integer k>=3, since
   2k^2-(k+1)^2=k^2-2k-1>0. At the initial k=6144 the required
   right side is less than 2^54, whereas 2^6144 is larger.
   This is an all-integer proof, not an extrapolation from a
   finite threshold table.

8. The residue matrix at 1 is G/2, where G is the positive
   definite Petersson Gram. Whitening by the CONSTANT G^(-1/2)
   gives Id/[2(s-1)] plus a bounded Hermitian remainder.
   Thus I(s) is negative definite sufficiently near 1 from the
   left, for each fixed weight.

9. At the centre, the h_d quadratic value is strictly positive.
   Continuity of the largest Hermitian eigenvalue forces a zero
   strictly between the centre and the negative-definite interval.
   Positivity for real s>1 excludes an identically zero determinant.
   Analyticity gives positive finite zero order; exact reflection
   gives the same order at the distinct reflected point.
   No simple-eigenvalue branch or determinant sign change is assumed.

10. For each FIXED j>=2, Delta^j E4^(3(d-j)) is genuinely in W.
    Its own slab k/(4pi j)<=y<=k/(4pi j)+1 gives a positive
    central direction eventually in d, by the same argument.
    The positive/negative mass ratio has logarithm
    k log k-O_j(k)-2 log k, tending to infinity.
    Consequently det I_W also develops off-central real zeros
    eventually. The packet does not compare their locations.

11. Separate positive directions in the full space and W do not
    establish a relative inertia gap. At a possible common point,
    ord Q=ord det I-ord det I_W remains the exact required
    cancellation calculation. Positive Schur minimization for
    real s>1 cannot be reused at an indefinite central form.

## Alternate exact arithmetic and safeguards

The root reconstructed all ten recorded prefixes, 90 coefficients
including zeros, without using either frozen constructor. It formed
formal log E4, combined it with -24j sum sigma_1(n)q^n/n, and expanded
the exponential by integer partitions. Twelve additional native
prefixes at d=4,11,511,1000 and j=1,2,3 also matched.

Root independently differentiated the fourth-power generating function,
verified all rational envelopes, the threshold's polynomial identities,
the central Laurent cancellation, and all 32 signed lattice-pair ledgers.
Twenty-eight extra resealed semantic/type/cap attacks failed in both
normal and optimized runs, using actual complete reconstruction.

The non-author reviewer separately used a mixed Ramanujan logarithmic
derivative with E6/E4, finite Euler products and E4 divisor sums.
All ten prefixes/90 coefficients matched. Ninety additional adversarial
cases passed in EACH execution mode, including source identity/size,
frozen constructor, every analytic-scope boundary and cosine-factor
attacks. These arithmetic replays do not machine-certify the analysis.

## Typographic release and reproducibility

Root found one U+000C form-feed at line 202 of the original proof,
where a literal backslash-f in the fraction command was intended.
The separate reviewer confirmed that exact original byte defect.
Release a12d0fbc changes it to the literal command, adds two assertions
to existing test 32, and reseals only the proof/test artifact digests
and payload. Producer and manifest bytes are unchanged; every
scientific JSON field is identical. The original frozen SHA is retained.

The new assertions reject the original control character, other C0
controls, and a control-free change of the threshold fraction. Root
scanned all five release files; the peer also checked Unicode control
characters in the original and corrected files.

- Root corrected-release 32 tests: normal PASS (2.712 s),
  optimized PASS (2.685 s).
- Separate reviewer corrected-release 32 tests: normal PASS
  (2.528 s), optimized PASS (2.582 s).
- Both producers and four report/manifest emissions PASS;
  normal/optimized/fixture LF bytes match in both emission modes.
- All seven primitive identities and four artifact locks match.
- Ruff check/format and full scientific-base-to-release diff check PASS.
- Independent root arithmetic replay: normal and optimized PASS.

Corrected fixture LF SHA-256:
ea44f9b40af18e6657729b6bb2e2b2ffdf9d814c596f77d7b8542b4249406514

Corrected payload SHA-256:
d15fb8ee64ad91d8cd388a03a87ae945539e2aba91abf83e0751fad95d3c1a6b

Corrected frozen Git blobs:

    proof     0fcafec61b564a1f2db4c15d24c881d99b8ebcd1
    producer  40e65f048cf602f937e326b1e1594c08da81c471
    fixture   ec6698279aed159326220061ccf36d6cd7ae15cd
    manifest  0d5ec23bab396ccf2d16cff89247805b935706e3
    tests     4f047bf05250ea6e70f93ae06ab26903b019b2ff

This is a classical-mechanism, source-specific full-parent zero theorem.
No exhaustive novelty claim, new representation, uncancelled quotient
zero, or conclusion about RH/GRH is attached to this acceptance.

