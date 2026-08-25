# Corrected FFPS physical-squareclass adapter and principal leverage

**Status:** exact local operator theorem, exact source contract, and tiny
prime-field collision controls.  The global FFPS moments remain open.

**Frozen source:** PR #751 at
`37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2`, specifically corrected frontier
`T-106121 / FFPS106121` together with `L-106024`, `R-106122`, `R-106123`, and
`L-106126`.  Their git blob identities are recorded in the JSON fixture.

**What was actually run:** exact rational matrix formulas and at most 408
prime-field collision atoms across (p=3,5,7,11).  No polynomial family,
zero set, conductor range, or global moment is enumerated.

**Smallest remaining gap:** prove cancellation in one incomplete varying-core
Kummer line family after removing the complete exceptional ledger.  A fixed
core or complete owner shell does not pay the global conductor family.

## 1. Source-faithful adapter contract

The corrected source coordinates are

\[
 X=Pc^2,\qquad Y=Qd^2,
\]

not (P,Q) alone.  A function-field adapter must preserve the following
order of operations.

1. Mark irreducible divisors (ell,rho) and partition roughness/tie strata
   exactly.  A degree-plus-lexicographic selector is combinatorial; it must
   not be advertised as an algebraic “least-prime map.”
2. Retain both complete Boolean source sums.
3. Insert the source-selected Artin--Schreier phases at (ell,rho).
4. Apply the Kummer variables (Pc^2) modulo (rho) and (Qd^2) modulo
   (ell).
5. Amplify both sides before squaring.
6. Keep the principal--principal member equal to the native untwisted
   incidence current.
7. Remove, with separate bookkeeping, the atomic diagonal, equal physical
   products, quadratic-root pieces, shared owner/incidence pieces,
   owner/core overlaps, and geometrically constant constituents.

The remaining gates are exactly `BTPS106121`, `BTMS106121`, and
`BTDS106121`.  None is proved here.

## 2. The exact local leverage spectrum

For an odd residue-field prime (p), aggregate a Hilbert-valued packet in
sign pairs and write

\[
 w=(w_1,\ldots,w_m),\qquad m={p-1\over2}.
\]

The complete nonzero square-phase energy is

\[
 \|w\|_{\rm ph}^2
 =p\sum_j\|w_j\|^2-\left\|\sum_jw_j\right\|^2,
\]

so its Gram matrix is

\[
 G_p=pI-J.
\]

The constant mode has eigenvalue ((p+1)/2); the (m-1) sum-zero modes
have eigenvalue (p).  The principal observation is

\[
 O_p(w)=\sum_jw_j.
\]

It vanishes on every sum-zero mode.  On the constant mode its sole nonzero
squared singular value is

\[
\boxed{\|O_p\|^2={p-1\over p+1}.}
\tag{1}
\]

Equality holds exactly for constant sign-pair packets.  Thus (1) is sharp,
not merely a convenient upper bound.  It tends to one and therefore supplies
no conductor-saving contraction by itself.

For independent tensor phases at (p_1,\ldots,p_k), squared leverage
multiplies:

\[
 \left\|\bigotimes_iO_{p_i}\right\|^2
 =\prod_i{p_i-1\over p_i+1}.
\tag{2}
\]

This tensor statement must not be confused with a positive sum over varying
conductor fibres.

## 3. Positive fibre assembly is an exact no-go model

Put the local phase spaces in an orthogonal direct sum and observe

\[
 O(w_1,\ldots,w_k)=\sum_i\alpha_iO_{p_i}(w_i).
\]

Duality on a block-diagonal Gram gives the exact identity

\[
\boxed{
 \|O\|^2=\sum_i|\alpha_i|^2{p_i-1\over p_i+1}.
}
\tag{3}
\]

Every local constant packet simultaneously attains equality after aligning
the output directions.  Hence positive block assembly has no hidden saving.
For the two unit-weight fibres (p=3,5), equation (3) already gives

\[
 {2\over4}+{4\over6}={7\over6}>1.
\]

This is a finite operator theorem, not the global arithmetic moment.  Its
consequence is methodological but binding: any conductor-saving amplifier
must use coherent cross-fibre structure before the fibres are positively
squared.  Summing local large-sieve constants cannot provide it.

## 4. Physical-squareclass collision lines

For units modulo an odd marked prime,

\[
 Pc^2\equiv\varepsilon P'c'^2\pmod p,
 \qquad\varepsilon\in\{+1,-1\},
\]

is equivalent to

\[
 c=\omega c',\qquad
 \omega^2=\varepsilon P'P^{-1}.
\]

Thus each sign contributes either zero or two exact lines.  Within one owner
quadratic class, the positive component always has two lines.  The negative
component has two additional lines precisely when (-1) is a square.  The
combined even-character collision therefore has two lines for
(p\equiv3\pmod4) and four for (p\equiv1\pmod4).

Two tiny controls show why the full coordinate is indispensable.

- Modulo (7), equal owners (P=P'=1) with cores (c=1,c'=2) have
  different physical values (1,4), not equal even up to sign.  Owner-only
  equality is a false positive.
- Modulo (7), ((P,c)=(1,2)) and ((P',c')=(2,3)) have different owners
  but the same physical value (4).  Owner-only separation is a false
  negative.

These are regression witnesses for the corrected coordinate, not evidence
for a global moment bound.

## 5. Normalization firewall

The canonical XD kernel uses the literal dyadic operator

\[
 K_1=(I-\sqrt2S_2)(I-S_2)^2.
\]

Polynomial norms occupy (q^{\mathbf Z}).  Replacing (2) by (q) would
create a new degree-wavelet analogue; retaining (X\mapsto X/2) does not
align with degree shells.  Neither choice is a literal source-faithful XD
port without a separate normalization theorem.

This packet therefore stays with the Boolean/Kummer source already native to
`T-106121`.  It does not rename a (q)-adic wavelet as XD.

## 6. Replay and limits

Run

```text
python -B research/l-families/atlas/function_field/ffps_principal_leverage.py --check
python -B -O research/l-families/atlas/function_field/ffps_principal_leverage.py --check
python -B -m unittest tests.test_ffps_principal_leverage
python -B -O -m unittest tests.test_ffps_principal_leverage
```

The packet proves (1)--(3), the finite collision-line identities, and the
adapter contract.  It does not prove a mixed/double FFPS trace moment, a
number-field large sieve, `BCI102990`, RH, or GRH.
