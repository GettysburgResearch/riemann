# Completed complete-source positivity on every interval through length one

Status: the full directed codimension-14 run and weighted/primitive replays
have accepted. Their analytic/source/implementation inputs were independently
reviewed before this run. The completed native matrices, exact coverage and
Cauchy budgets, and quantitative constant were independently accepted on
2026-10-10. See
[the completed independent review](../literature/COMPLETED_NATIVE_LOWER_INDEPENDENT_REVIEW.md).
No second full continuum integration is claimed.

For the exact native kernel W in
[COMPLETE_XI_KERNEL_BINDING.md](COMPLETE_XI_KERNEL_BINDING.md), b=3/2, define

    q_L(h,h)=b integral_0^L integral_0^L
                    conjugate(h(t))*W(t-u)*h(u) du dt,
    G_L h(t)=integral_0^t cosh((t-u)/2)*h(u) du.

The completed certificate, together with the reviewed inherited kernel,
domain and completion lemmas O1--O4 and the reviewed acceptance arguments,
gives the following native conclusion for every complex h in L2(0,L):

    q_L(h,h) >= ||G_L h||_2^2 / 1087078600000000000,
                      every 0<L<=1.                         (F1)

G_L is injective, so q_L(h,h)>0 for every nonzero native test. At L=1 the
same constant also pays ||Pi_E h||_2^2. This controls a compact primitive
norm; it is not a lower spectral gap against the native L2 norm.

## Exact finite definitions and complete continuum enclosure

At L=1 the finite space E is the L2 span of

    sin(j*pi*t), j=1,...,11; exp(t/2); exp(-t/2); cosh(3t/2).

It has dimension 14. V=E^perp has the independently proved primitive gap
6/5. The exact L2-orthonormal basis of E is defined by the exact Gram
Cholesky construction in the frozen upper producer. The trial space uses
the 100 high sines j=12,...,111 projected into V. Exact energy-Galerkin
tests z_i=e_i-u_i and their complete analytic coefficient balls are stored
in the source-U receipt embedded in the continuum file.

The full R=<Pi F_z_i,Pi F_z_j> source residual includes every literal
gamma term, prime power, complete prime tail and source constant. Its
three source cusp slabs are covered by 696 exact panels, with Gaussian
order 80 and 256-bit outward Arb arithmetic. The omitted endpoint scale
is 2^-60. The Cauchy-Gauss total FF error is below 1.869e-18 per entry,
and the complete logarithmic endpoint variation bound is below 1.976e-7.
Every endpoint neighborhood is separately enclosed; no sampled or truncated
residual replaces the complete continuum residual.

Both directed lower matrices accept the exact reserve

    U-(15/8)R >= 10^-11 I,
    U-B_128    >= 10^-11 I.                              (F2)

The first uses the scalar primitive gap. The second retains the exact
mode-dependent primitive weights and the entire cosine tail, with all
finite moments closed analytically. Positive interval LDL pivots after
subtracting the displayed reserve certify (F2). The reserve applies to
the finite normalized E coefficient vector, not to arbitrary native L2
norms. See [NATIVE_WINDOW_CERTIFICATE_FRAME.md](NATIVE_WINDOW_CERTIFICATE_FRAME.md)
for the complete native decomposition and zero-extension implication.

## Frozen receipts and replays

| Completed receipt | SHA256 |
|---|---|
| directed_residual_codim14_trial100.json | 9213accb90caa99e17172f620c3946ab638542eaf0523dfba89ab8f870d2016a |
| directed_weighted_lower_codim14_trial100.json | da0917e75a165b817c1ed7120dc17a467c88092a160f0f41da6b0b80a083b101 |
| directed_primitive_norm_codim14_trial100.json | ae6184c01dd29a107fce61eb0ab925dbfe00d5c7664b5e16106bd1a32a488e2e |

The continuum producer is frozen at
`e03d92bb09c1250b4a93e485aba6cc85bf2a4309b00e6d9217dbfbd39887cc92`.
The weighted checker is frozen at
`cc96f85d80d348bc3e2f11ab37e2b7f4c9d4eedfcda16b5a8533b32c1f1ce236`.
Its full normal and optimized replays produced byte-identical receipts.
The primitive extractor is frozen at
`a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0`.
It freshly replays the completed weighted bound before extracting any
constant; its normal and optimized receipts are byte-identical and give

    M=1, K=2717696, theta=1/200000000001,
    delta=1/1087078600000000000.

The exact derivation of these constants and their native norm implication
is [QUANTITATIVE_PRIMITIVE_COMPLETION.md](QUANTITATIVE_PRIMITIVE_COMPLETION.md).
The independent completed-matrix review is frozen at
`04eebe843815decf5f29fd11738a58c7778897b17beda168759ab15573632db9`.
Its coverage and rational-LDL oracle is frozen at
`44df44fbd91df5d6446dd243197dbe9ac63970cc66a29020b5cc720dec08cd03`.
The owner's full continuum run used python-flint 0.8.0; the independent
matrix and primitive replays used 0.9.0. The latter rebuilt the source U,
retained identical literal trial coefficient balls, and checked overlap of
every U entry before accepting the residual and lower matrix. Independent
normal and optimized weighted/primitive replays also matched exactly.

## Actual Xi binding and remaining scope

The independently accepted source identity is

    W(x)=sum_complete_rho exp((rho-1/2)*x)
                          /[(3/2)^2-(rho-1/2)^2],

with every analytic multiplicity and reflected member retained. The
arithmetic and complete-Xi zero descriptions therefore refer to the same
native kernel. The binding theorem proves RH equivalent to nonnegativity
for every native test at **every** length L>0. This certificate covers
0<L<=1, a proper bounded-window subset of that all-window criterion.
It proves neither the missing L>1 signs nor RH. It does not authenticate
a separate predecessor coefficient-trace identity.

The file labels left in the frozen producer say analytic review or source
binding is pending; those labels predate the separate accepted reviews.
The reviews and this completed receipt, not a mutation of the frozen
producer, record the current scope. The Taylor dimension-8 run is a
separate still-active full continuum computation and is not required
for (F1)--(F2).
