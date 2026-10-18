# Growing positive Taylor energies do not escape the entire closure

Status: **PROPOSED native corollary of ENTIRE_ONSITE_OBSTRUCTION.md.**
It extends that theorem beyond a fixed finite onsite family. The positive
coefficient hypothesis is essential. Signed growing-degree potentials
or other transfer constructions are not covered.

## Exact statement

Replace the fixed onsite sum in the entire-onsite theorem by

    U_N(z)=sum_(k>=2) a_{k,N} z^(2k),       a_{k,N}>=0,      (1)

where each U_N is entire. It may be a polynomial of arbitrarily growing
degree. Let c_N be an arbitrary real quadratic counterterm, let M_N be
the MGF of a symmetric bounded-support auxiliary law with one fixed
finite characteristic-function zero band, and assume

    p_N(x)=Z_N^(-1) exp[-U_N(x)-c_N x^2] M_N(x)             (2)

is integrable. If the laws(2) converge weakly to an everywhere-positive
continuous even density p, then p extends to an entire function.
Consequently (2) cannot converge to the actual theta density.

This includes varying positive sums of cosh terms, after their constant
and quadratic Taylor coefficients are absorbed into normalization and
c_N. No uniform degree, coefficient or complex bound is assumed at the
start.

## Proof

Use the single fixed rescaling from ENTIRE_ONSITE_OBSTRUCTION.md to
make the auxiliary MGF zero band `|Re zeta|<=1/10`. Positivity of the
Taylor coefficients is preserved. The logarithm of the density remains
concave as a function of u=x^2 outside u<=1/50, because U_N(sqrt(u))
is convex. The same weighted-restriction lemma therefore gives local
potential-ratio convergence at all x>=1.

At arbitrary fixed anchors R,2R,3R with R>=1, the exact normalization
and quadratic canceling difference is

    D_N(R)=V_N(3R)-(8/3)V_N(2R)+(5/3)V_N(R)
          =sum_(k>=2) a_{k,N}R^(2k) C_k
                  +sum_zeta mG_R(zeta),                     (3)

where `C_k=9^k-(8/3)4^k+5/3` and G_R is the same positive quartet
finite difference evaluated at R,2R,3R. Quartet log concavity gives
G_R>0. The local ratio convergence makes D_N(R) bounded for every
fixed R. The series in(3) is justified by absolute convergence of U_N
at3R; all its summands are nonnegative.

For k>=2,

    C_k/9^k=1-(8/3)(4/9)^k+(5/3)(1/9)^k
           >=1-128/243>1/3.

Thus

    sum_(k>=2) a_{k,N}(3R)^(2k)<=3D_N(R).                    (4)

For |z|<=3R, the left side dominates |U_N(z)| by coefficient
positivity. Equation(4), for each fixed R, proves that the entire
onsite family is locally uniformly bounded on the WHOLE complex plane.
This is the missing complex compactness resource; it follows from the
actual weak limit and local real ratios rather than from a formal
coefficient fit.

At R=1, (3) simultaneously bounds the far-zero resource
`sum_(r>=1)m/r^4` and the near-zero weighted count, by exactly the same
uniform positive quartet comparison as the parent theorem. Equation(4)
also bounds U_N(1),U_N(2). The potential difference from1 to2 therefore
bounds the renormalized quadratic counterterm C_N, even if the original
c_N diverges.

All other steps in the parent proof now apply unchanged. The far
Hadamard factors have uniformly bounded entire renormalized products;
the near factors normalized at1 have bounded count and compact bounds.
Equation(4) supplies the entire bound for the onsite exponential.
Consequently p_N(z)/p_N(1) is an entire normal family. Its unique entire
limit is identified on the real interval[1,2] by local density ratios.
Weak mass convergence on that interval identifies p_N(1), giving local
uniform convergence of densities on every real compact interval. The
limiting density p therefore agrees everywhere with the entire limit.

The actual theta density has no entire extension by the native modular
cusp proof in ../BESSEL_COMPLETION_ATTEMPT.md, so it is excluded.

## What remains outside the corollary

The result permits arbitrary growing degree provided the even onsite
Taylor coefficients from degree4 onward stay nonnegative. It does not
turn the same conclusion into a theorem for arbitrary signed
coefficients. Large cancellations among signed energies can destroy
(4), and then real-axis convergence need not imply complex compactness.
It also does not cover direct spin observables without the exact
transfer density(2), loss of a uniform auxiliary zero band, or a target
without the stated positive continuous density.
