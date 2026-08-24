# L-106073 — The scale-matched character family closes the HBC residual in logarithmic `L2`

Claim ID: `L-106073`  
Programme aliases: `LFAM1.HBC_L2_CLOSURE`, `STRESS.CROP_COMPOSITION`, `LFAM2.BLOCK_FAMILY_ASSEMBLY`  
Status: **PROVED COMPOSITION FROM BLOCK OCCUPANCY TO THE NATIVE RESIDUAL**  
Created: 2026-08-25  
Updated: 2026-08-25  
Depends on: `L-106001`, `L-106004`, `L-106060`, `L-106070--L-106072`; parent `L-102883`, `L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let \(R_{\rm HBC}(X)\) be the complete carrier-recombined, owner-excluded,
horizon-safe balanced distinct-product residual of parent `L-102888`.  The
Type-I row is already power-small and the smooth-boundary row is absent.

## 1. Principal recovery on each exact source piece

Use the disjoint block-colour partition of `L-106070`:

\[
R_{\rm HBC}(X)
=
\sum_{\mathcal B,A}R_{\mathcal B,A}(X).
\tag{L-106073.1}
\]

For the colour-safe prime \(\ell=\ell(B,A)\), every physical index in the
piece is coprime to \(\ell\).  Hence the character-twisted finite fields

\[
R_{\mathcal B,A;\chi}(X)
=
\sum_N r_{\mathcal B,A}(N;X)\chi(N)v_N
\]

satisfy

\[
R_{\mathcal B,A;\chi_0}(X)
=R_{\mathcal B,A}(X).
\tag{L-106073.2}
\]

Therefore the positive complete family norm contains the native piece.  On a
dyadic horizon \(I_X=[X,2X]\), put

\[
\mathfrak M_{\mathcal B,A}(I_X)
=
\int_{I_X}
\sum_{\chi\ ({\rm mod}\ \ell)}
\|R_{\mathcal B,A;\chi}(t)\|^2
\frac{dt}{t}.
\tag{L-106073.3}
\]

Then

\[
\boxed{
\int_{I_X}\|R_{\mathcal B,A}(t)\|^2\frac{dt}{t}
\le
\mathfrak M_{\mathcal B,A}(I_X).
}
\tag{L-106073.4}
\]

This is literal principal-character inclusion, not an amplifier lower bound.
No ramified completion is invoked after residual selection; unramifiedness was
proved coefficientwise before (L-106073.4).

## 2. Exact CROP adapter on the coloured block

Complete character orthogonality expands (L-106073.3) into physical pairs

\[
P c^2\equiv Qd^2\pmod\ell.
\]

The source-owned expansion has exactly:

```text
equal physical products;
nonsquare owner ratios, which vanish;
the plus collision line for each square owner ratio;
the minus collision line for each square owner ratio.
```

The equal-product energy is \(X^{o(1)}\) by parent `L-102883`.  The four
marked-\(67\) sectors obey the same partition with the finite ratio
\(67^{f-e}QP^{-1}\).

For every surviving line, insert the two same-occurrence nonzero phases of
`L-106060`.  With the direct-sum source index \(\mathfrak a\) fixed before
physical observation, that theorem gives

\[
\boxed{
\|S_{\mathfrak a}(t)\|^2
\le
(\ell-1)D_{\mathfrak a}(t)
<
\ell D_{\mathfrak a}(t).
}
\tag{L-106073.5}
\]

No one-phase estimate or phase-cardinality Cauchy is used.  All inherited
external owner phases and internal discrepancy phases commute with the
character and two-phase transforms.

The exact implication proved in `T-106060.2--T-106060.4`, now applied to this
single unramified block-colour family with its frozen modulus, is

\[
\boxed{
\mathfrak M_{\mathcal B,A}(I_X)
\ll
X^{o(1)}
+
X^{o(1)}
\int_{I_X}
\sum_{\mathfrak a\subset(\mathcal B,A)}
\ell D_{\mathfrak a}(t)
\frac{dt}{t}.
}
\tag{L-106073.6}
\]

This is the conclusion-facing normalization for which `CROP106060` was
defined; it is not a new pointwise inequality for individual signed Gram
entries.

By `L-106072.6`, the integral in (L-106073.6) is \(X^{o(1)}\).  Combining
(L-106073.4) and (L-106073.6) gives

\[
\boxed{
\int_{I_X}\|R_{\mathcal B,A}(t)\|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{L-106073.7}
\]

## 3. Recombination of all blocks

The number of block-colour pieces is \(X^{o(1)}\).  Cauchy in the finite
linear partition gives pointwise

\[
\|R_{\rm HBC}(t)\|^2
\le
X^{o(1)}
\sum_{\mathcal B,A}
\|R_{\mathcal B,A}(t)\|^2.
\]

Integrating and using (L-106073.7) proves

\[
\boxed{
\int_X^{2X}|R_{\rm HBC}(t)|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{L-106073.8}
\]

All-chaos carrier cancellation is retained inside each summand before this
Cauchy step.  Equal-core, one-sided and two-sided discrepancy packets have not
been assigned separate negative parts.

## 4. Negative mass

For the scalar fixed observation, logarithmic Cauchy--Schwarz gives

\[
\int_X^{2X}(R_{\rm HBC}(t))_-
\frac{dt}{t}
\le
(\log2)^{1/2}
\left(
\int_X^{2X}|R_{\rm HBC}(t)|^2\frac{dt}{t}
\right)^{1/2}.
\]

Using (L-106073.8) and summing the \(O(\log Y)\) dyadic horizons proves

\[
\boxed{
\int_2^Y(R_{\rm HBC}(t))_-
\frac{dt}{t}
=Y^{o(1)}.
}
\tag{L-106073.9}
\]

Thus

\[
\boxed{\mathrm{HBCQDSP}_{102888}}
\]

is proved by the scale-matched family construction, subject to the exact CROP
adapter already claimed in `T-106060`.

## Exact boundary

```text
linear block/colour source partition          PROVED EXACT
principal recovery on every coloured block    PROVED EXACT
character collision classification            INHERITED PROVED EXACT
equal products                                INHERITED PROVED SUBPOWER
two-phase line contraction                     INHERITED PROVED SHARP
weighted root occupancy                        PROVED SUBPOWER
CROP-to-family adapter                         INHERITED FROM T-106060
native HBC logarithmic L2                      PROVED SUBPOWER
HBCQDSP102888 negative mass                    PROVED SUBPOWER
```

The further detector-to-RH composition uses only the already-published parent
implication and is recorded separately in `T-106070` so that reviewers can
audit this new arithmetic closure independently from the older Mellin
consumer.