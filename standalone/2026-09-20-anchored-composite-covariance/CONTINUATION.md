# SFC30: squarefree completion and sparse coprime-pair covariance

20 September 2026. Continuation AFTER publication of ACC29 at `e4498096eb9eeea7147e7128d89ef56fdd34fa0b`, draft PR #905.

**PROPOSED component proofs; independent mathematical review required. The full native high-composite estimate and RH remain OPEN.** This is a new source construction and an actual family of mixed-term norm estimates. It is not a claim that all composite covariance has been paid.

## 0. New conclusions

1. The reciprocal-balanced native completion can be chosen squarefree-supported, |c(n)|<=16, L<=2Y, with whole completion-tail innovation energy <=32F_Y. It preserves every native coefficient through Y and the strict Newton endpoint (Y+1)^2. Thus c*c is cubefree and all higher prime-valuation layers vanish, including completion layers.
2. Every nonzero composite amplitude has an exact conditional-square and coprime-pair expansion. Its complete algebraic square-amplitude sector has full physical energy <=648 K^4 H_L^6. This includes all prime and powerful modes AND a specified part of every remaining denominator.
3. For ANY symmetric partner graphs on the primitive coprime cofactors, with maximum degree Delta, the complete selected mixed component has full physical energy <=209952 Delta^2 K^4 H_L^8. In particular all pairs with 0<|u-v|<=G have cost O(G^2 K^4 H_L^8), uniformly in their magnitudes and common squarefree factor. Taking G polylogarithmic gives a polylogarithmic bound.
4. The NCG28 source-amplitude estimate survives the new completion with 16 replaced by 192. Its 4/3 exponent and window exponents survive, with new constants, and with all tail-activation corrections still required.

Here 'square-amplitude' means diagonal in the conditional divisibility amplitudes U_d, NOT a diagonal of the outer physical covariance matrix. Each selected function is summed BEFORE its norm is taken. All its cross-frequency covariance and its infinite physical tail are included.

## 1. A squarefree-supported completion with an actual energy budget

Let m(k)=sum_(n<=k)mu(n)/n, F_Y=sum_(k<=Y)m(k)^2, a=|m(Y)|. Retain c(n)=mu(n) for n<=Y. At successive SQUAREFREE integers n>Y, correct the reciprocal residual with coefficient of opposite sign and magnitude min(16,n*|residual|); skip nonsquarefree n. Stop when the residual is zero.

For Y>=256 this terminates at L<=2Y and

    sum_(k>Y)m_c(k)^2<=32 F_Y,
    J(c)<=33F_Y.                                       (S1)

The finite cases 2<=Y<=255 are checked by exact rational arithmetic in the supplied replay, which gives the same assertions. The analytic theorem for all Y>=256 does not depend on those finite checks. No assertion for arbitrary nonsquarefree source data is made.

### 1.1 Elementary squarefree count

A nonsquarefree integer is divisible by some p^2. In an interval of J integers contained in [1,Y+J], the union bound gives

    number squarefree >= J*(1-sum_p 1/p^2)-sqrt(Y+J).

The elementary bound sum_p 1/p^2<1/2 follows by majorizing odd primes by all odd integers and using

    1/4+1/9+1/25+1/49+1/14 < 1/2.

The term 1/14 bounds the tail over odd integers >=9 by the integral from 7 to infinity with spacing two. Thus the count is at least J/2-sqrt(Y+J).

Take

    J0=ceil(Ya/2+4sqrt(2Y)).

NCG28's elementary native bounds are a<=1 and Ya^3<=9F_Y. For Y>=256, J0<=Y. Since J0>=4sqrt(2Y), there are at least J0/4 squarefree indices in (Y,Y+J0]. Each full correction has reciprocal capacity >=16/(2Y), so total capacity is >=2J0/Y>=a. The algorithm therefore terminates by Y+J0, with no change to the native prefix.

The reciprocal residual decreases monotonically in absolute value and never exceeds a. Hence

    tail energy <=a^2 J0
       <=(1/2)Ya^3+4sqrt(2Y)a^2+a^2
       <=32F_Y.

For the last line use F_Y>=1, a^2<=(9F_Y/Y)^(2/3), 9^(1/3)<21/10, and 4sqrt(2)<6. The resulting constant is less than 9/2+6*(21/10)^2+1=799/25<32. These deliberately conservative constants are not optimized.

### 1.2 The native endpoint is unchanged

Put v=2c-1*c*c and e=delta-1*c. Since c agrees with mu through Y, e vanishes below Y+1, and

    mu-v=mu*e*e.

Therefore v(n)=mu(n) for every n<(Y+1)^2. This also proves that changing from PCR26's consecutive correction to the squarefree correction changes none of the target native coefficients. It DOES change the spectral components, so this is not a relabeling of previous numerical sector measurements.

### 1.3 NCG28's source-energy input survives

For squarefree d, the native prefix contribution is mu(d)m_d(Y/d)/d; prime deletion and the cubic point bound give the inherited ceiling

    18^(1/3)(F_Y/Y)^(1/3)d^(-2/3)G(d),
    G(d)=product_(p|d)(1-p^(-2/3))^(-1).

The squarefree correction lies inside a consecutive interval of length <=J0 even though some indices are skipped. Its absolute contribution to U_d is at most

    (16/Y)(J0/d+1)
      <=8a/d+64sqrt(2)/(d sqrt(Y))+32/Y.

For d<=L<=2Y, comparison with (F_Y/Y)^(1/3)d^(-2/3), using F_Y>=1, shows

    |U_d|<=192(F_Y/Y)^(1/3)d^(-2/3)G(d).                (S2)

Indeed 18^(1/3)+8*9^(1/3)+64sqrt(2)+32*2^(2/3)<192. If d is not squarefree, U_d=0 for the entire new source. If d>L it is also zero. The same comparison works in the finite base whenever J<=J0; this is unnecessary for the asymptotic application, which uses Y>=256.

Thus NCG28's threshold-tensor, mean-square majorant and large-sieve proofs can be rerun with amplitude constant 192 in place of 16. The completion budget is now 33F_Y instead of 2F_Y. Neither constant substitution changes the source exponent 4/3 or the powers 10/11 and 16/11 of its admissible windows.

## 2. Exact dilation and a sharper kernel norm

Continue to write r_q=R_q-R_q(0), ||f||_ph^2=sum_(k>=1)f(k)^2/[k(k+1)]. Define

    w(n)=product_(p|n)(1+p^(-1/2)), w(1)=1.

For f(0)=0 and integer a>=1, let (D_a f)(k)=f(floor(k/a)). Grouping the exact weight over k=aj,...,a(j+1)-1 proves

    ||D_a f||_ph^2=(1/a)||f||_ph^2.                    (S3)

For q>=2, d=rad(q), m=q/d, divisor inversion gives

    r_q(k)=m r_d(floor(k/m)).                          (S4)

Also ||k mod e||_ph^2<=2e. Applying Minkowski to the divisor expansion of r_q gives the useful uniform estimate

    ||r_q||_ph<=sqrt(2q) w(q).                         (S5)

Nonzero terms correspond to q/e with e squarefree, so the sum of square roots factors as w(q). This is sharper than replacing every divisor by the largest denominator.

Two harmonic estimates used below are

    sum_(n<=L)w(n)/n<=3H_L,
    sum_(n<=L)w(n)^2/n<=18H_L.                         (S6)

For the second, expand w(n)^2 over squarefree divisors with local coefficient g(p)=2/sqrt(p)+1/p. Then the harmonic sum is at most H_L times

    product_p(1+2/p^(3/2)+1/p^2)
       <=zeta(3/2)^2 zeta(2)<=18.

The first is the analogous bound product_p(1+p^(-3/2))<=zeta(3/2)<=3. Only absolutely convergent positive Euler products are used.

## 3. Composite amplitudes become conditional squares

From now on c is ANY finite real, reciprocal-balanced, squarefree-supported source with |c(n)|<=K, support <=L. The new native completion is one such source, with K=16.

Since z=c*c is cubefree, B_q=0 if q has any prime exponent >=3. Every remaining q uniquely has the form

    q=a^2 b, a and b squarefree, gcd(a,b)=1.

The condition a^2|rs forces a|r and a|s because the source factors are squarefree. Inclusion-exclusion on b therefore gives

    B_(a^2 b)=sum_(e|b)mu(e)
                    [sum_(f|e)mu(f)U_(af)]^2.          (S7)

Expanding and using the divisor sum of mu gives an equivalent ordered-pair formula

    B_(a^2 b)=mu(b)*sum_(f,g|b,lcm(f,g)=b)
                         mu(f)mu(g)U_(af)U_(ag).       (S8)

All diagonal f=g terms cancel except f=g=b. Hence their complete contribution is

    mu(b)U_(ab)^2.                                    (S9)

For example, B_(a^2)=U_a^2 and

    B_(a^2 p)=2U_a U_(ap)-U_(ap)^2, gcd(a,p)=1.

At a=1 balance gives the prime negative square; at a>1 the linear term is real and must be retained. For two singleton primes this contains the mixed-square identity in ACC29, not a sign-definite extension of it.

## 4. A full-denominator square-amplitude sector is paid

Define

    D(k)=sum_(a,b squarefree,(a,b)=1,a^2 b>=2)
                            mu(b)U_(ab)^2 r_(a^2 b)(k).

The sum is finite because U_(ab)=0 for ab>L. Group by d=ab. For d>=2 squarefree,

    K_(d;1)(k)=sum_(a|d)mu(d/a)r_(ad)(k),
    D(k)=sum_(d squarefree,d>=2)U_d^2 K_(d;1)(k).        (S10)

There is no q=1 issue: the excluded d=1 coefficient would be U_1^2=0. Equations (S3)-(S5) give

    ||K_(d;1)||_ph<=sqrt(2)d w(d)^2.

Since |U_d|<=KH_L/d, (S6) and Minkowski yield

    ||D||_ph<=18sqrt(2)K^2 H_L^3,
    ||D||_ph^2<=648K^4 H_L^6.                         (S11)

This includes a prescribed square-amplitude contribution at EVERY surviving denominator, however many large singleton primes it contains. It is not only a bound for prime powers. It is also not the whole composite coefficient: the off-diagonal pairs in (S8) remain.

As a narrower corollary, the entire powerful-denominator function consists only of q=d^2 with B_(d^2)=U_d^2. Using the first bound in (S6),

    ||sum_(d>=2,squarefree)U_d^2 r_(d^2)||_ph^2
       <=18K^4 H_L^6.                                (S12)

This improves ACC29's general powerful-sector logarithmic bound for this NEW source class. It does not retroactively change the old completion.

## 5. Disjoint common-factor regrouping of ALL remaining mixed terms

In (S8) write h=gcd(f,g), f=hu, g=hv. Then h,u,v are pairwise coprime squarefree integers, b=huv, and the sign is mu(h). The diagonal corresponds exactly to u=v=1. Put d=ah and sum over all a|d. This is a bijective reindexing, so there is no repeated choice of a pivot prime.

For d squarefree, b>1 squarefree, gcd(d,b)=1, set

    K_(d;b)(k)=sum_(a|d)mu(d/a)r_(adb)(k).              (S13)

Then the COMPLETE original function P=sum_(q>=2)B_q r_q is exactly

    P(k)=D(k)+O(k),
    O(k)=sum_(d,u,v pairwise coprime squarefree, u!=v)
                  U_(du)U_(dv)K_(d;uv)(k).            (S14)

The pair (u,v) is ORDERED. Thus (u,v) and (v,u) produce the factor two present in (S8). The bounds du,dv<=L make the sum finite; equivalently zero coefficients can be retained. These are primitive coprime cofactors of the DIVISIBILITY INDICES, not a statement that the original source integers themselves are coprime.

Since rad(adb)=db, (S3)-(S5) give

    ||K_(d;b)||_ph
       <=sqrt(2)d sqrt(b) w(d)^2 w(b).                 (S15)

An exact operator interpretation is available. With F(k)=k,

    K_(d;b)=mu(b)*product_(p|d)(I-pD_p)^2
                         *product_(p|b)(I-pD_p)F.

This is a pointwise polynomial identity; F itself has infinite physical norm, so no norm estimate is applied to F before the differences. Products commute because D_a D_b=D_(ab). No contraction of an Euler product on the critical line is assumed.

## 6. A sparse-partner theorem for genuine mixed terms

For each d let E_d be an undirected, loop-free graph on the possible cofactor vertices 1,...,floor(L/d). Retain only coprime squarefree vertices u,v also coprime to d. Suppose maximum degree is at most Delta, uniformly in d. Let O_E denote (S14) restricted to BOTH ordered orientations of graph edges.

Then

    ||O_E||_ph<=324sqrt(2)Delta K^2 H_L^4,
    ||O_E||_ph^2<=209952 Delta^2 K^4 H_L^8.             (S16)

Proof: by (S15), the elementary amplitude bound, and Minkowski,

    ||O_E||_ph
      <=sqrt(2)K^2 H_L^2 sum_d [w(d)^2/d]
            *sum_((u,v) ordered edge of E_d)
                          w(u)w(v)/sqrt(uv).

For x_u=w(u)/sqrt(u), the graph inequality 2x_u x_v<=x_u^2+x_v^2 gives

    sum_((u,v) ordered edge)x_u x_v
        <=Delta sum_u x_u^2<=18Delta H_L.

Apply (S6) once more to the outer d sum. All constraints dropped in these estimates remove only nonnegative terms. This proves (S16) for arbitrary signs in the original source. No covariance term is declared orthogonal or negative.

### A concrete new family: neighboring coprime cofactors

Choose E_d to contain all pairs with 0<|u-v|<=G. Its degree is at most 2G. Thus the ENTIRE sector, including unbounded cofactor magnitudes as L increases, has

    ||O_gap||_ph^2<=839808 G^2 K^4 H_L^8.              (S17)

For G=floor((log L)^A), with fixed A>=0, this is polylogarithmic. More generally any cutoff- or source-dependent bounded-degree partner selection is covered; the theorem does not require the same graph for every d.

One can replace Delta by a uniform spectral norm bound for the nonnegative adjacency matrices. This is a graph quadratic-form inequality, not a claimed spectral bound on the full arithmetic covariance operator.

The diagonal and graph-sector estimates are full physical norms. The exact tail map T of ACC29/NCG28 is a contraction, so the same upper bounds hold for their transformed innovation components, including the entire future.

## 7. What this does and does not buy for the native problem

For the squarefree completion, all prime exponents >=3 disappear exactly; every prime and powerful mode is in D; and a specified square-amplitude part of every mixed denominator is also in D. The graph theorem additionally pays genuine products U_(du)U_(dv), not just squares.

With O=O_E+O_rem, on the native interval Y<k<(Y+1)^2,

    m(k)=2m_c(k)-TD(k)-TO_E(k)-TO_rem(k).               (S18)

Consequently, with B=(Y+1)^2-1,

    sqrt(F_B-F_Y)
      <=2sqrt(33F_Y)+18sqrt(2)K^2 H_L^3
              +324sqrt(2)Delta K^2 H_L^4
              +||TO_rem||_(ell2 on Y<k<=B).           (S19)

This keeps the actual completion, every selected mixed term, and the native endpoint. No infinite-future bound for O_rem is required.

The remaining coefficient at each denominator is a SUBSUM of the exact threshold-pair expansion (S8). Its absolute majorant is therefore bounded by the same positive threshold tensor as NCG28, with source constant 192 from (S2). Accordingly its fixed/moving LOW-denominator part still admits NCG28's F_Y^(4/3) estimate with new constants. Implement the moving split in the remaining UNANCHORED coefficient representation and retain its future-activation correction. The fixed paid D and O_E have the same transforms whether expressed anchored or unanchored, because T annihilates constants. This yields an exact compatible split into completion, paid fixed components, moving-low remainder, and high remainder.

**Still unproved:** the source-specific restricted transformed HIGH remainder after those subtractions. The graph left after removing a polylogarithmic gap band can have large degree. Taking Delta of order L makes (S16) polynomial, not subpower. Covering the whole graph by many matchings does not remove that cost. No general cancellation estimate for those many remaining partners has been obtained here.

The next arithmetic question is not whether a few isolated denominators have small self-energy, but how the native identities constrain these dense partner sums. A useful source-sensitive, but not yet uniformly small, upper envelope follows before replacing U by KH/d:

    ||O_E||_ph<=sqrt(2) sum_d d*w(d)^2 * y_d^T A_d y_d,
    y_d(u)=sqrt(u)w(u)|U_(du)|.

This is computable from the short source, but evaluating it is not a proof that it is subquadratic in F_Y. The signs in the exact (S14) should be retained in any further arithmetic attack.

## 8. Executed validation and limitations

Run, from this directory:

    python verify.py
    python -O verify.py
    python verify_continuation.py
    python -O verify_continuation.py
    python verify_continuation.py --mutate  # expected NONZERO exit

ACC29 ordinary and optimized runs each passed 96,190 exact comparisons. The final SFC30 ordinary and optimized runs each passed 179,941 exact comparisons on 82 balanced squarefree sources, the exact finite completion base Y=2,...,255, all native Newton coefficients for Y=3,7,15,31,63,95,255, extra completion examples Y=256,512,1023,2047, and independent integer-point kernel regroupings. The largest complete native reconstruction endpoint is 65,535. These are comparison counts, not independent test methods or independent proof verifications.

The SFC30 checker independently constructs c*c and B_q, then checks the conditional-square expansion, lcm expansion, disjoint common-factor regrouping, cubefree support, full physical decomposition on small sources, and completion energy. All accepting comparisons use exact integers/Fractions. Descriptive completion-energy ratios in JSON are floats; their inequalities and the finite-base maximum are checked exactly. The base maximum tail/F is exactly 1/46 at Y=3, much smaller than the theorem's conservative 32; no improved asymptotic constant is inferred.

A deliberate regrouping-sign mutation initially escaped a weak fixture containing only prime support: those fixtures did not exercise a shared-prime mixed channel. The fixture was strengthened to include 6 and a separate source involving 6,10,15,30. The FINAL mutation run fails as required, with 19/18 versus 5/18 for a regrouped coefficient. This is a disclosed test-coverage correction, not a suppressed failed mathematical identity. One final actual CLI negative control was run; no broad mutation campaign is claimed.

No whole-repository validator, remote CI, Lean build, external proof review, interval certificate of infinite energy, or full predecessor replay is claimed. The analytic norm proofs are not certified by the finite tests. The squarefree completion is new to this packet; its results must not be attributed to the previous cap-3 completion without rerunning the relevant derivations.

## 9. Attribution and research status

The source Newton identity and divisor-inverse machinery are classical; ACC29 records Huxley--Watt and the repository predecessors. Squarefree union bounds, positive Euler-product majorants, inclusion-exclusion, dilation cell grouping and graph quadratic-form inequalities are elementary tools. The proposed contribution here is their exact composition into a squarefree native completion and full-norm conditional-amplitude sector bounds. External novelty is not established. All infinite estimates are proposed manuscript results awaiting independent review; the remaining native high-composite estimate is explicitly open.
