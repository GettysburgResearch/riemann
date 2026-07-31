# Research report — sacrificial count and direct harmonic-Schur bypass

Agent: `gpt56-02-p`  
Date: 2026-07-31  
Branch: `agent/gpt56-02-p/156-sacrificial-count`  
Stacked base: draft PR #169  
Status: two exact reductions and one new direct bypass; no proof of RH

## 1. Starting point

The harmonic three-block continuation reduces its last visible gate to

```text
N_(G_C^-1/2 K_T^C G_C^-1/2)(B_T+beta) <= dim R.
```

A concurrent right-inverse branch proves this count on an explicitly constructed
cardinal–radical packet. Its own proof boundary correctly retains a separate
complete-low-index capture theorem. The target here is therefore the count on
the actual complete harmonic packet, or a route that avoids the count.

## 2. Sacrificial-subspace theorem

For positive metric `G`, positive evaluation Gram `K`, and threshold `tau`, it
is enough to find **any** subspace `W` satisfying

```text
codim_U W <= r,
K|W >= tau G|W.
```

Courant--Fischer immediately gives

```text
N_(G^-1/2 K G^-1/2)(tau) <= r.
```

The witness need not equal `R^(perp_G)` and no principal angle is assumed.

If `dim R=r` and

```text
K|R <= epsilon G|R,
epsilon < tau,
```

then the count is exactly `r` and

```text
||P_(N^perp) P_R||^2 <= epsilon/tau.
```

Thus the angle used by the harmonic visible transfer is an output.

## 3. Two quotient constructions

### Cardinal quotient

If the complete packet is represented as exact radical directions plus a finite
critical-line cardinal quotient, take the cardinal quotient as `W`. Its global
transform is one at its selected zero and zero at every omitted zeta zero, so
its finite-section residual is controlled by the exterior localization tail.
This gives a fixed-zero implementation of the count without an unbounded
critical-line verification assumption.

### Source corrector

An external source repair

```text
R=(I-Q ell)P
```

preserves the full dimension of `P`. In

```text
U_src=P + Ran Q,
```

the fixed corrector space `Ran Q` has codimension `dim R`. The self-dual Hermite
sector has one corrector, `h_0/h_0(0)`.

Poisson summation gives its exact logarithmic boundary channel. If

```text
R_0(x)=E(h_0)(e^x),
```

then

```text
R_0(x)=R_0(-x)+q/2(e^(-x/2)-e^(x/2)).
```

For the truncation to `[-L,L]`, evaluation at every fixed real ordinate has
magnitude squared of order `e^L`, whereas its Hardy metric is at most
`e^((1+2tau)L)`. The normalized frame quotient therefore loses only
`e^(-2tau L)`, far larger than the Gaussian radical evaluation scale
`e^(-c lambda^2)`.

This scale separation is exact, but the raw Gaussian corrector does not vanish
at omitted zeros. It needs a complete residual theorem or a growing certified
zero block. The cardinal quotient is cleaner.

## 4. Direct harmonic-Schur bypass

The count itself can be avoided.

Let `S_U` be the exact harmonic Schur form and let `R` have rank `r`. Assume,
after metric whitening,

```text
-alpha I <= S_R <= alpha I,
X*X <= beta^2 I,
```

where `X` is the complete cross residual from `R` to its orthogonal complement.
If some `W` has

```text
codim W <= r,
S_U|W >= Gamma I,
```

then min--max saturates the complete low index. For any

```text
alpha < t < Gamma,
```

an inverse-Ritz argument gives the sharper explicit floor

```text
lambda_min(S_U)
>= -alpha-beta^2/(t-alpha).
```

The proof uses

```text
D=tI-B,
K=D^2+X*X,
s=t+alpha+beta^2/(t-alpha),
q=-1/s,
qK-H>=0.
```

This route uses the complete harmonic form, not a positive selected-zero
subform, and therefore retains cancellations before absolute values are taken.

## 5. One-end local-Weyl candidate

For a two-boundary low packet, restrict to one endpoint sector. Opposite-end
terminal-prime Hankel terms vanish from that restricted quadratic. If its
codimension is at most the radical rank and the exact harmonic lifts remain in
the graph-bounded shrinking-profile class, the dimension-uniform local-Weyl
theorem supplies

```text
S_U|W >= [log R-O(1)-o(1)] G_C|W.
```

Then `Gamma->infinity`. With a fixed `t>0` and the Gaussian radical rates,

```text
alpha -> 0,
beta -> 0,
```

the direct floor tends to zero from below. This simultaneously bypasses:

- the generalized selected-zero eigenvalue count;
- the omitted-zero absolute budget;
- the opposite-end terminal-prime norm;
- an explicit principal-angle theorem.

The load-bearing remaining check is now a same-end harmonic-lift profile theorem
and the exact codimension inequality.

## 6. Exact finite replay

`X-18501` uses only integers and `fractions.Fraction`. The retained `4 x 4`
certificate has a nontrivial radical/witness cross in `K`, so it is not a block-
diagonal tautology.

```text
radical rank                 2
threshold                    1/2
radical evaluation endpoint  3/100
count lower/upper            2 / 2
angle squared upper          3/50
witness floor pivots         3/2, 187/75
radical moat pivots          1/50, 1/100
proof SHA-256
997492a615abfd5bd5a4ada88a9513b649d3126cfe2b38833f12b488de10b8e2
```

Nine central/adversarial Fraction checks pass. The verifier accepts singular
positive semidefinite evaluation Grams, as required in production.

## 7. Comparison with the concurrent count proof

The concurrent exact right-inverse result is mathematically useful: on its
cardinal–radical packet it gives a finite nonzero singular-value gap and hence
the requested count. It explicitly does not prove that the packet captures the
complete dangerous low hierarchy.

The present contribution adds two things:

1. the count only needs a high-frame subspace of the correct codimension; it does
   not need a right inverse or the radical complement itself;
2. the complete harmonic Schur floor can be obtained directly from such a
   subspace, eliminating the selected-zero count altogether.

Neither result silently identifies a constructed packet with the complete low
packet.

## 8. Honest frontier

No unconditional RH proof has been obtained. The strongest new production
question is now:

```text
Does the actual complete harmonic low packet contain a one-end or cardinal
quotient W with codim W <= dim R, and does its exact harmonic lift satisfy a
strict frame/local-Weyl floor?
```

A positive answer closes the final count or bypasses it and, with the already
proved Gaussian radical and assembly rates, gives the cofinal lower floor.
