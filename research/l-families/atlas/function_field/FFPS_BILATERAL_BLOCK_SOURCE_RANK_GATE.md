# The bilateral FFPS source has quotient rank two, but no improving two-block partition

Status: **exact correction and source-arity/leverage gate; no
varying-conductor estimate, RH, or GRH claim**

Exact replay:
[`ffps_bilateral_block_source_rank_gate.py`](ffps_bilateral_block_source_rank_gate.py).

## 0. Outcome and correction

The current bilateral FFPS fibre does contain the full Fourier spectrum of
the quotient

\[
 K=C_2^2.
\]

Its two physical square-phase coordinates are

\[
 X=Pc^2\pmod\rho,
 \qquad
 Y=Qd^2\pmod\ell.
\]

After quartic orientation, write their binary characters as
`epsilon_X,epsilon_Y`.  The four quotient characters are exactly

\[
 1,\qquad \epsilon_X,\qquad\epsilon_Y,
 \qquad\epsilon_X\epsilon_Y.
\tag{0.1}
\]

They are respectively the principal--principal, nonprincipal--principal,
principal--nonprincipal, and double-nonprincipal channels of the frozen
tensor Gauss family (up to the order in which the `ell` and `rho` factors are
written).  The two mixed channels are **retained**, not removed by the clean
source or Wick ledger.

An earlier version of this packet incorrectly called the mixed characters
"single-sided/root channels" and deleted them.  That conflated the harmless
choice of a square root of a character with the principal/nonprincipal
channel split.  Frozen `L-106120.8`, `T-106121` Section 1,
`L-106131.13`, and `T-106140.6` explicitly retain both mixed channels.

Thus there is no Fourier-rank obstruction to the complete rank-two
off-coset kernel on the live bilateral fibre.  The actual obstruction is a
leverage/partition theorem:

* two disjoint nonempty blocks on the two local phase factors must be the
  singleton blocks `{ell}` and `{rho}`;
* an eligible singleton at `p=1 mod 4` has leverage

  \[
  L_{\{p\}}={4(p-1)\over3p+1}\ge1;
  \tag{0.2}
  \]

* because `ell!=rho`, the two-singleton product is in fact strictly greater
  than one (its smallest eligible value is `6/5` at `(5,13)`).

So the current fibre supports either one strictly improving two-factor
checkerboard block, or a native rank-two quotient with no contraction.  It
does **not** support two disjoint strictly improving binary blocks.

The four-coordinate lower bound survives with its proper scope:

\[
 \boxed{
 \text{two disjoint strictly improving blocks in this binary Gram}
 \Longrightarrow \text{at least four local physical phase coordinates}.}
\tag{0.3}
\]

## 1. Exact frozen source ledger

The correction uses PR #751 at
`98af0db6ec7f77d6333a77a3dac53c4698852f43`:

| claim | frozen blob | load-bearing statement |
|---|---|---|
| `L-106120` | `a8d829dc10611adb7bfb4853902bdff0ab02a065` | equation (8) splits the complete tensor family into PP, P--NP, NP--P, NP--NP |
| `T-106121` | `9111983ae4bf199a8315310a9ce090561430c33b` | Section 1 retains both one-collision mixed channels |
| `L-106131` | `37722c3f36ec7d1681f34d4329a3795e5028f7ae` | equation (13) gives all four Wick-centered tensor summands |
| `T-106140` | `d5be8e376c88b63de0be19e0d9e8791624e99ae2` | equation (6) globally recombines both mixed and the double-NP channels |

The physical coordinate and orientation are imported from
`FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md` and
`FFPS_CHECKERBOARD_SOURCE_BRIDGE.md`.  The latter identifies
`epsilon_X epsilon_Y` with the double-NP checkerboard, but nowhere says that
the two mixed members have left the complete tensor source.

The exceptional-source ledger removes literal atoms, equal physical
products, quadratic-root pieces, shared incidence, owner/core overlaps, and
geometrically constant constituents at their declared scopes.  None of
those operations is deletion of the mixed Fourier summands in (0.1).

## 2. The native rank-two kernel

On `K=C_2^2`, Fourier orthogonality gives

\[
 k_{\rm full}(x,y)
 =1-{1\over3}\sum_{\chi\ne1}\chi(x)\chi(y)
 =\begin{cases}
 0,&x=y,\\
 4/3,&x\ne y.
 \end{cases}
\tag{2.1}
\]

All three nonprincipal characters in (0.1) occur in the frozen source, so
(2.1) is algebraically available.  It is atom-free and distinguishes all
four quotient cosets.

For comparison, retaining only the double-NP product mode would give

\[
 k_{\rm product}(x,y)
 =1-(\epsilon_X\epsilon_Y)(x)(\epsilon_X\epsilon_Y)(y),
\tag{2.2}
\]

which coarsens the quotient to two product-parity classes.  Formula (2.2) is
the existing one-block checkerboard.  It is a legitimate subfamily, but it
is **not** forced by the clean-source ledger.

## 3. The exact leverage obstruction

For a singleton binary block,

\[
 M={p-1\over2},\qquad Q={p+1\over2},\qquad P=p,
\]

and the block theorem gives (0.2), with

\[
 L_{\{p\}}-1={p-5\over3p+1}.
\tag{3.1}
\]

Quartic physical orientation requires `p=1 mod 4`, hence `p>=5`.
Therefore no singleton strictly contracts.  Since the two marked primes of
`L-106120` are distinct, the smallest eligible two-singleton partition is
`(5)|(13)` and has leverage

\[
 1\cdot{6\over5}={6\over5}>1.
\tag{3.2}
\]

By contrast, putting both factors in one checkerboard block gives the frozen
bilateral leverage

\[
 L_{\{\ell,\rho\}}
 ={4(\ell-1)(\rho-1)\over
   5\ell\rho+\ell+\rho+1}<1.
\tag{3.3}
\]

At `(5,13)` this is `24/43`.  The live source therefore presents an exact
choice:

\[
 \begin{array}{c|c|c}
 \text{partition}&\text{quotient rank}&\text{leverage}\\ \hline
 \{\ell,\rho\}&1&<1\\
 \{\ell\}\mid\{\rho\}&2&>1.
 \end{array}
\tag{3.4}
\]

Tensoring two already-squared one-block inequalities does not alter this
partition ledger or create a joint rank-two principal current.

## 4. Smallest viable native four-phase architecture

The most direct source candidate is a four-phase lift of `L-106120`.  On a
stratum where each reduced core supplies two distinct eligible internal
primes, mark

\[
 \ell_1,\ell_2\mid c,
 \qquad
 \rho_1,\rho_2\mid d,
\]

with every marked prime absent from the opposite physical product.  Retain
the four physical coordinates

\[
 X_j=Pc^2\pmod{\rho_j},
 \qquad
 Y_j=Qd^2\pmod{\ell_j},
 \qquad j=1,2,
\tag{4.1}
\]

before one common square.  The two block characters would be

\[
 B_j=\epsilon_{\rho_j}(X_j)\epsilon_{\ell_j}(Y_j),
 \qquad j=1,2.
\tag{4.2}

Then `B_1`, `B_2`, and `B_1B_2` all belong to the complete fourfold tensor
Gauss spectrum, and each block contains two factors, so strict local
contraction is algebraically possible.

This is a design specification, not yet a source theorem.  It still needs:

1. a coefficient-exact partition selecting the second distinct reduced-core
   primes and paying the strata with fewer eligible factors;
2. four same-occurrence nonzero Ramanujan phases, including all opposite-owner
   incidence exclusions;
3. owner-sector orientations and hard deletion before one common square;
4. a recomputed atomic/equal-product/shared-incidence ledger;
5. one signed varying-conductor estimate keeping all three selected modes
   together, followed by principal individualization.

This is the most viable native route because it extends the already exact
bilateral identity rather than tensoring two different conclusion targets.

## 5. Proof ledger

Proved exactly:

* the full native `C2^2` Fourier ledger and the correction of the prior
  rank-one claim;
* the complete and product-only kernels (2.1)--(2.2);
* the singleton formula and the noncontracting two-singleton partition;
* the strictly improving one-block formula (3.3);
* the four-coordinate lower bound (0.3) for two disjoint strictly improving
  binary blocks.

Not proved:

* construction of the four-phase lift in Section 4;
* that every conceivable rank-two mask needs four coordinates under a
  different local Gram or higher cyclic quotient;
* WCADD, WCKUM, CYSEL, principal individualization, RH, or GRH.

## 6. Bounded replay

Run:

```text
python -B research/l-families/atlas/function_field/ffps_bilateral_block_source_rank_gate.py --check
python -B -O research/l-families/atlas/function_field/ffps_bilateral_block_source_rank_gate.py --check
python -B -m unittest tests.test_ffps_bilateral_block_source_rank_gate
python -B -O -m unittest tests.test_ffps_bilateral_block_source_rank_gate
```

The replay evaluates one `4 x 4` quotient kernel and tiny rational prime
panels through `29`.  It enumerates no conductor, source family, curve, or
point.
