# Two native angular theorems over any fixed imaginary quadratic field

**Scope:** complete ideal coefficients, fixed imaginary quadratic field, original separate caps, fixed radial parameters, and full logarithmic-Gaussian tails. Both proofs are unconditional in the sense that they do not assume quasi-RH, zero-free strips or unproved inverse moments. They use standard ideal counting and character periodicity. The results are **proposed**, not independently refereed.

## 1. Set-up and angular extension

Let K be a fixed imaginary quadratic field with discriminant d_K<0, ring of integers O_K, h_K ideal classes and w_K units. Let Q be any fixed squarefree positive integer divisible by rad(|d_K|), and S the set of ALL prime ideals over rational primes p|Q (rational saturation). Write chi=chi_(d_K) for the quadratic Dirichlet character of K. The finite excluded ideal Mobius is mu_K^S(I)=mu_K(I)1_((I,S)=1).

On principal fractional ideals set Psi((alpha))=(alpha/|alpha|)^w_K. This is independent of the generator because units have order dividing w_K. It extends to a unitary character Psi on all fractional ideals: the principal-ideal subgroup has finite index in the ideal group, and a character to U(1) extends across each additional cyclic quotient generator by choosing an appropriate complex root. Fix ANY such extension once and for all. Its powers Psi_l=Psi^l, l integer, have the same positive-rational invariance Psi_l((a))=1. No finite-order theorem is being applied to Psi_l.

Define normalized discrete Gaussian weights for R>=1, arbitrary integer l0:

    p_R(l-l0)=exp(-(l-l0)^2/(2R^2)) / sum_(j in Z) exp(-j^2/(2R^2)).

For any finitely supported ideal coefficient sequence a(I), put

    F_l(a)=sum_I a(I) Psi(I)^l .

The Fourier kernel Theta_R(phi)=sum_l p_R(l)e^(il phi) equals the normalized positive periodization of exp(-R^2 phi^2/2), times a harmless center phase. Uniformly for R>=1,

    |Theta_R(phi)| <= C exp(-c R^2 dist(phi,2pi Z)^2),      (1)

with absolute c,C>0.

## 2. Rational content and classwise angular separation

Every integral nonzero ideal has a unique decomposition I=(a)J, with a in positive integers and J *rational-primitive*: there is no integer b>1 with (b)|J. For a principal ideal this is just the rational content of any integral generator, but the definition works in all ideal classes.

For two distinct primitive J,J' IN THE SAME ideal class with norms <=Y, there is a c_K>0 such that

    dist(arg Psi(J)-arg Psi(J'),2pi Z) >= c_K/Y.             (2)

To prove it, choose for that class a fixed integral representative A of its inverse class; JA=(alpha), J'A=(beta) with alpha,beta in the fixed lattice A and |alpha|^2=(NA)(NJ), |beta|^2=(NA)(NJ'). Their angular ratio is (alpha/|alpha|)^w_K/(beta/|beta|)^w_K; the unknown Psi(A) cancels. Rotate one generator by a unit to make |theta|<=pi/w_K<=pi/2. If theta=0, alpha/beta is a nonzero rational number, so J/J'=(r) for positive rational r. The uniqueness of primitive rational content gives J=J', contradiction. Otherwise the nonzero lattice determinant Im(alpha*conj(beta)) has absolute value >=c_A>0 and |alpha beta|<=NA*Y. Since dist=w_K|theta| and |theta|>=|sin(theta)|, (2) follows. Class representatives are finite, giving a common c_K.

Consequently, among primitive J of ONE class with NJ<=Y, a Gaussian-neighbor packing argument gives

    sup_J sum_(J') |Theta_R(arg Psi(J)-arg Psi(J'))|
                  <= C_K (1+Y/R).                         (3)

Indeed a fixed J sees at most two angular neighbors in each distance interval of length c_K/Y, and sum_n exp(-c(Rn/Y)^2) << 1+Y/R. The kernel has a center phase, but the Schur test uses its absolute value. Between distinct ideal classes no comparable separation is asserted: use instead |sum_(classes)F_class|^2 <= h_K sum_class |F_class|^2. Hence for any b_J supported on rational-primitive NJ<=Y,

    sum_l p_R(l-l0)|sum_J b_J Psi(J)^l|^2
        <= C_K(1+Y/R) sum_J |b_J|^2.                       (4)

This proof is also a precise reason the class-number-one exact ray-diagonal comparison of #972 cannot just be copied unchanged into a nontrivial class group.

Standard ideal counting follows from the same class lattices: # {I integral: NI<=Y} <<_K Y for Y>=1. Hence

    sum_(NJ<=Y, J primitive) 1/NJ <<_K log(2Y).            (5)

## 3. The sharp second-moment theorem for the actual signed source

Consider for X>=2 and real t

    A_(t,l)(X)=sum_(X/2<NI<=X) mu_K^S(I)(NI)^(it)Psi(I)^l.

**Theorem A.** Uniformly in X>=2, R>=1, l0 integer and t real,

    sum_l p_R(l-l0)|A_(t,l)(X)|^2
          <<_(K,Q) (1+|t|)^2 X(1+X/R).                    (6)

The ideal content decomposition is literal. A squarefree ideal I=(a)J prime to S has a squarefree primitive J supported on at most one of the two primes above each split rational p; all inert prime ideals lie in (a), and ramified primes are excluded. This gives a bijection with pairs

    J primitive squarefree, (J,S)=1;
    a squarefree, (a,Q*NJ)=1.

Crucially,

    mu_K((a)J)=mu_K(J)mu(a)^2 chi(a),
    Psi_l((a)J)=Psi_l(J).                                 (7)

At an unramified split rational prime (p) has two prime-ideal factors and sign +1, while at an inert prime (p) itself is one prime ideal and sign -1. These signs are chi(p).

For M divisible by Q define f(M)=prod_(p|M)(1+p^(-1/2)) and

    S_M(Y)=sum_(a<=Y,(a,M)=1) mu(a)^2 chi(a).

Using mu(a)^2=sum_(d^2|a)mu(d) and finite Mobius removal of (a,M)=1,

    S_M(Y)=sum_(d<=sqrt Y,(d,M)=1)mu(d)
             sum_(e|rad M)mu(e)chi(e)
               sum_(b<=Y/(d^2 e))chi(b).

The primitive nonprincipal chi has sum zero over a complete period, so each last partial sum has modulus <=|d_K|. Restricting d<=sqrt(Y/e) gives

    |S_M(Y)| <= C_K sqrt Y f(M).                           (8)

This is the essential actual-sign cancellation. Partial summation of a^(2it) over (sqrt(X/NJ)/sqrt2,sqrt(X/NJ)] now gives the exact ray coefficient b_J with

    |b_J| <= C_K(1+|t|)(X/NJ)^(1/4) f(Q*NJ).               (9)

Its square is summable without a logarithmic cost. For squarefree n, let
h(p)=2p^(-1/2)+p^(-1), so f(n)^2=sum_(d|n)h(d). To count primitive split-support ideals J divisible by rational d, choose at most 2^omega(d) prime-ideal factors of norm p, and bound the remaining ideals by C_K Y/d. Thus

    sum_(J primitive squarefree, NJ<=Y) f(NJ)^2
      <= C_K Y product_(p split)(1+4p^(-3/2)+2p^(-2))
      <<_K Y.                                             (10)

Partial summation gives sum_(NJ<=X) f(NJ)^2/sqrt(NJ) <<sqrt X. Therefore
sum_J |b_J|^2 <<_(K,Q) (1+|t|)^2 X. Inserting into (4) at Y=X proves (6), uniformly in l0. No averaging over t was introduced.

A useful complementary fact is that this diagonal is >=c_(K,Q)X for all sufficiently large X, uniformly in t. Restrict to primitive squarefree J with X/2<NJ<=X; their rational ray has only a=1 and |b_J|=1. They have positive density. In fact their Euler series is

    H(s)=prod_(p split,p∤Q)(1+2p^(-s)) = zeta_K^S(s) V(s),

where V has factors (1-3p^(-2s)+2p^(-3s)) at split p and (1-p^(-2s)) at inert p; it has absolutely summable coefficients at every real sigma>1/2. Fixed-field ideal counting with O(sqrt Y) boundary error, convolved at sigma=3/4, gives # {such J:NJ<=Y}=kappa_(K,Q)Y+O_(K,Q)(Y^(3/4)), with kappa_(K,Q)>0. This is a diagonal lower bound, NOT a global lower bound for the angular mean across classes.

## 4. All tails: full Gaussian and energy at the fixed radial parameter

Let W_c(u)=u^(-c) exp(-(log u)^2/4)/(2sqrt(pi)) and

    A_(t,l)^c(X)=sum_I mu_K^S(I)(NI)^(it)Psi(I)^l W_c(NI/X).

**Theorem B.** For fixed K,Q,c and all D>=2,R>=1, l0 and t,

    sum_l p_R(l-l0) integral_0^D |A_(t,l)^c(X)|^2 dX/X^2
      <<_(K,Q,c) (1+|t|)^2[log(3+D)+D/R].                 (11)

Proof: partition NI/X into all dyadic bands (2^j,2^(j+1)], j integer. Write Y_j=2^(j+1)X and w_j=sup_band W_c. Then
w_j<<_c exp(-c_0 j^2+C_c |j|). Partial summation in (8) with the full norm derivative of W_c gives the j-th band signed ray l2 norm

    ||b^(j)||_2 <<_(K,Q,c) (1+|t|) sqrt(Y_j)(1+|j|)w_j. (12)

For two bands j,j', the polarized classwise Schur estimate (3)-(4) uses max(Y_j,Y_j') and bounds their inner product in angular L2 by C_K(1+max(Y_j,Y_j')/R)||b^(j)||_2||b^(j')||_2. Summing ALL ordered pairs (j,j') converges absolutely by Gaussian decay and yields, for X>=1,

    sum_l p_R(l-l0)|A_(t,l)^c(X)|^2
           <<_(K,Q,c) (1+|t|)^2 [X+X^2/R].                (13)

For 0<X<1, total absolute ideal counting and the right Gaussian tail give |A|<<_A X^A for every fixed A, uniformly in t and l. Thus that interval contributes O(1) to (11); integrating (13) for 1<=X<=D proves (11). All norms, tail bands, and cross terms are present. Setting R=D and t=0 gives O_(K,Q,c)(log(3+D)) without a radial average. It does NOT single out l=0.

## 5. Rectangular all-fixed-order theorem

Let k>=1 be fixed, X_i>=2, T=prod_(i=1)^k X_i. Let a_i(I) be ANY ideal coefficients supported in X_i/2<NI<=X_i and with |a_i(I)|<=d_(v_i)(I), where v_i>=1 are fixed integers, d_v the v-fold ideal divisor coefficient. Define F_i(l)=sum_I a_i(I)Psi(I)^l. All polynomial phases e(P_i(NI)), independent norm twists (NI)^(it_i), fixed angular-free Hecke characters and individually capped full L/reciprocal product coefficients fit this hypothesis without any loss of uniformity in phase coefficients.

**Theorem C (rectangular moment).** For every epsilon>0,

    sum_l p_R(l-l0) |prod_(i=1)^k F_i(l)|^2
        <<_(K,k,v_i,epsilon) T^(1+epsilon)(1+T/R).         (14)

In particular for a_i(I)=mu_K^S(I)(NI)^(it)e(P(NI)) and all X_i=X,

    sum_l p_R(l-l0)|F_l(X)|^(2k)
        <<_(K,k,epsilon) X^(k+epsilon)(1+X^k/R),          (15)

uniformly in real polynomial coefficients at EVERY fixed polynomial degree (indeed for arbitrary per-ideal unit phases), all l0, t and R.

Proof: expand the product as a Dirichlet convolution C(I) of the k separately capped columns. Every tuple of factors has product norm NI<=T and
|C(I)|<=d_V(I) with V=sum_i v_i, since d_(v_1)*...*d_(v_k)=d_V for ideals. The classical fixed-order divisor estimate gives d_V(I)<<_(K,V,epsilon)(NI)^epsilon. Collect by rational-primitive J:

    prod_i F_i(l)=sum_(NJ<=T) B_J Psi(J)^l,
    B_J=sum_(a<=sqrt(T/NJ)) C((a)J).                      (16)

Since Psi((a))=1 and every |C((a)J)|<<T^epsilon, one has |B_J|<<T^epsilon sqrt(T/NJ). By (5),

    sum_J |B_J|^2 <<_(K,V,epsilon) T^(1+epsilon).          (17)

The classwise packing estimate (4), now at Y=T, proves (14). It does NOT use cancellation of Mobius signs: that is why it works uniformly under arbitrary polynomial phases, and why it does not improve the fixed principal source.

For COMPLETE individually Gaussian-weighted columns with X_i>=2 and fixed c_i, partition each norm into all dyadic bands and apply (14) to every ordered k-tuple of bands. The L2 angular norm obeys Minkowski's inequality. The envelope for band j_i is exp(-c j_i^2+C|j_i|), and its cap increases by at most 2^(j_i+1); hence the sum of all k-dimensional bands is bounded by a convergent product of Gaussian series. After squaring,

    sum_l p_R(l-l0)|prod_i sum_I a_i(I)W_(c_i)(NI/X_i)Psi(I)^l|^2
          << T^(1+epsilon)(1+T/R).                        (18)

Here unweighted a_i(I) may be any of the divisor-bounded sequences just described; there is no compact truncation of W. For one repeated Gaussian column and D>=2, its higher critical energy is

    sum_l p_R(l-l0) integral_0^D |A_l^c(X)|^(2k) dX/X^(k+1)
             <<_(K,k,c,epsilon) D^epsilon(1+D^k/R).       (19)

For X<1 the absolute Gaussian source is O_A(X^A) and its contribution converges. For 1<=X<=D insert (18) and integrate. The original k=1 signed result (11) is logarithmically sharper than this general divisor estimate.

## 6. Which theorem is still missing?

At large resolution R about X^k, (15) gives the natural averaged size X^k up to subpowers, for every fixed k. But p_R(0)^(-1) asymptotic to sqrt(2pi)R. Positivity at the single principal l=0 yields at best

    |A_0(X)|^(2k) << X^(k+epsilon)(R+X^k).                (20)

For any R>=1, minimizing the right side still gives |A_0(X)|<<X^(1+epsilon): no improvement over the elementary O(X) bound. Increasing fixed k cannot remove the factor X^k introduced by angular localization. The same observation persists for the full Gaussian.

To get RH from this family would require a NEW signed, fixed-member extraction that cancels the off-diagonal terms **before** the Schur/absolute-value step. The exact arithmetic signs and that target are written in SIGNED_DETERMINANT.md. This is not hidden in an arbitrary high moment or in polynomial-phase orthogonality.
