# The remaining continuous completion: a calculation and its unpaid gates

**PROPOSED research calculation, not a primitive Type-I theorem.** This
note records the actual attempted analytic transfer. The complete
primitive continuous mixed norm and its complementary high-core sector
remain open. In particular no new zero-free boundary follows here.

The source pins are rStation paper8 v1, SHA256
`f1f9aed624908ccb9b6842911d898916230545ff76dc123187d7eadc3558def1`,
paper10 v2, SHA256
`525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`,
and paper5 v3, SHA256
`414d196862672b5aefbfa671b4b2e60f60ad9dde12dc3042d038a1bfb1d08d39`.
Their source URLs and exact normalization conventions are in NOTES.md.

## 1. What a full, unprimitive Eisenstein Type-I interface would give

Put `u=1+eta+it`, `0<eta<1/12`. The full Eisenstein Fourier coefficient
has the form

    t_u(n)=(Nn)^((u-1)/2) D(n,u).

Suppose its COMPLETE finite cusp vector has the progression Voronoi
formula obtained by continuing paper8 Section5 from its fixed residue
form to this full Eisenstein family, with polynomial t-growth, its TWO
cusp constants, the required fixed derivative bounds, and complete
cusp-coefficient dyadic norms `H^((1+eta)/2+epsilon)`. This uniform
spectral interface has not been proved in this packet; the calculation
below is conditional on it. The weighted full-series means in paper10
are relevant input, but do not by themselves state this entire cusp
interface with all the required uniformities.

The two constant powers would give the raw-D progression main terms

    A(u) X Phi_hat(1) sum_a alpha_a/Na,
    B(u) X^(2-u) Phi_hat(2-u) sum_a alpha_a/Na.           (1)

Their presence is retained. Neither is automatically annihilated by the
primitive residue response `sum alpha_a v(a)/Na`.

The completed Mellin factor is, up to fixed exponentials,

    G_u(s)=Gamma(s+(u-1)/2) Gamma(s-(u-1)/2).

On a dual norm block H, the full-series coefficient norm would be
`H^((1+eta)/2+epsilon)`. In the notation of paper8 Section6 the
unrestricted sextic character sieve contributes `H^(1/12)R^(1/2)`
when `H<=R`, the progression aggregation contributes
`A^(-1/2)R^(-1) ||alpha||_2`, and the physical transform contributes X.
The dual length is `K=R^2/X`; its small-argument kernel singularity is
`(K/H)^(eta/2+epsilon)`. Thus the complete dyadic contribution is

    X A^(-1/2)R^(-1/2)
             H^(7/12+eta/2)(K/H)^(eta/2+epsilon)
                  ||alpha||_2.                         (2)

For `R<=A<=X`, summing all H blocks and rapid tails, then all R, gives
the t_u Type-I error
`X^(5/12-eta/2)A^(1/6+eta)||alpha||_2`.
Removing `(Nn)^((u-1)/2)` therefore gives the raw-D error

    X^(5/12-eta)A^(1/6+eta)||alpha||_2.                 (3)

The GROWING_PROFILE_COMPARISON coefficient resource is genuinely
enough for the arithmetic norm in (3): it gives
`||alpha||_2<=A^(1/2+epsilon)` and subpower pointwise coefficients
throughout its Gram range. This does not supply the unproved spectral
interface, remove the two terms (1), or perform primitive transfer.

For illustration, applying (3) to ONE full-series adjoint pairing
with the native prefactor `U^eta X^(-1/2)`, and putting `A=D`, would
give squared error

    U^(2eta) X^(-1/6-2eta) D^(4/3+2eta).               (4)

At `D=U,X=U^(3/2)` this is `U^(13/12+eta)`. It is not a full mixed
norm: an individual flat Gauss-row pairing is already paid by the
known inverse/plain second moments. Summing a finite collection of
such pairings does not estimate the complementary row space.

## 2. The first actual primitive transfer has a price

Paper10 (3.6)--(3.7), for squarefree r, gives the exact expansion

    H(r,u)=E_r(u)^(-1) sum_(b|r)
       mu(b)nu(b)^2 gamma_2(b) bar(chi_b(r/b))^2
              (Nb)^(3/2-2u) D(r b^2,u).               (5)

All ray changes, original zero masks and shared numerator primes must
be retained. In particular (5) introduces numerators `q b^3` and a
nonconstant cubic phase, with coefficient size `b^(-1/2-2eta)`.
The product-column polar density identity does not turn this entire
nonconstant expansion into (3). Applying a squarefree progression
Gauss identity to the inflated nonsquarefree moduli would be false:
`g(1,p^2)=0` does not imply `g(n,p^2)=0` at nonunit dual n.

Paper10's weighted `h a b^3` mean handles the resulting family in
MEAN SQUARE. It does not state the required signed Type-I estimate
against our convolution. A proof must keep the two source input
lengths, every b branch, the shifted common profile, and the growing
ramified cusp components. None of those prices has been erased here.

## 3. Keeping the existing centered expression does not improve its power

Paper5 Section10 keeps the true diagonal and the separately restored
principal pair before estimating nonzero frequencies. Its exact (10.11)
is, prior to coarsening,

    DF+K^(5/6)D^(1/6)F^(-2/3).                        (6)

In the unlabelled case `F=1`, reflect at dual length `K=D^2/U` and
restore the native prefactor `U/D`. The second term becomes

    (U/D) K^(5/6) D^(1/6)=U^(1/6)D^(5/6).            (7)

This is the existing inverse-amplification cost. Subtracting the true
original diagonal does not remove (7): it is already the centered
NONZERO-frequency term. Moreover (6) is a positive normalized label
average. Our short Mobius/Gauss labels are coherent, so it cannot be
used without paying their full cross-label norm. This is the remaining
correlation task, rather than an omitted diagonal.

## 4. Why the new bounded head does not yet license the square-root phase import

The primary phase estimate is de Faveri--Pandey,
[Corollary1.4, arXiv2610.01035v1](https://arxiv.org/html/2610.01035v1#S1.SS2),
for bounded INTEGER-index coefficients and phase
`w(sqrt(n/N)+eta(n/N)^(3/2))`, with
`N<=W<=N^(4/3)`, `|eta|<=cW/N^2`, and one-spaced w.

The exact complex-place Voronoi quotient above has TWO gamma pairs.
Its large-argument stationary scale is `x^(1/4)`, where
`x=Nn X/(Nr)^2`, rather than sqrt(x). The main smooth dual range
`x` comparable to one is nonoscillatory; at much larger x the common
smooth transform is rapidly decreasing.

Cartesian slicing does retain every lattice direction, but does not
fix the stated phase condition. For fixed b and `a-b/2>0`,

    (a^2-ab+b^2)^(1/4)
       =(a-b/2)^(1/2)
           +(3b^2/16)(a-b/2)^(-3/2)+... .              (8)

The perturbation has a NEGATIVE power, and the dominant `|b|~|a|`
range has an order-one shape change. Corollary1.4 does not include
this phase. Subdividing into short intervals must pay the number of
pieces and the phase error; that cost has not been shown smaller than
the potential saving.

There is a separate coefficient obstacle. In paper8 (5.8), the new
bounded head enters only through the aggregated OUTER coefficient

    Psi_r=unit_phase(r)(Nr)^(-1/2) sum_(r|a)alpha_a/Na.

The phase in this variable varies as `const/(Nr)^(1/2)`. The dual
variable with phase (8) instead has coefficient `t_[r](n/M)`, for
which the imported theorem supplies ell2, not the essential bounded
ell-infinity input of Corollary1.4. Our head bound cannot be silently
transferred to those unknown dual Fourier coefficients. Thus no phase
estimate has yet been legally imported into the full native source.

Finally all positive-tail norm comparisons in this packet use the
SAME original nonprincipal character presentation. A canonical power
can become principal on original nonprincipal rows; it must be split
and paid separately. The bounded-head matrix theorem alone licenses
neither a TWO-INVERSE moment nor such principal branches.

## 5. An actual beta-dependent zero-angular cubic Type-I estimate

The following scalar estimate IS proved relative to its declared
zero-free input and the primary cubic transformation. It has not been
identified with the complete cleaned canonical vector.

Assume `1/2<=beta<1` and the fixed Eisenstein zeta reciprocal is
holomorphic on `Re s>beta`, with polynomial vertical growth on each
closed inner half-plane. Equivalently for this argument one may assume
the complete smoothly weighted Mobius estimate

    sum_(c primary,(c,r)=1) mu(c) V(Nc/C)(Nc)^(it)
       <<_(epsilon,V) C^(beta+epsilon)(Nr)^epsilon
                                      (1+|t|)^A.          (9)

Only the finite-order, zero-angular zeta function is needed. Moving
punctures in r have coefficient norm `(Nr)^epsilon` on each fixed
inner half-plane. Mellin inversion of `1/zeta_E(s)` proves (9) under
the reciprocal hypothesis. For the fixed primary convention a finite
unit/ray subdivision is retained.

Let r be squarefree primary, `R=Nr`, and use the normalized cubic Gauss
sum `g_tilde` of Dunn--Radziwill. For a fixed smooth W supported on a
compact positive annulus, put

    S_r(X)=sum_(u primary) g_tilde(u r) W(Nu/X).

Then, uniformly for `X,R>=1`,

    S_r(X)= kappa W_hat(5/6) X^(5/6)
              phi(r)/[R^(7/6) zeta_E(2;1_r)]
       +O_(epsilon,W)((XR)^epsilon
                     X^((2beta+1)/6) R^((5-2beta)/12)),  (10)

where `kappa=(2pi)^(5/3)/(3^(7/2)Gamma(2/3))` in that primary
convention. Every shared prime has its literal Gauss zero; there is
no coprime-input replacement of a nonunit character value.

Here is the proof and the precise import. Use the UNCONDITIONAL cube
completion and its full ramified dual coefficients in
[Dunn--Radziwill, arXiv2109.07463v3, (8.2)--(8.8)](https://arxiv.org/html/2109.07463v3#S8).
The two uses of GRH in their subsequent argument are weighted Mobius
sums in the cube-removal variable c. Replacing those uses by (9),
while leaving their exact transformation and coefficient estimates
unchanged, gives the following bounds for a c-norm dyad C:

    large-C block:       << (XR)^epsilon X C^(beta-5/2),
    small-C dual error:  << (XR)^epsilon R^(1/2) C^(beta+1/2). (11)

Here the dyadic cutoff V is KEPT inside the Mobius sum. Only its
other common norm factors are Mellin separated. Before that separation
one may insert a fresh smooth cutoff on `N(ud^3)C^3/X` equal to one on
the original support; it bounds the remaining absolute u,d resource
without using a sharp c cutoff. Thus every invocation is precisely
the SMOOTH estimate (9), with polynomial separated-height cost. No
sharp Mertens estimate is inferred from a polynomial reciprocal bound.
The final main-term tail below is also a sum of the original smooth
dyadic pieces.

For the first line, the remaining complete u,d absolute resource is
`O(X/C^3)`, since `sum_d (Nd)^(-5/2)` converges. The weighted Mobius
sum costs `C^(beta+1/2)`. For the second, the SAME weighted Mobius
sum multiplies the full dual coefficient resource from their
(5.67)--(5.68). The exact ramified divisor factors are included. Their
weighted nu,d sum is subpower uniformly at every polynomial dual
cutoff, as in the coefficient estimate in their (8.10); it is not
replaced by a unit-root formula at ramified primes.

Split the cube-removal variable at

    C0=(X/R^(1/2))^(1/3),                              (12)

initially when `R<=X^2`. Both exponents of C in (11) have strict
summation margins. Their complete dyadic sums are respectively bounded
by `X C0^(beta-5/2)` and `R^(1/2)C0^(beta+1/2)`, which are EQUAL to
the error power in (10). The main term also needs its complete
c-sum: partial summation of (9) gives tail
`O(R^epsilon C0^(beta-2+epsilon))`. Multiplying by
`X^(5/6)R^(-1/6)` yields the same X-power as (10) and the smaller
R-power `(1-beta)/6`. Thus no omitted main-term tail introduces an
`X^(1/2)` loss. Fixed support endpoints only change constants.

If `R>X^2`, the trivial complete count is O(X): nonzero normalized
cubic Gauss sums at squarefree moduli have modulus one and all other
moduli vanish. The error power in (10) is then at least X, and also
absorbs the displayed main term. This covers every r,X range.

For the imported working exponent `beta=7/8`, (10)'s error is

    (XR)^epsilon X^(11/24) R^(13/48).                  (13)

It is smaller by a power than the natural main scale
`X^(5/6)R^(-1/6)` whenever `X>=R^(7/6+delta)` for a fixed positive
delta, choosing the internal epsilon sufficiently small. More
generally the threshold exponent is
`(7-2beta)/(8-4beta)`. This is a genuine scalar Type-I improvement
from the stated weaker zero-free input, not an assumption of GRH.

Its application gate is substantial. The original long inverse Gauss
identity gives `mu(a)gamma_1(a)=conjugate(C_-1(a))G(a)`.
Radial geometric smoothing removes optional angular profile modes,
but not this arithmetic angular factor. For a NONZERO angular order
ell the Mobius cube variable carries `alpha^(3ell)`, whose reciprocal
L-function is not covered by the original finite-order beta input.
Nor does (10) estimate a coherently weighted short-label sum or its
full primitive continuous covariance. Matching such an actual
zero-angular calibrated branch, including its primitive inversion and
every source profile, remains the task before (13) can improve the
ordinary-zeta consumer.

## 6. Honest complete-vector baseline and the remaining long-frame saving

The imported FAMILY-wide beta bound also improves the elementary
pointwise estimate. This uses all finite-order characters over the ONE
field E, not a theorem over every number field. In the pinned original
source, `lem:logarithmic-control` (lines 1531--1619) explicitly gives

    |L(s,psi)|+|1/L(s,psi)|
        <<_(v,epsilon) {2Q(3+|Im s|)^2}^epsilon,
                         Re s>=beta_*+v, v>0,            (14)

for every primitive nonprincipal finite-order psi. The adjacent deleted
Euler-factor lemma supplies the natural presentation's full zero mask
with a radical subpower. For each nonunit physical row Nu~U, its
primitive conductor and deletion radical are O(U), up to the fixed ray
data. Fixed S-supported twists cannot remove its good ramification.

For a compact smooth annular profile, shift Mellin inversion of the
exact inverse or plain Dirichlet series to beta_*+v. There is no Mellin
pole from an annular cutoff and no L-pole for these nonprincipal rows.
Taking beta=7/8 from the imported family theorem, and choosing v and
the internal losses small, gives uniformly

    |M_psi(D)| << D^(beta-1/2)(UD)^epsilon,
    |S_psi(N)| << N^(beta-1/2)(UN)^epsilon.              (15)

The fixed polynomial norm-height/profile costs are restored before the
norm; rapid common-profile Fourier decay absorbs them. Unit principal
rows are not included in (15).

At the actual corner D=U, N=sqrt(U), the imported inverse second moment
is sum|M|^2<<U^(1+epsilon). Combining it with the SECOND bound in (15)
therefore proves the complete actual mean

    sum_(Nu~U,physical nonunit)|M_psi(U)S_psi(sqrt U)|^2
             << U N^(2beta-1)(UN)^epsilon
              = U^(11/8+epsilon).                     (16)

All sixth-free physical row powers and their natural zeros remain in
this estimate. Equivalently, use M-infinity, inverse second moment and
the licensed zero-slot plain fourth moment to get the same exponent.
This is an honest consequence of already imported inputs, not a new
arithmetic improvement. The annular-debiased intermediate vector has
the same upper bound, since its complete norm difference costs only
U^(6/5+epsilon).

The long frame in `LONG_ARITHMETIC_FRAME.md` has both lower and upper
row-frame bounds of scale K/U up to prescribed subpowers. Thus at the
corner its complete unpaid coordinate vector t+e has the honest bound
K U^(3/8+epsilon), after adding its already controlled matched mainterm.
The desired U^(6/5) full norm would follow from K U^(1/5+epsilon)
instead. The remaining actual saving is therefore U^(7/40), even at
this representative corner. The whole witness polygon and physical
row powers still need the uniform corresponding estimate.

Finally averaging unitary radial norm-height phases does not provide
that saving by itself. If Psi_t=D_t Psi for a diagonal unitary D_t,
then Psi_t Psi_t*=D_t S_K D_t*. For every fixed t the exact energy is
F* D_t S_K D_t* F. In the long-label range its dominant diagonal is
(K/U)sum_u d(u)|F(u)|^2, d(u)=c prod_(p|u)(1-1/Np), independent of t.
The Schur off-diagonal error is smaller by U^(-eta+epsilon). Positive
averaging over t preserves this leading energy. A further saving must
use the prescribed Mobius-times-plain arithmetic in the continuous
coordinates, rather than the unitarity or label count alone.

There is a particularly concise ORIGINAL-source formulation of the
remaining task. Choose the fixed smooth unit phase a from the final
paragraph of `LONG_ARITHMETIC_FRAME.md`, so (ha)_hat(2/3)=0. Replace
the frame by D_a Psi and keep the ORIGINAL target F=h M S and its
ORIGINAL exact convolution coefficients c_A. Paper 10's raw residue
factor is now zero for EVERY R and EVERY fixed ray section, before any
Type-I main/error separation. Thus the exact analysis coordinates are

    a_R=sqrt(W(NR/K)) sum_A c_A overline(E_(U,R)^(ha)(A)). (17)

They have no separate residue vector at all. The unchanged row-frame
upper and lower bounds show that the desired squarefree-row mean
U^(6/5+epsilon) is equivalent, up to prescribed subpowers, to

    sum_(R good) W(NR/K)
       |sum_A c_A overline(E_(U,R)^(ha)(A))|^2
                          << K U^(1/5+epsilon),         (18)

at K=U^(2+eta), with the complete natural character zeros and all
product powers retained. This is a pole-free continued-Kubota bilinear
average for the original coefficient, not a replacement zero detector.
Calibration is optional for this formulation. The known complete
baseline is still K U^(3/8+epsilon), and (18) is OPEN. Its all-physical-
row extension needs the additional primitive-character adapter already
identified in the frame note. Killing the raw pole cheaply therefore
isolates the continuous arithmetic problem; it does not solve it.
