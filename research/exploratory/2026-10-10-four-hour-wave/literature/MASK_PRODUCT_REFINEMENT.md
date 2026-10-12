# A sharper elementary error for polynomial ideal masks

Status: proved component deduction from the independently reviewed
prime-ideal count and moving-mask squarefree count. No moment estimate
or zero-free theorem is proved here. Constants depend only on the fixed
Eisenstein field K, unless additional fixed data are explicitly named.

Sources: `arithmetic/MASK_DENSITY_REFINEMENT.md` R-M1–R-M3 and
`arithmetic/MASKED_CRT_NONRETURN.md` C-M1–C-M3. The first reconstructs
the elementary bounds pi_K(y)<<y/log y and
sum[Np<=y](Np)^(-1/2)<<sqrt(y)/log y using rational Chebyshev and
ideal counting. Both proofs were read independently. The source's
weaker bound for the product below is valid; choosing its splitting
point differently strengthens that error term.

## P1. The sharper product bound

For every nonzero integral ideal h put X=log(3Nh)>1 and

    P(h)=product[p|h](1+(Np)^(-1/2)).

Then

    P(h) <= exp(C_K sqrt(X)/log X).                    (P1)

Proof: set Y=max(9,X), and use log(1+t)<=t. The small-prime
contribution, including only primes dividing h, is at most

    sum[Np<=Y](Np)^(-1/2) << sqrt(Y)/log Y.

The number of distinct prime divisors of h with Np>Y is at most
log(Nh)/log Y, because the norm of their product is at most Nh.
Their contribution is consequently at most

    log(Nh)/(sqrt(Y) log Y) <= X/(sqrt(Y) log Y).

For X>=9 both quantities are O(sqrt(X)/log X). For 1<X<9,
the first bound is constant and the second is bounded; sqrt(X)/log X
has a positive lower bound on the actual interval
[log3,9]. Enlarging C_K covers this range. Exponentiation proves P1.
Every prime ideal, including both ideals over a split rational prime,
is counted with its true norm and exactly once.

## P2. Uniform squarefree counting error

Combining P1 with the proved C-M3 gives, uniformly in every nonzero h
and x>=1,

    Q_h(x) = (kappa_K/zeta_K(2)) x
             product[p|h](1+1/Np)^(-1)
       + O_K(sqrt(x) log(2x)
             exp(C_K sqrt(log(3Nh))/log log(3Nh))).     (P2)

Here Q_h includes every squarefree ideal coprime to h; the source's
exact main term and all moving coprimality masks are retained.
The improvement changes its error bound, not its main coefficient.

For Nh<=C_S D^A, with A,S fixed and D sufficiently large, the error
at either fixed positive multiple of D is at most

    D^(1/2) log(2D)
      exp(O_(A,S)(sqrt(log D)/log log D)).              (P3)

To justify the uniformity, t^(1/2)/log t is increasing for t>e^2.
Its maximum over the bounded smaller t is a fixed constant; above
that range it is bounded by its value at
t=A log D+O_S(1). This proves P3 without an h-dependent threshold.

## P3. What is paid by the refinement

The separately reviewed small-prime Euler product gives
product[p|h](1+1/Np)<<log log(3Nh). Thus the main difference between
Q_h(beta D) and Q_h(alpha D), for fixed 0<alpha<beta, is at least
c_(A,S) D/log log(3D). Error P3 is smaller than half this main
difference for sufficiently large D, uniformly in h. Any fixed
nonnegative nonzero smooth W therefore retains

    sum[n squarefree, (n,bS)=1] W(Nn/D)
        >= c_(A,S,W) D/log log(3D),  Nb<=D^A.

This is the same positive-density order as the source R-M8, with a
sharper elementary error budget. Its application to CRT nonreturn
still assumes the uniform polynomial-row input U_B. Neither the
ideal count nor this refinement establishes that analytic input,
controls the complete CRT frequency sum, or pays a generalized
inverse moment.

Validation: complete written proof with the previously reviewed
lattice, Chebyshev, partial-summation and inclusion-exclusion inputs.
No numerical test is presented as a certificate of an infinite
asymptotic statement.
