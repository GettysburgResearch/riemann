# FFPS conditioning by masking cannot improve principal leverage

**Status:** exact local operator theorem. This closes one proposed amplifier
shortcut; it does not estimate the open varying-conductor FFPS moments.

**Frozen source:** corrected PR #751 frontier `T-106121 / FFPS106121` at
`37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2`, through the exact phase Gram
packet `ffps_principal_leverage.json`. The dependency hash is locked in the
fixture.

**Computation:** 17 exact rational control rows for (p=3,5,7,11,13). The
theorem itself is a closed matrix calculation for every odd residue-field
cardinality with the same complete square-phase Gram. No L-function family,
conductor interval, or zero set is enumerated.

## 1. The question

The corrected local FFPS phase frame has

\[
 G_p=pI-J,\qquad m={p-1\over2},
\]

on its (m) sign-pair coordinates. Its principal observation is the sum of all
coordinates, with sharp squared leverage

\[
 L_{\rm full}={m\over p-m}={p-1\over p+1}.
\]

A tempting amplifier move is to condition on a smaller panel--for example a
root-number, owner, or core subfamily--and hope the smaller raw phase norm
isolates the principal member more efficiently. This packet settles the model
in which that condition only masks and reweights the existing coordinates.

Retain a support (A) of size (a), and write

\[
 O_\alpha(w)=\sum_{j\in A}\alpha_jw_j.
\]

On a constant packet the original observation has amplitude (m). Preserving
the native principal member therefore requires

\[
 \sum_{j\in A}\alpha_j=m.
\tag{1}
\]

Without (1), a smaller operator norm may simply mean that the desired signal
was attenuated.

## 2. Exact optimization theorem

The restricted Gram and its inverse are

\[
 G_{p,A}=pI_a-J_a,
 \qquad
 G_{p,A}^{-1}={1\over p}I_a+{1\over p(p-a)}J_a.
\]

Consequently

\[
 \|O_\alpha\|^2
 ={1\over p}\sum_j\alpha_j^2
 +{1\over p(p-a)}\left(\sum_j\alpha_j\right)^2.
\tag{2}
\]

Under (1), Cauchy--Schwarz gives the sharp identity

\[
 \boxed{
 \min_{\sum\alpha_j=m}\|O_\alpha\|^2
 ={m^2\over a(p-a)}.}
\tag{3}
\]

The unique real extremizer is uniform, (\alpha_j=m/a), and more precisely

\[
 \|O_\alpha\|^2-{m^2\over a(p-a)}
 ={1\over p}\sum_j\left(\alpha_j-{m\over a}\right)^2.
\tag{4}
\]

Thus negative or nonuniform real weights do not rescue the mask.

Since

\[
 a(p-a)
\]

is strictly increasing for (1\leq a\leq m), equation (3) is strictly larger
than the full-panel leverage whenever (a<m). The full unconditioned panel is
the unique optimum among all pure support restrictions and reweightings.

## 3. The false raw gain

An unweighted mask has raw leverage

\[
 L_{\rm raw}(a)={a\over p-a},
\]

which can look better than (L_{\rm full}). But its constant/principal signal
is only the fraction (a/m) of the native signal. Dividing by that squared
loss gives exactly

\[
 {L_{\rm raw}(a)\over(a/m)^2}
 ={m^2\over a(p-a)}.
\]

The apparent gain is therefore signal deletion, not amplification.

Writing (a=m-k), the normalized mask is contractive precisely when

\[
 k(k+1)<m;
\]

it is critical or expansive when the inequality becomes equality or reverses.
In particular, discarding a fixed positive fraction is fatal asymptotically:
if (a/m\to\theta\in(0,1)), then

\[
 {m^2\over a(p-a)}\longrightarrow {1\over\theta(2-\theta)}>1.
\]

Only (O(\sqrt m)) dropped coordinates can retain even a subunit local norm,
and every nonempty deletion still worsens the original contraction.

## 4. What this rules out--and what it does not

This is an exact no-go theorem for any local condition whose sole operator
effect is:

1. delete some existing sign-pair coordinates;
2. reweight the survivors by real scalars; and
3. renormalize the principal member to its native amplitude.

It therefore blocks a broad class of naive owner/core/root-number subsampling
arguments. It does **not** say that every arithmetically conditioned family is
useless. A genuine condition may change the Gram matrix, add signed or
phase-coherent cross terms before squaring, expose cross-prime Fourier
structure, or supply new arithmetic information. Those mechanisms lie
outside the mask model and remain live.

The tensor corollary is immediate: because every local normalized factor is
worsened, pure masks cannot improve either the coherent tensor contraction or
a positive direct-sum leverage bound. Any useful conditioned amplifier must
change the operator, not merely shrink its panel.

## 5. Replay and limits

```text
python -B research/l-families/atlas/function_field/ffps_conditioned_mask_no_go.py --check
python -B -O research/l-families/atlas/function_field/ffps_conditioned_mask_no_go.py --check
python -B -m unittest tests.test_ffps_conditioned_mask_no_go
python -B -O -m unittest tests.test_ffps_conditioned_mask_no_go
```

This packet proves only the local matrix theorem. It does not prove
`BTPS106121`, `BTMS106121`, `BTDS106121`, a varying-conductor large sieve,
RH, or GRH.
