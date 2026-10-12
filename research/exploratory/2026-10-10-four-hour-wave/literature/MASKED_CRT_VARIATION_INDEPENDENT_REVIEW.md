# Independent moving-mask and variation-tail review

Date: 2026-10-10. Full scoped mathematical/source review and finite
normal/optimized replay: PASS. The conditional uniform full-twist input,
Mertens hypothesis and hypothetical nonreal pole are not established.
No native moment upper bound or RH result follows from this review.

Frozen files reviewed:

- arithmetic/MASKED_CRT_NONRETURN.md:
  be821d39b3c4da3a61ff32b9ceb2e154853be15fe5b5da28be33c6344888f1ba.
- arithmetic/check_masked_crt_nonreturn.py:
  308e7d6a16e8247fb304beb8af9b6a5e377c4c108e4e11977716dbd07c0abb05.
- arithmetic/VARIATION_TAIL.md:
  4e4306a66731a6e57721c88231bf02028b76bd88167e2892435a0ff55c3ce3a5.
- arithmetic/test_variation_tail.py:
  e943b0ff25653b6f3a342fb3bc6789a9dc05686d8e492658e2b60ef9800fccbd.

## Moving masks and conditional nonreturn

C-M1's ideal-count constant is correct: planar covolume sqrt(3)/2
and six associates per ideal give pi/(3 sqrt(3)). The O(sqrt(y)) error
also holds for 0<y<1, where the count vanishes. This small-scale case
is needed when inclusion-exclusion runs over a large moving radical.

The coprimality inclusion-exclusion error is exactly charged to
P(h)=product(1+(Np)^(-1/2)). The squarefree d-sum retains (d,h)=1;
its harmonic error contributes log(2x), and extending its main term
has a uniform absolute O(x^(-1/2)) tail. The local Euler ratio
(1-1/q)/(1-1/q^2)=(1+1/q)^(-1) is correct. No constant hidden in the
lattice or discarded tail depends on h.

The elementary products in C-M4 have uniform fixed-epsilon constants
because each small prime occurs only once. For Nh=O(D^A), choosing
A epsilon<min(gamma,1/4) makes the main exponent 1-A epsilon strictly
larger than the error exponent 1/2+A epsilon. Taking the difference
of counts at alpha D and beta D and using W>=w0 proves the positive
mass bound uniformly in the moving b. This is a written asymptotic
proof, not an inference from the finite census.

In C-M6, v=t_D b and w=v b^5 preserve the exact nonunit mask.
At p not dividing b, the six powers of chi_p(b) cancel and the result
is -1; at p dividing b both v and w are nonunits and the result is
zero. Therefore mu(n) chi_n(w) is precisely the squarefree
coprimality indicator on the active source. No unit premise on b
has slipped into the deduction.

C-M9's contradiction is valid conditional on the declared uniform
U_B. The norm exponent is C+5A, and the gap between the positive
lower bound and U_B is (1-B)/2. I checked the cited PR #912
MELLIN_AND_SPIKES.md Section 5 at commit
6afd64e042ce7b59d550c3d76e9e2cca8b2c7379, file SHA256
f3bdeb168714d838a4b13347cd353675d9644b9629041cdf7def78dc496162e3.
Its reciprocal estimates, polynomial conductor bound and deleted
Euler estimates have exactly the uniformity used here. Applying
them to a different fixed smooth W is legitimate by rapid Mellin
decay. They do not independently prove a full-twist boundary B<1.

The physical representative limitation in C-M5 is essential and
correctly stated: the nonreturn theorem does not control the enormous
finite CRT frequency family or the norm-ball Fourier discrepancy.

## Atomic variation and the negative continuous tail

C-V1's coefficient identity holds in every local valuation case,
including exponent two at 67 and squares of other primes. The
elementary squarefree asymptotic therefore gives the complete
absolute beta count with constant (1+1/67)/zeta(2).

J has atom beta(n)n^(-3/2) at log n. Abel summation using the inclusive
prefix at Y correctly computes the strict tail n>Y, for arbitrary
real Y, including integer activations. Its constant is
2(1+1/67)/zeta(2), with O(Y^(-1)) error. The ac derivative is exactly
3e^(-u)F(e^u). Atomic and ac variations are mutually singular, so
their absolute variations add without cancellation.

Under the explicitly stated theta<1 Mertens hypothesis, the ac tail
has exponent theta-3/2+epsilon. It is lower order than Y^(-1/2)
when epsilon<1-theta. Thus the full variation has the fixed positive
atomic leading term even under a stronger assumed Mertens exponent;
this makes no assertion about an improved negative ac tail.

C-V7 uses exactly the triangle lower bound in the previously reviewed
NEGATIVE_MASS.md A-NM3 (SHA256
11a0e48a094ce262ca60224942c9bffd2207380ff55cf83dee96d5561f8f3f16).
With R(Y)=integral_Y^infinity F_-(x)dx/x^2, integration by parts gives
M_-(sigma)=R(1)+(1-sigma) integral_1^infinity R(x)x^(-sigma)dx.
The sign is positive for c<sigma<1. A finite proposed limsup implies
the boundary vanishes. The gamma integral supplies (r-1)!, yielding
the claimed constant 3|A|/[2(1-c)(r-1)!]. A nonreal pole, its actual
multiplicity and absolute Mellin convergence remain explicit premises;
the proof does not manufacture a zero or use isolated-pole inversion.

## Independent execution and source controls

The full masked checker passed normal and -O runs to /tmp. Their JSON
is byte-identical at SHA256
dc058c5113152b2ac462d7259d8b998219be98501ddbf26739276656621f2bfa.
All five scales 32,64,128,256,512 and their 25 unit/nonunit base panels
passed the actual split/inert sextic source and independent lattice
ideal census. Its Hensel lifted prime-square tests, six-associate
division, bad-prime exclusions and polynomial contradiction guards
were read independently. The finite profile is sharp, not a smooth
asymptotic test; the checker says so explicitly.

Both variation unittest controls passed in normal and -O modes,
including all coefficients through 10000, high 67-adic cases and
exact pole constants. Their unittest assertions remain active under
optimization. The timing text differs; the mathematical outcomes agree.

An additional independent symbolic/rational oracle checked the local
Euler ratio, full n-dependent ac derivative and atom, three masked
Euler-product configurations and 15 exact pole-tail constants. Its
source bindings and controls are in
`masked-crt-variation-independent-controls.json`, SHA256
7e8b0d5a28b5b83fa6daa14b9efeec74580d7362f08e60dd9d3424a66a016343.
That receipt explicitly records U_B and the Mertens hypothesis as
unproved. Neither a finite control nor this review upgrades those inputs.
