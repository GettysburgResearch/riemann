## T105371 addendum — source–critical Stieltjes capacity

This addendum supersedes the malformed display drafts `L-105371` and
`T-105370`. The normative files are `L-105372` and `T-105371`.

**The Riemann Hypothesis remains unproved.**

### Exact source budget split

At the parity-symmetric origin, regularize the source ratio and write

```text
mhat_F(z)=z sum_(n>=0) a_n z^(2n).
```

Under real nonpositive critical residues, every critical pair `+/-c` gives the
positive atom

```text
s_c=1/c^2,
W_c=-2 F(c)/(c^2 F''(c)).
```

For both the ordinary and shifted Stieltjes matrices,

```text
source matrix
  = critical atomic matrix
    + boundary reserve matrix.
```

Equivalently,

```text
S_(k,Omega)^(a)=A_k^(a)-C_(k,Omega)^(a),  a=0,1.
```

Thus `BRP105220` is exactly the requirement that the critical atoms not
consume more than the fixed origin source moment budget.

### Exact capacity normal form

When the source matrix is positive definite, define

```text
B=A^(-1/2) C A^(-1/2).
```

Then

```text
boundary reserve PSD  <=>  lambda_max(B)<=1.
```

For singular source matrices the same statement uses the pseudoinverse and the
exact range condition.

The normalized critical operator is a sum of rank-one features. Its trace is

```text
sum_c W_c K_(k,a)(s_c),
```

where `K_(k,a)` is the source Christoffel leverage. Therefore the scalar bound

```text
sum_c W_c K_(k,a)(s_c) <= 1
```

is sufficient, though generally not necessary, for the order-`k` boundary
gate.

### Correct conclusion graph

Define `OSCC105371` as the exact all-order source–critical capacity condition.
Then

```text
OSCC105371 <=> OASH105350 <=> BRP105220,
```

and

```text
CRVH105330 AND OSCC105371 -> RH.
```

Define the stronger scalar trace lane `SCLC105371`. Then

```text
CRVH105330 AND SCLC105371 -> RH.
```

Neither capacity gate nor `CRVH105330` is proved for Xi.

### Exact first capacity at odd level

For odd `F`, the source coefficient is `a_0=1`, so

```text
beta_0(F;Omega)
 = 1 - sum_(0<c in Omega) [-2 F(c)/(c^2 F''(c))].
```

The first boundary pivot is nonnegative exactly when the weighted critical
capacity is at most one.

### Replay

```text
PASS_X_105370_SOURCE_CRITICAL_CAPACITY
71 exact rational checks
```

The replay records

```text
crvh105330_proved_for_xi = false
oscc105371_proved_for_xi = false
sclc105371_proved_for_xi = false
rh_established           = false
```
