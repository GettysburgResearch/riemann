# Genuine Xi derivative proportion transfer through residue coherence

## Correction to the previous high-band claim

The earlier `L-104517` theorem is mathematically useful but was not a genuine
proportion transfer.  Its saddle argument independently proved `100%`
real-rootedness at both adjacent derivative levels in the high band.  The input
proportion therefore did no work.

`R-104513` now makes that scope correction binding.

## New exact theorem

At each simple real zero `c` of `Xi^(k)`, define

\[
\rho_{k,c}
={\Xi^{(k-1)}(c)\over\Xi^{(k+1)}(c)}.
\]

Negative residues are Rolle-generating extrema; positive residues are wrong
extrema.

For the real critical points in a regular interval put

\[
A_k=-\sum_c\rho_{k,c},
\qquad
B_k=\sum_c\rho_{k,c}^2,
\qquad
\mathfrak C_k={A_{k,+}^2\over R_kB_k}.
\]

Cauchy--Schwarz gives at least `R_k mathfrak C_k` good extrema.  The exact
factor-two reverse-Rolle identity then yields

\[
N_\mathbb R(\Xi^{(k-1)})
\ge
(2\mathfrak C_k-1)
N_\mathbb R(\Xi^{(k)})-1.
\]

Consequently, if the level-`k` line proportion is at least `p` and

\[
\mathfrak C_k\ge{1+c\over2}+o(1),
\]

then the level-`k-1` line proportion is at least `cp`.

This is the requested theorem shape.  The premise `p` is load bearing and is
not established elsewhere inside the proof.

## Mean/variance form

If the residue mean is `-mu<0` and its second moment is `nu`, then

\[
\mathfrak C={\mu^2\over\nu}.
\]

The threshold is

\[
2\mu^2>\nu.
\]

Equivalently, if the squared coefficient of variation around the negative
carrier is `v^2<1`, the transfer constant is

\[
\boxed{
c={1-v^2\over1+v^2}.}
\]

Examples:

```text
v^2 <= 1/3  -> c >= 1/2;
v^2 <= 1/9  -> c >= 4/5.
```

Thus a `99%` line proportion at one derivative would imply at least `49.5%` at
the preceding derivative under the first moment bound, or at least `79.2%`
under the second.

## Why the new input is independent

The two required moments are sampled only at the already-given real zeros of
`Xi^(k)`:

\[
\mathcal M_{1,k}
=-\sum {\Xi^{(k-1)}(c)\over\Xi^{(k+1)}(c)},
\]

\[
\mathcal M_{2,k}
=\sum \left|{\Xi^{(k-1)}(c)\over\Xi^{(k+1)}(c)}\right|^2.
\]

They neither count nor assume any real zero of the parent.  Local contour
formulas in `L-104523` make both moments source-visible.

## New arithmetic/analytic target

The exact remaining theorem is `RCMV104530`:

\[
\mathcal M_{1,k}(T)^2
>
\left({1\over2}+\delta\right)
R_k(T)\mathcal M_{2,k}(T)
\]

for some fixed derivative level `k` and some `delta>0`.

This is a signed inverse-curvature mean value at relative extrema.  It is a
natural target for:

1. mollified critical-point moment calculations;
2. the Conrey--Ghosh relative-extrema machinery;
3. Pick/Voorhoeve phase-velocity sampling;
4. contour formulas for adjacent derivative ratios.

Unlike the old cumulative charge, `RCMV104530` is not the desired parent zero
count in disguise.

## Status

```text
high-band count comparison as p-transfer   WITHDRAWN
residue-coherence transfer                 PROVED EXACT
p -> c p with load-bearing p               PROVED CONDITIONAL ON RCMV
RCMV104530                                  OPEN
PRES104518 / HARG104521                     OPEN
RH                                          UNPROVED
```
