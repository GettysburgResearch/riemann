# X-14308 — Exact prolate-source and projective radical-tail verifier

Claim ID: X-14308  
Title: Fraction-only verification of the three-mode source repair and weighted radical-tail quotient  
Status: EMPIRICAL  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: finite algebra in L-14314 and L-14315  
Scope: synthetic exact regression only  
Related counterexample candidates: none

## Objective

Implement the exact finite algebra behind two new positive-route interfaces
without floating point, numerical eigensolvers, prolate special functions, or
trusted claimed coefficients.

## Verified kernels

### Three-mode source repair

The checker reconstructs

```text
m_j = chi_j v_j,
a   = v cross m,
```

and verifies exactly

```text
a dot v = 0,
a dot m = 0,
2 sum a_j^2(1-chi_j)/sum a_j^2 <= 2(1-chi_2).
```

The retained certificate gives

```text
coefficients                    (-3/5, 3/5, -1/5)
normalized leakage squared      6/19
leakage bound squared           3/5
```

### Weighted radical-tail quotient

For a rational symmetric form and a declared radical `r=k+t`, the checker
verifies

```text
Q(k,g)=-Q(t,g),
Q(k,k)=Q(t,t),
```

and computes the weighted projective residual both by the `W^-1` Schur formula
and by the explicit weighted dual over the ordinary annihilator of `k`. Both
routes give

```text
4/11.
```

## Verification performed

```text
python3 -m py_compile                         PASS
python3 -m unittest discover                  8/8 PASS
exact proof-object replay                     PASS
sha256sum -c SHA256SUMS                       6/6 PASS
```

The mutation suite rejects incorrect concentration ordering, a vanishing cross
product, false leakage data, a false radical, a nonsymmetric form, an
indefinite weight, and Boolean rational contamination.

## Proof boundary

This exact checker does not establish that any input is genuine prolate data,
that a Schwartz approximation has a stated analytic error, that the imported
Weil radical theorem has the repository normalization, or that a cofinal lower
spectral floor exists. It supplies only the small finite consumer for those
future producers.
