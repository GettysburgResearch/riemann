# Conditional CRT nonreturn with the actual nonunit mask

Status: **Proposed component deductions C-M1--C-M5, pending independent
review.** The ideal counting estimate is proved here. The nonreturn
conclusion explicitly assumes the uniform full-twist analytic input of
PR912 Section 5. It proves no new zero-free line, short-row moment upper
bound, or RH statement.

Scope: K=Q(sqrt(-3)), O_K=Z[omega], omega^2+omega+1=0, and N denotes
the ideal or element norm. S is a fixed finite set of prime ideals that
contains the primes over 6. The coefficient character is **nu=1**.
All ideals below are nonzero integral ideals. W is a fixed nonzero
nonnegative function in C_c^infinity((0,infinity)). Constants may depend
on K,S,W and the fixed exponents, but not on the moving elements b,v or
the scale D.

Exact dependencies: the finite ideal CRT and literal sextic zero
extensions in `correlations/MOBIUS_CRT_TRANSLATION.md` T-M1--T-M3;
the unit-frequency argument C-F5 in `CRT_SHORT_FOURIER.md`; and PR912,
`standalone/2026-10-10-generalized-inverse-moments/MELLIN_AND_SPIKES.md`,
Section 5 at commit `6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`.
The lattice count and squarefree inclusion-exclusion are classical;
the contribution is their uniform moving-mask adapter for C-F5.

What was actually run: `check_masked_crt_nonreturn.py` enumerates actual
split and inert prime ideals and literal squarefree sharp-band columns,
constructs a coherent CRT element, and checks the masked identity with
unit and nonunit base rows by exact integer residue arithmetic. Its finite
output does not certify the asymptotic counting theorem or imported
analytic hypothesis. `MASKED_CRT_EXECUTION.json` records the runs.

## C-M1. Ideal counting with a moving coprimality mask

Put kappa_K=pi/(3sqrt(3)). The number I_K(y) of integral ideals of norm
at most y satisfies, uniformly for all y>0,

    I_K(y)=kappa_K y+O_K(sqrt(y)).                         (C-M1)

Indeed O_K has class number one, six units, and lattice covolume
sqrt(3)/2 in C. Each ideal has six generators. Counting nonzero lattice
points in the disc of radius sqrt(y), by cells intersecting its boundary,
gives area/covolume with error O(sqrt(y)+1). For y>=1 the constant is
absorbed by sqrt(y); for 0<y<1 the actual count is zero and y<=sqrt(y).
This also gives I_K(y)=O_K(y) for y>=1. Partial summation consequently
gives

    sum_(Nd<=T) 1/Nd = O_K(log(2T)),
    sum_(Nd>T) 1/(Nd)^2 = O_K(1/T),                       (C-M2)

for T>=1.

For an arbitrary nonzero ideal h, let rad(h) be the product of its distinct
prime factors and define

    Q_h(x)=sum_(Nn<=x,(n,h)=1) mu_K(n)^2,
    P(h)=product_(p|h)(1+(Np)^(-1/2)).

For every x>=1 the following error constant is independent of h:

    Q_h(x)=(kappa_K/zeta_K(2)) x
             product_(p|h)(1+1/Np)^(-1)
           +O_K(sqrt(x) log(2x) P(h)).                   (C-M3)

Proof: coprimality inclusion-exclusion and (C-M1), also when y/Ne<1,
give

    I_h(y):=sum_(Nm<=y,(m,h)=1)1
      =sum_(e|rad(h))mu_K(e) I_K(y/Ne)
      =kappa_K y product_(p|h)(1-1/Np)
         +O_K(sqrt(y) P(h)).

Use the exact identity mu_K(n)^2=sum_(d^2|n)mu_K(d). Because (n,h)=1
forces (d,h)=1,

    Q_h(x)=sum_(Nd<=sqrt(x),(d,h)=1) mu_K(d) I_h(x/(Nd)^2).

The errors sum to O_K(sqrt(x) P(h) log(2x)) by (C-M2).
The absolutely convergent main series extended to all d is

    sum_((d,h)=1) mu_K(d)/(Nd)^2
      =1/zeta_K(2) product_(p|h)(1-(Np)^(-2))^(-1).

Its discarded absolute tail is O_K(x^(-1/2)), uniformly in h, by
(C-M2). Multiplying by x product_(p|h)(1-1/Np)<=x adds O_K(sqrt(x)).
Finally (1-1/Np)/(1-(Np)^(-2))=(1+1/Np)^(-1), proving (C-M3).

## C-M2. Polynomial masks retain almost linear positive mass

For every fixed epsilon>0 there are positive constants c_epsilon,
C_epsilon, independent of h, such that

    product_(p|h)(1+1/Np)^(-1) >= c_epsilon (Nh)^(-epsilon),
    P(h) <= C_epsilon (Nh)^epsilon.                      (C-M4)

For all sufficiently large Np, each of 1+1/Np and 1+(Np)^(-1/2) is
at most (Np)^epsilon. The finitely many smaller prime ideals cost one
constant, because each appears at most once. Since Nrad(h)<=Nh, the
products give (C-M4). No prime-ideal theorem or uniform Mertens product
estimate is needed.

Fix A>0 and gamma>0. For every nonzero b with Nb<=D^A,

    sum_(n squarefree,(n,bS)=1) W(Nn/D)
         >= c_(A,gamma,S,W) D^(1-gamma)                  (C-M5)

for all sufficiently large D, uniformly in b. Here bS abbreviates the
ideal (b) times the fixed product of S.

Choose 0<alpha<beta and w_0>0 with W(y)>=w_0 on [alpha,beta]; such
an interval exists by continuity and W not identically zero. Set
h=(b) product(S), so Nh<=N(product(S))D^A. Apply (C-M3) to beta D
and alpha D and subtract. By (C-M4) its main term is at least
c D^(1-A epsilon), whereas its error is at most
C D^(1/2+A epsilon) log(2D). Choose epsilon>0 with
A epsilon<min(gamma,1/4). The main exponent exceeds the error exponent
and is at least 1-gamma. Counting alpha D<Nn<=beta D, then multiplying
by w_0, proves (C-M5). All thresholds are independent of b; no effective
constant or claimed best product loss is supplied.

## C-M3. Exact cancellation with the retained zero mask

For each D let P_D consist of the prime ideals occurring in any squarefree
ideal n coprime to S for which W(Nn/D)>0, and let Q_D=product(P_D).
This is finite. Choose any unit t_D modulo Q_D satisfying
chi_p(t_D)=-1 for every p in P_D, as permitted by ideal CRT.

If b,v are nonzero elements and v==t_D b modulo Q_D, put w=v b^5.
For every p in P_D,

    chi_p(w)=-1 if p does not divide b,
    chi_p(w)=0  if p divides b.                          (C-M6)

For p not dividing b, multiplicativity gives
chi_p(w)=chi_p(t_D)chi_p(b)^6=-1. For p dividing b, the congruence
also gives p|v and hence p|w, so the literal zero extension gives zero.
Consequently, on the whole active source,

    mu_K(n) chi_n(w)=1_((n,b)=1),

including all nonunits. Therefore the actual source at nu=1 satisfies

    A_w(D;W)=sum_((n,S)=1)mu_K(n)chi_n(w)W(Nn/D)
       =sum_(n squarefree,(n,bS)=1)W(Nn/D).               (C-M7)

The right side is a positive masked squarefree sum, rather than the
unmasked sum in the original coherent translator argument. No assertion
that b^6 is a unit residue is made.

## C-M4. Exact conditional nonreturn theorem

Explicit analytic hypothesis U_B: for a fixed B with 1/2<=B<1, every
fixed P>0 and every fixed delta>0, the literal nu=1 family satisfies

    |A_u(D;W)| <= C_(P,delta,S,W) D^(B+delta)
       for all D>=D_0 and 0<Nu<=D^P.                    (C-M8)

This is the uniform polynomial-row estimate supplied by PR912 Section 5
when the entire sextic twist family is zero-free in Re(s)>B and the
uniform reciprocal, polynomial conductor, and deleted-factor estimates
(5.1)--(5.3) hold. Pointwise bounds with uncontrolled u-dependent
constants are insufficient. The fixed smooth W need not be the universal
test W_*: its Mellin transform has the same required rapid vertical decay.
We do not establish U_B or a full-family B<1 here.

Under U_B, for every fixed A,C>0, for all sufficiently large D there
are **no nonzero** elements b,v such that

    Nb<=D^A, Nv<=D^C, v==t_D b modulo Q_D.               (C-M9)

There is no unit hypothesis on b. Otherwise w=v b^5 is nonzero with
Nw=Nv(Nb)^5<=D^(C+5A). Equations (C-M5) and (C-M7), with
gamma=(1-B)/4, give A_w>=c D^(1-gamma). Hypothesis U_B with
P=C+5A and delta=(1-B)/4 gives |A_w|<=C' D^(B+delta).
Since 1-gamma-(B+delta)=(1-B)/2>0, these bounds contradict one another
for sufficiently large D. Both thresholds and constants are uniform in
the moving b,v. The contradiction also excludes any sequence of such
returns with D tending to infinity.

## C-M5. What this does and does not remove from Fourier transport

C-M9 extends the conditional unit-frequency exclusion C-F5 to actual
nonunit masks. The new counting estimate is the additional argument;
the frozen C-F5 proof and its stated guard remain unchanged.

The conclusion still concerns polynomially small **element representatives**
b,v. A nonzero additive frequency on the enormous finite CRT group need
not have such a representative in the physical dual normalization. The
inactive prime coordinates and huge CRT modulus in C-F2 remain in the
actual norm-ball transform. Neither C-M9 nor its finite controls bound the
sum of all relevant frequencies, the short-row discrepancy, or a native
2k-th moment. A quantitative signed dual-weight estimate remains open.

The smallest assumption whose failure invalidates C-M9 is U_B. The
elementary C-M1--C-M7 statements remain valid without it.
