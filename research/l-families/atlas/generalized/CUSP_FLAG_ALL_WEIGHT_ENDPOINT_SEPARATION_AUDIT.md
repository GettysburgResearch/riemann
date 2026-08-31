# Independent audit: all-weight cusp endpoint separation

Accepted: 2026-08-31 at the exact scientific identity below.

## Frozen identity and decision

Scientific source: 98b4058ac29ba88cf993d7a3ce67579fab0c7844.
Authoring parent: 27496745df9dd49fcde17699d333a54cf8620772.
Programme import: 16ffd7a35c157abe23605142c5bc3a3f33dbd1be.

Exactly five additions were imported without changing scientific bytes.
The frozen proposed status is historical; this audit records acceptance.
Root read the full proof, producer, tests and manifest, parsed the entire
fixture and independently reconstructed its finite mathematics.
The complete EP, UQ and CF parent proofs had already been read in this
continuing pass. A separate non-author reviewer personally read the five
new files, the complete EP/CF proofs, the UQ linkage, the required CZ
bounds, and all frozen producer code executed by the new checker.

The [proof](CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md) extends effective
uncancelled endpoint-zero existence to EVERY even weight k>=65536 in
the existing canonical level-one cusp-flag family. The fine asymptotic
is uniform over the six classes, with its own non-effective onset.

## The genuinely new all-weight argument

1. The native weight decomposition is k=12d+4a+6b with
   a in {0,1,2}, b in {0,1}, and residual weight in
   {0,4,6,8,10,14}. The residue 2 modulo 12 uses residual
   FOURTEEN and d=(k-14)/12. It must not use d=floor(k/12).
   The actual witness is

       h=Delta E4^(3d-3+a) E6^b, ell(h)=[q]h=1.

   It belongs to the actual S_k. The full W=ker([q]) is unchanged.
   Replacing Miller f1 by h is unitriangular relative to that flag,
   so it preserves the canonical Schur quotient.

2. The divisor bound sigma5(n)<(5/4)n^5 and the exact power-sum
   identity give

       S5(rho)=(1+26rho+66rho^2+26rho^3+rho^4)/(1-rho)^6,
       S5(1/100)=422208670000/313826716467<8/5.

   The derivative numerator is [32,262,342,82,2], with positive
   coefficients. Thus the bound holds on the entire radial interval,
   not just at four fixture samples. Consequently on the whole
   fundamental domain, uniformly in the horizontal coordinate,

       |E6-1|<=1008rho, |E6|<277/25<16.

   E6 need not be zero-free on the low part of the domain.

3. With p=3d-3+a, the exact weight identities are

       4p+8b=k-12+2b<=k,
       2p=k/2-6-3b<=k/2.

   Together with the established Delta/E4 bounds, the first gives
   |h|^2<=2^k on the full fundamental domain. The E6 contribution
   is accounted for, not discarded.

4. Above y=log(k), rho<=k^-6 and the squared-product error is bounded by

       u=48rho/(1-rho)+240k rho+2016rho
         <=(240k+2065)rho<=289k rho<=289k^-5.

   The valid conclusion is ONE-SIDED:

       1-u<=|h/q|^2<=exp(u)<=(1-u)^-1.

   The lower bound follows from nonnegative factors and Bernoulli's
   product inequality. It is not an unsupported symmetric absolute-log
   estimate. No low-region zero-free hypothesis is smuggled in.

5. These are exactly the low/high hypotheses used in EP's mass
   comparison. Its all-integer tail induction did not require 12|k.
   Therefore the same 998/1000 and 1003/1000 comparison holds for
   the actual weight-k Gamma moments in every native class.

6. The all-W Parseval bound depends on the Fourier gap N=2 and
   the actual weight, not on a choice of residue class or basis.
   EP's completed-zeta constants 19 and 48, the same Jensen estimates,
   and the unchanged Petersson normalization therefore give

       I_s(f,f)/G_f<=-k/144+60<0
         for every f in W and 1-18/k<=s<1,
       I_(1-18/k)(h,h)/G_h>=773k/72000-2019/100>0.

   Negative definiteness of the WHOLE W block makes the quotient
   positive at the left endpoint and non-singular throughout the
   interval. Its positive endpoint residue makes it negative near
   one. An odd-order uncancelled zero follows, and reflection supplies
   the partner. The block rank argument gives corank one and nonzero
   ell on the full matrix's nullvector.

7. The six first covered weights are 65544, 65536, 65538, 65540,
   65542 and 65546 for residuals 0,4,6,8,10,14, respectively.
   Their union begins at 65536 and covers every subsequent even
   integer. The assertion is a sufficient threshold, not optimality.

8. For the sharper asymptotics the proof separately controls the
   COMPLEX ratio by product telescoping:

       |h/q-1|<=exp(v)-1,
       v=24rho/(1-rho)+480p rho+1008b rho
         <=(120k+1033)rho.

   With cutoff A log(k), A fixed for each requested order, this
   retains exact high-cusp Fourier orthogonality against every W
   vector. EP's dimension-free cross estimate, coercive inverse
   and genuine Schur correction then transfer to all six classes.

9. The scalar comparator remains exactly

       A_k(beta)=Gamma(k-1+beta)/(4pi)^(k-1+beta).

   Neither the exponent nor the leading q coefficient has a residual
   shift. Hence, uniformly for compact J inside (0,24),

       Q_k(1-c/k)/G_h
        =k(1/24-1/(2c))-(c/24+1/2)log(k/(4pi))
          +B0-1/24-c Lambda'(2)/(2pi)+O_J(log^2(k)/k).

   Here B0=(gamma-log(4pi))/2. The fine real-zero location has the
   same C12=B0-1/24-6 Lambda'(2)/pi and inverse leading slope 288.
   The finite number of classes and the uniform estimates permit
   common asymptotic constants, but do not make their onset effective.

## Independent replay and exact checks

Root passed all 32 named tests normally (3.917 seconds) and under -O
(3.849 seconds), both producer checks, four LF-byte-identical emissions,
Ruff check/format and the complete base-to-source whitespace check.
All five files also passed Unicode C0/C1 inspection.

Root's independent prefix method combined the formal logarithmic
derivatives of Delta, E4 and E6 before taking a coefficient exponential.
It reconstructed all 36 fixture prefixes and 324 coefficients, plus
36 held-out prefixes across all six classes, in normal and optimized modes.

The fifth Eulerian numerator was independently recovered by enumerating
the descents of all 120 permutations of five symbols. Its rational
generating function, monotonicity numerator and exact endpoint checked
all four radial controls. All six class onsets, low/high exponents,
complex/squared envelopes and effective reserves also passed.
A fresh formal Laurent multiplication and inversion recovered

    288 log(k/(4pi))-288 B0+12+1728 Lambda'(2)/pi.

Root checked all six retained fixed-order ledgers and rejected 30
independently resealed attacks per mode against actual full reconstruction.
No patched report oracle was used for these root attacks.

The non-author reviewer separately passed 32 tests in both modes and all
release checks. Its different sieve/discriminant/binary-power calculation
verified 36 fixture plus 84 held-out native prefixes, comprising 1080
coefficients and 86265 integer products. It additionally checked all
491521 even weights in the bounded API range; that finite enumeration was
not substituted for the all-weight proof. It rejected 106 further attacks
per mode: 42 independently resealed reports with fresh unpatched full
reconstruction and 64 type/cap/shape/JSON/source/size/pre-execution/control
guards.

## Authentication and exact scope

Ten literal source Git blobs and LF digests, four artifact seals, all
five frozen imported blobs and the payload were independently checked.
Executed source strings are authenticated before compilation. Only the
specified finite EP ledgers and CF primitive/power functions are called;
their reviewed execution does not silently read live parent scientific
files. Source-work caps are separate from local-work caps.

Fixture LF SHA-256:

    0cfd9a8742b4f9ef9eb503e6a818a87ecb27774989403f9a3f07aff49aefcf23

Payload SHA-256:

    f6a2b187cf34817d8b7b1ce34db2625a276c24f6ab641504401685a6122d62d7

Frozen Git blobs:

    proof     3e6a8d13959a69bf7f261747f65ea5e52f3d82ff
    producer  1f1ec4ba008f86de0c4ad553748aabe98cd38bef
    fixture   4174d3423c2b901f09fc320a51afbda32c5ad1f9
    manifest  1c07e50b1a25bdeed5c98a536ce561c383c174c1
    tests     4b7222beb363d83e2468c72aae757a835e5c2bfc

Classical modular and Gamma/Eisenstein inputs retain the parent proofs'
explicit primary references. This audit establishes no new modular family
or general asymptotic theory. It does not certify an optimal threshold,
6144 for the quotient, an effective fine-asymptotic onset, simplicity,
uniqueness, endpoint-escaping zero control, global zero classification,
external priority, RH or GRH.
