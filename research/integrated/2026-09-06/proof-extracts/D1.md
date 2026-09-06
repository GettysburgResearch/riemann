# Reviewer D — counterexamples and replacement statements

Status: proposed review deductions and repairs; not canonical promotion.
Scope: the exact sources in `SOURCES.tsv`, frozen from the integrated-main audit.
Baseline: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
What was run: independent bounded reconstructions in `checks.py`; see `VALIDATION.md`.
Remaining boundary: arithmetic producer estimates and RH remain unproved. An
upstream statement is not validated merely because a corrected statement exists.

Source identifiers P01–P46 and M01–M21 below resolve to exact commit, path and
blob records in [SOURCES.tsv](SOURCES.tsv). Local R/D-F labels are review IDs,
not recycled canonical claim numbers.

## R1 / D-F01 — fixed inverses do not invert a varying-order filter

**Source:** P12, L-95601, after equation (L-95601.4).

The fixed-filter theorem survives with bounded initial-interval values and an
actual subpower inverse coefficient bound. Its endpoint-dependent-order
extension does not follow from the displayed bound for each frozen order.

Let the backward difference be `Delta f_n=f_n-f_(n-1)`, with zero extension at
negative indices. Define

```
h_(3m)   = 0,
h_(3m+1) = (-2)^m,
h_(3m+2) = 2(-2)^m,
Delta^2 f_n = h_n,   f_-1=f_-2=0.
```

Choose `k_n=2` when `n=0 mod 3` and `k_n=4` otherwise. Then

```
Delta^(k_n) f_n=0  for every n>=2.
```

Indeed the residue-zero rows equal `h_(3m)=0`. For the other rows the fourth
difference equals `Delta^2 h`. At `3m+1`, with `m>=1`, this is
`(-2)^m+2(-2)^(m-1)=0`; at `3m+2` it is `2(-2)^m-2(-2)^m=0`.
The only nonzero initial output is the row at `n=1`.

The input is not subexponential: otherwise its fixed second difference would
be subexponential, contrary to `|h_(3m+1)|=2^m`. Equivalently its generating
function is

```
F(z)=(z+2z^2)/[(1+2z^3)(1-z)^2].
```

The factor `1+2z^3` has poles of modulus `2^(-1/3)` that the numerator does
not cancel. On the original scale set `F(X)=f_floor(log_2 X)` for `X>=1`,
zero below one. The output is eventually zero, but the input is not subpower.
Orders in `{2,4}` satisfy the source's proposed slow-order condition, and
both individually frozen inverses have polynomial coefficient mass.

**Replacement:** retain the fixed-order theorem. For a varying family, require
either coherent control of one fixed-order transform throughout every prefix,
or a subpower norm for the actual lower-triangular varying-row inverse. A
bound for different frozen Toeplitz inverses is not that hypothesis.

This is a synthetic function counterexample. It does not assert that the
arithmetic Q4 source has this behavior, nor reject the fixed-filter criterion.

## R2 / D-F02 — use point spectrum at the Birman–Schwinger threshold

**Source:** P20, L-91900.6.

On `ell^2(N)`, with indices `n>=1`, take

```
A=I,       G=diag(1-2^-n),
K(0)=GG*=diag((1-2^-n)^2),
H=I-G*G=diag(2^(1-n)-4^-n).
```

Every diagonal entry of H is positive, so `ker H={0}`. Nevertheless
`||(K(0)-I)e_n|| -> 0`, so `1 in spectrum(K(0))`. It is not an eigenvalue.
The spectrum strictly above one is empty, hence discrete; that condition
does not repair the threshold assertion.

The correct statement is

```
ker H != {0}  iff  1 in point_spectrum(K(0)).
```

This follows from the source's own maps `f -> Gf` and
`y -> A^-1 G*y`. To replace point spectrum by spectrum one may assume,
for example, compact K, or that 1 is an isolated spectral point with the
appropriate eigenvalue property. For unbounded A, the factorization and
inertia statement are understood on its quadratic-form domain.

The eigenvalue correspondence, positive small-gain criterion and discrete
negative-index theorem are not refuted by this example.

## R3 / D-F03 — all principal minors, not just leading ones

**Resident source:** P34, the certificate-boundary paragraph in section 3.

For a finite Hermitian matrix H,

```
H is PSD  iff  every principal minor is nonnegative.
```

One proof of the less immediate direction is the identity

```
det(tI+H)=sum_(I subset {1,...,n}) t^(n-|I|) det H[I].
```

If all principal minors are nonnegative, the empty-set term `t^n` makes
this determinant strictly positive for every `t>0`. A negative eigenvalue
of H would make it zero at a positive t, a contradiction. The other direction
follows by restricting a positive semidefinite form to coordinate subspaces.

Thus a negative principal minor is both sufficient and necessary for non-PSD.
It need not be a **leading** principal minor. For `diag(0,-1)` all leading
principal determinants vanish, but the second singleton minor is negative.

**Replacement sentence:** “A negative principal minor is a complete finite
non-PSD witness; checking only leading principal minors is insufficient for
semidefiniteness. Exact inertia or LDL with appropriate pivoting is an
efficient complete alternative.” The Hermite inertia theorem itself survives.

## R4 / D-F04 — repair the wavelet energy, then recover the literal criterion

**Sources:** P13 section 5 and P14 equations L-100130.2–L-100130.3.

Write

```
a=X/8,
d_X(n)=mu(n)n^(-1/2) K_0(X/n),
G(X)=sum_n d_X(n),
S_X(v)=sum_(n>=v) d_X(n).
```

The finite support is contained in `[a,X]`. For any such complex coefficient
packet and any `tau>0`, expansion of the square gives

```
sum_(m,n) d_m conjugate(d_n) min(m,n)^(2tau)
 = a^(2tau)|sum d_n|^2
   +2tau int_a^X |S_X(v)|^2 v^(2tau-1) dv.             (R4.1)
```

This is the identity `min(m,n)^(2tau)=a^(2tau)+int_a^min(m,n)
2tau v^(2tau-1)dv`, followed by finite summation.

At `tau=1`, P14's Cauchy average is exactly the left side: its coefficients
are `n d_X(n)`, and the Cauchy characteristic function contributes
`exp(-|log(m/n)|)=min(m,n)/max(m,n)`. Therefore

```
Q_P(X)=a^2 |G(X)|^2 + 2 int_a^X |S_X(v)|^2 v dv.
```

P13 instead defines

```
Q_old(X)=|G(X)|^2 + 2 int_a^X |S_X(v)|^2 v dv.
```

Their difference is `(a^2-1)|G(X)|^2`; they are not identical. The new exact
rational interval calculation proves `G(16)>0`, approximately
`0.0107400328395`. Consequently `Q_P(16)-Q_old(16)=3G(16)^2>0`, approximately
`0.0003460449162`. Full rational endpoints are in the replay output. This is
an actual finite Mobius-source mismatch, not merely an arbitrary-vector test.

### The literal old MWOC criterion still has a proof

The false identity must be removed, but it is unnecessary to discard the
literal old criterion. Here is a separate replacement proof. Define

```
A_X(r)=sum_(n>=rX) mu(n)n^(-1/2) K_0(X/n),  1/8<=r<=1,
H=L^2([1/8,1],2r dr).
```

Changing variable `v=rX` gives exactly

```
Q_old(X)/X^2=|G(X)|^2/X^2 + ||A_X||_H^2.              (R4.2)
```

Assume the literal source premise, with its original normalization,

```
int_2^Y sqrt(Q_old(X))/(X/8) dX/X = Y^o(1).            (R4.3)
```

Here and below subpower means an upper bound for every positive exponent,
not a positive asymptotic equality. For each fixed `g in H`, Cauchy–Schwarz
and (R4.2) give subpower cumulative absolute logarithmic mass for

```
f_g(X)=int_(1/8)^1 A_X(r) conjugate(g(r)) 2r dr.
```

Abel summation therefore makes the actual Mellin transform of f_g holomorphic
in `Re s>0`. Initially in `Re s>1/2`, absolute source Fubini gives

```
M[f_g](s)=Khat_g(s)/zeta(s+1/2),
K_g(y)=K_0(y) int_(1/8)^(1/y) conjugate(g(r)) 2r dr,
1<=y<=8.                                             (R4.4)
```

For every complex s, not all these compact Mellin multipliers can vanish.
If they did, duality in H would force

```
Phi_s(r)=int_1^(1/r) K_0(y)y^(-s-1)dy =0
```

almost everywhere and then everywhere, by continuity. But its a.e.
derivative is

```
Phi_s'(r)=-K_0(1/r) r^(s-1),
```

which is not identically zero because K_0 is a nonzero compact kernel.
This is a contradiction.

If zeta had a zero rho with `Re rho>1/2`, some fixed g would therefore have
`Khat_g(rho-1/2)!=0`. Equation (R4.4) would have a pole in the region where
the actual Mellin integral is holomorphic. Multiplicity only increases its
order. Reflection then yields RH.

The tests need not be invented after a hypothetical zero: fix once and for
all a countable dense family of rational complex step functions in H. A
nonzero continuous linear functional is nonzero on at least one member of
that family. The single norm premise controls every member simultaneously.

Conversely, under the classical RH Mertens estimate
`M(t)=O_epsilon(t^(1/2+epsilon))`, partial summation gives

```
sup_(1/8<=r<=1) |A_X(r)| + |G(X)| = O_epsilon(X^epsilon).
```

The compact kernel is fixed and piecewise smooth; a moving suffix endpoint
adds only a uniformly bounded variation term. Equation (R4.2), followed by
integration with a smaller exponent, proves (R4.3).

**Conclusion:** the old criterion remains RH-equivalent by this suffix-field
argument. The corrected Poisson energy has its separate correct identity.
Neither energy estimate is proved. This argument does not assert pointwise
comparability of the two energies, nor discharge the general reciprocal-zeta
vertical-growth input in P15's quantitative abscissa theorem.

## R5 / D-F05 — restore n>=2 in the matched-pole annihilator

**Sources:** resident P32 section 6 versus original P33, which explicitly
requires `n>=2`.

Keep the source notation `P(z)=prod(z-x_i)`, `w_i=1/P'(x_i)`,
`alpha_i=x_i/(x_i^2-d)`, `S0=sum w_i alpha_i`,
`S1=sum w_i x_i alpha_i`, `D=prod(x_i^2-d)` and
`c_i=D w_i(S1-S0 x_i)`. For one node c is identically zero. Its claimed
negative normalization cannot equal -1. This is a lost integration hypothesis,
not an error in the original statement.

For completeness, the corrected normalization has a direct proof. Let
`a=sqrt(d)`, and put `A=sum w_i/(x_i^2-d)`. When `n>=2`, `sum w_i=0`, so
`S1=dA`. Partial fractions give

```
S0+aA = -1/P(a),
S0-aA = -1/P(-a),
P(a)P(-a)=D.
```

Thus `dA^2-S0^2=-1/D` and

```
sum c_i/(x_i^2-d)=D(S1 A-S0^2)=-1,
sum c_i x_i/(x_i^2-d)=D(S1 S0-S0 S1)=0.
```

Polynomial moments through degree `n-3` vanish by the usual barycentric
identity `sum w_i x_i^j=0` for `j<=n-2`. The isolated modeled pair has
quadratic value `-2md`. All other actual xi contributions remain present.

## R6 / D-F06 — state the Robin tail caps and feasibility explicitly

**Sources:** resident P29 section 5 versus original P31.

The resident dynamic program uses `n_r` without defining it and omits the
original nonempty-subtree condition. Restore the following contract:

```
A>=1, R=prod_i q_i <= M=floor(B/P), M0=floor(M/R),
A>=m_1>=...>=m_n>=1,
b_i<=m_i for every admissible completion,
n_r=#{i:m_i>=r}.
```

The caps must be certified for the actual bounded subtree. Taking all caps
`m_i=A`, hence `n_r=n`, is a valid weaker alternative. If `R>M`, the subtree
is empty and is disposed of before this positive-budget formula is used.
For A=1 the dynamic program is the empty product 1.

With these hypotheses the source's nested-level proof is valid: every legal
sequence of active prefix lengths is included in the backward maximization,
and its cost product is at most M0. Thus `J(b)^d <= M0^a V`, giving the
stated powered abundancy envelope.

The independent exact fixture uses `P=16`, tail `(3,5,7)`, `B=8400`,
`M0=5`, caps `(2,2,1)`, and `(a,d)=(1,64)`. It verifies

```
U < (39/10)^64 < (12493/3150)^64,
max actual abundancy =403/105.
```

This is a definition/contract repair. It neither rejects the envelope nor
claims a new large Robin verification range.

## R7 / D-F07 — charge both boundary components in the excursion inequality

**Source:** P45, L-101103.4.

On logarithmic coordinates let `f(u)=u-1` and `log Y=2`. Its negative mass is
1/2, and there is no terminal negative component. If the initial component
is omitted from the interior sum, the printed right side is zero. If it is
included as length one with derivative energy one, the right side is
`1/pi<1/2`. In either reading the stated general finite inequality fails:
the value at its initial endpoint is -1 rather than zero.

Let `B_partial(Y)` be the total negative mass in all components meeting
`0` or `log Y`, counting a component meeting both endpoints only once. Let
L_int and V_int sum only genuine interior excursions whose two endpoint
values are zero. The valid formula is

```
int_0^(log Y) f_- du
 <= (1/pi) L_int(Y)^(3/2) V_int(Y)^(1/2) + B_partial(Y).
```

On each interior interval, Dirichlet Poincare and Cauchy–Schwarz give
`int f_- <= ell^(3/2)||f'||_2/pi`. Sum by Cauchy–Schwarz and use
`sum ell^3 <= (sum ell)^3`. Add the boundary integrals exactly. Alternatively,
assume `f(0)>=0` in the original theorem.

For a single fixed locally absolutely continuous f, the initial component
that ends at a finite point contributes only a fixed finite constant C_f.
If it never ends it is already the terminal component at every horizon.
Thus the asymptotic implication can also be repaired by adding C_f.

A separate scope correction is immediate: `L_int(Y)<=log Y`. Its subpower
condition is automatic. After the endpoint repair, the source's
`V(Y)+B(Y)=Y^o(1)` premise alone implies subpower negative mass. The assertion
that neither premise alone suffices is false at this stated normalization.
Main already warns that subpower log-length is not an independent key;
this review additionally identifies the missing initial boundary term.

## R8 — first-chaos support is not input-Gram domination

**Source:** P37. This is a contract clarification, not a counterexample to a
fully specified conservative colligation.

An orthogonal expansion `K_r=sum_(m>=1) r^m K_m`, with every K_m PSD and
`K_r=rK_1`, forces K_m=0 for m>=2. It does not by itself prove that the
remaining features Y_x are the image of the particular source vectors h_x
under a contraction. The rescaling `Y_x=2h_x` is still pure first chaos and
linear in intensity; its Gram is four times the source Gram.

The exact sufficient and necessary family condition for such a contraction is

```
Gram(Y_x:x in packet) <= Gram(h_x:x in packet)
```

for every finite packet. Define `C(sum c_i h_i)=sum c_i Y_i`. The inequality
makes this well-defined on the source span and bounded by one; completion
extends it. Conversely every contraction gives this inequality. Equal Grams
give an isometry on the closed source span.

If “conservative source-linear colligation” is intended to include this
property, state it explicitly. Do not derive it merely from chaos support.

## R9 — quantify regional Schur estimates uniformly when the partition grows

**Source:** P46. The displayed pointwise and integrated Schur estimates are
valid; the implication for a growing number of regions needs uniformity.

For `j>=0`, let region j contain only entry `(2j,2j+1)` of a matrix, equal to
`-2^j` when `2^j<=X<2^(j+1)` and zero otherwise. At that scale take unit
vectors a and b selecting that entry, and take `F(X)=-2^j`. Each matrix has
only one active entry, and regions are disjoint. Then

```
int_1^Y R_j dX/X = int_1^Y C_j dX/X = 2^j log 2
```

once `Y>=2^(j+1)`. For every fixed j their product is a bounded constant,
hence subpower in Y. At `Y=2^N`, only N regions contribute, but

```
int_1^Y F_- dX/X=(2^N-1)log 2.
```

Thus a subpower region count and pointwise-in-fixed-region estimates do not
control the total. This is a synthetic matrix counterexample to that reading,
not a statement about the native arithmetic entries.

**Replacement:** for every epsilon>0 require one constant valid for all
regions active below Y, together with a subpower count, or directly require

```
sum_nu sqrt[(int_1^Y R_nu)(int_1^Y C_nu)] = Y^o(1).
```

For a fixed finite partition, pointwise regional subpower bounds suffice;
there is no such quantifier problem in that case.

## R10 — the complete first-Hermite domain remains necessary

**Sources:** P27, P28, M13.

The criterion quantifies over all q>0 and all real centers x, or the proved
countable equivalent. A large-center result below
`q=(4-epsilon)loglog|x|` removes that region only. A condition merely on a
thin transition curve is not the remaining full criterion: bounded centers
and arbitrarily large q at each such center must still be controlled.

State the open gate on the entire complement of the already proved region,
or provide a new propagation theorem from the thin boundary to that
complement. D supplies no such propagation theorem and no counterexample to
the actual first-Hermite sign; this is a quantifier boundary.
