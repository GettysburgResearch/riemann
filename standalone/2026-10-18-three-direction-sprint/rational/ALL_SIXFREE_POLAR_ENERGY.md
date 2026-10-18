# Complete weighted principal-functionals, including exponent-five labels

**PROPOSED source-qualified component theorem.** These are bounds for
the exact principal coordinates with their ACTUAL label weights. No
claim that they exhaust a spectral or physical row operator is made.
The full nonconstant/covariance remainder is OPEN.

Use the annular corrected head of `ANNULAR_PROFILE_DEBIAS.md`, the
omitted-response estimate (5) of `ALL_LABEL_POLAR_TAIL.md`, and the
BASE fixed section's complete local principal formula in
`../eisenstein/RESIDUE_VALUATIONS.md`. For every good sixth-free R put

    L_R=sum_(g|rad R) c_R(g)F_g,
    c_R(g)=product_(p|g)c_(e_p)(p), e_p=ord_p R,
    c_e(p)=1/q-1/q^2 for 1<=e<=4,
    c_5(p)=q-1/q, q=Np.                              (1)

The true principal term has, in addition to its common constants,
the factors X^(5/6)*(NR)^(-1/6)*v(R)*Phihat(5/6). Here v(R)=v(rad R)
has absolute value at most one. The unweighted SF scalar argument
cannot cover e=5 because c_5 is large; both estimates below retain
the missing true (NR)^(-1/6) factor or its square.

All assertions hold also for each fixed kappa derivative, with a fixed
factor (1+|kappa|)^A. Their original common Fourier densities integrate
that factor exactly as in the annular comparison. The profiles and
base section have the same scope as the cited exact local formula.

## 1. A uniform weighted scalar bound

The root agent independently identified this direct weighted extension.
For every divisor g|rad R, split g=g_s*g_t, where g_t contains exactly
the primes of valuation five in R. By (1),

    |c_R(g)|<=Ng_t/Ng_s,
    (NR)^(-1/6)|c_R(g)|
                 <=(Ng_t)^(1/6)/(Ng_s) <=(Ng)^(1/6).  (2)

The first bound uses c_5<=q and c_e<=1/q for e<=4; the second retains
the valuation-five contribution p^(-5/6) from the actual R weight.
The exact solved constraints kill every Ng<=G. Multiplying the two
terms of the omitted-response estimate by (2), for Ng>G, bounds each by

    D^(beta-1)G^(1/6-beta),

since beta>1/2>1/6. Divisor counting therefore proves, for EVERY
polynomially bounded sixth-free R,

    (NR)^(-1/6)|v(R)L_R|
       << (1+|kappa|)^A
           D^(beta-1)G^(1/6-beta)(DGR)^epsilon.         (3)

This is weaker than the SF unweighted-functional bound and includes
all valuations through five. It still requires the true X^(5/6)
and Mellin-profile factors when inserted in the full principal term.

## 2. The complete natural label-energy bound

The exponent-five rarity gives the stronger COMPLETE positive energy
estimate, for every polynomially bounded Z>=1,

    sum_(R good sixth-free,NR<=Z)
             (NR)^(-1/3)|v(R)L_R|^2
       << (1+|kappa|)^A (DGZ)^epsilon
                    Z^(2/3)D^(2*beta-2)G^(-2*beta-2).   (4)

This sum includes EVERY permitted label and every exponent-five prime;
there is no radical cutoff or condition that a large label be squarefree.

Indeed divisor Cauchy bounds |L_R|^2 by R^epsilon times
sum_(g|rad R)|c_R(g)|^2|F_g|^2. Swap these finite positive sums.
For a fixed squarefree g write R=R0*r, where R0 has exactly the primes
of g, each to one of its five possible exponents, and (r,g)=1. The
remaining sixth-free restriction may be enlarged positively. The
elementary fixed-field ideal count gives

    sum_(Nr<=Z/NR0)(Nr)^(-1/3) << (Z/NR0)^(2/3).

Including R0^(-1/3), its resource is Z^(2/3)/NR0. Consequently the
complete local factor for each p|g is

    sum_(e=1..5) |c_e(p)|^2/q^e << q^(-3).             (5)

For e<=4 this starts with q^(-3); for e=5 the apparently large q^2
is multiplied by q^(-5), giving the SAME q^(-3). The product of the
bounded local constants is g^epsilon. Thus

    sum_(NR<=Z,g|rad R) (NR)^(-1/3)|c_R(g)|^2
                         <<_epsilon Z^(2/3)(Ng)^(-3+epsilon). (6)

All g<=G have F_g=0. For the remaining g, the omitted-response bound
and the ideal integral give

    sum_(Ng>G) |F_g|^2/(Ng)^(3-epsilon)
       << (1+|kappa|)^A (DG)^epsilon
              D^(2*beta-2)G^(-2*beta-2).              (7)

The two integrals are respectively sum g^(-2*beta-3) and
G^(2-2*beta)sum g^(-5); both have the same displayed G power.
Equations (6)--(7) prove (4). No cancellation or independence between
different principal coordinates is needed for this POSITIVE label sum.

## 3. Explicit budget and remaining interface

For beta=7/8 and G=D^(1/5), whose COMPLETE annular mixed-norm
comparison costs U^(1+epsilon), equation (4) is

    sum_(NR<=Z, sixth-free) R^(-1/3)|v(R)L_R|^2
                              << (DGZ)^epsilon Z^(2/3)/D. (8)

At the adaptive U^(6/5) comparison cutoff G=U^(4/25)D^(1/5), it is

    << (UDZ)^epsilon U^(-3/5)Z^(2/3)/D.                (9)

If the common full principal coordinate is
P_R=C*X^(5/6)*R^(-1/6)*v(R)*Phihat(5/6)*L_R, multiply (4),
(8), or (9) by |C*Phihat(5/6)|^2*X^(5/3). Bounded varying profile
Mellin values are paid by their supremum after the original common
profile separation. An unrelated weight on R or a different numerator
section needs its own resource calculation.

For the ACTUAL adjoint normalization, the primary
[rStation paper 10/v2, (7.1)--(7.3)](https://rstation.ai/problems/riemann_hypothesis/papers/10)
gives `A^*v_R(n)=U^(1/6)*w_hat(2/3)*rho_prim(nR)+E_R(n)`.
Pairing its residue term with the normalized mixed coefficient,
whose product length is L=DN, has a factor L^(-1/2). The Type-I
MAINTERM in the matched base fixed section therefore has the actual
normalization

    M_R=C U^(1/6)L^(1/3)R^(-1/6)v(R)L_R.              (10)

Here the Type-I length is X=L and C includes the two fixed Mellin
values and fixed local constants. Equations (4) and (10) give

    sum_(NR<=K,sixth-free)|M_R|^2
       << (UDGK)^epsilon U^(1/3)L^(2/3)K^(2/3)
                              D^(2*beta-2)G^(-2*beta-2). (11)

At beta=7/8 and G=D^(1/5), this is
`U^(1/3)D^(-1/3)N^(2/3)K^(2/3)` times subpowers. Across
D>=U,N<=sqrt(U), it is at most U^(1/3)K^(2/3), hence at most U
for EVERY K<=U. The adaptive U^(6/5) comparison cutoff further
multiplies this bound by U^(-3/5).

Equation (11) controls the Type-I MAINTERM of those actual pole
pairings in the matched fixed section. It does not control the whole
residue pairing: its nonconstant Type-I error and the independent
adjoint contour remainder E_R are still present. Nor is it a
synthesis/eigenbasis statement. Other fixed sections require their
own verified local principal formula before being added. The factor
U^(1/3)L^(2/3) in (11) is essential; it cannot be discarded by
calling the mainterm a normalized scalar.

These are complete weighted PRINCIPAL-coordinate estimates. Applying
them to the original mixed mean requires an exact matching of its
coordinates, their normalizations and the full nonconstant part.
They do not assume or prove a Gram orthogonality theorem, a complete
eigenbasis, or a paid continuous operator. The full U^(6/5) mixed
estimate and every improved zeta boundary therefore remain unproved.

