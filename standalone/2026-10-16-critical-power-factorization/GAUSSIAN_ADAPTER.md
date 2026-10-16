# The literal Gaussian detector, with every dilation retained

Status: PROPOSED complete adapter and conditional criterion, not a proved RH
estimate. Same author as PROOF.md and the checker; no independent review.

The gap addressed here is explicit in #948 Section 5: a compact-test
convolution theorem cannot simply be substituted into the noncompact Gaussian
Mellin detector. This note proves the required infinite interchanges and
same-measure bounds directly. It does NOT establish the resulting arithmetic
bound, even for the principal scalar source.

## 1. The actual test and its absolutely convergent physical series

Keep F,S,m,a,b,p_m,q_m,u_m,v_m from PROOF.md. For a fixed real c set

    W_c(y)=(2 sqrt(pi))^(-1)y^(-c)exp(-(log y)^2/4), y>0.

It satisfies, for every real N, |W_c(y)|<=C_(c,N)y^(-N) globally on y>0.
Completing a square proves this immediately. Its Mellin transform is

    integral_0^infinity W_c(y)y^s dy/y = exp((s-c)^2).     (G1)

Substitute t=log y and evaluate the Gaussian Fourier integral; alternatively
complete the square first for real s, then extend the two entire functions
by analytic uniqueness. Gaussian domination on compact s-sets proves that
the integral is entire. In particular it has NO zeros.

All phase-uniform absolute Dirichlet series for p_m and q_m converge for
real sigma>1. For p_m use the local majorant
1+(1-1/q)q^(-sigma)+q^(m/2-1-m sigma); for q_m use
(1+q^(-sigma))(1+q^(m/2-1-m sigma)). Their prime sums converge. The Mobius
source has the majorant product(1+q^(-sigma)).

Define A_u(X),B_u(X),C_u(X) as in PROOF.md but with W=W_c. These are infinite
sums, absolutely and locally uniformly convergent on X>0, uniformly in all
phases and masks. To prove this, choose sigma>1, dominate each summand by
C_(c,sigma)X^sigma |coefficient| (Nn)^(-sigma), and bound X on a compact set.
For X<=1 and any B>0 choose sigma>max(1,B); this gives O(X^B), uniformly in u.
For a row measure w of total mass Z, the same statements hold in Lp(w) with
an additional factor Z^(1/p). This also proves finiteness of the truncated
scale envelopes appearing below. Z=0 is harmless.

## 2. Infinite convolution really commutes with this Gaussian sum

For every X>0 the two identities

    B_u(X)=sum_n u_m(n;u) C_u(X/Nn),
    C_u(X)=sum_n v_m(n;u) B_u(X/Nn)                       (G2)

hold with absolute locally uniform convergence. Indeed at any sigma>1 the
double absolute majorant factors into the finite coefficient norms of the
kernel and source, times C X^sigma. Fubini and the finite coefficient
identities (3) of PROOF.md then apply. The same proof in Lp(w) is justified
by the row-independent majorants. No truncation of the Gaussian tails is
being assumed.

It follows exactly as in Corollary 3 of PROOF.md that the critical envelopes
for B and C, now at this SAME Gaussian, compare with cost exp(5d) in both
directions. The critical kernel tail bound also survives unchanged.

Similarly the exact two-channel identities are

    C_u(X)=sum_n mu_F(n)b(n;u)(Nn)^(m/2-1) A_u(X/(Nn)^m),
    A_u(X)=sum_n b(n;u)(Nn)^(m/2-1) C_u(X/(Nn)^m).       (G3)

To justify Fubini before estimating, use sigma>1 as above. The extra absolute
series is zeta_F^S(m sigma-m/2+1)<infinity. This is also an elementary way
to check the inverse sign and scale. There is no extra condition that the
dilation ideal and residual coefficient ideal be coprime.

### Theorem G (same-Gaussian, same-height comparison)

Let alpha>1/2, p>=1, D>0, and define E_(A,alpha,p)(D) as the supremum over
0<X<=D of X^(-alpha)||A(X)||_(Lp(w)); similarly for B,C. Then

    E_(B,alpha,p)(D) <= K E_(A,alpha,p)(D),
    E_(A,alpha,p)(D) <= K E_(B,alpha,p)(D),               (G4)

where a phase-, m-, p-, D-, and row-measure-independent choice is

    K=exp(5d) zeta_F^S(1+2(alpha-1/2)).                  (G5)

A sharper m-dependent choice replaces 2 by m.

Proof. The correction kernel's alpha-norm is at most its 1/2-norm. Apply
Minkowski to (G2) and (G3). The power in the latter kernel is
(Nn)^(m/2-1-m alpha), whose sum is at most
zeta_F^S(1+m(alpha-1/2)). Since m>=2 and the positive ideal zeta series
decreases on real arguments >1, this is bounded by the zeta factor in (G5).
All scale arguments on the right are <=X<=D. Their actual row measure is
unchanged. This proves both directions. QED.

For a single fixed row and fixed phase data, (G4) proves the equivalence

    A(X)=O_epsilon(X^(1/2+epsilon)) for every epsilon>0
    iff
    B(X)=O_epsilon(X^(1/2+epsilon)) for every epsilon>0.  (G6)

The small-X bounds in Section 1 handle the lower end of the envelopes.
For a varying physical family w_H, (G4) instead compares estimates at ALL
SHORTER scales with H held fixed. A bound supplied only on H=X^h is not
silently strengthened to that premise. This distinction remains even though
the test is now fixed and noncompact rather than an arbitrary compact test.

At alpha=1/2 the zeta factor in (G5) is divergent. The theorem does not
claim constant-cost native recovery at the endpoint. All-epsilon estimates
use alpha>1/2 fixed first. This does not conceal a uniform growing-order or
shrinking-zero-height bound.

## 3. Match the source's normalization, not just its Euler factors

Specialize to m=6, c=5/6, the principal target a_p=1, and the actual b_p from
the pinned source. Put C_S=product_(p notin S)(1-q^(-2)). Keep the notation
widetilde g of #949, which includes its factor Z^(61/100) relative to the
Quantitative.Spectral.f function. It is NOT the differently normalized g
in Section 4 of #948.

On Re(s)=2, #949's source identity and its signed dilation give

    widetilde g(Z) = C_S B(Z).                           (G7)

Here is the source-dependent derivation in full. The initial Mellin numerator
is exp((s-5/6)^2) H(s)/L^S(s). Multiplying by E_b(6s-3) as in #949 replaces
H by widetilde H. For the principal target, the exact local identity gives

    widetilde H(s)/zeta_F^S(s)=C_S product_p P_p(q^(-s)).

Expand the absolutely convergent coefficient series on Re(s)=2 and interchange
it with Gaussian Mellin inversion. The vertical Gaussian has modulus
exp((2-5/6)^2-t^2), and the coefficient absolute series on that line is finite.
Inversion using (G1) yields C_S sum_n p_6(n)W_(5/6)(Nn/Z), exactly (G7).
Thus no compact-test hypothesis or undocumented removal of the Gaussian tails
is used. Equality with the imported theta source still depends on its actual
Mellin identity; that entire external proof is not independently certified here.

The new factorization also gives, initially Re(s)>1,

    integral_0^infinity widetilde g(Z)Z^(-s)dZ/Z
      = C_S exp((s-5/6)^2) U_6(s)
                     E_b(6s-2)/zeta_F^S(s).             (G8)

The shifted argument is now 6s-2, NOT 6s-3. On Re(s)>1/2, E_b(6s-2) is an
absolutely convergent, nonvanishing Euler product regardless of whether b
is a Hecke character. U_6 is nonvanishing there by PROOF.md. These statements
do not authorize an Euler product for 1/zeta_F^S below Re(s)=1.

Consequently #949's OPEN-R at every positive epsilon is equivalent, via
(G6)-(G7), to the same all-epsilon Gaussian Mobius estimate for the original
fixed scalar source A. This is a transparent reduction, NOT a new estimate.
It closes the specified Gaussian adapter, not the original analytic frontier.

## 4. A mean-square alternative that also detects every off-critical zero

The pointwise bound is sufficient but need not be the first arithmetic target.
For the actual B of Section 3, consider

    integral_X^(2X) |B(Z)|^2 dZ/Z <= C_epsilon X^(1+epsilon)
      for every X>=1 and every epsilon>0.               (OPEN-G2)

This bound is NOT PROVED. It is sufficient for zero exclusion on Re(s)>1/2.
Indeed, for sigma>1/2, choose epsilon>0 with (1+epsilon)/2<sigma. Cauchy on
each dyadic interval bounds its absolute Mellin integral by a constant times
X^((1+epsilon)/2-sigma). Summing geometrically and using small-Z flatness
proves absolute Mellin convergence. Logarithmic factors needed to differentiate
are absorbed by the strict margin, so the transform is holomorphic there.
Multiply (G8) by the actual continued zeta_F^S and use analytic uniqueness
on the half-plane with the point 1 removed. A zeta zero would make the left
side zero while the entire Gaussian times U_6 E_b is nonzero. Contradiction.
Finite excluded Euler factors have no zeros in this region and can be restored.

For the auxiliary field F used by the imported Dedekind proof, its existing
abelian descent would then give the corresponding original-field result.
This implication remains conditional on OPEN-G2; no L2 estimate has been
obtained by merely writing Mellin--Plancherel or a positive Gram form.

## 5. What the attempted resolution did not establish

The source's old power bounds, inserted into (G2)-(G3), retain their old
exponent. The multiplier cost is now completely controlled, including the
literal Gaussian, but neither channel has acquired a square-root arithmetic
bound. The same original signed prime/cofactor correlations are still present.

#946's injection-minus-compensation theorem pertains to its stated native
family. An identification of that family with the imported theta/Poisson
probe, before Cauchy or absolute values, still requires proof. This note does
not invent that missing equality. Nor does uniformity of (5) in m prove an
automorphic construction or a moment theorem for varying covers.
