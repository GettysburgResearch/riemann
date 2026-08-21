# Weighted shell-tail carry proposal after the Green/balayage review

Date: 2026-08-08  
Agent: `gpt56-pro`  
Issue: #238  
Branch: `agent/gpt56-pro/238-carry-packing-minorant`  
Status: full conditional RH proposal; `WSTS` open; RH not claimed proved

## Executive result

The former source-coordinate two-contact theorem is no longer the preferred
hinge. The abstract `SGQB(K)` source identity has also been reduced to a smaller,
fully explicit scalar object.

The new spine is

```text
parabolic carry seed
-> dyadic endpoint shell
-> exact normalized continuum upper-tail moat
-> finite shell profile plus summable carry-floor error
-> logarithmically weighted prime-tail charge
-> exact zero-cost carry transport
-> in-support shell correction
-> dyadic shell telescope
-> prime ramp
-> square screw / Landau
-> RH.
```

The single open theorem is the finite weighted shell-tail estimate

```text
B_X
=max_z [sum_(z<=p<=X) log(p)
        (r_X(p)-1_(p<=floor(X/2))r_(floor(X/2))(p))]_+
=X^o(1).
```

## New exact theorem 1: normalized shell order

For the parabolic continuum defect `E`, let

```text
H(theta)=integral_theta^1 E(u)du,
J(theta)=H(theta)/sqrt(theta).
```

On the reciprocal cell `1/(N+1)<=theta<=1/N`,

```text
J'(theta)
=2 theta^(-3/2)
 [N theta+1-(S_N+1)sqrt(theta)].
```

The elementary estimate

```text
S_N+1<=2sqrt(N)
```

proves that `J` is nondecreasing. The stronger bound

```text
S_N+1<=2sqrt(N)-1/10, N>=2,
```

gives

```text
J'(theta)>=1/(5theta), 0<theta<=1/2.
```

For every fixed ratio `0<c<1`, the shell defect is

```text
E_c(theta)=E(theta)-c^(-1/2)E(theta/c)1_(theta<=c),
```

and its tail is exactly

```text
H_c(theta)=H(theta)-sqrt(c)H(theta/c)
           =sqrt(theta)[J(theta)-J(theta/c)]
```

below `c`. Hence

```text
H_c(theta)<=0.
```

For the dyadic shell,

```text
H_(1/2)(theta)<=-(log2/5)sqrt(theta), theta<=1/4.
```

This is an actual signed defect-to-slack theorem, not a face-count analogy.

## New exact theorem 2: weighted prime transport costs zero

For ordered primes `p_i`, put

```text
mu_i=log(p_i)r_i.
```

If every weighted upper tail is nonpositive, the positive `mu_i` can be matched
to negative weighted mass at larger primes.

One weighted transfer `alpha` from `p_i` to `p_j` is implemented by:

```text
raw prime transfer        alpha/log(p_i),
destination endpoint cut  alpha(1/log(p_i)-1/log(p_j)).
```

The resulting weighted changes are `-alpha,+alpha`, and the two objective
changes cancel exactly. Therefore all prime constraints become feasible with
zero prime-objective loss.

For a general residual, the least weighted top-tail charge is

```text
B(r)=max_j [sum_(i>=j)log(p_i)r_i]_+.
```

It can be paid at the largest existing prime at objective cost exactly `B(r)`;
no oversupport coordinate is needed.

## New exact theorem 3: only prime sampling remains

For the finite parabolic residual,

```text
r_X(q)=X^(-1/2)E(q/X)
       +O(q^(-3/2)[1+log(X/q)]).
```

For the shell `Y<X`,

```text
s_(X,Y)(q)=X^(-1/2)E_(Y/X)(q/X)
           +the same summable error.
```

After multiplication by `log p`, the carry-floor error is absolutely summable.
Stieltjes summation yields

```text
sum_(z<=p<=X)log(p)s_(X,Y)(p)
 =sqrt(X)H_(Y/X)(z/X)
  +E_Chebyshev(X,Y,z)
  +O(polylog X).
```

The first term is nonpositive. The only unresolved object is

```text
E_Chebyshev
=X^(-1/2) integral E_(Y/X)(t/X)d[theta(t)-t].
```

Thus the remaining theorem is a one-sided source-specific prime-sampling
remainder after the exact continuum moat has been retained.

## Full conditional composition

Apply the in-support correction to every dyadic shell

```text
X, floor(X/2), floor(X/4), ... .
```

The shell targets and parabolic seeds telescope literally. If

```text
B_Z<=C_epsilon Z^epsilon
```

for every dyadic endpoint, the total objective loss is `O_epsilon(X^epsilon)`.
The explicit parabolic seed then gives

```text
P_X>=4sqrt(X)-X^o(1).
```

Proper prime powers cost only `O(log^2X)`. The square-screw/Landau theorem gives
RH.

## Why this is materially stronger

The proof target is no longer:

```text
bounded source rank;
bounded face dimension;
a positive reflected Schur reserve;
a generic Green norm;
a nonnegative cover;
an abstract lower-scale source identity.
```

All geometric work is complete. The sole hinge is the finite scalar

```text
max weighted upper tail of one explicit dyadic shell residual.
```

The `2/3` Mertens/Farey cell is a mandatory mutation of this scalar, so the
proposal does not hide the RH mode.

## Exact replay

`X-23821-weighted-shell-transport` verifies with rational arithmetic:

```text
classification
EXACT_WEIGHTED_TAIL_TRANSPORT_VERIFIED

least boundary charge      1
transport objective change 0
charged final residual     nonpositive
mutations rejected         4

proof-object SHA-256
41753d1842a8c0e7f39bc45b97cafb9c429bae4f5bd9728247a853a7af90502b
```

The replay proves finite transport algebra only.

## Review order

1. `L-23823-normalized-tail-and-fixed-ratio-shell-majorization.md`
2. `L-23824-zero-cost-weighted-prime-tail-transport.md`
3. `X-23821-weighted-shell-transport/verify.py`
4. `L-23825-finite-shell-profile-and-prime-sampling-remainder.md`
5. `L-23826-in-support-weighted-tail-charge-and-shell-sum.md`
6. `T-23811-weighted-shell-tail-carry-proposal.md`
7. `M-23811-weighted-shell-tail-review-protocol.md`
8. fixed-ratio Mertens mutation and square-screw consumer

## Exact status

```text
continuum shell majorization       proposed complete
weighted finite prime transport    proposed complete
finite shell approximation         proposed complete
shell assembly                     proposed complete
WSTS                               open / RH-bearing
WSTS -> RH                         complete conditional chain
Riemann Hypothesis                 unproved
```
