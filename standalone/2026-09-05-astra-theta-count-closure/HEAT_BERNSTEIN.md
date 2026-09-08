# All-time invariant heat positivity and the Bernstein layer

Status: PROPOSED PROVED ANALYTIC THEOREMS; independent mathematical review required.
Scope: the actual Riemann xi function, every real u >= 0, every t > 0,
and every derivative order. RH is NOT proved. No external novelty claim.
Dependencies: classical xi/theta/Hadamard/Jensen theory; the published
Platt--Trudgian zero verification restricted ONLY to height 100; a separately
replayed directed-interval sign change at ordinates 14 and 15.
What was run: `verify_exact.py` and `verify_low_zero.py`; see VALIDATION.md.
Smallest remaining RH gap: complete monotonicity of S, NOT positivity of S.

## 1. Fix the function and the multiplicity convention

Throughout,

    xi(s) = s(s-1) pi^(-s/2) Gamma(s/2) zeta(s) / 2,
    Xi(z) = xi(1/2 + iz),
    X(u)  = xi(1/2 + sqrt(u+1/4)),
    h(u)  = X'(u)/X(u).

Reflection makes X single-valued and entire. X(0)=1/2. Its order is at most
1/2. In the standard, full-line Fourier normalization,

    Xi(z) = integral_R Phi(tau) exp(iz tau) d tau,
    X(u)  = 2 integral_0^infinity Phi(tau) cosh(tau sqrt(u+1/4)) d tau.

Here Phi is even, smooth, and superexponentially decreasing. For tau >= 0,

    x_m = pi m^2 exp(2 tau),
    g_m = exp(tau/2 - x_m),
    Phi(tau) = sum_(m>=1) (4 x_m^2 - 6 x_m) g_m > 0.

Every differentiation used below is justified by locally uniform convergence
of the Gaussian series and its differentiated series. These are classical
identities; the normalization agrees with PR #785's spectral theta note.

Let rho=beta+i gamma run over ALL nontrivial zeta zeros with gamma>0, counted
with multiplicity. Put

    a_rho = rho(1-rho)
          = gamma^2 + beta(1-beta) + i gamma(1-2 beta).

This upper-half-plane list is one copy of each reflection orbit. In
particular an off-line quartet supplies TWO conjugate a's, not four.
The critical strip gives

    Re(a_rho) >= gamma^2 > 0,       |Im(a_rho)| <= gamma.          (1)

The genus-zero product and its logarithmic derivative are

    X(u) = (1/2) product_(gamma>0) (1+u/a_rho),
    h(u) = sum_(gamma>0) 1/(u+a_rho).                            (2)

The sum of |a_rho|^(-1) converges. This follows, for example, from the
O(T log T) zero-count bound proved below. The order-below-one Hadamard
theorem excludes a nonconstant exponential factor in (2).

Define

    S(t) = sum_(gamma>0) exp(-a_rho t),             t>0.         (3)

S is real, because the a-list is conjugation invariant. It and every time
derivative converge absolutely on compact subintervals of (0,infinity).
The parent dossier uses K=2S and q=2h. Do NOT import that factor two twice.
This zero heat is not the de Bruijn--Newman deformation of the theta kernel.

## 2. A deliberately crude, proved zero-count envelope

Write N(T) for the number of zeros with 0<gamma<=T, with multiplicity.

**Lemma ASTRA-TC-01.** For every T>=100, N(T)<=T^2. In addition,
N(T)=O(T log(T+2)). No RH or zero-density estimate is needed.

Proof. The disk |s-2|<=T+2 contains all zeros with |Im s|<=T. Apply Jensen
at s=2, comparing radii r=T+2 and R=2(T+2). The positive theta integral gives

    max_(|s-2|=R) |xi(s)| <= xi(R+2) = xi(2T+6).

Indeed |s-1/2|<=R+3/2, and |cosh(w tau)|<=cosh(|w| tau).
Also xi(2)=pi/6>1/2. Put sigma=2T+6. Since zeta(sigma)<2 and pi^(-sigma/2)<1,

    xi(sigma) < sigma^2 Gamma(sigma/2).

For x=T+3, log-convexity of Gamma between its neighboring integer arguments
implies Gamma(x)<=ceil(x)!<=(T+4)^(T+4). Thus

    2 N(T) log 2
      <= 2 log(2T+6) + (T+4) log(T+4) + log 2.                  (4)

Boundary coincidences are dealt with by a limiting outer radius; Jensen's
inequality for zeros in the smaller disk has the same conclusion.
Equation (4) already gives O(T log T). For an elementary explicit bound,
use log x<=sqrt(x), T+4<=2T, 2T+6<=3T, and 2 log 2>1. Then

    N(T) <= 4 sqrt(T) + 3 T^(3/2) + 1
          <= 4 T^(3/2) <= T^2,                 T>=100.

The penultimate inequality follows from 4 sqrt(T)+1<=T^(3/2).
This completes the proof. No numerical asymptotic constant is imported.

**Lemma ASTRA-TC-02 (Gaussian tail).** For t>0 and B>=100,

    sum_(gamma>B) exp(-t gamma^2)
       <= (B^2 + 1/t) exp(-t B^2).                             (5)

Proof. Stieltjes integration by parts gives the upper bound
2t integral_B^infinity x exp(-t x^2) N(x) dx after dropping the nonpositive
lower endpoint. Insert N(x)<=x^2 and evaluate the elementary integral.
The convention gamma>B also handles an atom at B correctly.

## 3. Exactly which finite zero information is used

External input V100:

    Every nontrivial zero with 0<gamma<=100 has beta=1/2.

This is a tiny restriction of the published, rigorous interval verification
of Platt and Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
Bull. London Math. Soc. 53 (2021), 792--797, DOI 10.1112/blms.12460,
arXiv:2004.09765. The theorem is IMPORTED, not rerun. No simplicity is used.

Input Z14/15:

    At least one critical-line zero has 14<gamma_0<15.

The included `verify_low_zero.py` encloses Xi(14)>0 and Xi(15)<0 using
mpmath 1.3.0 interval arithmetic and an exact analytic eta-series error.
It proves existence by continuity, not uniqueness, simplicity, or a census.
Its Gamma implementation is an explicit software trust dependency.

For completeness, the error estimate is derived here. For Re(s)=sigma>0,
Euler's eta transform is

    eta(s) = sum_(k>=0) 2^(-k-1)
                 sum_(j=0)^k (-1)^j binom(k,j) (j+1)^(-s).

The inner difference is

    Gamma(s)^(-1) integral_0^infinity
        t^(s-1) exp(-t) (1-exp(-t))^k dt.

Its absolute value is at most Gamma(sigma)/|Gamma(s)|, so the tail beginning
at k=N is at most 2^(-N) Gamma(sigma)/|Gamma(s)|. At sigma=1/2 this ratio is
sqrt(cosh(pi Im(s))). At t=14 or 15 it is less than exp(24)<3^24<2^39, using
pi<22/7. Taking N=128 makes the error <2^(-89), enclosed by the script's
larger exact radius 2^(-80). Divide by 1-2^(1-s) and multiply by the xi
completion entirely in intervals. The resulting real enclosures have signs
as recorded in `low_zero_result.json`. These steps do not use a zero table.

The selected zero has a_0=gamma_0^2+1/4<226. Set A=226 and H=100.

## 4. The all-time theorem

**Theorem ASTRA-TC-03.** Subject only to the established classical inputs
and V100/Z14/15 above, the actual invariant zero heat satisfies

    S(t) > (1-2^(-83)) exp(-226 t) > 0,            every t>0.    (6)

In particular this is an unconditional theorem in the ordinary mathematical
sense of using published verified results. It is not a new full zero census.

Proof. Put

    C = (H^2+H) exp(-H+A/H) = 10100 exp(-97.74).

Since 10100<2^14, 97.74>97, and e>2, C<2^(-83).

First suppose 0<t<=1/H. Every zero with gamma<=1/t contributes
exp(-Re(a)t) cos(Im(a)t) >= 0 to the real sum, by (1) and cos(1)>0.
Retain the single real zero contribution exp(-a_0 t)>exp(-A t).
All possibly negative terms lie above B=1/t. Lemma 2 gives

    S(t) >= exp(-A t) - (t^(-2)+t^(-1)) exp(-1/t).

The ratio of this error to exp(-A t), with w=1/t>=H, is
(w^2+w) exp(-w+A/w). Its logarithmic derivative is

    (2w+1)/(w^2+w) - 1 - A/w^2 < 2/w - 1 < 0.

The ratio is therefore at most C.

Next suppose t>=1/H. All zeros with gamma<=H are real in the centered
coordinate by V100, so their heat contributions are positive. Keeping the
same selected zero and bounding the rest in absolute value gives

    S(t) >= exp(-A t) - (H^2+1/t) exp(-H^2 t).

The relative error is at most
(H^2+H) exp(-(H^2-A)t) <= C. Both ranges prove (6).
Notice that an infinite unknown zero tail is explicitly paid, not inferred
from the verified prefix. The Gaussian/time-dependent split is essential.

## 5. The all-order consequence

Absolute integration using (1) and sum gamma^(-2)<infinity yields

    h(u) = integral_0^infinity exp(-u t) S(t) dt,       u>=0.    (7)

Differentiation is justified at every finite order, also at u=0: the
individual integrated absolute bounds are O_n(gamma^(-2n)). Equation (6)
therefore proves the following theorem.

**Theorem ASTRA-TC-04.** For n>=1 and u>=0,

    (-1)^(n-1) h^(n-1)(u)
      > (1-2^(-83)) (n-1)! / (u+226)^n.                        (8)

Thus h=X'/X is strictly completely monotone. Equivalently,

    phi(u)=log(X(u)/X(0))

is a Bernstein function. In fact its positive Levy representation is

    phi(u) = integral_0^infinity (1-exp(-u t)) S(t) dt/t.        (9)

The integral is justified by (7) and Tonelli now that S>0. Near zero,
S(t)=O(t^(-1/2) log(2/t)) from (4), and at infinity it is exponentially
bounded. Consequently integral min(1,t) S(t)dt/t is finite.

For every c>0, (X(0)/X(u))^c is completely monotone and is the Laplace
transform of an infinitely divisible nonnegative random variable. One can
prove this directly by truncating the positive Levy measure S(t)dt/t,
using compound Poisson transforms, and passing to the continuous limit at
u=0. This probability realization is not a self-adjoint realization of the
zeta zeros: its Laplace parameter is the invariant u coordinate.

## 6. What has and has not been closed

The exact hierarchy is

    S(t) >= 0 for every t
       <=> h is completely monotone (uniqueness of Laplace transforms);

    S is completely monotone
       <=> h is Stieltjes
       <=> RH.                                                (10)

The first row is established here. The second is NOT. For the reverse
implication in the first row, use uniqueness for locally finite measures
with the exponential integrability supplied by (7). The second row follows
from Bernstein's representation and the nonremovable conjugate poles in
(2), or from the one-scale Hausdorff argument in THETA_COUNT.md.

A positive heat density need not itself be a mixture of positive real
exponentials. COUNTERFEITS.md proves this distinction both in a rational
polynomial model and in an explicit positive-source perturbation of Xi.
In particular (8) is not an all-order Widder/Stieltjes inequality: those
contain additional mixed powers and differences. No new zero-free region,
critical-line percentage, simplicity theorem, or RH proof is claimed.

## 7. Relationship to the source-only count inequality

For any v>0 define P_v(z)=X(vz)/X(v), and let

    p_n^*(v) = (-1)^(n-1) n [y^n] log P_v(1+y),       n>=1.

These are logarithmic factorial-cumulant coordinates, not probabilities.
Equations (7)--(8) give the uniform result

    p_n^*(v) = v^n/(n-1)! integral_0^infinity
                         t^(n-1) exp(-vt) S(t)dt
             > (1-2^(-83)) (v/(v+226))^n.                     (11)

THETA_COUNT.md derives p_n^* directly from the positive theta mixture by an
all-order joint-cumulant formula, then identifies the mixed Hausdorff
inequalities that remain. Equation (11) proves the b=0 face at EVERY order
and scale, not just a finite sequence of checks.
