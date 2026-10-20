# The unselected long-inverse bottleneck after the new cubic mean

20 October 2026. Status: source interface and necessary-strength
calculation. No new centered estimate is asserted.

The new completed cubic mean does not immediately improve the long
unselected inverse exponent. The obstruction can be located before
the selected-prime analysis, in the original inverse Poisson step.

## 1. The precise positive-child obstruction

Use the inverse and canonical normalizations of the pinned Ope26a
source, commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
The local source is `ope26a-pinned-source.tex`; relevant labels are
`inverse-initial-row`, `initial-poisson-prefactor`,
`initial-canonical-lengths`, `initial-positive-child`,
`initial-weighted-count`, and `inverse-initial-margins`.

First take the unselected, trivial-overlap sector. Let the inverse
column length be \(D\), and its original row length be \(H\).
The nonprincipal inverse Poisson transform has a canonical column of
length \(D\), a dual row of length

\[
                         K=D^2/H,                       \tag{C1}
\]

and the normalized root factor \(H/D\). Its main positive child is
therefore controlled by \((H/D)J(K,D)\), in addition to the original
diagonal of size \(H\).

The old canonical target is \(J(K,D)\ll D\), with its admissibility
margin \(D>K\). In the general source notation this is exactly
\(F-M-Q=m-r\) when the selected length and the other overlaps are
zero. The second canonical margin is \(3m-2r\).

The newer all-length unmarked theorem of
[rStation paper 5](https://rstation.ai/problems/riemann_hypothesis/papers/5)
gives \(J(K,D)\ll K\) for every \(D\). Substitution into (C1)
gives

\[
              (H/D)K=D.                               \tag{C2}
\]

Thus it yields \(H+D\), which is useful when \(D\le H\) but does
not extend the raw row-scale inverse mean into \(D>H\). The issue
is not failure to state the newer canonical theorem at every column
length: it is the size of its target bound.

For \(D>H\), one has \(K>D\). Its formal diagonal has size
\(K\) for a nonzero fixed annular profile. Thus an argument that
bounds that diagonal separately already loses the desired target
\(D\). This is not a lower bound for the prescribed squared norm:
off-diagonal terms may cancel its diagonal. A direct theorem
\(J(K,D)\ll D\) in a range \(D<K<D^2\), if established, would
itself contain additional cancellation absent from the supplied
\(J\ll K\) estimate.

## 2. The operation that would have to be retained

Before positive enlargement, the source opens two inverse columns as
\(c_i=Cz_i\), and later uses the full common-divisor projector
\(1_{(z_1,z_2)=1}=\sum_{s\mid z_1,z_2}\mu(s)\).
After writing \(z_i=s n_i\), this creates the canonical child.
On its formal diagonal \(n_1=n_2\), the signed sum in \(s\)
reconstructs \(\sum_{s\mid z}\mu(s)\); it vanishes unless
\(z=1\). The remaining principal contribution is the one already
handled separately in the source.

That cancellation is lost when the two-column expression is replaced
by the positive children in `initial-positive-child` and
`initial-weighted-count`. A possible improvement must therefore
preserve a centered two-profile canonical form, or otherwise exploit
the signed common-divisor sum before this Cauchy step.

This is more demanding than subtracting a scalar from a finished
large-sieve bound. The full common smooth kernel, finite ray phases,
row divisibility restrictions, punctures, and signed projector must
still agree. Even without selected prime slots, the gcd splits create
the auxiliary fourth-power label \(f=d's\) and fixed puncture
\(t=C/d'\). These labels and punctures must be retained in a full
centered theorem. A result only for the isolated \(f=t=1\) sector
would identify an encouraging special case, not complete the inverse
estimate.

The pure cubic Type-I mean in this packet is an upper bound for a
different positive average. It does not give this asymptotic or
centered sextic-row statement. Applying it after losing the signed
projector cannot restore the cancellation.

### Exact diagonal reconstruction, including masks

Here is the cancellation at the level of the actual source identity,
before any proposed analytic estimate. Freeze \(C,d',h',j\), the
earlier Fourier mode and the ray summand in
`initial-formal-component`. On a diagonal put
\(z_1=z_2=z\), where \(z\) is squarefree and
\((z,Cj)=1\). For every \(s\mid z\), put \(n=z/s\).
The source definitions are \(t=C/d'\), \(k=d'h'\),
\(f=d's\). The original and extracted zero extensions agree:

\[
 \begin{split}
 &1_{(s,Cj)=1}1_{(s,h')=1}\rho_{t,j}(n)
        |\chi_n(k)\chi_n(f)^4|^2\\
 &\hspace{20mm}=1_{(z,Cj)=1}1_{(z,h')=1}.             \tag{C2a}
 \end{split}
\]

Indeed \(d'\mid C\), \(s\mid z\), and \(z\) squarefree
give \((s,n)=1\); the factors from \(d',t,j,s\) restore
exactly the displayed coprimalities, and the two \(h'\) zeros
combine to \((z,h')=1\). The two extracted Gauss/character
scalars have absolute square \(1_{(s,h')=1}\), as in
`initial-common-extraction`. All remaining ray coefficients are
unchanged outer scalars.

Most importantly, the full root, old column windows, and kernel
recombine to expressions in \(z\), independent of its divisor \(s\):

\[
 \frac{H}{Dq_{d'}q_s q_n}=
 \frac{H}{Dq_{d'}q_z},\qquad
 \mathcal K_{\rm init}\!\left(
 \frac{Hq_{h'}}{q_{d'}q_s^2q_n^2}\right)=
 \mathcal K_{\rm init}\!\left(
 \frac{Hq_{h'}}{q_{d'}q_z^2}\right),\qquad
 W_0(q_Cq_s q_n/D)=W_0(q_Cq_z/D).                       \tag{C2b}
\]

Here \(D=Z^{D'}\), \(H=Z^m\); no approximate dyadic center
has replaced an actual norm. In the unselected case the marks are
one. In a marked identity, they must first be reassembled to the
original \(|\mathfrak d_0(Cz)|^2\), including every priority mask.
The individual \(s\)-dyad cutoffs sum to one. The full common
Fourier inversion restores (C2b), including both old windows;
neither individual separated Fourier factors nor a fixed
\(s\)-dyad need exhibit this cancellation.

Consequently the full reconstructed diagonal is its original
\(s\)-independent weight times

\[
                  \sum_{s\mid z}\mu(s)=1_{z=1}.        \tag{C2c}
\]

The \(z=1\) term is the restored principal pair
\(c_1=c_2=C\), whose restoration cost is already treated in the
source. The remaining outer \(\mu(d')\), row ball,
\(1_{(C,j)=1}\), and ray coefficient do not affect (C2c).
Thus the diagonal cancellation is exact; it is not an assumed
asymptotic for one isolated canonical squared norm.

The first irreversible step for this cancellation is the triangle
over the \(s\)-refinements followed by the weighted Cauchy step
on `initial-separated-identity`, leading to
`initial-positive-child` and `initial-weighted-count`.
A viable replacement would estimate the signed, fully reassembled
centered two-column form before those operations. A centered bound
for one arbitrary positive child is neither asserted nor implied
by (C2c).

## 3. The quantitative payoff of a genuine extension

Suppose a new argument proved the raw unselected inverse mean at row
scale whenever

\[
                        H\ge D^{1-\eta},\qquad \eta>0, \tag{C3}
\]

with the same punctures, full row support and smooth uniformity as
the existing amplification lemma. Sixth-power amplification would then
give, up to arbitrary small powers,

\[
 I(U,D)\ll U^{1/6}\max\{U,D^{1-\eta}\}^{5/6}.           \tag{C4}
\]

At \(D=U^r\) in the amplified branch this replaces
\(e(r)=1/6+5r/6\) by

\[
                   e_\eta(r)=1/6+5(1-\eta)r/6,         \tag{C5}
\]

a saving \(5\eta r/6\). This establishes why a small genuine
extension of the raw range could matter; it does not supply that
extension. At its boundary (C3), the dual row in (C1) is
\(K=D^{1+\eta}\), so the required centered control would remove
the diagonal-sized excess \(D^\eta\) while preserving the full
signed identities.

The numerical zero-free boundary remains unchanged by the present
positive means. The unselected centered problem is separate from,
and potentially smaller than, a complete marked mixed moment theorem.
