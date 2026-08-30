# Independent audit: positive-kernel reverse-Rolle descent firewall

Status: exact-source review passed. The constructed example separates the
listed positive-kernel and high-derivative properties from zero-defect
descent. It is not a counterexample to RH or to an unspecified density
estimate.

Reviewed source: e2d145ce1b113c1bb87dd2bc67f717f72be74328.
Programme copy: c7397631e3d95ad7c8708ed7dd4f254440e8eb06.
Review date: 2026-08-31.

The root read the entire proof, producer, fixture, manifest and tests,
reconstructed the estimates and reran the frozen checks. A separate
reviewer independently read and replayed the same frozen identity. No
repair of the five frozen scientific files was required.

## Frozen identities

The reviewed Git blobs are:

- XI_POSITIVE_KERNEL_DESCENT_FIREWALL.md:
  3add974ec832901996002df37a34398c605c6879.
- xi_positive_kernel_descent_firewall.py:
  9462917e71a339fa824842efe4b2da0231135a01.
- xi_positive_kernel_descent_firewall.json:
  8c050d8f20af9c002aaf09f663f6071a7ba3a566.
- xi_positive_kernel_descent_firewall.sources.json:
  870e40a232e1b30df91d4c7709f27dad923bd7e8.
- tests/test_xi_positive_kernel_descent_firewall.py:
  2c694214713d83000245d42bd9bed4d531b1b0d7.

The fixture's LF-normalized SHA256 is
dc429d7abc3bc04f021ae5f1066a3b09f61f4f6dff97d92d943f1ddfa58f97cf.
All eight repository source bindings authenticate by literal commit,
path, Git blob and LF-normalized hash. The programme import preserves all
five reviewed file blobs.

## Construction and local obstruction

The reviewed normalization uses the actual half-line cosine kernel
Phi-plus=4 phi0 and full-line Fourier kernel Phi=2 phi0. Let beta be an
even unit-mass nonnegative smooth bump supported on [-1/8,1/8], let B be
its cosine transform, and put

    P(z) = cos(4z) + cos(8z)/3,
    F(z) = B(z) P(z) + Xi(z)/64,
    Fcal(z) = 64 F(z).

Fcal has a strictly positive smooth half-line kernel equal to the actual
Xi kernel outside the fixed compact interval ending at R=65/8. Its
even extension is smooth, and its entire transform is real and even.
The compact perturbation is not asserted to be frequency-real-analytic
or arithmetic. The tail coefficient of Fcal, not F, is exactly one;
this distinction matters for absolute quadratic densities.

The root checked both local obstructions:

1. The explicit simple root of P at
   z-star=(pi+i acosh((3+sqrt(17))/4))/4 has a disk of radius 1/256
   inside the critical strip. The linear Rouché reserve is 107/8192.
   On the disk boundary, abs(BP) is at least 26429/2097152 while
   abs(Xi/64)<=1/128. The remaining strict reserve is
   10045/2097152. Thus Fcal has a simple off-real zero in this disk
   and the symmetry-related zeros.
2. On the real interval centered at pi/4 with radius 1/64,
   F is negative, its derivative changes from positive to negative,
   and F-second is strictly negative. The reviewed reserves are
   F<=-245/384, endpoint derivative magnitudes at least 113/6144,
   and F-second<=-7303/1536. There is exactly one simple wrong-sign
   negative maximum.

For that interval the literal first-rung ledger is

    N(F)=0, N(F-prime)=1, r=1, iota=1, R=2, epsilon=1,
    0 = 1 - 2 + 1.

The note claims only the needed first-rung endpoint nonvanishing. It
does not assume that all higher derivatives avoid those same endpoints.

## Two distinct asymptotic checks

The proof keeps its two limiting regimes separate.

For derivative order k tending to infinity, the added compact mass is
exponentially negligible relative to a fixed actual-kernel interval
beyond twice its support. At fixed moment order j and
H<=B0 sqrt(S), its weighted relative error is bounded by

    constant * 2^(-k) (a+L)^j exp(H(a+L))
      = exp(-k log(2) + o(k)),

with the same actual saddle a and S asymptotic to 2k/log(k). The
normalizing denominator is paid. The accepted F, F-prime and F-second
bounds, growing rectangles T+H=o(sqrt(k/log(k))), both derivative
parities, and the enlarged full-disk height Hstar survive. So do the
simple real high-derivative zeros, positive Laguerre reserve and weighted
Gaussian limit. A fixed-sigma tail remains a positive Gaussian tail;
it is not relabeled exponentially small.

For xi tending to infinity at a fixed odd K, the scalar two-copy kernel
and its odd-polynomial weight are changed only when one factor lies in
the compact perturbation. The affected displacement set is contained
in xi-2R<=abs(d)<=xi+2R, with total length at most 8R. The original
global bound

    H_xi(d)/H_xi(0) <= 9 exp(-pi exp(xi) d^2)

also controls abs(d)>xi; the separately checked hyperbolic identity
pays the reflected-frequency factor in that region. The resulting
normalized perturbations are
O(exp[-(pi/8) exp(xi) xi^2]) at fixed parameters.

The reviewed normalized-observable identity is

    Etilde(A)-E(A) =
      [DeltaJ/Z - E(A) delta] / (1+delta).

It pays the changed denominator explicitly. For the current ratio,
using A=sinh(hd)/(hd)-1 preserves the factor h^2, including uniformity
as h tends to zero. Consequently the previously accepted scalar
m2, g, p, mismatch-band and current asymptotics survive with their
absolute normalizations. This does not transfer authentic Xi source
jets, its Pick matrix, or its arithmetic identities to Fcal.

## Independent reproduction

The root reran all 31 tests in normal and optimized Python, both
producer checks, Ruff lint/format checks and Git whitespace checks.
All passed. The producer also passed after import; the programme copy
was checked against the original five file blobs.

The separate reviewer reported the same 31-test and producer results,
plus 16 symbolic odd-order checks through K=31, 208 rational weight
controls, 36 signed-normalization controls, 84 compact-mass controls,
168 exponent checks and eleven guard controls. Its largest reported
coefficient used 1031 bits, below the 4096-bit cap. The author also
reported a fresh detached CRLF replay and the 48 adjacent actual-kernel
and high-derivative tests in both modes. These additional checks are
attributed, not counted as extra root unit tests.

The machine artifact checks finite exact algebra, source integrity and
declared budgets. It does not numerically certify a smooth bump,
transcendental root, entire-function zero count or asymptotic theorem.
Those claims are supported by the reviewed analytic proof.

## Prior art and acceptance boundary

The root checked
[Farmer, Section 4.2](https://arxiv.org/pdf/2008.07206):
moving finitely many cosine zeros illustrates the information that
differentiation can discard. That discussion is not claimed to prove
this exact positive theta-tail construction. The accepted
[Gunns--Hughes Theorem 3.1](https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf)
provides the classical compact-domain high-derivative comparison; the
native proof supplies the additional stated estimates. No external
priority claim is made.

Accept the explicit obstruction to inferring zero-defect reverse-Rolle
descent from the listed generic positivity, tail and high-derivative
properties. A finite off-real pair does not refute every possible
quantitative defect estimate or a proposed o(N) density bound. The
packet does not settle the Xi-specific XICURV107110 target, full native
charge, critical-line percentages, RH or GRH. Any successful descent
argument must still identify and pay the relevant defect terms.

