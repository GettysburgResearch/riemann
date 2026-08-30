# Exactly which circle probes detect multiplicative recurrence rigidity?

Status: **proposed exact companion theorem; external novelty unreviewed**.
Scope: continuous multiplicative complex maps and ordinary generating
series along irrational circle rotations. No natural-boundary, global
L-function, or zero-location theorem is claimed.

Frozen precursor: `8834fdc7a0dfe15f6bb95eefe0729cb77c93c807`, including the
reviewed proof and zero-endpoint-hardened replay of
[multiplicative recurrence rigidity](MULTIPLICATIVE_RECURRENCE_AND_MIXED_PARENTS.md).
This companion leaves that source unchanged.

## 1. Complete classification by the geometry of one probe

Every continuous multiplicative `Phi:C->C` with `Phi(1)=1` is either the
constant map one, or uniquely

\[
 \Phi(re^{it})=\exp(a\log r)e^{ikt}\quad(r>0),\qquad
 \Phi(0)=0,
 \qquad \operatorname{Re}a>0,\ k\in\mathbb Z.
\tag{1.1}
\]

This is the coordinate classification proved in the precursor. Conversely
every map in (1.1) is continuous and multiplicative, including at zero.
In particular arbitrary imaginary parts of `a` are allowed at this stage.
The constant one has value one, not zero, at zero.

Fix `theta/(2pi)` irrational and `c>=0`, and sample

\[
 b_r=\Phi(c+e^{ir\theta}),\qquad r\ge0.
\tag{1.2}
\]

### Theorem GLO764.PROBE.CIRCLE_GEOMETRY_CLASSIFICATION

For the constant map, every probe has order one. For a nonconstant map
(1.1), the exact rationality classification is:

| Probe | Necessary and sufficient condition for recurrence | Minimal order |
|---|---|---|
| `c=0` | every `a,k` allowed by (1.1) | `1` |
| `c=1` | `a=N` is a positive integer and `k=N mod 2` | `N+1` |
| `c>0, c!=1` | `a=m+n`, `k=m-n` for integers `m,n>=0`, `m+n>0` | `m+n+1` |

“Recurrence” means eventual constant-coefficient recurrence, equivalently
rational ordinary generating series. At `c=1` **there is no condition
`|k|<=N`**. Those unbounded angular weights are the full family of false
positives left by an origin-touching circle.

## 2. The origin-touching proof, including every exceptional case

The precursor's dense-orbit argument applies to every continuous function
on the circle, even when it vanishes. Therefore recurrence in (1.2)
forces `Phi(1+w)` on `|w|=1` to be a nonzero Laurent polynomial `P(w)`.
Nonzero follows from its value at `w=1`, namely `Phi(2)!=0`.

Near `w=1`, choose the ordinary analytic logarithms of `w` and `1+w`.
For `w=exp(it)` with `t` near zero,

\[
 1+e^{it}=2\cos(t/2)e^{it/2}.
\]

Consequently the holomorphic germ

\[
 F(w)=(1+w)^a w^{(k-a)/2}
\tag{2.1}
\]

agrees with `Phi(1+w)` on that arc. Since `P` agrees with the same arc,
the identity theorem gives equality of their germs. Thus, as rational
functions,

\[
 \frac{P'(w)}{P(w)}=\frac{a}{1+w}+\frac{k-a}{2w}.
\tag{2.2}
\]

At the nonzero point `w=-1`, the residue of a Laurent polynomial's
logarithmic derivative is a nonnegative integer zero multiplicity, so
`a=N in Z_{>=0}`. Since this is the nonconstant case, `Re(a)>0` forces
`N>=1`. At zero a Laurent polynomial may have either a zero or a pole;
the residue is an arbitrary integer. Hence `j=(k-N)/2 in Z`. No
nonnegativity condition on `j` is available or justified.

Conversely, for any `N>=1` and any integer `j`, take `k=N+2j`. On the
whole unit circle one has

\[
 \Phi(1+w)=w^j(1+w)^N
        =\sum_{i=0}^N\binom Ni w^{j+i}.
\tag{2.3}
\]

The equality follows first on the arc `-pi<t<pi` from (2.1). At `w=-1`
both sides are zero, so continuity completes it. Each coefficient in
(2.3) is nonzero, and irrationality makes the `N+1` sampled characteristic
roots distinct. Summing their geometric series gives the exact order.

The constant map one is handled separately: (2.3) with `N=0,j=0` gives
it, but `N=0,j!=0` does **not** define a continuous map on all of `C`.
Such a map would have unit modulus at nonzero points approaching zero
while its angular values differ. No zero-value convention repairs that
discontinuity. This proves the middle row of Theorem 1.

For `c=0`, (1.2) is simply `exp(ikr theta)`, proving the first row.

## 3. The held-out inside-origin circles: `0<c<1`

The original theorem used `c>1`, where the two factors `c+w` and
`c+w^(-1)` have convenient logarithms. For `0<c<1` the geometry is
different: the circle winds around zero. One must keep its integral
angular character instead of pretending the same logarithms exist.

Put `mu=(a+k)/2`, `nu=(a-k)/2`. On the nonempty annulus
`c<|w|<1/c`, the logarithms of `1+c/w` and `1+cw` are defined by their
power series. The single-valued nonzero holomorphic function

\[
 F(w)=w^k\exp\{\mu\log(1+c/w)+\nu\log(1+cw)\}
\tag{3.1}
\]

equals `Phi(c+w)` on `|w|=1`, by multiplicativity applied to
`c+w=w(1+c/w)`. The factor `w^k` is single valued precisely because
`k` is an integer.

If the sampled sequence is recurrent, the dense-orbit lemma again makes
`F` a Laurent polynomial on the annulus. Logarithmic differentiation gives

\[
 \frac{F'(w)}{F(w)}
 =\frac{\mu}{w+c}-\frac{\nu}{w(cw+1)}.
\tag{3.2}
\]

The residues at the distinct nonzero points `-c` and `-1/c` are
`mu` and `nu`. A Laurent polynomial forces both to be nonnegative
integers, exactly as in the `c>1` proof. Their distinctness, not which
side of the unit circle contains which point, is decisive.

Conversely, for `Phi(z)=z^m bar z^n`,

\[
 \Phi(c+w)=(c+w)^m(c+w^{-1})^n.
\tag{3.3}
\]

For every `c>0` its Laurent coefficients at all exponents `-n,...,m`
are positive. Thus the order is exactly `m+n+1`. At `c=0` all but the
single exponent `m-n` disappear. Together with the frozen `c>1` proof,
this proves the final row and completes Theorem 1.

## 4. What the degeneracy permits, and what moving the circle removes

For each fixed integer `N>=1`, the origin-touching probe accepts infinitely
many different maps of order `N+1`, indexed by `k=N+2j`, `j in Z`.
Only those with `|k|<=N` are global polynomials in `z,bar z`. For every
other accepted map, recurrence fails at **every** positive `c!=1`.
This is an all-parameter statement proved by distinct residues, not
inferred by looking at nearby circle centers.

The complete nonconstant picture for a fixed map is therefore:

- polynomial maps recur for every center;
- an exotic `a=N,k=N mod 2,|k|>N` map recurs exactly at `c=0,1`;
- every other allowed map recurs only at `c=0`.

For arbitrary center `C in C` and radius `R>0`, rotate and multiply by
the nonzero scalar `R`: multiplicativity changes the samples only by a
nonzero scalar and an orbit phase shift. Hence the same classification
depends only on `c=|C|/R`. The two exceptional geometries are a circle
centered at zero and a circle passing through zero.

The finite triangular moduli count and local-constancy proof in the
precursor apply to the **nondegenerate** probes. They must not be copied
to the `c=1` chamber: bounded order there leaves infinitely many angular
weights. No general local-constancy assertion for pointwise-continuous
families over arbitrary parameter spaces is made here.

### Corollary GLO764.PROBE.CONNECTED_DEGENERATE_FAMILIES

Let `X` be a connected topological space and let `x -> Phi_x` be a family
of continuous normalized multiplicative maps. Suppose that for every fixed
`z in C`, the evaluation `x -> Phi_x(z)` is continuous, and that every
`Phi_x` passes the origin-touching irrational probe. Then the family is
constant. No uniform order bound is required.

Indeed Theorem 1 assigns integers `(N_x,k_x)`, with `N_x>=1` and matching
parity, or `(0,0)` for the constant-one map. Evaluation at two gives
`Phi_x(2)=2^{N_x}`. Its image lies in the discrete subset
`{1,2,4,8,...}`, so connectedness fixes `N_x=N`. For each positive integer
`q`, evaluation at `zeta_q=exp(2pi i/q)` gives
`Phi_x(zeta_q)=zeta_q^{k_x}` in the finite set of `q`th roots of unity.
Connectedness fixes this value as well. Therefore for any `x,y in X`,
the difference `k_x-k_y` is divisible by every positive integer `q`, and
must be zero. Thus `(N_x,k_x)` is constant and determines the entire map.

This argument uses every root-of-unity evaluation to prove constancy on
a connected space. It does not infer local discreteness of the infinite
angular-weight set from one irrational evaluation. In particular it does
not reinstate the precursor's stronger local-constancy claim in the
arbitrary pointwise topology. Nor is a finite list of these evaluations
sufficient: for fixed `N`, replacing `k` by
`k+2*lcm(q_1,...,q_s)` preserves parity and all selected root-of-unity
values, while changing the map.

## 5. Replay and provenance

`circle_probe_geometry.py` authenticates the frozen precursor note and
producer before importing its exact Gaussian-rational arithmetic. It
replays positive/negative angular-weight examples on rational unit-circle
points, explicitly includes the point `w=-1`, compares polynomial probes
at `c=0,1/2,1,2`, and records finite specializations of the residue
classification with rigorous scope labels.

The checker uses no numerical evaluation of noninteger powers. Its
nonrational rows are **specializations of the proved theorem**, not
analytic certificates manufactured from finite samples. All hard bounds
are small, and Boolean/float/oversized requests are rejected.

The Fourier, character, and rational-function ingredients are classical;
the primary-literature boundary is the one documented in the frozen
precursor. This companion claims an exact repository classification of
probe degeneracy and no external publication priority. It provides no
prime-indexed family, conductor, gamma completion, or RH/GRH consequence.
