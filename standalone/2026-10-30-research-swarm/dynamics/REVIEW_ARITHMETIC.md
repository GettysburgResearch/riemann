# Independent review of the arithmetic lane

Reviewer: dynamics lane. Date: 30 October 2026.  
Reviewed objects: `swarm/arithmetic/report.md` and `replay.py` in the shared swarm working tree. This review is of the mathematical identities and stated scope, not a proof of the proposed contour upper bound.

## Outcome

**No blocking mathematical error found in Propositions A–D, the infinite identity in its stated convergence domain, the finite complement, or the contour/conductor accounting.** Two improvements were sent to the author: an explicit classical cyclotomic identification and a stronger elementary bound in the safe half-plane. The latter is derived below.

## Checks of the load-bearing claims

1. **Negative prime classes.** Conjugation-symmetric exponents make the character polynomial real. Its group mean is exactly the principal exponent, while Parseval gives the stated energy. Cauchy–Schwarz then gives the claimed lower bound on the fraction of negative classes. Translating it into a prime density requires the separately stated prime number theorem in arithmetic progressions; the finite inequality does not.
2. **Positive mixtures.** Each real nonprincipal Dirichlet value at 1 is positive, and each conjugate pair contributes a positive squared modulus, including imprimitive finite Euler corrections. Thus positive weights cannot cancel the largest principal pole at 1. After excluding positive principal exponents, the averaged prime coefficient has negative mean whenever one term has a negative principal exponent. The example involving zeta plus its reciprocal is correctly excluded by the pole at 1.
3. **Sparse support and uniqueness.** For a prime of order f modulo q, the character-value multiset contains each f-th root h/f times. This yields the exact local polynomial. Each supported local monomial is 1 modulo q, so the multiplicative support and initial gap follow. Fourier inversion proves the stated uniqueness inside the finite monomial class.
4. **Pole preservation.** At a nontrivial zeta zero, the principal finite Euler corrections are nonzero because their zeros have real part zero. Nonprincipal L-functions are holomorphic there. Their zeros can only increase the reciprocal-product pole order. The logarithmic derivative's residue is the sum of the zero multiplicities, with the correct positive sign.
5. **Shifted-zeta identity.** Summing q with absolute convergence for real part greater than 2 gives the totient weight n−1. Removing q=1 contributes the second copy of minus zeta-prime over zeta. The signs are correct. At rho, the shifted argument rho−1 is not another zeta zero, so the negative residue on the analytically continued right side is correctly identified as a failure of convergence of the positive-residue infinite sum, rather than a contradiction.
6. **Finite complement.** The remaining divisor weight is nonnegative and vanishes through n≤Q+1. Adding it to the continued shifted-zeta expression gives exactly the finite sum. Its meromorphic continuation does not preserve the positive Dirichlet-series argument outside convergence.
7. **Contour and conductor counts.** The domains exclude 1 and the line of finite-Euler-factor zeros. Thus every counted residue is nonnegative. A primitive conductor d≥2 occurs in exactly floor(Q/d) of the moduli, while the principal conductor occurs Q−1 times. The exact principal coefficient is 1 after normalization. A summable primitive high-conductor tail cannot remove it. The proposed liminf less than 1 is indeed sufficient, but remains the principal unpaid analytic claim.

## Stronger safe-region bound

For fixed real sigma>1, uniformly in the ordinate, the congruence formula and the elementary bound Lambda(n)≤log n give

$$
|D_q(s)|\le q\sum_{m\ge1}\log(mq+1)(mq+1)^{-\sigma}.
$$

Since q≥2 and m≥1, mq+1≤(3/2)mq. Therefore

$$
|D_q(s)|\le q^{1-\sigma}
 \left[\zeta(\sigma)\log q-\zeta'(\sigma)
       +\log(3/2)\zeta(\sigma)\right].
$$

Averaging over q yields

$$
T_Q(s)=
\begin{cases}
O_\sigma(Q^{1-\sigma}\log Q),&1<\sigma<2,\\
O(\log^2 Q/Q),&\sigma=2,\\
O_\sigma(1/Q),&\sigma>2.
\end{cases}
$$

Consequently the normalized detector tends to zero uniformly on every closed half-plane Re s≥1+epsilon, with constants depending on epsilon. This strengthens the initial report's greater-than-2 safe region. It supplies no estimate inside the target strip and does not justify continuation of the infinite modulus sum.

## Classical identification to make explicit

The product A_q has exactly the good-prime Euler factors of the reciprocal Dedekind zeta function of the cyclotomic field Q(zeta_q), with ramified factors omitted. Its degree and conductor growth, and the retention of a zeta factor, fit that classical interpretation. The author was advised to state it, while retaining the new finite-mixture, sparse-support, and normalized-contour bookkeeping as the contribution of this pass. No worldwide novelty claim is supported by the unavailable public-web search.

## Reproduction

The reviewer inspected `replay.py`: it uses only integer arithmetic and standard-library operations, with synthetic zero multiplicities correctly labeled as such. An independent execution passed: nine Euler-factor moduli, 78,125 Walsh/Fourier examples, 2,500 finite complement checks, and 79 conductor-counting checks. The totient identity was checked through 500. These checks authenticate the finite algebra only, not any zero-free conclusion or analytic continuation estimate.
