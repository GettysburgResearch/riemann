# STAR26 accepting arithmetic and complete source contract

**Status: proposed computer-assisted component proof, requiring independent mathematical and implementation review.** The certificate establishes the two specified fourteen-moment roots, their nonzero sixteenth-moment error, and a native zero/nonzero-triple control. It does not prove the infinite analytic statements merely by passing tests, and does not establish OPEN-STAR or RH.

## 1. Primitive source, not a stored moment table

`native_source.py:primitive` regenerates exactly the source (1) of PROOF.md. `verify.py --check result.json` always calls it. Scouting moments, optimizer residuals, zeta values, zeros, and a cached native_result.json are not accepting inputs. The rational root centers and three Fourier sample locations are input proposals only; all their mathematical tests are reconstructed.

The retained primitive cover is:

- t in [0,3]: 192 consecutive cells, center c_j=(2j+1)/128, half-width h=1/128, j=0,...,191;
- theta indices 1 through 10, every cell; 667 summands use degree-128 Taylor jets, 1253 individually small summands receive complete pointwise bounds instead;
- raw moments M_0,M_2,...,M_16;
- real Fourier arguments l,r,3(l+r)/2 as specified in the paper;
- every n>=11 on [0,3], every t>=3 for every n, and all omitted cell Taylor coefficients are bounded below. There is no unbudgeted endpoint or perpetuity truncation.

For b=9/2 and 5/2, write

    f(x)=b(c+hx)-pi n^2 exp(2(c+hx)), g(x)=exp(f(x)).

Its Taylor coefficients satisfy

    f_j=-pi n^2 exp(2c)(2h)^j/j! + b h 1_(j=1), j>=1,
    g_0=exp(bc-pi n^2 exp(2c)),
    g_k=(1/k) sum_(j=1)^k j f_j g_(k-j).

Multiplication by the exact prefactors and addition give the phi jet. For moments it is multiplied by the FULL polynomial (c+hx)^k and integrated exactly, using integral_-1^1 x^j dx=2/(j+1) for even j and zero for odd j. For Fourier values, multiply by the exponential jet of exp(iz(c+hx)) and retain total degree 128; the real part is the cosine integral. Every arithmetic operation carries its outward ball.

## 2. Complete cell Taylor remainder

Use a complex t-disk of radius R=1/16 about any cell center. Then Re t<=49/16, |Im t|<=1/16, and

    Re(pi n^2 exp(2t))
      >=pi n^2 exp(-1/8)cos(1/8)>2n^2.

The last strict inequality follows from pi>3, exp(-1/8)>=7/8 and cos(1/8)>=127/128. In particular the modulus of the negative exponential is at most one. For ANY subset of the first ten theta summands,

    |phi_partial(t)|
      <=64*3^14 sum_(n=1)^10 n^4+24*3^8 sum_(n=1)^10 n^2
      <2^46.                                                    (C1)

Here e<3 and pi<4 suffice. The integer last inequality is checked separately. Thus with h/R=1/8 the full remainder after degree D=128 is

    err_phi <=2^46*8^(-129)*(8/7).                               (C2)

The raw kth moment error over ALL cells is at most 6*3^k*err_phi. Since all three real Fourier arguments have modulus <43, on those disks |exp(izt)|<=exp(43/16)<2^5. Apply the same Cauchy argument to the PRODUCT phi_partial(t)exp(izt), with 2^51 in place of 2^46. Its full Fourier error is at most 6*2^51*8^(-129)*(8/7). This pays both the phi and weight Taylor tails, not just one of them.

A pointwise-bounded summand is skipped only after a lower ball endpoint proves pi n^2 exp(2(c-h))>=512. On the entire real cell the positive source summand is bounded by

    4 pi^2 n^4 exp((9/2)(c+h)-pi n^2 exp(2(c-h))).                (C3)

Its outward upper endpoint is multiplied by the whole cell length, the even-extension factor two, and max(1,(c+h)^k) for a kth moment. These payments are accumulated for all 1253 skipped summands. A skip never sets the source to zero without error.

## 3. All omitted theta indices and the whole real tail

Every positive summand's first part decreases on t>=0; its logarithmic derivative is 9/2-2pi n^2 exp(2t)<0. For n>=11 its maximum is therefore bounded by 64 n^4 exp(-3n^2). The successive n ratio is less than 1/2. Since exp(3)>16,

    2 integral_0^3 t^k sum_(n>=11) phi_n(t)dt
        <=768*3^k*11^4*2^(-484).                                (C4)

For the complete t>=3 tail, summing the same ratio bound from n=1 gives

    phi(t)<=128 exp(9t/2)exp(-3 exp(2t)).

For every k<=16 and t>=3, t^k<=exp(8t). Put u=exp(2t)>256, use exp(6)>256, and enlarge u^(21/4) to u^6. This gives

    2 integral_3^infinity t^k phi(t)dt
       <=128 integral_256^infinity u^6 exp(-3u)du
       <128*2^(-1024) sum_(j=0)^6
               [6!/(6-j)!]*256^(6-j)/3^(j+1).                  (C5)

It also bounds the Fourier tail, since |cos(zt)|<=1 at the real arguments used. Equation (C5) is the whole future integral and all theta indices, not an extrapolation from the last cell. The complete reconstructed record contains every separate rational remainder and pointwise-skip sum. `result.json` stores a readable binding receipt and the SHA256 of that WHOLE record. Add `--dump-full PATH_OUTSIDE_PACKET` to export all exact balls and remainders; the downloadable archive also retains that full record.

## 4. Dyadic L1 arithmetic

`ball_core.py` is byte-identical to the BRN27 implementation at commit `f21012f63adac789653e9bf6dbb8c309fa5fe7c5`, blob `2d5dd98a78d0afe279cde2610819165f4b3bef1c`. It is attributed, not independently authored again. No earlier full BRN27 numerical certificate is imported as a theorem or replayed by this packet.

A ball `(a,b,e)` encloses all complex w with

    |Re w-a/Q|+|Im w-b/Q|<=e/Q, Q=2^512.

Integer divisions round centers down and add one ulp for each nonexact component. Addition adds radii. Multiplication pays

    (|center1|_1*radius2+|center2|_1*radius1+radius1*radius2),

plus both coordinate roundings. Inversion requires max(|a|,|b|)>e; the error is bounded by twice the absolute reciprocal error using that maximum as a lower modulus bound. The factor two explicitly converts a complex absolute error to L1. Rational scaling also rounds outward.

`exp` scales to L1 norm <=1/2, computes 128 terms, adds a full tail bounded by

    2*(1/2)^129/129! <2^-512,

then squares back with ball arithmetic. Pi is enclosed by the Machin arctangent formula with alternating full remainders. Real square roots use integer square roots and an outward ulp. Gamma, logarithm and other unused functions remain in the unmodified imported core but do not enter this certificate. There is no floating special-function library in acceptance. Floating conversions in final log messages are for display only.

`controls.py` separately verifies rational arithmetic panels, biased-sign coefficients against direct moment/cumulant inversion, small complete spin enumerations and their score derivatives, the star modulus-square identity, the common-bias coupling variance, the elementary exponential/pi bounds and the disk majorant. Finite controls are not themselves proofs of the infinite statements.

## 5. Root equations and strict acceptance

`parameters.json` contains ten exact rational centers, fixed group counts, the seven active coordinates, radius 10^-24, the bias rule and the harmonic starting index. Its scope is fixed and typed: Boolean aliases, changed orders, changed multiplicities or a substituted bias rule are not permitted.

The unknowns are the seven active head weights. All target constants come from the actual source balls and the exact standardization in PROOF.md. For the infinite model the FULL tail conditional cumulants are enclosed using (30); these balls are inserted before moments and derivatives are formed. They are not differentiated as head variables.

At the center, a rational matrix is obtained from the dyadic centers of the seven-by-seven derivative enclosure. It is inverted by Fraction Gaussian elimination. Both matrix products are exactly the identity: 98 scalar checks. A hash and row norm of this reconstructed preconditioner are retained rather than hundreds of kilobytes of redundant fractions. This hash is not used in place of recalculating the inverse.

With the actual box Jacobian, compute

    delta=||R f(c)||_infinity,
    q=sup_box ||I-R Df||_infinity.

The output compares integer/rational upper bounds, requiring q<1 and delta+q*r<r, as well as positive weights and valid biases on the entire box. The same box is used for two DIFFERENT root problems (finite and harmonic). The largest retained q is below 1.267e-11. The finite delta is below 4.481e-61; the harmonic one is below 1.337e-29. Each satisfies the strict self-map inequality. Actual roots, not rounded centers, define the resulting laws.

Both roots' entire sixteenth-moment enclosures must lie in (-.115,-.114). The finite physical weights and strict positive edge-coupling enclosures are also retained; m<atanh(m)<m/(1-m^2) supplies the latter without a logarithm oracle. The native Fourier signs and the entire triple interval must pass as in (4)–(5).

## 6. Producer, verifier and refusal semantics

Run from a clean packet directory:

    python -S -B verify.py --check result.json --self-test
    python -S -B -O verify.py --check result.json --self-test

Each checks the complete file inventory and SHA256 hashes, regenerates EVERY native moment and Fourier value, reconstructs BOTH root certificates, runs the finite algebra controls, and compares the complete readable binding receipt, including the digest of the ENTIRE canonical reconstruction record. Hashes bind the executed bytes; only the actual arithmetic and paper estimates justify mathematical claims. `--emit` creates a proposed receipt and is explicitly not a stored-receipt verification. No source-only or cached mode is labeled a full replay.

The built-in self-test accepts the freshly reconstructed pristine record and rejects eight changed records plus duplicate-key JSON through the actual comparison/parser functions. These are NOT nine fresh numerical CLI reruns, and the logs say exactly what they are. A separate mutation test changes executable primitive/model code and reseals the file inventory; VALIDATION.md records its actual outcomes and scope.

All accepting logic uses explicit exceptions, not Python `assert`, so optimization does not remove acceptance checks. No Lean theorem, remote CI result, full-repository validation, or independent-author acceptance is implied by these commands.
