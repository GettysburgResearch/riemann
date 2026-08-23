## T105380 addendum — Xi source endpoint and trigonometric saturation

**The Riemann Hypothesis remains unproved.**

### Exact Xi source formulas

For odd `F=Xi^(r)`, use the positive tilt

```text
dP(u) proportional to u^(r+1) Phi(u) du,
X=U^2.
```

Then

```text
a_0=1,
a_1=E[X]/3,
a_2=(5E[X]^2-E[X^2])/30,
a_3=(210E[X]^3-77E[X]E[X^2]+3E[X^3])/2520.
```

The two order-two source determinants are explicit. A single sufficient
condition pays both:

```text
E[X^2]/E[X]^2 <= 35/27.
```

For even derivatives, remove the central residue first and use the tilt
`u^(r+2)Phi(u)`. With

```text
h=E[X^(-1)], x=E[X], y=E[X^2],
```

one gets

```text
a_0=(3-hx)/6,
a_1=(15x-10hx^2+3hy)/360.
```

The single sufficient condition

```text
E[X]E[X^(-1)] <= 15/7
```

pays both order-one source pivots.

### Exact first critical capacities

Under real nonpositive critical residues, put

```text
s_c=1/c^2,
W_c=-2F(c)/(c^2F''(c)).
```

At an odd level, the complete order-one boundary gate is

```text
sum W_c <= 1,
sum W_c s_c <= E[X]/3.
```

At an even level the right sides are `a_0` and `a_1` above.

### Trigonometric saturation

For `sin(omega z)` and regularized `cos(omega z)`, the complete source
Stieltjes measure is exactly the complete critical-residue atom measure.
Finite windows leave only a positive tail measure, and that tail tends to zero
moment by moment. The normalized critical-capacity operator equals the
identity at full exhaustion.

Thus the natural high-derivative model lies on the sharp boundary of the
source-critical capacity cone.

### Unconditional real-saddle endpoint

The positive Xi kernel has a unique large real Mellin saddle `w_s` with

```text
w_s = (1/2) log s + O(log log s),
kappa_s = (2s/w_s)(1+O(1/w_s)).
```

Real-line Laplace concentration gives, for every fixed real `a`,

```text
M_(s+a)/M_s = w_s^a (1+o(1)).
```

Consequently, for every fixed finite source order `k`, all sufficiently high
odd and even Xi derivatives have both source matrices strictly positive:

```text
FOSP105380:
  for every k there exists R_k such that r>=R_k implies
  A_k^(0)(Xi^(r))>0 and A_k^(1)(Xi^(r))>0.
```

This is an unconditional real-line theorem, marked for independent hostile
review. It does not use the proposed moving complex saddle.

The quantifier is

```text
for every k, there exists R_k,
```

not one `R` valid for all orders.

### Remaining obstruction

For each fixed high-tail order, the source sign is eventually settled. The
unresolved boundary burden is the actual critical domination

```text
C_(k,Omega)^(a) <= A_k^(a),  a=0,1,
```

plus all-order and low-order descent. Therefore

```text
CRVH105330 AND OSCC105371 -> RH
```

remains the sharp conclusion graph. Neither gate is proved.

### Replay

```text
PASS_X_105380_XI_SOURCE_MOMENT_LAYERS
122 exact rational checks
```

The replay records the odd/even concentration, critical capacity and RH flags
as false. It authenticates the algebraic layers, not the analytic real-saddle
proof.
