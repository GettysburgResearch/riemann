# One CT-admissible field suffices: a complete three-factor ordinary deflator

Status: **PROPOSED exact arithmetic and approximation component.** No new
bound for its complete signed energy is proved. This supplies a legal fixed
field version of PROOF.md, rather than applying the mu_12 interface to a
field that lacks mu_12.

The consumer here is #983's exact ideal-Mobius Gaussian source criterion.
It is not an automatic identification of that source with CT's physical
weighted average; the latter carries an additional Euler correction H.
Section 6 states that remaining interface explicitly.

Let F=Q(zeta_12)=Q(i,sqrt(3)). It contains mu_12 and has degree four and unit
rank one. Let S contain precisely the primes above 2 and 3 for the identities
below; if a particular CT realization enlarges S, retain those finitely many
omissions explicitly as described in section 5. Put

    E_F(D)=sum_(exterior I) mu_F(I) W(NI/D),
    R(D)=sum_((n,6)=1) mu(n) W(n/D),
    W(y)=y^(-c)exp[-log(y)^2/(4tau)]/sqrt(4pi tau), tau>0.

All sums are complete, including every ideal and both tails. The four
characters of Gal(F/Q) give the exact abelian Euler identity

    zeta_F^S(s)=zeta^(6)(s) L_1^(6)(s)L_2^(6)(s)L_3^(6)(s),   (1)

where the three characters on the residues 1,5,7,11 mod12 are respectively

    chi_-4:  +1,+1,-1,-1;
    chi_-3:  +1,-1,+1,-1;
    chi_12:  +1,-1,-1,+1.                                (2)

They vanish on the other residues. Their Dirichlet series are the primitive
quadratic L-functions with their factors at 2 and 3 omitted; the notation
L_j^(6) includes that omission. Consequently

    R=T_1 T_2 T_3 E_F,
    (T_j A)(D)=sum_(n>=1)chi_j(n) A(D/n).                  (3)

For each D these multiple sums converge absolutely by Gaussian flatness
at zero and polynomial divisor counting. Formula (1), or equality of every
Euler coefficient, proves (3). Its fixed Mellin transform is
exp[tau(s-c)^2]/zeta^(6)(s). Thus every ordinary-zeta zero in Re s>0 is
retained and all three unnecessary auxiliary L factors cancel, including
multiplicities of shared zeros.

## 1. The unconditional analytic resource

Fix sigma0>1. Absolute convergence gives

    # {I: NI<=x} <= zeta_F(sigma0) x^sigma0.

No O(x) ideal count or bounded-unit assertion is needed. Integrating this
count against the Gaussian bounds

    sum_I W(NI/D) <= C D^sigma0,
    C=zeta_F(sigma0) integral_0^infinity |W'(y)| y^sigma0 dy. (4)

This finite variation constant follows directly from Stieltjes integration;
it does not assume monotonicity of W. For complex D on a principal-log
sector, the Gaussian identity gives

    |E_F(D)| <= C |D|^sigma0 exp[arg(D)^2/(4tau)].         (5)

All finite-ray and unit choices remain inside the actual E_F. The unit rank
does not disappear from the CT construction; (5) merely counts its ideals.

For F_D(x)=E_F(D/x), Cauchy on |z-x|=x/2 gives, for every m>=0,

    |F_D^(m)(x)| <= C_* |D|^sigma0 m!2^m/x^(m+sigma0),   (6)

uniformly when arg D lies in a fixed compact sector. If at most three such
Cauchy circles are nested, their total argument shift is <=pi/2 and their
moduli are >=1/8. The Gaussian constant is therefore finite and independent
of all derivative orders. Use one larger fixed C_* for all three stages.

## 2. One periodic Euler--Maclaurin compressor

Let chi be any character in (2), q=12, M>=2 even, N=qK, and define

    C_j(chi)=-q^(j-1)/j! sum_(a=1)^q chi(a)B_j(a/q).

The mean-zero property removes the integral term exactly. Applying the
shifted-lattice Euler--Maclaurin formula to each of the four nonzero residue
classes gives the COMPLETE identity

    T_chi E_F(D)=sum_(n<=N)chi(n)E_F(D/n)
           +sum_(j=1)^M C_j(chi)F_D^(j-1)(N)+Rem(D).     (7)

Since chi(N)=0, no endpoint is counted twice. The periodic Bernoulli bound
sup|B_M({x})|<=4 M!/(2pi)^M and (6) give

    |Rem(D)| <=(16/q) C_* |D|^sigma0 N^(1-sigma0)
            M!/(M+sigma0-1) [q/(pi N)]^M.                (8)

This sums all four remainder integrals on [N,infinity); it is not a finite
truncation of an unevaluated infinite tail. With N=48M, K=4M,

    |Rem(D)| <=(4/3) C_* |D|^sigma0 (4pi)^(-M)
                                         /(M+sigma0-1). (9)

The possible sign and endpoint issues in (7) can also be read from the
generating function

    sum_(j>=1) C_j(chi) z^(j-1)
               =sum_(a=1)^q chi(a)e^(az)/(1-e^(qz)).    (10)

Both sides are regular at z=0 by mean zero. This is an authentication of
the signs; the complete remainder is proved by periodic Bernoulli integration.

Normalize J_m=(D partial_D)_m E_F/(2^m m!). Then
F_D^(m)(N)=(-1)^m 2^m m! N^(-m) J_m(D/N). The normalized jet coefficient is

    beta_m=(-1)^m C_(m+1)(chi) 2^m m!/N^m.

The Fourier bound for Bernoulli polynomials and four nonzero residues imply

    |beta_m| <=(8/pi) m![q/(pi N)]^m,
    sum_(m=0)^(M-1)|beta_m| <=(8/pi)/(1-1/(4pi))<3.     (11)

Thus each compressor uses 16M raw rational dilations and M normalized jets,
with a uniformly bounded normalized-jet mass. Each J_m has the compact
Cauchy representation in PROOF.md (18), whose measure has mass one. The
maximal raw derivative order is M-1; its factorial cost has not been hidden.

## 3. Three stages and every mixed remainder

Let P_j be the finite operator in (7). For sigma0>1, the raw dilations have
bounded weighted analytic norm because sum |chi_j(n)|n^(-sigma0)<=zeta(sigma0).
The compact Cauchy representations and (11) show that the jet terms also
have a fixed weighted analytic bound, with a factor at most 3 times
2^sigma0 and the fixed Gaussian sector-width resource. These bounds are
independent of M and N. The exact T_j operators have the same fixed bound
zeta(sigma0) on every fixed sector, by their positive rational dilations.

The telescoping identity

    T_1T_2T_3-P_1P_2P_3
      =(T_1-P_1)T_2T_3+P_1(T_2-P_2)T_3+P_1P_2(T_3-P_3)  (12)

therefore pays all mixed tails using (8)--(11). Every input in each error
term is still an absolutely convergent rational dilation or a compact
Cauchy integral of the original Gaussian source. At most three circles
occur, so (5)--(6) provide one fixed majorant. Hence

    |R(D)-P_1P_2P_3 E_F(D)| <= C_(F,c,tau,sigma0) D^sigma0 (4pi)^(-M). (13)

No dependence on growing jet order or horizon is inside this constant.
This source-specific argument does not claim a bounded inverse on arbitrary
weighted Lp functions.

## 4. A complete cofinal approximation

Fix 0<sigma<sigma0, 1<=p<=infinity, A>0 and T>=2. Choose the least even M
at least (A+sigma0-sigma)log T/log(4pi), enlarged by a fixed constant if
needed, and N=48M. Integrating (13) against D^(-sigma) on the entire past
gives

    ||R-P_1P_2P_3 E_F||_(sigma,p,T) <= C T^(-A).          (14)

There are O_A((log T)^3) finite rational-dilation/normalized-jet terms before
combining coincidences. Their raw coefficient mass is O_A((log T)^3), and
each normalized jet has a fixed compact complex-profile representation.
All constants are for this ONE field. The resulting complete signed energy
upper estimate is still open; taking separate norms of its ideal pieces
can restore the unnecessary three auxiliary L-function burdens.

## 5. Enlarged S

If the legal source removes an extra finite set of rational primes P0,
first target the ordinary source with those primes omitted. At such p the
field factor and all four rational Dirichlet factors are omitted together,
so (1)--(14) hold with the characters additionally zero on p multiples.
They remain mean-zero periodic with a fixed, possibly larger common period;
take q equal to that period, N=4qM, and replace 4 by the fixed number of
nonzero residues in (8),(11). The constants remain fixed.

The resulting rational Mellin denominator is zeta(s) times finitely many
1-p^(-s), all nonzero in Re s>0. It therefore retains every ordinary-zeta
zero in that half-plane. No claim that CT's auxiliary local set is literally
only {2,3} is needed to use this fixed-field reduction.

## 6. The physical CT correction must still be retained

CT's principal physical average has Mellin numerator H(s), a fixed real
shift and a nonzero scalar, rather than the pure transform of E_F above.
Multiplication by the three auxiliary L-functions cancels those factors
from its denominator too, but leaves H(s)/zeta^(6)(s). The argument here
does not silently divide H out.

In the source interface, H is proved holomorphic and nonzero only in its
displayed right half-plane. Zero detection from the deflated PHYSICAL
principal term is therefore justified only in that proved domain, unless
one additionally establishes nonvanishing or constructs a controlled
inverse for H in a larger domain. The cofinal approximation (14) concerns
the exact Mobius E_F and ordinary R as defined, so it has no such correction
factor. A claimed direct physical realization of its complete signed
critical energy would still have to supply this additional interface.
