# Source-derived production-moat continuation

## Published prefix

The prepared X-16205 cofinal-prefix status and digest manifest were committed to
PR #164 in commit

```text
e75294743d155affaf0ae2ea4a586a06524c3e4b
```

without duplicating the newer X-16206 production stack.

## Actual gamma=4096 source replay

The directed infinite Legendre--Jacobi calculation resolves the modes
`0,4,8,12`, their concentration defects, point values and integral values. The
exact determinant formulas produce the two repaired columns

```text
target      modes 0,4,8
complement  modes 4,8,12
```

with both source constraints identically zero.

The resulting outward replacements are

```text
radial tail L2 squared              <= 1e-4181
frequency-derivative tail L2^2      <= 1e-4174
horizontal-strip tail L2^2          <= 1e-4180
source packet fourth derivative L1  <= 45000
endpoint point charge               <= 1e-5
endpoint L2 squared charge          <= 2e-10
deterministic error                 <= 1/40000
```

The exact full result has proof-object digest

```text
185814dceb233ba87f14dcb154c0adb576a99d50c936376421f376414dd04cdb
```

and file digest

```text
5529e40d6e11a3698c853a550b9747842eca4542e8c7d9e15a46d6cf748c32aa
```

## Downstream binding

`verify.py` reconstructs every replacement from the two repaired columns.
`bind_downstream.py` writes the radial, endpoint, deterministic-error, and Gram
fields into an X-16204 wrapper only after the complete arithmetic alias ledger
is present.

The exact first-alias Gram satisfies

```text
0.9999999 I <= D_first <= 1.0000001 I.
```

But the full arithmetic profile is

```text
D_full=D_first+P_self+C_cross,
P_self>=0.
```

Therefore the production lower floor is

```text
lambda_min(D_full)
 >=0.9999999-||C_cross||.
```

The current certificate leaves `||C_cross||` unresolved and is classified

```text
SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN.
```

This prevents the inherited/synthetic profile-Gram ledger from being reused.

## Smallest exact blocker

Produce one outward operator bound for the complete first-versus-higher Poisson
cross-alias matrix of this same repaired packet. No new support block is useful
until that number is below the exact first-alias floor. A directed radial phase
quadrature or an equivalent finite stationary/nonstationary phase ledger is the
remaining production moat.

No RH proof is claimed.
