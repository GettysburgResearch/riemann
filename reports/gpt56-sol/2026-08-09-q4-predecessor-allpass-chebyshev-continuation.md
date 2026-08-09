# Q=4 predecessor-row, all-pass, and filtered-Chebyshev continuation

## Scope

This continuation follows the live Q=4 route after the Jordan product-curvature theorem. It does not claim RH.

## Exact advances

### 1. Physical centered-interval fields are predecessor carry rows

`L-33803` proves for any arithmetic prefix `C` and integer endpoint `N` that on the theta-cell `(j/N,(j+1)/N)`,

```text
C(N)-C(N theta)-C(N(1-theta))
 =c(N)+C(N-1)-C(j)-C(N-1-j).
```

Thus the physical bilinear form is exactly a finite predecessor-row Gram plus one explicit endpoint coefficient.  For a Dirichlet source `b`, the row defect is exactly the carry image of `b`.

For ordinary Mobius, the endpoint collar vanishes and the physical row energy is exactly `(N-2)/N`, reproducing the coefficient-one boundary energy of PR #334.

For the Q=4 Jordan family, the bare source, current, and second current become the same predecessor-row coordinates `Y,Q,T`, with explicit collars `gamma_0,gamma_1,gamma_2`.  The complete product-source curvature and individual reflected cross term therefore have exact finite row formulas.

### 2. The Q=4 all-pass defect is a two-frequency state telescope

`L-33804` proves

```text
1-phi(z)phi(w)=R(z)R(w)[1-exp(-L(z+w))].
```

At independent frequencies `z=it,w=-iu`, multiplication by the physical block kernel gives exactly

```text
B_I(f)-B_I(phi f)
 =B_I(Rf)-B_(I-L)(Rf).
```

For Q=4, `E4=2 phi`, so

```text
4 B_I(f)-B_I(E4 f)
 =4[B_I(Rf)-B_(I-log4)(Rf)].
```

This removes the neutral Euler factor itself as an unidentified off-diagonal cross term. The remaining obstruction is arithmetic, not a failure of localizing the all-pass factor.

### 3. The true Q=4 prefix is ordinary Chebyshev plus an explicit staircase

`L-33805` proves, with `R=floor(log_4 x)`,

```text
G4(x)
 =psi(x)
  -3 sum_(r>=1) psi(x/4^r)
  +(3/2)R(R+1) log 4.
```

All exponential four-adic generalized-prime mass cancels exactly.  Hence the pole-sensitive physical current is a nested four-adic filter of the ordinary Chebyshev function plus a deterministic `O(log^2 x)` staircase.

## Discovery target and weaker sufficient theorem

The pointwise reconnaissance

```text
|Q4_phys(n,j)|^2 <=4 S4(n,j)
```

remains discovery only.  Source-blind entrywise kernel domination fails, so any proof must use the actual Q=4 arithmetic source.

The physical criterion does not require that pointwise theorem.  By `L-33803`, it is enough to prove an averaged quarter-balanced estimate of the shape

```text
sum_j |Q4_phys(n,j)|^2
 <= n^2 log^A(2n).
```

Equivalently one may compare the average current square to the average positive forcing `S4`; PR #325 already gives `S4(n,j)=O(n log n)` rowwise.

Under the exact predecessor-row placement this yields polylogarithmic centered-interval energy at integer endpoints; PR #325's one-raw-coefficient real-X collar then extends it between integers. The existing vector-valued pole criterion would give RH.

This averaged estimate is still RH-bearing. Standard unconditional Selberg mean-square estimates do not supply it at the required strength.

## Failed shortcuts retained as firewalls

1. The stronger two-contact inequality `Q2^2<=S2` is false on finite rows.
2. Source-blind entrywise domination of Q=4 wavelet products by product carries is false.
3. A uniform Bessel bound for the raw dyadic centered-interval wavelet family is false; its operator norm grows linearly with scale. The constant-density coefficient mode is exactly annihilated, so the surviving large modes are precisely density fluctuations.
4. Higher naive Haar differences do not repair the source-blind frame bound.
5. The generalized-factorial object of superseded `L-32408` is an extra-floor transform and cancels the zeta poles; it cannot be substituted for the physical current.

## Current proof boundary

```text
source quotient placement                     exact / proposed complete
Jordan product curvature                      exact / proposed complete
physical predecessor-row placement             exact / proposed complete
two-frequency all-pass state telescope         exact / proposed complete
filtered-Chebyshev prefix collapse             exact / proposed complete
pointwise SQFD                                 discovery only
averaged RH-scale Q4 mean square               OPEN / RH-bearing
Riemann Hypothesis                             UNPROVED
```

The next attack should work directly on the filtered-Chebyshev Jensen mean square or the equivalent source-convolved reflected row average. It should not reintroduce a generic physical transference operator: that part is now exact.
