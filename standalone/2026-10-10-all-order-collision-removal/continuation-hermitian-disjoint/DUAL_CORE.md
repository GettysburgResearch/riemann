# The remaining arithmetic core has primitive conductor and no common-prime masks

**Status:** proposed complete sector bounds and exact dual identities, plus a conditional moment-to-zero implication. The high-conductor signed estimate is NOT proved.

Use PROOF.md, its enlarged fixed S, m=2k, sigma=1/2+delta with 0<delta<1/2, and the Gaussian row measure exp(-Nu/H) on all nonzero Eisenstein elements. Use the nonnegative W_* from the frozen integrated-window packet for the final zero implication. A generic nonnegative bounded compact window suffices for the sector estimates.

## 1. Exact primitive-only decomposition

For squarefree COPRIME r,s put

    Q=Nr Ns,
    psi_(r,s)(u)=chi_r(u)bar(chi_s(u)),
    J_D(r,s)=integral_0^D w_X(r)w_X(s) X^(-2k sigma)dX/X.

The Hermitian scalar is

    I_C(D;H)=U_0(D;H)
       +sum_(r!=s, (r,s)=1) mu_K(r)mu_K(s)nu(r)bar(nu(s))
                                  J_D(r,s) S_psi(H),        (1.1)
    U_0(D;H)=[sum_(u!=0) exp(-Nu/H)]
                     integral_0^D W(1/X)^(2k)X^(-2k sigma)dX/X,
    S_psi(H)=sum_(u in O) psi(u)exp(-Nu/H).

Every term with r!=s has Q>1 and primitive nonprincipal psi. The u=0 term is zero for those characters. It is NOT inserted into U_0. The lattice count gives 0<=U_0(D;H)<<H, uniformly in D,H>=2.

Let j(r)=sum_(p|r)(Np-1)/6 modulo 6. Radial invariance under the six units gives S_psi(H)=0 unless j(r)=j(s). Since each Np is 1 modulo 6,

    j(r)=(Nr-1)/6 modulo 6.

Thus every surviving pair has Nr=Ns modulo 36. In particular psi(-1)=1. These are exact finite-character identities, not probabilistic cancellation claims.

## 2. Stronger low-conductor decay after removing all overlaps

Let A_prim,<=Q0 be the ABSOLUTE sum of the nonunit terms of (1.1) with conductor at most Q0. For every fixed A>0 and epsilon>0,

    Q0<=H:
      A_prim,<=Q0 << D^epsilon H^(-A) Q0^(A+1-delta),
    Q0>=H:
      A_prim,<=Q0 << D^epsilon min{Q0^(1-delta),
                                             H Q0^(1/2-delta)}. (2.1)

There are also absolute constants c>0 and C_(fixed data,epsilon) such that

    Q0<=H:
      A_prim,<=Q0 << D^epsilon H Q0^(-delta) exp(-cH/Q0).     (2.2)

The constant in the first line of (2.1) may depend on A. For every fixed eta>0 and N>0, (2.2) implies

    A_prim,<=H^(1-eta) << D^epsilon H^(-N).                  (2.3)

When eta>=1 the retained nonunit range is eventually empty; the interesting case is 0<eta<1. This super-polynomial removal is a property of the NEW primitive-only scalar, not an assertion about all the shared-gcd terms in the old covariance.

**Proof.** The finite character is primitive modulo the primary generator of rs. Put c_K=2pi/sqrt(3), tau(psi)=sum_(x mod rs)psi(x)e_K(x/(rs)), where e_K(z)=exp(4pi i Im(z)/sqrt(3)). The saved Gaussian packet proves, with the original zero conventions,

    |tau(psi)|=sqrt(Q),
    S_psi(H)=c_K (H/Q) tau(psi)
       sum_(v!=0) bar(psi(v)) exp(-c_K^2 H Nv/Q).            (2.4)

There is no zero-frequency term and, because (r,s)=1, NO divisor-mask sum. Gaussian lattice counting, together with the direct row count, yields

    |S_psi(H)| << min{H, sqrt(Q), sqrt(Q)(Q/H)^A},
    |S_psi(H)| << (H/sqrt(Q)) exp(-c_0 H/Q) when H>=Q.       (2.5)

For the exponential bound, the nonzero lattice norm is at least one and the Gaussian sum at parameter t>=1 is O(exp(-c_0 t)); a smaller fixed c_0 absorbs its polynomial factor.

The allocation bound and compact support give

    J_D(r,s) << D^epsilon max(Nr,Ns)^(-2sigma)
              <=D^epsilon Q^(-sigma).                     (2.6)

The number of ideal pairs with Nr Ns<=R is O(R log(2R)), by ideal counting and the ideal harmonic sum. On a dyadic conductor band Q<Nr Ns<=2Q, (2.5)-(2.6) therefore give a small D-power times

    min{H Q^(1/2-delta), Q^(1-delta),
                                      H^(-A)Q^(A+1-delta)}.

Logarithms can be absorbed into D^epsilon since only Q<=(bD)^(2k) occurs. The relevant powers increase with Q for 0<delta<1/2. Summing bands proves (2.1). Applying the exponential bound similarly gives band mass at most D^epsilon H Q^(-delta)exp(-c_1H/Q). Summing downward dyads costs a fixed constant after slightly decreasing c_1, proving (2.2). Finally exponentials dominate each fixed power in (2.3). QED.

The absence of the former common-divisor sum is essential. Its positive absolute estimate only supplied (Q/H)^(2delta). That sum has not been declared zero; its completed SIGNED effect was absorbed by PROOF.md Theorem 1.1.

## 3. Conditional zero-free implication from this smaller primitive core

Set Q_*=H^(1/(1-delta)). Define R_prim(D;H) by retaining from the ordered signed sum (1.1) ONLY

    (r,s)=1, Q=Nr Ns>Q_*, and Nr=Ns modulo 36.               (3.1)

Every original ordered allocation and every nu phase remains. The ordered sum is real by the r,s interchange. Equations (1.1)-(2.1) give

    I_C(D;H)=R_prim(D;H)+E(D;H),
    |E(D;H)|<<D^epsilon H.                                 (3.2)

Because I_C>=0 by the Hermitian comparison, R_prim>=-C_epsilon D^epsilon H. The error E need not be nonnegative.

Suppose, for fixed h>0, lambda>=0, all epsilon>0 and all sufficiently large D, that

    R_prim(D;D^h)<=C_epsilon D^(h+lambda+epsilon).            (3.3)

THIS IS THE UNPROVED ARITHMETIC INPUT. Then (3.2) and (1.3) of PROOF.md imply the same bound for the FULL original integrated 2k-th moment I_M with Gaussian rows.

For completeness, its prime extraction is direct. With Y=D^(h/6), there are asymp Y/log Y prime ideals outside the fixed S with Y/2<Np<=Y. The rows p^6 have Gaussian weights at least exp(-1). Exact prime removal reads

    A_1(X)=A_(p^6)(X)-nu(p) A_(p^6)(X/Np).

The norm in L^(2k)((0,D),X^(-2k sigma)dX/X) of a q-dilate is at most q^(-sigma) times the original norm. Thus the target norm is at most twice each replica norm. Summing these distinct replica rows gives

    integral_0^D |A_1(X)|^(2k)X^(-2k sigma)dX/X
                       <<D^(lambda+5h/6+epsilon).           (3.4)

No prime is inserted into the fixed-data constants. The row range remains fixed in every scale integral.

The fixed W_* has Mellin transform

    F_*(s)=product_(j>=1) sinh(2^(-j)s)/(2^(-j)s),

which is nonzero for Re(s)>0. Holder on dyadic X intervals applied to (3.4) makes integral A_1(X)X^(-s)dX/X holomorphic when

    Re(s)>alpha=1/2+delta+(lambda+5h/6)/(2k).                 (3.5)

On Re(s)>1 that transform is F_*(s)/L_K^S(s,nu). Divide locally by nonzero F_*, and use nonvanishing of the finitely deleted Euler factors on Re(s)>0. This proves the conditional zero-free statement. Principal poles are allowed; the boundary is strict. The full proof of the single-window properties and the fixed-field prime count interface is retained in the integrated-window predecessor.

Cofinal k with delta_k->0 and (lambda_k+h_k)/k->0 would give the critical-line conclusion, with constants allowed to depend on k. For zeta alone the principal Hecke target over K suffices logically via zeta_K=zeta L(chi_-3). None of these conclusions is attained here, since (3.3) is not proved.

## 4. The high-conductor dual source is exact, but not automatically shorter

In (2.4) put omega_psi=tau(psi)/sqrt(Q), so |omega_psi|=1. It gives the exact identity

    S_psi(H)=c_K H/sqrt(Q) omega_psi
                       S_(bar psi)(Q/(c_K^2 H)).            (4.1)

Substituting this into (3.1) gives the high-conductor source with all Mobius signs, allocation weights and normalized Gauss phases preserved. Its effective dual row norm is Q/(c_K^2 H). There are no exterior gcd masks. This is a genuine simpler input for a new cubic-theta or coefficient-sensitive estimate, not such an estimate itself.

Applying (4.1) twice returns the original H. Indeed c_K^2 H[Q/(c_K^2 H)]/Q=1 and the Gauss identity gives omega_psi omega_(bar psi)=psi(-1)=1 in the surviving unit sector. For odd parity both radial sums vanish. Thus merely repeating Gaussian Poisson summation is an INVOLUTION, not a contraction. A proof must use an additional arithmetic estimate or an admissible range-enlargement argument with its full cost; it cannot declare the second transform shorter by omitting Q/H.

Finally Q<=(bD)^(2k). Extending the generic removable range Q<=H^(1/(1-delta)) across the whole support would require h>=2k(1-delta) at the exponent level. Formula (3.5) then gives alpha>=4/3+delta/6>1. This explicitly prevents turning the sector result into a spurious full RH proof.
