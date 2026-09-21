# RSC26 L-family adapter: unchanged coefficients, correct central energy

**Proposed component proof for independent review; no GRH conclusion.** This continues #738's explicitly declared CM cubic-twist reference extension. It preserves STC26's inert-factor removal and central-singularity warning. Here NO Euler factors are removed and no auxiliary sign family is substituted.

## 1. An entire residual bound at the arithmetic center

For an elliptic reciprocal source nu in arithmetic normalization, use

    E_1(nu;X)=integral_1^X |sum_(n<=x)nu(n)|^2 dx/x^3.

On integer cells the weights are

    w_1(k)=1/(2k^2)-1/[2(k+1)^2].

This is not the zeta dx/x^2 energy. Assume the standard elliptic Euler factors: at a good prime p the inverse factor is 1-a_p T+pT^2 with |a_p|<=2sqrt(p); the usual bad factors have degree at most one and coefficient bounded by sqrt(p). Multiplicativity then gives

    |nu(n)|^2<=n tau(n)^2.                               (1)

At exponent one, the normalized square is <=4=tau(p)^2; at exponent two it is <=1<=tau(p^2)^2; higher good exponents vanish. Multiply the local inequalities. Bad factors satisfy the same ceiling. This is an imported Hasse/Euler input, not proved by the finite fixture.

Let A(k)=sum_(n<=k)nu(n), and let Pi_1 subtract the w_1-weighted mean on each q=1 root cell. Then

    ||(I-Pi_1)A||_(w_1)^2<=36 H_N^4,   N=X-1.           (2)

The estimate remains true under integer-resolution refinements and for intervals clipped inside [1,N].

Proof. For a cell [s,t] of length ell and weight W, pairwise variance and Cauchy give

    V_(w_1)(A)<=ell W/4 sum_(r=s+1)^t |nu(r)|^2.

Indeed the crossing weight for a fixed increment is W_left W_right/W<=W/4, and a difference uses at most ell increments. Here W<=ell/s^3 and ell^2<=9s for root cells. Also r<=4s. Applying (1) bounds each increment coefficient by

    [ell^2 r/(4s^3)]tau(r)^2 <=36 tau(r)^2/r.

Sum over disjoint cell interiors and use tau^2<=tau_4, sum_(r<=N)tau_4(r)/r<=H_N^4. QED.

The bound controls ALL within-cell signed interactions together. It is deliberately conservative. There is no conclusion about the coarse part of E_1 and no assumption that its size follows from the native zeta calculation.

## 2. Endpoint means with no altered central singularity

Define R_2(n)=sum_(r<=n)nu(r)/r^2. Exact summation by parts gives

    sum_(k=s)^t A(k)w_1(k)
      =1/2 [R_2(t)-R_2(s-1)+A(s-1)/s^2-A(t)/(t+1)^2].   (3)

Thus endpoint data plus (2) bound the complete finite energy. The proof changes only an observation-space projection; it does NOT change nu, L(s), its central rank, or its Euler factors. No half-order singularity is introduced by this operation.

However the coarse statistic is NOT itself a completed L-function. One must not run the old Pick/central-deflation test on it as if it had the functional equation and zeros of the original completed function. The previous rank-one assertions remain imported from the Sylvester paper and are not re-proved here.

Equation (1) of PROOF.md always relates ordinary and reciprocal cumulatives in the zeta weights, as finite algebra. That fact alone does NOT make those weights the correct elliptic detector. This adapter proves (2)-(3) in the actual arithmetic-center-one norm instead.

## 3. Exact finite Euler fixture and limits

algebra.py directly counts E_17: y^2=x^3+17^2/4 over the fifteen good primes

    5,7,11,13,19,23,29,31,37,41,43,47,53,59,61.

It multiplies their inverse Euler polynomials through N=4095. This is a FINITE Euler model; all omitted good and bad factors are unmodeled, so the resulting array is not the complete E_17 reciprocal sequence.

Every coefficient satisfies the squared bound (1). The arithmetic-energy decomposition gives descriptive values

    full energy       0.8885573038367806,
    coarse energy     0.7228034614833648,
    residual energy   0.16575384235341575.

All finite arithmetic is integer/rational-directed, not a floating sign test. There are 63 root cells. The generic upper bound in (2) is about 225350.70 and is NOT advertised as a sharp numerical estimate. No L-value, global rank, zero, height, CM integral, or unbounded family-energy bound is computed.

References: prior STC26/PET26/DCN26 family notes for normalization and source conventions; Hasse's theorem as stated in Andrew Sutherland's MIT 18.783 Lecture 7 (2023), Theorem 7.3. The cube-sum rank-one family motivation remains Burungale--Tian, arXiv:2609.14893v2, not a theorem used to prove (2).
