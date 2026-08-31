# Fixed compact kernels cannot suppress the complete positive candidate

This is a direct corollary of the complete canonical coefficient theorem
at `4353858fbfedc3acacb568bf8357c39a16da093f`, not a new identification of
the retained-gamma native source. It varies the observation kernel while
keeping that theorem's arithmetic coefficients, conductor weights, clean
chart and source ordering unchanged. For a kernel different from the native
kappa, the observed function is explicitly a different candidate moment.

## 1. The admissible fixed observation

Let eta be any fixed nonzero compactly supported element of L2(R), with
Fourier convention

    eta_hat(t) = integral eta(x) exp(-itx) dx,
    dnu_eta(t) = abs(eta_hat(t))^2 dt/(2pi).

Compact support and Cauchy--Schwarz give eta in L1. Differentiation under
the integral on compact subsets of the complex plane makes eta_hat entire.
It is not identically zero, by Fourier injectivity or Plancherel. Therefore
its zero at t=0 has a finite order m>=0:

    eta_hat(t)=a t^m+O(t^(m+1)), a!=0.

Consequently

    nu_eta((-delta,delta))
       ~ abs(a)^2 delta^(2m+1)/(pi(2m+1)) as delta tends to zero.       (1.1)

Every nonempty real interval also has strictly positive nu_eta mass.
Otherwise continuity would make eta_hat vanish on that interval, and the
identity theorem would make it identically zero. These statements do not
require eta to be real or positive.

## 2. The unchanged complete fibres give the lower bounds

The frozen complete-candidate theorem classifies EVERY allowed cofactor
in its selected rough conductor fibres. Its three-prime core coefficients
vanish and all surviving two-prime coefficients are positive. This is an
arithmetic coefficient statement independent of the observation kernel.
The dense seven-window owner blocks and their PNT counts in fixed
proportional intervals
are unchanged as well.

For nonnegative coefficients b_j and frequencies with abs(lambda_j)<=L,
the elementary pointwise estimate is

    abs(sum_j b_j exp(it lambda_j))^2 >= (sum_j b_j)^2/4
    whenever abs(t)<=1/(2L).                                        (2.1)

Indeed each cosine is at least cos(1/2)>1/2, so the real part of the sum
has this lower bound. Integrate (2.1) against the nonnegative dnu_eta.
No orthogonality of coefficient restrictions or comparison between two
different masks is used.

For the ratio-eight masked candidate, L=log(8) is fixed. Its small
observation interval has strictly positive nu_eta mass by Section 1.
Repeating the frozen complete-fibre count gives

    P_(B,eta)^masked(Y) >= C_eta Y^(1/2)/(log Y)^11.                  (2.2)

For the entirely unmasked candidate, the same complete-fibre theorem
gives 6U^4<N,M<=16U^6, Y=U^6. Thus one may take

    L_U=log((8/3)U^2), delta_U=1/(2L_U).

The owner/conductor count before observation contributes
Y^(1/2)/(log Y)^11. Equation (1.1) costs exactly an additional power
(log Y)^(-(2m+1)) up to fixed positive constants. Therefore

    P_(B,eta)^all(Y)
       >= C'_eta Y^(1/2)/(log Y)^(12+2m).                            (2.3)

Both estimates hold for all sufficiently large dyadic U, with constants
and thresholds allowed to depend on the FIXED eta. No matching upper
orders for the complete candidates are asserted. For the actual native
kappa, the already proved simple Fourier zero has m=1; (2.3) recovers
the frozen exponent fourteen.

## 3. What a kernel repair can and cannot accomplish

Any fixed finite number of vanishing moments of eta merely increases m.
It changes the logarithmic loss in (2.3), but the power Y^(1/2) remains.
Thus replacing kappa by another fixed nonzero compact kernel, including
one with more vanishing moments, cannot make this complete canonical
candidate's moment subpower. The ratio-eight conclusion (2.2) does not
even change its logarithmic exponent.

If a proposed comparison in the eta-observed, original conductor-weighted
Hilbert space has W_native,eta=W_B,eta+R_eta and the native moment there
is subpower, the reverse triangle inequality further forces

    norm(R_eta) = Omega_eta(Y^(1/4)/(log Y)^(11/2))       (masked),
    norm(R_eta) = Omega_eta(Y^(1/4)/(log Y)^(6+m))        (unmasked).

This implication is conditional on BOTH the exact common-space comparison
and a subpower target for that eta observation. No such native comparison
or estimate is constructed here. In particular choosing eta is not an
authorized change to the original native reduction's norm.

There is no uniform assertion for horizon-dependent kernels eta_Y: their
first nonzero derivative, order of vanishing, support, normalization or
small-interval mass could vary with Y. A noncompact high-pass kernel whose
Fourier transform vanishes near zero also lies outside the theorem. The
zero kernel is excluded. Infinite-order vanishing at zero is impossible
for a nonzero compact kernel, because its Fourier transform is entire.

## 4. Verification scope

This corollary uses the exact coefficient classification and PNT source
count in the named frozen proof, plus elementary Fourier analyticity,
the identity theorem and a local Taylor expansion. It introduces no new
source fixture, point count, numerical integral or computational test.
The analytic argument is the verification; finite sampling could not
establish its universal quantifier over fixed compact kernels. Independent
proof reading is recorded separately at the publication freeze. No full
native moment failure, number-field transfer or RH consequence is claimed.
