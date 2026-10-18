# Joint dual moments for a longer, source-preserving mollifier

Status: PROPOSED analytic deductions, requiring independent mathematical review.
Scope: the fixed n-th-order Hecke family, n>=6, full power-free ideal prefixes.
The main estimate concerns the finite, uncapped relative inversion error LM-1.
The inverse-value consequence remains CAPPED. Neither theorem proves RH.

## 1. Source contracts, notation, and the main statement

Fix de Faveri's field F containing mu_n, n>=6, admissible fixed S, and all ray/generator choices. Let a range over ALL n-th-power-free exterior integral ideals of full norm Na<=U, U>=2. One fixed permitted finite-order S-supported twist psi may be included. Put

    L_a(s)=L_F^S(s,psi chi_a),
    M_A(s,a)=sum_(Ne<=A) mu_F(e) psi(e) chi_a(e) (Ne)^(-s).

Characters keep their original zeros at nonunits. Distinct ideals of equal norm are distinct. Constants may depend on the fixed field, S, ray data, twist, fixed moment orders, and compact height set. The finitely many inducing-principal rows are treated separately when using a functional equation for an entire L-function. They are included in the final prefix estimates. No field, growing-order, or critical-line uniformity is asserted.

The deep imported inequality is de Faveri Theorem 1.1, in the four-monomial form

    sum_(Na<=U)^flat |sum_(Nb<=V)^flat z_b chi_a(b)|^2
      << (UV)^epsilon K_n(U,V) sum_b |z_b|^2,
    K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).       (S)

BOTH indices are n-th-power-free. The other analytic input is the classical Hecke functional equation with its actual inducing conductor Q_a<<Na and fixed gamma types. The precise flat-cutoff/finite-S interface is the one reconstructed in #984, MOLLIFIED_APPROXIMATION.md, frozen at b6a29037a2be358294401d71d7305b0f402c2eea. We reconstruct the new norm argument below; we do not newly certify the deep sieve or all upstream character choices.

Fix s=3/4+it, with t in a fixed compact subset of R, and define

    a_n=2(n-3)/(3n-8),
    f_n=2(n^2-2n-2)/(n(3n-8)),
    A=X=U^(a_n).

**Theorem 1.** For every epsilon>0,

    sum_(Na<=U)^flat |L_a(s)M_A(s,a)-1|^2
                     << U^(f_n+epsilon).                (1)

In the actual sextic case,

    A=X=U^(3/5),              f_6=11/15.                 (2)

#984's stated balanced-cutoff theorem permits A<=U^(1/4) at this s, and at its longest stated length gives exponent 7/8. Thus (2) improves that displayed exponent by 17/120, while allowing a substantially longer mollifier. This is a comparison with the specified predecessor, not a literature-priority claim, not a new zero-free fraction, and not a claim to improve #979's zero-density exponent at 3/4. A zero contributes one to (1), which still permits exceptional members.

## 2. Complete-column polynomial lemma

Write

    k_n(v)=max(1,v,1-1/n+2v/n,2/n+(1-1/n)v).

If a common coefficient array on V<Nb<=2V is bounded by C (Nb)^(-u) times a fixed-order ideal divisor function, (S) gives

    sum_rows |sum_b z_b (psi chi_a)(b)|^2
            << C^2 (UV)^epsilon V^(1-2u) K_n(U,V).       (3)

To justify full columns, factor b=c e^n uniquely, c n-free. There is NO condition (c,e)=1. Precisely

    (psi chi_a)(c e^n)
       =psi(c)psi(e)^n chi_a(c) 1_((a,e)=1).

At fixed e the coefficient square mass is at most
C^2 V^(1-2u+epsilon)/(Ne)^n. Apply (S) with c-length V/(Ne)^n (or enlarge this length to V), keeping the row mask until the nonnegative square is formed. Minkowski in the row norm costs sum_e (Ne)^(-n/2+epsilon), which converges. Initial losses are chosen small enough for the requested final epsilon. The same argument works for conjugate characters. This is the established full-column adapter, not a new orthogonality assertion.

For any fixed positive integer r, expand M_A^r before applying (3). The coefficient on b is a complete ordered r-fold divisor sum, supported on Nb<=A^r and bounded by d_r(b)(Nb)^(-3/4). Thus

    sum_rows |M_A|^(2r)
       << U^epsilon max_(0<=v<=r log_U A) U^(k_n(v)-v/2). (4)

Fixed constant multiples of endpoints and logarithms are absorbed in epsilon. The unit term is retained. Since k_n(v)-v/2 is convex and is at most one at both endpoints v=0 and v=2 for n>=3,

    A^r<=U^2  ==>  sum_rows |M_A|^(2r)<<U^(1+epsilon).   (5)

In particular, 1/2<a_n<2/3 for n>=6, so A^3<U^2 and

                         sum_rows |M_A|^6<<U^(1+epsilon). (6)

This is a moment of the actual truncated polynomial, not a bound for its reciprocal. Shared-prime tuples and all n-th-power aliases are retained in (4).

## 3. Exact cancellation in the main polynomial

Choose one fixed smooth V_0 with V_0(y)=1 on 0<y<=1 and V_0(y)=0 on y>=2. Its Mellin transform has a simple pole of residue one at zero and is rapidly decreasing on fixed vertical lines away from zero. Set

    P_X(s,a)=sum_b (psi chi_a)(b)(Nb)^(-s)V_0(Nb/X).

For A<=X, multiplication by the literal mollifier gives EXACTLY

    P_X M_A-1
       =sum_(A<Nb<=2AX) (psi chi_a)(b)(Nb)^(-s) h_(A,X)(b),
    h_(A,X)(b)=sum_(e|b,Ne<=A) mu_F(e)V_0(Nb/(Ne X)).     (7)

Every nonunit coefficient through A vanishes: every divisor is present and every cutoff equals one. The unit coefficient is subtracted exactly. For all remaining b, |h_(A,X)(b)|<=C d_2(b). Neither a nonunit character value nor an endpoint is altered.

Apply (3) on every dyad in (7). At s=3/4+it the four bounds are

    U V^(-1/2),
    V^(1/2),
    U^(1-1/n) V^(2/n-1/2),
    U^(2/n) V^(1/2-1/n).                                (8)

For n>=6, the first and third decrease in V; the second and fourth increase. With A=X=U^a, the complete main-error exponent is therefore the maximum of

    1-a/2,  a,
    1-1/n+(2/n-1/2)a,
    2/n+(1-2/n)a.                                      (9)

At a=a_n, the last two coincide with f_n. Their margins over the first two are, respectively,

    f_n-(1-a_n/2)=(n-4)/(n(3n-8)),
    f_n-a_n=2(n-2)/(n(3n-8)).                            (10)

Both are positive. Consequently

                    sum_rows |P_X M_A-1|^2<<U^(f_n+epsilon). (11)

For n=6 the four exponents are 7/10, 3/5, 11/15, 11/15. This proof estimates the entire signed error AFTER the exact low-coefficient cancellation, not a selected off-diagonal sector.

## 4. Actual-conductor dual moments, including complete tails

For an inducing-nonprincipal row write L_a=P_X+R_X. For a primitive character, the exact functional-equation identity has the form

    R_X(s,a)=epsilon_a Q_a^(1/2-s)
      sum_c conjugate((psi chi_a)(c)) (Nc)^(s-1)
                                  V_s(Nc X/Q_a).        (12)

The weight V_s is defined by a complete Mellin integral, not by a hard truncation. It and any fixed number of logarithmic derivatives are bounded at small positive arguments and decay faster than any prescribed fixed power at infinity. These assertions follow by moving the Mellin line on either side of its zero pole, without crossing a gamma pole: initially move to a large negative line to apply the functional equation, and for small arguments move right by less than 1-Re(s), retaining the pole at zero. Gamma poles are to the right of that last line. Stirling and smooth Mellin decay control horizontal limits. Height constants are uniform on the fixed compact t set.

Retain the ACTUAL conductor by partitioning into Q<=Q_a<2Q, 1<=Q<<U. Fourier/Mellin separation of localized log Q and log Nc gives common coefficient arrays with an integrable Fourier norm; the finite list of gamma types is separated first. Root numbers are modulus-one row factors. This does not permit independently chosen coefficient arrays for each row.

Here is the exact cost for every FIXED r>=1. The effective dual length is L=Q/X. If L>=1, powering a localized polynomial r times and applying (3) to its complete product coefficients gives a 2r-th moment bound

    << U^epsilon Q^(-r/2) L^(r/2) K_n(U,L^r)
     = U^epsilon X^(-r/2) K_n(U,(Q/X)^r).                (13)

Indeed the product coefficient line is 1/4, not 3/4; its square mass has weight V^(1/2), and its product length is L^r. Lower dyads are summed by positive powers, while upper dyads receive arbitrarily rapid decay. One can first use finite sums, apply Minkowski in l^(2r), and pass to the full series using these summable bounds. The displayed Q cancellation occurs BEFORE replacing Q by U.

If L<1, all positive norm bands are on the rapidly decreasing side. For any fixed J>r/2, increasing the original profile decay if necessary gives

    sum_rows |R_X|^(2r)
       << U^(1+epsilon) Q^(-r/2) (Q/X)^J
       <= U^(1+epsilon) X^(-r/2).                       (14)

The last exponent difference is (J-r/2)log_U(Q/X)<=0. A subunit effective length is NOT declared an empty sum. All its terms are bounded by (14).

Combining the two cases, summing conductor dyads, and absorbing logarithms yields, for 1<=X<=U,

    sum_rows |R_X|^(2r)
       << U^epsilon X^(-r/2) K_n(U,(U/X)^r).             (15)

Fixed multiplicative constants in Q_a<<U change only constants. For the incomplete L-function, first expand the finite Euler polynomial at S. It gives fixed rescalings of X and fixed coefficients. In the dual, decompose each ideal into its S-part and exterior part. The S-part has absolute weight (Nc_S)^(-1/4); its geometric sum converges. Additional dilations only shorten L, and are covered by (13)-(14). Take Minkowski before the positive moment. This retains the actual S zeros and all S-supported tails. Exterior imprimitive factors are those in the pinned family contract; no new character with a different zero mask is substituted.

For X=U^(a_n), 1-a_n<1/2 and 1/2<2(1-a_n)<1. On these respective intervals k_n is 1 and 1-1/n+2v/n. Hence (15), for r=1 and r=2, gives

    sum_rows |R_X|^2 << U^(r_2+epsilon), r_2=1-a_n/2,
    sum_rows |R_X|^4 << U^(r_4+epsilon),
                     r_4=1+3/n-(1+4/n)a_n.             (16)

At n=6 these are U^(7/10+epsilon) and U^(1/2+epsilon).

## 5. The missing improvement over the pointwise-mollifier step

The dual in (12) has conjugate characters. Multiplying it into M_A as one same-character polynomial would be false. We instead use the three-factor Holder inequality

    sum_rows |M_A R_X|^2
       <= (sum_rows |M_A|^6)^(1/3)
          (sum_rows |R_X|^2)^(1/3)
          (sum_rows |R_X|^4)^(1/3).                     (17)

This is Holder applied to |M_A|^2, |R_X|^(2/3), |R_X|^(4/3). The exponents of |R_X| sum to two. It uses the same actual rows and needs no independence, no deletion of cross terms, and no fictitious identity chi(e)conj(chi(c))=chi(ec).

Equations (6), (16), and (17) give the dual-product exponent

    g_n=1+1/n-(1/2+4/(3n))a_n,
    f_n-g_n=2(n-6)/(3n(3n-8))>=0.                       (18)

At n=6 it is exactly (1+7/10+1/2)/3=11/15. This is stronger than the pointwise-M_A treatment in #984. The exploratory bound 7/9 from changing X alone is valid but superseded by (17).

Finally |LM_A-1|^2<=2|P_X M_A-1|^2+2|R_X M_A|^2. Finitely many principal rows contribute O(1+A^(1/2)) at fixed s, by ordinary ideal counting and the fixed L-value; this fits (1) since a_n/2<f_n. This proves Theorem 1 from the stated contracts.

## 6. An all-order capped inverse estimate with no deleted rows

This consequence does NOT use #984's zero-density theorem or its reciprocal-moment asymptotic. It is an upper bound, not an explicit Euler leading term.

First an additional length choice will be useful. For n>=6, 0<a<=1/2, take A=U^a and X=U^(3/4). Then

    sum_rows |LM_A-1|^2 << U^(1-a/2+epsilon).             (19)

The four main dyad exponents are bounded by 1-a/2: after subtracting this number their upper-endpoint differences are

    a-5/8,
    -1/n+2a/n,
    -5/8+5/(4n)+(1-1/n)a,

all nonpositive on the stated interval (the first is strictly negative; the third may vanish at n=6,a=1/2). The U V^-1/2 term gives equality. Also M_A^6 has total moment O(U^(1+epsilon)) because 3a<=3/2. At X=U^(3/4), (15) gives R_X second moment U^(5/8+epsilon) and fourth moment U^(1/4+epsilon). Equation (17) costs U^(5/8+epsilon), below (19). All previous tail and principal-row arguments remain valid.

Define

    theta_(n,k)=1-f_n,                     1<=k<=3;
    theta_(n,k)=1/k,                       k>=4.         (20)

For k<=3 use Theorem 1's A. Equation (6) and Holder imply sum|M_A|^(2k)<<U^(1+epsilon). For k>=4 choose A=U^(2/k); then (5) with r=k proves the same bound, while (19) has error exponent 1-1/k.

Let B_U={a:|L_a M_A-1|>1/2}. Markov applied to the corresponding relative-error estimate gives

                         #B_U<<U^(1-theta_(n,k)+epsilon). (21)

On its complement |L_a M_A|>=1/2, so L_a!=0 and |1/L_a|<=2|M_A|. On B_U impose a cap, without changing or discarding a row. For every T>=1,

    sum_(Na<=U)^flat min(|L_a(s)|^(-2k),T)
      << U^(1+epsilon) + T U^(1-theta_(n,k)+epsilon).     (22)

An actual zero is assigned T. Equivalently, the transfer follows from the pointwise inequality, valid for every pair of complex numbers L,M,

    min(|L|^(-2k),T) <= 2^(2k)|M|^(2k)+4T|LM-1|^2,       (22a)

with the same zero convention. This is proved by splitting at |LM-1|=1/2, and makes explicit that no exceptional row or its uncapped contribution has been silently removed. In particular,

    sum_(Na<=U)^flat min(|L_a(s)|^(-2k),U^theta_(n,k))
                            << U^(1+epsilon).           (23)

All orders k here are fixed, and constants may depend on k. At n=6, theta=4/15 for k=1,2,3, and theta=1/k for k>=4. The first three cases allow the reciprocal POWER cap U^(4/15), compared with U^(1/80) in #984's displayed sextic asymptotic. The larger-cap conclusion is ONLY an upper estimate; it does not retain that asymptotic's leading constant or power error. For k>=80 the cap 1/k is no larger than that earlier 1/80, so no all-k superiority is claimed.

For example the new full-prefix bound is

    sum_(Na<=U)^flat min(|L_a(3/4+it)|^(-2),U^(4/15))
                                 << U^(1+epsilon).      (24)

If psi is trivial and the identity representative is included, the principal member is literally among these rows. Unlike a dyadic conductor/norm annulus, this prefix does not automatically lose it as U grows.

## 7. Exactly why this does not finish RH

At an actual zero, LM_A-1=-1. Estimate (1) allows U^(f_n+epsilon) such rows; it does not force that number below one. In (23) a zero contributes only U^theta, while the upper bound is U^(1+epsilon). At n=6, theta=4/15<1, so even one persistent principal zero is compatible with every displayed bound. Letting k grow is not justified by fixed-k constants, and the caps in (20) do not approach a zero-excluding threshold anyway.

The reciprocal values are also not the finite-scale Gaussian Mobius source from #976/#983. Passing to that source still needs a legal full vertical contour and a bound for its complete exceptional contribution. No such bound follows from (23). This packet does not assert a new zero-free line, a principal square-root estimate, or an RH proof.

A useful LIMITED optimization check rules out squeezing more from the same main-polynomial envelope at 3/4. Let A=U^a, X=U^x, with 0<a<=x. The positive (S)-based dyad estimate always includes

    L_1=1-1/n-(n-4)a/(2n),
    L_2=2/n+(n-2)(a+x)/(2n)>=2/n+(n-2)a/n.

The positive weights 2(n-2)/(3n-8) and (n-4)/(3n-8) sum to one and cancel a in the weighted sum, leaving exactly f_n. Thus the maximum of THESE ESTIMATED MONOMIALS is >=f_n. Theorem 1 attains this bound while paying the full dual. This is not a lower bound for the actual arithmetic error: further progress must exploit cancellation in h_(A,X), a different cancellation-preserving cutoff, or a genuinely stronger mixed-family input rather than merely retune a,x in (8).

## 8. Validation boundary

The included checker reconstructs finite cutoff/divisor identities and literal finite-field root/nonunit algebra, checks the exact exponent formulas, small-conductor identities, the three-factor Holder inequality on finite rational fixtures, and both branches of the capped transfer. It does not certify infinite functional equations, contour moves, the imported sieve, or the family identification. No independent referee, proof-assistant verification, L-value census, or mathematical-priority claim is made.
