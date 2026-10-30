# Independent audit of the arithmetic profile compensator

Reviewer: dynamics lane. Date: 30 October 2026.  
Source reviewed: `swarm/arithmetic/progression_profile.md`.  
Exact SHA256: **`1314c3a59a08245b56c032635ed11fde09531129eb18d8f1486522988ed97a31`**.  
Scope: the fixed-k weighted prime asymptotic, divisor switch, Euler-product constants, Mellin compensator, and quantifier claims. No source file was modified.

## Outcome

**No blocking error or hidden uniform-in-growing-u assumption found.** The fixed-scale asymptotic and compensator follow from the stated classical inputs. The report correctly leaves the target-strip Mellin error estimate open. This review makes no claim of global novelty and does not independently reprove the fixed-modulus prime number theorem or Brun–Titchmarsh theorem.

## 1. Fixed-k weighted prime asymptotic

For a fixed positive integer k, expansion of phi(m) gives the inner prime sum

$$I_d(Y)=\sum_{\substack{m\le Y,\ d\mid m\\km+1\ {m prime}}}m\log(km+1).$$

Writing p=km+1, this is exactly

$$I_d(Y)=\frac1k\sum_{\substack{p\le kY+1\\p\equiv1\ (kd)}}(p-1)\log p.$$

For each fixed d, fixed-progression PNT and partial summation give
$I_d(Y)\sim kY^2/(2\varphi(kd))$. There is no missing factor d or k in this normalization.

The two truncation ranges also check:

- For D<d≤sqrt(Y), Brun–Titchmarsh applies to the reduced class 1 modulo kd. Its denominator satisfies log((kY+1)/(kd))≥(1/2)log Y. Bounding the prime weight by Y log(kY+1) therefore gives $I_d(Y)=O_k(Y^2/\varphi(kd))$ uniformly in this range. Multiplication by 1/d and $\varphi(kd)\ge\varphi(k)\varphi(d)$ produce the summable tail asserted in the source.
- For d>sqrt(Y), putting R=floor(Y/d) gives

$$\sum_{\substack{m\le Y\\d\mid m}}m
=\frac{dR(R+1)}2\le\frac{Y^2}{2d}+\frac Y2.$$

After the additional weight 1/d and the elementary log(kY+1) bound, summing this range gives
$O_k(Y^{3/2}\log Y+Y\log^2Y)=o_k(Y^2)$.

The proper-prime-power contribution is separately bounded by $O_k(Y^{3/2}\log^2Y)$ using phi(m)≤m and the elementary count of prime powers. Thus it causes no issue with using a prime-counting version of Brun–Titchmarsh in the main calculation.

The order of limits is legitimate: first Y tends to infinity with D fixed; then the absolutely summable d-tail is removed by sending D to infinity. No PNT uniform in d up to sqrt(Y) is assumed.

## 2. Euler factors and normalization

The coefficient is

$$C(k)=k\sum_{d\ge1}\frac{\mu(d)}{d\varphi(kd)}.$$

For p not dividing k, the squarefree d-factor is $1-1/[p(p-1)]$. For p dividing k, it is $1-1/p^2$, accompanied by the factor p/(p−1) from k/phi(k). Their ratio to the base Artin factor is exactly

$$\frac{p^2-1}{p^2-p-1}.$$

Consequently

$$\mathcal C(s)=A\zeta(s)\prod_p\left(1+\frac{p^{1-s}}{p^2-p-1}\right)$$

has the stated normalization. The auxiliary factors differ from 1 by $O(p^{-1-\sigma})$, uniformly on compact subsets of Re s>0, so the asserted absolute local convergence is valid. Possible zeros of this product are harmless because the construction does not invert it.

Both claimed constants can be checked locally:

$$\left(1-\frac1{p(p-1)}\right)
 \left(1+\frac1{p^2-p-1}\right)=1,$$

and

$$\left(1-\frac1{p(p-1)}\right)
 (1-p^{-2})^{-1}
 \left(1+\frac1{p(p^2-p-1)}\right)=1.$$

Absolute convergence permits multiplying these identities. They give Res at 1 equal to 1 and C(2)=1 respectively.

## 3. Divisor switch and fixed-scale limit

The full divisor weight excluding q=1 is n−2. The omitted q>Q part is counted exactly once by n=kq+1. The strict outer inequality k<(x−1)/Q may include an empty inner interval but excludes no admissible pair.

For x=uQ with u fixed, only finitely many k<u survive. Applying the fixed-k weighted-prime asymptotic to the difference of the endpoints Q and (uQ−1)/k gives the displayed profile. If u is an integer, the prospective k=u contribution is zero in the limit and is correctly excluded by k<u. Floor and boundary terms are negligible after division by Q(Q−1).

The small-x identity was checked separately, including the n−2 weight and fractional-part term. It is consistent at x=2, at nonintegral x, and at x=Q+1; it does not insert a progression main term before the first possible von Mangoldt contribution.

## 4. Compact-u uniformity is valid and properly limited

For every Q, u↦Psi_Q(uQ)/Q is nondecreasing. Its fixed-u limit P is continuous: the newly activated term at an integer k has the factor u²/k²−1 and vanishes there. Pointwise convergence of monotone functions to a continuous limit is uniform on each fixed compact u-interval by a finite-grid sandwich argument. Monotonicity in Q is not required.

The resulting o(Q) error is therefore uniform on aQ≤x≤bQ for fixed positive a and finite b. Substitution x=Qu yields the asserted o(Q^(1−Re s)) bound for the Mellin integral on that block, uniformly for s in a fixed compact set. This proves no statement with b growing with Q and supplies no control of the unbounded endpoint ranges. The source explicitly preserves those restrictions.

## 5. Growth and Mellin transform

Let $S(v)=\sum_{k\le v}C(k)$. The nonnegative convolution expansion and AG(1)=1 give S(v)≤v. A useful equivalent expression for the displayed profile is

$$P(u)=u^2\int_u^\infty S(v)v^{-3}\,dv.$$

It follows directly by partial summation, with the atomic endpoint treated by S(u−). In particular P(u)≤u, agreeing with the source's growth claim. The same convolution expansion and dominated convergence give S(v)∼v; no unproved Tauberian input is hidden here.

Since $P'(u)=u\sum_{k\ge u}C(k)/k^2$ away from integers and P itself is continuous, Tonelli gives

$$\int_0^\infty u^{-s}\,dP(u)
=\sum_k\frac{C(k)}{k^2}\int_0^k u^{1-s}\,du
=\frac{\mathcal C(s)}{2-s}$$

in exactly the initial strip 1<Re s<2.

For x<1, the scaled profile QP(x/Q) equals x²/(2Q), because Q≥2. Removing that lower interval contributes $Q^{-1}/(2-s)$, which verifies both the subtraction and sign in

$$C_Q^*(s)=\frac{Q^{1-s}\mathcal C(s)-Q^{-1}}{2-s}.$$

The apparent pole at s=2 is removable by C(2)=1. The transform from x=1 to infinity is holomorphic throughout Re s>1 by P(u)≤u, so continuation through 2 is justified. Its residue at 1 is +1; elsewhere in Re s>0 the explicit expression is holomorphic. In particular, there is no compensating pole at a nontrivial zeta zero, and adding it to T_Q preserves the positive zero residues.

Finally, M_Q*(1)=0, so integration by parts introduces no missing boundary constant in the signed Mellin source. The error integral is established only for Re s>1. The report does not infer its convergence or smallness in the target strip from the fixed-scale limit.

## Decision

The reviewed hash is mathematically consistent at the stated scope. The explicit removal of the first-transition drift is a valid constructive refinement of the original detector. Its quantitative signed error, particularly over growing x/Q and on contours to the left of 1, remains unpaid. No source correction was requested by this review.
