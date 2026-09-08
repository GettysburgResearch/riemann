# Mixed heat inequalities: 27 global layers and an all-order late-time bound

Status: PROPOSED PROOFS; independent mathematical review required.
Scope: actual Riemann xi; all a >= 0 and v > 0; finite mixed depth as stated.
Base: PR #790 at bc3c35d8f434949748a2185783bf831d3afd9126.
Dependencies: the exact product, count envelope, V100 and Z14/15 in the
parent HEAT_BERNSTEIN.md; the exact integral in parent THETA_COUNT.md.
Computation: finite rational constants and identities only; see VALIDATION.md.
Smallest remaining gap: the full unbounded mixed-depth inequality, not the
implication from that inequality to RH. RH remains unproved.

All claim IDs ASTRA-TC2-* are local to this continuation. The original
manuscripts, source locks, certificates and claimed scopes remain unchanged.

## 1. Normalization and the exact target

Use the parent's X(u) = xi(1/2 + sqrt(u+1/4)). For EVERY nontrivial zero
rho = beta+i gamma with gamma > 0, counted with multiplicity, put

    A = rho(1-rho) = gamma^2 + beta(1-beta) + i gamma(1-2 beta),
    S(t) = sum_A exp(-At),
    D_m(t) = (-1)^m S^(m)(t) = sum_A A^m exp(-At).

The sum includes two conjugate A's for an off-line quartet. It is real and
locally normally convergent with every derivative for t > 0. The strip gives

    Re A >= gamma^2,   |Im A| <= gamma,
    |arg A| <= 1/gamma,   |A| <= gamma^2+1  (gamma >= 1).        (1)

For the last bound, square both sides and use beta(1-beta) <= 1/4.

Put kappa_A = v/(v+A). The parent's mixed differences are EXACTLY

    H_(a,b)(v) = sum_A kappa_A^(a+1) (1-kappa_A)^b
              = v^(a+1)/(a+b)! * integral_0^infinity
                    t^(a+b) exp(-vt) D_b(t) dt.               (2)

Here a,b are nonnegative integers and v > 0. Absolute convergence follows
from N(T)=O(T log T); (2) also follows by integrating each exponential.
The equality is unconditional and does not assume a sign for D_b.

Inputs from the parent:

    N(T) <= T^2 for T >= 100;
    V100: all zeros with 0 < gamma <= 100 have beta=1/2;
    Z14/15: one zero has 14 < gamma_0 < 15.

Thus the selected real invariant A_0 obeys 196 < A_0 < 226, and

    A_0^m exp(-A_0 t) > 196^m exp(-226t).                      (3)

V100 is imported from Platt--Trudgian; Z14/15 is the parent's directed
interval sign-change certificate. Neither simplicity nor uniqueness is used.

## 2. A weighted tail with its entire infinite complement paid

**Lemma ASTRA-TC2-01.** If B >= 100, m >= 0 is integral, and

    y = t B^2 >= 2(m+1),

then

    sum_(gamma>B) gamma^(2m) exp(-t gamma^2)
      <= t^(-m-1) Gamma(m+2,y)
      <= 2 B^(2m+2) exp(-t B^2).                              (4)

Proof. The function f(x)=x^(2m) exp(-tx^2) decreases on [B,infinity).
Stieltjes integration by parts, with the convention gamma>B, gives

    integral_(B,infinity) f dN
      <= integral_B^infinity (-f'(x)) N(x) dx
      <= 2t integral_B^infinity x^(2m+3) exp(-tx^2) dx.

The discarded endpoint is nonpositive. The last expression is the first
bound in (4). For integer m, the incomplete-gamma identity is

    Gamma(m+2,y) = exp(-y) y^(m+1)
       * sum_(j=0)^(m+1) ((m+1)!/(m+1-j)!) y^(-j).

Successive terms have ratio at most (m+1)/y <= 1/2, so the finite sum is
less than 2. This proves the second bound. Boundary atoms are not lost.

For arbitrary m and H >= 100, (1) and (4) give the useful variant

    sum_(gamma>H) |A|^m exp(-t Re A)
      <= 2 (1+H^(-2))^m H^(2m+2) exp(-tH^2),                 (5)

provided tH^2 >= 2(m+1). No bound on m is hidden in (5).

## 3. Twenty-seven complete mixed layers, using only V100

**Theorem ASTRA-TC2-02.** For every t>0 and every integer 0 <= m <= 27,

    D_m(t) > (15/16) 196^m exp(-226t).                        (6)

Therefore, for every a >= 0, v > 0 and 0 <= b <= 27,

    H_(a,b)(v) > (15/16) 196^b v^(a+1)/(v+226)^(a+b+1) > 0.  (7)

Proof. Fix c=123/100 and t_0=c/100=123/10000. For m<=27,
(1+1/10000)^m < 2. Thus (4) bounds a complex invariant tail by

    sum_(gamma>B) |A|^m exp(-t Re A)
       < 4 B^(2m+2) exp(-tB^2),                              (8)

whenever B>=100 and tB^2 >= 2(m+1).

First take 0<t<=t_0 and set B=c/t >= 100. For every unverified zero with
100<gamma<=B, its summand's phase satisfies

    |m arg A - t Im A| <= m/100+tB <= 27/100+123/100
                        = 3/2 < pi/2.                       (9)

Its real contribution is positive. The verified prefix is positive too.
Also tB^2=cB>=123>2(m+1), so only the tail above B can be negative. Keeping
(3), the ratio of (8) to 196^m exp(-226t) is at most

    R_m(B) = 4 B^(2m+2) 196^(-m) exp(-cB+226c/B).

For B>=100 its logarithmic derivative is

    (2m+2)/B-c-226c/B^2 <= 56/100-123/100 < 0.

Its maximum is consequently at B=100.

Next take t>=t_0. Use the entire verified prefix, not the phase argument,
and apply (8) with B=100. The relative error decreases in t, so its maximum
again occurs at t_0. For either case, the maximum over 0<=m<=27 is at m=27:

    C = 40000 (2500/49)^27 exp(-120.2202)
      < 40000 (2500/49)^27 (7/19)^120
      < 1/16.                                               (10)

The first inequality uses e>19/7, proved by its Taylor sum through degree 6;
the second is an exact rational integer-power comparison in verify_pass2.py.
It is not a floating-point estimate. This proves (6), and (2) gives (7).

For b=0 the original bound is stronger. Equation (7) is a new extension to
mixed b>0, not a replacement of the original b=0 result.

## 4. Every order is positive beyond an explicit time

Let V_H mean that every nontrivial zero with 0<gamma<=H is critical,
where H>=100. Define, for m>=0,

    T_m(H) = max( 2(m+1)/H^2,
        [m log((H^2+1)/196)+log(32H^2)]/(H^2-226) ).          (11)

**Theorem ASTRA-TC2-03.** Under V_H and the same Z14/15 input,

    t >= T_m(H)  =>  D_m(t) > (15/16)196^m exp(-226t).         (12)

Proof. Every term through H is positive; keep A_0. By (5), the whole
unverified tail, divided by the retained lower bound, is at most

    2H^2 ((H^2+1)/196)^m exp(-(H^2-226)t) <= 1/16.

Both conditions used here are exactly the two terms in (11).

This is an all-order statement with an ORDER-DEPENDENT time threshold.
It does not give a common late-time interval for all m. That distinction
is necessary: D_m contains the phase m arg A, which is unbounded in m
for a fixed hypothetical nonreal A.

## 5. Continuation and precise scope

SMALL_TIME_ALL_ORDERS.md proves an order-UNIFORM interval 0<t<=10^-8.
Combining that result with (12) and the full published V_(3*10^12) yields
all mixed depths b<=10^15, at every a and v. The full unbounded-b statement
is NOT obtained by taking that very large finite number as infinity.

The new finite replay verifies constants, normalizations, Laguerre algebra,
and adversarial polynomial controls. It does not execute an infinite zero
sum, rerun Platt--Trudgian, prove the analytic lemmas inside a proof assistant,
or independently referee this manuscript.
