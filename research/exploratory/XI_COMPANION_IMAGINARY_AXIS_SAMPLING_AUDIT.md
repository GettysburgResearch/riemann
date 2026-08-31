# Independent audit: native Xi imaginary-axis companion sampling

Accepted: 2026-08-31 at the exact source below.
The axis theorem is unconditional. Its inner-factor and physical-operator
consequences retain their explicit conditional premise.

## Identity and decision

Scientific source: d38961c15fc76d671cef4fddfc92d3c866af4fd5.
Authoring parent: 7aed2ec0b99b9d7f2fb94a774922a83d5b84a870.
Programme import: 3325f1033d7a47b5e9ef738090876b8f3ce53468.

Exactly five additions were imported without editing their scientific
bytes. The proposed status in the frozen note is historical; this
separate audit records acceptance.

Root read all five files completely, parsed the entire fixture and
independently reconstructed its finite mathematics. The relevant frozen
parent notes had already been read in this continuing pass. A separate
non-author reviewer independently read the five additions and all six
complete pinned notes, including historical L/T via their exact Git
objects. The packet's tests were written by the author team; that replay
alone was not treated as independent scientific acceptance.

## Actual-source analytic argument

The [proof](XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md) uses the unrescaled
actual Xi kernel Phi=2 phi_0. It does not substitute a finite atomic model.

1. Put h(y)=Xi(iy), D0=h'/h and D5=h^(6)/h^(5). Evenness of Phi
   justifies either sign in the exponential defining h. Its positive,
   superexponentially decreasing density makes all tilted moments finite.
   The exact phase f^(r)(iy)=(-i)^r h^(r)(y) gives

       Theta_k(iy)=(1-lambda D_k)/(1+lambda D_k), k=0,5.

   The denominators do not vanish for y>0, without assuming RH.

2. D0' is the strictly positive tilted variance. Since D0(0)=0 and
   the frozen fixed-function asymptotic makes D0 tend to infinity,
   Theta0 has exactly one positive-axis zero iy0, and that zero is simple.

3. Symmetrizing the covariance gives

       K=h h^(6)-h' h^(5)
        =1/2 integral integral (u-v)(u^5-v^5)
          Phi(u) Phi(v) cosh(y(u+v)) du dv
        >=mu0 mu6>0.

   The fifth power is strictly increasing on the whole real line.
   Hence D5>D0. Separately, yu cosh(yu)>sinh(yu) for u,y>0
   gives yD5>1. Every positive-axis Theta5 zero therefore satisfies

       lambda<y<y0(lambda), Theta0(iy)>0.

   At such a zero, the proof also gives the strict fixed-lambda bound
   Theta0(iy)>mu0 mu6/[2h(y0)h^(6)(y0)]. This is not uniform as
   lambda tends to zero and is not an estimate on an off-axis sequence.

4. Writing g=h^(5) and H=gg''-(g')^2, the full-quadrant kernel is

       Q_uv(y)=1/4[(u-v)^2 cosh((u+v)y)
                         -(u+v)^2 cosh((u-v)y)].

   The factor is 1/4 for the FULL quadrant, not 1/2.
   Q_uv(0)=-uv; its derivative is strictly positive for u!=v,y>0.
   Thus H(0)=-mu6^2 and H'(y)>0. Superexponential decay justifies
   the differentiations and Fubini on each compact y interval.

5. Subtracting Q_uv(0) before integrating leaves a nonnegative
   integrand. On a compact rectangle with separated positive u,v,
   its growing term dominates uniformly and tends to infinity.
   Thus H tends to infinity, without subtracting divergent integrals.
   H has exactly one zero with strictly positive derivative.
   Consequently D5 has exactly one nondegenerate global minimum.

6. If lambda_* is the reciprocal of that minimum, Theta5 has
   exactly two simple positive-axis zeros for 0<lambda<lambda_*,
   one double zero at equality, and none above the threshold.
   Nondegeneracy proves exact complex-analytic multiplicity; a real
   sign-change argument alone would not establish the double case.
   No numerical threshold is claimed. A one-atom control does not
   satisfy the actual-kernel support hypotheses for this trichotomy.

7. Analytic inversion of h^(5)/h^(6) at zero gives the small branch

       y5^-=lambda+(mu8/(3mu6))lambda^3+O(lambda^5),
       Theta0(i y5^-)=1-2(mu2/mu0)lambda^2+O(lambda^4).

   The moments belong to the one fixed actual Xi function. The limit
   changes the constant lambda, not the underlying kernel.

8. The frozen GH differentiated estimates give
   D5-D0~5/(y log y), D0'=1/(2y)+O(y^-2), and
   D5=(1/2)log(y/(2pi))+O(y^-1). First obtaining relative
   equivalence to 2pi exp(2/lambda), then exponentiating the O(1/y)
   logarithmic error, gives additive O(1) for both large roots.
   The mean value theorem then gives

       y0-y5^+~10/log(y5^+)~5lambda,
       Theta0(i y5^+)~5/[y5^+ (log(y5^+))^2] ->0.

   No unspecified remainder is differentiated.

## Conditional physical interpretation and its limits

Assume both companions are inner for the lambda values considered;
RH is a sufficient single premise. GH then makes them pure Blaschke
products. If Theta0=G U and Theta5=G B after maximal common-inner
reduction, the no-common-axis-zero result shows that every denominator
axis zero survives in B, with its original multiplicity.

At such a zero b,

    |U(b)|=|Theta0(b)|/|G(b)|>=Theta0(b)>0.

The inequality points this way because |G|<=1. The small raw sample
therefore supplies a reduced-numerator lower bound. The large raw sample
does NOT supply a reduced-numerator upper bound tending to zero.

The actual corrected source is P_U=M_U M_U*, projection onto U H2.
It is neither multiplication M_U alone nor projection onto K_U.
A normalized reproducing kernel e_b at a zero of B belongs to K_B and

    ||P_U e_b||=|U(b)|.

The surviving small-axis zero consequently proves

    ||P_U P_KB||_op ->1 as lambda->0,
    ||P_U P_KB||_HS^2 >=1-4(mu2/mu0)lambda^2+O(lambda^4),

where the latter squared norm may be infinite. This excludes CP's
synthetic global bound <1/9 uniformly for this actual small-lambda family.

It concerns ONE direction with real part zero. It proves neither a
divergent trace at any fixed lambda nor a lower bound for every output
band. This direction is not retained in the native high-T geographic
windows. No high-T local capture or total-charge conclusion follows.

The exact remaining source bridge is

    R5=R0^(5),
    Theta0-Theta5=2i lambda (f f^(6)-f' f^(5))/(C0 C5),
    U-B=2i lambda (f f^(6)-f' f^(5))/(G C0 C5).

At a reduced zero of multiplicity q, the remainder's value jets through
order q-1 equal those of U. The physical coefficient matrix is their
adjoint, with the retained outer metric. Imaginary-axis positivity does
not control the oscillatory Fourier integral at other points.

## Verification independent of the analytic proof

Root named replay passed all 32 tests normally (4.076 seconds) and
under optimized Python (4.081 seconds). Both producer checks, all four
LF-byte-identical emissions, Ruff check/format, full base-to-source
whitespace and Unicode C0/C1 checks passed.

Root used polynomial modular inversion over the rationals and solved the
original implicit equation g(y)=lambda g'(y) coefficient by coefficient.
This is separate from the producer's inverse-series recurrence.
The differential determinant independently reconstructed the covariance.
Four-exponential algebra reconstructed the full-quadrant pair kernel.

In both normal and optimized modes these checks covered:

- all six moment models and their 336 moment/series entries;
- all seven pair models and 63 even kernel coefficients;
- nine held-out moment/cutoff models;
- the exact Wronskian sign and all large-branch leading constants;
- 26 independently resealed attacks against actual full reconstruction;
- six literal source bindings, four artifact seals and all five frozen blobs.

The first transient Wronskian check compared an expanded expression to
an unexpanded one structurally. Root corrected that scaffold to test the
expanded polynomial difference for zero before either accepted full run.
No source edit was required.

The non-author reviewer independently passed 32 tests in both modes,
all producer/emission checks, and the GH producer in both modes.
It reconstructed all pair/moment records and nine held-outs separately,
and rejected 42 resealed attacks (four full rebuilds), eight manifest
attacks, three source/size attacks, 44 type/domain/cap/parser checks and
a control-character attack in both modes. Its source worktree stayed clean.

## Seals and boundary

Fixture LF SHA-256:

    2fd131a9ee70bf02fbc35802ad92abb68fbaf00bf2392e2f33b08d267d664b83

Payload SHA-256:

    e27a292ebde73964ced691ee7b6abce6a7d9c7264cf842859446dc2887344616

Frozen Git blobs:

    proof     9688e30825fcc3d2b13570539bf03299407eae87
    producer  5a1df4304cd0984212a640a20147d32e29af8463
    fixture   11a5223a1af683e42153a7e28b21fca501f229ff
    manifest  fcb84c28f5be15aa7aa1e52a2387be7b86dc7fe6
    tests     0a67ae08a25e313f0f22e0186278f6e745d67a28

Root checked the primary [xi normalization](https://dlmf.nist.gov/25.4),
[digamma expansion](https://dlmf.nist.gov/5.11.E2), and
[differentiated Gamma expansion](https://dlmf.nist.gov/5.15.E9).
Remote bytes are context, not part of the offline authentication contract.

No off-axis common-divisor classification, native Riesz/interpolation
bound, confluent sampling estimate, cofinal/free-energy closure, exhaustive
novelty claim, RH or GRH conclusion is accepted here.
