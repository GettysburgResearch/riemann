# The angular pole disappears, but that cancellation is already in the source

Status: **source audit and proposed next target; no new exponent.** The
complete-vector estimates in ANGULAR_COEFFICIENTS.md are quantitative
arithmetic results. They must not be advertised as a newly removed pole in
the native CT proof.

The primary check is [Dunn--Radziwill, 2109.07463v3, Propositions 5.1--5.3](https://arxiv.org/html/2109.07463v3#S5.SS6).
Its formula (5.80) is valid for every integer angular index ell. The completed
cubic sum has polar contribution exactly proportional to

    1_(ell=0) X^(5/6) W_hat(5/6).                       (1)

Proposition 5.2 states that its completed Dirichlet series is entire when
ell!=0. The more general periodic twist formulation in Proposition 5.1
has the same entire angular component under its specified finite-Fourier
support hypothesis. These are unconditional automorphic component formulas;
the conditional prime-sum conclusions elsewhere in that paper are not used.

An independent primary normalization check is OpenAI's
[angular appendix at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex).
It obtains the same indicator by multiplying DR (5.80) by G(r)theta_ell(r),
and retains the dual angular phase and all cube terms. Its transform quotient is

    Q_ell(z)=Gamma(5/6+|ell|/2-z)Gamma(7/6+|ell|/2-z)
                /[Gamma(z+|ell|/2-1/6)Gamma(z+|ell|/2+1/6)]. (2)

This verifies that no hidden angular companion pole at 5/6 survives in that
specific completed cubic architecture. It does not assert that every
arbitrary coefficient vector avoids every large-sieve obstruction.

## The native correction and the surviving principal residue

In CT v2 `lem:corrections`, the actual fixed character is

    vartheta=conjugate(Lambda) conjugate(G),
    gamma_2(P)^3=-Lambda(P),
    gamma_1(P)gamma_2(P)=-Lambda(P)G(P),
    gamma_1(P)gamma_2(P)vartheta(P)=-1.                  (3)

Lambda has angular order +1 or -1 at each complex place; G is finite order
and unramified outside the fixed S. For its Gaussian native B_m, CT
`prop:reflection` already removes the constant terms using this nontrivial
angular character. The resulting exact reflection contains nonzero
frequencies only. Thus (1)'s angular disappearance is already paid in the
estimate used by the repository.

The desired reciprocal-zeta term is not that vanished constant term. It
arises in the later joint Poisson evaluation. Its first local coefficient
uses the product of the TWO Gauss sums in (3), and is exactly -1. The
principal double residue w=1,z=1/6 has nonzero scalar

    c0=(R_S^2/6) M_W0(1/6) W1hat(1).                   (4)

This explains why removing an isolated cubic radial bias can coexist with
a surviving principal detector. It does not supply an extra cancellation
after that detector has been produced. Changing the same W0 to annihilate
Hhat(5/6) instead kills (4), by ../CROSS_ROUTE.md.

## Where the remaining estimate spends its powers

After reflection, the source separates a powerful ideal h and squarefree
d from mR=h d. The joint d,c character becomes

    chi_d(c)^3,                                       (5)

with every prescribed common-prime exclusion and higher-power local term
retained. Fixing the cube index n and the other finite data, the effective
dual squarefree length is C approximately D^2 P/Z, where P=Nh and D=Nd.
The quadratic sieve spends C+D. CT `prop:moment` records the full bound

    sum_(m in the P,D dyad) |B_m(Z)|^2
           << Z^epsilon P^(1/2) [D+D^2 P/Z].            (6)

The factor P^(1/2) pays the powerful population. Its largest-P,D aggregate
is of size Z^(2M-1+epsilon) on a norm box of length Z^M, M>1. The outer
additive probe and Cauchy--Schwarz then spend an additional square norm,
giving the physical upper bound X Y^(1/2) Z^(-1/2+epsilon).

Therefore another angular projection of the already reflected sum does
not by itself lower (6). A substantive next gain must control the
nonzero-frequency quadratic interactions for the ACTUAL coefficient vector,
or retain their correlation with the outer additive probe before the two
Cauchy/sieve steps. The full masks, cube factors, frequency dependence and
profile transforms must survive such an estimate.

GAUSSIAN_FILTER.md gives a legal two-scale change of this remaining profile,
with all target zeros retained and bounded coefficient mass. Separate
absolute estimates for its two summands reproduce (6). Identifying a
specific nonzero-frequency homogeneous component canceled by that filter
remains an open task; the radial pole in (1) cannot be used as that component.
