## T105410 addendum — second-order tail scaling

The positive real-saddle law has an exact second-moment centering:

```text
E[V^2]=1,
E[V-1]=-(1/2)E[(V-1)^2].
```

Using this cancellation upgrades the normalized Xi sine/cosine approximation from first-order `Y/sqrt(r omega)` to

```text
(1+Y)^2/(r omega)
```

through two derivatives.

The exact tangent/cotangent tail has the universal scaling

```text
J * pushforward_(u=pi^2 J^2 s)(nu_tail)
 -> pi^(-2) u^(-1/2) 1_(0,1) du,
```

and its order-`k`, block-`a` smallest eigenvalue has the sharp exponent

```text
lambda_min ~ c_(k,a) J^(-(4k+2a-3)).
```

Consequently the unconditional growing critical prefix improves to

```text
J_r=r^gamma,  gamma<1/(4k-1),
```

from the previous `gamma<1/[2(3k(k-1)+5)]`.

For the complete remote tail, the natural moment grading is `J^(2n+1) Delta_n`, not one common moment rate. Under the complete sharp critical sign, one scalar zeroth capacity pivot prevents all mass escape at the reciprocal-square endpoint and forces every fixed remote moment.

Exact replay:

```text
PASS_X_105410_SHARP_TAIL_SCALING
a6772e54d586a0ae89ddc51f6231a06626642bc1f1ecaa0d46b9ad2119207cd2
```

RH remains unproved. The complete sharp critical sign, scalar endpoint pivot, and low-order reverse-Rolle descent remain open.
