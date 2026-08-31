# Independent audit: pure Blaschke low-pass height equivalence

Status: PASS at the exact frozen source. Independent acceptance is recorded
here; the original five-file packet and its proposed status are preserved.

Scientific source: 36eddbbf065959f535ca4a7b08455d489ed4bd18.
Authoring base: 9da33e7ea2b15a4badb3cb436e38e54762ad5e1d.
Programme import: 66e2dbb4ff92effee372a9a385fcdd69a00f1b32.
Review date: 2026-08-31.

Root and a separate non-author reviewer completely read the
[proof](HARDY_LOW_PASS_HEIGHT_EQUIVALENCE.md), producer, fixture, manifest
and tests. Both audited the analytic equivalence and its countercontrols;
no source repair was required.

## Accepted theorem

Let B be any PURE upper-half-plane Blaschke product, with multiplicities
included, and S(B)=sum Im b. With the unitary inverse Fourier convention
f(z)=(2pi)^(-1/2) integral_0^infinity h(t)exp(izt)dt and boundary measure dx,

    A_L(B)=tr(Pi_[0,L] P_KB Pi_[0,L]).

Then these conditions are equivalent:

- S(B)<infinity.
- A_L(B)<infinity for some L>0.
- A_L(B)<infinity for every L>0.
- integral_R [1-|B(x+iy)|^2] dx<infinity for some y>0.
- The last integral is finite for every y>0.

In the finite case A_L<=2L S(B). Thus infinite total height forces infinite
BARE low-pass trace for every L>0. The result requires neither separation
of zeros nor meromorphic continuation across the real axis. Repetitions,
finite-real-boundary accumulation and a constant B are handled explicitly.

## Load-bearing analytic checks

1. Finite confluent model spaces have row basis
   w_(j,r)=t^r exp(-(eta_j+i a_j)t)/r!. With w'=wA,
   G=integral w* w and c=w(0), integration by parts gives
   A*G+GA=-c*c. Consequently

       k'(t)=-|w(t)G^-1 c*|^2<=0,
       k(0)=cG^-1 c*=-tr(A+A*)=2 sum m_j eta_j.

   All real-part phases and multiplicities are retained.

2. Any enumeration of the pure zero divisor gives nested finite model
   spaces with dense union in K_B. Orthogonality to their union means
   Hardy divisibility by every finite subproduct, hence by B through
   inner factorization. This does not assume that a bounded geographic
   disk contains finitely many zeros near its real boundary.

3. Compatible finite orthonormal bases give a pointwise increasing sum
   k_B(t)=sum |h_l(t)|^2. Since every finite diagonal is decreasing,
   its extended limit is decreasing too. Tonelli and the basis
   definition of Hilbert--Schmidt norm give
   A_L=integral_0^L k_B and monotone finite-prefix trace convergence.
   Infinity is allowed throughout; finite-height sufficiency is not
   obtained by assuming trace convergence.

4. Direct evaluation of the Hardy kernel in this normalization gives
   i/[2pi(z-bar w)]. Subtracting its BH^2 projection gives

       K_B(z,z)=[1-|B(z)|^2]/[4pi Im z].

   Plancherel on the horizontal line, followed by Tonelli over the
   orthonormal basis, therefore gives the exact extended bridge

       integral_0^infinity exp(-2yt) k_B(t)dt
         = integral_R [1-|B(x+iy)|^2] dx/(4pi y).

   The factor is 4pi y, not 2pi y or a rescaled frequency convention.

5. If A=A_L<infinity, decreasing k_B satisfies k_B(t)<=A/L for
   t>=L. The weighted integral is at most
   A[1+exp(-2yL)/(2yL)] and hence finite for every y>0.
   Conversely the weight is bounded below by exp(-2yL) on [0,L],
   so finite weighted trace implies finite A_L.

6. Put q(x)=1-|B(x+iy)|^2. Half-plane Schwarz--Pick gives
   |B'|<=q/(2y), hence |q'|<=1/y. Nonnegative integrable q with
   that uniform Lipschitz bound tends to zero at both infinities:
   otherwise disjoint intervals contribute a fixed positive mass.

7. Outside a compact interval q<=1/2, so
   -log|B|=-(1/2)log(1-q)<=q. On the compact horizontal segment,
   zeros of B are finite in number and are interior analytic zeros.
   Their logarithmic singularities are integrable. This is where
   interior holomorphy suffices; no real-boundary extension is used.

8. For one zero b=a+i eta, a nonnegative logarithmic integral gives

       integral_R -log|beta_b(x+iy)|dx = 2pi min(y,eta).

   Write the half-log ratio as the integral of
   t/[(x-a)^2+t^2] from |y-eta| to y+eta. Tonelli pays the
   y=eta endpoint correctly; no logarithmic divergence is omitted.
   For a pure product the nonnegative logarithms add, so the total
   is 2pi sum min(y,eta). Finiteness of this sum is equivalent to
   finite S: only finitely many heights can exceed the fixed y.

These steps prove the converse, not merely a finite-product analogy.

## Essential countercontrols

The theorem is not a numerator-independent statement about the operators
T_I=||Pi_I M_U P_KB||_HS^2 or
C_I=||Pi_I P_(UH^2) P_KB||_HS^2.

For U=exp(i tau z), tau>=L, the shift makes BOTH low-pass expressions
zero even when S(B)=infinity. This is a nonnative example. Separately,
B=exp(i tau z) has zero zero-height sum but K_B=L^2(0,tau), giving
infinite low-pass trace. This proves why purity is essential.

The shifted-band counterexample is also valid. For zeros i256^n,
n>=1, the displayed pure Blaschke product extends meromorphically
across every finite real point and has infinite total height. Its
normalized exponential kernels have Gram bounds

    (11/15)Id <= G <= (19/15)Id,

from the geometric off-diagonal row bound 4/15. They form a complete
Riesz basis for K_B by the same zero-divisibility argument. Thus
P_KB=V G^-1 V*, and every band [A,D] with A>0 has finite trace, bounded
by (15/11)sum exp(-2A256^n). Its [0,L] trace is infinite. The two
claims are compatible and do not support a conclusion for arbitrary
shrinking bands.

## Independent exact replay

The root reconstructed the seven recorded confluent models using exact
SymPy Gram inverses and a COMPLEX-CONTOUR residue integral of the finite
horizontal modulus defect. This is independent of the producer's linear
partial-fraction system in x^2. All recorded Gram entries, inverses,
origins, weighted traces and full partial-fraction identities matched.

Four additional models retained nonzero, differing real parts together
with repeated zeros. Their complex Lyapunov identities, negative-square
derivative matrices, positive Grams and contour/weighted-Gram bridges
matched. Three held-out real-height models also passed.

Thirty exact principal minors checked the finite lacunary lower/upper
Gram envelopes. Factor, logarithmic-integral coefficient, Lipschitz
interval mass, weighted-tail and delay endpoint identities were checked
separately. Twenty-seven extra resealed semantic/type/cap attacks were
rejected with actual full reconstruction in both normal and optimized
runs.

The separate reviewer performed 626 additional checks per mode,
including 540 every-leaf resealed mutations, four independent complex
confluent contour/Gram checks and four held-out real models. These
checks support the bounded algebra; neither review calls them a
machine proof of the infinite-dimensional analytic theorem.

## Reproducibility and frozen identity

- Root supplied 32 tests: normal PASS (0.826 s), optimized PASS
  (0.818 s). Separate reviewer supplied 32 tests per mode: PASS.
- Producer --check and independent root replay: PASS in both modes.
- All four report/manifest emissions are LF-byte-identical to their
  respective fixtures and to each other across execution modes.
- Both primitive source identities and all four artifact locks match.
- Ruff check/format and full authoring-base-to-source diff check PASS.
- All five frozen files match, including a C0 control-character scan.

Fixture LF SHA-256:
22b1cae1830c0c7719c07a31ca710939ba7948dcb11f551f334aa1b84bba92e9

Payload SHA-256:
5d055216ec0c101eb9c4b2c73ffabb87f3f5ac63eb774fc6e4f618d54055cdf4

Frozen Git blobs:

    proof     d44f3b58e7dbd9ec847d771b2299c6fabc21f5df
    producer  2e8c02ab2fbec449cd44d3da0ddb422b9e1bb3d1
    fixture   148d6e086fbd88586f0957a9f03d3f449c91ba6d
    manifest  5f0132c38c52198b6ae8a61734282fe8d386e32e
    tests     237127e72c47ed4eb398e001ff5733547b259c2f

Root visually inspected the complete relevant
[Fricain--Hartmann--Ross pages 11--12](https://arxiv.org/pdf/1605.07418v2)
and directly read
[Tao's Schwarz lemma and disk automorphisms](https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/).
The classical kernel and Fourier normalizations agree after the
explicit convention conversion. Remote bytes are not offline locked.

Under EXACTLY GH's existing inner/RH premise, both unreduced actual-Xi
companion components therefore have infinite bare [0,L] trace. This
does not determine the reduced denominator after common-inner cancellation,
control the native numerator or corrected physical projection, prove
cofinal physical failure, or settle RH. No exhaustive novelty or new
abstract Hardy theory is claimed.
