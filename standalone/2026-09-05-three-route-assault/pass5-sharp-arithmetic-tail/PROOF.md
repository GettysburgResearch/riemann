# A sharp, growing-degree arithmetic-tail theorem

**Status:** PROPOSED COMPLETE COMPONENT PROOFS; independent mathematical review required.
**Scope:** the actual Laguerre/Mobius source of PR #793 and an explicit same-support positive control. No RH proof or new signed-cancellation upper bound is claimed.
**Parent:** GettysburgResearch/riemann PR #793, `6ebbe5efe6430584736649b87495af2be073f693`.
**What changes:** the growing-degree omitted-tail requirement in pass4/MOBIUS_FALSE_CONVERGENCE.md is discharged at a specified exponential cutoff. The optimal universal exponential cutoff is determined, including its critical boundary and the separate Gaussian transition of the countercontrol.
**Smallest remaining gap:** subexponential growth of the full signed energy, equivalently the completely specified finite energy in Theorem AT-2. Tail accuracy is not a sign estimate.

All statement labels below are local. Standard Laguerre generating functions, the Laguerre modulus bound, Cauchy estimates, saddle-point integration, and the characteristic-function continuity theorem are credited. No external novelty claim is made.

## 1. Definitions and normalization

Let q=67, and put

    w_q(k)=mu(k)^2 1_(q does not divide k),
    mu_q(k)=mu(k) 1_(q does not divide k),
    delta_q=1/[zeta(2)(1+1/q)]=201/(34 pi^2).

For any fixed sequence of complex numbers |b_k|<=1 define

    a_n(b)=sum_(k>=1) b_k k^(-3/2) L_n(2log k),
    a_n^(X)(b)=sum_(k<=X) b_k k^(-3/2) L_n(2log k).

The infinite sum is absolutely convergent for each fixed n; no assertion of uniformity in n follows just from that fact. An outer-horizon cutoff X is the SAME for all degrees 0,...,N. The intended source is b=mu_q. Write

    E_N=sum_(n=0)^N |a_n(mu_q)|^2,
    E_N^(X)=sum_(n=0)^N |a_n^(X)(mu_q)|^2.

The ordinary Laguerre convention is

    L_n(t)=sum_(j=0)^n binom(n,j)(-t)^j/j!,
    sum_(n>=0) L_n(t)z^n=(1-z)^(-1)exp(-tz/(1-z)).       (1)

We will separately use the classical bound |L_n(t)|<=exp(t/2) for t>=0 (DLMF 18.14.8, alpha=0). It is used only in the Gaussian-transition proof, not in the uniform tail estimate.

## 2. AT-1: a fully explicit, unconditional vector-tail bound

For any 0<p<1/3 put

    alpha(p)=(1-3p)/[2(1+p)]>0.

For every integer X>=1, N>=0, and every |b_k|<=1,

    || (a_n(b)-a_n^(X)(b))_(0<=n<=N) ||_2
      <= X^(-alpha) p^(-N)
           /[alpha(1-p)sqrt(1-p^2)].                    (2)

This estimate includes the intended Mobius source, with no use of its signs, PNT, a zero table, or RH.

### Proof

On |z|=p, elementary algebra gives

    Re[-z/(1-z)] <= p/(1+p).

Cauchy's formula applied to (1) therefore gives, for every t>=0,

    |L_n(t)| <= p^(-n)/(1-p) exp(tp/(1+p)).              (3)

For integer X, monotone integral comparison gives

    sum_(k>X) k^(-1-alpha) <= X^(-alpha)/alpha.

Since -3/2+2p/(1+p)=-1-alpha, the nth coefficient tail is at most

    X^(-alpha) p^(-n)/[alpha(1-p)].

Square, sum the finite degree range, and bound the geometric sum by
p^(-2N)/(1-p^2). This proves (2). All sums estimated here are absolute, so there is no unproved exchange of conditional arithmetic series. QED.

A convenient entirely predetermined choice is

    p=1/11, alpha=1/3, X_N=1728^N=12^(3N), N>=1.

The exact rational inequality

    [(33/10)^2/(1-1/121)] < (10/3)^2

then proves the clean bound

    || (a_n(b)-a_n^(X_N)(b))_(0<=n<=N) ||_2
          < (10/3)(11/12)^N.                            (4)

There is no factor sqrt(N) in (4); the degree dependence was summed geometrically before estimating.

## 3. AT-2: finite records with no hidden arithmetic tail

The reverse triangle inequality and (4) give

    |sqrt(E_N)-sqrt(E_N^(1728^N))|
           < (10/3)(11/12)^N.                           (5)

Consequently the following statement is equivalent to the existing RH endpoint:

    For every epsilon>0 there is C_epsilon<infinity such that
    E_N^(1728^N) <= C_epsilon exp(epsilon N), every N>=1. (6)

For clarity, this equivalence does NOT prove (6).

Here is a self-contained check of the terminal implication. Initially for |z|<1/3, absolute convergence and (1) give

    A(z)=sum_(n>=0)a_n(mu_q)z^n
        =1/[(1-z)zeta(s(z))(1-q^(-s(z)))],
    s(z)=1/2+(1+z)/(1-z).                               (7)

If E_N is subexponential for every epsilon, its individual coefficients have radius of convergence at least one. The right side of (7), continued meromorphically to the disk, must then be holomorphic. The Cayley map s sends the disk onto Re s>1/2; its finite Euler factor does not vanish there. A zeta zero in that half-plane would give a nonremovable pole. The functional equation therefore gives RH. Conversely RH makes (7) holomorphic throughout the disk, and Cauchy's coefficient bounds on every smaller circle give the asserted subexponential energy. The exponentially small norm difference (5) transfers both directions to (6).

If a computed finite vector has numerical Euclidean error at most eta_N, its distance from the infinite coefficient vector is at most

    eta_N+(10/3)(11/12)^N.                               (8)

Arithmetic evaluation error is not silently absorbed into the analytic tail. No sums through 1728^N at growing N were executed here. This cutoff is exponential and is not advertised as computationally cheap.

The earlier arbitrary-sign envelope E_N^(X)<=4X(N+1) becomes exponential at this cutoff and proves no cancellation. The positive squarefree countercontrol has root growth 3 even in these finite records: the erroneous automatic pass from subexponential cutoffs is gone, not the original signed estimate.

## 4. Squarefree counting with a complete elementary remainder

Let W_q(x)=sum_(k<=x) w_q(k). For all x>=1,

    W_q(x)=delta_q x+R_q(x), |R_q(x)|<=4sqrt(x).          (9)

Indeed mu(k)^2=sum_(d^2|k)mu(d), and q not dividing k implies q not dividing d. Thus

    W_q(x)=sum_(d<=sqrt(x), q not dividing d)mu(d)
       [floor(x/d^2)-floor(x/(q d^2))].                 (10)

The floor errors total at most 2sqrt(x). Replacing the remaining finite d-sum by the infinite sum costs at most 2sqrt(x), since sum_(d>sqrt(x))d^-2<=2/sqrt(x). Its infinite Euler product is delta_q. This proves (9), including the stated uniform constant. This is elementary squarefree density, not a use of PNT or square-root cancellation in the signed Mobius sum.

Define the positive-control tail and its continuous comparison by

    T_n^+(X)=sum_(k>X) w_q(k) k^(-3/2)L_n(2log k),
    I_n(U)=integral_U^infinity exp(-u/2)L_n(2u)du.

For any 0<p<1, set beta(p)=(1-p)/(1+p)>0 and

    K(p)=4/(1-p)
       +(4/beta)[3/(2(1-p))+2p/(1-p)^2].

Then, for real X>=1,

    |T_n^+(X)-delta_q I_n(log X)|
        <= K(p)p^(-n) X^(-beta(p)).                    (11)

### Proof of the uniform arithmetic transfer

Use Stieltjes integration by parts on (X,infinity), retaining the lower boundary -R_q(X)g_n(X), with

    g_n(x)=x^(-3/2)L_n(2log x).

Besides (3), differentiating (1) and using the same circle gives

    |L_n'(t)| <= p^(1-n)/(1-p)^2 exp(tp/(1+p)).

Since

    g_n'(x)=x^(-5/2)[-(3/2)L_n(2log x)+2L_n'(2log x)],

(9) bounds the boundary by 4p^(-n)X^(-beta)/(1-p). Integration of the derivative term gives the second term of K(p). The upper boundary vanishes at each degree. This proves (11), with no degree-dependent hidden constant. At p=1/3 the constant is exactly K(1/3)=36 and beta=1/2. QED.

## 5. AT-3: the countercontrol crosses at log X=(8/3)n

The exact integral in (1) gives

    sum_(n>=0)I_n(U)z^n
       =2/(1+3z) exp[-U(1+3z)/(2(1-z))].               (12)

At U=0, I_n(0)=2(-3)^n. The normalized real SIGNED measure

    dnu_n(u)=(-1)^n exp(-u/2)L_n(2u)du/(2*3^n), u>=0, (13)

has total mass one. It is not asserted to be a probability measure at finite n.

### Negligibility of its negative part

The Laguerre recurrence implies that (-1)^j L_j(t)>0 for t>=4n and 0<=j<=n. One can prove this directly without a root-location theorem. Put v_j=(-1)^jL_j(t). Then v_0=1, v_1=t-1, and

    v_j/v_(j-1)=(t-2j+1)/j-[(j-1)/j]/(v_(j-1)/v_(j-2)).

Induction gives v_j/v_(j-1)>=1 for j<=n, since t>=4n. Thus the negative part of (13) is supported in [0,2n]. The imported Laguerre modulus bound yields

    ||(nu_n)_-|| <= (1/(2*3^n))integral_0^(2n)exp(u/2)du
                 <(e/3)^n ->0.                        (14)

Normalizing its positive part produces probability measures whose total variation distance from nu_n is at most twice this bound.

### The central limit calculation

For t near zero the exact exponential transform is

    integral exp(tu)dnu_n(u)
        =(1+2t/3)^n(1-2t)^(-n-1).                     (15)

Its first two cumulants are

    mean=(8/3)n+2, variance=(32/9)n+4.                 (16)

For the standardized coordinate (u-(8/3)n)/sqrt((32/9)n), substituting imaginary t in (15) and expanding the logarithm gives limiting characteristic function exp(-t^2/2). By (14) and the probability characteristic-function continuity theorem, the standardized signed measures have the same normal limit. No numerical or uniform Berry--Esseen rate is claimed.

Let Phi be the standard normal distribution function, fix real z, and set

    U_n=(8/3)n+z sqrt((32/9)n), X_n=exp(U_n).

Then (11), with p=1/3, has relative error at most a constant times exp(-U_n/2) after division by 3^n. Consequently

    T_n^+(X_n)/[2delta_q(-3)^n] -> 1-Phi(z).          (17)

The parent's positive-source generating function, or a direct Euler-product calculation, gives

    a_n(w_q)=2delta_q(-3)^n+O_r(r^(-n)), 1/3<r<1.      (18)

For completeness, its generating function is

    zeta(s(z))/[(1-z)zeta(2s(z))(1+q^(-s(z)))].

In the open disk its only pole is z=-1/3, with principal part 2delta_q/(1+3z); subtracting that principal part proves (18) by Cauchy's estimate. No zeta zeros are assumed absent outside the Euler zero-free region needed for zeta(2s).

Subtracting (17) from (18) gives the retained finite fraction:

    a_n^(X_n)(w_q)/[2delta_q(-3)^n] -> Phi(z).         (19)

In particular a cutoff X=exp(cn) misses asymptotically the entire 3^n signal if c<8/3, half if c=8/3, and a vanishing FRACTION if c>8/3. The last assertion is only relative to 3^n; it does not mean the absolute omitted tail tends to zero. That is a different threshold, proved next.

For c<8/3 or c>8/3 the assertions follow from tightness of the normal limit when the standardized endpoint tends to minus or plus infinity. If an endpoint lies in the low interval containing negative mass, (14) still controls the discrepancy. For c<=2, the elementary finite-sum bound |a_n^(exp(cn))(w_q)|<=2exp(cn/2) and (18) also give the missing-signal assertion directly.

## 6. AT-4: exact large-deviation tail and the optimal exponential cutoff

Fix c>8/3. There is a unique p=p(c) in (0,1/3) with

    c=(1+p)^2/(2p),
    p=c-1-sqrt(c(c-2)).

Set

    beta=(1-p)/(1+p),
    Psi(c)=-log p-c(1-3p)/[2(1+p)].                   (20)

Then the literal squarefree control satisfies

    T_n^+(exp(cn))
      ~ (-1)^n [2delta_q/((1-3p)sqrt(2pi beta n))]
                         exp(n Psi(c)).              (21)

This is a fixed-c asymptotic; it is NOT uniform as c decreases to 8/3. Its constants and the Gaussian transition cannot be interchanged without another uniform argument.

### Complete saddle proof for the continuous tail

Use (12) on z=-p exp(i theta). Cauchy's coefficient formula becomes

    (-1)^n I_n(cn)=p^(-n)/(2pi) integral_(-pi)^pi
      2/(1-3p exp(i theta))
      exp(n[-c/2+2cp exp(i theta)/(1+p exp(i theta))-i theta]) dtheta. (22)

The first derivative of the bracket vanishes at zero because 2cp/(1+p)^2=1. Its second derivative is -beta. Its real part has a unique maximum at zero: subtracting its value at theta from its value at zero gives

    2cp(1-p)(1-cos theta)
       /[(1+p)(1+2p cos theta+p^2)]
      >= beta(1-cos theta) >= (2beta/pi^2)theta^2.     (23)

The amplitude in (22) is bounded because p<1/3. On scaling theta=v/sqrt(n), Taylor expansion gives exp(-beta v^2/2), while (23) gives an integrable Gaussian majorant for all n. Dominated convergence, with the endpoints going to infinity, proves

    I_n(cn) ~ (-1)^n [2/((1-3p)sqrt(2pi beta n))] exp(n Psi(c)).

No large-degree Laguerre asymptotic is imported; this is a direct saddle evaluation of the exact integrated generating function.

The arithmetic error in (11), at the same p, is bounded by

    K(p) exp(n[-log p-c beta])
      =K(p) exp(n[Psi(c)-c/2]).                       (24)

It is exponentially smaller than the preceding main term, proving (21). In particular (21) uses the actual squarefree support and q-exclusion, not a continuous surrogate alone.

### The critical constant and what is sharp

Differentiating (20) at its saddle gives Psi'(c)=-alpha(p)<0. Also

    Psi(8/3+)=log 3, Psi(c)->-infinity as c->infinity.

Thus there is exactly one c_*>8/3 with Psi(c_*)=0. Equivalently p_* is the unique root in (0,1/3) of

    -log p-(1+p)(1-3p)/(4p)=0,
    c_*=(1+p_*)^2/(2p_*).                             (25)

The derivative of the left side is (1-p)(1-3p)/(4p^2)>0. The rational logarithm certificate in verify.py proves, without floating-point acceptance,

    7.17798836313058 < c_* < 7.17798836313060.          (26)

For the positive squarefree control, the absolute tail is exponentially large for 8/3<c<c_*, has order n^(-1/2) at c=c_*, and decreases exponentially for c>c_*. Thus c_* is the exact threshold for absolute approximation, not the different relative-signal threshold 8/3.

## 7. AT-5: the threshold is sharp for the entire coefficient vector

For fixed c>2 and N>=1 define a map from bounded sequences on the q-free squarefree support into C^(N+1):

    (T_(N,c)b)_n=sum_(k>exp(cN)) b_k k^(-3/2)L_n(2log k),
    0<=n<=N, |b_k|<=w_q(k).

The norm below means the supremum of the output Euclidean norm over this coefficient box. Since 2log k>2cN>4N, every row has the fixed sign (-1)^n. Therefore the SAME choice b=w_q simultaneously attains the absolute bound in every row:

    ||T_(N,c)||^2=sum_(n=0)^N |T_n^+(exp(cN))|^2.      (27)

There is no cancellation assumption in this operator norm.

The recurrence in Section 5 further gives, for t>=2cN and 1<=j<=N,

    (-1)^j L_j(t)/[(-1)^(j-1)L_(j-1)(t)] >= 2c-3>1.

It follows that, for 0<=j<=N,

    |T_(N-j)^+(exp(cN))| <= (2c-3)^(-j)|T_N^+(exp(cN))|. (28)

For c>8/3 and each fixed j, the saddle formula (21) with degree N-j and endpoint cN gives the sharper limiting ratio p(c)^j. To justify this without silently assuming uniformity, observe that cN/(N-j) stays in a compact neighborhood of c; the domination and Taylor remainders in (22)-(23) are uniform on that compact set. The derivative of the optimized exponent -n log p-U alpha(p) with respect to n at fixed U is -log p, so reducing n by j multiplies its leading exponential by p^j. The remaining prefactors converge to their unshifted values.

Now (28) dominates the squares by a fixed summable geometric sequence. Equations (21) and (27) therefore prove the full operator-norm asymptotic

    ||T_(N,c)||
      ~ [2delta_q/((1-3p)sqrt(2pi beta(1-p^2)))]
                              N^(-1/2) exp(N Psi(c)). (29)

In particular, at the OPTIMAL cutoff exp(c_* N) the vector-tail norm still tends to zero, of order N^(-1/2). For c>c_* it tends to zero exponentially; for 8/3<c<c_* it grows exponentially. For 2<c<=8/3, Section 5 makes its last coordinate exponential. For 0<c<=2, the same last-coordinate lower bound follows from (18) and the elementary finite-sum estimate. Thus among all fixed exponential schedules exp(cN), c_* is the exact threshold for universal vanishing arithmetic-vector error on this support. It is not proved to be the optimal cutoff for the PARTICULAR signed Mobius sequence, which may benefit from cancellation.

The clean schedule 1728^N in (4) has 3log 12>c_*, as expected. It trades optimality for a small explicit rational error certificate at every N.

## 8. The attempted RH closure, with the remaining step exposed

This pass resolves the omitted-tail question in the proposed finite Laguerre route. In particular, one cannot dismiss a finite-energy argument on the new schedule merely by pointing to an unbounded unknown arithmetic tail: (4)-(8) pay that tail uniformly, at all degrees in each record, and (29) identifies the sharp universal scale behind that choice.

It does NOT prove a subexponential upper bound for the retained signed finite energy. The most immediate closure attempt was to apply the parent all-degree diagonal estimate to that retained energy after using (5). That remains invalid: the positive squarefree control has the identical diagonal and still has exponential energy after the new accurately covered cutoff. The controlled tail prevents false acceptance; it does not create the Mobius cancellation that is needed for actual acceptance.

Routes 1 and 3 remain active. Their existing full-source moment and compression certificates are not changed. This tail theorem concerns integer-coefficient Laguerre truncation, NOT positivity of finite Euler cutoffs in those other routes, and it is not transferred to their operators without a separate exact map.

The exact remaining arithmetic proposition is (6), or an equivalent all-order full-source positivity theorem. No proof of (6), full positive xi determinant, full Hardy positivity, or RH has been obtained in this pass.
