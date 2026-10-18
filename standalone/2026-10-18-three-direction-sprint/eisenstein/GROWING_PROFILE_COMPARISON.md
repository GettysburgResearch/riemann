# Height-adaptive pole removal as a comparison of actual mixed norms

**PROPOSED source-qualified comparison theorem.** The ORIGINAL zero
detector and ORIGINAL mixed vector are retained. A new vector is used
only as an intermediate in estimating that norm. Its construction may
depend on a separated profile height; it is not claimed to be a single
new zero-preserving detector. The whole difference has a proved cost.
The full continuous/complementary norm of the new vector remains OPEN.

Use the arithmetic, positive response matrix B, and fixed-field ideal
count of `GROWING_RESIDUE_DEBIAS.md`, Sections1--2. The only analytic
moment input in this file is the pinned unrestricted zero-slot
TWO-PLAIN source theorem, with its common-profile calculus and fixed
polynomial height costs. No zero-free input or inverse moment is needed
for the comparison error.

## 1. One common profile, without a false detector substitution

Let the actual row scale be U, inverse length D, and plain length N.
They range over fixed polynomial scales. Let K be a fixed smooth common
profile supported in fixed compact positive norm-ratio boxes. Write

    f_K(u)=(DN)^(-1/2) sum_(a,n)
             mu(a)psi_u(an) K(Na/D,Nn/N,Nu/U).                (1)

The actual common finite twist and orientation are included in psi, and
every original nonunit zero remains. The weighted row space consists of
the complete native nonprincipal sixth-free physical rows. Profiles with
fixed polynomial norm-twist costs are included.

Change independent profile coordinates to

    x=Na/D, y=N(an)/(DN), z=Nu/U.

The transformed common profile is `K(x,y/x,z)`. Fresh fixed cutoffs
`omega_a(x), omega_A(y), omega_u(z)` and Fourier inversion on their
logarithms give

    f_K=integral c(xi,eta,lambda) f_(xi,eta,lambda) dxi deta dlambda,

where a mode has outer coefficient

    alpha_xi(a)=mu(a)omega_a(Na/D)(Na/D)^(i xi),

one product profile `Phi_eta(N(an)/(DN))`, and the row factor
`omega_u(Nu/U)(Nu/U)^(i lambda)`. The density c has finite weighted
Fourier L1 norm at every required FIXED order. This is one common
profile; no separate coefficient choice is made after observing a row.

Fix `G<=D^(1/2-eta_0)`, `eta_0>0`. For each fixed xi set

    Z_g(xi)=sum_(g|a) alpha_xi(a)v(a)/Na,   Ng<=G, g squarefree.

The annular ideal count gives, for each fixed k,

    |partial_xi^k Z_g(xi)| <<_k (Ng)^(-1).                   (2)

Using unnormalized powers instead only adds fixed powers of log D.
The same weaker polylogarithmic bounds also cover an initial prefix
profile equal to one near zero. There is NO assertion of a small
`D^(beta-1)` factor at nonzero xi: that special gain at xi=0 came from
the reciprocal zero at the zeta pole.

Solve the SAME matrix equation

    B xi_vector(xi)=-Z(xi).

Define a modified coefficient at this mode by

    alpha_new,xi(a)=alpha_xi(a)
       +mu(a)^2/v(a) W(Na/D) sum_(g|a,Ng<=G) xi_g(xi).        (3)

The positive matrix B is independent of xi. Its normalized inverse bound
therefore gives, with fixed powers of logarithms suppressed,

    ||partial_xi^k xi_vector(xi)||_f << G^epsilon,
    sum_g |partial_xi^k xi_g(xi)|/sqrt(Ng)
                                << G^(1/2+epsilon).          (4)

For the first estimate, (2) gives
`sum_g |Z_g|^2/f(g)<<G^epsilon`, since the remaining ideal harmonic
sum is logarithmic. The second follows by Cauchy over O(G) labels.
The matrix inverse is a fixed linear map, so the same proof applies to
each indicated derivative. Thus mode-dependent choices are measurable
and have the required smoothness; this is not an uncontrolled choice of
a profile depending on an actual ideal or row.

## 2. The complete comparison error

Replace alpha by (3) in each mode, leaving its product and row profiles
unchanged, and let `f_new,K` be the integral of these modified modes
against the ORIGINAL density c. Then

    ||f_K-f_new,K||_row^2
          << U^(1+epsilon) G (1+height)^C ||K||_J^2,          (5)

where J is a fixed seminorm order. Every sum and profile tail is included.

Indeed, for each g extract `a=g b` in the positive squarefree tail.
It contributes the exact scalar `psi_u(g)/(sqrt(Ng)v(g))`, and the
remaining b-input excludes primes dividing g. As proved in the growing
debiaser, its COMPLETE squarefree-tail Euler representation has absolute
coefficient mass `g^epsilon` times a logarithm, including that moving
input mask. The original nonunit zeros are retained coefficientwise.
The zero-slot TWO-PLAIN theorem bounds its joint root norm with the
plain factor by `U^(1/2+epsilon)g^(-1/2+epsilon)`.

The product profile in (3) is still common. Its additional separation
into the two plain norm coordinates has one fixed weighted Fourier L1
cost, uniformly at every actual shortened length. Apply Minkowski first
over g using (4), and then over the ORIGINAL profile modes using c.
The fixed polynomial height factors are absorbed by its weighted Fourier
L1 norm. This proves (5). No orthogonality between different g, between
different profile heights, or between the tail and the original vector
is assumed.

Consequently

    ||f_K||_row^2 <= 2||f_new,K||_row^2
                       +O(U^(1+epsilon)G(1+height)^C||K||_J^2). (6)

The same comparison can use an arbitrary fixed triangle parameter in
place of two. For `G=U^(1/5)` in the stated Gram range, the complete
error costs `U^(6/5+epsilon)`. More generally the cost is UG.

This leaves the original detector unchanged. In particular, no assertion
that `f_new,K` separately preserves a hypothetical L-zero is needed or
used. Treating (3) as a replacement physical zero detector would require
a different proof and is not licensed by this norm comparison.

### Arithmetic coefficient energy does not lose G

Let `t_xi(a)=alpha_new,xi(a)-alpha_xi(a)`. It has the additional exact
positive energy resource

    xi_vector(xi)^* B xi_vector(xi)
          = Z(xi)^* B^(-1) Z(xi) << (DG)^epsilon.             (8)

This follows from the same normalized inverse bound and (2), rather
than from the pointwise size of a tail coefficient. On the supported
tail annulus `Na` is comparable to D, `W^2<=C W`, and
`v(a)^(-2)<<_epsilon D^epsilon`. Hence directly from the DEFINITION of B,

    sum_a |t_xi(a)|^2
       <= C D^(1+epsilon) sum_a mu(a)^2 W(Na/D)/Na
                         |sum_(g|a)xi_g(xi)|^2
       = C D^(1+epsilon) xi_vector(xi)^*B xi_vector(xi)
       << D^(1+epsilon).                                    (9)

The original annular coefficients also have squared norm O(D).
Consequently `||alpha_new,xi||_ell2<<D^(1/2+epsilon)`, uniformly in the
separated height. The same argument applies to every required fixed
height derivative, with its already displayed logarithmic or profile
cost. This is a complete arithmetic coefficient norm on all ideals,
with no row-dependent choice or omitted mask.

The distinction between resources matters. A theorem depending only
on the arithmetic ell2 norm can use (9) without a factor sqrt(G).
The row comparison (5) was obtained by Minkowski and STILL costs UG;
(9) does not improve that claim. Converting only the normalized ell2
bound to a pointwise bound would cost `G^(1/2+epsilon)`. The exact
inverse below removes that artificial price for EVERY bounded common
annular head, including the original Mobius head.

### Every bounded annular head has subpower pointwise tail coefficients

Keep the annular coefficient alpha_xi from (1), or replace it by any
bounded coefficient sequence with the same common annular profile.
Assume the original
range `G<=D^(1/2-eta_0)`, with fixed `eta_0>0`. Then

    |partial_xi^k xi_g(xi)| <<_(epsilon,k) D^epsilon,
    |partial_xi^k t_xi(a)| <<_(epsilon,k) D^epsilon           (10)

for every required fixed k, uniformly in the separated height and all
supported ideals. For the generalized head the bound uses its supremum
norm and its fixed profile-derivative norms. An initial prefix profile
adds only fixed logarithmic factors. This is a statement for responses
arising from bounded heads, not arbitrary response vectors.

Here is an exact inversion proof. Write `B_0=c_W F` for the main
matrix, `F_(g,h)=f([g,h])`. Extracting `a=g c` in Z_g gives

    w_g=-Z_g/(c_W f(g))=mu(g) A_g,
    |partial_xi^k A_g| <<_k 1.                              (11)

The extracted sum is harmonic over one fixed annulus and its norm
logarithm is bounded there. Its multiplicative prefactor is uniformly
bounded, because

    v(g)/(Ng f(g))
       =product_(p|g) (1+1/((Np)^2+Np-1)) << 1.

The last bound follows from the absolutely convergent prime-ideal
series at exponent two. The coprimality condition on c is retained;
only its absolute value is enlarged in (11).

Solve `B_0 xi^0=-Z`. The downward-closed squarefree label set permits
two exact divisor inversions. Indeed put

    Y_d=Nd sum_(d|h) f(h)xi_h^0.

Then `w_g=sum_(d|g)Y_d`, so
`Y_d=mu(d)sum_(e|d)A_e`. Inverting once more gives

    f(g)xi_g^0
       =mu(g) sum_(g|d,Nd<=G) (1/Nd) sum_(e|d) A_e.         (12)

All signs here use squarefreeness: respectively
`mu(d/e)mu(e)=mu(d)` and `mu(d/g)mu(d)=mu(g)`.
The ideal harmonic divisor bound applied to (12) proves

    |partial_xi^k xi_g^0|
       << tau(g)/(Ng f(g))
                 sum_(Nk<=G/Ng) tau(k)/Nk
       <<_(epsilon,k) G^epsilon.                           (13)

This does not assume that the A_e have one sign. The Mobius factorization
is useful for this exact formula but is not needed for the general
pointwise assertion.

There is a stronger stability estimate in the ACTUAL coefficient
infinity norm than follows by converting the normalized ell2 bound.
The same two divisor inversions give the exact inverse entries

    (F^(-1))_(g,h)
       =mu(g)mu(h)/(f(g)f(h))
                       sum_([g,h]|d,Nd<=G) 1/Nd,
    |(F^(-1))_(g,h)| <<_epsilon (N(g,h)) G^epsilon.        (14)

Indeed, for ANY bounded annular head (2) and (14) give directly

    |xi_g^0| << G^epsilon sum_(Nh<=G) N(g,h)/Nh
       =G^epsilon sum_(d|g) phi(d)/Nd
                             sum_(Nk<=G/Nd) 1/Nk
       << G^epsilon.

All internal small powers are chosen before the prescribed final one.
Thus the main infinity-norm bound holds without any arithmetic sign
factorization of the head. Fixed height derivatives satisfy the same
argument.

Let `E=B-B_0`. Its unnormalized entry error is
`|E_(h,k)|<<D^(-1/2)(N[h,k])^(-1/2)(DG)^epsilon`.
Expanding a divisor majorant for the greatest common divisor gives

    sum_k |E_(h,k)|
        << D^(-1/2)sqrt(G)/sqrt(Nh) (DG)^epsilon,
    sum_h N(g,h)/sqrt(Nh) << sqrt(G)(Ng)^epsilon.          (15)

For the first inequality use
`sum_(Nk<=G) sqrt(N(h,k))/sqrt(Nk)
 <= sum_(d|h) sqrt(Nd) sum_(d|k,Nk<=G) 1/sqrt(Nk)
 << sqrt(G)sum_(d|h)(Nd)^(-1/2)`.
For the second use the exact ideal identity
`N(g,h)=sum_(d|g,d|h)phi(d)` and then
`sum_(d|h,Nh<=G)(Nh)^(-1/2)<<sqrt(G)/Nd`.
Consequently the finite matrix infinity norm satisfies

    ||B_0^(-1)E||_(infinity->infinity)
                         << D^(-1/2)G^(1+epsilon).        (16)

Choose the internal epsilon smaller than the fixed Gram margin.
The right side tends to zero. The Neumann series for
`xi=(I+B_0^(-1)E)^(-1)xi^0` and the main bound after (14) prove the first assertion of
(10) throughout the full range `G<=D^(1/2-eta_0)`. The matrix is
independent of height, so the same proof applies to every fixed
height derivative. The divisor bound and `v(a)^(-1)<<D^epsilon`
give the second assertion of (10).

Thus an analytic estimate requiring a bounded arithmetic phase
coefficient may use (10), with a prescribed arbitrarily small power
loss, for every such bounded head in this range. The comparison (5) STILL
costs UG: bounded pointwise coefficients do not give orthogonality
between the different divisor-tail terms, and their weighted absolute
mass may still cost sqrt(G). Outside these bounded-head and Gram hypotheses, the
corresponding unproved coefficient price must be retained unless
separately bounded. Extending the response construction to a different
head does not establish any new canonical recursion or authorize a
different analytic moment interface.

At the SPECIAL zero height, the reciprocal zero-free input of the
growing-residue debiaser gives a further resource for its original
prefix head. If that input has exponent `beta<1`, its estimate for
Z_g implies `|A_g|<<D^(beta-1)(Ng)^(1-beta)(DG)^epsilon` in (11).
Applying (12) with this weight gives

    max_g |xi_g^0|
        << D^(beta-1)G^(1-beta)(DG)^epsilon.

For example the divisor sum in (12) is bounded by
`D^(beta-1)sum_(g|d,Nd<=G)(Nd)^(-beta+epsilon)`, and its ideal
integral is `O(D^(beta-1)G^(1-beta+epsilon)/Ng)`; the factor
`f(g)^(-1)` costs `Ng` times a subpower. The infinity-norm Neumann
bound (16) preserves this estimate for the actual solution. Thus the
prefix's pointwise correction is
`(G/D)^(1-beta)(DG)^epsilon` throughout the full Gram range.
This extra zero-height gain does not extend to independent nonzero
norm heights. It also does not improve the already displayed
weighted-l1 TWO-PLAIN comparison cost by itself.

## 3. Exact vanishing of all specified modal polar terms

The modified coefficients satisfy

    sum_(g|a) alpha_new,xi(a)v(a)/Na=0
                                 (squarefree Ng<=G).         (7)

For every mode, the actual product-column pairing with
`rho_prim(nR)` is the functional proved in Section3 of the growing
debiaser. Thus (7) removes EVERY squarefree numerator-label polar term
with `NR<=G`, for every xi, eta and lambda. The scalar residue of the
row profile can change with lambda; it still multiplies zero.
These zero terms may be recombined before taking any absolute value.

For the base sixth-power-periodic section, `RESIDUE_VALUATIONS.md`
extends this statement to sixth-free R with `Nrad(R)<=G`, including
fourth-power labels. That radical cutoff must not be replaced by a norm
cutoff in a nonpolar estimate.

This resolves the specific independent-height obstacle for the
PRODUCT-COLUMN polar comparison, at the paid cost UG. It does NOT prove
that the modified coefficients form the canonical family required by
every subsequent two-Poisson recursion. In particular the exceptional
initialization can involve `mu(a)b_D(a)gamma_2(a)`, and the nonconstant
Fourier transforms at exponent-two moduli remain. Neither the full
continuous space nor the complementary row operator has been estimated
at the required strength. A new zero-free boundary does not follow from
(6) until that remaining norm is proved.

The proof is analytic. Exact matrix and local-response identities are
replayed by `growing_residue_check.py`; those finite checks do not test
the Bochner integral or the imported source moment.
