# Subexponential arithmetic cutoffs make even the wrong source look subexponential

Status: PROPOSED COMPLETE COMPONENT PROOFS; independent review required. No new Mobius cancellation bound and no RH proof.
Scope: the exact Laguerre coefficients from PR #793/pass3; any coefficients bounded by one; same outer cutoff for the finite energy. Local labels MF-1 through MF-3.

## 1. An unconditional all-cutoff bound

For |b_k|<=1 define

    a_n^(X)=sum_(k<=X)b_k k^-3/2 L_n(2log k),
    E_N^(X)=sum_(n=0)^N |a_n^(X)|^2.

The classical Laguerre inequality (DLMF 18.14.8 at alpha=0) says

    exp(-t/2)|L_n(t)|<=1, t>=0, n>=0.

Therefore for every finite X>=1 and N>=0,

    |a_n^(X)|<=sum_(k<=X)k^-1/2<=2sqrt X,
    E_N^(X)<=4X(N+1).                                    (MF1)

Consequently every schedule log X_N=o(N) satisfies

    limsup_N (E_N^(X_N))^(1/(2N))<=1.                     (MF2)

This holds for EVERY choice of signs, not specifically Mobius signs. If different cutoffs are used by degree, the same result holds with max_(n<=N)X_n. This is an upper-growth assertion, not an equality at one for arbitrary b_k (the zero source is an immediate counterexample to equality).

The target in the parent uses the infinite coefficients a_n, not a_n^(X_N). MF2 cannot discharge it without controlling the omitted tail uniformly in growing degree.

## 2. The existing same-support control quantifies the missed tail

Fix q=67 and take the positive squarefree source b_k=mu(k)^2 1_(q does not divide k). It has exactly the same support and squared weights as the intended signed source. For each fixed n the infinite sum converges absolutely.

Let delta_q=1/[zeta(2)(1+1/q)]. The generating germ is

    A_+(z)=sum_(n>=0)a_n^+ z^n
       =zeta(w(z))/[(1-z)zeta(2w(z))(1+q^-w(z))],
    w(z)=1/2+(1+z)/(1-z).                                (MF3)

This follows first by absolute convergence and the ordinary Laguerre generating function (DLMF 18.12.13), then by meromorphic continuation. On the disk Re w>1/2; zeta(2w) and 1+q^-w are zero-free there. The unique pole is at z=-1/3, corresponding to w=1.

Since w'(-1/3)=9/8, its principal part is

    2delta_q/(1+3z).

Subtract this part. The remainder is holomorphic on the entire open unit disk. For every fixed 1/3<r<1, Cauchy's formula therefore proves the stronger coefficient asymptotic

    a_n^+=2delta_q(-3)^n+O_r(r^-n).                       (MF4)

This strengthens the parent's root-limsup control to an explicit leading term. No zero simplicity, RH, or PNT is used; only Euler's zero-free absolute-convergence half-plane and the pole at one.

For ANY subexponential cutoff schedule log X_n=o(n), MF1 and MF4 now give

    a_n^+-a_n^(X_n) ~ 2delta_q(-3)^n.                     (MF5)

Thus essentially the ENTIRE exponentially growing wrong-source signal can sit in the omitted arithmetic tail, while the computed finite energy necessarily satisfies the desired subexponential upper test. This is an exact failure of interchange of limits, not evidence against RH.

## 3. What remains for the actual signed source

The actual b_k=mu(k)1_(q does not divide k) is not declared to have the growth in MF4 or MF5. Its infinite generating germ is reciprocal zeta, not MF3. A proof must control the full signed tail, or assemble the infinite coefficients with rigorous growing-degree error bounds.

Pointwise convergence at every fixed n is insufficient; it coexists with MF5. The parent exact all-degree diagonal bound also does not help with this tail: the positive squarefree source preserves that diagonal identically. Neither result is a substitute for signed cancellation.

The same pass proves a complementary error in the moment/operator routes: finite prime truncations there create false negativity. Here modest arithmetic truncations create false apparent success. The two errors have different signs but the same cause: arithmetic truncation is not uniform in the degree or test scale of the RH criterion.
