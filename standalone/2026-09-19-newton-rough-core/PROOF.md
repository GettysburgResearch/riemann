# RCB26 — subpower bounds for rough-squareclass blocks of the Newton covariance

**Status:** proposed component proofs, supplied in full for independent review.
**Conclusion:** an unconditional upper bound for a specified, large part of the
actual covariance. **No native cross-block bound, scale-to-scale gain, or RH
proof is supplied.**

Date: 19 September 2026. Research continuation of issue #902 and PR #848,
frozen at `9e4375952c87835c2f4f2cca10a996009e74a435`. The existing NIR26
innovation and PCR26 bounded-completion improvements are used rather than
rediscovered. Everything here is additive; no earlier statement is promoted.

The main new estimate in this packet is not another implication to RH. It
bounds, uniformly in the cutoff, **all within-block absolute interactions**,
including off-diagonal products. The partition retains the parity of prime
valuations outside a chosen finite bank. For a bank of primes up to
`(log L)^2`, its entire within-block budget is subpower in `L`.

The estimate does not use the full native divisor-inverse equations. Those
enter the exact connection to the Newton update, but the remaining cross-block
estimate still needs additional arithmetic. Section 8 gives a cap-three
counterfamily for which that remaining term is quadratically large.

## 1. Objects, endpoints, and what is being bounded

Let `H_0=0`, `H_n=sum_(j=1)^n 1/j`, and, for positive integers `d,k`, put

    K_d(k) = [H_floor(k/d) - H_k + log d]/d.                 (1.1)

In particular `K_1=0`. This is exactly PCR26's centered harmonic kernel, not
TC26's odd-source Legendre kernel. All values at integer boundaries use the
literal floor. No midpoint Fourier convention is involved.

For a finite real source `c` supported on `1,...,L`, let

    z(d) = (c*c)(d) = sum_(rs=d) c(r)c(s),    d<=L^2,
    Q(k) = sum_(d<=L^2) z(d) K_d(k).                       (1.2)

Dirichlet convolution, not additive convolution, is used. Products `rs=d`
are coalesced **before** defining the diagonal or any other block. Terms with
`d` greater than an observation endpoint remain in (1.2): their harmonic
floor term may vanish but their centered kernel need not.

Let `S` be any finite set of primes. Define the rough parity core

    a_S(d) = product_(p not in S, v_p(d) odd) p.            (1.3)

Thus `a_empty(12)=3`, not `rad(12)=6`. Every `d` has a unique expression

    d = a b r^2,

where `a=a_S(d)`, `b` is squarefree with all prime factors in `S`, and `r`
is a positive integer. Here `a` and `b` are coprime, but `r` need not be
coprime to them for a general source.

Two products are in the same block exactly when

    a_S(d)=a_S(e)
    iff every prime of the squarefree part of d*e lies in S.   (1.4)

Equivalently their ratio is a rational square times a product of primes in
`S`, with integer positive or negative exponents. Their sizes need not be
close, and this is not a geometric frequency-separation condition.

For any set `I` of positive integer observation indices, finite or infinite,
write

    Q_a(k) = sum_(a_S(d)=a) z(d) K_d(k),
    D_S(I) = sum_a sum_(k in I) Q_a(k)^2,
    C_S(I) = sum_(a != a') sum_(k in I) Q_a(k) Q_a'(k).    (1.5)

The cross-block sum is ordered. Then exactly

    sum_(k in I) Q(k)^2 = D_S(I) + C_S(I).                 (1.6)

The stronger nonnegative envelope we will bound is

    B_S = sum_a sum_(k>=1)
                  [sum_(a_S(d)=a) |z(d) K_d(k)|]^2.       (1.7)

It includes diagonal terms and the absolute pointwise products of every
within-block pair. In particular,

    D_S(I) <= B_S,
    sum_(a_S(d)=a_S(e)) |z(d)z(e)|
        * |sum_(k in I) K_d(k)K_e(k)| <= B_S.              (1.8)

The second inequality is stronger than merely controlling the signed
within-block covariance. All sums over `d,e` are finite. The complete infinite
sum over `k` will be justified by the estimates below.

## 2. RCB26-1: a complete overlap bound for two harmonic kernels

The single-column bound

    sum_(k>=1) K_d(k)^2 <= 18/d                            (2.1)

is imported from PCR26 and rederived below. The additional overlap estimate
used here is, for `1<=d<=e`,

    sum_(k>=1) |K_d(k)K_e(k)|
        <= 32 [1+log(e/d)]^2/e.                          (2.2)

Constants are deliberately conservative, not optimized.

### Proof, including the whole tail

Put `r(t)=H_floor(t)-log t-gamma`, where Euler's constant obeys `0<gamma<1`.
Elementary harmonic integral bounds give

    |r(t)| <= 1/t,                   t>=1,
    |r(t)| <= log(1/t)+1,            0<t<1.                (2.3)

For clarity, when `n<=t<n+1`, use
`0<H_n-log n-gamma<1/n` and `log(t/n)>=1/n-1/t` for the upper bound.
Using `H_n=H_(n+1)-1/(n+1)` gives the lower bound `r(t)>-1/(n+1)>=-1/t`.

Since `K_d(k)=[r(k/d)-r(k)]/d`,

    |K_d(k)| <= [log(d/k)+2]/d,      1<=k<d,
    |K_d(k)| <= 2/k,                k>=d.                (2.4)

Also `sum r(k/d)^2<=7d`: the part `k<d` is bounded by
`integral_0^d (log(d/t)+1)^2 dt=5d`, and the rest by `2d`.
Since `sum r(k)^2<=2`, squaring the difference proves (2.1).

For (2.2), put `u=log(e/d)>=0` and split the sum into `k<d`,
`d<=k<e`, and `k>=e`.

The first part is at most

    (1/e) integral_0^1 (-log t+2)(u-log t+2) dt
       = (3u+10)/e.                                    (2.5)

The function in this integral is decreasing as a function of `t`, so its
integral over each preceding unit cell bounds the corresponding discrete
sample after scaling. The middle part is at most

    (2/e) sum_(d<=k<e) [log(e/k)+2]/k
       <= (u^2+6u+4)/e,                                (2.6)

using its value at `d` plus the integral from `d` to `e`. The complete last
part is at most `4 sum_(k>=e) k^-2 <= 8/e`.
Thus the sum is at most `(u^2+9u+22)/e`, which is bounded by the right side of
(2.2). This proves absolute convergence as well. No tail has been sampled or
set to zero. QED.

## 3. RCB26-2: the native truncated source has a fifth-logarithmic block budget

Here take ONLY the actual truncated source

    c_0(n)=mu(n) for n<=Y; c_0(n)=0 otherwise,
    z_0=c_0*c_0.

It need not satisfy the reciprocal moment condition. Consequently `Q_0`
below is its centered-kernel expression; **do not identify it with the native
Newton output without the completion or deterministic terms.** Sections 5-6
supply exact source interfaces.

Define

    P_S = product_(p in S) (1+2/sqrt(p)).

Then the complete absolute within-block envelope of `z_0` satisfies

    B_S(z_0) <= 832 H_Y H_(Y^2)^4 P_S^2.                 (3.1)

For `S` empty this is `O((log(2Y))^5)`, and includes all pairs with square
ratio, not only identical products.

### Exact native product-fibre arithmetic

A nonzero `z_0(d)` has `d=a r^2`, with `a,r` squarefree and coprime. The two
factors whose product is `d` are `r a_1` and `r a_2`, where `a_1 a_2=a`.
Every allowed factorization therefore has the SAME sign `mu(a)`. Consequently

    z_0(a r^2) = mu(a) N_Y(a,r),
    0<=N_Y(a,r)<=2^omega(a),                             (3.2)

where `N_Y` counts the ordered factorizations with `r a_1,r a_2<=Y`.
It can be smaller than `2^omega(a)` near the product boundary; that boundary
is not replaced by an infinite Euler coefficient.

### Summing an entire square tower, rather than one column

For any positive integer `A` and integer `R>=1`, (2.2) gives

    || sum_(r<=R) |K_(A r^2)| ||_ell2^2
      <= (64/A) sum_(s<=R) s^-2
                          sum_(r<=s) [1+2log(s/r)]^2
      <= (832/A) H_R.                                  (3.3)

The first step counts each ordered pair at most twice in the triangular sum.
For the second step,

    sum_(r<=s) [1+2log(s/r)]^2
       <= s integral_0^1 (1-2log t)^2 dt = 13s.

This estimate is for absolute kernels and thus can be used before adding
terms with different squarefree `S`-parts.

For a fixed rough core `a`, separate its products as `a b r^2`, with squarefree
`b` supported in `S`. Formula (3.2) and (3.3), followed by the triangle inequality
in `ell2`, give

    || sum_(a_S(d)=a) |z_0(d) K_d| ||_ell2
       <= sqrt(832 H_Y) * 2^omega(a)/sqrt(a)
                     * sum_(b|product S) 2^omega(b)/sqrt(b)
       = sqrt(832 H_Y) * 2^omega(a)/sqrt(a) * P_S.        (3.4)

Omitting support and coprimality restrictions only enlarges the positive
majorant. Finally

    sum_(a<=Y^2, a squarefree) 4^omega(a)/a <= H_(Y^2)^4, (3.5)

because `4^omega(a)=tau_4(a)` on squarefree integers, and the weighted sum
of `tau_4` is bounded by the fourth power of the harmonic sum. Squaring
(3.4) and summing proves (3.1). QED.

The same-sign property in (3.2) is an exact native support fact. The proof
uses its magnitude consequence; it does not establish the missing
cancellation between distinct rough cores.

## 4. RCB26-3: a uniform bound for the actual bounded completion, at every cutoff

Let `|c(n)|<=K` for all `n`, with support at most `L`. No moment condition is
needed for this block estimate itself. Then

    B_S(c*c) <= 18 K^4 H_L^6 H_(L^2)^4 P_S^2.            (4.1)

For the actual PCR26 clipped completion, `K=3`, so

    B_S <= 1458 H_L^6 H_(L^2)^4 P_S^2.                  (4.2)

This weaker tenth-logarithmic bound is useful because the completion may
contain nonsquarefree integers. Applying (3.1) to it without accounting for
that change would be incorrect.

### Proof

For all `d`, `|z(d)|<=K^2 tau(d)`. In the unique representation `d=a b r^2`,
submultiplicativity of the divisor function gives

    tau(a b r^2) <= 2^omega(a) 2^omega(b) tau(r^2).

At a prime power, `2e+1 <= (e+1)(e+2)/2`, hence `tau(r^2)<=tau_3(r)`. Therefore

    sum_(r<=L) tau(r^2)/r <= H_L^3.                       (4.3)

Using (2.1) and the `ell2` triangle inequality, the absolute envelope for a
fixed core has norm at most

    K^2 sqrt(18) * [2^omega(a)/sqrt(a)] * H_L^3 * P_S.

Square and sum over `a<=L^2`, using (3.5) with `Y^2` replaced by `L^2`.
This proves (4.1)-(4.2). QED.

This theorem actually holds for every source in its stated bounded-coefficient
class. The full divisor-inverse equations are NOT a premise of this estimate.
They remain necessary for identifying the native update and for any further
claim about its cross-block covariance.

## 5. RCB26-4: polylogarithmically growing prime banks still cost subpower

For all primes in `S` at most `y>=exp(16)`,

    log P_S^2 <= 4 sum_(p<=y) p^-1/2
              <= 56 sqrt(y)/log y.                      (5.1)

The prime-sum bound is the elementary one already proved in PPD26; here is
its short derivation. The central-binomial argument gives
`vartheta(x)<3x`. Partial summation gives
`sum_(p<=y) log(p)/sqrt(p) < 6sqrt(y)`. Split at `sqrt(y)`.
The smaller primes contribute at most `2y^(1/4)` after enlarging to integers;
the larger ones contribute at most `12sqrt(y)/log y`.
For `y>=exp(16)`, `log y<=y^(1/4)`, giving the claimed factor 14.
The first inequality in (5.1) follows from `log(1+x)<=x`.

Take `t=log L>=exp(8)` and `S` any subset of the primes up to `t^2`.
Then (4.2) implies the explicit estimate

    B_S <= 1458 (1+2t)^10 exp(28t/log t) = L^o(1).        (5.2)

For the uncompleted native source, replace 1458 and exponent 10 by 832 and
exponent 5, respectively, using `t=log Y`.

These enormous thresholds concern a deliberately elementary explicit bound;
no numerical campaign at such cutoffs was performed. Subpower means that for
every fixed positive epsilon the bound is eventually at most a constant
times `L^epsilon`. It does not mean the displayed finite constants are small.

The conclusion controls every pair whose parity difference uses only primes
up to the bank cutoff, including arbitrary square factors. It does NOT bound
pairs with different rough cores. A large prime in that parity difference
does not guarantee separation of `d` and `e`, or cancellation of their kernels.

## 6. RCB26-5: exact connection to the native Newton update, including the collar

Use the already established PCR26 clipped completion of the actual prefix:
`c(n)=mu(n)` for `n<=Y`; afterward subtract the reciprocal residual with
coefficients of magnitude at most three until it is zero. The complete rule
and its elementary proof give

    P_c(1)=0,  |c(n)|<=3,  L<=Y+ceil(Y/2)<=2Y,
    T_Y=sum_(k=Y+1)^(L-1) m_c(k)^2 <= F_Y,
    F_Y=sum_(k<=Y) m(k)^2.                              (6.1)

The tail-price estimate follows by comparing the forward residual, which
falls by `3/(Y+j)`, with the possible backward variation of the actual
reciprocal sums, which rises by at most `1/(Y-j+1)`; the former is larger
for `j<=ceil(Y/2)`. Summing the squared pointwise comparison pays the tail.
These are inherited PCR26 facts, not new results of this packet.

Let `b=Y+1`, `B=b^2-1`, and `v=2c-1*c*c`. The classical exact identity

    mu-v=mu*(delta-1*c)*(delta-1*c)

makes `v(n)=mu(n)` for every `n<=B`. Equality need not hold at `b^2`.
The moment condition also gives the EXACT finite equalities

    sum_d z(d)/d = 0,
    sum_d z(d)log(d)/d = 0.

Thus on the entire new annulus `I={b,...,B}`,

    m(k) = 2m_c(k)-Q(k).                                (6.2)

In particular the new energy is exactly

    F_B-F_Y = 4T_Y+D_S(I)+C_S(I)
                      -4 sum_(k in I) m_c(k)Q(k).        (6.3)

The last term is signed; it is not zero when the completion has more than
one atom. The tests include a genuinely nonzero native collar at `Y=95`.
The full observation extends beyond `L`, so the definition of `T_Y` is
consistent with (6.3).

Combining the proved block bound with the triangle inequality gives

    F_B <= F_Y + [2sqrt(T_Y)+sqrt(B_S+C_S(I)^+)]^2
        <= F_Y + [2sqrt(F_Y)+sqrt(B_S+C_S(I)^+)]^2.        (6.4)

Here `C_S(I)^+=max(C_S(I),0)` is taken after the entire signed cross-block
sum. Formula (6.4) does NOT bound that positive part. Unlike TC26's infinite
conditionally convergent covariance, the product sums here are finite, but
replacing the remaining signed sum by an uncontrolled absolute one is still
not a solution.

The all-scale gain requested in #902 remains unproved. What (6.3)-(6.4)
add is a proved, cutoff-uniform estimate for one explicit part of the actual
covariance, with the complement and the normalization cost still present.

## 7. Optional interface at native reciprocal crossings: a constant completion budget

Let `Y>=2` satisfy `mu(Y)!=0` and `m(Y-1)m(Y)<=0`. Then `|m(Y)|<=1/Y`.
Complete the native truncated source by ONE atom

    c=c_0+t delta_b,     t=-b m(Y),     b=Y+1.

It is reciprocal-balanced and, on the annulus through `B=b^2-1`,

    m=-Q_0-R,
    R=2t sum_(r<=Y) mu(r)K_(br) + t^2 K_(b^2).           (7.1)

The product at `b^2`, despite exceeding `B`, must remain in the last term.
By (2.1) and `sum_(r<=Y)r^-1/2<=2sqrt(Y)`,

    ||R||_ell2 <= sqrt(18)[4sqrt(b/Y)+b/Y^2] < 25.        (7.2)

For `Y>=2`, bound `b/Y<=3/2`, `b/Y^2<=3/4`; then the left side is at most
`12sqrt(3)+(9/4)sqrt(2)<25`.
Consequently

    |sqrt(F_B-F_Y)-||Q_0||_ell2(I)| <=25.                (7.3)

This supplies a concrete, fully paid interface for using the sharper native
bound (3.1) at such cutoffs. It is not a free choice of an oracle tail, not a
bound for every Y, and not an all-scale gain. Existence or spacing of crossings
is not needed for (7.1)-(7.3); the statement is conditional on the displayed
finite crossing predicate.

## 8. RCB26-6: the remaining cross-block term can be quadratically large for bounded fake sources

The upper bounds above are not secretly a proof for every bounded balanced
source. An explicit counterfamily isolates what they leave uncontrolled.

Prescribe the fake prefix `a(1)=1`, `a(n)=0` for `2<=n<=Y`, and use the SAME
cap-three clipped completion. It has `P_c(1)=0`, `|c(n)|<=3`, `L<=2Y`, and
input innovation energy `Y` before the completion. It fails the native
inverse relation already at `n=2`.

All tail coefficients are nonpositive. Put `w_n=-c(n)/n` for `n>Y`.
Then `w_n>=0`, `sum w_n=1`, and `Y+1<=n<=L<=2Y` on their support.
For `k>=L` with `k<(Y+1)^2`, every product of two tail indices exceeds k.
The exact harmonic formula for the output therefore reduces to

    q(k)=-H_k+2 sum_(n>Y) w_n H_floor(k/n).               (8.1)

For every integer `Y>=128` and

    ceil(Y^2/8) <= k <= floor(Y^2/4),

we have `k>=L` and `k/n>=1`. Using (2.3),

    q(k) <= log(k/(Y+1)^2)+gamma+4Y/k
          <= -log4+1+32/Y < -1/8.                      (8.2)

The final elementary inequality uses `log4>11/8`; for example the first two
terms of the atanh series give `log2>56/81>11/16`.
There are at least `Y^2/9` integers in the indicated interval. Since
`Q=-q` there,

    ||Q||_ell2({Y+1,...,(Y+1)^2-1})^2 >= Y^2/576.        (8.3)

For a fixed bank, or a bank growing at the scale in Section 5, its within-block
energy is subpower by (4.2)-(5.2). Thus the fake source satisfies

    C_S(I) >= Y^2/576-Y^o(1).                            (8.4)

This shows exactly why paying the within-block sector does not bound the
remaining cross-block term. It also strengthens the finite falsification
controls: bounded source coefficients and a reciprocal balance do not force
a subquadratic output law. The fake prefix is related to NIR26's earlier
counterexample, but its completion here has the uniform cap three rather
than an atom of size b. No claim of broad external priority is made.

## 9. What the finite calculations do and do not establish

The accepting checker reconstructs the literal finite source, exact clipped
completion, all coalesced products including products above B, and every
Newton coefficient through B. It independently compares native coefficients
with a prime sieve; a separate trial-factorization route checks the sieve.

It constructs harmonic and logarithm intervals using rational inequalities
and outward-rounded integers at 112 fractional bits. The reported energy
intervals include every integer in each specified finite annulus. Grouped
quantities are compared with the rational aggregate and the complete collar
ledger. The written infinite-k estimates, rather than extrapolation of these
panels, supply the global component bounds.

There are actual native controls against two tempting sign shortcuts:

* At Y=15 with an empty bank, the within-squareclass off-diagonal is positive.
* At Y=31, expanding the bank from {2,3} to {2,3,5,7} INCREASES the sum of block
  energies. Block merging is not monotone in the presence of signed terms.

The fake cap-three family has positive cross-block covariance. Its Y=128
large-output control checks every integer in [2048,4096]. These examples
are not native counterexamples to RH.

Normal and optimized Python use the same accepting implementation and the
same author. Neither constitutes independent mathematical review. No new
zero-free region, unbounded native gain, formal theorem, or whole-repository
validation is inferred from the computations.

## 10. The next mathematical question, without claiming it has been answered

After the grouping, every unpaid pair has a different parity pattern at some
prime exceeding the bank. The next bound must exploit the actual divisor
inverse equations to control that signed cross-block sum. Large primes alone
are not enough; Section 8 keeps large cross-block mass even with bounded
coefficients and exact reciprocal balance.

A genuine continuation would supply a uniform estimate for the native
cross-block term, or a provable gain for a substantial part of it with the
rest still charged. Another diagonal regrouping, an average over altered
sources, or a negative finite table is not that estimate.

The intended research direction has been pursued here through a specific
upper-bound calculation. It has not yet produced the scale-to-scale saving
requested in #902. That distinction is part of the result, not a task silently
assigned to a reviewer.
