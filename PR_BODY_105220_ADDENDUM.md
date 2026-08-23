## T105220 addendum — sharp Bezoutian/boundary correction

This addendum supersedes `ESDE105212` as the normative low-order frontier.

### Binding counterexample

The exact polynomial

```text
p(x)=x^5/5-7x^3-10x^2+8/5
```

has five simple real zeros and all four critical residues negative, but

```text
R(1-C)=946907/459983 > 2.
```

Thus global subunit residue coherence is not necessary for real-rootedness.
`ESDE105212` remains only an optional strong sufficient condition.

### Exact replacement

For a real polynomial,

```text
B_p(x,y)
 = p'(x)p'(y)/n
   - sum_(p'(c)=0) rho_c p'(x)/(x-c) p'(y)/(y-c).
```

Hence

```text
negative index of B_p
 = number of positive critical residues
 = number of nonreal conjugate pairs.
```

For an entire real function in one bounded regular window,

```text
B_F
 = boundary Cauchy-Loewner remainder
   - sum_c rho_c q_c tensor q_c.
```

The boundary remainder vanishes on every real critical-point row and column.
It cannot hide a positive residue.

### New sharp gates

```text
PRES105220:
  every real critical residue at the last defective level is nonpositive;

BRP105220:
  the finite-window boundary Cauchy function has a PSD all-packet Loewner
  kernel under the exact Xi exhaustion, and the nonreal critical correction is
  absent.
```

Then

```text
PRES105220 AND BRP105220 -> RH.
```

Neither gate is proved.

### Unconditional structure

The Bezoutian is also an exact chord average of polarized Laguerre phase
numerators. For every fixed low Xi derivative its center average is an explicit
sinc transform of the positive squared Fourier source and is strictly positive
on an explicit short-chord interval.

### Replay

```text
PASS_X_105220_BEZOUTIAN_BOUNDARY_DECOMPOSITION
182 exact rational/Sturm checks
```

The replay records `pres105220_proved=false`, `brp105220_proved=false`, and
`rh_established=false`.
