# Polynomial moving masks retain a logarithmic positive density

Status: **Proposed elementary quantitative refinement R-M1--R-M4,
pending independent review.** The entire result is an ideal counting
statement. Only its application to CRT nonreturn imports the explicit
conditional hypothesis U_B from `MASKED_CRT_NONRETURN.md`.

Scope: the same fixed Eisenstein field K, nonzero integral ideal h, fixed
bad-prime set S, and fixed nonnegative nonzero smooth W. All constants in
the ideal product estimates below depend only on K. All logarithms are
natural; log log(3Nh)>0 even for Nh=1. Statements about sufficiently large
D have uniform thresholds in the moving b.

Exact dependencies: the fully proved uniform squarefree mask count C-M3
in `MASKED_CRT_NONRETURN.md`, and the elementary prime/ideal estimates
derived below. No prime-ideal theorem or assumed Mertens product asymptotic
is used. These are classical elementary product bounds, reconstructed as
a concrete source adapter, not claimed as a new prime-counting theorem.

What was actually run: analytic derivation only; no numerical computation
is needed for these inequalities. The existing masked source checker tests
the finite literal character identity and independently reconstructs its
ideal count, not the infinite estimates here.

## R-M1. Elementary prime-ideal bounds

Write theta_Q(y)=sum_(p<=y)log p over rational primes. Every rational
prime n<p<=2n divides the integer binomial(2n,n), so

    theta_Q(2n)-theta_Q(n)<=log binomial(2n,n)<=2n log2.

Summing on powers of two and then enlarging y to the next power gives
theta_Q(y)=O(y), uniformly y>=2. In the Eisenstein field a split rational
prime contributes two prime ideals of norm p, an inert prime contributes
one of norm p^2, and the ramified prime is fixed. Consequently

    theta_K(y):=sum_(Np<=y)log Np=O_K(y).                 (R-M1)

Prime ideals with Np>sqrt(y) each cost at least (log y)/2 in theta_K.
The smaller ones number at most I_K(sqrt(y))=O_K(sqrt(y)). Thus

    pi_K(y):=#{p:Np<=y}=O_K(y/log y), y>=3.              (R-M2)

Partial summation of theta_K gives

    sum_(Np<=y)log(Np)/Np=O_K(log y).

Also

    sum_(Np<=y)(Np)^(-1/2)=O_K(sqrt(y)/log y), y>=3.     (R-M3)

For (R-M3), the primes of norm at most sqrt(y) contribute at most
pi_K(sqrt(y))=O_K(sqrt(y)/log y), since each weight is at most one.
On (sqrt(y),y], partial summation of pi_K(t)=O_K(t/log t), with
log t>=(log y)/2, bounds the remaining contribution by
O_K(sqrt(y)/log y). Adjusting constants covers the fixed small range.

## R-M2. A small-prime Euler product bound

For L>=3 put sigma=1+1/log L. The logarithmic ratio satisfies

    log product_(Np<=L) [(1-(Np)^(-sigma))/(1-(Np)^(-1))]
      <=sum_(Np<=L) [1-(Np)^(-(sigma-1))]/(Np-1)
      <=(sigma-1)sum_(Np<=L)log(Np)/(Np-1)=O_K(1).       (R-M4)

Here log(1+t)<=t, 1-e^(-t)<=t for t>=0, and
1/(Np-1)<=2/Np give every inequality explicitly. By the absolutely
convergent Euler product at sigma>1,

    product_(Np<=L)(1-(Np)^(-1))^(-1)
      <=C_K zeta_K(sigma)=O_K(log L).                   (R-M5)

Indeed zeta_K(sigma)=sigma integral_1^infinity I_K(t)t^(-sigma-1)dt
and I_K(t)=O_K(t) for t>=1 give zeta_K(sigma)=O_K(1/(sigma-1))
on this bounded sigma range. Thus (R-M5) does not need a prime-ideal
theorem or a prime-product asymptotic.

## R-M3. Two uniform products for an arbitrary ideal mask

Set H=3Nh. We claim

    product_(p|h)(1+1/Np) <=C_K log log H,

    product_(p|h)(1+(Np)^(-1/2))
      <=exp(C_K log H/log log H).                       (R-M6)

First choose L=max(9,log H). The primes dividing h with Np<=L cost
at most the entire product in (R-M5), hence at most C_K log L.
The number of primes dividing h with Np>L is at most log(Nh)/log L,
since Nrad(h)<=Nh. Their logarithmic contribution is at most

    sum_(p|h,Np>L)1/Np<=log(Nh)/(L log L)=O(1).

Therefore the first product is O_K(log L)=O_K(log log H).
The latter equality adjusts a constant for bounded H; log log H has the
positive lower bound log log3 there.

For the second product choose L=max(9,(log H)^2). By (R-M3),
the small primes have logarithmic contribution at most

    sum_(Np<=L)(Np)^(-1/2)
        =O_K(sqrt(L)/log L)=O_K(log H/log log H).

The large primes dividing h have logarithmic contribution at most

    log(Nh)/(sqrt(L) log L)=O(1).

Enlarge the constant for bounded H. Exponentiation proves the second
claim. Every prime ideal, including both ideals over a split rational
prime, occurs with its actual norm and multiplicity one in these products.

## R-M4. An explicit logarithmic-order positive mass

Combining (R-M6) with the already proved C-M3 gives uniformly for all
nonzero h and x>=1,

    Q_h(x)=(kappa_K/zeta_K(2))x product_(p|h)(1+1/Np)^(-1)
      +O_K(sqrt(x)log(2x)
             exp(C_K log(3Nh)/log log(3Nh))).             (R-M7)

Fix A>0, S, and nonnegative nonzero W in C_c^infinity((0,infinity)).
Then there is c_(A,S,W)>0 such that, uniformly in nonzero b with
Nb<=D^A, for all sufficiently large D,

    sum_(n squarefree,(n,bS)=1)W(Nn/D)
         >=c_(A,S,W) D/log log(3D).                     (R-M8)

Choose a fixed interval [alpha,beta] and w_0>0 with W>=w_0 on it,
as in C-M2. For h=(b)product(S), Nh<=C_S D^A. The main difference
Q_h(beta D)-Q_h(alpha D) is at least c_(A,S)D/log log(3D), by the
first product estimate. Its error is at most

    D^(1/2)log(2D) exp(O_(A,S)(log D/log log D))
      =D^(1/2+o(1)).

To justify the uniform little-o: log(3Nh)<=A log D+O_S(1); the function
t/log t is increasing for t>e, so its maximum over those h is
O_(A,S)(log D/log log D). This error is eventually smaller than half
the displayed main term. Multiplication by w_0 proves (R-M8).

Consequently in C-M9's exact masked identity, any hypothetical polynomial
nonzero return would give A_(v b^5)(D;W)>=c D/log log(3D). Under its
explicit U_B hypothesis, the uniform upper bound D^(B+delta), with
delta=(1-B)/2, contradicts this for every B<1. This is a quantitative
strengthening of the same conditional nonreturn conclusion. It still
provides no new analytic input or short-row moment estimate.
