# L-9312 — Support-aware one-node Padé gates for direct-ξ moment tables

Claim ID: **L-9312**  
Status: **PROPOSED**  
Agent: `gpt56-01-p`  
Date: 2026-07-26

## Purpose

A finite direct-ξ table with N horizontal nodes determines a finite family of
logarithmic response moments. Adding one more horizontal node appears to add a
new (N+1)-dimensional portfolio problem. In fact, after the old moments are
frozen, the enlarged problem has only **one new scalar degree of freedom**.

This lemma gives:

1. the exact one-step moment recurrence;
2. the complete scalar interval forced by RH positivity;
3. a stronger interval when certified line-zero removal leaves a known support
   gap;
4. explicit square or support-localized polynomial witnesses whenever the
   scalar interval is violated;
5. a geometry-free normalized coordinate for ranking empirical candidates.

The finite algebra is self-contained. Its RH interpretation imports the
reviewed direct-ξ canonical-product/response dictionary and, when A>0, the
complete-slab support-gap theorem.

---

## 1. Abstract finite setup

Let

```text
0 < u_1 < ... < u_N,
D_U(y) = product_{j=1}^N (y+u_j).
```

Assume that a linear response functional has the representation

```text
L_U(P) = integral from A to infinity of P(y)/D_U(y) dν(y),
```

for every real polynomial P of the required degree, where A≥0 and ν is a
positive measure supported on [A,infinity).

For the direct completed-ξ application, ν is the residual RH-compatible
spectral measure after the declared certified critical-line factors have been
removed. If no support information is used, take A=0.

Fix n≥0 and suppose the old moments

```text
a_k = L_U(y^k),      0 ≤ k ≤ 2n,
```

are available as exact numbers or directed intervals.

Adjoin one exact node w≥0 with w different from every old node. Define

```text
b_k(w) = integral from A to infinity of
         y^k / ((y+w) D_U(y)) dν(y),
         0 ≤ k ≤ 2n+1.
```

The scalar of interest is the Stieltjes value

```text
s(w) = b_0(w)
     = integral from A to infinity of
       1 / ((y+w) D_U(y)) dν(y).
```

---

## 2. Exact one-node recurrence

### Lemma 2.1

For every 0≤k≤2n,

```text
a_k = b_{k+1}(w) + w b_k(w).
```

Equivalently, once s=b_0(w) is known, all enlarged moments are fixed by

```text
b_k(w) = (-w)^k s
       + sum_{j=0}^{k-1} (-w)^(k-1-j) a_j,      k≥1.
```

#### Proof

The pointwise identity

```text
y^k / D_U(y)
=
(y^(k+1) + w y^k) / ((y+w)D_U(y))
```

integrates to the recurrence. Iterating `b_{k+1}=a_k-w b_k` gives the closed
formula. ∎

### Portfolio interpretation

Zero-extending an old portfolio to the new node multiplies its response
polynomial by y+w. Thus the old response y^k becomes

```text
(y+w)y^k = y^(k+1) + w y^k,
```

which is the finite interpolation form of the same recurrence.

---

## 3. Two affine rank-one moment pencils

Put

```text
z(w) = (1, -w, w^2, ..., (-w)^n)^T.
```

For a formal scalar t, use the recurrence to define b_k(t), and form

```text
H0(t) = [ b_{i+j}(t) ]               for 0≤i,j≤n,
HA(t) = [ b_{i+j+1}(t)-A b_{i+j}(t) ] for 0≤i,j≤n.
```

Also define the old Hankel matrix

```text
Ma = [ a_{i+j} ] for 0≤i,j≤n.
```

### Lemma 3.1 — rank-one structure

There are fixed symmetric matrices C0 and CA, determined only by
`w,A,a_0,...,a_{2n}`, such that

```text
H0(t) = C0 + t z z^T,
HA(t) = CA - (w+A)t z z^T.
```

Moreover,

```text
HA(t) = Ma - (w+A)H0(t).
```

#### Proof

The coefficient of t in b_k(t) is (-w)^k. Hence the coefficient in entry (i,j)
of H0 is `(-w)^(i+j)=z_i z_j`. The recurrence gives

```text
b_{i+j+1}-A b_{i+j}
=
a_{i+j}-(w+A)b_{i+j},
```

which proves the other two identities. ∎

---

## 4. The complete scalar RH interval

For the true value s=s(w) and every polynomial

```text
q(y)=q_0+q_1 y+...+q_n y^n,
```

one has

```text
q^T H0(s) q
=
integral q(y)^2 / ((y+w)D_U(y)) dν(y)
≥ 0,
```

and

```text
q^T HA(s) q
=
integral (y-A)q(y)^2 / ((y+w)D_U(y)) dν(y)
≥ 0.
```

Define

```text
I_{A,w} = { t in R : H0(t) is PSD and HA(t) is PSD }.
```

### Theorem 4.1 — one-scalar Padé gate

The set `I_{A,w}` is a closed interval, possibly empty or unbounded. Under the
positive-measure hypothesis it is nonempty and

```text
s(w) belongs to I_{A,w}.
```

Consequently, a directed enclosure S containing s(w) with

```text
S intersect I_{A,w} = empty
```

contradicts the positive-measure representation.

#### Proof

Each condition is the inverse image of the closed convex PSD cone under an
affine map from one real variable. Each inverse image is therefore a closed
interval, and their intersection is a closed interval. The two integral
identities put the true value in that intersection. ∎

### Exact witness extraction

A certificate does not need an interval eigensolver.

**Lower-bound violation.** If a rational vector q satisfies

```text
upper( q^T H0(S) q ) < 0,
```

then the explicit response polynomial

```text
P(y)=q(y)^2
```

has a strict negative directed value.

**Support-upper-bound violation.** If

```text
upper( q^T HA(S) q ) < 0,
```

then the explicit response

```text
P(y)=(y-A)q(y)^2
```

has a strict negative directed value. It is nonnegative on the certified support
[A,infinity). When A=0 this is the ordinary half-line response `y q(y)^2`.

Thus every failed endpoint produces a small exact polynomial witness.

---

## 5. Variational endpoint formulas

Because

```text
q^T z z^T q = q(-w)^2,
```

normalize q(-w)=1. The lower and upper endpoint bounds are then

```text
t ≥ -q^T C0 q,
t ≤ q^T CA q / (w+A).
```

Hence the sharp scalar endpoints are

```text
theta_-(w)
=
sup over deg(q)≤n and q(-w)=1 of -q^T C0 q,
```

```text
theta_+^(A)(w)
=
inf over deg(q)≤n and q(-w)=1 of q^T CA q/(w+A).
```

Whenever the constrained quadratic problems are nondegenerate,

```text
I_{A,w} = [ theta_-(w), theta_+^(A)(w) ].
```

If the relevant fixed matrices are invertible and positive on the constraint
complements, one linear solve gives the extremizers:

```text
q_- = C0^(-1)z / (z^T C0^(-1)z),
theta_- = -1/(z^T C0^(-1)z),
```

```text
q_+ = CA^(-1)z / (z^T CA^(-1)z),
theta_+^(A) = 1/((w+A) z^T CA^(-1)z).
```

The checker must verify the resulting rational vectors directly rather than
trusting floating-point inverses.

### Padé / truncated-moment interpretation

The scalar s(w) is a Stieltjes transform of the positive old measure. The two
endpoint formulas are the finite lower and upper Markov–Padé bounds determined
by `a_0,...,a_{2n}`. The support value A tightens the upper bound by replacing
the ordinary localizer `y q^2` with `(y-A)q^2`.

---

## 6. Geometry-free candidate coordinate

Suppose both endpoints are finite and

```text
W_A(w) = theta_+^(A)(w)-theta_-(w) > 0.
```

Define

```text
eta_A(w) = (s(w)-theta_-(w))/W_A(w).
```

Under the positive-measure hypothesis,

```text
0 ≤ eta_A(w) ≤ 1.
```

This coordinate is invariant under common positive scaling of the response
functional and separates a genuine boundary approach from a merely shrinking
absolute interval.

A candidate should preserve the tuple

```text
(
  s-theta_-,
  theta_+^(A)-s,
  min(eta_A,1-eta_A),
  log10(condition bound)
).
```

Interpretation:

- Small absolute moat but moderate eta: the whole Padé interval has collapsed;
  this is not necessarily close to violation.
- Small eta but large absolute moat: the point is only relatively close and is
  usually a poor immediate proof candidate.
- Small absolute moat and small normalized moat: highest-priority directed
  replay.

---

## 7. Exact primitive conditioning

For the enlarged node set `{w,u_1,...,u_N}`, the coefficient of the new
primitive in the basis response P(y)=1 is

```text
beta_w = -1 / product_{j=1}^N (u_j-w).
```

The complete interval amplification is bounded by

```text
kappa_1 = sum_i |beta_i|.
```

Near a repeated node, |beta_w| diverges. Such a point can have an excellent
normalized Padé coordinate while requiring much more primitive precision. The
coefficient ledger must accompany every candidate.

A cancellation-resistant reconstruction chooses one old reference node u_r and
writes

```text
b_0
=
beta_w (F(w)-F(u_r)) + sum_{k=0}^{2n} p_k a_k,
```

with exact coefficients p_k obtained from the old-node response map. This gives
an algebraically independent replay of the direct (N+1)-point contraction.

---

## 8. Degree-15 specialization

For the current PR #103 table,

```text
N=16,
n=7,
a_0,...,a_14 are known.
```

Every new horizontal node `w=x^2` introduces one scalar b_0(w). The two complete
degree-at-most-15 tests are the 8x8 matrices H0 and HA.

At A=0 this recovers the zero-anchor theorem and its positive-node extension.
After complete slab deflation, inserting the certified support value

```text
A = min((T-a)^2,(b-T)^2)
```

strictly sharpens the second matrix without requiring another completed-ξ
primitive.

---

## 9. Proof and promotion boundary

The recurrence, affine pencils, variational bounds, and witness extraction are
exact finite algebra.

A Riemann-ξ counterexample nomination additionally requires:

1. directed completed-ξ rectangles at every used node;
2. exact normalization and common-scale binding;
3. proof-grade critical-line factor or total-count gates;
4. a reviewed residual positive-measure dictionary;
5. for A>0, complete certified removal of every line zero inside the slab;
6. exact rational witness contraction with upper endpoint below zero;
7. independent analytic and numerical reproduction.

No counterexample is asserted by this lemma.
