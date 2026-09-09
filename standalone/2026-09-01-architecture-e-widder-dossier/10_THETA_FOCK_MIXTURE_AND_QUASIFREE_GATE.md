# Theta–Fock mixture and the one-determinant gate

Status: **PROPOSED EXACT SOURCE DECOMPOSITION AND RH-EQUIVALENT CONSTRUCTIVE GATE; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

The invariant count law of
[`09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md`](09_INVARIANT_ORDER_PRODUCT_AND_COUNT_LAW.md)
has a direct decomposition from the actual theta source.  Every conditional
fiber is an explicit Poisson-binomial, or fermionic quasi-free, count.  The
completed Riemann law is a positive mixture of those fibers.  RH is equivalent
to that particular mixture collapsing to one quasi-free determinant.

This is more specific than asking for an abstract Stieltjes measure.  It
identifies the source variables, the conditional eigenvalues, the latent
selector and the precise closure theorem that would finish Architecture E.

## 1. Logarithmic theta coordinate

Use

\[
 \psi(t)=\sum_{m\ge1}e^{-\pi m^2t}
\]

and set `t=e^(2 tau)` in the split xi integral.  Then

\[
 \boxed{
 \mathfrak X(v)
 =\frac12
 +2v\int_0^\infty
 e^{\tau/2}\psi(e^{2\tau})
 \cosh\left(\tau\sqrt{v+\frac14}\right)d\tau.
 }
 \tag{1.1}
\]

All terms are positive for `v>0`.

For fixed `tau>0`, the entire function

\[
 v\longmapsto
 \cosh\left(\tau\sqrt{v+\frac14}\right)
\]

has the simple negative zeros

\[
 -A_j(\tau),
 \qquad
 \boxed{
 A_j(\tau)=\frac14+
 \frac{\pi^2(j+1/2)^2}{\tau^2},
 \quad j\ge0.
 }
 \tag{1.2}
\]

Its order is `1/2`, so the genus-zero product is

\[
 \boxed{
 \frac{\cosh(\tau\sqrt{v+1/4})}{\cosh(\tau/2)}
 =\prod_{j\ge0}\left(1+\frac{v}{A_j(\tau)}\right).
 }
 \tag{1.3}
\]

## 2. Every theta fiber is Poisson-binomial

Fix `v>0` and define

\[
 \boxed{
 p_j(\tau;v)=\frac{v}{v+A_j(\tau)}\in(0,1).
 }
 \tag{2.1}
\]

Then, for every complex `z`,

\[
 \boxed{
 \frac{\cosh(\tau\sqrt{vz+1/4})}
      {\cosh(\tau\sqrt{v+1/4})}
 =\prod_{j\ge0}
  \bigl(1-p_j(\tau;v)+p_j(\tau;v)z\bigr).
 }
 \tag{2.2}
\]

The sum of the `p_j` is finite.  Thus the right side is the pgf of

\[
 \sum_{j\ge0}B_j(\tau;v),
\]

where the `B_j` are independent Bernoulli variables with the displayed
probabilities.

The extra factor `v` in (1.1) becomes one forced Bernoulli of parameter one.
Consequently the conditional source count is

\[
 \boxed{
 N_{v,\tau}=1+\sum_{j\ge0}B_j(\tau;v).
 }
 \tag{2.3}
\]

This is a literal quasi-free fermionic occupation law: its one-particle
contraction is diagonal with eigenvalues

\[
 1,p_0(\tau;v),p_1(\tau;v),\ldots.
\]

## 3. The completed count law is an explicit positive mixture

Normalize by `mathfrak X(v)` and define the subprobability measure

\[
 \boxed{
 d\nu_v(\tau)
 =\frac{2v}{\mathfrak X(v)}
 e^{\tau/2}\psi(e^{2\tau})
 \cosh\left(\tau\sqrt{v+\frac14}\right)d\tau.
 }
 \tag{3.1}
\]

Its total mass is

\[
 \nu_v((0,\infty))
 =1-\frac1{2\mathfrak X(v)}.
\]

The invariant count law has the exact decomposition

\[
 \boxed{
 \frac{\mathfrak X(vz)}{\mathfrak X(v)}
 =\frac1{2\mathfrak X(v)}
 +\int_0^\infty
 z\prod_{j\ge0}
  \bigl(1-p_j(\tau;v)+p_j(\tau;v)z\bigr)
 d\nu_v(\tau).
 }
 \tag{3.2}
\]

Equivalently:

```text
with probability 1/[2 mathfrak X(v)], N_v=0;
otherwise choose tau from the explicit theta density;
conditionally, N_v=1+an independent Bernoulli string.
```

No zero of zeta occurs in this representation.  The source labels are the
literal theta scale `tau` and the half-integer spectral modes `j+1/2`.

## 4. The one-determinant theorem that would prove RH

For fixed `tau`, let `K_(v,tau)` be the diagonal positive contraction with
eigenvalues

\[
 1,p_0(\tau;v),p_1(\tau;v),\ldots.
\]

Then

\[
 z\prod_j(1-p_j+p_jz)
 =\det(I-K_{v,\tau}+zK_{v,\tau}).
\]

Equation (3.2) is therefore a positive arithmetic mixture of Fredholm
determinants:

\[
 P_v(z)
 =\frac1{2\mathfrak X(v)}
 +\int\det(I-K_{v,\tau}+zK_{v,\tau})d\nu_v(\tau).
 \tag{4.1}
\]

The constructive completion theorem is now exact.

### Theta quasi-free gate `TQF(v)`

Construct, directly from the theta source in (3.1), one positive trace-class
contraction `K_v` such that

\[
 \boxed{
 \frac{\mathfrak X(vz)}{\mathfrak X(v)}
 =\det(I-K_v+zK_v).
 }
 \tag{4.2}
\]

By Theorem 2.1 of the preceding note,

\[
 \boxed{
 TQF(v)\text{ for one }v>0
 \iff \mathrm{RH}.
 }
 \tag{4.3}
\]

Under RH, `K_v` has eigenvalues

\[
 \frac{v}{v+\gamma^2+1/4}
\]

with zero multiplicities.  The point of `TQF(v)` is to construct the operator
without using those zeros.

## 5. Why direct integration of the fiber operators is not enough

A convex mixture of determinants is not generally the determinant of the
convexly averaged operator.  Nor does the direct integral solve the problem:
for a decomposable operator,

\[
 \det\left(\int^\oplus
  (I-K_{v,\tau}+zK_{v,\tau})d\nu_v(\tau)
 \right)
\]

is governed by an exponential integral of logarithmic determinants, not by
the arithmetic mixture (4.1).

Thus the latent theta selector is load-bearing.  It must be removed through a
genuine source coupling, exterior-power identity or conservative dilation.
Simply writing every fiber as a determinant does not prove RH.

This is the Fock-space version of the positive-sum firewall in PR #784:
`PF_infinity` and quasi-free determinantal laws are not closed under arbitrary
positive mixtures.

## 6. Exterior-power form of the gate

For a positive trace-class contraction `K`,

\[
 \det(I-K+zK)
 =\sum_{n\ge0}z^n
 \operatorname{Tr}\left[
  \bigwedge^nK\,igwedge(I-K)
 \right],
\]

or, in the more convenient variable `y=z-1`,

\[
 \det(I+yK)
 =\sum_{n\ge0}y^n\operatorname{Tr}(\bigwedge^nK).
 \tag{6.1}
\]

The theta mixture gives explicit positive averages of the fiber exterior
traces.  `TQF(v)` asks for one operator whose entire exterior-power character
matches those averages simultaneously.

This is the precise point where the Segre/Koszul work from PRs #769 and #781
can re-enter Architecture E.  The syzygy machinery already organizes
alternating exterior characters; the missing extra datum is a positive
Hilbert-space realization that removes the latent selector without replacing
an arithmetic average by an Euler-characteristic cancellation.

## 7. Modified-Bessel spectral structure

The coefficient kernel of one theta fiber is

\[
 \boxed{
 [v^n]\cosh\left(\tau\sqrt{v+\frac14}\right)
 =\frac{\sqrt\pi}{2n!}
  \tau^{n+1/2}I_{n-1/2}(\tau/2).
 }
 \tag{7.1}
\]

A recent theorem of D. S. P. Salazar,
*Strict Total Positivity from Spectral Darboux and Toeplitz Smoothing
Mechanisms*, arXiv:2607.02778, proves that

\[
 (x,s)\longmapsto I_s(x),
 \qquad x>0,\ s\ge0,
\]

is strictly totally positive of infinite order.

This does **not** by itself prove that the mixed xi coefficient sequence is
`PF_infinity`: the factors `tau^n/n!`, the forced-one extension and the common
latent integration must all be retained.  It does, however, expose a serious
new route.

### Spectral-Darboux composition gate

Prove that the specific theta projection

\[
 c_n
 =\int_0^\infty
 e^{\tau/2}\psi(e^{2\tau})
 \frac{\sqrt\pi}{2(n-1)!}
 \tau^{n-1/2}I_{n-3/2}(\tau/2)d\tau,
 \qquad n\ge1,
 \tag{7.2}
\]

together with `c_0=1/2`, preserves the one-sided Toeplitz total positivity of
all orders.

A valid proof must use a composition or planar-network theorem that sees the
common `tau` selector.  It may not invoke closure of `PF_infinity` under
positive sums, which is false.

The Darboux theorem is relevant because it supplies positive Wronskians for
the spectral family before mixing.  The research task is to propagate that
strict spectral order through the exact theta weight and the Toeplitz shift
geometry.

## 8. A conservative-colligation interpretation

Equation (4.1) can also be viewed as a visible channel of a larger positive
source space carrying:

- the vacuum atom `N=0`;
- the latent scale `tau`;
- the half-integer Fock modes;
- the forced occupation;
- all Bernoulli occupations.

A conservative source map that compresses this space to one quasi-free output
without losing the exterior character would prove `TQF(v)`.  This is a more
concrete version of the canonical-system or colligation target:

\[
 \text{theta source}
 \longrightarrow
 \text{positive Fock dilation}
 \longrightarrow
 \text{one trace-class contraction}
 \longrightarrow
 \mathrm{RH}.
\]

The non-isometric compression firewall remains in force.  The output metric
must be inherited from the source, not chosen after observing the desired
zeros.

## 9. Immediate theorem-sized targets

The strongest next targets are, in order:

1. **finite exterior closure:** construct `K_v^(N)` matching all coefficients
   through degree `N`, with a source-uniform trace-norm bound;
2. **projective consistency:** prove the `K_v^(N)` can be chosen as compatible
   compressions of one positive contraction;
3. **Darboux composition:** prove Toeplitz positivity of the mixed coefficient
   sequence using the strict total positivity of the Bessel spectral kernel;
4. **latent-selector dilation:** realize the arithmetic mixture as one
   conservative quasi-free transfer rather than an average of transfers.

Any complete version closes the all-order E–Widder inequality.  A finite
version yields reviewable higher-order positivity without reverting to an
unstructured derivative scan.

## 10. Review checklist

Independent review should check:

1. the `t=e^(2 tau)` normalization in (1.1);
2. the half-integer zero set in (1.2);
3. convergence and normalization of the product (1.3);
4. the Bernoulli probabilities in (2.1);
5. the forced factor `z` in (2.3);
6. the vacuum mass and continuous mass in (3.2);
7. the one-scale determinant converse;
8. the direct-integral firewall;
9. the Bessel coefficient normalization in (7.1);
10. the distinction between imported Bessel total positivity and the open
    theta-composition theorem.

Finite Bernoulli-string algebra is included in
[`verify_order_product_and_reciprocal.py`](verify_order_product_and_reciprocal.py).
