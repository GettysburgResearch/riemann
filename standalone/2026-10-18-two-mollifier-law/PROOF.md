# Two mollifiers: density-free capped reciprocal moment laws

Status: PROPOSED complete deductions from the named analytic contracts below;
independent mathematical review required. No RH, zero-density theorem,
zero-free rectangle, analytic logarithm of L, or uncapped inverse moment is
assumed. The cap remains essential. Recovery of the earlier ten-file packet
is separate from this new mathematics.

## 1. Statements and scope

Fix the de Faveri family over a number field F containing mu_n, n>=3, its
admissible finite S and ray/generator choices, and one fixed allowed
S-supported finite-order twist psi. All rows are n-th-power-free EXTERIOR
INTEGRAL IDEALS, ordered by their FULL ideal norms. Distinct ideals of equal
norm are not identified. Write

    L_a(s)=L_F^S(s,psi chi_a),
    M_A(s,a)=sum_(Nd<=A) mu_F(d) psi(d) chi_a(d) (Nd)^(-s),
    E_A(s,a)=L_a(s)M_A(s,a)-1.

All character zeros at nonunits remain. Fix a nonzero nonnegative smooth
weight W supported in (1,2). Prefix bounds are applied at2U for this window;
fixed multiples of U and cutoff lengths only change the fixed constants. Define

    c_W = Res_(z=1) zeta_F^S(z) / zeta_F^S(n) * integral W(x) dx,
    w_p = (1-1/q)/(1-q^(-n)), q=Np,
    C_k(s)=product_(p outside S) [1-w_p+(w_p/n)
                  sum_(zeta^n=1)|1-psi(p) zeta q^(-s)|^(2k)].     (1)

For every fixed k and Re s>1/2, this product converges to a finite positive
number. Additional congruence classes at k>=n are included. A zero of L is
assigned the cap in every expression min(|L|^(-2k),T).

### Theorem A: an explicit sextic cap/error tradeoff

Take n=6, s=3/4+it, with t in any fixed compact interval. All k below are
FIXED positive integers. Define

 k              delta_k
 1              4/15
 2              1/4
 3,...,5        1/5
 6,...,10       1/k
 11,...,15      19/194
 k>=16          3/(2k),

and put e_k=1/(8k+2). For every FIXED 0<theta<delta_k and epsilon>0,

 sum_a W(Na/U) min(|L_a(s)|^(-2k), U^theta)
   = c_W C_k(s) U + O(U^(1-eta_k(theta)+epsilon)),
 eta_k(theta)=min(e_k,theta,delta_k-theta).                     (2)

Every row in the weighted family is included; there is no zero-selected
exceptional family in (2). Constants depend on all fixed data, k,theta,
epsilon and the compact height interval. No growing-k or critical-line
uniformity is asserted. The same statement holds after adjoining any fixed finite set of prescribed
rows with bounded nonnegative weights: their capped contribution is
O(U^theta), which fits the displayed error. This can include the principal
member but does not remove the cap.

In particular, at k=1 there are TWO useful specializations:

 cap U^(1/6): error O(U^(9/10+epsilon));
 cap U^(1/4): error O(U^(59/60+epsilon)).                       (3)

Both have the actual leading constant

    C_1(3/4+it)=product_(p outside S)(1+w_p q^(-3/2)).

The first has a much stronger power error; the second has a larger cap.
The #984 displayed law uses cap U^(1/80), error O(U^(127/128)). We do not
change that historical theorem. Taking, for example, epsilon<1/1000 in (3)
keeps both new errors stronger than that displayed old error.

For every fixed k, theta=delta_k-e_k gives error
O(U^(1-1/(8k+2)+epsilon)). For k>=16 its cap exponent is

    3/(2k)-1/(8k+2) = (11k+3)/(2k(4k+1)) ~ 11/(8k).           (4)

This improves the recovered packet's U^(1/k) high-order CAP for an upper
bound and now supplies a leading-term law, but it is not uniformly larger
than #984's U^(1/80) cap as k tends to infinity. No all-k superiority over
that different guarantee is claimed.

### Theorem B: every fixed line right of 1/2, without zero density

For general fixed n>=3, s=sigma+it, 1/2<sigma<1, put

    d=2sigma-1, a=min(d/2,1/(4k)), Delta=d a.

Then, for every epsilon>0,

 sum_a W(Na/U) min(|L_a(s)|^(-2k), U^(3Delta/4))
   = c_W C_k(s) U + O(U^(1-Delta/4+epsilon)).                   (5)

Uniformity is only on fixed compact t intervals, and constants may depend
on sigma,k,n,F,S,psi,W. This asserts neither sigma=1/2 nor an unbounded-order
limit. It avoids the zero-density input used by #984 to define a common good
set. It does not preserve that common-good-set theorem: the auxiliary good
set used here may depend on k and t, and the FINAL statement is capped.

## 2. Analytic inputs, without circular use of inverse moments

We adopt the exact family and its four-term large-sieve contract from the
pinned source notes #984 and #986:

 sum_(Na<=U)^flat |sum_(Nc<=V)^flat z_c chi_a(c)|^2
   << (UV)^epsilon K_n(U,V) sum_c |z_c|^2,
 K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).                (LS)

Both indices are n-th-power-free. Its deep proof is external. For full
columns c=e f^n, retain exactly chi_a(c)=chi_a(e)1_((a,f)=1), with NO added
condition (e,f)=1. Minkowski in row l2 costs the convergent sum
sum_f (Nf)^(-n/2+epsilon). Thus a full column dyad with divisor-bounded
coefficients of size (Nc)^(-u) has squared norm

    << (UV)^epsilon V^(1-2u)K_n(U,V).                         (6)

For A=U^a, integer j>=1 and d=2sigma-1, powering the COMPLETE mollifier
before (6), including every individual cap, gives

 sum |M_A|^(2j) << U^(m_j+epsilon),
 m_j=max(1,k_n(ja)-dja),
 k_n(v)=max(1,v,1-1/n+2v/n,2/n+(1-1/n)v).                     (7)

These polynomial bounds have no inverse-L or zero-free premise.

The other adopted analytic contract is the exact flat-cutoff functional
equation in #984 MOLLIFIED_APPROXIMATION and #986 PROOF Section 3. It splits
NONPRINCIPAL L_a=P_X+R_X, where P_X has a smooth cutoff equal to one below X,
and the complete conjugate dual has actual conductor Q_a, length Q_a/X and
factor Q_a^(1/2-s). Both tails, all fixed S terms and all conductor dyads,
including Q_a<X, are retained. This is NOT the statement that the dual is a
finite polynomial or that chi(c)bar(chi(b))=chi(cb). Primitive principal
rows carry a pole term and are instead paid directly in the FINAL residual.

For clarity, the exact consequence of that contract used here is #986's
Theorem C, reconstructed at its exponent level. For fixed 0<a<=x<=1,
r>=1 and p>=2 integers, define

 b_j=k_n(j(1-x))-jd x,
 g_r=max(k_n(ra)-dra,k_n(r(a+x))-dr(a+x)),
 G=max(g_r,[m_(pr)+(p-2)b_r+b_(2r)]/p,0,ra(1-d)).             (8)

Then the FULL family satisfies sum |E_(U^a)|^(2r)<<U^(G+epsilon).
Indeed the main coefficients vanish exactly through A before estimating;
the remaining r-fold support is A^r<Nc<=(2AX)^r. Its (6) bound is g_r.
On actual conductor Q, the powered dual has scalar Q^(-jd) and positive
column weight C^(jd); at C=Q/X these combine to X^(-jd) BEFORE Q is bounded
by U. When Q<X, rapid decay bounds the entire subunit tail. This gives b_j
for nonprincipal rows. Holder uses M_(2pr), R_(2r), R_(4r), with weights
1/p,(p-2)/p,1/p. The finitely many principal final residuals cost
O(1+A^(r(1-d))). These are precisely the terms of G. This summary keeps the
source contracts explicit; it is not a fresh verification of their full
Hecke/gamma or finite-S derivations.

For Theorem B we also use the simpler #984 bound, at its stated scope:

 0<a<=d/2 ==> sum_all |E_(U^a)|^2 << U^(1-da+epsilon).          (9)

No zero-density theorem or reciprocal-moment conclusion of #984 is used.
If any of these source interfaces is false, the application below fails;
the elementary transfer theorem of Section 3 remains valid independently.

## 3. A two-mollifier transfer theorem for arbitrary finite arrays

This is the new operation. Let L_i,P_i,Q_i be arbitrary complex arrays on a
finite weighted family, with 0<=w_i<=C and sum_i w_i=O(U). Fix k and r. Suppose

 sum w_i(|P_i|^(4k)+|Q_i|^(4k)) << U^(1+epsilon),
 sum w_i|L_i P_i-1|^(2r) << U^(1-delta+epsilon),
 sum w_i|L_i Q_i-1|^2 << U^(1-lambda+epsilon),
 sum w_i|Q_i|^(2k)=cU+O(U^(1-tau+epsilon)).                    (10)

All losses are available arbitrarily small; no independence or nonvanishing
of any L_i is assumed. For any fixed 0<theta<delta, these imply

 sum w_i min(|L_i|^(-2k),U^theta)
 =cU+O(U^(1-eta+epsilon)),
 eta=min(lambda/2,tau,delta/2,theta,delta-theta).               (11)

Proof. Let B={i:|L_i P_i-1|>1/2} and G its complement. Weighted Markov gives
sum_B w_i<<U^(1-delta+epsilon). In particular EVERY L_i=0 lies in B. On G,
I_i=1/L_i exists and |I_i|<=2|P_i|. With F_i=L_i Q_i-1, exactly

    I_i-Q_i=-I_i F_i.

The elementary difference-of-powers estimate and Young's inequality give

 ||I_i|^(2k)-|Q_i|^(2k)|
  <=C_k |F_i|(|P_i|^(2k)+|Q_i|^(2k)), i in G.                 (12)

For example C_k=4k(2^(2k-1)+1) suffices: bound |I_i-Q_i| by 2|P_i||F_i|,
then use |P_i||Q_i|^(2k-1)<=|P_i|^(2k)+|Q_i|^(2k). Cauchy and (10) show
that the total error in (12) is O(U^(1-lambda/2+epsilon)). The missing Q
mass is at most

 sum_B w_i |Q_i|^(2k)
 <=(sum w_i|Q_i|^(4k))^(1/2)(sum_B w_i)^(1/2)
 << U^(1-delta/2+epsilon).                                  (13)

We do NOT assert that the cap is inactive on G. Its entire cost is

 sum_G w_i (|I_i|^(2k)-min(|I_i|^(2k),U^theta))
 <=U^(-theta)sum_G w_i|I_i|^(4k)
 << U^(1-theta+epsilon).                                    (14)

All bad rows, including zeros, contribute at most
U^theta sum_B w_i<<U^(1-delta+theta+epsilon). Combine (12)--(14) with the
last line of (10). This proves (11). The long polynomial P is used only to
CONTROL inverse size and the bad-row mass; the short polynomial Q is used
to COMPUTE the leading term. Neither must be a statistically independent
approximation of the other. The construction of G uses no zeros. QED.

## 4. Short-polynomial moments and the exact Euler constant

We reconstruct #984 RECIPROCAL_MOMENTS Sections 3--4, not its zero-density
Section 2 or its inverse transfer. Reciprocity, followed by Fourier inversion
on the FIXED ray-class group, expresses the n-free-row generating series for
chi_a(b) as a finite linear combination of

    L^S(z,xi chi_b)/zeta_F^(S union supp(b))(nz).               (15)

Neutral prime powers still impose coprimality masks in the numerator. For
b not an n-th power, each inducing character has nontrivial exterior
ramification, which a fixed S-supported xi cannot cancel. Its conductor is
O(N rad(b)). Classical conductor convexity on Re z=1/2+epsilon and smooth
Mellin inversion give

 sum_a W(Na/U)chi_a(b)
 <<U^(1/2+epsilon)(N rad(b))^(1/4+epsilon)(Nb)^epsilon.         (16)

The reciprocal factor in (15) is in absolute Euler convergence because
n(1/2+epsilon)>1. There is no inverse-L contour through unknown zeros.
For b an n-th power, chi_a(b)=1_((a,b)=1) exactly, and the same calculation
with its pole at one gives main term c_W U product_(p|b)w_p, with error
O(U^(1/2+epsilon)(Nb)^epsilon). These are the precise imported reciprocity
and conductor conventions of #984, not arbitrary character families.

Expand |M_B|^(2k). Its row label is b_+ b_-^(n-1), where b_+,b_- are complete
products of k separately capped squarefree columns. All common primes and
all distinct ideals remain. Its radical has norm at most B^(2k), although
its formal label can have norm B^(nk). A principal label means primewise
exponent differences divisible by n, NOT equal rational norms.

Apply (16) to each nonprincipal tuple. The total error is at most

 U^(1/2+epsilon)(sum_(Nd<=B)(Nd)^(1/4-sigma+epsilon))^(2k)
 << U^(1/2+epsilon)B^(k(5/2-2sigma)+epsilon).                  (17)

The principal tuple sum is the truncated version of C_k(s). Its absolute
Euler expansion converges since any nonconstant local neutral term uses at
least TWO column occurrences; n>=3. To bound an omitted column Nd>B,
use Rankin with exponent d/2, d=2sigma-1. The charged local terms still
decay at least q^(-2sigma+d/2), with 2sigma-d/2>1. Summing over the 2k
possible omitted columns gives error O(B^(-d/2)). Thus

 sum W|M_B|^(2k)=c_W C_k(s)U
   +O(U B^(-d/2)+U^(1/2+epsilon)B^(k(5/2-2sigma)+epsilon)).    (18)

This retains the whole principal tuple sum, which can have complex phase
terms at k>=n. Positivity of the total local factor follows directly from
the root average in (1). No independent-row model is substituted.

## 5. Explicit long-mollifier choices at sigma=3/4

Here n=6,d=1/2. By (7), sum |M_(U^a)|^(2j)<<U^(1+epsilon) whenever ja<=2:
k_6(v)-v/2 is convex and at most one at both v=0 and v=2. In particular

    a<=1/k ==> sum |M_(U^a)|^(4k)<<U^(1+epsilon).              (19)

The complete residual bounds needed for P are:

 (i) a=3/5: residual second moment U^(11/15+epsilon) [#986].
 (ii) 0<a<=1/2: residual second moment U^(1-a/2+epsilon).
 (iii) 0<a<=1/5: residual fourth moment U^(1-a+epsilon).
 (iv) 0<a<=19/291: residual sixth moment U^(1-3a/2+epsilon).     (20)

For (ii), take x=3/4,r=1,p=3 in (8). The main endpoint powers are
1-a/2, (a+3/4)/2, 5/6-a/6, 1/3+(a+3/4)/3; each is at most 1-a/2.
M6 has exponent one; the dual second and fourth powers are 5/8 and1/4.
Their mixed exponent is5/8, which fits. The principal final cost a/2 fits.

For (iii), take x=1/2,r=2,p=5. For a<=1/5, m_10=1, b_2=2/3,b_4=1, so
the mixed exponent is4/5. The main exponent is
max(1-a,2/3+2a/3)=1-a. The principal cost a is smaller. Its endpoint a=1/5
is #987's fourth residual theorem; extending to smaller lengths is this
direct specialization of the SAME envelope, not a new analytic mechanism.

For (iv), take x=293/582,r=3,p=11. At a0=19/291, #987 gives
m_33=209/194,b_3=159/194,b_6=285/194 and mixed/main exponent175/194.
For a<=a0, m_33 is nondecreasing in a and hence at most its endpoint value.
The mixed bound is therefore <=175/194<=1-3a/2. The low main endpoint is
1-3a/2. The high endpoint is 1/3+a+x, also <=1-3a/2 for a<=a0. This last
branch identity uses 3(a+x) between 3x>3/2 and 3(a0+x)<2. The principal
cost3a/2 is smaller. This proves the WHOLE interval (iv), not a sampled fit.

Choose P=M_(U^a) by the following table. The listed 2r is the residual
moment used in weighted Markov; it is NOT the requested negative order2k.

 k         a             2r       delta from (20)
 1         3/5           2        4/15
 2         1/2           2        1/4
 3--5      1/5           4        1/5
 6--10     1/k           4        1/k
 11--15    19/291        6        19/194
 >=16      1/k           6        3/(2k).

Every entry has a<=1/k, so (19) proves the necessary P4k bound. The terminal
range uses 1/16<19/291. These are convenient valid choices, not a claim to
optimize every possible moment interpolation or mollifier architecture.

## 6. Proof of Theorem A

Set b=2/(4k+1), Q=M_(U^b). Then b<=2/5<1/2, so (20)(ii) supplies
lambda=b/2 in (10). Also 2k b<1, so (19) supplies Q4k. At sigma3/4,
(18) has the two error exponents

    1-b/4 = 1/2+kb = 1-1/(8k+2).                            (21)

Thus tau=lambda/2=e_k. The long choice in Section5 gives delta=delta_k.
In every range delta_k>=2e_k: for k>=16 this is the elementary inequality
3/(2k)>=1/(4k+1); the bounded remaining ranges follow directly from the
listed rational fractions. Hence delta_k/2 is redundant in the minimum
of (11), proving (2). Choosing theta=delta_k-e_k gives error e_k and is
legal because delta_k>e_k and theta>=e_k. Substitution gives (3)--(4).
All loss constants are chosen after fixed k,theta and the requested epsilon.
There is no silently uniform limit as theta tends to delta_k. QED.

## 7. Proof of Theorem B

Let a=min(d/2,1/(4k)), b=a/2. Take P=M_(U^a), Q=M_(U^b). Then (9) gives
delta=da=Delta and lambda=db=Delta/2. Because2k a<=1/2, k_n(v)=1 on the
entire relevant polynomial range0<=v<=2k a for every n>=3. Thus (7) gives
both P4k and Q4k bounds U^(1+epsilon).

The first error in (18) has saving db/2=Delta/4. For the second,

 1/2+kb(5/2-2sigma)=1/2+kb(3/2-d)<=11/16,

since kb<=1/8 and0<d<1. This is smaller than1-Delta/4: indeed Delta<=d/(4k)
so Delta/4<1/16. Therefore tau=Delta/4 is permissible. Apply (11) with
theta=3Delta/4. Its minimum isDelta/4, proving (5). QED.

## 8. What was tried toward removing the cap, and what remains

The long residual condition |L P-1|<=1/2 is algebraic, not a zero-free-region
assumption. It supplies enough inverse control to replace the zero-density
and analytic-log step of #984 for this CAPPED conclusion. The bad set can
still contain every copy of a problematic fixed member. Its total capped
contribution is explicitly paid, not deleted.

At an actual zero L=0, E_A=-1 for every mollifier. Every residual exponent
used here is positive, and every chosen reciprocal POWER cap has exponent
less than one. The new laws therefore still accommodate a persistent zero.
The literal moving annulus eventually omits every fixed member. Even after
adjoining a prescribed member as permitted in Theorem A, a hypothetical zero
contributes only U^(1/4) in the largest second-moment example, far below both
the main U and the allowed U^(59/60+epsilon) error. No contradiction follows. VERTICAL_CAP_AUDIT.md also records the
attempt to detect that zero after vertical averaging; its singular mass
still fits these powers.

No uncapped exceptional contribution, critical Gaussian Mobius moment,
theta-to-native signed projection, or improved individual zero-free boundary
has been proved. The strict improvement is the full capped Euler law, its
larger cap and sharper error, and the removal of a zero-density premise.
The residual estimates themselves are credited to #984/#986/#987. Neither
this composition nor its finite checker is independent referee acceptance.
