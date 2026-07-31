# Counted inverse–Ritz completion of the finite lower-floor chain

Agent: `gpt56-pro-09-c`  
Date: 2026-07-31  
Issue: #156  
Stacked base: PR #157 on PR #152

## Result

The requested principal-angle theorem is sufficient but not necessary.

A complete symbol/complement theorem already provides an integer upper bound
`d` for the number of localized-Weil eigenvalues below a positive threshold
`Gamma`.  If an exact repaired radical packet has the same dimension and lies
strictly below a smaller shift `t`, then the packet's inverse-resolvent Ritz
values account for the complete low spectral multiplicity.

The exact generalized forms are

```text
H = <(A-t)u_i,u_j>
K = <(A-t)u_i,(A-t)u_j>.
```

If `H<0` and a rational `q<0` obeys

```text
q K - H >= 0,
```

then

```text
inf spectrum(A) >= t + 1/q.
```

No selected low-symbol eigenbasis or principal angle enters the certificate.

## Scalar envelope

For trial Gram `G`, compression `B`, and complete cross-residual Gram `R`, assume

```text
-alpha G <= B <= alpha G
R <= beta^2 G
0 <= alpha < t.
```

Then

```text
F = -(3 t alpha + alpha^2 + beta^2)/(t-alpha)
```

is an ambient lower floor.  Fixed positive `t` and `alpha,beta -> 0` give
`F -> 0-`.

This is the exact squared-residual weakening needed by the positive route.

## Relationship to the newest branches

- PR #152 supplies the symbol count/complement interfaces and the cofinal lower
  envelope theorem.
- PR #155 supplies an optional whole-space bathtub floor and reusable directed
  symbol cells.  If its scalar floor is insufficient, its cells can still feed
  a count cap.
- PR #157 repairs the exact Connes--Consani radical source domain and constructs
  growing fixed-rank packets.
- L-15601 combines the count from the first stack and the trial packet from the
  second without a direct subspace comparison.

## Remaining asymptotic gate

Define:

```text
D(a,t,Gamma) = certified number of possible eigenvalues below Gamma
C(a,eps)     = maximum rank of exact radical packets with alpha,beta <= eps.
```

The remaining theorem is precisely

```text
D(a_j,t_j,Gamma_j) <= C(a_j,eps_j)
eps_j -> 0
```

on a cofinal support sequence.  Existing fixed-rank diagonal arguments do not
prove this simultaneous growing-rank inequality.

## Exact regression

The synthetic operator

```text
A = [[0,1/100],[1/100,1]]
```

has at most one eigenvalue below `Gamma=1/2`.  With trial `e1`, `t=1/4`, and
`q=-1249/313`, the verifier proves

```text
qK-H = 1/5000 > 0
inf spectrum(A) >= -3/4996.
```

Nine adversarial tests pass using Python integers and `fractions.Fraction` only.
Proof-object SHA-256:

```text
5b08520088725ed983b6bb035ee5cfd818a5352c59656c7cbc269fdee1f4007a
```

## Status

- `L-15601`, `L-15602`, `T-15601`, `M-15601`: `PROPOSED`.
- `X-15601`: exact finite arithmetic and synthetic control.
- No production localized-Weil packet or cofinal rank-capacity theorem exists.
- RH is not claimed proved.
