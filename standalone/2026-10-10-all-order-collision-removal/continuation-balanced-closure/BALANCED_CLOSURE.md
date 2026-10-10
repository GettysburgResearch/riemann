# Balanced-only closure by a small inverse kernel

**Status:** proposed complete component proofs. This removes a hypothesis from the preceding reduction; it does not prove an arithmetic higher moment, a new zero-free boundary, or RH. No independent review or Lean verification has been performed.

**Frozen predecessor:** PR #916, first publication `dabd6da99fb92eead7c99f941331ed9cbd2ec4ad`. All eight predecessor files are preserved. The exact inverse identity is PROOF.md Theorem 3.1; it is restated below. The result here does not use either imported quasi-RH theorem or the sibling large-sieve estimates.

## 1. What changes

The preceding direct transfer asked for a mean square of a pairwise-coprime polynomial at every rectangle of factor lengths. Here a *balanced-only* mean square suffices, after allowing an arbitrarily small exponent loss and making one fixed finite-prime exclusion. The unequal-length terms are absorbed using Holder and a genuinely small inverse-kernel tail.

This is not a claim that balanced estimates directly control each unequal-length summand. Instead we compare finite scale envelopes, which are finite without any conjectural bound, and absorb a coefficient less than one. The same physical row set is used at every scale.

## 2. Fixed source and a quantitative smallness lemma

Fix K=Q(sqrt(-3)), k>=2, W in C_c^infinity((0,infinity)), supported in [a,b], and a finite-order character nu. For a finite set S containing the conventional primes over 6 and the conductor of nu, put

    theta_u(n)=nu(n) chi_n(u),  (n,S)=1,
    A_u(X)=sum_(n,S)=1 mu(n) theta_u(n) W(Nn/X).

Retain all zero values of the sextic character. Define

\[
 B_{k,u}(X_1,\ldots,X_k)=
 \sum_{\substack{n_i\ \mathrm{squarefree},\ (n_i,n_j)=1\ (i\ne j)\\
                 (\prod_i n_i,S)=1}}
 \mu(\prod_i n_i)\theta_u(\prod_i n_i)
 \prod_i W(Nn_i/X_i).
\tag{2.1}
\]

Only complete multiplicativity and |theta_u(n)|<=1 are needed in the norm proof. The row set can be any finite set with any nonnegative measure.

Let

\[
 Q_k(\mathbf z)=\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
 =\sum_{\mathbf e\ge0}b_k(\mathbf e)\mathbf z^{\mathbf e},
 \qquad
 b_k(0)=1,\quad b_k(\mathbf e)=1-|\mathrm{supp}(\mathbf e)|\ (\mathbf e\ne0).
\tag{2.2}
\]

The multiplicative ideal-tuple coefficient is

    D_k(d_1,...,d_k)=product_(p not in S) b_k(v_p(d_1),...,v_p(d_k)).

Fix 0<delta<=1/2 and sigma=1/2+delta. Define the nonidentity weighted mass

\[
 q_{k,S}(\sigma)=
 \sum_{\mathbf d\ne(1,\ldots,1)}
 \frac{|D_k(\mathbf d)|}{(\prod_i Nd_i)^\sigma}.
\tag{2.3}
\]

### Lemma 2.1. A fixed cutoff makes q at most 1/3

It suffices to include in S every prime ideal of norm at most

\[
 P\ge\max\left\{(2k)^3,
       \left(\frac{24k^2}{\delta}\right)^{1/(2\delta)}\right\}.
\tag{2.4}
\]

Then the series (2.3) converges and q<=1/3. This cutoff is deliberately conservative, independent of D, H, the row, and W. It may depend on k and the requested exponent loss.

**Proof.** At one prime write t=(Np)^(-sigma). Summing absolute coefficients gives

\[
 F_k^-(t)=2-\frac{1-kt}{(1-t)^k}.
\]

For a nonempty support of size s, |b_k|=s-1<=binom(s,2). Therefore, when kt<=1/2,

\[
 0\le F_k^-(t)-1
 \le {k\choose2}\frac{t^2}{(1-t)^k}
 \le k(k-1)t^2\le k^2t^2.
\tag{2.5}
\]

The middle inequality uses (1-t)^k>=1-kt>=1/2. The cutoff (2.4) ensures kt<=1/2.

There are at most 3x nonzero integral ideals of norm at most x, for x>=1. Indeed each ideal has six generators in the Eisenstein lattice, and N(r+s omega)>= (r^2+s^2)/2 bounds the nonzero lattice count by (2 sqrt(2x)+1)^2-1 <18x. Dyadic summation consequently gives

\[
 \sum_{Np>P}(Np)^{-1-2\delta}
 \le \frac{6P^{-2\delta}}{1-2^{-2\delta}}
 \le \frac{6}{\delta}P^{-2\delta}.
\tag{2.6}
\]

The last inequality follows from concavity of 1-2^(-2delta) on [0,1/2], which puts it above the chord delta. Equations (2.4)-(2.6) imply that the sum T of all local nonconstant absolute masses is at most 1/4. For any finite set of nonnegative numbers t_p of sum at most T<1, the product of (1+t_p) is at most sum_(j>=0) T^j=1/(1-T). Passing to the convergent product gives

    1+q = product_(p not in S) F_k^-((Np)^(-sigma)) <= 4/3.

This proves the claim, without a distribution-of-primes theorem. QED.

## 3. The inverse identity and finite-envelope absorption

Coefficientwise multiplication of (2.2) gives, for every positive scale vector,

\[
 B_{k,u}(\mathbf X)=
 \sum_{\mathbf d} D_k(\mathbf d)\theta_u(\prod_i d_i)
 \prod_i A_u(X_i/Nd_i).
\tag{3.1}
\]

This is a finite identity on each horizon, because a nonzero summand has Nd_i<=bX_i. It is valid at theta_u(p)=0: there is no division by a character value. No extra coprimality exclusion is introduced.

Fix a finite row measure and D>=max(2,1/b). Define

\[
 M_\sigma(D)=\sup_{1/b\le X\le D}
 \frac{\sum_u|A_u(X)|^{2k}}{X^{2k\sigma}},
\tag{3.2}
\]
\[
 B_\sigma(D)=\sup_{1/b\le X\le D}
 \frac{\sum_u|B_{k,u}(X,\ldots,X)|^2}{X^{2k\sigma}},
\tag{3.3}
\]
\[
 C_\sigma(D)=\sup_{1/b\le X_i\le D}
 \frac{\sum_u|B_{k,u}(\mathbf X)|^2}{\prod_iX_i^{2\sigma}}.
\tag{3.4}
\]

All three quantities are finite: the original row set and the coefficient supports below bD are finite, and the scales lie in a compact interval. This observation, not a desired moment estimate, justifies absorption.

### Theorem 3.1. Balanced closure at every fixed order

With q=q_(k,S)(sigma)<1,

\[
 \boxed{(1-q)^2 M_\sigma(D)\le B_\sigma(D)
        \le C_\sigma(D)\le(1+q)^2M_\sigma(D).}
\tag{3.5}
\]

In particular the cutoff of Lemma 2.1 gives

\[
 M_\sigma(D)\le\frac94 B_\sigma(D),
 \qquad C_\sigma(D)\le4B_\sigma(D).
\tag{3.6}
\]

The constants are independent of D and of the finite row measure. The quantities still depend on the actual arithmetic source; (3.5) does not assert that any of them is small.

**Proof.** Holder at unequal lengths Y_i gives

\[
 \left\|\prod_i A_\cdot(Y_i)\right\|_2
 \le\prod_i\|A_\cdot(Y_i)\|_{2k}
 \le M_\sigma(D)^{1/2}\prod_iY_i^\sigma.
\tag{3.7}
\]

Terms with some Y_i<1/b vanish. Multiplication by theta_u(prod d_i) is a contraction on row L2, so (3.1), Minkowski, and (3.7) prove the last inequality in (3.5). The middle inequality is just inclusion of the balanced scales among the rectangles.

For the first inequality, isolate the d=(1,...,1) term in (3.1) at X_1=...=X_k=X. It is A_u(X)^k, with coefficient exactly one. Move every other term to the other side, apply (3.7), and divide by X^(k sigma). This gives

\[
 \frac{\|A_\cdot(X)^k\|_2}{X^{k\sigma}}
 \le B_\sigma(D)^{1/2}+qM_\sigma(D)^{1/2}.
\]

Taking the supremum over X and subtracting the last term yields

    (1-q) M_sigma(D)^(1/2) <= B_sigma(D)^(1/2).

The quantity being subtracted is finite. Squaring proves (3.5), and q<=1/3 proves (3.6). QED.

**Why the predecessor's rectangular qualification is no longer an independent premise:** its direct square-root-weight reconstruction estimated every shortened rectangle separately. Here the mixed products are bounded by the same unknown diagonal moment envelope, and their *entire* coefficient mass is less than one at sigma>1/2. This is a new absorption argument, not a claim that the old critical-weight argument already supplied it.

## 4. Reinsert the fixed excluded primes

Let S0 be the desired original finite exclusion and S contain S0 plus the cutoff primes. Let m be the squarefree product of primes in S minus S0. Exact squarefree separation gives

\[
 A_u^{S0}(X)=\sum_{d\mid m}\mu(d)\nu(d)\chi_d(u)A_u^S(X/Nd).
\tag{4.1}
\]

This identity retains zeros at primes dividing the row. Minkowski in L^(2k) shows that a sigma-weighted envelope for A^S transfers to A^(S0) with factor

\[
 \sum_{d\mid m}(Nd)^{-\sigma}
 =\prod_{p\mid m}(1+(Np)^{-\sigma}).
\tag{4.2}
\]

It is a fixed finite constant, independent of D and the rows. It can be very large. Thus an auxiliary S depending on the requested epsilon does not prevent a final moment theorem for the original S0, with the usual epsilon-dependent constant. We do not assume a bound uniform in growing cutoffs.

### Theorem 4.1. A balanced-only sufficient moment theorem

Fix h>0 and lambda>=0. Suppose that for every fixed finite S containing S0 and every epsilon1>0,

\[
 \sum_{0<Nu\le D^h}|B_{k,u}^S(X,\ldots,X)|^2
 \ll_{k,h,\lambda,\nu,S,W,\epsilon_1}
 D^h X^k D^{\lambda+\epsilon_1}
\tag{4.3}
\]

for all D>=2 and all 1/b<=X<=D. Then, for every epsilon>0,

\[
 \sum_{0<Nu\le D^h}|A_u^{S0}(D)|^{2k}
 \ll_{k,h,\lambda,\nu,S0,W,\epsilon}
 D^h D^{k+\lambda+\epsilon}.
\tag{4.4}
\]

It is enough to have (4.3) for the fixed cutoffs selected by Lemma 2.1, rather than every finite S. There is no moving c or independently assumed rectangle estimate.

**Proof.** It suffices to consider 0<epsilon<=1. Set delta=epsilon/(4k), epsilon1=epsilon/2, and choose S once using Lemma 2.1. For the fixed physical row set 0<Nu<=D^h, (4.3) gives

    B_sigma(D) << D^h D^(lambda+epsilon/2),

since X^(-2k delta) is bounded on X>=1/b. Theorem 3.1 gives the same bound for M_sigma(D). Apply (4.1)-(4.2), then raise the L^(2k) norm estimate to the 2k-th power. The top-scale exponent is

    lambda+epsilon/2+2k sigma = lambda+k+epsilon.

Every constant depends only on fixed data and epsilon, not on D or a moving prime. QED.

**Unchanged row-range requirement:** the rows in (4.3) extend to D^h even when X<D. A theorem only on the curve H=X^h is not asserted to imply (4.3). No rowwise selected height or moving-conductor uniformity is supplied by this lemma.

## 5. The predecessor's moving-c condition follows as well

Let B_(k,c,u) include the additional exclusion (prod_i n_i,c)=1. Its exact finite-horizon deletion kernel has local factor (1-sum z_i)^(-1) at p dividing c outside S. The sigma-weighted mass is

\[
 V_c(\sigma)=\prod_{p\mid c,p\notin S}(1-k(Np)^{-\sigma})^{-1}.
\tag{5.1}
\]

Minkowski and (3.6) therefore give, uniformly for 1/b<=X_i<=D,

\[
 \sum_u |B_{k,c,u}(\mathbf X)|^2
 \le4 V_c(\sigma)^2 B_\sigma(D)\prod_iX_i^{2\sigma}.
\tag{5.2}
\]

For every eta>0, V_c(sigma) <<_(k,S,sigma,eta) (Nc)^eta. To see this, use -log(1-t)<=2t at t<=1/2. For sufficiently large Np, 2k(Np)^(-sigma)<=eta log Np. The finitely many other primes contribute one constant, and only their presence, not their valuation in c, matters. This proves the claimed uniform bound.

For k=2, (5.2) recovers the uniform moving-exclusion statement needed in PR #910 from (4.3), with an arbitrarily small power loss when Nc is polynomially bounded in D. Crucially, it also derives the needed rectangles rather than assuming them. The new arithmetic target can therefore start with c=1 and equal factor lengths, with the fixed-cutoff and full-row quantifiers above.

## 6. Limits of the advance

At sigma=1/2, the absolute inverse kernel has local pair mass binom(k,2)/(Np); its full mass diverges for every finite S. The logarithmic critical-weight theorem in the predecessor is unchanged. Our constants and cutoff are not uniform as delta tends to zero. Arbitrarily small *fixed* delta is enough for the conditional zero-free deduction, but not an effective growing-order theorem.

The actual balanced mean square (4.3) remains unproved. The Liouville-phase countermodel in the predecessor satisfies all these algebraic identities and norm comparisons while violating diagonal-size moments. No independence of genuine sextic rows follows from the contraction.

As a numerical-strength comparison only, the all-row sieve stated in sibling PR #913 gives, for a balanced squarefree product column of length X^k, the bound

    D^epsilon [H X^k + H^(2/3) X^(5k/3) + H^(1/6) X^(2k)].

At X=D, H=D^h, its excess exponent is max(0,(2k-h)/3,k-5h/6). At k=2,h=1 this is 7/6, whereas improving 7/8 by the present extraction needs a defect strictly less than 2/3. This comparison is conditional on that sibling's stated sieve, not a new audit of its proof. Balanced closure eliminates an unnecessary analytic hypothesis; it does not erase the long-column obstruction.
