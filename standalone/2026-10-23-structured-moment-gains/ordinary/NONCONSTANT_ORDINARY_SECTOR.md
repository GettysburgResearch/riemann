# The ordinary nonconstant sector has only divisor costs

Status: proposed component theorem with a complete proof. This removes a
growing-level evaluation cost for specified ordinary Eisenstein sections at
the cusp infinity. It is not a metaplectic second-moment theorem and does not
improve a zero-free boundary.

Source relationship: continue the ordinary old-section identity in
`FINITE_COVER_AND_CUSP.md` and PR #1016,
`7ea66551190f291101b0dd44fb1fc9b3331c560d`,
`QUARTIC_SPECTRAL_INTERFACE.md`, Section 3. The coefficient argument and the
uniform horosphere bound below are derived directly, retaining the ordinary
reciprocal-zeta factor. No bounded evaluation norm on a finite cover is
assumed. This statement does not include a different cusp, metaplectic
scattering, angular companion columns, or the centered arithmetic diagonal.

## 1. Exact ordinary normalization

Let K=Q(i), O=Z[i]. On hyperbolic three-space write w=(z,y), y>0. For
Re(s)>2 use

    E(z,y;s) = (1/4) sum_(c,b in O, (c,b)=1)
                  y^s / (|cz+b|^2+|c|^2 y^2)^s.

Its incoming term is y^s. Fourier characters on C/O are
`exp(2 pi i Re(kz))`, k in O, so the Bessel argument below is `2 pi |k|y`.
This convention differs from the doubled-trace convention in the quartic
source; it is stated here explicitly and is used consistently throughout.
Good odd-ideal divisibility is unchanged by that fixed convention change.

Write

    a_s(k)=(Nk)^((s-1)/2) sigma_(1-s)((k)),
    C(s)=2 pi^s / [Gamma(s) zeta_K(s)].

The Fourier expansion is

    E(z,y;s) = y^s + phi(s)y^(2-s)
       + C(s) sum_(k!=0) a_s(k)y K_(s-1)(2 pi |k|y)
                                  exp(2 pi i Re(kz)),          (1)

where `phi(s)=pi zeta_K(s-1)/[(s-1)zeta_K(s)]`. The sum defining sigma is
over ideal divisors, so associates are not counted repeatedly.

Here is a direct derivation of the normalization. For c!=0 fix its ideal
generator up to units, write b=b_0+cn, and apply planar Poisson summation to
the sum over n in O. The nonzero-frequency Fourier integral is

    integral_C y^s(|z|^2+y^2)^(-s) exp(-2 pi i Re(kz)) dz
        = [2 pi^s/Gamma(s)] |k|^(s-1)y K_(s-1)(2 pi |k|y).

This follows by the Gamma integral and the Gaussian Fourier transform. The
primitive sum over b_0 is the ordinary Ramanujan sum, whose local elementary
identity gives

    sum_c Ramanujan(k,c)/(Nc)^s
        = sigma_(1-s)((k))/zeta_K(s).

The zero-frequency integral is `pi y^(2-s)/(s-1)`, and its primitive sum is
`zeta_K(s-1)/zeta_K(s)`. This proves (1) in absolute convergence; the
coefficient identities continue meromorphically. Equivalently their local
identities can be continued without asserting a finite value at a pole.

For a squarefree odd ideal d, let E_(d^2) be the primitive-bottom-row
subseries with d^2 dividing c. Fix generators and put
`T_r(z,y)=(rz,|r|y)`. Independent prime-by-prime primitive-row partitions
give the exact identity

    E_(d^2)(w;s)
      = (Nd)^(-s) product_(p|d)(1-q_p^(-s))^(-1)
           sum_(e|d) mu(e)(Ne)^(-s/2) E(T_(d^2/e)w;s).        (2)

Its one-prime proof is provided in `FINITE_COVER_AND_CUSP.md`, Theorem 3.
No choice of generator changes an ordinary coefficient in (1), because
the divisor sum and Bessel term are radial and units permute the lattice.

## 2. Fourier support removes the growing cutoff

Define b_(d,s)(k) by removing the common factor
`C(s)y K_(s-1)(2 pi |k|y)` from the kth nonzero Fourier coefficient of
E_(d^2). Dilation by r sends a frequency n to nr, with vertical factor |r|.
Consequently (2) gives the exact formula

    b_(d,s)(k)
      = (Nd)^(1-s) product_(p|d)(1-q_p^(-s))^(-1)
         sum_(e|d, d^2/e divides k)
              mu(e)(Ne)^(-(s+1)/2) a_s(k e/d^2).              (3)

In particular,

    b_(d,s)(k)=0 unless d divides (k).                       (4)

This literal divisibility is the reason a Fourier-mode estimate does not
pay the generic R^(3/2) evaluation norm of the growing finite-cover space.

**Theorem 4.** Fix 0<u<=1 and epsilon>0. Let lambda(d) be any finitely
supported coefficients on squarefree good ideals satisfying

    |lambda(d)| <= A^(omega(d)),                              (5)

where A is fixed. For s=u+it, uniformly in real t, the support of lambda,
and every nonzero k in O,

    |sum_d lambda(d)b_(d,s)(k)|
       <<_(u,epsilon,A) (Nk)^((1-u)/2+epsilon).                (6)

The coefficient in (6) is the normalized arithmetic coefficient. The
common `1/zeta_K(s)` in C(s) remains present in the actual Eisenstein
series. The theorem does not assert continuation through its unknown poles.

*Proof.* The divisor formula gives

    |a_s(n)| <= tau((n))(Nn)^((1-u)/2).

Substitute this in (3). The d powers cancel exactly, while the e power is
`(Ne)^(-u)`. Since k e/d^2 divides k whenever it occurs, its divisor count
is at most tau((k)). Thus

    |b_(d,s)(k)|
      <= 1_(d|k) tau((k))(Nk)^((1-u)/2)
             product_(p|d) (1+q_p^(-u))/(1-q_p^(-u)).         (7)

There are no small denominators depending on t, since
`|1-q_p^(-s)|>=1-q_p^(-u)`. Sum (7) using (5). The additional factor is at
most

    product_(p|k)
          [1+A(1+q_p^(-u))/(1-q_p^(-u))].                    (8)

For every fixed delta>0, (8) and tau((k)) are each
`O_(u,delta,A)((Nk)^delta)`: finitely many small primes cost a fixed
constant, and each large-prime factor is bounded by q_p^delta; the usual
prime-power argument handles tau. Choosing the two deltas with sum epsilon
proves (6). The proof is independent of the number of ideals in the
original cutoff. QED.

### Two actual ordinary sections covered by the theorem

First take

    lambda_R(d)=mu(d) 1_(Nd<=R).

The corresponding ordinary series is E[V_R]=sum lambda_R(d)E_(d^2), and
(6) is uniform in R with A=1.

Second take the pointwise finite-section square V_R^2. Since
`v_d v_e=v_lcm(d,e)`, its coefficient is

    lambda_R^(2)(l)
       = sum_(Nd,Ne<=R, lcm(d,e)=l) mu(d)mu(e).               (9)

For every squarefree l, the pair of divisor membership bits has three
nonempty choices at each prime, so
`|lambda_R^(2)(l)|<=3^omega(l)`. Formula (6) therefore applies to the
ordinary Eisenstein series E[V_R^2] with A=3, again uniformly in R.

**E[V_R^2] is not |E[V_R]|^2.** It is the Eisenstein series induced from
the pointwise square of the finite section. A Rankin--Selberg unfolding
would have to identify this particular ordinary series before the estimate
could be used for a product of automorphic functions.

## 3. A full nonconstant horosphere bound, with spectral growth paid

Let E_lambda^nc denote the complete nonconstant Fourier series in (1)--(3)
for coefficients satisfying (5). Use Euclidean probability measure on the
unit-area torus C/O.

**Theorem 5.** For every 0<u<=1 and epsilon>0, uniformly for real t, y>0
and all such finite coefficient arrays,

    integral_(C/O) |E_lambda^nc(z,y;u+it)|^2 dz
       <<_(u,epsilon,A)
          (1+|t|)^(6-4u+epsilon)
          y^(2u-2-epsilon) / |zeta_K(u+it)|^2.                (10)

At points where zeta_K(u+it)=0 the right side is interpreted as an
unavailable bound, not as analytic continuation through that zero. The
constants are locally uniform in u away from zero. The bound retains the
entire nonzero frequency set and is uniform in the sieve cutoff R in both
applications above.

*Proof.* Apply (6) with epsilon/4. Parseval reduces the left side to at
most a constant times

    |C(s)|^2 y^2 sum_(k!=0)
         |k|^(2-2u+epsilon)
         |K_(u-1+it)(2 pi |k|y)|^2.                          (11)

Put a=u-1 and L=4-2u+epsilon. A dyadic annulus of radius r contains O(r^2)
Gaussian lattice points. A one-dimensional Sobolev bound on the logarithmic
interval [log(r/2),log(4r)] gives, for any C1 function f on (0,infinity),

    sum_(k!=0) |k|^(L-2)|f(c|k|y)|^2
       <<_L y^(-L) integral_0^infinity
                x^(L-1)(|f(x)|^2+|x f'(x)|^2) dx,           (12)

with c=2pi absorbed in the constant. Indeed one bounds the supremum on each
annulus by the indicated Sobolev integral, multiplies by O(r^L), and uses
the bounded overlap of the enlarged annuli. Extending the dyadic sum below
the smallest lattice radius only increases the resulting positive bound.

For f=K_(a+it), the exact Bessel product integral is

    integral_0^infinity x^(L-1)|K_(a+it)(x)|^2 dx
      = 2^(L-3)/Gamma(L)
           Gamma(L/2+a)Gamma(L/2-a)|Gamma(L/2+it)|^2,        (13)

valid for L>2|a|. To verify (13), insert the two Schlaefli integrals
`K_nu(x)=(1/2)(x/2)^nu integral_0^infinity
 t^(-nu-1)exp(-t-x^2/(4t))dt`. Integrating x first gives a Gamma factor.
The substitution t=r v, w=r(1-v) in the remaining positive-absolute
convergent double integral gives a second Gamma integral and a Beta
integral, yielding the four factors in (13). The hypotheses ensure absolute
convergence, so the same calculation covers the conjugate orders.

The identity `K_nu'=-(K_(nu-1)+K_(nu+1))/2` bounds the derivative term in
(12) by the two versions of (13) with L replaced by L+2 and a replaced
by a-1 or a+1. All convergence inequalities hold. Fixed-real-part Stirling
bounds, supplemented by compact-t continuity, give

    integral x^(L-1)(|K_(a+it)|^2+|xK'_(a+it)|^2) dx
       <<_(u,epsilon) exp(-pi|t|)(1+|t|)^(L+1).              (14)

Finally

    |Gamma(u+it)|^(-2)
       <<_u exp(pi|t|)(1+|t|)^(1-2u).

The exponential factors cancel against those in (14). Equations
(11)--(14) give y^(2-L)=y^(2u-2-epsilon) and spectral exponent
`L+2-2u=6-4u+epsilon`, proving (10). No exponential spectral factor has
been hidden in a smooth-profile constant. QED.

For a common wavepacket `integral a(t)D^(u+it-1)
 E_lambda^nc(z,y;u+it)dt`, Minkowski consequently gives

    ||wavepacket||_(L2(C/O))
      << D^(u-1)y^(u-1-epsilon/2)
          integral_R |a(t)|(1+|t|)^(3-2u+epsilon/2)
                       /|zeta_K(u+it)| dt,                  (15)

whenever the explicitly displayed integral is finite. A claimed
polynomial reciprocal-zeta bound is a separate analytic input. The same
profile a(t) and the complete frequency sum are retained.

## 4. What has been improved, and what still blocks the application

The generic cover evaluation norm grows as R^(3/2), and some actual sieve
cosets also have large values. Nevertheless ordinary nonzero Fourier modes
at this specific cusp impose d|k. This gives the uniform-in-R theorem (10)
for E[V_R] and E[V_R^2], with only ordinary reciprocal-zeta and explicit
height/spectral costs. It is a positive estimate for a complete ordinary
nonconstant sector, not merely a counterexample or a conditional desired
moment.

The metaplectic quartic inverse requires a further precise identity:
its unfolded, centered, two-column low-divisor quadratic expression must
be represented by these ordinary induced sections (or another explicitly
controlled collection), with all cusp changes, row-dependent punctures,
angular kernels, and arithmetic diagonal included. This note does not
prove that identity. It would be incorrect to substitute (10) directly for
the missing quartic estimate merely because an ordinary Eisenstein series
occurs somewhere in a spectral calculation.

This distinction can be checked directly against de Faveri, Dunn and
Hoffstein, [arXiv:2607.07911v2](https://arxiv.org/html/2607.07911v2), Sections
4.2, 7.1 and 8. Their Rankin--Selberg transform is formed from
`|E_i(w,s,chi_4)|^2`, with its four cusp constant-term contributions in
equation (7.12), and its nonconstant transform in equation (7.15).
It is not an identity with the induced ordinary series E[V_R^2]. Their
fixed-level numerator moment does not itself supply the missing
growing-level bilinear local and archimedean unfolding. For this note's
bound to apply, that unfolding must retain every (d,e) cross term and
produce ordinary coefficient arrays with a fixed A in (5), while
preserving the Fourier divisibility used in (4). The angular first-Poisson
columns of the quartic problem also require an independently derived
angular normalization; no phase-free angular formula is claimed here.

No full inverse moment and no improved zero-free boundary follow yet.
