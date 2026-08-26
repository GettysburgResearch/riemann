# The current bilateral FFPS source has block rank one

Status: **exact source-arity/Fourier gate; no varying-conductor estimate, RH,
or GRH claim**

Exact replay:
[`ffps_bilateral_block_source_rank_gate.py`](ffps_bilateral_block_source_rank_gate.py).

## 0. Outcome

The new block-checkerboard interferometer cannot be inserted with rank two
into the currently frozen bilateral FFPS fibre.

This is not because its formal Gram theorem fails.  It is because the live
fibre has only two joint physical square-phase coordinates,

\[
 X=Pc^2\pmod\rho,
 \qquad
 Y=Qd^2\pmod\ell,
\]

and its clean Kummer channel requires both sides to be nonprincipal.  The
four Fourier characters of the apparent binary quotient are

\[
 1,\qquad \epsilon_X,\qquad\epsilon_Y,
 \qquad\epsilon_X\epsilon_Y.
\tag{0.1}
\]

The middle two are the single-sided/root channels removed by the frozen
source ledger.  The last is the existing double-nonprincipal checkerboard.
After the removal, the selected character span has dimension one, so the
four formal cosets coarsen to the two product-parity classes:

\[
 \boxed{
 C_2^2\longrightarrow C_2,
 \qquad(x,y)\longmapsto xy.}
\tag{0.2}
\]

There is a second obstruction.  A one-prime block at an eligible
`p=1 mod 4` prime has exact leverage

\[
 \boxed{L_{\{p\}}={4(p-1)\over3p+1}.}
\tag{0.3}
\]

It equals one at `p=5` and is greater than one for every larger eligible
prime.  Thus every strictly improving block needs at least two local phase
factors.  A genuinely improving rank-two block architecture therefore needs

\[
 \boxed{\text{at least four joint physical phase coordinates before squaring}.}
\tag{0.4}
\]

The live bilateral fibre has two.  Tensoring two already-squared fibre
inequalities does not supply the missing joint source.

## 1. Frozen source facts

The result uses the source contract already frozen in:

- `FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md`: the physical variables are
  `Pc^2,Qd^2`, and both phase sides must be retained before squaring;
- `FFPS_CHECKERBOARD_SOURCE_BRIDGE.md`: the one binary product parity is the
  live `(kappa_ell,kappa_rho)` double-nonprincipal member;
- `FFPS_CYCLIC_SOURCE_REALIZATION_GATE.md`: an exact-order-`k` product phase
  realizes a cyclic quotient whose nonconstant powers keep both sides
  nonprincipal;
- `FFPS_BLOCK_CHECKERBOARD_COSET_INTERFEROMETER.md`: `r` independent binary
  block parities require the full `2^r-1` nonprincipal quotient spectrum.

Nothing in this note changes those packets.  It composes them into the
smallest native-source test for the new block proposal.

## 2. Exact Fourier collapse on one bilateral fibre

Label the two local binary phases by points of `K=C_2^2`.  The complete
rank-two off-coset kernel is

\[
 k_{\rm full}(x,y)
 =1-{1\over3}\sum_{\chi\ne1}\chi(x)\chi(y)
 =\begin{cases}
 0,&x=y,\\
 4/3,&x\ne y.
 \end{cases}
\tag{2.1}
\]

It needs all three nonprincipal characters in (0.1).  If the two
single-sided channels are removed, only
`chi=epsilon_X epsilon_Y` remains.  The correctly normalized atom-free
kernel is then

\[
 k_{\rm clean}(x,y)
 =1-(\epsilon_X\epsilon_Y)(x)
       (\epsilon_X\epsilon_Y)(y)
 =\begin{cases}
 0,&xy=x'y',\\
 2,&xy\ne x'y'.
 \end{cases}
\tag{2.2}
\]

This is exactly the ordinary two-coset checkerboard kernel.  It deletes all
pairs sharing product parity, not merely literal atoms, but it has only one
selected mode.  Calling (2.2) a rank-two block interferometer would count two
forbidden Fourier channels that are no longer present.

Equivalently, using the rank-two denominator `1/3` with only the product mode
would fail even the atom ledger: it would cancel only one third of the
principal diagonal.  Renormalizing it to cancel atoms produces (2.2), hence
the rank-one collapse.

## 3. Exact leverage arity

For a singleton block, the block theorem has

\[
 M={p-1\over2},\qquad Q={p+1\over2},\qquad P=p.
\]

Substitution gives (0.3), and

\[
 L_{\{p\}}-1={p-5\over3p+1}.
\tag{3.1}
\]

The quartic physical orientation requires `p=1 mod 4`, so `p>=5`.
Consequently no eligible singleton is a strict contraction.  Two singleton
blocks have product leverage at least one.

This does not say that every block must always contain two primes in a future
source.  A different local Gram or a higher cyclic quotient could change the
formula.  It says exactly that the current binary square-phase Gram cannot
realize the strict rank-two panel inside one bilateral fibre.

## 4. Smallest constructive next source

The minimal candidate is a source atom carrying four physical coordinates

\[
 (X_1,Y_1,X_2,Y_2)
\]

jointly before amplification and squaring, with two disjoint
double-nonprincipal block characters

\[
 \epsilon_{X_1}\epsilon_{Y_1},
 \qquad
 \epsilon_{X_2}\epsilon_{Y_2}.
\]

All three selected modes—including their product—would then remain
double-nonprincipal.  Algebraically this is exactly what the block packet
needs.  Arithmetically four checks remain:

1. the four coordinates must belong to one native principal current rather
   than a tensor product of two different targets;
2. hard deletion must occur before the one common square;
3. root, shared-incidence, owner/core, and equal-product exclusions must be
   recomputed on the joint source;
4. the varying-conductor signed estimate must keep the three modes together.

This is a concrete source-design specification.  The present repository does
not yet contain such a four-phase FFPS identity.

## 5. Proof ledger

Proved exactly:

- the bilateral Fourier ledger (0.1)--(0.2);
- the complete and clean kernels (2.1)--(2.2);
- the singleton formula and no-contraction result (0.3), (3.1);
- the four-coordinate lower bound (0.4) for two strictly improving binary
  blocks in the current Gram.

Not proved:

- impossibility of every conceivable multi-place FFPS source;
- that single-sided/root channels can never be controlled by some future
  renormalized source;
- construction of the four-coordinate candidate;
- WCADD, WCKUM, CYSEL, principal individualization, RH, or GRH.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_bilateral_block_source_rank_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_bilateral_block_source_rank_gate.py --check
python -B -m unittest tests.test_ffps_bilateral_block_source_rank_gate
python -B -O -m unittest tests.test_ffps_bilateral_block_source_rank_gate
```

The replay evaluates one `4 x 4` quotient kernel and four rational prime
rows through `29`.  It enumerates no conductor, source family, curve, or
point.
