# A four-prime affine refinement of the arithmetic lower bound

2026-10-21. This supplements, and does not modify, the frozen two-prime
proof. It retains the original BTY polynomial and the bound ||w''||<350.

Let t=eta^2 and T=(3/400)^2. For each row of the table, put

    G_p(x)=sum_(m=1)^M P(mx)/(p^m+1),
    H_p(x)=sum_(m=1)^M m^2 P(mx)/(p^m+1).

The rational upper bound L_p for log p is also displayed.

| p | M | g_p | h_p | L_p |
|---|---|-----|-----|-----|
| 2 | 10 | .2164 | 380 | .6932 |
| 3 | 6 | .0477 | 140 | 1.0987 |
| 5 | 4 | .0073 | 51 | 1.6095 |
| 7 | 4 | .00204 | 20 | 1.9460 |

The companion exact Bernstein checker verifies for every real x,
at both t=0 and t=T,

    5.67 G_p(x)-175 t L_p^2 H_p(x)
       >5.67 g_p-h_p t.                               (F1)

Both sides are affine in t, so the same strict bound holds throughout
0<=t<=T by taking their convex combination. The retained coefficient
5.67-175 t L_p^2 m^2 is positive in every row; the checker verifies
this before multiplication by the cosh comparison in the two-prime
proof. Thus the actual prime contribution is at least eta log p times
the left side of (F1).

Use rational lower logarithms (.6931,1.0986,1.6094,1.9459) in the
positive constant and upper logarithms L_p in the negative term.
Their bounds are proved by exact atanh series. Summing (F1) gives

    arithmetic detector sum > 1.236 eta-540 eta^3.      (F2)

The exact intermediate constants are 30916853793/25000000000>1.236
and 1076477/2000<540. This improves the use of P(0) in the cubic
error: each whole trigonometric polynomial is certified before
taking its lower bound. No assumption about where its minimum occurs
is needed.

`verify_logistic_four_prime_refinement.py` and its JSON record exact
Bernstein positivity and gap-free dyadic covers for all eight endpoint
polynomials. The code imports the frozen two-prime polynomial machinery,
whose hash is recorded. This is a scalar prime-side lemma; it does not
by itself certify a new zero-free constant.
