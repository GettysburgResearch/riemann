# The coset interferometer has a quadratic-weight barrier

Status: **exact finite-field countermodel and source firewall; not an FFPS
estimate and not an RH or GRH claim**

Exact replay:
[`ffps_coset_interferometer_weight_barrier.py`](ffps_coset_interferometer_weight_barrier.py).

## 0. Outcome

The block-coset interferometer deletes every same-coset pair, not merely the
literal diagonal.  That is valuable, but it does **not** by itself lower the
cohomological weight of the surviving correlation.

For every odd prime `p` and `r>=1`, take

\[
 \Omega=(\mathbf F_p^\times)^r,
 \qquad z_x=\psi(x_1+\cdots+x_r),
 \qquad
 \Phi(x)=(\kappa(x_1),\ldots,\kappa(x_r))\in C_2^r,
\tag{0.1}
\]

where `psi` is a nontrivial additive character and `kappa` the quadratic
character.  Put `h=2^r`.  The principal trace is tiny:

\[
 P=\sum_xz_x=(-1)^r,
 \qquad |P|^2=1.
\tag{0.2}
\]

For the quotient character indexed by `S subset {1,...,r}`, tensor
factorization and the quadratic Gauss identity give

\[
 |H_S|^2=p^{|S|}.
\tag{0.3}
\]

Consequently

\[
 \boxed{
 \sum_{S\ne\varnothing}|H_S|^2=(p+1)^r-1,
 \qquad
 \mathcal I
 =1-{(p+1)^r-1\over2^r-1}.}
\tag{0.4}
\]

The kernel of `I` is still exactly zero on all same-coset pairs.  Its literal
atomic diagonal is zero.  Nevertheless `|I|` is of order `p^r`: the full
quadratic scale of this `r`-dimensional model.

Thus the implication

\[
 \text{atom-free + every selected mode nonconstant}
 \quad\Longrightarrow\quad
 \text{square-root-sized interferometer}
\tag{0.5}
\]

is false.  Principal recovery uses the exact signed cancellation

\[
 \boxed{
 |P|^2=\mathcal I+{1\over2^r-1}
 \sum_{S\ne\varnothing}|H_S|^2.}
\tag{0.6}
\]

Bounding the two terms separately loses the entire mechanism.

## 1. Exact proof

For one coordinate,

\[
 \sum_{x\ne0}\psi(x)=-1,
 \qquad
 \left|\sum_{x\ne0}\kappa(x)\psi(x)\right|^2=p.
\tag{1.1}
\]

The replay certifies both identities without floating point.  For a weight
`w` on `F_p`, extended by `w(0)=0`, form

\[
 C(t)=\sum_xw(x+t)w(x).
\]

For `w=1_{F_p^times}`, one has `C(0)=p-1` and `C(t)=p-2` for `t!=0`.
For `w=kappa`, one has `C(0)=p-1` and `C(t)=-1` for `t!=0`.  Since
`sum_{t!=0}psi(t)=-1`, their Fourier powers are respectively `1` and `p`.

Now let `chi_S` multiply the quadratic coordinates in `S`.  Fubini gives

\[
 H_S
 =\prod_{i\in S}\sum_{x\ne0}\kappa(x)\psi(x)
  \prod_{i\notin S}\sum_{x\ne0}\psi(x),
\]

which proves (0.2)--(0.3).  Summing `p^|S|` over all nonempty `S` proves the
first identity in (0.4).  Substitution in the exact quotient-Fourier identity
from the block-coset packet proves the second.

The literal atomic mass before centering is `(p-1)^r`.  It cancels exactly
between the principal energy and selected average, as the general atomic
ledger predicts.  Formula (0.4) shows that off-diagonal coherence remains
after that cancellation.

## 2. The one-curve warning already occurs at `r=1`

No high-dimensional construction is needed to see the obstruction.  On
`G_m/F_p`,

\[
 P=-1,
 \qquad |H_\kappa|^2=p,
 \qquad \mathcal I=1-p.
\tag{2.1}
\]

The additive Artin--Schreier line and its quadratic Kummer twist are
geometrically nonconstant.  Their compactly supported trace sums have the
expected curve-scale sizes `1` and `sqrt(p)`.  Squaring the latter produces a
weight-two term of size `p`.  Removing the diagonal in a square does not turn
the resulting two-variable correlation back into a weight-one trace.

This is the precise reason that an invariant audit and a first-Betti bound
for each selected line are insufficient.  A successful application must
either:

1. keep (0.6) intact inside one trace/cohomology calculation;
2. find an additional correspondence forcing cancellation between its two
   terms; or
3. replace separate absolute bounds by a signed bilinear estimate adapted to
   the off-coset kernel.

## 3. Consequence for the block-checkerboard architecture

The preceding block packet proves three exact positive facts: multiplicative
hard leverage, literal atom removal, and an invariant-free path realization
of every selected quotient mode.  The present countermodel leaves all three
facts intact.  It closes only an invalid shortcut:

\[
 \text{modewise Deligne bounds}
 \not\Rightarrow
 \text{a saving for }\mathcal I
 \text{ after triangle inequality}.
\tag{3.1}
\]

In the path model, the selected average has only linear *average* Betti
complexity.  But its traces are squared before averaging, so their natural
scale is still quadratic.  The same normalization that makes the complexity
average affordable also makes exact cancellation with `I` load-bearing.

The smallest strengthened FFPS target is therefore a **joint signed
interferometer estimate**, not `h-1` independent selected-mode estimates:

\[
 \mathcal I+{1\over h-1}\sum_{\chi\ne1}|H_\chi|^2
 \quad\text{with the native principal source retained.}
\tag{3.2}
\]

Algebraically (3.2) is `|P|^2`; arithmetically the point is to realize the two
pieces before destructive absolute values and exploit source correlations.
This still does not individualize the zeta member, but it prevents the
block programme from spending its atom cancellation twice.

## 4. Proof ledger and scope

Proved exactly:

- the prime-field autocorrelation certificates in (1.1);
- all mode energies (0.3);
- the selected-energy and interferometer formulas (0.4);
- zero literal atomic diagonal, imported from and directly consistent with
  the quotient kernel;
- failure of the formal inference (0.5), already for one curve.

Not proved:

- that model (0.1) is the native FFPS source;
- any WCADD, WCKUM, CYSEL, or varying-conductor estimate;
- a joint signed estimate of type (3.2);
- principal-member individualization, RH, or GRH.

The `r`-fold tensor is a countermodel to an inference, not a model of the
one-dimensional FFPS family.  The `r=1` row is included to show that the
quadratic-weight obstruction itself is already one-dimensional.

## 5. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_coset_interferometer_weight_barrier.py --check
python -B -O research/l-families/atlas/function_field/ffps_coset_interferometer_weight_barrier.py --check
python -B -m unittest tests.test_ffps_coset_interferometer_weight_barrier
python -B -O -m unittest tests.test_ffps_coset_interferometer_weight_barrier
```

The largest exact autocorrelation panel has fewer than `30^2` cells; tensor
ranks stop at five.  There are no point counts and no floating-point
operations.

Primary background for the sheaf-language interpretation is Deligne's Weil
II theorem and Katz's treatment of Gauss/Kummer sheaves.  The finite
identities used in the proof are elementary and fully replayed here.  No
external novelty claim is made without a dedicated literature review.
