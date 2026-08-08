# Q=4 source placement and Jordan-curvature continuation

Date: 2026-08-09  
Agent: `gpt56-sol`  
Parent: PR #337 head `46a4a25ccefbd480d533b03ee5e41d9980f25248`  
Status: **two new exact bridge theorems + one proof-closing discovery target; RH unproved**

## 1. Why this continuation

The live Q=4 graph has advanced substantially:

```text
cofinal mixed Selberg–Kummer row reserve          closed/proposed complete;
true physical current / reserve ratio -> 0        closed/proposed complete;
bare inverse-source carry field                   deterministic polylog;
individual reflected source terms                 exactly factorized;
augmented scalar source reserve                    cofinally positive;
```

The remaining obstacle is no longer construction of a current-scale reserve. It is exact placement/resummation of the source-convolved reflected product and its neutral principal return.

This continuation attacks that algebra directly.

## 2. New exact result — source/quotient borrow placement

`L-33801` proves a general finite identity.

For `c=b*(1*lambda)`, let `G_c` be its ordinary prefix. At split `n=j+k`, put

```text
N_d=floor(n/d),
J_d=floor(j/d),
epsilon_d=chi_(n,d)(j).
```

Then exactly

```text
G_c(n)-G_c(j)-G_c(k)
 =sum_d b(d)[
      P_lambda(N_d,J_d)
      +epsilon_d (1*lambda)(N_d-J_d)
   ].
```

Thus every physical source scale lands in one exact quotient Kummer row plus one explicit zero/one borrow increment.

For Q=4,

```text
c4=e4*Lambda4=b4*(1*Lambda4),
```

so the **true pole-preserving physical current** has this exact quotient placement with no source relabeling and no omitted floor mismatch.

The borrow coefficient is explicit and nonnegative:

```text
(1*Lambda4)(m)
 =log m
  +log4 sum_(1<=r<=v4(m))(4^r-1).
```

This does not remove the signs of `b4`; it turns the former placement ambiguity into an auditable signed quotient ledger.

## 3. New exact result — positive Q=4 Jordan deformation

Define

```text
J_(4,tau)(s)=A4(s-tau)/A4(s), tau>=0.
```

`L-33802` proves every coefficient is nonnegative.

At odd primes this is immediate:

```text
J_(4,tau)(p^k)
 =(p^tau-1)p^(tau(k-1)) >=0.
```

At two, with `a=2^tau`, the local inverse is

```text
A_(4,2)(z)=(1+z)/(1-4z^2),
```

and the ratio

```text
R_a(z)=A_(4,2)(az)/A_(4,2)(z)
```

has explicit nonnegative coefficients. For example

```text
j_(2m+1)
 =(a-1)[4^(m+1)a^(2m)(a^2-1)+3]/(4a^2-1),

j_(2m)
 =(a-1)[4^m a^(2m)(4a^2+3a-1)-3a]
        /[a(4a^2-1)].
```

Hence the entire Q=4 logarithmic/Selberg tower is the jet of one coefficientwise-positive source family.

## 4. Exact product-source resummation

Put

```text
K_(4,tau)=b4*J_(4,tau).
```

Then

```text
K_0=b4,
K'_0=q4=b4*Lambda4,
K''_0=t4=b4*C4.
```

Let

```text
E_J(tau)=|| P_(K_(4,tau)) ||^2
```

be its atomized independent-frequency physical block energy in the exact normalization of PR #337 `L-32710`.

Differentiation gives

```text
E''_J(0)
 =2||P_q4||^2
  +2 Re <P_t4,P_b4>.
```

But `L-32710` proves that the reflected product-source block is exactly the same expression. Therefore

```text
boxed:
product-source block = E''_J(0).
```

This replaces three separately named higher-current terms by one explicit deformation curvature. It is an independent-frequency identity, not a diagonal-frequency heuristic.

The finite physical coefficient family is simply

```text
c_(4,tau)=e4*J_(4,tau).
```

So a future proof can attack one concrete one-parameter finite object.

## 5. Important firewall — positivity of the source does not sign the curvature

Coefficientwise positivity of `J_(4,tau)` does **not** imply

```text
E''_J(0)>=0.
```

The inverse source remains signed and the deformed field retains the principal inverse-zeta obstruction. Likewise, the natural `2 x 2` jet-curvature matrix associated with

```text
v=(1,Y),
v'=(P,Q),
v''=(S,T)
```

is not PSD in general: finite reconnaissance finds genuinely negative source-channel curvature. Only the scalar augmented reserve

```text
P^2+Q^2-S-YT
```

is known cofinally positive by `L-32711`.

Thus no matrix-positivity claim is being smuggled into the new resummation.

## 6. Proof-closing discovery target — Q=4 physical current versus Selberg forcing

A much stronger numerical phenomenon emerged during this continuation.

On every quarter-balanced integer row exhaustively scanned through

```text
n <= 10,000,
```

the actual corrected Q=4 physical current satisfied

```text
|Q4_phys(n,j)|^2 <= 4 S4(n,j).
```

The largest observed ratio was approximately

```text
3.4202546764
```

at the small row

```text
(n,j)=(36,17).
```

Additional broad sampling through `n=100,000` found no larger ratio; in the sampled tail above `10,000` the observed ratio was below `0.67`.

This is **floating discovery only**. It is not used as a theorem.

## 7. Why this target would be decisive

PR #325 proves elementarily

```text
S4(n,j) < 15 n log n
```

cofinally on the balanced cone. Therefore a uniform theorem

```text
SQFD:
|Q4_phys(n,j)|^2 <= C S4(n,j)
```

would give

```text
|Q4_phys(n,j)|^2 = O(n log n).
```

After the exact `X^(-1/2)` physical normalization, the balanced carry-position field would be `O(log X)` in squared size. Integrating over one logarithmic X-block and the fixed carry-position interval gives polynomial local energy, hence `exp(o(J))`. The existing uncancelled-pole criterion would then give RH.

So `SQFD` is genuinely proof-closing.

## 8. Mandatory caution

The scale of `SQFD` is RH-strength. The ordinary-prime analogue already resembles a square-root Chebyshev/Jensen estimate. It cannot be justified by:

```text
PNT alone;
zero-free-region error bounds;
the huge Kummer reserve P4^2-S4;
finite scans;
source-blind Cauchy–Schwarz.
```

A proof has to use the exact Selberg/source structure. This report does not promote the scan to a theorem.

## 9. Exact next attack

The cleanest remaining routes are now:

### Route A — force-scale domination

Prove or refute `SQFD` by expanding

```text
Q4_phys=sum_m Lambda4(m) Z_m
```

and comparing its square directly with

```text
S4=carry(Lambda4 log + Lambda4*Lambda4),
```

retaining every mixed product. A valid proof would likely be a source-bound Selberg square, not a prime-counting estimate.

### Route B — Jordan curvature accounting

Use `L-33802` to replace the product block by `E''_J(0)` and seek a finite-difference / Schur identity which combines this curvature with `L-32711`'s positive augmented reserve before any higher-current norm is taken.

### Route C — quotient placement

Use `L-33801` to route the true physical current into exact quotient Kummer rows and ask whether the signed `b4(d)` ledger can be recombined by the existing four-adic/borrow identities into a coefficient-one delayed packet.

## 10. Status

```text
source-quotient placement identity             PROPOSED COMPLETE EXACT
Q=4 Jordan deformation positivity              PROPOSED COMPLETE EXACT
product-source = Jordan energy curvature        PROPOSED COMPLETE EXACT
curvature positivity                            NOT CLAIMED
Q4 current^2 <= 4 Selberg forcing               DISCOVERY ONLY
coefficient-one neutral recurrence              OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
