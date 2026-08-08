# Eta-preconditioned lattice contraction and two-contact endpoint absorption

## Scope

This continuation attacks the two explicit unresolved mechanisms in the
reciprocal-eta/two-contact proposal:

1. repeated accumulation of the shifted lattice endpoint `2kq-1`;
2. the unweighted two-contact coordinate omitted by the positive logarithmic
   Selberg moments.

Both mechanisms are closed below at their exact natural scopes.  The remaining
RH-bearing statement is the source-coupled interior/lower-scale recurrence.

## 1. Exact lattice factorization

For

```text
U f(q)=sum_k [f(2kq)-f((2k+1)q)],
C f(q)=sum_k [f(2kq-1)-f((2k+1)q)],
E=C-U,
```

let `B=(I-U)^(-1)` be the reciprocal-eta resolvent.  The divisor prefix of its
coefficient sequence is supported only on powers of two:

```text
sum_(d|h) b_eta(d)=h if h is a power of two, else 0.
```

Therefore

```text
K:=B E,

K f(q)=sum_(r>=0) 2^r
       [f(2^(r+1)q-1)-f(2^(r+1)q)],
```

and exactly

```text
I-C=(I-U)(I-K).
```

On the full critical power-log Jordan bank

```text
sum_m (u_m+v_m log x)x^(-sigma-m), sigma>=1/2,
```

with coefficient radius `1/16` and logarithmic weight eight, `L-28014` proves

```text
||K|| <= 6/31,
||(I-K)^(-1)|| <=31/25.
```

Thus every shifted/cutoff cascade is a bounded analytic dressing of the
unshifted reciprocal-eta source.  The lattice commutator is not an independent
RH obstruction.

For the finite filter

```text
p=epsilon-3 delta_2+2 delta_4,
p*b_eta=b_2,
```

the complete shifted solution is

```text
(I-C)^(-1)p=(I-K)^(-1)b_2.
```

The only remaining analytic source is exactly the two-contact source already
used in the reflected/factor-five programme.

## 2. Exact endpoint absorption

For the positive generalized-prime system

```text
A_2=zeta/(1-2^-s),
a_2(n)=v_2(n)+1,
Lambda_2=Lambda+(log2)1_(2-powers),
```

let

```text
R_2(n,j)=P_2(n,j)^2-S_2(n,j)>=0
```

be the pointwise generalized Selberg reserve of `L-28009`.  The unweighted
source has two endpoint contacts with normalized energy

```text
E_end(n)=2 L_2(n)^2/(n+1),
L_2(n)=log n+v_2(n)log2.
```

`L-28015` proves

```text
R_2(n,2)>=L_2(n)^2/32,
```

and the same at `n-2`.  Consequently

```text
E_end(n)
 <=32 [R_2(n,2)+R_2(n,n-2)]/(n+1)
```

for every `n>=5`, with the coincident `n=4` row handled separately by the same
constant.  Only `n=2,3` lack an interior coordinate.

The inequality is homogeneous in the row amplitude and therefore survives a
row-direct-sum source ledger.  It does not license deletion of cross-row terms
from an arbitrary physical Gram.

## 3. Exact regressions

```text
X-28003
  reciprocal-eta divisor checks             256
  sparse preconditioned operator checks      256
  exact factorization checks                 256
  tau=1 coefficient checks                    64
  verdict PASS_EXACT_ETA_PRECONDITIONED_SHIFT_FACTORIZATION
  digest  5ca61b668f568bbac5cff3f5117f38203a506379d38d2a09df5029d13d3ed9aa

X-28004
  directed logarithmic rows                  12
  minimum row                                n=6
  verdict PASS_EXACT_TWO_CONTACT_ENDPOINT_RESERVE
  digest  352a5265ab52a9251965ed1eb16ffab1e47c036b18970403648e0c9b0725c3ea
```

The first checker authenticates the exact operator algebra; the `6/31` estimate
is proved analytically.  The second checker proves only the finite rows
`4<=n<=15`; the infinite range is proved by elementary inequalities in the
claim file.

## 4. Corrected proof frontier

The following items are no longer open on this branch:

```text
accumulation of 2kq-1 lattice shifts;
positive-order power/Peano boundary jets;
transference from reciprocal eta to b_2;
uncontrolled two-contact endpoint energy for rows n>=4.
```

The actual surviving theorem is:

> Assemble the complete source-convolved reflected identity in a coupled
> interior row/physical block, preserve every cross term, use the exact endpoint
> absorption above, and route the two finite rows plus the product/cutoff
> forcing to strict lower scale with total coefficient at most one.

This is narrower than generic BTP, SIFD, WSTS, or a complete carry-flow
positivity theorem.  It is still RH-bearing because the surviving source is

```text
B_2(s)=(1-2^-s)/zeta(s).
```

## Status

```text
eta-preconditioned lattice contraction      PROVED / proposed exact
endpoint two-contact reserve absorption      PROVED / proposed exact
full source-coupled interior recurrence       OPEN
Riemann Hypothesis                            UNPROVED
```
