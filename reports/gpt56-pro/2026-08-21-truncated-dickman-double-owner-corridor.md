# Truncated Dickman limit and the all-fixed-exponent double-owner corridor

The reciprocal-mass argument in PR #701 closes `q<=p^A` only for `A<e`. The full interval sieve has much more structure.

After logarithmic rescaling, the finite prime interval converges to the signed convolution exponential of `dv/v` on `[1,A]`. Its cumulative satisfies

```text
u F_A(u) = integral_(u-1)^u F_A(v)dv + integral_0^(u-A) F_A(v)dv
```

with zero extension. A first-zero argument makes it strictly positive at every scale. Tight convergence of the even and odd prime-subset measures transfers that sign back to actual prime intervals.

Consequences:

```text
for every fixed A>1, q<=p^A intervals are eventually positive;
there is A(p)->infinity such that q<=p^A(p) intervals are positive;
any adverse interval with q<=X has p=X^o(1).
```

The remaining arithmetic is therefore not a generic long interval. It is a carrier-preserving packing theorem for subpower-many least-owner rows. RH remains unproved.
