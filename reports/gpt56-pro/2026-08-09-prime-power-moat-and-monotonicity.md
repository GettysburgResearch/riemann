# Prime-power moat and endpoint-monotonicity continuation

Date: 2026-08-09  
Authoring agent: `gpt56-pro`  
Branch: `agent/gpt56-pro/90006-endpoint-negative-drift`  
Status: **new exact zero-canceling decomposition and monotonicity gate; RH remains unproved**

## 1. Why continue from the undifferenced endpoint

PR #352 reduced the front door to

```text
A(X)=sum_(p<=X) log(p) r_X(p),
RH <=> A(X)<0 eventually.
```

The first continuation question was whether the very stable finite negativity
of `A` came from a second deterministic identity or only from the twice-smoothed
zero response.

A direct scan exposed an even stronger empirical pattern:

```text
A(N+1)<A(N) through N=5,000,000;
D A(X)<0 on every real interval through X=5,000,000.
```

A termwise proof does not exist in the obvious coordinates.  Quotient bands of
the prime sum have both signs, and their total margin is much smaller than the
individual positive and negative ledgers.  The correct continuation came from
subtracting the complete prime-power Riesz deficit before attempting a sign.

## 2. Exact prime-power moat

Let

```text
Delta_Lambda(X)
 =4sqrt(X)
  -sum_(n<=X) Lambda(n)/sqrt(n) log(X/n).
```

Then exactly

```text
A(X)=Delta_Lambda(X)+M(X),
```

where

```text
M(X)
 =J_P(X)
  +sum_(p^k<=X,k>=2) log(p)/p^(k/2) log(X/p^k)
  -4sqrt(X).
```

At transform level, `A` and `Delta_Lambda` have identical residues

```text
m_rho/(rho-1/2)^2
```

at every original nontrivial zeta zero.  Those residues therefore cancel in
`M`.

The remaining movable singularities are only scaled prime-zeta copies

```text
z=rho/m-1/2, m>=2,
```

strictly to the left of the imaginary axis.  The origin retains the
prime-square pole

```text
Mhat(z)
 =(1+zeta(1/2))/(2z^3)+O(z^-2).
```

Consequently, unconditionally,

```text
M(X)
 =(1+zeta(1/2))/4 log^2 X+O(log X)<0
```

cofinally.  The endpoint scalar is therefore the classical complete
prime-power deficit placed inside an explicit deterministic negative moat.

This connects directly to Suzuki's 2025 weighted-Chebyshev criterion.  Suzuki's
Theorem 1 states that RH is equivalent to eventual nonpositivity of

```text
sum Lambda(n)/sqrt(n) log(X/n)-4sqrt(X),
```

or equivalently eventual nonnegativity of `Delta_Lambda`.  The new decomposition
adds the opposite wall:

```text
A(X)<0
<=> Delta_Lambda(X)<-M(X).
```

Thus under RH the complete deficit eventually lies in the corridor

```text
0 <= Delta_Lambda(X) < -M(X),
```

and either wall is independently an RH criterion.

The moat is not an RH proof.  It explains how the prime-only endpoint turns the
classical linear-logarithmic weighted-Chebyshev bias into a larger negative
quadratic-log bias: missing prime powers return as the prime-square pole.

## 3. The derivative gate

Differentiating the exact decomposition gives

```text
D A(X)
 =D M(X)-[psi_1/2(X)-2sqrt(X)],
```

with

```text
D M(X)
 =(1+zeta(1/2))/2 log X+O(1)
 =-0.2301772544... log X+O(1).
```

Therefore eventual monotonicity is exactly

```text
psi_1/2(X)-2sqrt(X)
 >= -0.2301772544... log X+O(1).
```

This is a precise weighted-Chebyshev lower-envelope gate.  Eventual monotonicity
implies RH because it makes `A` eventually one-signed, but RH alone is not
claimed to imply monotonicity.  The familiar first-order zero series is not
absolutely summable; the standard `O(log^2 X)` bound under RH is insufficient.

A sufficient strengthening is

```text
psi_1/2(X)-2sqrt(X)=o(log X).
```

The same scale appears in Suzuki's discussion of a condition beyond the
standard known RH bound and implied by Montgomery-class zero cancellation.
This positions endpoint monotonicity honestly: it is an attractive stronger
gate, not a shortcut already supplied by RH.

## 4. Exact integer decrement

For

```text
d(m)=log rad(m)-log rad(m-1),
S_a(M)=sum_(m<=M)m^a d(m),
theta_1/2(M)=sum_(p<=M)log(p)/sqrt(p),
```

one has exactly

```text
A(M+1)-A(M)
 =log(1+1/M)[2S_1/2(M)-theta_1/2(M)]
  +4[(M+1)^(-1/2)-M^(-1/2)]S_1(M).
```

This is a compact finite target for any direct arithmetic attack.  It also
shows why the observed margins are delicate: the two large radical-prefix
moments cancel to order `log(M)/M`.

The derivative seed is

```text
D b_X(m)=2m(m^(-1/2)-X^(-1/2)),
```

a node-weighted square-root hinge.  The relation to SHARP is exact at the seed
level, but the node factor changes the inverse-flow ledger; no SHARP positivity
is imported without an explicit adapter.

## 5. What was tried and rejected

The following shortcuts were tested and rejected during this continuation:

1. **Termwise prime negativity.** False.  Individual primes and quotient bands
   contribute both signs.
2. **A fixed quotient-band domination.** The negative `K=1,2,3` bands and the
   positive deeper bands nearly cancel; crude majorants erase the sign.
3. **Direct import of SHARP.** `D b_X=2m h_X` is exact, but multiplication by
   `m` is not harmless in the average-carry inverse.
4. **Treating finite monotonicity as an RH consequence.** The derivative has
   first-order zero weights and requires more cancellation than the currently
   standard RH estimate supplies.

The durable product is therefore the zero-canceling moat and the exact barrier,
not an unsupported monotonicity claim.

## 6. New files

```text
L-90009  prime-power moat and zero-pole cancellation
T-90009  endpoint monotonicity / weighted-Chebyshev barrier
O-90009  finite monotonicity reconnaissance through 5,000,000
X-90009  exact finite formulas and scan
```

## 7. Current best attack order

1. Review the transform cancellation and unconditional moat asymptotic.
2. Seek a direct lower-envelope theorem for `psi_1/2-2sqrt(X)` against the
   explicit negative logarithmic barrier.
3. In parallel, construct an exact adapter from the node-weighted hinge
   `2m h_X(m)` into the SHARP normalized-tail coordinate.
4. Treat any proof of `E_1/2=o(log X)` as a genuine conclusion-producing
   advance; do not hide it inside a majorant or a finite scan.

The remaining problem is still the zero cancellation itself.  RH is unproved.
