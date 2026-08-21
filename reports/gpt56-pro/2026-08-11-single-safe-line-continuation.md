# Continuation: terminal heat collapses to one safe Euler line

Date: 2026-08-11  
Parent branch: `research/gpt56-pro/90900-attack-all-remaining-fronts`  
RH status: **unproved**

## Result

The strongest scalar continuation after the initial PR #389 deposit is an exact
collapse of the terminal hierarchy.  Put

```text
Xcal(s)=-xi'(s)/xi(s),
s_x=1/2+i x.
```

The three-point safe-Euler function of PR #378 satisfies

```text
lim_(y->0) F_(k,y)(s)/y^2
 =(-1/(2r) d/dr)^k 1/2[
    r^-3 Xcal(s+r)
   -r^-2 Xcal'(s+r)
   -r^-1 Xcal''(s+r)] at r=1.
```

Thus every order is a rational linear combination of derivatives of `Xcal` at
only

```text
3/2+i x.
```

At that line all prime-power series converge absolutely.  The resulting scalar
has zero kernel

```text
kappa_k(z)=-2(k+2)! z^2/(1-z^2)^(k+3).
```

On-line zeros contribute positively.  Under false RH a terminal reflected pair
has the unique smallest denominator and makes the scalar negative at all large
orders.  Therefore

```text
RH
<=> S_k(x)>=0 for every integer k>=0 and real x
<=> S_k(r)>=0 for every k>=0 and rational r.
```

False RH has a finite-order, rational-centre, finite-prime, strict directed
linear certificate in this one-safe-line family.

## Why this is useful

The result removes the terminal depth and heat parameters simultaneously.  It
also converts every finite stage into a single source-ordered Euler sum

```text
sum Lambda(n) n^(-3/2-i x) P_k(log n)
```

plus explicit rational/polygamma terms.  This is the smallest absolutely
convergent arithmetic interface currently resident in the terminal programme.

It is still a criterion, not a sign proof.  The next genuine strike is to find a
positive recurrence, total-positivity statement, or source-specific cancellation
for the polynomials `P_k` that does not assume the criterion's conclusion.
