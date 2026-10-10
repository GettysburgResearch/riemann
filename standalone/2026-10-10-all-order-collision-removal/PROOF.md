# All-order removal of prime collisions

**Status:** new proposed component proofs, not independently reviewed or Lean-checked. No new fourth/sixth moment, zero-free half-plane, or RH proof is claimed.

**Scope:** exact identities, unconditional comparisons between finite row norms, and the precise logarithmic cost of the comparison for every fixed order. The arithmetic cancellation estimate to which these comparisons reduce the problem remains open.

**Source:** extends the fixed-source definitions and fourth-moment gcd reduction in PR #910, frozen at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`. It changes none of that packet. The proofs below do not assume the September 30 or October 5 quasi-RH theorems.

## 1. Exact source and the remaining target

Let K=Q(sqrt(-3)), with its usual ideal norm N and ideal Möbius function mu. Fix an integer k>=2, a finite-order Hecke character nu, and a finite set S of prime ideals containing the conductor and the conventional primes over 6. We may and do enlarge S to include every prime of norm at most (2k)^3. This enlargement is fixed before any scale or row is varied. Deleted Euler factors are nonzero in Re(s)>0, so this is harmless for a subsequent zero-free deduction, not an assertion that their deletion is harmless for every intermediate estimate without proof.

For every nonzero Eisenstein row u, retain the original zero-extended sextic symbols and write

    theta_u(n) = nu(n) chi_n(u),       (n,S)=1.

The only properties used in Sections 2–7 are complete multiplicativity in n and |theta_u(n)|<=1. In particular, a prime dividing u remains zero even when its exponent is divisible by six. No equidistribution of these phases is assumed.

For fixed W_i in C_c^infinity((0,infinity)), with supports in [a_i,b_i], define

\[
 A_{i,u}(X_i)=\sum_{(n,S)=1}\mu(n)\theta_u(n)W_i(Nn/X_i).
\tag{1.1}
\]

Define a **collision-free polynomial with the same fixed S**:

\[
 B_{k,u}(\mathbf X)=
 \sum_{\substack{n_1,\ldots,n_k\ {\rm squarefree}\\
                  (n_i,n_j)=1\ (i\ne j)\\(\prod_i n_i,S)=1}}
 \mu(\prod_i n_i)\theta_u(\prod_i n_i)
 \prod_iW_i(Nn_i/X_i).
\tag{1.2}
\]

The adjective refers only to prime overlap among the k factors. All divisor allocations with the indicated weights are retained. It does not mean that product-column correlations disappear when a row norm is expanded.

The main conclusion is that the product of the k polynomials (1.1) can be reconstructed from **fixed-S** expressions (1.2) at independently shortened scales, at a logarithmic norm cost. Thus moving coprimality exclusions do not have to be a separate hypothesis in an all-order analytic theorem. The price is that the collision-free estimate must cover a full rectangle of factor scales, not only equal scales.

## 2. A positive local kernel

Introduce k formal variables z_1,...,z_k. Set

\[
 R_k(\mathbf z)=\frac{\prod_{i=1}^k(1-z_i)}{1-\sum_{i=1}^kz_i}
              =\sum_{\mathbf a\ge0}c_k(\mathbf a)\mathbf z^{\mathbf a}.
\tag{2.1}
\]

### Theorem 2.1. Positivity, support, and exact coefficients

All coefficients c_k(a) are nonnegative integers. The constant coefficient is 1. A nonconstant coefficient is zero when only one coordinate of a is positive. When a has s entries equal to one and all other entries zero, its coefficient is the derangement number !s. For arbitrary a, writing m=sum a_i and supp(a)={i:a_i>0}, one also has the independent formula

\[
 c_k(\mathbf a)=\sum_{I\subseteq\operatorname{supp}(\mathbf a)}
 (-1)^{|I|}\frac{(m-|I|)!}{\prod_i(a_i-1_{i\in I})!}.
\tag{2.2}
\]

**Proof.** Expanding the denominator as a geometric series gives (2.2). Multiplying (2.1) by 1-sum z_i gives the recurrence

\[
 c_k(\mathbf a)=\sum_{i:a_i>0}c_k(\mathbf a-\mathbf e_i)+q(\mathbf a),
\tag{2.3}
\]

where q(a)=(-1)^m if every a_i is 0 or 1, and q(a)=0 otherwise. The constant case is handled separately. On a binary support of size s this becomes C_s=s C_{s-1}+(-1)^s, with C_0=1 and C_1=0. Its solution is !s>=0. If a is not binary, q(a)=0, and induction on m proves nonnegativity. A single-coordinate coefficient is zero, first for m=1 and then by the same recurrence. This proves all assertions. No analytic convergence is used. QED.

For k=2 the complete formula simplifies to

\[
 R_2(z_1,z_2)=1+\frac{z_1z_2}{1-z_1-z_2},\qquad
 c_2(a,b)=\binom{a+b-2}{a-1}\quad(a,b\ge1).
\tag{2.4}
\]

The positive kernel is not a statement that the original Möbius coefficients are positive. It is the exact quotient between two specified signed coefficient systems.

### Theorem 2.2. The inverse kernel

Write

\[
 Q_k(\mathbf z)=R_k(\mathbf z)^{-1}
 =\frac{1-\sum_i z_i}{\prod_i(1-z_i)}
 =\sum_{\mathbf a\ge0}b_k(\mathbf a)\mathbf z^{\mathbf a}.
\tag{2.5}
\]

Then b_k(0)=1 and, for a!=0,

\[
 b_k(\mathbf a)=1-|\operatorname{supp}(\mathbf a)|.
\tag{2.6}
\]

**Proof.** In the product of geometric series every multi-index has coefficient 1. The subtracted term z_i contributes exactly when a_i>0. QED.

Thus both the positive kernel and the absolute value of its inverse have no degree-one terms; their degree-two mass is binom(k,2). This fact, not the total count of prime-overlap patterns, controls the norm cost.

## 3. Global exact identities, including all zero masks

For an ideal tuple d=(d_1,...,d_k) prime to S, define multiplicatively

\[
 C_k(\mathbf d)=\prod_{p\notin S}c_k(v_p(d_1),\ldots,v_p(d_k)),
 \qquad
 D_k(\mathbf d)=\prod_{p\notin S}b_k(v_p(d_1),\ldots,v_p(d_k)).
\tag{3.1}
\]

These products are finite, and C_k>=0. Both vanish unless every prime in a nontrivial tuple d appears in at least two of its coordinates.

### Theorem 3.1. Exact forward and inverse reconstruction

For every row u and every positive scale vector X,

\[
 \prod_{i=1}^k A_{i,u}(X_i)
 =\sum_{\mathbf d}C_k(\mathbf d)\theta_u(\prod_i d_i)
 B_{k,u}(X_1/Nd_1,\ldots,X_k/Nd_k),
\tag{3.2}
\]

and

\[
 B_{k,u}(\mathbf X)
 =\sum_{\mathbf d}D_k(\mathbf d)\theta_u(\prod_i d_i)
 \prod_{i=1}^k A_{i,u}(X_i/Nd_i).
\tag{3.3}
\]

Each displayed sum is finite after support restrictions: a nonzero summand has Nd_i<=b_i X_i. These statements do not enlarge S by the primes of d, nor do they drop any original row.

**Proof.** At a prime p, the coefficient generating function for the independent Möbius factors is prod_i(1-z_i). For the pairwise-coprime factors it is 1-sum_i z_i, because the prime may occupy at most one slot. Identity (2.1) gives their exact formal convolution, and (2.5) gives the reverse. Apply these identities separately at every prime dividing the finite tuple of original indices. Substitute

    z_i = theta_u(p) times the formal variable for p in slot i.

Complete multiplicativity gives the factor theta_u(prod d_i) in each convolution. If theta_u(p)=0, the same formal identity remains valid after substitution; no division by theta_u(p) occurs. Finally, convolution in coordinate i replaces W_i(Nn_i/X_i) by W_i(Na_i/(X_i/Nd_i)). This proves the smoothed formulas coefficient by coefficient. Compact support makes the realized convolution finite. QED.

For k=2 this bypasses the exterior gcd mask in PR #910 entirely. The terms X/Nd_1 and X/Nd_2 need not agree. Claiming that its older balanced c=1 estimate alone already handles this new rectangle would be incorrect.

## 4. The exact logarithmic cost

Let r=binom(k,2). Put

\[
 K_k^+(Z)=\sum_{\prod_iNd_i\le Z}\frac{C_k(\mathbf d)}{\sqrt{\prod_iNd_i}},
 \quad
 K_k^-(Z)=\sum_{\prod_iNd_i\le Z}\frac{|D_k(\mathbf d)|}{\sqrt{\prod_iNd_i}}.
\tag{4.1}
\]

### Theorem 4.1. Sharp kernel mass

For fixed k,K,S and Z>=2,

\[
 K_k^\pm(Z)\ll_{k,K,S}(1+\log Z)^r.
\tag{4.2}
\]

More precisely there are positive constants E_k^+(1/2), E_k^-(1/2) such that

\[
 K_k^\pm(Z)=
 \frac{\kappa_S^r E_k^\pm(1/2)}{2^r r!}(\log Z)^r
 +O_{k,K,S}((1+\log Z)^{r-1}),
\tag{4.3}
\]

where kappa_S=Res_{s=1} zeta_K^S(s)>0. Hence a bounded absolute-convolution norm at the square-root weight is not available for k>=2. This is sharpness of this particular kernel mass, not a lower bound on losses in the unknown arithmetic moment theorem.

**Proof.** Collapse a multi-index to its total degree. By positivity, the two local scalar generating functions are respectively

\[
 F_k^+(t)=\frac{(1-t)^k}{1-kt},\qquad
 F_k^-(t)=2-\frac{1-kt}{(1-t)^k}.
\tag{4.4}
\]

The second equality uses (2.6): every nonconstant inverse coefficient is nonpositive. Both scalar series have nonnegative coefficients and expansion

\[
 F_k^\pm(t)=1+r t^2+O_k(t^3).
\tag{4.5}
\]

Define E_{k,p}^\pm(t)=(1-t^2)^r F_k^\pm(t). Its first two positive-degree coefficients vanish. On any closed disk strictly inside |t|<1/k, its absolute coefficient sum beyond degree two is O_k(|t|^3), with the constant depending on the disk radius. For every p outside S and Re(s)>1/3, |(Np)^(-s)|<1/(2k). Consequently

\[
 E_k^\pm(s)=\prod_{p\notin S}E_{k,p}^\pm((Np)^{-s})
\tag{4.6}
\]

has an ideal Dirichlet series sum e_k^\pm(b)(Nb)^(-s) converging absolutely on Re(s)>1/3. This follows by multiplying the absolute local series and using sum_p(Np)^(-3 sigma)<infinity for sigma>1/3. Uniform convergence on compact subsets also gives holomorphy. At s=1/2 each local factor is positive and differs from one by a summable amount, so E_k^\pm(1/2)>0.

The scalar Dirichlet series of the grouped tuple coefficients therefore factors as

\[
 \sum_n f_k^\pm(n)(Nn)^{-s}
  =\zeta_K^S(2s)^r E_k^\pm(s)\qquad(\Re s>1/2).
\tag{4.7}
\]

Here f_k^+(n) sums C_k(d) over prod d_i=n, and f_k^-(n) sums |D_k(d)|. Let d_{r,S}(a) count the ordered r-tuples of ideals prime to S with product a. Coefficient comparison gives the exact identity

\[
 f_k^\pm(n)=\sum_{a^2b=n}d_{r,S}(a)e_k^\pm(b).
\tag{4.8}
\]

We record the elementary harmonic input, to specify the analytic dependency. For this fixed imaginary quadratic field, counting lattice points in a sector modulo its six units gives

    #{a integral ideal:(a,S)=1, Na<=X} = kappa_S X+O_S(sqrt(X)+1).

Finite inclusion-exclusion handles S. Partial summation gives

\[
 \sum_{Na\le X,(a,S)=1}\frac1{Na}
 =\kappa_S\log X+c_S+O_S(X^{-1/2}).
\tag{4.9}
\]

Taking r-fold multiplicative convolution and partial summation, by induction on r, gives

\[
 H_{r,S}(X):=\sum_{Na\le X}\frac{d_{r,S}(a)}{Na}
 =\frac{\kappa_S^r}{r!}(\log X)^r
  +O_{r,S}((1+\log X)^{r-1}).
\tag{4.10}
\]

For completeness, the induction writes H_{r+1,S}(X)=sum_{Na<=X,(a,S)=1}(Na)^(-1) H_{r,S}(X/Na). The main weighted integral is kappa_S int_1^X (log(X/t))^r dt/t = kappa_S(log X)^(r+1)/(r+1); the constant and decaying remainder in (4.9) contribute O((1+log X)^r). The accumulated previous error has the same size. This proves (4.10), including its asserted remainder.

Now (4.8) implies

\[
 K_k^\pm(Z)=\sum_{Nb\le Z}\frac{e_k^\pm(b)}{\sqrt{Nb}}
 H_{r,S}\left(\sqrt{Z/Nb}\right).
\tag{4.11}
\]

Absolute convergence of E at, for example, 5/12 ensures that
sum_b |e(b)|(Nb)^(-1/2)(1+log Nb)^r is finite. Substitute (4.10) into (4.11). Replacing (log Z-log Nb)^r by (log Z)^r costs O((1+log Z)^(r-1)); the omitted tail Nb>Z is a negative power of Z times a logarithm. The remaining sum is E(1/2). The factor 2^(-r) comes from sqrt(Z/Nb). This proves (4.3) and (4.2). QED.

An independent upper-bound-only proof needs no asymptotic: in (4.8), bound the inner harmonic convolution by (sum_{Na<=sqrt Z}1/Na)^r and sum |e(b)|/sqrt(Nb). This yields (4.2) directly.

## 5. Unconditional norm comparison

Let U be any finite row set with any fixed nonnegative measure. Write ||.||_p for the corresponding row norm. No independence, randomness, or cancellation assumption is made about this measure.

### Theorem 5.1. Forward norm transfer

For Z=prod_i(b_i X_i)>=1,

\[
 \left\|\prod_i A_{i,\cdot}(X_i)\right\|_2
 \le K_k^+(Z)\sqrt{\prod_iX_i}
 \sup_{\substack{0<Y_i\le X_i\\B_{k,\cdot}(\mathbf Y)\ne0}}
 \frac{\|B_{k,\cdot}(\mathbf Y)\|_2}{\sqrt{\prod_iY_i}}.
\tag{5.1}
\]

The corresponding reverse inequality uses K_k^-(Z) and the supremum of
||prod_i A_i(Y_i)||_2/sqrt(prod_iY_i) to bound ||B_k(X)||_2/sqrt(prod_iX_i).

**Proof.** Apply Minkowski to (3.2). Multiplication by theta_u(prod d_i) is a contraction in row L2, including zero rows. For Y_i=X_i/Nd_i, insert the supremum from (5.1) and sum C_k(d)/sqrt(prod Nd_i). The product support lies inside prod Nd_i<=Z. This is (5.1). Apply the same argument to (3.3) with absolute inverse coefficients for the reverse inequality. All sums are finite. QED.

This proves a comparison theorem, not the missing smallness of either supremum.

### Theorem 5.2. Reversible all-order energy reduction

Take all W_i equal to a fixed W supported in [a,b]. For the complete physical row set U_H={u:0<Nu<=H}, define

\[
 \mathfrak M_k(D,H)=\sup_{1/b\le X\le D}
 \frac{\sum_{u\in U_H}|A_u(X)|^{2k}}{H X^k},
\tag{5.2}
\]

\[
 \mathfrak C_k(D,H)=\sup_{1/b\le X_1,\ldots,X_k\le D}
 \frac{\sum_{u\in U_H}|B_{k,u}(\mathbf X)|^2}{H\prod_iX_i}.
\tag{5.3}
\]

For D>=max(2,1/b),

\[
 \mathfrak M_k(D,H)\ll_{k,S,W}
 (1+\log D)^{k(k-1)}\mathfrak C_k(D,H),
\tag{5.4}
\]

\[
 \mathfrak C_k(D,H)\ll_{k,S,W}
 (1+\log D)^{k(k-1)}\mathfrak M_k(D,H).
\tag{5.5}
\]

All original rows, including sixth-power rows, are retained. The same H is used at every shortened factor scale.

**Proof.** For (5.4), use X_1=...=X_k=X in (5.1), then square and apply (4.2). For (5.5), the reverse formula requires products at possibly unequal scales. Hölder gives

\[
 \|\prod_iA_\cdot(Y_i)\|_2
 \le\prod_i\|A_\cdot(Y_i)\|_{2k}
 \le H^{1/2}\sqrt{\prod_iY_i}\,\mathfrak M_k(D,H)^{1/2}.
\]

Insert this into the reverse part of Theorem 5.1 and square. All nonzero shortened factors have Y_i>=1/b. Since 2r=k(k-1), the logarithmic exponents are as displayed. QED.

**Important quantifier:** (5.2) is a scale-envelope statement at one fixed full row range H. The earlier moment conjecture only on the single curve H=X^(1+theta) does not automatically give this stronger envelope for X<D. Conversely, proving (5.3) at H=D^(1+theta) suffices for the needed top-scale moment, by (5.4). This packet does not conflate these two assertions.

## 6. Fourth and sixth moments explicitly

For k=2, the new sufficient theorem is the fixed-mask rectangular estimate

\[
 \sum_{0<Nu\le D^{1+\theta}}|B_{2,u}(X_1,X_2)|^2
 \ll D^\epsilon D^{1+\theta}X_1X_2
\tag{6.1}
\]

for every 1/b<=X_i<=D. Unlike the previous sufficient estimate, it has no varying exterior c. Unlike its balanced c=1 special case, it must cover X_1!=X_2. The proven adapter costs (log D)^2 in the resulting fourth moment. Neither (6.1) nor the fourth moment is proved here.

For k=3, replace the two-factor disjoint product by the three-factor disjoint product. The same fixed-mask rectangle target with X_1 X_2 X_3 gives

\[
 \sum_{0<Nu\le H}|A_u(D)|^6\ll H D^{3+\epsilon},
\tag{6.2}
\]

conditionally, with (log D)^6 absorbed into D^epsilon. The kernel automatically retains and removes pair overlaps, triple overlaps, repeated prime powers, and all shared row zeros. There is no new separately assumed moving-mask lemma at order six.

At general fixed k, the exponent of the logarithmic energy cost is k(k-1), not a new fixed power of D. Constants depend on k; this is sufficient for a qualitative all-orders implication to RH. It is not a claim of a practical algorithm uniform in k.

## 7. A separate exact moving-exclusion adapter

The direct reconstruction above already avoids moving exclusions. The following independent adapter explains their cost when they are needed elsewhere.

Let B_{k,c,u}(X) be (1.2) with the extra condition (prod n_i,c)=1. At each p|c, its source deletes 1-sum z_i, so its inverse local factor is

\[
 (1-\sum_i z_i)^{-1}
 =\sum_{\mathbf a\ge0}\frac{|\mathbf a|!}{\prod_i a_i!}\mathbf z^{\mathbf a}.
\tag{7.1}
\]

Multiplying these local series gives an exact finite-horizon expression for B_{k,c,u} in terms of unmasked B_{k,u} at shorter, generally unequal, scales, with row multipliers theta_u(prod d_i). The square-root weighted absolute mass is bounded by

\[
 \prod_{p\mid c,p\notin S}(1-k/\sqrt{Np})^{-1}.
\tag{7.2}
\]

For every epsilon>0, (7.2) is O_{k,S,epsilon}((Nc)^epsilon). Indeed, each factor is defined and positive because of S; for all sufficiently large prime norms its logarithm is <=epsilon log Np. The finitely many smaller norms cost one fixed constant. Hence a fixed-mask rectangular norm bound transfers to all exclusions Nc<=D^A with only D^epsilon loss, for every fixed A after choosing the preliminary epsilon smaller.

This adapter is unconditional as an operator estimate. It does not derive a rectangular theorem from an equal-scale theorem. Treating c as fixed while hiding arbitrary c-dependence in a constant would still be invalid.

## 8. Why this does not close the moment theorem

There remains one literal off-diagonal problem: the row norm of the fixed-mask polynomial (1.2), with its full balanced/rectangular divisor-allocation weights. Multiplicative phases alone do not give this bound.

A decisive countermodel to an overly general approach is theta(n)=(-1)^Omega(n). For squarefree n, mu(n)theta(n)=1. Give every abstract row this same phase system. All identities and norm comparisons in this packet remain valid, and each local phase is a sixth root of unity; nevertheless, for nonnegative nonzero W, A(D) is of order D and its 2k-th row moment has order H D^(2k), not H D^k. This follows from the positive density of squarefree ideals, obtained by fixed-field ideal counting and Möbius inversion. This synthetic phase family is NOT asserted to occur as the genuine Hecke/sextic family. It shows exactly why a proof using only the algebra already established here cannot supply the missing cancellation.

Nor does squaring a polynomial and applying a generic length bound solve the issue: the k-factor column length is about D^k, whereas the useful physical row range is near D. The new reduction preserves the arithmetic coefficient, but does not make that mismatch disappear.

The substantive completed result is the all-order, reversible, polylogarithmic transfer and the elimination of moving exclusions as an independent analytic premise. A new fixed-mask rectangular estimate, even with the losses allowed in `MOMENT_FRONTIER.md`, is still necessary.
