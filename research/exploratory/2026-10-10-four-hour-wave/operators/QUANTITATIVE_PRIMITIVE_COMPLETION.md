# A quantitative native primitive norm after the finite certificate

Status: exact conditional consequence of the reviewed weighted residual
mechanism. The completed outward finite lower receipt is still pending.
No additional numerical sign, L2 spectral gap, source adapter or RH claim
is supplied here.

This strengthens the acceptance implication in
[NATIVE_WINDOW_CERTIFICATE_FRAME.md](NATIVE_WINDOW_CERTIFICATE_FRAME.md).
It gives an explicit norm controlled by the native form, rather than only
pointwise strict positivity. All hypotheses concern the same native L=1
source, exact complement and exact Galerkin tests; no minimizer in native
L2 is assumed.

Let E have the exact L2-orthonormal basis e_1,...,e_d and let V=E^perp.
Suppose the reviewed primitive estimate gives

    q(w,w) >= kappa ||G w||_2^2,       w in V,

where kappa>0 and

    G h(t) = integral_0^t cosh((t-u)/2) h(u) du.

Thus G h is the derivative of the native initial-value primitive solving
phi''-phi/4=h, phi(0)=phi'(0)=0. Let the exact energy-Galerkin tests be
z_i=e_i-u_i, with u_i in the trial space H contained in V, and put
U_ij=q(z_j,z_i). Let B be a positive-semidefinite valid upper matrix for
the complete squared dual coupling, meaning

    |q(w,z_x)|^2 <= (x* B x) q(w,w),  z_x=sum_i x_i z_i,
    U-B >= epsilon I,               epsilon>0.

The reviewed finite weighted-cosine residual B_N has exactly this property.
Fix certified real numbers M,K with

    M >= max(1, trace B),
    K >= sum_i ||G z_i||_2^2,

and define

    theta = epsilon/(2M+epsilon),
    delta = min(epsilon/[2(1+2K)], theta*kappa/2) > 0.       (Q1)

Then every native h in L2(0,1) satisfies

    q(h,h) >= delta [ ||Pi_E h||_2^2 + ||G h||_2^2 ].       (Q2)

For a native test on any 0<L<=1, zero extension gives in particular

    q_L(h,h) >= delta ||G_L h||_L2(0,L)^2.                 (Q3)

The operator G is injective on native L2, so these are strict for nonzero
tests. They control a compact primitive norm and do not imply a positive
uniform lower bound against ||h||_2^2.

## Proof

Write h=e_x+v=z_x+w with v in V and w=v+u_x in V. Weighted Young's
inequality and the complete dual residual bound give

    q(h,h) >= theta q(w,w) + x* [U-B/(1-theta)] x.

Since B is positive semidefinite, its largest eigenvalue is at most trace B,
which is at most M. Also theta/(1-theta)=epsilon/(2M). Consequently

    U-B/(1-theta)
      = (U-B) - [theta/(1-theta)] B >= (epsilon/2) I.

Hence

    q(h,h) >= (epsilon/2)||x||^2 + theta*kappa ||G w||_2^2. (Q4)

The finite synthesis map satisfies
||G z_x||_2^2 <= K ||x||^2. Thus

    ||Pi_E h||_2^2 + ||G h||_2^2
       <= (1+2K)||x||^2 + 2||G w||_2^2.

Equation (Q1) and (Q4) prove (Q2). Literal-kernel zero extension preserves
q_L exactly. Restricting G of the zero extension to (0,L) gives G_L h;
its full (0,1) squared norm is at least its restricted squared norm, proving
(Q3). Finally G h=0 implies its primitive phi=0, hence h=0 by
phi''-phi/4=h. All steps apply to native L2 tests directly.

## Elementary certified bounds from the frozen trial coefficients

No additional source integration is needed to produce K. The Hilbert--Schmidt
bound is

    ||G||^2 <= integral_0^1 integral_0^t cosh^2((t-u)/2) du dt
             <= (1/2) cosh^2(1/2) < 18/25.

For completeness, after the 1+1/8 terms in the cosh series, the first omitted
term is 1/384 and all successive ratios are at most 1/120. Therefore
cosh(1/2) <= 9/8 + 5/1904 = 2147/1904 < 6/5.

The frozen producer uses the unnormalized high sines sin(j*pi*t).
Their L2 norms are at most one, and their orthogonal projections into V
also have norms at most one. If a_ki are the exact coefficients of u_i in
these projected high sines, then

    ||z_i||_2^2 = 1+||u_i||_2^2 <= 1+(sum_k |a_ki|)^2.

One may thus take

    K = (18/25) sum_i [1+(sum_k |a_ki|)^2].               (Q5)

The high-sine rows of exact_trial_z_coefficients_balls are -a_ki, so their
directed absolute upper endpoints bound (Q5) without a new solve. A directed
upper endpoint of trace(U-(U-B)) supplies M from the completed weighted
receipt and its fresh source-U receipt. This extraction inherits the
reviewed receipt's exact source, trial and residual provenance; it cannot
be applied to ordinary sampled matrices.
