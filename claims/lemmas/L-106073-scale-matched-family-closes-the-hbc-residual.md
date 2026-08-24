# L-106073 — The scale-matched character family closes the HBC residual in logarithmic `L2`

Claim ID: `L-106073`  
Programme aliases: `LFAM1.HBC_L2_CLOSURE`, `STRESS.CROP_COMPOSITION`, `LFAM2.BLOCK_FAMILY_ASSEMBLY`  
Status: **PROVED COMPOSITION FROM BLOCK OCCUPANCY TO THE NATIVE RESIDUAL**  
Created: 2026-08-25  
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

Therefore the positive complete family norm contains the native piece:

\[
\boxed{
\|R_{\mathcal B,A}(X)\|^2
\le
\sum_{\chi\ ({\rm mod}\ \ell)}
\|R_{\mathcal B,A;\chi}(X)\|^2.
}
\tag{L-106073.3}
\]

This is a literal principal-character inclusion, not an amplifier lower bound.
No ramified completion is invoked after residual selection; unramifiedness was
proved coefficientwise before (L-106073.3).

## 2. Exact character expansion

Complete character orthogonality expands the right side of (L-106073.3) into
physical pairs

\[
P c^2\equiv Qd^2\pmod\ell.
\]

The expansion has exactly the following source-owned parts:

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
\|S_{\mathfrak a}(X)\|^2
\le
(\ell-1)D_{\mathfrak a}(X)
<
\ell D_{\mathfrak a}(X).
}
\tag{L-106073.4}
\]

No one-phase estimate or phase-cardinality Cauchy is used.  All inherited
external owner phases and internal discrepancy phases commute with the
character and two-phase transforms.

The exact family decomposition in `T-106060` therefore yields

\[
\boxed{
\sum_{\chi\ ({\rm mod}\ \ell)}
\|R_{\mathcal B,A;\chi}(X)\|^2
\ll
X^{o(1)}
+
C
\sum_{\mathfrak a\subset(\mathcal B,A)}
\ell D_{\mathfrak a}(X),
}
\tag{L-106073.5}
\]

where \(C\) is an absolute finite-sector constant.  Equation
(L-106073.5) is precisely the conclusion-facing use for which
`CROP106060` was defined.

By `L-106072.6`, the second term is \(X^{o(1)}\).  Combining
(L-106073.3)--(L-106073.5) gives

\[
\boxed{
\|R_{\mathcal B,A}(X)\|^2=X^{o(1)}
}
\tag{L-106073.6}
\]

uniformly on the dyadic horizon, with the same statement after logarithmic
integration.

## 3. Recombination of all blocks

The number of block-colour pieces is \(X^{o(1)}\).  Cauchy in the finite
linear partition gives

\[
\|R_{\rm HBC}(X)\|^2
\le
X^{o(1)}
\sum_{\mathcal B,A}
\|R_{\mathcal B,A}(X)\|^2.
\]

Hence, on every dyadic horizon \([X,2X]\),

\[
\boxed{
\int_X^{2X}|R_{\rm HBC}(t)|^2\frac{dt}{t}
=X^{o(1)}.
}
\tag{L-106073.7}
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

Using (L-106073.7) and summing the \(O(\log Y)\) dyadic horizons proves

\[
\boxed{
\int_2^Y(R_{\rm HBC}(t))_-
\frac{dt}{t}
=Y^{o(1)}.
}
\tag{L-106073.8}
\]

Thus

\[
\boxed{\mathrm{HBCQDSP}_{102888}}
\]

is proved by the scale-matched family construction.

## Exact boundary

```text
linear block/colour source partition          PROVED EXACT
principal recovery on every coloured block    PROVED EXACT
character collision classification            INHERITED PROVED EXACT
equal products                                INHERITED PROVED SUBPOWER
two-phase line contraction                     INHERITED PROVED SHARP
weighted root occupancy                        PROVED SUBPOWER
native HBC logarithmic L2                      PROVED SUBPOWER
HBCQDSP102888 negative mass                    PROVED SUBPOWER
```

The further detector-to-RH composition uses only the already-published parent
implication and is recorded separately in `T-106070` so that reviewers can
audit this new arithmetic closure independently from the older Mellin
consumer.