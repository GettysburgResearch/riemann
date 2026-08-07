# Full-Φ regular augmented tail audit

Date: 2026-08-01  
Agent: `gpt56-05-l`  
Issue: #180

## Requested target

After the singular Cauchy/endpoint channel was closed, prove that

```text
A_omega^reg * ghat_omega
```

is the positive completed Volterra-tail Gram and hence that the augmented
Green-resolvent defect is positive.

## Exact outcome

The requested raw regular identity is false.

With

```text
q = u-(1+omega),
a = 2 omega,
c = 1/zeta(1+2 omega),
A(q) = zeta(1+q)/zeta(1+2 omega+q),
B(q) = pi^omega Gamma(3/2+q/2)/Gamma(3/2+omega+q/2),
```

and

```text
A(q)=c/q+q Rhat(q),   R>=0,
ghat(q)=B(q) q/(q+a),
```

the exact completed kernel is

```text
xi(u-omega)/xi(u+omega)
 = c B(q)/(q+a)
   + q^2 B(q) Rhat(q)/(q+a).
```

The first summand is a complete positive moving endpoint Gram. If only its
constant value at `q=0` is retained, the omitted regular boundary-tail cross is

```text
c [ B(q)/(q+a)-B(0)/a ].
```

It is load-bearing and initially negative.

The second, raw-tail summand is not a positive Hankel kernel. It vanishes
linearly at `q=0` while remaining nonzero for `q>0`, which contradicts the
`2 x 2` Cauchy--Schwarz condition of every positive Hankel Gram. An exact
rational model in `X-15413` reproduces the failure and exact endpoint-cross
cancellation.

## Corrected one-Green target

After the Mellin primitive trace, the regular tail becomes

```text
G_reg(q)=q B(q) Rhat(q)/(q+a)=Laplace[m_omega'](q),
```

where

```text
m_omega=n_omega * R_omega,
Laplace[n_omega](q)=B(q)/(q+2 omega),
n_omega>=0,
R_omega>=0.
```

Its positive-kernel property is equivalent to the explicit smoothed Jordan
inequality

```text
sum_(log n <= t)
  J_(2 omega)(n)/n^(1+2 omega)
  n_omega(t-log n)
 >=
  1/zeta(1+2 omega) * integral_0^t n_omega(r) dr.
```

Harris association proves only `R_omega>=0`; it does not prove the derivative
sign above.

## Proof boundary

- The prepared intertwiner patch and the new regular-tail files are published
  on PR #165.
- The singular channel and full boundary-tail cross are explicit.
- The raw regular Gram claim is refuted.
- The one-Green smoothed Jordan inequality remains unproved.
- Consequently the augmented Green-resolvent defect and RH remain unproved.

## Smallest blocker

Prove the beta-resolvent-smoothed Jordan inequality uniformly for
`0<omega<1/2`, or prove its matrix-valued full-Φ analogue directly in the
augmented endpoint-plus-tail graph norm.
